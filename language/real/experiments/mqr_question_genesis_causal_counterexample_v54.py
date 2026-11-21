"""MQR 5.4 chat44: observational equivalence versus intervention divergence.
Exact fractions; synthetic causal counterexample, NOT empirical evidence.
"""
from fractions import Fraction

def distribution(model: str, action: str = "observe"):
    """Joint probability of (X,Y) under exogenous fair binary U."""
    assert model in ("cause", "common_source")
    assert action in ("observe", "do_x_0", "do_x_1")
    out = {}
    for u in (0, 1):
        x = u if action == "observe" else int(action[-1])
        y = x if model == "cause" else u
        out[x, y] = out.get((x, y), Fraction(0)) + Fraction(1, 2)
    return out

def y_one(dist):
    return sum((p for (x,y),p in dist.items() if y == 1), Fraction(0))

def verify():
    assert distribution("cause") == distribution("common_source")
    assert distribution("cause") == {(0,0):Fraction(1,2),(1,1):Fraction(1,2)}
    assert y_one(distribution("cause", "do_x_1")) == 1
    assert y_one(distribution("common_source", "do_x_1")) == Fraction(1,2)
    assert y_one(distribution("cause", "do_x_0")) == 0
    assert y_one(distribution("common_source", "do_x_0")) == Fraction(1,2)
    for m in ("cause","common_source"):
        for a in ("observe","do_x_0","do_x_1"):
            assert sum(distribution(m,a).values(), Fraction(0)) == 1
    return True

if __name__ == "__main__":
    assert verify()
    print("PASS: observation equal, interventions different, normalization exact")
