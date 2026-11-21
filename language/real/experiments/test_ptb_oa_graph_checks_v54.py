"""Negative controls for PTB figure-export arithmetic."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ptb_oa_graph_checks_v54 import summarize_closure, analyze, load_time_voltage


class GraphTests(unittest.TestCase):
    def test_offset_train_then_holdout(self):
        p = ((0.,2.),(1.,4.),(2.,6.),(3.,8.))
        n = ((0.,-1.),(1.,-1.),(2.,-1.),(3.,-1.))
        w = ((0.,1.2),(1.,3.2),(2.,5.2),(3.,7.2))
        r = summarize_closure(p,n,w)
        self.assertAlmostEqual(r["mean_unadjusted"], -0.2)
        self.assertLess(r["holdout_rmse_after_offset"],1e-10)

    def test_mismatched_grid_rejected(self):
        with self.assertRaisesRegex(ValueError,"grid"):
            summarize_closure(((0,1),(1,1)),((0,1),(2,1)),((0,2),(1,2)))

    def test_small_cases_rejected(self):
        with self.assertRaises(ValueError): summarize_closure([],[],[])
        with self.assertRaises(ValueError): summarize_closure(((0,1),),((0,1),),((0,1),))

    def test_zero_offset_is_not_physical_correspondence(self):
        a=((0,1),(1,4)); b=((0,2),(1,2)); whole=((0,3),(1,6))
        result=summarize_closure(a,b,whole)
        self.assertEqual(result["holdout_rmse_after_offset"], 0.)
        self.assertIn("no dark calibration", result["interpretation"])

    def test_original_publisher_archive_if_present(self):
        p=Path("/mnt/data/Opto-JAWS.zip")
        if not p.exists():self.skipTest("Original archive not mounted")
        r=analyze(str(p))
        self.assertEqual(r["n"],999)
        self.assertAlmostEqual(r["mean_unadjusted"],-0.2295063963963961,places=9)
        self.assertAlmostEqual(r["holdout_rmse_after_offset"],0.0038220474107747288,places=9)

    def test_unknown_export_rejected(self):
        with self.assertRaises(ValueError):load_time_voltage("not-present.zip","../../../etc/passwd")


if __name__=="__main__":
    unittest.main()
