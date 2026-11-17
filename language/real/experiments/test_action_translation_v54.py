"""Exercise singleton collisions, composition witnesses, and protocol ambiguity."""

from itertools import product
import unittest

from action_translation_v54 import assess, common_protocol
from protocol_frontier_v54 import Machine, ResultKind


# States represent horizontal, vertical and extinguished transmitted beams.
LEFT = Machine(("1", "1", "0"), {"a": (1, 0, 2), "b": (0, 2, 2)})
RIGHT = Machine(("1", "1", "0"), {"x": (1, 0, 2), "y": (0, 2, 2)})
LEFT_OPEN = ({"a": 0, "b": 0},)
RIGHT_OPEN = ({"x": 0, "y": 0},)
COSTS = {"a": 1, "b": 1}
STRAIGHT = (("a", "x"), ("b", "y"))
SWAPPED = (("a", "y"), ("b", "x"))


class ActionTranslationTests(unittest.TestCase):
    def test_individual_matches_hide_two_dictionaries(self):
        results = assess(LEFT, RIGHT, LEFT_OPEN, RIGHT_OPEN, COSTS)
        self.assertEqual([r.dictionary for r in results], [STRAIGHT, SWAPPED])
        self.assertEqual(results[0].comparison.kind, ResultKind.EQUIVALENT_UNDER_PROTOCOL)
        w = results[1].comparison.witness
        self.assertEqual(results[1].comparison.kind, ResultKind.DISTINGUISHABLE)
        self.assertEqual(w.actions, ("a", "b"))
        self.assertEqual((w.left_trace, w.right_trace), (("1", "1", "0"), ("1", "1", "1")))

    def test_optical_state_trace_against_exact_jones_vectors(self):
        matrices = {"a": ((0, -1), (1, 0)), "b": ((1, 0), (0, 0))}
        for length in range(8):
            for word in product("ab", repeat=length):
                x, y = 1, 0
                trace = ["1"]
                for action in word:
                    (a, b), (c, d) = matrices[action]
                    x, y = a*x + b*y, c*x + d*y
                    trace.append(str(x*x + y*y))
                self.assertEqual(LEFT.trace(word), tuple(trace))

    def test_budget_applies_to_refutation(self):
        results = assess(LEFT, RIGHT, LEFT_OPEN, RIGHT_OPEN, COSTS, budget=1)
        self.assertEqual(results[1].comparison.kind, ResultKind.BEYOND_BUDGET)
        self.assertEqual(results[1].comparison.witness.cost, 2)

    def test_native_protocol_intersection_can_hide_both_followups(self):
        right = ({"x": 1, "y": 2}, {"y": 0}, {})
        results = assess(LEFT, RIGHT, LEFT_OPEN, right, COSTS)
        self.assertEqual(len(results), 2)
        self.assertTrue(all(
            r.comparison.kind == ResultKind.EQUIVALENT_UNDER_PROTOCOL for r in results
        ))
        both = common_protocol(LEFT_OPEN, right, (STRAIGHT, SWAPPED))
        known = common_protocol(LEFT_OPEN, right, (STRAIGHT,))
        self.assertEqual(both[0], {"a": 1, "b": 2})
        self.assertEqual((both[1], both[2]), ({}, {}))
        self.assertEqual(known[1], {"b": 0})

    def test_true_symmetry_persists_under_arbitrarily_long_words(self):
        left = Machine(("0", "1"), {"a": (1, 0), "b": (1, 0)})
        right = Machine(("0", "1"), {"x": (1, 0), "y": (1, 0)})
        results = assess(left, right, LEFT_OPEN, RIGHT_OPEN, COSTS)
        self.assertEqual(len(results), 2)
        for result in results:
            self.assertEqual(result.comparison.kind, ResultKind.EQUIVALENT_UNDER_PROTOCOL)

    def test_initial_or_single_action_conflict(self):
        wrong_initial = Machine(("9", "1", "0"), RIGHT.transitions)
        wrong_single = Machine(RIGHT.observations, {"x": (2, 0, 2), "y": (2, 2, 2)})
        for wrong in (wrong_initial, wrong_single):
            self.assertEqual(assess(LEFT, wrong, LEFT_OPEN, RIGHT_OPEN, COSTS), ())

    def test_invalid_protocol_budget_and_alphabet(self):
        with self.assertRaises(ValueError):
            assess(LEFT, RIGHT, LEFT_OPEN, ({"x": 1},), COSTS)
        with self.assertRaises(ValueError):
            assess(LEFT, RIGHT, LEFT_OPEN, RIGHT_OPEN, COSTS, budget=-1)
        with self.assertRaises(ValueError):
            assess(LEFT, RIGHT, LEFT_OPEN, RIGHT_OPEN, {"a": 1})
        with self.assertRaises(ValueError):
            assess(LEFT, Machine(("0",), {}), LEFT_OPEN, ({},), COSTS)

    def test_independent_word_oracle_for_common_protocol(self):
        def execute(protocol, word):
            state = 0
            for action in word:
                if action not in protocol[state]:
                    return False
                state = protocol[state][action]
            return True

        right = ({"x": 1, "y": 2}, {"y": 0, "x": 2}, {"x": 0, "y": 1})
        for dictionaries in ((STRAIGHT,), (SWAPPED,), (STRAIGHT, SWAPPED)):
            common = common_protocol(LEFT_OPEN, right, dictionaries)
            maps = tuple(dict(d) for d in dictionaries)
            for length in range(7):
                for word in product("ab", repeat=length):
                    expected = all(execute(right, tuple(m[a] for a in word)) for m in maps)
                    self.assertEqual(execute(common, word), expected)


if __name__ == "__main__":
    unittest.main()
