"""MQR 5.4 Chat45 R61 — postselection strength vs apparent CHSH score.

All values are exact rationals. This is a *globally coordinated, context-dependent*
filter; it is NOT an implementation of a locally independent detector loophole,
nor is it experimental Bell data.
"""
from fractions import Fraction as Q
from itertools import product

ASSIGNMENTS = list(product((-1, 1), repeat=4))
SETTINGS = list(product((0, 1), repeat=2))


def selected_context(x: int, y: int, rho: Q):
    """Accept matching product with weight 1 and mismatching with weight rho."""
    assert Q(0) <= rho <= Q(1)
    weights = {(a, b): Q(0) for a, b in product((-1, 1), repeat=2)}
    total = Q(0)
    for a0, a1, b0, b1 in ASSIGNMENTS:
        a, b = (a0, a1)[x], (b0, b1)[y]
        w = Q(1) if a*b == (-1)**(x*y) else rho
        weights[a, b] += w
        total += w
    return {ab: v/total for ab, v in weights.items()}, total/len(ASSIGNMENTS)


def score(rho: Q):
    correlations = {}
    rates = {}
    for x, y in SETTINGS:
        joint, rate = selected_context(x, y, rho)
        correlations[x, y] = sum(Q(a*b)*prob for (a, b), prob in joint.items())
        assert sum(joint.values()) == 1
        for outcome in (-1, 1):
            assert sum(p for (a, b), p in joint.items() if a == outcome) == Q(1, 2)
            assert sum(p for (a, b), p in joint.items() if b == outcome) == Q(1, 2)
        rates[x, y] = rate
    s = correlations[0, 0] + correlations[0, 1] + correlations[1, 0] - correlations[1, 1]
    assert len(set(rates.values())) == 1
    return s, rates[0, 0]


def test_exact():
    cases = {
        Q(0): (Q(4), Q(1, 2)),
        Q(1, 10): (Q(36, 11), Q(11, 20)),
        Q(1, 4): (Q(12, 5), Q(5, 8)),
        Q(1, 3): (Q(2), Q(2, 3)),
        Q(1, 2): (Q(4, 3), Q(3, 4)),
        Q(1): (Q(0), Q(1)),
    }
    for rho, expected in cases.items():
        assert score(rho) == expected
        assert score(rho) == (4*(1-rho)/(1+rho), (1+rho)/2)

    # Uniform assignments have CHSH score zero before selection.
    correlations = {}
    for x, y in SETTINGS:
        correlations[x, y] = sum(Q((a0,a1)[x]*(b0,b1)[y], 16)
                                 for a0,a1,b0,b1 in ASSIGNMENTS)
    assert all(e == 0 for e in correlations.values())

    # A setting-INDEPENDENT reweighting of deterministic hidden assignments
    # cannot exceed the local CHSH bound. Enumerate all nonempty subsets.
    for mask in range(1, 1 << 16):
        chosen = [ASSIGNMENTS[i] for i in range(16) if mask & (1 << i)]
        n = len(chosen)
        c = {xy: sum(Q((z[0],z[1])[xy[0]]*(z[2],z[3])[xy[1]], n)
                    for z in chosen) for xy in SETTINGS}
        s = c[0,0]+c[0,1]+c[1,0]-c[1,1]
        assert abs(s) <= 2

    return {"rho_boundary": "1/3", "max_selected_CHSH": "4",
            "cases": len(cases), "context_independent_subsets": 65535}


if __name__ == "__main__":
    print(test_exact())
