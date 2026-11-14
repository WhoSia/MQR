"""Exact tests for admissible, weighted experiment traces."""

import itertools
import unittest

from protocol_frontier_v54 import Machine, ResultKind, compare


LEFT = Machine(("0", "0", "1"), {
    "prepare": (1, 1, 2), "read": (0, 2, 2), "reset": (0, 0, 0),
    "direct": (2, 2, 2),
})
RIGHT = Machine(("0", "0", "1"), {
    "prepare": (1, 1, 2), "read": (0, 1, 2), "reset": (0, 0, 0),
    "direct": (0, 1, 2),
})
COSTS = {"prepare": 1, "read": 1, "reset": 1, "direct": 5}
ORDINARY = ({"prepare": 0, "read": 0, "reset": 0},)
RESET_ONLY = ({"prepare": 1, "read": 1, "reset": 0}, {"reset": 0})
WITH_DIRECT = ({"prepare": 0, "read": 0, "reset": 0, "direct": 0},)


class ProtocolFrontierTests(unittest.TestCase):
    def test_individual_actions_agree_and_order_matters(self):
        for action in ORDINARY[0]:
            self.assertEqual(LEFT.trace((action,)), RIGHT.trace((action,)))
        self.assertEqual(LEFT.trace(("read", "prepare")), RIGHT.trace(("read", "prepare")))
        result = compare(LEFT, RIGHT, ORDINARY, COSTS)
        self.assertEqual(result.kind, ResultKind.DISTINGUISHABLE)
        self.assertEqual(result.witness.actions, ("prepare", "read"))
        self.assertEqual(result.witness.left_trace, ("0", "0", "1"))
        self.assertEqual(result.witness.right_trace, ("0", "0", "0"))

    def test_protocol_can_remove_the_distinction_without_removing_any_action(self):
        result = compare(LEFT, RIGHT, RESET_ONLY, COSTS)
        self.assertEqual(result.kind, ResultKind.EQUIVALENT_UNDER_PROTOCOL)
        self.assertIsNone(result.witness)
        self.assertEqual(result.settled_states, 3)

    def test_budget_and_shortest_length_are_different(self):
        affordable = compare(LEFT, RIGHT, WITH_DIRECT, COSTS, budget=2)
        unaffordable = compare(LEFT, RIGHT, WITH_DIRECT, COSTS, budget=1)
        shortest = compare(LEFT, RIGHT, WITH_DIRECT, dict.fromkeys(COSTS, 1))
        self.assertEqual(affordable.kind, ResultKind.DISTINGUISHABLE)
        self.assertEqual(unaffordable.kind, ResultKind.BEYOND_BUDGET)
        self.assertEqual(affordable.witness, unaffordable.witness)
        self.assertEqual(affordable.witness.cost, 2)
        self.assertEqual(shortest.witness.actions, ("direct",))

    def test_initial_observation_is_a_zero_cost_witness(self):
        other = Machine(("1",), {})
        result = compare(LEFT, other, ({},), {}, budget=0)
        self.assertEqual(result.kind, ResultKind.DISTINGUISHABLE)
        self.assertEqual((result.witness.actions, result.witness.cost), ((), 0))

    def test_same_protocol_and_outputs_are_equivalent_after_state_renaming(self):
        renamed = Machine(("1", "0", "0"), {
            "prepare": (0, 2, 2), "read": (0, 1, 0), "reset": (1, 1, 1),
            "direct": (0, 0, 0),
        }, initial=1)
        self.assertEqual(
            compare(LEFT, renamed, WITH_DIRECT, COSTS).kind,
            ResultKind.EQUIVALENT_UNDER_PROTOCOL,
        )

    def test_invalid_contracts_fail_before_search(self):
        for protocol, costs in [
            ((), COSTS), (({"read": 1},), COSTS), (({"missing": 0},), COSTS),
            (ORDINARY, {"prepare": 1, "read": 0, "reset": 1}), (ORDINARY, {}),
        ]:
            with self.subTest(protocol=protocol, costs=costs), self.assertRaises(ValueError):
                compare(LEFT, RIGHT, protocol, costs)
        with self.assertRaises(ValueError):
            compare(LEFT, RIGHT, ORDINARY, COSTS, budget=-1)
        with self.assertRaises(ValueError):
            Machine(("0",), {"read": (1,)})

    def test_one_step_agreement_has_no_uniform_horizon_as_state_space_grows(self):
        protocol = ({"prepare": 0, "read": 0},)
        for count in (1, 2, 5, 16, 64):
            observations = ("0",) * (count + 1) + ("1",)
            prepare = tuple(min(i + 1, count) for i in range(count + 1)) + (count + 1,)
            left_read = tuple(range(count)) + (count + 1, count + 1)
            right_read = tuple(range(count + 2))
            left = Machine(observations, {"prepare": prepare, "read": left_read})
            right = Machine(observations, {"prepare": prepare, "read": right_read})
            result = compare(left, right, protocol, COSTS, budget=count)
            self.assertEqual(result.kind, ResultKind.BEYOND_BUDGET)
            self.assertEqual(result.witness.actions, ("prepare",) * count + ("read",))
            self.assertEqual(result.witness.cost, count + 1)

    def test_exhaustive_independent_small_word_oracle(self):
        rows = list(itertools.product(range(2), repeat=2))
        machines = [
            Machine(("0", last), {"a": a, "b": b})
            for a, b, last in itertools.product(rows, rows, ("0", "1"))
        ]
        costs = {"a": 1, "b": 3}
        words = [
            (sum(costs[a] for a in word), word)
            for length in range(4)
            for word in itertools.product(costs, repeat=length)
        ]
        for left, right in itertools.product(machines, repeat=2):
            # A shortest witness is simple in the four-state product.
            expected = min(
                (cost for cost, word in words if left.trace(word) != right.trace(word)),
                default=None,
            )
            result = compare(left, right, ({"a": 0, "b": 0},), costs)
            actual = None if result.witness is None else result.witness.cost
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
