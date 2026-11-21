"""Exact executable regression suite for MQR 43 / research version 5.4."""
import unittest
from fractions import Fraction as F
from itertools import product

from preparation_mixture_bridge_v54 import (
    NativeLabPair, balanced_masking_pair, nondisturbing_pooled_rival,
    exact_mixture, order_gap, pointwise_order_equal, rank_exact,
    certified_mixture_family_identifies_pointwise,
)


class TestMixtureBridge(unittest.TestCase):
    def test_balanced_pooled_agreement_misses_each_state(self):
        pair = balanced_masking_pair()
        self.assertEqual(order_gap(pair, (F(1, 2), F(1, 2))), 0)
        self.assertFalse(pointwise_order_equal(pair))
        self.assertNotEqual(pair.read(0, "AB"), pair.read(0, "BA"))
        self.assertNotEqual(pair.read(1, "AB"), pair.read(1, "BA"))

    def test_pooled_rival_is_identical_in_balanced_runs_but_different_in_cause(self):
        adversarial = balanced_masking_pair()
        stable = nondisturbing_pooled_rival()
        for order in ("AB", "BA"):
            self.assertEqual(exact_mixture(adversarial, order, (F(1, 2), F(1, 2))),
                             exact_mixture(stable, order, (F(1, 2), F(1, 2))))
        self.assertTrue(pointwise_order_equal(stable))
        self.assertFalse(pointwise_order_equal(adversarial))

    def test_preparation_shift_exposes_masked_order_effect(self):
        bad = balanced_masking_pair()
        good = nondisturbing_pooled_rival()
        self.assertEqual(order_gap(bad, (F(3, 4), F(1, 4))), F(1, 2))
        self.assertEqual(order_gap(good, (F(3, 4), F(1, 4))), 0)
        for numerator in range(11):
            p = F(numerator, 10)
            self.assertEqual(order_gap(bad, (p, 1 - p)), abs(2 * p - 1))

    def test_two_distinct_mixtures_form_spanning_probe_family(self):
        bad = balanced_masking_pair()
        weights = ((F(1, 2), F(1, 2)), (F(3, 4), F(1, 4)))
        self.assertEqual(rank_exact(weights), 2)
        self.assertFalse(certified_mixture_family_identifies_pointwise(bad, weights))
        self.assertTrue(certified_mixture_family_identifies_pointwise(nondisturbing_pooled_rival(), weights))

    def test_rank_deficiency_blocks_conclusion(self):
        good = nondisturbing_pooled_rival()
        rows = ((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)))
        self.assertEqual(rank_exact(rows), 1)
        self.assertFalse(certified_mixture_family_identifies_pointwise(good, rows))

    def test_three_state_exact_rank_and_nonsquare(self):
        self.assertEqual(rank_exact(((1, 0, 0), (0, 1, 0), (0, 0, 1))), 3)
        self.assertEqual(rank_exact(((1, 0, 0), (0, 1, 0))), 2)
        self.assertRaises(ValueError, rank_exact, ((1, 2), (3,)))

    def test_invalid_weights_and_order_fail_closed(self):
        pair = balanced_masking_pair()
        for w in ((F(1, 2),), (-1, 2), (0, 0), (F(1, 3), F(1, 3))):
            with self.assertRaises(ValueError):
                exact_mixture(pair, "AB", w)
        self.assertRaises(ValueError, pair.read, 0, "AC")
        self.assertRaises(ValueError, pair.read, 2, "AB")
        self.assertRaises(ValueError, NativeLabPair, (0, 1), (0, 1), (0, 2), (0, 1))

    def test_exhaustive_two_state_rank_sufficiency(self):
        vals = list(product((0, 1), repeat=2))
        maps = list(product((0, 1), repeat=2))
        rows = ((F(1, 2), F(1, 2)), (F(3, 4), F(1, 4)))
        seen_masked = False
        checked = 0
        for a, b, ma, mb in product(vals, vals, maps, maps):
            pair = NativeLabPair(a, b, ma, mb)
            checked += 1
            pooled_agree = all(order_gap(pair, w) == 0 for w in rows)
            self.assertEqual(pooled_agree, pointwise_order_equal(pair))
            if order_gap(pair, rows[0]) == 0 and not pointwise_order_equal(pair):
                seen_masked = True
        self.assertEqual(checked, 256)
        self.assertTrue(seen_masked)


if __name__ == "__main__":
    unittest.main()
