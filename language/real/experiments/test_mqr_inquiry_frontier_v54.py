import unittest
from fractions import Fraction as F
from mqr_inquiry_frontier_v54 import (target_vs_random, correlated_reports_posteriors, partitions, verify)

class InquiryFrontierTests(unittest.TestCase):
    def test_global(self):
        self.assertTrue(verify().startswith("PASS"))
    def test_known_target_beats_random(self):
        for n in range(1,10):
            r=target_vs_random(n)
            self.assertGreater(r["known_targeted"],r["known_random"])
    def test_novelty_outside_target(self):
        for n in range(1,10):
            r=target_vs_random(n)
            self.assertGreater(r["novelty_random"],r["novelty_targeted_outside"])
    def test_no_data_is_no_detection(self):
        self.assertEqual(target_vs_random(0)["novelty_random"],0)
        self.assertEqual(target_vs_random(0)["known_targeted"],0)
    def test_one_ancestral_report_not_four_independent(self):
        naive, ancestry=correlated_reports_posteriors(4)
        self.assertEqual(naive,F(81,82))
        self.assertEqual(ancestry,F(3,4))
    def test_independent_ancestry_assumption_is_explicit(self):
        self.assertEqual(correlated_reports_posteriors(1), (F(3,4),F(3,4)))
    def test_pair_observables_refine(self):
        a,b,ab=partitions()
        self.assertEqual((len(a),len(b),len(ab)),(2,2,4))

if __name__=="__main__":
    unittest.main()
