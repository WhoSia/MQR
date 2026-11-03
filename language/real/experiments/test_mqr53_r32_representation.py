"""Regression tests: MQR-5.3 R32 synthetic identification counterexamples."""
import unittest
from mqr53_r32_representation import (
    best_affine_parity_accuracy, binary_entropy,
    new_sensor_mutual_information, independent_sensor_disagreement,
    infer_independent_error_rate, shared_error_disagreement,
    fair_latent_observable_joint,
)


class RepresentationAndCalibrationTests(unittest.TestCase):
    def test_xor_affine_restriction(self):
        self.assertEqual(best_affine_parity_accuracy(), 0.75)
        self.assertEqual(best_affine_parity_accuracy(enriched=True), 1.0)

    def test_information_distinction(self):
        self.assertAlmostEqual(new_sensor_mutual_information(0.1),
                               0.5310044064107188)
        self.assertEqual(new_sensor_mutual_information(0.5), 0.0)
        self.assertEqual(new_sensor_mutual_information(0.0), 1.0)
        self.assertAlmostEqual(binary_entropy(0.1), 0.4689955935892812)

    def test_independent_error_inversion(self):
        d = independent_sensor_disagreement(0.1)
        self.assertAlmostEqual(d, 0.18)
        self.assertAlmostEqual(infer_independent_error_rate(d), 0.1)
        for p in (0.0, 0.02, 0.25, 0.49, 0.5):
            self.assertAlmostEqual(
                infer_independent_error_rate(
                    independent_sensor_disagreement(p)), p)

    def test_shared_error_counterexample(self):
        self.assertEqual(shared_error_disagreement(0.1), 0.0)
        self.assertEqual(infer_independent_error_rate(0.0), 0.0)
        self.assertEqual(fair_latent_observable_joint(shared_error_rate=0.1),
                         fair_latent_observable_joint(shared_error_rate=0.0))

    def test_input_validation(self):
        for fn in (binary_entropy, shared_error_disagreement,
                   independent_sensor_disagreement):
            with self.assertRaises(ValueError):
                fn(-0.01)
        with self.assertRaises(ValueError):
            infer_independent_error_rate(0.51)
        with self.assertRaises(ValueError):
            new_sensor_mutual_information(0.51)


if __name__ == "__main__":
    unittest.main()
