"""A simple selection-reward reversal between epistemic yield and prize incentives.

Not a replication of Gross & Bergstrom or an admissions policy model.
"""
from fractions import Fraction as F

SAFE_GAIN = F(1)
RISK_SUCCESS_GAIN = F(3)
RISK_SUCCESS_PROB = F(1, 4)
RIVAL_FIXED_SCORE = F(2)

def payoffs(prize):
    prize = F(prize)
    assert prize >= 0
    safe_win = int(SAFE_GAIN > RIVAL_FIXED_SCORE)
    risky_win = int(RISK_SUCCESS_GAIN > RIVAL_FIXED_SCORE)
    safe_value = SAFE_GAIN + prize * safe_win
    risky_yield = RISK_SUCCESS_PROB * RISK_SUCCESS_GAIN
    risky_value = risky_yield + prize * RISK_SUCCESS_PROB * risky_win
    return safe_value, risky_value

def verify():
    assert payoffs(0) == (F(1), F(3,4))
    assert payoffs(1) == (F(1), F(1))
    assert payoffs(2) == (F(1), F(5,4))
    assert payoffs(F(1,2))[0] > payoffs(F(1,2))[1]
    assert payoffs(3)[1] > payoffs(3)[0]
    return 'PASS: prize threshold 1; safe epistemic return 1 > risky 3/4, but prize 2 induces risky'

if __name__ == '__main__':
    print(verify())
