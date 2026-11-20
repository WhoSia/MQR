from fractions import Fraction
import unittest
from two_wavelength_jones_v54 import RetarderHypothesis, first_discriminating_wavelength


class WavelengthWitnessTests(unittest.TestCase):
    def setUp(self):
        self.a=RetarderHypothesis("A", (("lambda_0",1),("lambda_1",2)))
        self.b=RetarderHypothesis("B", (("lambda_0",1),("lambda_1",1)))

    def test_same_jones_at_first_wavelength_not_second(self):
        self.assertEqual(self.a.jones_diagonal("lambda_0"), self.b.jones_diagonal("lambda_0"))
        self.assertNotEqual(self.a.jones_diagonal("lambda_1"), self.b.jones_diagonal("lambda_1"))

    def test_analyzer_45_detects_difference_only_on_heldout_wavelength(self):
        self.assertEqual(self.a.analyzer_45_intensity("lambda_0"), Fraction(1,2))
        self.assertEqual(self.b.analyzer_45_intensity("lambda_0"), Fraction(1,2))
        self.assertEqual(self.a.analyzer_45_intensity("lambda_1"), Fraction(0))
        self.assertEqual(self.b.analyzer_45_intensity("lambda_1"), Fraction(1,2))
        self.assertEqual(first_discriminating_wavelength(self.a,self.b,("lambda_0","lambda_1")),"lambda_1")

    def test_total_intensity_cannot_distinguish_any_retarder_here(self):
        self.assertIsNone(first_discriminating_wavelength(self.a,self.b,("lambda_0","lambda_1"),"total"))

    def test_sign_of_phase_is_not_resolved_by_this_single_analyzer(self):
        a=RetarderHypothesis("+i",(("one",1),))
        b=RetarderHypothesis("-i",(("one",3),))
        self.assertNotEqual(a.jones_diagonal("one"),b.jones_diagonal("one"))
        self.assertIsNone(first_discriminating_wavelength(a,b,("one",)))

    def test_all_quarter_phases_have_exact_table(self):
        expected=(Fraction(1),Fraction(1,2),Fraction(0),Fraction(1,2))
        for q, exp in enumerate(expected):
            r=RetarderHypothesis(str(q),(("x",q),))
            self.assertEqual(r.analyzer_45_intensity("x"),exp)
            self.assertEqual(r.total_intensity("x"),Fraction(1))

    def test_bad_labels_phases_and_probes(self):
        for name,probes in (("",(("x",0),)),("x",()),("x",(("x",0),("x",1))),
                            ("x",(("",0),)),("x",(("x",-1),)),("x",(("x",4),)),("x",(("x",1.5),))):
            with self.subTest(name=name,probes=probes),self.assertRaises(ValueError):
                RetarderHypothesis(name,probes)
        with self.assertRaises(ValueError):
            self.a.total_intensity("missing")
        with self.assertRaises(ValueError):
            first_discriminating_wavelength(self.a,self.b,("lambda_0","lambda_0"))
        with self.assertRaises(ValueError):
            first_discriminating_wavelength(self.a,self.b,("lambda_0",),"unknown")


if __name__=='__main__':
    unittest.main()
