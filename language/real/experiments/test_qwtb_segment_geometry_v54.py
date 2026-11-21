"""Unit tests for reproducible energy partition; real waveform not bundled."""
import unittest
import numpy as np
from qwtb_segment_geometry_v54 import qwtb_vector, segment_energy_profile


class TestQwtbSegmentGeometry(unittest.TestCase):
    def test_parse_integer_vectors(self):
        self.assertEqual(qwtb_vector('#startmatrix:: S\n "[1,3,6]"\n#endmatrix:: S','S'),(1,3,6))

    def test_reject_unavailable_vector(self):
        with self.assertRaises(ValueError):qwtb_vector('#startmatrix:: M\n "[1]"\n#endmatrix:: M','S')

    def test_reject_noninteger_vector(self):
        with self.assertRaises(ValueError):qwtb_vector('#startmatrix:: M\n "[1, 0.5]"\n#endmatrix:: M','M')

    def test_identical_energy_by_direct_and_partitioned_formula(self):
        x=np.array([1.,0.,-2.,3.,-4.,5.])
        r=segment_energy_profile(x,(0,2,5,6))
        self.assertAlmostEqual(r['direct_all_sample_rms_V'],np.sqrt(55/6))
        self.assertAlmostEqual(r['weighted_segment_reconstruction_rms_V'],np.sqrt(55/6))
        self.assertEqual(r['segment_widths'],[2,3,1])

    def test_explicit_zero_segment_retained(self):
        r=segment_energy_profile([0,0,2,2],(0,2,4))
        self.assertEqual(r['segment_rms_V'],[0.,2.])
        self.assertAlmostEqual(r['direct_all_sample_rms_V'],np.sqrt(2))

    def test_reject_overlap_or_gaps(self):
        for starts in [(0,2,2,4),(0,2,3),(1,2,4),(0,5,4)]:
            with self.assertRaises(ValueError):segment_energy_profile(np.arange(4.),starts)

    def test_reject_nonfinite_samples(self):
        for x in ([1,float('nan')],[1,float('inf')]):
            with self.assertRaises(ValueError):segment_energy_profile(x,(0,1,2))

    def test_different_window_weighting_changes_summary(self):
        x=np.array([10.,10.,0.,0.,0.,0.]);r=segment_energy_profile(x,(0,2,6))
        self.assertEqual(r['segment_rms_V'],[10.,0.])
        self.assertAlmostEqual(r['direct_all_sample_rms_V'],np.sqrt(200/6))
        self.assertNotAlmostEqual(r['direct_all_sample_rms_V'],np.mean(r['segment_rms_V']))


if __name__=='__main__':unittest.main()
