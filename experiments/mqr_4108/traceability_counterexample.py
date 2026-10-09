"""MQR 4.108 P1: finite exact shared-reference metrology court.
Synthetic population, not Regnault or SNO data. Python stdlib only.
"""
from fractions import Fraction as F
from itertools import product
def sample_mean(x): return sum(x,F(0))/len(x)
# Independent fair Rademacher reference bias and two readout errors.
# Each b +/-2, ea +/-1, eb +/-1. Two physically different channels
# share b; their difference never contains b.
worlds=[(F(b),F(a),F(c)) for b,a,c in product((-2,2),(-1,1),(-1,1))]
y=[(b+a,b+c) for b,a,c in worlds]
diff=[a-c for b,a,c in worlds]
est=[(a+c)/2+b for b,a,c in worlds]
avg=lambda a:sum(a,F(0))/len(a)
var=lambda a:avg([(z-avg(a))**2 for z in a])
assert var(diff)==2
assert var(est)==F(9,2) # shared reference variance 4 + instrument average noise 1/2
assert var(est)!=F(5,2) # naive independence of marginal channels would imply 2.5
# Perfectly agreeing sensors can be jointly wrong: choose ea=eb=0 and b nonzero.
for b in (-2,2):
    assert F(10)+b==F(10)+b and F(10)+b!=F(10)
# A truly independently traced reference C = T + ec gives C-vs-A
# contrast b + ea - ec; if C shares b, it cancels, just like A-vs-B.
assert all((b+a)-(b+c)==a-c for b,a,c in worlds)
print("PASS 8 exact worlds; Var(A-B)=",var(diff),
      "Var((A+B)/2 - T)=",var(est))
print("CANCELLED shared error in A-B does not certify absolute target validity")
print("Independent third reference requires its own traceability/uncertainty proof")
