"""MQR 5.4 R10: forced one-bit integration can destroy target-specific predictive sufficiency.
Finite arithmetic thought experiment, NOT an actual scientific dataset or a new theorem.
"""
from itertools import product
from fractions import Fraction as F

S = tuple(product((0, 1), repeat=2))

def optimal_accuracy(law, target, code):
    """Optimal Bayes classifier on one-bit code; law: P(X,Y)."""
    return sum((max(sum(law[s] for s in S if code[s] == z and s[target] == k)
                    for k in (0,1)) for z in (0,1)), start=F(0))

def all_codes():
    for bits in product((0,1), repeat=4):
        yield dict(zip(S, bits))

def run():
    independent = {s:F(1,4) for s in S}
    coupled = {s:F(1,2) if s[0]==s[1] else F(0) for s in S}
    values = [(optimal_accuracy(independent,0,h),optimal_accuracy(independent,1,h))
              for h in all_codes()]
    assert len(values)==16
    assert max((a+b)/2 for a,b in values)==F(3,4)
    assert any(a==b==F(3,4) for a,b in values)
    assert any((a,b)==(F(1),F(1,2)) for a,b in values)
    assert all(a+b<=F(3,2) for a,b in values)
    assert optimal_accuracy(independent,0,{s:s[0] for s in S})==F(1)
    assert optimal_accuracy(independent,1,{s:s[1] for s in S})==F(1)
    assert all(optimal_accuracy(coupled,t,{s:s[0] for s in S})==F(1) for t in (0,1))
    assert optimal_accuracy(independent,0,{s:0 for s in S})==F(1,2)
    assert optimal_accuracy(independent,1,{s:0 for s in S})==F(1,2)
    return values

if __name__ == "__main__":
    values=run()
    print("PASS: 16/16 one-bit codes, 9 exact assertions")
    print("forced common bit optimal two-target mean:",max((a+b)/2 for a,b in values))
