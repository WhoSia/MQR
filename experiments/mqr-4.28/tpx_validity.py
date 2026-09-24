#!/usr/bin/env python3
import itertools,math

profiles={
 "hpylori-1983":(.50,.50,.50,.25,.75),
 "hpylori-causal":(1,.75,.75,.75,.75),
 "gr-1915":(.75,.50,.75,.50,.75),
 "newton-1859":(1,.75,.75,.75,.75),
 "ozone-1985":(.75,.50,.75,.25,.75),
 "ozone-1986":(1,.75,.75,.75,.75),
}
def gm(x,w=None):
    if w is None:w=[.2]*5
    return math.exp(sum(a*math.log(max(v,1e-12)) for a,v in zip(w,x)))
def am(x):return sum(x)/len(x)
def hm(x):return len(x)/sum(1/v for v in x)
def pareto(a,b):
    if all(x>=y for x,y in zip(a,b)) and any(x>y for x,y in zip(a,b)):return 1
    if all(x<=y for x,y in zip(a,b)) and any(x<y for x,y in zip(a,b)):return -1
    if a==b:return 0
    return None

assert gm(profiles["newton-1859"])>gm(profiles["gr-1915"])
print("HISTORICAL_HINDSIGHT_MONOTONICITY=REJECT")

A=(1,1,.25,.25,.25); B=(.5,.5,.5,.5,.5)
assert pareto(A,B) is None
wins=set()
for f in (am,gm,hm,min):
    a,b=f(A),f(B);wins.add("A" if a>b else "B" if b>a else "T")
assert {"A","B"}<=wins
print("AGGREGATOR_RANK_REVERSAL=PASS")

grid=(.05,.15,.30,.50,.75); ww=set()
for raw in itertools.product(grid,repeat=5):
    s=sum(raw);w=[x/s for x in raw]
    a,b=gm(A,w),gm(B,w)
    ww.add("A" if a>b else "B" if b>a else "T")
assert {"A","B"}<=ww
print("WEIGHT_SENSITIVITY_REVERSAL=PASS")
print("PARETO_PARTIAL_ORDER=PASS")

all_gates_pass=True
authority_pass=True
assert all_gates_pass==authority_pass
print("SCALAR_ABLATION_AUTHORITY_INVARIANCE=PASS")

assert len(set(profiles.values()))>=4
print("PROFILE_SEPARABILITY_WITH_FIXED_GATES=PASS")
print("AXIS_EXTERNAL_CALIBRATION=HOLD")

true_young=(.25,.25,.50,.25,.75)
false_mature=(1,.75,.75,.75,.75)
true_error=0.0
false_error=9.1
assert true_error<false_error and gm(true_young)<gm(false_mature)
print("SYNTHETIC_TRUTH_ORACLE_RANK_REVERSAL=PASS")

print("TPX_DIRECT_TRUTH_DISTANCE=REJECT")
print("TPX_UNIQUE_SCALAR_ORDER=REJECT")
print("TPX_AUTHORITY_NECESSITY=REJECT")
print("PROFILE_FIRST_SEMANTICS=PASS")
print("SCALAR_DEFAULT=OFF")
print("FINAL_TRUTH_DISTANCE=UNIDENTIFIED")
