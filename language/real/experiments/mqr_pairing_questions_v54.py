"""MQR 5.4: paired data, causal intervention, and measurable question space.

Synthetic exact models. Does not analyze real participants or physical experiments.
"""
from fractions import Fraction as F
from itertools import product

STATES = tuple(product((0, 1), repeat=2))
HALF = F(1, 2)

def distribution(association):
    """Joint A,B with A fair; B=A or B=1-A."""
    assert association in ("same", "opposite")
    return {(a,b): HALF if (b == (a if association == "same" else 1-a)) else F(0)
            for a,b in STATES}

def marginal(p, i):
    return {x: sum(p[s] for s in STATES if s[i] == x) for x in (0,1)}

def parity(p):
    return sum(prob for (a,b),prob in p.items() if a ^ b)

def fork(do_a=None):
    """U -> A=U, U -> B=U; intervention on A leaves B tied to U."""
    return {(a,b): (HALF if (do_a is None and a == b) else F(0)) if do_a is None
            else (HALF if a == do_a else F(0)) for a,b in STATES}

def chain(do_a=None):
    """U -> A=U -> B=A; do(A) changes B."""
    if do_a is None: return distribution("same")
    return {(a,b): F(1) if a == b == do_a else F(0) for a,b in STATES}

def rank(matrix):
    """Exact rank over Q; vectors are rows."""
    if not matrix: return 0
    a = [[F(x) for x in row] for row in matrix]
    width = len(a[0]); assert all(len(row) == width for row in a)
    pivot_row = 0
    for col in range(width):
        row = next((i for i in range(pivot_row,len(a)) if a[i][col]), None)
        if row is None: continue
        a[pivot_row],a[row]=a[row],a[pivot_row]
        pivot=a[pivot_row][col]
        a[pivot_row]=[x/pivot for x in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row:
                x=a[i][col]
                a[i]=[v-x*p for v,p in zip(a[i],a[pivot_row])]
        pivot_row+=1
        if pivot_row == len(a): break
    return pivot_row

def indicator(predicate):
    return tuple(F(int(predicate(s))) for s in STATES)

BASIS_UNPAIRED=(indicator(lambda s: True), indicator(lambda s:s[0]==1),
                indicator(lambda s:s[1]==1))
BASIS_PAIRED=tuple(indicator(lambda s:s==state) for state in STATES)
PARITY_FUNCTION=indicator(lambda s:s[0]^s[1]==1)

def verify():
    same, opposite=distribution("same"), distribution("opposite")
    assert marginal(same,0)==marginal(opposite,0)=={0:HALF,1:HALF}
    assert marginal(same,1)==marginal(opposite,1)=={0:HALF,1:HALF}
    assert parity(same)==0 and parity(opposite)==1
    assert fork()==chain()==same
    assert marginal(fork(do_a=1),1)=={0:HALF,1:HALF}
    assert marginal(chain(do_a=1),1)=={0:F(0),1:F(1)}
    assert rank(BASIS_UNPAIRED)==3
    assert rank(BASIS_UNPAIRED+(PARITY_FUNCTION,))==4
    assert rank(BASIS_PAIRED)==4
    assert sum(same.values())==sum(opposite.values())==F(1)
    return "PASS: unpaired rank=3, paired rank=4, parity unidentifiable before pairing; causal intervention still needed"

if __name__=="__main__": print(verify())
