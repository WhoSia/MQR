"""Finite exact examples for limited-information science and selection.

No real admissions data or people. Conceptual demonstration, not advice for gaming selection.
"""
from fractions import Fraction
from math import log2

Q = Fraction(1, 4)

def unconditional():
    return {(a, b): Q for a in (0, 1) for b in (0, 1)}

def admission():
    prior = unconditional()
    accepted = {(a,b): w for (a,b),w in prior.items() if (a or b)}
    norm = sum(accepted.values())
    return {pair: w/norm for pair,w in accepted.items()}

def moments(dist):
    ex = sum(Fraction(a)*p for (a,b), p in dist.items())
    ey = sum(Fraction(b)*p for (a,b), p in dist.items())
    exy = sum(Fraction(a*b)*p for (a,b), p in dist.items())
    vx = ex*(1-ex)
    vy = ey*(1-ey)
    return exy-ex*ey, vx, vy

# Three toy hypotheses consistent with the initial seed 2-4-6.
def hypotheses(triple):
    a, b, c = triple
    return (
        a < b < c,                # strictly increasing
        b-a == c-b,              # arithmetic progression
        all(v % 2 == 0 for v in triple), # all-even
    )

def binary_information_gain(outcomes):
    """Uniform prior over 3 hypotheses; a binary feedback channel."""
    n = len(outcomes)
    yes = sum(outcomes)
    no = n-yes
    if yes in (0, n):
        return 0.0
    p = yes/n
    return -p*log2(p) -(1-p)*log2(1-p)

def verify():
    c0,vx0,vy0 = moments(unconditional())
    assert (c0,vx0,vy0) == (0,Fraction(1,4),Fraction(1,4))
    c,vx,vy = moments(admission())
    assert (c,vx,vy) == (-Fraction(1,9),Fraction(2,9),Fraction(2,9))
    assert c*c == vx*vy/Fraction(4)  # corr=-1/2
    assert sum(admission().values()) == 1
    assert hypotheses((2,4,6)) == (True,True,True)
    assert hypotheses((3,5,7)) == (True,True,False)
    assert hypotheses((3,5,8)) == (True,False,False)
    assert binary_information_gain(hypotheses((2,4,6))) == 0.0
    assert abs(binary_information_gain(hypotheses((3,5,8))) - 0.9182958340544896) < 1e-12
    return 'PASS: exact collider correlation -1/2; rule-query info 0 vs 0.9183 bits'

if __name__ == '__main__':
    print(verify())
