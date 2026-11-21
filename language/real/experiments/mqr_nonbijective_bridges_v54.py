"""Finite non-bijective cross-science bridge test: deterministic coarsening.

Three equiprobable source states, two target categories. No semantic identity claim.
"""
from fractions import Fraction
from itertools import product

A = (0, 1, 2)
B = ("left", "right")


def all_maps():
    return [dict(zip(A, bs)) for bs in product(B, repeat=len(A))]


def target_probabilities(f):
    return {b: sum(Fraction(1, 3) for a in A if f[a] == b) for b in B}


def identified(preferred=(Fraction(2, 3), Fraction(1, 3)), anchors=()):
    return [f for f in all_maps()
            if tuple(target_probabilities(f)[b] for b in B) == preferred
            and all(f[a] == b for a, b in anchors)]


def conditional_entropy_preimage(f):
    # For a size-2 and size-1 preimage, conditional H(A|B)=2/3 bit exactly.
    sizes = [sum(f[a] == b for a in A) for b in B]
    assert sorted(sizes) == [1, 2]
    return Fraction(2, 3)


def verify():
    f0 = identified()
    f1 = identified(anchors=((0, "left"),))
    f2 = identified(anchors=((0, "left"), (1, "left")))
    assert (len(f0), len(f1), len(f2)) == (3, 2, 1)
    assert f2[0] == {0: "left", 1: "left", 2: "right"}
    assert not identified(anchors=((0, "left"), (1, "left"), (2, "left")))
    assert all(conditional_entropy_preimage(f) == Fraction(2, 3) for f in f0)
    assert all(len(set(f.values())) == 2 for f in f0)
    assert len({f[0] for f in f0}) == 2
    return 'PASS nonbijective: 3->2->1 candidate coarsenings, H(A|B)=2/3 bits'

if __name__ == '__main__':
    print(verify())
