#!/usr/bin/env python3
"""MQR-4.121 P1B finite rational toy — chemical species != spectral data rank.

Not a reproduction of Griffiths & Potts (1974) source measurement.
No new experimental data; all four toy wavelengths and concentration vectors constructed.
"""
from fractions import Fraction as F

def rank(rows):
    a = [[F(v) for v in row] for row in rows]
    if not a: return 0
    m, n, r = len(a), len(a[0]), 0
    for j in range(n):
        p = next((i for i in range(r, m) if a[i][j]), None)
        if p is None: continue
        a[p], a[r] = a[r], a[p]
        v = a[r][j]
        a[r] = [x / v for x in a[r]]
        for i in range(m):
            if i != r:
                k = a[i][j]
                a[i] = [x - k*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m: break
    return r

# Four arbitrary spectral channels; three distinguishable endmember response columns.
E = [
    list(map(F, ["1", "1", "1.01"])),
    list(map(F, ["0.55", "1.20", "1.195"])),
    list(map(F, ["0.20", "0.82", "0.811"])),
    list(map(F, ["0.80", "1.40", "1.398"])),
]

def composition(acid, yellow_ratio):
    """Total concentration fixed at 1, three species: acid, pseudoacid, base."""
    return [acid, (1-acid)*yellow_ratio, (1-acid)*(1-yellow_ratio)]

def observation(conditions):
    return [[sum(E[w][k]*x[k] for k in range(3))
             for x in conditions] for w in range(len(E))]

def affine_rank(Y):
    return rank([[v - row[0] for v in row] for row in Y])

conditions = [composition(F(x), F(2,5))
              for x in ["0.1", "0.25", "0.4", "0.55", "0.7", "0.85"]]
restricted = affine_rank(observation(conditions))
expanded = affine_rank(observation(conditions + [composition(F("0.4"), F(1,10))]))
assert rank(E) == 3, rank(E)
assert restricted == 1, restricted
assert expanded == 2, expanded
print("toy_endmember_response_rank=3")
print("toy_constant_yellow_ratio_affine_observation_rank=1")
print("toy_changed_yellow_ratio_affine_observation_rank=2")
print("STATUS=EXACT_RATIONAL_TOY_ONLY; NOT_REAL_SPECTRAL_DATA")
