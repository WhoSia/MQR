import unittest
from itertools import permutations
from unpaired_native_readouts_v54 import LocalInventory,UnpairedInventories

A=LocalInventory(('a0','a1','a2','a3'),('a','a','b','b'))
B=LocalInventory(('b0','b1','b2','b3'),('x','x','y','y'))

class UnpairedReadoutTests(unittest.TestCase):
    def test_without_contact_joint_partition_is_not_identifiable(self):
        r=UnpairedInventories(A,B)
        self.assertEqual(len(r.hypotheses()),24)
        self.assertEqual(r.possible_joint_class_counts(),{2:8,4:16})

    def test_one_verified_contact_not_enough(self):
        r=UnpairedInventories(A,B,(('a0','b0'),))
        self.assertEqual(len(r.hypotheses()),6)
        self.assertEqual(r.possible_joint_class_counts(),{2:2,4:4})

    def test_two_contact_choice_changes_joint_deduction(self):
        same=UnpairedInventories(A,B,(('a0','b0'),('a1','b1')))
        crossed=UnpairedInventories(A,B,(('a0','b0'),('a1','b2')))
        self.assertEqual(same.possible_joint_class_counts(),{2:2})
        self.assertEqual(crossed.possible_joint_class_counts(),{4:2})

    def test_two_seemingly_sensible_anchors_may_leave_ambiguity(self):
        r=UnpairedInventories(A,B,(('a0','b0'),('a2','b2')))
        self.assertEqual(r.possible_joint_class_counts(),{2:1,4:1})

    def test_output_renaming_does_not_change_joint_class_counts(self):
        other=LocalInventory(B.tokens,('q','q','r','r'))
        self.assertEqual(UnpairedInventories(A,B).possible_joint_class_counts(),
                         UnpairedInventories(A,other).possible_joint_class_counts())

    def test_independent_count_matches_bipartite_two_by_two_tables(self):
        counts={2:0,4:0}
        for p in permutations(range(4)):
            signatures={(A.outcomes[i],B.outcomes[p[i]]) for i in range(4)}
            counts[len(signatures)]+=1
        self.assertEqual(counts,{2:8,4:16})

    def test_failed_anchor_validation(self):
        for anchors in ((('a0','b0'),('a1','b0')),
                        (('a0','b0'),('a0','b1')),
                        (('alien','b0'),)):
            with self.subTest(anchors=anchors),self.assertRaises(ValueError):
                UnpairedInventories(A,B,anchors)

if __name__=='__main__':unittest.main()
