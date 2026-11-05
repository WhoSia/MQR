import unittest
from mqr53_r46_e_comparability import (
    Question, Status, HistoricalJudgment, comparable, grounded_conflict,
    later_uptake_cannot_decide_pursuit,
)


def case(question=Question.PURSUIT, status=Status.SUPPORTED,
         domain='mathematics', year=1921, source='contemporaneous', name='brouwer'):
    return HistoricalJudgment(name, domain, question, status, year, source)


class ComparisonGateTests(unittest.TestCase):
    def test_matching_opposed_judgments_can_conflict(self):
        self.assertTrue(grounded_conflict(case(), case(status=Status.REJECTED)))

    def test_unknown_is_not_conflict(self):
        self.assertFalse(grounded_conflict(case(), case(status=Status.UNDETERMINED)))

    def test_question_mismatch(self):
        self.assertFalse(comparable(case(), case(question=Question.UPTAKE)))

    def test_different_historical_cutoffs(self):
        self.assertFalse(comparable(case(), case(year=1930)))

    def test_cross_domain_does_not_imply_same_verdict(self):
        self.assertFalse(comparable(case(), case(domain='biochemistry')))

    def test_secondary_only_does_not_establish_historical_actor_conflict(self):
        self.assertFalse(grounded_conflict(
            case(source='historiography'),
            case(status=Status.REJECTED, source='later_translation')))

    def test_uptake_is_not_pursuit(self):
        self.assertTrue(later_uptake_cannot_decide_pursuit(case(question=Question.UPTAKE)))
        with self.assertRaises(ValueError):
            later_uptake_cannot_decide_pursuit(case())


if __name__ == '__main__':
    unittest.main()
