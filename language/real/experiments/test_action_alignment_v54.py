from itertools import permutations
import unittest

from active_observable_v54 import Experiment, ObservationTable
from action_alignment_v54 import equality_pattern, compatible_action_alignments


class AlignmentTests(unittest.TestCase):
    def setUp(self):
        worlds = ("A", "B", "C", "D")
        self.first = ObservationTable(worlds, (
            Experiment("pulse", ("0", "0", "1", "1")),
            Experiment("hold", ("0", "0", "1", "0")),
        ))
        self.second = ObservationTable(worlds, (
            Experiment("native-x", ("small", "small", "large", "small")),
            Experiment("native-y", ("low", "low", "high", "high")),
        ))

    def test_shared_three_cases_leave_both_action_translations_possible(self):
        options = compatible_action_alignments(self.first, self.second, ("A", "B", "C"))
        self.assertEqual(len(options), 2)

    def test_fourth_case_eliminates_one_but_does_not_prove_causation(self):
        self.assertEqual(compatible_action_alignments(self.first, self.second),
                         ((("pulse", "native-y"), ("hold", "native-x")),))

    def test_outcome_renaming_is_not_action_translation(self):
        self.assertEqual(equality_pattern(("red", "red", "green", "blue")), (0, 0, 1, 2))
        self.assertEqual(equality_pattern(("5", "5", "9", "8")), (0, 0, 1, 2))
        self.assertEqual(equality_pattern(("a", "a", "a")), (0, 0, 0))

    def test_no_possible_mapping_is_a_result_not_an_exception(self):
        incompatible = ObservationTable(self.first.worlds, (
            Experiment("native-x", ("0", "1", "0", "1")),
            Experiment("native-y", ("1", "1", "1", "1")),
        ))
        self.assertEqual(compatible_action_alignments(self.first, incompatible), ())

    def test_unaligned_world_cases_and_actions_are_rejected(self):
        with self.assertRaises(ValueError):
            compatible_action_alignments(self.first,
                ObservationTable(tuple(reversed(self.first.worlds)), self.second.experiments))
        with self.assertRaises(ValueError):
            compatible_action_alignments(self.first,
                ObservationTable(self.first.worlds, self.second.experiments[:1]))
        for subset in (("A", "A"), ("unknown",)):
            with self.subTest(subset=subset), self.assertRaises(ValueError):
                compatible_action_alignments(self.first, self.second, subset)

    def test_all_six_renamings_of_a_three_symbol_alphabet(self):
        base = ("p", "q", "r", "q", "p")
        for perm in permutations(("W", "X", "Y")):
            coding = dict(zip(("p", "q", "r"), perm))
            self.assertEqual(equality_pattern(base),
                             equality_pattern(tuple(coding[c] for c in base)))

    def test_empty_probe_set_cannot_select_any_action_mapping(self):
        self.assertEqual(len(compatible_action_alignments(self.first, self.second, ())), 2)


if __name__ == "__main__":
    unittest.main()
