"""Cross-science handoff counterexamples. No unearned semantics in test names."""
import unittest
from math import factorial
from itertools import permutations
from contact_stabilizer_v54 import (EncounterProblem, LocalPractice,
                                    PhysicalHandoff, undirected_practice)

A = ("a0", "a1", "a2", "a3")
B = ("b0", "b1", "b2", "b3")
CYCLE_A = undirected_practice(A, (("a0", "a1"), ("a1", "a2"),
                                   ("a2", "a3"), ("a3", "a0")))
CYCLE_B = undirected_practice(B, (("b0", "b1"), ("b1", "b2"),
                                   ("b2", "b3"), ("b3", "b0")))
PATH_B = undirected_practice(B, (("b0", "b1"), ("b1", "b2"), ("b2", "b3")))


def hand(a, b, authenticated=True, stable=True):
    return PhysicalHandoff(a, b, authenticated, stable)


class TestStabilizer(unittest.TestCase):
    def test_nothing_shared_no_match_can_be_preferred(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B)
        self.assertEqual(len(p.candidates()), factorial(4))

    def test_local_graphs_only_used_with_explicit_cross_lab_invariance(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B, structural_invariance_established=True)
        self.assertEqual(len(p.candidates()), 8)
        self.assertEqual(len(EncounterProblem(CYCLE_A, PATH_B).candidates()), 24)
        self.assertEqual(EncounterProblem(CYCLE_A, PATH_B,
                         structural_invariance_established=True).candidates(), ())

    def test_neither_an_unauthenticated_nor_unstable_transfer_is_an_anchor(self):
        contacts = (hand("a0", "b0", authenticated=False), hand("a1", "b1", stable=False))
        p = EncounterProblem(CYCLE_A, CYCLE_B, contacts, True)
        self.assertEqual(len(p.candidates()), 8)

    def test_one_certified_contact_breaks_some_but_not_all_symmetry(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B, (hand("a0", "b0"),), True)
        self.assertEqual(len(p.candidates()), 2)

    def test_opposite_contact_is_uninformative_following_one_anchor(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B, (hand("a0", "b0"),), True)
        q = EncounterProblem(CYCLE_A, CYCLE_B,
                             (hand("a0", "b0"), hand("a2", "b2")), True)
        self.assertEqual(len(q.candidates()), len(p.candidates()))
        self.assertEqual(set(r["a_preparation"] for r in p.next_contact_value()), {"a1", "a3"})

    def test_neighbor_contact_resolves_cycle_orientation(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B,
                             (hand("a0", "b0"), hand("a1", "b1")), True)
        self.assertEqual(p.candidates(), (B,))
        self.assertEqual(p.next_contact_value(), ())

    def test_without_structural_hypothesis_two_contacts_leave_factorial_uncertainty(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B,
                             (hand("a0", "b0"), hand("a1", "b1")))
        self.assertEqual(len(p.candidates()), 2)

    def test_inconsistent_certified_contacts_return_empty_not_unique(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B,
                             (hand("a0", "b0"), hand("a0", "b1")), True)
        self.assertEqual(p.candidates(), ())
        self.assertEqual(p.next_contact_value(), ())

    def test_query_information_is_conditional_not_promise(self):
        p = EncounterProblem(CYCLE_A, CYCLE_B, (hand("a0", "b0"),), True)
        v = p.next_contact_value()
        self.assertEqual(len(v), 2)
        for choice in v:
            self.assertEqual(choice["class_sizes"], (1,1))
            self.assertEqual(choice["worst_case_remaining"], 1)
            self.assertEqual(choice["expected_remaining_uniform"], 1)
            self.assertAlmostEqual(choice["expected_information_bits_uniform"], 1)

    def test_complete_graph_remains_permutation_symmetric(self):
        ea = tuple((A[i], A[j]) for i in range(4) for j in range(i+1,4))
        eb = tuple((B[i], B[j]) for i in range(4) for j in range(i+1,4))
        p = EncounterProblem(undirected_practice(A,ea), undirected_practice(B,eb),
                             structural_invariance_established=True)
        self.assertEqual(len(p.candidates()), 24)
        self.assertEqual(len(EncounterProblem(p.a,p.b,(hand("a0","b0"),),True).candidates()),6)

    def test_non_matching_inventory_rejected(self):
        with self.assertRaises(ValueError):
            EncounterProblem(CYCLE_A, undirected_practice(("x",), ()))

    def test_invalid_graph_and_contact_rejected(self):
        with self.assertRaises(ValueError):
            undirected_practice(A, (("a0","a0"),))
        with self.assertRaises(ValueError):
            undirected_practice(A, (("a0","a1"),("a1","a0")))
        with self.assertRaises(ValueError):
            EncounterProblem(CYCLE_A,CYCLE_B,(hand("unknown","b1"),))

    def test_exhaustive_two_lab_graphs_four_nodes(self):
        # Exhaust over every one of the 64 possible labeled A graphs.
        # B is constructed by each of the 24 permutations; the exact
        # number of compatible mappings equals the automorphism size of A.
        all_edges=tuple((A[i],A[j]) for i in range(4) for j in range(i+1,4))
        b_lookup=dict(zip(A,B))
        for mask in range(1 << len(all_edges)):
            ea=tuple(edge for i,edge in enumerate(all_edges) if mask>>i&1)
            a=undirected_practice(A,ea)
            aut=EncounterProblem(a,undirected_practice(B,tuple(
                (b_lookup[x],b_lookup[y]) for x,y in ea)),
                structural_invariance_established=True).candidates()
            self.assertGreaterEqual(len(aut),1)
            for p in permutations(B):
                relabel=dict(zip(B,p))
                b=undirected_practice(B,tuple((relabel[b_lookup[x]],relabel[b_lookup[y]]) for x,y in ea))
                c=EncounterProblem(a,b,structural_invariance_established=True).candidates()
                self.assertEqual(len(c),len(aut))

if __name__ == '__main__':
    unittest.main()
