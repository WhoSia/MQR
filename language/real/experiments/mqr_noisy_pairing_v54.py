"""MQR 5.4 — specimen link reliability as a separate unknown in cross-science integration.

Exact synthetic binary distribution model, not observed physical or human research.
"""
from fractions import Fraction as F
from math import exp

HALF = F(1, 2)

def parity_rate(true_agreement_bias, correct_link_probability):
    """P(A!=B) when true corr (P(same)-P(different)) is r and correct-link chance is p.

    Incorrectly paired B is an independent random specimen with a balanced marginal.
    """
    r, p = F(true_agreement_bias), F(correct_link_probability)
    assert -1 <= r <= 1 and 0 <= p <= 1
    return (1-p*r)/2

def infer_bias(parity_observed, known_link_probability):
    p, q = F(known_link_probability), F(parity_observed)
    assert 0 < p <= 1
    inferred = (1-2*q)/p
    assert -1 <= inferred <= 1
    return inferred

def hoeffding_one_sided(n, p):
    """Bound for wrong threshold at 1/2 under true r=+/-1, iid pairs."""
    assert isinstance(n, int) and n > 0
    p=float(p)
    assert 0 <= p <= 1
    return exp(-n*p*p/2)

def verify():
    assert parity_rate(1,F(1,2)) == parity_rate(F(1,2),1) == F(1,4)
    assert parity_rate(-1,F(1,2)) == F(3,4)
    assert parity_rate(1,0) == parity_rate(-1,0) == HALF
    assert infer_bias(F(1,4),F(1,2)) == 1
    assert infer_bias(F(1,4),1) == F(1,2)
    assert parity_rate(F(0),F(1,2))==HALF
    assert hoeffding_one_sided(100,F(1,2)) < 0.000004
    return 'PASS: unknown pairing quality confounds association; p=0 erases question, p>0 permits inference if calibrated'

if __name__ == '__main__':
    print(verify())
