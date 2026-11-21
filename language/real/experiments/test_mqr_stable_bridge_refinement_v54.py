import unittest
from mqr_stable_bridge_refinement_v54 import refine, normalise, stable, verify

class StableBridgeTests(unittest.TestCase):
    def test_full_example(self):
        self.assertTrue(verify().startswith('PASS'))
    def test_successive_splitting(self):
        initial=((0,1,2),(3,))
        shift={0:1,1:2,2:3,3:3}
        _, history=refine(range(4),initial,(shift,))
        self.assertEqual([len(b) for b in history], [2,3,4])
    def test_no_action_keeps_partition(self):
        p,_=refine(range(4),((0,1,2),(3,)),())
        self.assertEqual(p,((0,1,2),(3,)))
    def test_refinement_monotonic(self):
        source=((0,1,2),(3,))
        id4={i:i for i in range(4)}
        shift={0:1,1:2,2:3,3:3}
        p1,_=refine(range(4),source,(id4,))
        p2,_=refine(range(4),source,(id4,shift))
        self.assertLessEqual(len(p1),len(p2))
    def test_invalid_action_rejected(self):
        with self.assertRaises(AssertionError):
            refine(range(4),((0,1,2),(3,)),({0:0},))
    def test_invalid_partition_rejected(self):
        with self.assertRaises(AssertionError):
            refine(range(4),((0,1,2),(2,3)),())

if __name__ == '__main__':
    unittest.main()
