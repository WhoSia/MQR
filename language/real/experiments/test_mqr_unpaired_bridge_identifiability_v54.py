"""Regression tests for the MQR 5.4 unpaired bridge toy model.

Execute from any directory:
    python -m unittest discover -s language/real/experiments -p 'test_mqr_unpaired_bridge_identifiability_v54.py'
"""
import unittest
from fractions import Fraction
from itertools import product
from mqr_unpaired_bridge_identifiability_v54 import coupling, fibers, marginals

class UnpairedBridgeTests(unittest.TestCase):
    def test_same_marginals_three_different_couplings(self):
        cases = [coupling(Fraction(0)), coupling(Fraction(1, 4)),
                 coupling(Fraction(1, 2))]
        self.assertEqual(len(set(tuple(sorted(p.items())) for p in cases)), 3)
        for p in cases:
            self.assertEqual(marginals(p), ({0: Fraction(1, 2), 1: Fraction(1, 2)},
                                            {0: Fraction(1, 2), 1: Fraction(1, 2)}))

    def test_all_four_joint_signatures_distinguishable(self):
        self.assertEqual(len(fibers(lambda w: (w//2, w % 2))), 4)
        self.assertEqual(len(fibers(lambda w: w//2)), 2)
        self.assertEqual(len(fibers(lambda w: w % 2)), 2)

    def test_invalid_coupling_parameter_rejected(self):
        for t in [Fraction(-1, 4), Fraction(3, 4)]:
            with self.assertRaises(AssertionError):
                coupling(t)

    def test_normalization_extreme_and_interior(self):
        for t in [Fraction(0), Fraction(1, 8), Fraction(1, 4),
                  Fraction(3, 8), Fraction(1, 2)]:
            joint = coupling(t)
            self.assertEqual(sum(joint.values()), Fraction(1))
            self.assertTrue(all(p >= 0 for p in joint.values()))

if __name__ == "__main__":
    unittest.main()
