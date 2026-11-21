"""Exact two-step exploration mixture, fixed mutually exclusive objectives.

Synthetic policy model, not advice about real admissions or experiments.
"""
from fractions import Fraction as F

def success(explore, n=2, sites=4):
    """Exploitation resolves known hypothesis; exploration uniformly samples sites.

    Novel site is stipulated outside exploitation's diagnostic location.
    Return success under each goal and their equally weighted mean.
    """
    e=F(explore)
    assert 0<=e<=1 and n>=1 and sites>=2
    known=1-e**n
    novel=1-(1-e/F(sites))**n
    return known,novel,(known+novel)/2

def verify():
    optimum=F(4,17)
    assert success(0)==(F(1),F(0),F(1,2))
    assert success(1)==(F(0),F(7,16),F(7,32))
    assert success(optimum)==(F(273,289),F(33,289),F(9,17))
    assert success(optimum)[2]>success(0)[2]>success(1)[2]
    # U(e)=1/2 + e/4 - 17e^2/32; stationary point e=4/17.
    for k in range(1001):
        assert success(F(k,1000))[2]<=success(optimum)[2]
    return "PASS: e=4/17 interior optimum; utility 9/17; endpoints worse"

if __name__=="__main__":
    print(verify())
