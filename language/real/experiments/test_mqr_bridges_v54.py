import unittest
from fractions import Fraction
from mqr_nonbijective_bridges_v54 import identified, conditional_entropy_preimage
from mqr_dynamic_quotient_bridge_v54 import quotient_action, A, F


class ScientificBridgeTests(unittest.TestCase):
    def test_candidates_from_marginals(self):
        self.assertEqual((len(identified()),len(identified(anchors=((0,'left'),))),len(identified(anchors=((0,'left'),(1,'left'))))), (3,2,1))

    def test_conditional_information_loss(self):
        self.assertTrue(all(conditional_entropy_preimage(f)==Fraction(2,3) for f in identified()))

    def test_wrong_marginal_or_anchors(self):
        self.assertFalse(identified(anchors=((0,'left'),(1,'left'),(2,'left'))))

    def test_fiber_permutation_commutes(self):
        t={0:1,1:0,2:2}
        g=quotient_action(t)
        self.assertIsNotNone(g)
        self.assertTrue(all(F[t[a]] == g[F[a]] for a in A))

    def test_split_fiber_fails(self):
        self.assertIsNone(quotient_action({0:0,1:2,2:1}))

    def test_constant_map_preserves_quotient(self):
        self.assertEqual(quotient_action({0:2,1:2,2:2}), {'L':'R','R':'R'})

if __name__ == '__main__':
    unittest.main()
