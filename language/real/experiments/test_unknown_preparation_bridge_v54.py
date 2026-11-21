import unittest
from itertools import product
from math import factorial
from unknown_preparation_bridge_v54 import BridgeProblem, SharedChannel


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.a=("A0","A1","A2")
        self.b=("B0","B1","B2")

    def test_no_shared_preparation_or_predicate_has_full_permutation_ambiguity(self):
        self.assertEqual(len(BridgeProblem(self.a,self.b).possible_bijections()),6)

    def test_one_verified_anchor_leaves_two_equally_supported_mappings(self):
        b=BridgeProblem(self.a,self.b,anchors=(("A0","B2"),))
        self.assertEqual(len(b.possible_bijections()),2)

    def test_unique_shared_invariant_signatures_identify_mapping_conditionally(self):
        probe=SharedChannel("common",( "x","y","z"),("z","x","y"))
        b=BridgeProblem(self.a,self.b,channels=(probe,))
        self.assertEqual(b.possible_bijections(),(("B1","B2","B0"),))

    def test_identical_signatures_cannot_break_any_symmetry(self):
        same=SharedChannel("unchanging",("0",)*3,("0",)*3)
        b=BridgeProblem(self.a,self.b,channels=(same,))
        self.assertEqual(len(b.possible_bijections()),6)
        self.assertIsNone(b.best_proposed_channel((SharedChannel("other",("0",)*3,("0",)*3),)))

    def test_best_probe_demands_external_cross_agent_semantic_bridge(self):
        b=BridgeProblem(self.a,self.b,channels=(SharedChannel("flat",("0",)*3,("0",)*3),))
        split=SharedChannel("partial",("0","0","1"),("1","0","0"))
        unique=SharedChannel("unique",("0","1","2"),("2","0","1"))
        self.assertEqual(b.best_proposed_channel((split,unique)), "unique")
        self.assertEqual(b.possible_bijections((unique,)),(("B1","B2","B0"),))

    def test_contradictory_channel_creates_zero_candidates_not_false_certainty(self):
        p=BridgeProblem(self.a,self.b,channels=(SharedChannel("wrong",("0",)*3,("1",)*3),))
        self.assertEqual(p.possible_bijections(),())
        self.assertIsNone(p.best_proposed_channel((SharedChannel("new",("0","1","2"),("0","1","2")),)))

    def test_invalid_structure_and_duplicates_rejected(self):
        cases=(((),()),(("A","A"),("B","C")),(("A",),("B","C")))
        for a,b in cases:
            with self.subTest(a=a,b=b), self.assertRaises(ValueError):
                BridgeProblem(a,b)
        with self.assertRaises(ValueError):
            BridgeProblem(self.a,self.b,anchors=(("A0","B0"),("A1","B0")))
        with self.assertRaises(ValueError):
            BridgeProblem(self.a,self.b,channels=(SharedChannel("invalid",("0",),("0",)*3),))
        with self.assertRaises(ValueError):
            BridgeProblem(self.a,self.b).possible_bijections((SharedChannel("x",("0",),("0",)*3),))

    def test_exhaustive_binary_signatures_with_identical_histogram(self):
        for bits in product("01",repeat=3):
            n0=bits.count("0")
            b=BridgeProblem(self.a,self.b,channels=(SharedChannel("binary",bits,bits),))
            self.assertEqual(len(b.possible_bijections()),factorial(n0)*factorial(3-n0))

    def test_value_relabeling_without_semantic_bridge_is_not_evidence(self):
        a=SharedChannel("verified",("0","1","2"),("0","1","2"))
        b=BridgeProblem(self.a,self.b,channels=(a,))
        self.assertEqual(len(b.possible_bijections()),1)
        # The model has explicitly assumed the channel outputs are comparable.
        # Without that assumption, even same-looking labels leave 3! mappings.
        self.assertEqual(len(BridgeProblem(self.a,self.b).possible_bijections()),6)


if __name__=="__main__":
    unittest.main()
