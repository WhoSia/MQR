"""MQR 5.4 / Chat 45 R58: exact CHSH and postselection toy model.

Reconstruction of established results, not quantum-device data.
All arithmetic is rational.
"""
from fractions import Fraction as F
from itertools import product

SETTINGS = tuple(product((0, 1), repeat=2))
ASSIGNMENTS = tuple(product((-1, 1), repeat=4))


def chsh(correlations):
    return correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)]


def local_correlations(assignment):
    a0, a1, b0, b1 = assignment
    return {(0, 0): a0*b0, (0, 1): a0*b1,
            (1, 0): a1*b0, (1, 1): a1*b1}


def pr_pair_distribution(x, y):
    """P(a,b|x,y): independent uniform marginals, parity (-1)^(xy)."""
    return {(a, b): F(1, 2) if a*b == (-1)**(x*y) else F(0)
            for a, b in product((-1, 1), repeat=2)}


def correlations_from_pair_distributions(table):
    return {(x, y): sum(F(a*b)*p for (a, b), p in table[(x, y)].items())
            for x, y in SETTINGS}


def selected_classical_pair_distribution(x, y):
    """Toy GLOBAL postselection using both settings and outcomes.

    This is NOT a realistic local-detection mechanism. It illustrates why
    retrospective cross-site outcome-dependent selection spoils inference.
    """
    accepted = []
    for z in ASSIGNMENTS:
        a = z[x]
        b = z[2+y]
        if a*b == (-1)**(x*y):
            accepted.append((a, b))
    assert len(accepted) == 8
    return {(a, b): F(accepted.count((a, b)), len(accepted))
            for a, b in product((-1, 1), repeat=2)}


def isotropic_pr(eta):
    """PR mixed with uniform box; eta in [0,1]."""
    assert F(0) <= eta <= F(1)
    result = {}
    for x, y in SETTINGS:
        raw = pr_pair_distribution(x, y)
        result[(x, y)] = {ab: (1-eta)*p + eta*F(1, 4)
                          for ab, p in raw.items()}
    return result


def verify():
    assert len(ASSIGNMENTS) == 16
    assert {chsh(local_correlations(z)) for z in ASSIGNMENTS} == {-2, 2}
    pr = {(x,y): pr_pair_distribution(x,y) for x,y in SETTINGS}
    for (x,y), pairs in pr.items():
        assert sum(pairs.values()) == 1
        assert all(sum(p for (aa,b),p in pairs.items() if aa == a) == F(1,2)
                   for a in (-1,1))
        assert all(sum(p for (a,bb),p in pairs.items() if bb == b) == F(1,2)
                   for b in (-1,1))
    assert chsh(correlations_from_pair_distributions(pr)) == 4
    assert not any(all(local_correlations(z)[xy] == (-1)**(xy[0]*xy[1])
                       for xy in SETTINGS) for z in ASSIGNMENTS)
    for eta in (F(0), F(1,4), F(1,2), F(3,4), F(1)):
        assert chsh(correlations_from_pair_distributions(isotropic_pr(eta))) == 4*(1-eta)
    unsel = {xy: sum(F(local_correlations(z)[xy],16) for z in ASSIGNMENTS)
             for xy in SETTINGS}
    assert chsh(unsel) == 0
    selected = {xy: selected_classical_pair_distribution(*xy) for xy in SETTINGS}
    assert selected == pr
    assert chsh(correlations_from_pair_distributions(selected)) == 4
    # Any selection made independently of settings leaves a local mixture.
    for i in range(1, 16):
        selected_z = ASSIGNMENTS[:i]
        means = {xy: sum(F(local_correlations(z)[xy], i) for z in selected_z)
                 for xy in SETTINGS}
        assert abs(chsh(means)) <= 2
    return {"global_assignments": 16, "local_CHSH_abs_max": 2,
            "PR_CHSH": 4, "selected_classical_CHSH": 4,
            "selected_acceptance_each_context": "1/2",
            "isotropic_PR_eta_half_CHSH": "2"}


if __name__ == "__main__":
    print(verify())
