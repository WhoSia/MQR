"""MQR 43: exact stochastic negative control for preparation-mixture claims.

Bernoulli conditional output probabilities abstract away instrument dynamics.
This tests general inference limits, not a physical noise model.
"""
import unittest
from fractions import Fraction as F
from itertools import product
from preparation_mixture_bridge_v54 import rank_exact


def pooled_u_probability(weights, conditionals):
    if not weights or len(weights) != len(conditionals):
        raise ValueError("Weights and conditionals must have equal nonzero length")
    w = tuple(F(x) for x in weights)
    v = tuple(F(x) for x in conditionals)
    if any(x < 0 for x in w) or sum(w) != 1:
        raise ValueError("Invalid mixture weights")
    if any(x < 0 or x > 1 for x in v):
        raise ValueError("Invalid conditional Bernoulli probability")
    return sum((x * y for x, y in zip(w, v)), F(0))


class TestStochasticBridge(unittest.TestCase):
    def test_single_biased_mixture_can_hide_stochastic_order_effect(self):
        weights = (F(3, 4), F(1, 4))
        ab = (F(3, 5), F(1, 5))
        ba = (F(1, 2), F(1, 2))
        self.assertNotEqual(ab, ba)
        self.assertEqual(pooled_u_probability(weights, ab), F(1, 2))
        self.assertEqual(pooled_u_probability(weights, ba), F(1, 2))

    def test_second_mixture_exposes_stochastic_cancellation(self):
        ab = (F(3, 5), F(1, 5))
        ba = (F(1, 2), F(1, 2))
        weights = (F(1, 2), F(1, 2))
        self.assertEqual(pooled_u_probability(weights, ab), F(2, 5))
        self.assertEqual(pooled_u_probability(weights, ba), F(1, 2))
        self.assertEqual(rank_exact(((F(3, 4), F(1, 4)), weights)), 2)

    def test_two_spanning_mixtures_identify_conditional_equality_on_grid(self):
        grid = (F(0), F(1, 3), F(2, 3), F(1))
        weights = ((F(3, 4), F(1, 4)), (F(1, 2), F(1, 2)))
        checked = 0
        for a0, a1, b0, b1 in product(grid, repeat=4):
            ab = (a0, a1)
            ba = (b0, b1)
            same_mixtures = all(pooled_u_probability(w, ab) == pooled_u_probability(w, ba)
                                for w in weights)
            self.assertEqual(same_mixtures, ab == ba)
            checked += 1
        self.assertEqual(checked, 256)

    def test_failure_states(self):
        for w, p in [((F(1, 2),), (F(1, 2), F(1, 2))),
                     ((F(1, 2), F(1, 3)), (0, 1)),
                     ((-1, 2), (0, 1)),
                     ((F(1, 2), F(1, 2)), (F(5, 4), 0))]:
            with self.assertRaises(ValueError):
                pooled_u_probability(w, p)


if __name__ == "__main__":
    unittest.main()
