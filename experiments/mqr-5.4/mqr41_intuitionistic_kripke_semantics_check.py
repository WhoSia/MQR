"""MQR 5.4 / Chat MQR 41 — intuitionistic Kripke semantics sanity check.

Two epistemic worlds, w0 <= w1; P becomes verified at w1.
This is a formal proof-theory illustration, not a model of a real civilization.
"""
from itertools import combinations

W = (0, 1)
ORDER = {(0, 0), (0, 1), (1, 1)}
UPSETS = [
    frozenset(s)
    for n in range(3)
    for s in combinations(W, n)
    if all(w not in s or v in s for w, v in ORDER)
]
VALUATION = {"p": frozenset({1})}

def forced(formula, world):
    op = formula[0]
    if op == "p":
        return world in VALUATION["p"]
    if op == "not":
        return all(
            not forced(formula[1], future)
            for future in W if (world, future) in ORDER
        )
    if op == "or":
        return forced(formula[1], world) or forced(formula[2], world)
    if op == "and":
        return forced(formula[1], world) and forced(formula[2], world)
    raise ValueError("Unknown connective: " + op)

def test():
    p = ("p",)
    not_p = ("not", p)
    excluded_middle = ("or", p, not_p)
    not_not_p = ("not", not_p)
    assert UPSETS == [
        frozenset(), frozenset({1}), frozenset({0, 1})
    ]
    assert not forced(p, 0)
    assert not forced(not_p, 0)
    assert not forced(excluded_middle, 0)
    assert forced(excluded_middle, 1)
    # Distinguish double-negation from a naive three-valued reading:
    assert forced(not_not_p, 0)
    assert not forced(p, 0)
    # Under ordinary Boolean valuation, P or not P is true:
    assert all(bit or not bit for bit in (False, True))
    print("accessible worlds: 0<=1")
    print("P at w0/w1:", forced(p, 0), forced(p, 1))
    print("not P at w0/w1:", forced(not_p, 0), forced(not_p, 1))
    print("LEM at w0/w1:", forced(excluded_middle, 0), forced(excluded_middle, 1))
    print("double negation P at w0/w1:", forced(not_not_p, 0), forced(not_not_p, 1))
    print("PASS: excluded middle differs across consequence semantics")

if __name__ == "__main__":
    test()
