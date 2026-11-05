"""Bounded R46 regression checks; synthetic rules, not historical findings."""
import unittest
from mqr53_r46_verdicts import (
    Judgment, Question, Rival, Verdict, competing_witnesses,
    example_rivals, recorded_outcome,
)


class R46VerdictTests(unittest.TestCase):
    def setUp(self):
        self.left, self.right = example_rivals()
        self.names = ("feasible", "new_question", "independent_support")

    def test_two_disagreements(self):
        w = competing_witnesses(self.left, self.right, self.names, Question.PURSUIT)
        self.assertEqual(len(w), 2)
        self.assertTrue(all(dict(x.conditions)["feasible"] for x in w))
        self.assertTrue(all(x.left.judgment != x.right.judgment for x in w))

    def test_identical_rivals_never_disagree(self):
        self.assertEqual(competing_witnesses(self.left, self.left, self.names, Question.PURSUIT), ())

    def test_unknown_is_not_disagreement(self):
        other = Rival("unknown", lambda c: Verdict(Question.PURSUIT, Judgment.UNKNOWN))
        self.assertEqual(competing_witnesses(self.left, other, self.names, Question.PURSUIT), ())

    def test_cross_question_comparison_is_invalid(self):
        other = Rival("acceptance", lambda c: Verdict(Question.ACCEPTANCE, Judgment.YES))
        with self.assertRaises(ValueError):
            competing_witnesses(self.left, other, self.names, Question.PURSUIT)

    def test_invalid_axes_are_rejected(self):
        for names in (("x", "x"), (), tuple(map(str, range(17)))):
            with self.assertRaises(ValueError):
                competing_witnesses(self.left, self.right, names, Question.PURSUIT)

    def test_historical_evidence_remains_separate(self):
        v = Verdict(Question.PURSUIT, Judgment.YES)
        self.assertEqual(recorded_outcome(v, None), "historical-evidence-hold")
        self.assertEqual(recorded_outcome(v, True), "evidence-available-for-independent-review")
        self.assertEqual(recorded_outcome(Verdict(Question.PURSUIT, Judgment.UNKNOWN), True), "verdict-underdetermined")


if __name__ == "__main__":
    unittest.main()
