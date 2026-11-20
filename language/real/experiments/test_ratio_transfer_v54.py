from fractions import Fraction
from itertools import product
import unittest

from ratio_transfer_v54 import LinearRatio, first_ratio_disagreement


class RatioTransferTests(unittest.TestCase):
    def test_equal_basis_ratios_can_fail_on_a_mixture(self):
        reference = LinearRatio((1, 0), (1, 1))
        candidate = LinearRatio((2, 0), (2, 1))
        self.assertEqual(first_ratio_disagreement(reference, candidate), (0, 1))
        self.assertEqual(reference.probe((0, 1)), Fraction(1, 2))
        self.assertEqual(candidate.probe((0, 1)), Fraction(2, 3))

    def test_agreement_can_survive_a_nonproportional_calibration(self):
        reference = LinearRatio((1, 3), (1, 3))
        candidate = LinearRatio((2, 1), (2, 1))
        self.assertIsNone(first_ratio_disagreement(reference, candidate))

    def test_reports_the_first_single_probe_before_mixtures(self):
        reference = LinearRatio((1, 0, 2), (1, 1, 1))
        candidate = LinearRatio((1, 0, 1), (1, 1, 1))
        self.assertEqual(first_ratio_disagreement(reference, candidate), (2,))

    def test_check_matches_exact_enumeration_on_a_bounded_grid(self):
        ratios = [
            LinearRatio(numerator, denominator)
            for numerator in product(range(3), repeat=2)
            for denominator in product(range(1, 3), repeat=2)
        ]
        mixtures = [(a, b) for a, b in product(range(4), repeat=2) if a or b]

        def response(ratio, weights):
            a, b = weights
            return Fraction(
                a * ratio.numerator[0] + b * ratio.numerator[1],
                a * ratio.denominator[0] + b * ratio.denominator[1],
            )

        for reference, candidate in product(ratios, repeat=2):
            expected = all(response(reference, x) == response(candidate, x) for x in mixtures)
            self.assertEqual(first_ratio_disagreement(reference, candidate) is None, expected)

    def test_undefined_basis_ratios_and_incompatible_dimensions_are_rejected(self):
        for numerator, denominator in (((), ()), ((1,), (0,)), ((1,), (1, 2))):
            with self.subTest(numerator=numerator, denominator=denominator):
                with self.assertRaises(ValueError):
                    LinearRatio(numerator, denominator)
        with self.assertRaises(ValueError):
            first_ratio_disagreement(LinearRatio((1,), (2,)), LinearRatio((1, 0), (1, 1)))
