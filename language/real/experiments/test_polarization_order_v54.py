"""Validate time balancing and the two-preparation optical sign reversal."""

from fractions import Fraction as F
from itertools import combinations, product
from math import cos, pi, sin, sqrt
import unittest

from polarization_order_v54 import (
    LINEAR_BLOCK, QUADRATIC_BLOCK, contrast, moment_imbalance, optical_difference,
)


class PolarizationOrderTests(unittest.TestCase):
    def test_abba_removes_linear_additive_and_gain_drift(self):
        a, b = F(1, 5), F(4, 5)
        values = [
            4 + 7 * t + (2 + F(3, 4) * t) * (a if k == "A" else b)
            for t, k in enumerate(LINEAR_BLOCK)
        ]
        self.assertEqual(contrast(LINEAR_BLOCK, values), F(25, 8) * (a - b))

    def test_curvature_reverses_abba_but_not_the_eight_reading_design(self):
        def values(block):
            return [t * t + (k == "B") for t, k in enumerate(block)]

        self.assertEqual(contrast(LINEAR_BLOCK, values(LINEAR_BLOCK)), 1)
        self.assertEqual(contrast(QUADRATIC_BLOCK, values(QUADRATIC_BLOCK)), -1)
        times = tuple(range(len(QUADRATIC_BLOCK)))
        self.assertEqual([moment_imbalance(QUADRATIC_BLOCK, times, j)
                          for j in range(4)], [0, 0, 0, -12])

    def test_eight_is_minimum_for_even_equal_weight_equidistant_quadratic_blocks(self):
        survivors = {}
        for n in (2, 4, 6, 8):
            times = range(n)
            survivors[n] = [
                "".join("A" if t in a else "B" for t in times)
                for a in combinations(times, n // 2)
                if all(2 * sum(t ** j for t in a) == sum(t ** j for t in times)
                       for j in (1, 2))
            ]
        self.assertEqual(survivors, {
            2: [], 4: [], 6: [],
            8: [QUADRATIC_BLOCK, "BAABABBA"],
        })

    def test_quadratic_gain_drift_cancels_at_equal_time_moments(self):
        a, b = F(1, 5), F(4, 5)
        gains = [1 + F(t, 2) + F(t * t, 3) for t in range(8)]
        readings = [7 - 5*t + 2*t*t + gain * (a if label == "A" else b)
                    for t, (gain, label) in enumerate(zip(gains, QUADRATIC_BLOCK))]
        self.assertEqual(contrast(QUADRATIC_BLOCK, readings), sum(gains)/8 * (a - b))

    def test_uneven_timestamps_reveal_a_residual(self):
        self.assertEqual(moment_imbalance(LINEAR_BLOCK, (0, 1, 2, 4), 1), F(1, 2))

    def test_opposite_sign_and_zero_controls(self):
        self.assertEqual(optical_difference(F(9, 10), F(1, 10), F(3, 4), vertical=False),
                         F(-3, 5))
        self.assertEqual(optical_difference(F(9, 10), F(1, 10), F(3, 4), vertical=True),
                         F(3, 5))
        self.assertEqual(optical_difference(F(1, 2), F(1, 2), 1, vertical=True), 0)
        self.assertEqual(optical_difference(1, 0, 0, vertical=False), 0)

    def test_against_direct_complex_jones_matrix(self):
        for theta, delta, vertical in product((0, pi/12, pi/4), (pi/3, pi), (False, True)):
            c, s = cos(theta), sin(theta)
            phase = complex(cos(delta), sin(delta))
            plate = ((c*c + phase*s*s, (1-phase)*c*s),
                     ((1-phase)*c*s, s*s + phase*c*c))

            def rotate(x, y):
                return tuple(a*x+b*y for a, b in plate)

            def polarize(x, y):
                return sqrt(.9)*x, sqrt(.1)*y

            prior = (0, 1) if vertical else (1, 0)
            a = sum(abs(z)**2 for z in polarize(*rotate(*prior)))
            b = sum(abs(z)**2 for z in rotate(*polarize(*prior)))
            q = sin(delta/2)**2 * sin(2*theta)**2
            expect = optical_difference(.9, .1, q, vertical=vertical)
            self.assertAlmostEqual(a-b, expect)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            contrast("AAAA", (1, 2, 3, 4))
        with self.assertRaises(ValueError):
            contrast(LINEAR_BLOCK, (1, 2))
        with self.assertRaises(ValueError):
            optical_difference(0, 1, 1, vertical=False)


if __name__ == "__main__":
    unittest.main()
