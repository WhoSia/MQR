"""A scientific interface can be informative for X but not Y, and vice versa.

All four world states (X,Y) are equiprobable. Synthetic example only.
"""
from fractions import Fraction as Q
from itertools import product

WORLDS=tuple(product((0,1),repeat=2))
PRIOR={w:Q(1,4) for w in WORLDS}


def channel_reveals(which):
    assert which in (0,1)
    return {w:{b:Q(1) if b==w[which] else Q(0) for b in (0,1)} for w in WORLDS}


def optimal_accuracy(channel, target):
    return sum(max(sum(PRIOR[w]*channel[w][signal] for w in WORLDS
                       if w[target]==value) for value in (0,1))
               for signal in (0,1))


def garbling_possible(source,target):
    # For deterministic source signals, each source-fiber must agree on target row.
    for s in (0,1):
        rows={tuple(target[w].values()) for w in WORLDS if source[w][s] == 1}
        if len(rows)>1:
            return False
    return True


def verify():
    X=channel_reveals(0)
    Y=channel_reveals(1)
    assert not garbling_possible(X,Y)
    assert not garbling_possible(Y,X)
    assert optimal_accuracy(X,0)==Q(1)
    assert optimal_accuracy(Y,0)==Q(1,2)
    assert optimal_accuracy(X,1)==Q(1,2)
    assert optimal_accuracy(Y,1)==Q(1)
    # If both channel outputs can be retained, either target is perfectly answerable.
    return 'PASS: X/Y channels incomparable; target-dependent accuracy 1 vs 1/2 (reversed)'


if __name__=='__main__':print(verify())
