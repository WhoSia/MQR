"""Tests for MQR-5.3 R33 2x2 crossed measurement decomposition."""
import unittest
from mqr53_r33_crossed_measurement import (
    CrossedMeasurement, contrasts, gauge_shift, reference_adjusted_measurand
)


class CrossedMeasurementTests(unittest.TestCase):
    def setUp(self):
        self.model = CrossedMeasurement(
            measurand=10.0, global_bias=2.0,
            preparation_bias=(-1.0, 1.0),
            detector_bias=(-0.5, 0.5)
        )

    def test_expected_matrix_and_contrasts(self):
        self.assertEqual(self.model.expected_readings(),
                         ((10.5, 11.5), (12.5, 13.5)))
        c = contrasts(self.model.expected_readings())
        self.assertEqual(c.mean, 12)
        self.assertEqual(c.preparation_difference, -2)
        self.assertEqual(c.detector_difference, -1)
        self.assertEqual(c.interaction_difference, 0)

    def test_gauge_counterexample(self):
        other = gauge_shift(self.model, 1.0)
        self.assertEqual(other.measurand, 11)
        self.assertEqual(other.global_bias, 1)
        self.assertEqual(other.expected_readings(),
                         self.model.expected_readings())

    def test_interaction_diagnostic_only(self):
        model = CrossedMeasurement(
            measurand=10, global_bias=2,
            preparation_bias=(-1, 1),
            detector_bias=(-0.5, 0.5), interaction=0.4
        )
        self.assertAlmostEqual(
            contrasts(model.expected_readings()).interaction_difference, 1.6
        )
        self.assertAlmostEqual(
            contrasts(model.expected_readings()).mean, 12.0
        )

    def test_reference_requires_extra_assumption(self):
        self.assertEqual(reference_adjusted_measurand(12, 2), 10)
        # Without a known global bias, theta=10 and theta=11 both fit.
        self.assertNotEqual(self.model.measurand,
                            gauge_shift(self.model, 1).measurand)


if __name__ == "__main__":
    unittest.main()
