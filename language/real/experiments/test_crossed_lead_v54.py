from fractions import Fraction
import unittest

from crossed_lead_v54 import LeadPair, held_out_gap_residual


class CrossedLeadTests(unittest.TestCase):
    def test_quadratic_differential_survives_arbitrary_common_effect(self):
        first = LeadPair(1000, Fraction(8), Fraction(11))
        second = LeadPair(1500, Fraction(-5), Fraction(1, 2))
        held_out = LeadPair(2000, Fraction(22), Fraction(31))
        self.assertEqual(held_out_gap_residual(first, second, held_out), 0)
        shifted = LeadPair(2000, held_out.short + 6, held_out.long + 6)
        self.assertEqual(held_out_gap_residual(first, second, shifted), 0)

    def test_extra_heldout_loading_is_detectable_but_not_attributable(self):
        first = LeadPair(1000, Fraction(0), Fraction(3))
        second = LeadPair(1500, Fraction(0), Fraction(11, 2))
        extra_long = LeadPair(2000, Fraction(0), Fraction(10))
        extra_short = LeadPair(2000, Fraction(-1), Fraction(9))
        self.assertEqual(held_out_gap_residual(first, second, extra_long), 1)
        self.assertEqual(held_out_gap_residual(first, second, extra_short), 1)

    def test_sign_and_frequency_validation(self):
        first = LeadPair(1000, Fraction(0), Fraction(3))
        second = LeadPair(1500, Fraction(0), Fraction(11, 2))
        low_residual = LeadPair(2000, Fraction(1), Fraction(9))
        self.assertEqual(held_out_gap_residual(second, first, low_residual), -1)
        for frequency in (0, -2000, 1000, 1500):
            with self.subTest(frequency=frequency), self.assertRaises(ValueError):
                held_out_gap_residual(first, second, LeadPair(frequency, Fraction(0), Fraction(0)))
