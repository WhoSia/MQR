"""Proof-control tests of source-independent textbook Lorentz algebra."""
import unittest
from fractions import Fraction as F
from spacetime_invariant_v54 import (
    all_verified_examples, galilean, interval_sq, lorentz,
    separation_type, validate_boost,
)


class ExactSpacetimeTests(unittest.TestCase):
    def test_relativity_of_simultaneity_exact(self):
        self.assertEqual(lorentz(0, 1, F(3, 5), F(5, 4)),
                         (F(-3, 4), F(5, 4)))

    def test_galilean_preserves_simultaneity(self):
        for velocity in (F(3, 5), F(-3, 5), F(4, 5)):
            self.assertEqual(galilean(0, 1, velocity)[0], 0)

    def test_signed_spacelike_order_changes(self):
        self.assertEqual(lorentz(0, 1, F(-3, 5), F(5, 4))[0], F(3, 4))
        self.assertEqual(lorentz(0, 1, F(3, 5), F(5, 4))[0], F(-3, 4))

    def test_spacelike_pair_can_be_simultaneous(self):
        self.assertEqual(lorentz(3, 5, F(3, 5), F(5, 4))[0], 0)

    def test_timelike_pair_rest_frame(self):
        self.assertEqual(lorentz(5, 3, F(3, 5), F(5, 4)), (4, 0))

    def test_future_timelike_order_cannot_reverse(self):
        for v, g in ((F(3, 5), F(5, 4)), (F(-3, 5), F(5, 4)),
                     (F(4, 5), F(5, 3)), (F(5, 13), F(13, 12))):
            self.assertGreater(lorentz(5, 3, v, g)[0], 0)

    def test_null_direction_remains_null(self):
        for v, g in ((F(3, 5), F(5, 4)), (F(-3, 5), F(5, 4))):
            self.assertEqual(interval_sq(*lorentz(1, 1, v, g)), 0)

    def test_exhaustive_fixture_identity(self):
        cases = list(all_verified_examples())
        self.assertEqual(len(cases), 20)
        self.assertEqual([c['causal_class'] for c in cases[:5]],
                         ['spacelike', 'spacelike', 'timelike', 'null', 'timelike'])

    def test_reject_bad_gamma_or_light_speed_boost(self):
        for v, g in ((F(3, 5), 1), (1, 1), (F(3, 5), -F(5, 4))):
            with self.assertRaises(ValueError):
                validate_boost(v, g)

    def test_reject_float_coordinates(self):
        with self.assertRaises(TypeError):
            lorentz(0.0, 1, F(3, 5), F(5, 4))


if __name__ == '__main__':
    unittest.main()
