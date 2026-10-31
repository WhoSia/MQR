"""MQR-5.3: bounded binary calibration and transport, NOT physical validation.

All intervals are deterministic identified sets, conditional on supplied bounds.
No historical apparatus is assigned these synthetic parameter values.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import log, sqrt

@dataclass(frozen=True)
class BinaryCalibration:
    positive_rate: float
    false_positive: float
    false_negative: float

    def prevalence(self) -> float:
        q, f, n = self.positive_rate, self.false_positive, self.false_negative
        if not all(0.0 <= x <= 1.0 for x in (q, f, n)):
            raise ValueError("Probabilities must lie in [0,1]")
        sensitivity_gap = 1.0 - f - n
        if sensitivity_gap <= 0:
            raise ValueError("Calibration inversion requires sensitivity > false positive")
        b = (q - f) / sensitivity_gap
        if not (0.0 <= b <= 1.0):
            raise ValueError("Observed positivity contradicts calibration assumptions")
        return b

def identified_interval(q: float, false_positive: tuple[float,float],
                        false_negative: tuple[float,float]) -> tuple[float,float]:
    """Sharp projection for independent interval bounds, when feasible.

    The two error rates are unknown but bounded. Since q=f+(1-f-n)*b,
    enumerate parameter-box corners and feasible edges q=f or q=1-n.
    """
    fl,fh=false_positive; nl,nh=false_negative
    if not (0 <= fl <= fh <= 1 and 0 <= nl <= nh <= 1 and 0 <= q <= 1):
        raise ValueError("Invalid bounds")
    candidates=[]
    for f in (fl,fh,q):
        for n in (nl,nh,1-q):
            if fl <= f <= fh and nl <= n <= nh and f+n < 1:
                try: candidates.append(BinaryCalibration(q,f,n).prevalence())
                except ValueError: pass
    if not candidates:
        raise ValueError("No identifiable feasible calibration in the specified box")
    return min(candidates),max(candidates)

def hoeffding_halfwidth(n: int, alpha:float, false_positive:float,
                        false_negative:float) -> float:
    if n < 1 or not (0 < alpha < 1):
        raise ValueError("Require n>=1 and 0<alpha<1")
    gap=1-false_positive-false_negative
    if gap <= 0: raise ValueError("No positive calibration discrimination")
    return sqrt(log(2/alpha)/(2*n))/gap

def transport_effect(prevalence:float, *, mechanism_flipped:bool=False)->float:
    """P(Y=1|do(A=1)) for Y=A XOR B or its flipped mechanism."""
    if not 0 <= prevalence <= 1: raise ValueError("Invalid prevalence")
    return prevalence if mechanism_flipped else 1-prevalence
