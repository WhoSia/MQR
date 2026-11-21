"""Exact synthetic tests of epistemic strategy tradeoffs, MQR 5.4.

Not an empirical admissions model, nor a replication of Dubova et al. 2026.
"""
from fractions import Fraction as F
from itertools import product

def target_vs_random(budget, sites=4):
    """Known diagnostic location yields certain identification by targeting.

    A hidden novelty is located in one of 'sites' equally likely sites.
    The targeted diagnostic site is conditioned to be outside novelty's site.
    Independent uniform site draws detect novelty by at least one visit.
    """
    assert budget >= 0 and sites >= 2
    p = 1 - F(sites-1, sites)**budget
    return {
        "known_targeted": F(1) if budget >= 1 else F(0),
        "known_random": p,
        "novelty_random": p,
        "novelty_targeted_outside": F(0),
    }

def correlated_reports_posteriors(n, reliability=F(3,4)):
    """Symmetric equal-prior binary truth, n identical positive reports.

    'independent' is an intentionally incorrect inference when reports
    repeat one original observation.
    """
    assert n >= 1 and F(1,2) < reliability < F(1)
    odds = reliability/(1-reliability)
    return odds**n/(1+odds**n), reliability

def partitions():
    """Four worlds and two nonnested binary observations."""
    W = (0,1,2,3)
    a = lambda w: w//2
    b = lambda w: w%2
    def fiber(f):
        return {key:frozenset(w for w in W if f(w)==key)
                for key in set(f(w) for w in W)}
    return fiber(a),fiber(b),fiber(lambda w:(a(w),b(w)))

def verify():
    for n in range(1,9):
        x=target_vs_random(n,4)
        assert x["known_targeted"] == 1
        assert x["known_random"] < x["known_targeted"]
        assert x["novelty_random"] > x["novelty_targeted_outside"]
        assert x["novelty_random"] == 1-F(3,4)**n
    assert target_vs_random(4,4)["novelty_random"] == F(175,256)
    a,b,c=partitions()
    assert len(a)==len(b)==2 and len(c)==4
    assert set().union(*a.values()) == {0,1,2,3}
    assert all(len(c[(i,j)]) == 1 for i,j in product((0,1),repeat=2))
    assert correlated_reports_posteriors(1) == (F(3,4),F(3,4))
    assert correlated_reports_posteriors(4) == (F(81,82),F(3,4))
    assert correlated_reports_posteriors(8)[0] > correlated_reports_posteriors(4)[0]
    assert correlated_reports_posteriors(8)[1] == F(3,4)
    return "PASS: known vs unknown targeting; shared-ancestor overconfidence; partition refinement"

if __name__ == "__main__":
    print(verify())
