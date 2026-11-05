"""Tests for observational-contrast helpers."""
import unittest
from mqr53_r46_d_contrast_audit import DATA, comparison, interaction


class TestObservedContrasts(unittest.TestCase):
    def test_one_axis(self):
        value, axes = comparison(DATA[0], DATA[1])
        self.assertEqual(value, 56.0)
        self.assertEqual(axes, ("supplement",))

    def test_bundled_regime(self):
        value, axes = comparison(DATA[1], DATA[4])
        self.assertEqual(value, -43.0)
        self.assertEqual(axes, ("regime",))

    def test_interaction(self):
        self.assertEqual(interaction(), -44.0)

    def test_no_self_contrast(self):
        with self.assertRaises(ValueError):
            comparison(DATA[0], DATA[0])


if __name__ == "__main__":
    unittest.main()
