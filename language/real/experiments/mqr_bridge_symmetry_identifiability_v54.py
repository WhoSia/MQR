"""Finite permutation symmetry limits unique cross-language identification.

Two languages have equally likely three labels. Paired anchors are explicitly
additional evidence, not consequences of matching marginal frequencies.
"""
from itertools import permutations
from fractions import Fraction

A=(0,1,2)
B=("red","green","blue")

def candidate_bridges(anchors=()):
    assert all(a in A and b in B for a,b in anchors)
    return [dict(zip(A,perm)) for perm in permutations(B)
            if all(perm[a]==b for a,b in anchors)]

def verify():
    prior=candidate_bridges()
    one=candidate_bridges(((0,"red"),))
    two=candidate_bridges(((0,"red"),(1,"blue")))
    assert (len(prior),len(one),len(two)) == (6,2,1)
    assert all(set(f.keys())==set(A) and set(f.values())==set(B) for f in prior)
    assert candidate_bridges(((0,"red"),(0,"blue"))) == []
    assert Fraction(1,3) == Fraction(1,len(A))
    return "PASS: 6 symmetry-related maps; one anchor leaves 2; two anchors identify 1; conflicting anchors 0"

if __name__=="__main__":
    print(verify())
