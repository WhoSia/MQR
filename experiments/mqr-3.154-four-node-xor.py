"""MQR-3.154 four-node quotient-composition stress test.

World:
    X1, X2 ~ iid Bernoulli(1/2)
    X3 = X1 XOR X2
    X4 = X3 XOR U4, U4 ~ Bernoulli(0.1)

The script demonstrates that atomic interventions on X1 or X2 are null at X4,
while joint interventions reveal a strong interaction. It is intentionally small:
the scientific claim lives in the receipts, not in a large simulation stack.
"""

from collections import Counter
from math import log2


def world(intervention=None):
    intervention = intervention or {}
    out = Counter()
    for x1 in ([intervention[1]] if 1 in intervention else [0, 1]):
        p1 = 1.0 if 1 in intervention else 0.5
        for x2 in ([intervention[2]] if 2 in intervention else [0, 1]):
            p2 = 1.0 if 2 in intervention else 0.5
            x3 = intervention.get(3, x1 ^ x2)
            for u4, pu4 in ((0, 0.9), (1, 0.1)):
                x4 = intervention.get(4, x3 ^ u4)
                out[(x1, x2, x3, x4)] += p1 * p2 * pu4
    return out


def p_x4_one(intervention=None):
    d = world(intervention)
    return sum(p for state, p in d.items() if state[3] == 1)


def mutual_information(indices_a, index_b=3):
    if isinstance(indices_a, int):
        indices_a = (indices_a,)
    d = world()
    pa, pb, pab = Counter(), Counter(), Counter()
    for state, p in d.items():
        a = tuple(state[i] for i in indices_a)
        b = state[index_b]
        pa[a] += p
        pb[b] += p
        pab[(a, b)] += p
    return sum(
        p * log2(p / (pa[a] * pb[b]))
        for (a, b), p in pab.items()
        if p > 0
    )


def main():
    probes = {
        "baseline": {},
        "do(X1=1)": {1: 1},
        "do(X2=1)": {2: 1},
        "do(X1=0,X2=0)": {1: 0, 2: 0},
        "do(X1=0,X2=1)": {1: 0, 2: 1},
        "do(X1=1,X2=0)": {1: 1, 2: 0},
        "do(X1=1,X2=1)": {1: 1, 2: 1},
    }
    for name, intervention in probes.items():
        print(f"{name:18s} P(X4=1)={p_x4_one(intervention):.3f}")

    print(f"I(X1;X4)={mutual_information(0):.6f} bits")
    print(f"I(X2;X4)={mutual_information(1):.6f} bits")
    print(f"I((X1,X2);X4)={mutual_information((0, 1)):.6f} bits")

    assert abs(p_x4_one({1: 1}) - 0.5) < 1e-12
    assert abs(p_x4_one({2: 1}) - 0.5) < 1e-12
    assert abs(p_x4_one({1: 1, 2: 1}) - 0.1) < 1e-12
    assert abs(p_x4_one({1: 1, 2: 0}) - 0.9) < 1e-12
    assert mutual_information(0) < 1e-12
    assert mutual_information(1) < 1e-12
    assert abs(mutual_information((0, 1)) - 0.5310044064107188) < 1e-12


if __name__ == "__main__":
    main()
