import unittest
from ptb_alignment_sensitivity_v54 import alignment_sensitivity


class TestAlignment(unittest.TestCase):
    def _traces(self,n=12):
        a=tuple((float(i),float(i*2)) for i in range(n))
        b=tuple((float(i),float(i*3)) for i in range(n))
        c=tuple((float(i),float(i*5+0.7)) for i in range(n))
        return a,b,c

    def test_zero_shift_preserves_exact_arithmetic_closure(self):
        x=alignment_sensitivity(*self._traces(),lags=(0,1,-1))
        self.assertLess(x[0]['holdout_rmse_mV'],1e-10)
        # Linear trends allow an offset re-fit to hide a one-step shift.
        self.assertLess(x[1]['holdout_rmse_mV'],1e-10)

    def test_nonlinear_curve_detects_shift_after_fitting_constant(self):
        a,b,c=self._traces()
        a=tuple((t,t*t) for t,_ in a)
        c=tuple((t,t*t+3*t+0.7) for t,_ in c)
        result=alignment_sensitivity(a,b,c,lags=(0,1,-1))
        self.assertLess(result[0]['holdout_rmse_mV'],1e-9)
        self.assertGreater(result[1]['holdout_rmse_mV'],1.0)

    def test_reject_time_grid_relabel(self):
        a,b,c=self._traces();b=list(b);b[2]=(2.5,b[2][1])
        with self.assertRaises(ValueError):alignment_sensitivity(a,b,c)

    def test_reject_unordered_grid(self):
        a,b,c=self._traces();a=list(a);b=list(b);c=list(c)
        for t in (a,b,c):t[1]=(t[0][0],t[1][1])
        with self.assertRaises(ValueError):alignment_sensitivity(a,b,c)

    def test_invalid_lags(self):
        for lag in (True,0.5,10,12):
            with self.subTest(lag=lag),self.assertRaises(ValueError):
                alignment_sensitivity(*self._traces(),lags=(lag,))

    def test_too_short(self):
        a,b,c=self._traces(3)
        with self.assertRaises(ValueError):alignment_sensitivity(a,b,c)


if __name__=='__main__':
    unittest.main()
