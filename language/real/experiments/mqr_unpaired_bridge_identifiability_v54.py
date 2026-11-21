"""MQR 5.4: unpaired marginals do not fix a cross-science observational bridge.

All probability measures here are synthetic. "Worlds" are constructed fixtures.
No claim is made that these distributions describe historical sciences.
"""
from fractions import Fraction
from itertools import product

ZERO = Fraction(0)
HALF = Fraction(1, 2)
QUARTER = Fraction(1, 4)

def marginals(joint):
    assert set(joint) == set(product((0, 1), repeat=2))
    assert all(p >= ZERO for p in joint.values())
    assert sum(joint.values(), ZERO) == 1
    left = {a: sum((joint[a, b] for b in (0, 1)), ZERO) for a in (0, 1)}
    right = {b: sum((joint[a, b] for a in (0, 1)), ZERO) for b in (0, 1)}
    return left, right

def coupling(t):
    """All symmetric binary couplings with uniform marginals, for 0<=t<=1/2."""
    assert ZERO <= t <= HALF
    return {(0, 0): t, (0, 1): HALF-t,
            (1, 0): HALF-t, (1, 1): t}

def fibers(signature):
    """Partition four equiprobable hidden worlds by observation signature."""
    out = {}
    for w in range(4):
        out.setdefault(signature(w), []).append(w)
    return tuple(sorted(tuple(values) for values in out.values()))

def verify():
    independent = coupling(QUARTER)
    equal = coupling(HALF)
    opposite = coupling(ZERO)
    assert independent != equal != opposite
    assert all(marginals(p) == ({0: HALF, 1: HALF}, {0: HALF, 1: HALF})
               for p in (independent, equal, opposite))
    assert fibers(lambda w: w // 2) == ((0, 1), (2, 3))
    assert fibers(lambda w: w % 2) == ((0, 2), (1, 3))
    assert fibers(lambda w: (w // 2, w % 2)) == ((0,), (1,), (2,), (3,))
    assert fibers(lambda w: w // 2) != fibers(lambda w: w % 2)
    return "PASS: 3 distinct joint couplings share marginals; paired signatures refine all 4 worlds"

if __name__ == "__main__":
    print(verify())
