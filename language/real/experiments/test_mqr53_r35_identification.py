import unittest
from mqr53_r35_identification import ChannelChanges, equivalent_witnesses, observed_with_offset_drift, sign_of_relative_change

class IdentificationTests(unittest.TestCase):
    def test_equivalence_family(self):
        a, b = equivalent_witnesses(1.7, 4.25)
        self.assertNotEqual(a, b)
        self.assertAlmostEqual(a.observed_contrast(), b.observed_contrast())

    def test_vapor_only_matches_liquid_only(self):
        self.assertAlmostEqual(ChannelChanges(0.8, 0).observed_contrast(1.25),
                               ChannelChanges(0, -0.8).observed_contrast(1.25))

    def test_common_movement_undetected(self):
        self.assertAlmostEqual(ChannelChanges(5.0, 5.0).observed_contrast(), 0.0)

    def test_gain_sign(self):
        for gain in (0.1, 1.0, 100.0):
            self.assertEqual(sign_of_relative_change(ChannelChanges(3.0, 1.0).observed_contrast(gain)), 1)

    def test_drift_mimics_physical_change(self):
        physical = observed_with_offset_drift(ChannelChanges(1.0, 0.0), 1.0, 0, 0)
        artifact = observed_with_offset_drift(ChannelChanges(0.0, 0.0), 1.0, 1.0, 0)
        self.assertEqual(physical, artifact)

    def test_invalid_gain(self):
        with self.assertRaises(ValueError):
            ChannelChanges(1, 0).observed_contrast(0)

if __name__ == "__main__":
    unittest.main()
