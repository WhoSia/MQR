"""MQR 5.4 — controlled preparation mixtures as order-effect probes.

A deterministic finite laboratory model, NOT physical experimental data.
All frequencies are exact Fractions and all state identities are analyst-given.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product


@dataclass(frozen=True)
class NativeLabPair:
    a: tuple
    b: tuple
    after_a: tuple
    after_b: tuple

    def __post_init__(self):
        n = len(self.a)
        if not n or len(self.b) != n or len(self.after_a) != n or len(self.after_b) != n:
            raise ValueError("All maps must have the same nonzero domain")
        if any(type(v) is not int or v < 0 or v >= n for v in self.after_a + self.after_b):
            raise ValueError("State-transition targets must be valid integer state indices")

    def read(self, s, order):
        if not isinstance(s, int) or s not in range(len(self.a)):
            raise ValueError("Invalid preparation state")
        if order == "AB":
            return self.a[s], self.b[self.after_a[s]]
        if order == "BA":
            return self.a[self.after_b[s]], self.b[s]
        raise ValueError("Order must be AB or BA")


def exact_mixture(pair, order, weights):
    n = len(pair.a)
    if len(weights) != n:
        raise ValueError("One preparation weight per state is required")
    try:
        weights = tuple(Fraction(w) for w in weights)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError("Invalid preparation weight") from exc
    if any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError("Weights must be nonnegative and sum to one")
    out = {}
    for s, weight in enumerate(weights):
        if weight:
            signature = pair.read(s, order)
            out[signature] = out.get(signature, Fraction(0)) + weight
    return out


def total_variation(p, q):
    return sum((abs(p.get(k, Fraction(0)) - q.get(k, Fraction(0)))
                for k in p.keys() | q.keys()), Fraction(0)) / 2


def order_gap(pair, weights):
    return total_variation(exact_mixture(pair, "AB", weights),
                           exact_mixture(pair, "BA", weights))


def pointwise_order_equal(pair):
    return all(pair.read(s, "AB") == pair.read(s, "BA")
               for s in range(len(pair.a)))


def rank_exact(rows):
    """Gaussian rank over Q, without floating-point tolerance assumptions."""
    if not rows:
        return 0
    n = len(rows[0])
    if any(len(row) != n for row in rows):
        raise ValueError("Nonrectangular matrix")
    a = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        div = a[rank][col]
        a[rank] = [x / div for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                t = a[i][col]
                a[i] = [x - t * y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def certified_mixture_family_identifies_pointwise(pair, rows):
    """Sufficient criterion, under fixed readout and transition kernels.

    This is not a claim that the named states can be controlled physically.
    """
    n = len(pair.a)
    if not rows:
        return False
    for weights in rows:
        exact_mixture(pair, "AB", weights)
        exact_mixture(pair, "BA", weights)
    return rank_exact(rows) == n and all(order_gap(pair, w) == 0 for w in rows)


def balanced_masking_pair():
    return NativeLabPair((0, 1), (0, 1), (1, 0), (1, 0))


def nondisturbing_pooled_rival():
    return NativeLabPair((0, 1), (1, 0), (0, 1), (0, 1))
