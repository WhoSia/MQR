"""Check calibration boundaries with rational readouts and finite grid replay."""

from fractions import Fraction as F
from itertools import combinations, product
import unittest

from readout_alignment_v54 import Reading, compatible


def exact(x, y):
    return Reading(x, y, y)


def readings(predicted, reported):
    return tuple(exact(x, y) for x, y in zip(predicted, reported, strict=True))


class ReadoutAlignmentTests(unittest.TestCase):
    def test_drop_rejects_constant_translation_even_without_calibration(self):
        for strict in (False, True):
            self.assertTrue(compatible(readings((1, 1, 0), (1, 1, 0)), strict=strict))
            self.assertFalse(compatible(readings((1, 1, 1), (1, 1, 0)), strict=strict))

    def test_flat_trace_can_hide_a_drop_if_detector_saturates(self):
        drop = readings((1, 1, 0), (1, 1, 1))
        constant = readings((1, 1, 1), (1, 1, 1))
        self.assertTrue(compatible(drop, strict=False))
        self.assertFalse(compatible(drop, strict=True))
        self.assertTrue(compatible(constant, strict=True))
        endpoints = (exact(0, 0), exact(1, 1))
        self.assertFalse(compatible(drop + endpoints, strict=False))
        self.assertTrue(compatible(constant + endpoints, strict=False))

    def test_interior_anchor_can_refute_both_or_select_one(self):
        endpoints = (exact(0, 0), exact(1, 1))
        middle = exact(F(1, 2), F(1, 2))
        for intensity in (F(1, 4), F(3, 4)):
            point = exact(intensity, F(1, 2))
            self.assertTrue(compatible(endpoints + (point,), strict=True))
            self.assertFalse(compatible(endpoints + (point, middle), strict=True))
            self.assertTrue(compatible(endpoints + (point, middle), strict=False))
        self.assertTrue(compatible(endpoints + (middle, exact(F(1, 4), F(1, 3))), strict=True))
        self.assertFalse(compatible(endpoints + (middle, exact(F(3, 4), F(1, 3))), strict=True))

    def test_repeated_intensity_merges_intervals(self):
        self.assertTrue(compatible((Reading(0, 0, 1), Reading(0, 1, 2)), strict=True))
        self.assertFalse(compatible((Reading(0, 0, 1), Reading(0, 2, 3)), strict=False))

    def test_distinct_intensities_and_attained_equality(self):
        constraints = (Reading(0, 1, 2), Reading(1, 0, 1))
        self.assertTrue(compatible(constraints, strict=False))
        self.assertFalse(compatible(constraints, strict=True))

    def test_empty_and_invalid_intervals(self):
        self.assertTrue(compatible((), strict=True))
        with self.assertRaises(ValueError):
            Reading(0, 2, 1)

    def test_against_finite_grid_oracle(self):
        grid = tuple(F(i, 3) for i in range(7))
        intervals = [(a, b) for a in range(3) for b in range(a, 3)]
        weak = [v for v in product(grid, repeat=3) if v[0] <= v[1] <= v[2]]
        strict = list(combinations(grid, 3))
        for limits in product(intervals, repeat=3):
            constraints = tuple(Reading(x, a, b) for x, (a, b) in enumerate(limits))
            for mode, sequences in [(False, weak), (True, strict)]:
                expected = any(all(a <= val <= b for val, (a, b) in zip(values, limits))
                               for values in sequences)
                self.assertEqual(compatible(constraints, strict=mode), expected)


if __name__ == "__main__":
    unittest.main()
