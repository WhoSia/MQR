"""Check which interventions distinguish one operation from its two-stage implementation."""

from itertools import product
import unittest

from action_words_v54 import compile_words
from protocol_frontier_v54 import Machine, ResultKind, compare


# Plant output, internal latch, and an independently copied latch reading.
STATES = tuple(product((0, 1), repeat=3))
OBSERVATIONS = tuple(f"{output}/{reading}" for output, _, reading in STATES)


def edge(update):
    return tuple(STATES.index(update(*state)) for state in STATES)


INSPECT = edge(lambda output, latch, reading: (output, latch, latch))
CLEAR = edge(lambda output, latch, reading: (output, 0, reading))
ATOMIC = Machine(OBSERVATIONS, {
    "begin": edge(lambda output, latch, reading: (output, latch, reading)),
    "finish": edge(lambda output, latch, reading: (1 - output, 0, reading)),
    "inspect": INSPECT,
    "clear": CLEAR,
})
STAGED = Machine(OBSERVATIONS, {
    "arm": edge(lambda output, latch, reading: (output, 1, reading)),
    "commit": edge(lambda output, latch, reading: (output ^ latch, 0, reading)),
    "inspect": INSPECT,
    "clear": CLEAR,
})
STAGED_TIMED = Machine(OBSERVATIONS, {
    "begin": STAGED.transitions["arm"],
    "finish": STAGED.transitions["commit"],
    "inspect": INSPECT,
    "clear": CLEAR,
})
BOUNDARIES = ({"begin": 1, "inspect": 0, "clear": 0}, {"finish": 0})
COSTS = {"begin": 1, "finish": 1, "inspect": 1, "clear": 1}


class ActionWordTests(unittest.TestCase):
    def test_composition_agrees_on_full_state_and_all_boundary_contexts(self):
        controls = {"inspect": ("inspect",), "clear": ("clear",)}
        left = compile_words(ATOMIC, {"apply": ("finish",), **controls})
        right = compile_words(STAGED, {"apply": ("arm", "commit"), **controls})
        self.assertEqual(left.transitions, right.transitions)
        result = compare(left, right, ({action: 0 for action in left.transitions},),
                         {"apply": 2, "clear": 1, "inspect": 1})
        self.assertEqual(result.kind, ResultKind.EQUIVALENT_UNDER_PROTOCOL)

    def test_two_matched_clock_steps_without_middle_access_agree(self):
        result = compare(ATOMIC, STAGED_TIMED, BOUNDARIES, COSTS)
        self.assertEqual(result.kind, ResultKind.EQUIVALENT_UNDER_PROTOCOL)

    def test_middle_inspection_gives_first_difference_without_writing_to_plant(self):
        protocol = (BOUNDARIES[0], {"inspect": 2, "finish": 0}, {"finish": 0})
        result = compare(ATOMIC, STAGED_TIMED, protocol, COSTS)
        self.assertEqual(result.kind, ResultKind.DISTINGUISHABLE)
        self.assertEqual(result.witness.actions, ("begin", "inspect"))
        self.assertEqual(result.witness.cost, 2)
        self.assertEqual((result.witness.left_trace[-1], result.witness.right_trace[-1]),
                         ("0/0", "0/1"))
        word = ("begin", "inspect", "finish")
        self.assertEqual((ATOMIC.trace(word)[-1], STAGED_TIMED.trace(word)[-1]), ("1/0", "1/1"))

    def test_middle_clear_changes_final_output_with_no_middle_readout(self):
        protocol = (BOUNDARIES[0], {"clear": 2, "finish": 0}, {"finish": 0})
        result = compare(ATOMIC, STAGED_TIMED, protocol, COSTS)
        self.assertEqual(result.kind, ResultKind.DISTINGUISHABLE)
        self.assertEqual(result.witness.actions, ("begin", "clear", "finish"))
        self.assertEqual((result.witness.left_trace[-1], result.witness.right_trace[-1]),
                         ("1/0", "0/0"))
        low_budget = compare(ATOMIC, STAGED_TIMED, protocol, COSTS, budget=2)
        self.assertEqual(low_budget.kind, ResultKind.BEYOND_BUDGET)
        self.assertEqual(low_budget.witness, result.witness)

    def test_word_compilation_keeps_initial_state_and_rejects_bad_specs(self):
        machine = Machine(ATOMIC.observations, ATOMIC.transitions, initial=3)
        self.assertEqual(compile_words(machine, {"apply": ("finish",)}).initial, 3)
        for word in ((), ("missing",)):
            with self.subTest(word=word), self.assertRaises(ValueError):
                compile_words(machine, {"apply": word})
