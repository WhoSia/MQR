"""MQR 5.4 chat44: proof/criticism versus menu expansion in inquiry.

Synthetic decision-theoretic counterexample. Not historical or empirical evidence.
Python 3 standard library only; exact rational arithmetic.
"""
from fractions import Fraction as F

THETA = (0, 1)
PRIOR = {0: F(1, 2), 1: F(1, 2)}
GOOD = {0: {0: F(3, 4), 1: F(1, 4)},
        1: {0: F(1, 4), 1: F(3, 4)}}
DECOY = {0: {"shiny": F(1)}, 1: {"shiny": F(1)}}
EXPERIMENTS = {"good": GOOD, "decoy": DECOY}

def check_kernel(kernel):
    assert set(kernel) == set(THETA)
    for theta in THETA:
        assert all(p >= 0 for p in kernel[theta].values())
        assert sum(kernel[theta].values(), F(0)) == 1

def expected_bayes_accuracy(kernel):
    """Optimal classification of theta given one experimental result."""
    check_kernel(kernel)
    outcomes = {y for conditional in kernel.values() for y in conditional}
    return sum(
        max(PRIOR[t] * kernel[t].get(y, F(0)) for t in THETA)
        for y in outcomes
    )

def optimum(available):
    return max(expected_bayes_accuracy(EXPERIMENTS[a]) for a in available)

def salience_policy(available):
    """A deliberately bad choice rule; illustrative only."""
    salience = {"good": 1, "decoy": 2}
    chosen = max(available, key=lambda a: salience[a])
    return chosen, expected_bayes_accuracy(EXPERIMENTS[chosen])

def run_checks():
    assert expected_bayes_accuracy(GOOD) == F(3, 4)
    assert expected_bayes_accuracy(DECOY) == F(1, 2)
    assert optimum({"good"}) == F(3, 4)
    assert optimum({"good", "decoy"}) == F(3, 4)
    assert salience_policy({"good"}) == ("good", F(3, 4))
    assert salience_policy({"good", "decoy"}) == ("decoy", F(1, 2))
    # Geometrical negative control: two disjoint cube-boundary components.
    one_cube = (8, 12, 6)
    two_components = tuple(2 * z for z in one_cube)
    assert one_cube[0] - one_cube[1] + one_cube[2] == 2
    assert two_components == (16, 24, 12)
    assert two_components[0] - two_components[1] + two_components[2] == 4
    return True

if __name__ == "__main__":
    assert run_checks()
    print("PASS: optimal set expansion monotone; realized salience-choice accuracy declines")
