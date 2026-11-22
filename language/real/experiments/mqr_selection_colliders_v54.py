"""Synthetic exact probability enumeration for selection-induced correlations."""
from fractions import Fraction as F
from itertools import product

WORLDS=tuple(product((0,1),repeat=2))
POP={w:F(1,4) for w in WORLDS}

def selected(weights):
    den=sum(POP[w]*F(weights[w]) for w in WORLDS)
    if den==0:raise ValueError('never selected')
    return {w:POP[w]*F(weights[w])/den for w in WORLDS}

def correlation(p):
    a=sum(v for (x,y),v in p.items() if x)
    b=sum(v for (x,y),v in p.items() if y)
    both=p[(1,1)]
    return both-a*b

def invert_selection(q,weights):
    assert all(F(weights[w])>0 for w in WORLDS)
    inv={w:q[w]/F(weights[w]) for w in WORLDS}
    s=sum(inv.values())
    return {w:inv[w]/s for w in WORLDS}

def verify():
    assert correlation(POP)==0
    agree={w:F(1) if w[0]==w[1] else F(0) for w in WORLDS}
    agree_q=selected(agree)
    assert agree_q=={(0,0):F(1,2),(0,1):0,(1,0):0,(1,1):F(1,2)}
    assert correlation(agree_q)==F(1,4)
    any_positive={w:int(w!=(0,0)) for w in WORLDS}
    q=selected(any_positive)
    assert correlation(q)==F(-1,9)
    soft={w:F(3,4) if w[0]==w[1] else F(1,4) for w in WORLDS}
    qs=selected(soft)
    assert correlation(qs)==F(1,8)
    assert invert_selection(qs,soft)==POP
    # Zero inclusion probabilities destroy identification under unknown base cell weights.
    alt={(0,0):F(1,8),(0,1):F(3,8),(1,0):F(3,8),(1,1):F(1,8)}
    def condition(base,weights):
        s=sum(base[w]*weights[w] for w in WORLDS)
        return {w:base[w]*weights[w]/s for w in WORLDS}
    assert condition(POP,agree)==condition(alt,agree)
    return 'PASS: zero population association; conditional covariances +1/4 and -1/9; soft selection +1/8 corrected to zero'

if __name__=='__main__':print(verify())
