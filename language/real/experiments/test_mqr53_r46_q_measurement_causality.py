"""R46-Q: checks for a deliberately synthetic observationally equivalent pair."""
import unittest
from mqr53_r46_q_measurement_causality import (
    attribute_causes_scores, common_cause_only,
    law, observationally_equivalent, separated_by_setting_x,
)


class MeasurementCausalityTests(unittest.TestCase):
    def test_observational_distribution_identical(self):
        self.assertTrue(observationally_equivalent())
        self.assertEqual(law(attribute_causes_scores), {(0, 0, 0): 0.5, (1, 1, 1): 0.5})
        self.assertEqual(law(attribute_causes_scores), law(common_cause_only))

    def test_intervene_zero(self):
        self.assertTrue(separated_by_setting_x(0))
        self.assertEqual(law(attribute_causes_scores, 0), {(0, 0, 0): 1.0})
        self.assertEqual(law(common_cause_only, 0), {(0, 0, 0): 0.5, (0, 1, 1): 0.5})

    def test_intervene_one(self):
        self.assertTrue(separated_by_setting_x(1))
        self.assertEqual(law(attribute_causes_scores, 1), {(1, 1, 1): 1.0})

    def test_invalid_interventions_rejected(self):
        for invalid in (-1, 2):
            with self.assertRaises(ValueError):
                law(attribute_causes_scores, invalid)
            with self.assertRaises(ValueError):
                separated_by_setting_x(invalid)


if __name__ == '__main__':
    unittest.main()
