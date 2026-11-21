"""Deterministic quotient bridge under all finite interventions.

No empirical scientific or historical claim; three-state source, two-state target.
"""
from itertools import product

A = (0, 1, 2)
B = ("L", "R")
F = {0: "L", 1: "L", 2: "R"}


def quotient_action(T):
    """Return the induced target operation or None if no such map exists."""
    action = {}
    for a in A:
        b = F[a]
        out = F[T[a]]
        if b in action and action[b] != out:
            return None
        action[b] = out
    return action


def verify():
    all_T = [dict(zip(A, outputs)) for outputs in product(A, repeat=3)]
    ok = [T for T in all_T if quotient_action(T) is not None]
    bad = [T for T in all_T if quotient_action(T) is None]
    assert (len(all_T), len(ok), len(bad)) == (27, 15, 12)
    swap01 = {0:1, 1:0, 2:2}
    swap12 = {0:0, 1:2, 2:1}
    assert quotient_action(swap01) == {"L":"L", "R":"R"}
    assert quotient_action(swap12) is None
    assert quotient_action({0:2,1:2,2:2}) == {"L":"R","R":"R"}
    for T in ok:
        G=quotient_action(T)
        assert all(F[T[a]] == G[F[a]] for a in A)
    return "PASS: 27 source actions; 15 quotient-compatible, 12 incompatible"

if __name__ == "__main__":
    print(verify())
