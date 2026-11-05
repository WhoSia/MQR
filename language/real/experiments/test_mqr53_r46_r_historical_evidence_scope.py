"""R46-R: no false same-question contradiction or time leakage."""
import unittest
from mqr53_r46_r_historical_evidence_scope import (
    HistoricalClaim, Target, TOBACCO_FRACTION_1956, TOBACCO_TMV_1956,
    SPINACH_1964, same_inferential_question, actual_opposition,
    accessible_by_year,
)


class HistoricalEvidenceScopeTests(unittest.TestCase):
    def test_tobacco_signal_is_not_virus_product(self):
        self.assertFalse(same_inferential_question(TOBACCO_FRACTION_1956, TOBACCO_TMV_1956))
        self.assertFalse(actual_opposition(TOBACCO_FRACTION_1956, TOBACCO_TMV_1956))

    def test_tobacco_and_spinach_are_not_same_preparation(self):
        self.assertFalse(same_inferential_question(TOBACCO_FRACTION_1956, SPINACH_1964))

    def test_a_negative_and_positive_same_question_can_disagree(self):
        positive = HistoricalClaim("A", "tobacco", "p", Target.VIRUS_PRODUCT, 1956, True, "observed")
        negative = HistoricalClaim("B", "tobacco", "p", Target.VIRUS_PRODUCT, 1956, True, "not_observed")
        self.assertTrue(actual_opposition(positive, negative))

    def test_tentative_does_not_imply_opposition(self):
        tentative = HistoricalClaim("A", "tobacco", "p", Target.PEPTIDE_BOND, 1954, True, "tentative")
        negative = HistoricalClaim("B", "tobacco", "p", Target.PEPTIDE_BOND, 1954, True, "not_observed")
        self.assertFalse(actual_opposition(tentative, negative))

    def test_no_future_source_in_1954_knowledge(self):
        self.assertFalse(accessible_by_year(TOBACCO_TMV_1956, 1954))
        self.assertFalse(accessible_by_year(SPINACH_1964, 1956))

    def test_publication_year_alone_is_not_proof_of_access(self):
        unpublished = HistoricalClaim("received manuscript", "rat", "homogenate",
                                      Target.FRACTION_LABEL, 1954, False, "observed")
        self.assertFalse(accessible_by_year(unpublished, 1954))
        self.assertFalse(accessible_by_year(unpublished, 1960))

    def test_publicly_available_in_time_is_only_eligibility(self):
        self.assertTrue(accessible_by_year(TOBACCO_TMV_1956, 1956))


if __name__ == "__main__":
    unittest.main()
