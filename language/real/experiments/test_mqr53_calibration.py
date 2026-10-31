"""Executable regression tests for MQR-5.3 calibration boundary."""
import unittest
from mqr53_calibration import (
    BinaryCalibration, identified_interval, hoeffding_halfwidth, transport_effect
)

class CalibrationTests(unittest.TestCase):
    def test_known_error_inversion(self):
        self.assertAlmostEqual(BinaryCalibration(.42,.1,.1).prevalence(),.4)
        self.assertAlmostEqual(transport_effect(.4),.6)

    def test_partial_identification(self):
        lo,hi=identified_interval(.42,(.08,.12),(.08,.12))
        self.assertAlmostEqual(lo,.375)
        self.assertAlmostEqual(hi,.425)

    def test_hoeffding_sufficient_n(self):
        self.assertLessEqual(hoeffding_halfwidth(289,.05,.1,.1),.1)
        self.assertGreater(hoeffding_halfwidth(288,.05,.1,.1),.1)

    def test_mechanism_instability(self):
        self.assertAlmostEqual(transport_effect(.4),.6)
        self.assertAlmostEqual(transport_effect(.4, mechanism_flipped=True),.4)

    def test_invalid_calibration(self):
        with self.assertRaises(ValueError):
            BinaryCalibration(.5,.5,.5).prevalence()
        with self.assertRaises(ValueError):
            BinaryCalibration(.05,.1,.1).prevalence()

    def test_consistency_of_interval_point(self):
        lo,hi=identified_interval(.42,(0.1,0.1),(0.1,0.1))
        self.assertAlmostEqual(lo,.4)
        self.assertAlmostEqual(hi,.4)

if __name__=="__main__":
    unittest.main()
