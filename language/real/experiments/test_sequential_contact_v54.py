import unittest
from itertools import product
from sequential_contact_v54 import Instrument, analyze_pair, partition


def ins(name, labels, after=None):
    n = len(labels)
    return Instrument(name, tuple(labels), tuple(range(n)) if after is None else tuple(after))


class SequentialContactTests(unittest.TestCase):
    def test_complementary_native_readouts_refine_without_shared_alphabet(self):
        a = ins('Alpha', ('alfa','beta','alfa','beta'))
        b = ins('Beta', ('cold','cold','warm','warm'))
        r = analyze_pair(a,b)
        self.assertEqual(len(r['a_partition']),2)
        self.assertEqual(len(r['b_partition']),2)
        self.assertEqual(r['ideal_partition'],((0,),(1,),(2,),(3,)))
        self.assertEqual(r['ab'],r['ba'])

    def test_commuting_backaction_does_not_imply_order_agreement(self):
        swap=(1,0,3,2)
        a=ins('A',('a','a','b','b'),swap)
        b=ins('B',('x','y','x','y'),swap)
        r=analyze_pair(a,b)
        self.assertTrue(r['physical_maps_commute'])
        self.assertFalse(r['order_agreement_globally'])

    def test_noncommuting_backaction_can_preserve_all_visible_readouts(self):
        a=ins('A',('a','a','a','b','b'),(1,0,2,3,4))
        b=ins('B',('u','u','u','v','v'),(0,2,1,3,4))
        r=analyze_pair(a,b)
        self.assertFalse(r['physical_maps_commute'])
        self.assertTrue(r['order_agreement_globally'])

    def test_measuring_first_can_cause_more_differentiation_than_joint_nondemolition(self):
        a=ins('A',('a','a','b','b'),(0,2,2,3))
        b=ins('B',('x','x','y','y'))
        r=analyze_pair(a,b)
        self.assertEqual(r['ideal_partition'],((0,1),(2,3)))
        self.assertEqual(r['ab_partition'],((0,),(1,),(2,3)))
        self.assertFalse(r['order_agreement_globally'])

    def test_readout_partition_and_empty_subset_checks(self):
        a=ins('A',('a','b','a'))
        b=ins('B',('x','x','y'))
        with self.assertRaises(ValueError):analyze_pair(a,b,())
        with self.assertRaises(ValueError):analyze_pair(a,b,(0,0))
        with self.assertRaises(ValueError):analyze_pair(a,b,(0,3))
        with self.assertRaises(ValueError):analyze_pair(a,ins('A',('x','x','y')))
        self.assertEqual(partition(('x','x','y')),((0,1),(2,)))

    def test_one_clean_state_does_not_certify_global_order(self):
        a=ins('A',('a','a','b','b'),(0,2,2,3))
        b=ins('B',('x','x','y','y'))
        r=analyze_pair(a,b,(0,))
        self.assertTrue(r['observed_order_agreement_on_checked'])
        self.assertFalse(r['order_agreement_globally'])

    def test_independent_exhaustive_order_non_disturbance_equivalence(self):
        # 8 binary readout vectors for each native instrument, each of 27 maps.
        # 8*8*27*27=46,656 independently enumerated 3-state cases.
        patterns=list(product('01',repeat=3))
        maps=list(product(range(3),repeat=3))
        checks=0
        for la in patterns:
            for lb in patterns:
                for ma in maps:
                    for mb in maps:
                        r=analyze_pair(ins('A',la,ma),ins('B',lb,mb))
                        predicted=all(lb[ma[s]]==lb[s] and la[mb[s]]==la[s] for s in range(3))
                        self.assertEqual(r['order_agreement_globally'],predicted)
                        checks+=1
        self.assertEqual(checks,46656)

    def test_invalid_maps_fail_closed(self):
        with self.assertRaises(ValueError):ins('A',('x','y'),(0,True))
        with self.assertRaises(ValueError):ins('A',('x','y'),(0,2))
        with self.assertRaises(ValueError):ins('A',('x',))


if __name__=='__main__':unittest.main()
