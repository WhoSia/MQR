#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, itertools, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RDIR=ROOT/"language"/"r"
spec=importlib.util.spec_from_file_location("rpacket",RDIR/"rpacket.py")
rp=importlib.util.module_from_spec(spec); spec.loader.exec_module(rp)

packets=[rp.parse(p) for p in sorted((RDIR/"examples").glob("*.rpacket"))]
by={p["id"]:p for p in packets}

def coords(p):
    return tuple(p["truth_proximity"]["TPP"][a] for a in ("W","N","I","T","D"))

def gm(x,w=None):
    if w is None: w=[1/len(x)]*len(x)
    return math.exp(sum(wi*math.log(max(v,1e-12)) for v,wi in zip(x,w)))

def am(x): return sum(x)/len(x)
def hm(x): return len(x)/sum(1/v for v in x)
def pareto(a,b):
    ge=all(x>=y for x,y in zip(a,b)); le=all(x<=y for x,y in zip(a,b))
    gt=any(x>y for x,y in zip(a,b)); lt=any(x<y for x,y in zip(a,b))
    if ge and gt: return "A_DOMINATES"
    if le and lt: return "B_DOMINATES"
    if a==b: return "EQUAL"
    return "INCOMPARABLE"

# A1 Historical rank-reversal / hindsight firewall.
newton=by["newton-mercury-1859"]["truth_proximity"]["TPX"]
gr=by["newton-gr-1915"]["truth_proximity"]["TPX"]
assert newton>gr
print(f"HISTORICAL_CONTEMPORARY_TPX_NEWTON1859={newton}")
print(f"HISTORICAL_CONTEMPORARY_TPX_GR1915={gr}")
print("SUCCESSOR_JUDGMENT=GR_CONTRACTS_NEWTON_FINAL_LAW_AUTHORITY")
print("RETROSPECTIVE_TRUTHLIKELINESS_MONOTONICITY=FAIL")
print("A1_HISTORICAL_RANK_REVERSAL_ATTACK=PASS")

# Current corpus happens to be Pareto-chain robust.
for a,b in itertools.combinations(packets,2):
    pa,pb=coords(a),coords(b)
    rel=pareto(pa,pb)
    print(f"CORPUS_PAIR {a['id']} {b['id']} {rel}")

# A2/A3: crossing profiles expose aggregation and weight underdetermination.
A=(1.0,1.0,0.25,0.25,0.25)
B=(0.5,0.5,0.5,0.5,0.5)
assert pareto(A,B)=="INCOMPARABLE"
agg={
 "arithmetic":(am(A),am(B)),
 "geometric":(gm(A),gm(B)),
 "harmonic":(hm(A),hm(B)),
 "minimum":(min(A),min(B)),
}
for k,(x,y) in agg.items():
    print(f"AGGREGATOR {k} A={x:.6f} B={y:.6f} WINNER={'A' if x>y else 'B' if y>x else 'TIE'}")
winners={('A' if x>y else 'B' if y>x else 'TIE') for x,y in agg.values()}
assert 'A' in winners and 'B' in winners
print("AGGREGATOR_RANK_REVERSAL=PASS")

# Broad positive weight grid; normalize to simplex.
grid=[0.05,0.15,0.30,0.50,0.75]
seen=set(); witnesses=[]
for raw in itertools.product(grid,repeat=5):
    s=sum(raw); w=tuple(x/s for x in raw)
    sa,sb=gm(A,w),gm(B,w)
    win='A' if sa>sb else 'B' if sb>sa else 'TIE'
    seen.add(win)
    if len(witnesses)<8 and win in ('A','B'):
        witnesses.append((win,w,sa,sb))
assert 'A' in seen and 'B' in seen
for win,w,sa,sb in witnesses:
    print("WEIGHT_WITNESS",win,",".join(f"{x:.4f}" for x in w),f"{sa:.6f}",f"{sb:.6f}")
print("A2_AXIS_WEIGHT_UNDERDETERMINATION=PASS")
print("A3_PARETO_PARTIAL_ORDER=PASS")

# A4 Scalar ablation: scientific gate decisions do not use TPX.
for p in packets:
    gate_decision=all(p["gates"][g]=="PASS" for g in ("C","E","P","R"))
    authority_decision=(p["authority"]["state"]=="SCOPED_REALIST_AUTHORITY")
    assert gate_decision==authority_decision
    # shocks/residue are serialized independently of scalar.
    assert "successor_shocks" in p and "residue" in p
print("A4_SCALAR_ABLATION_DECISION_INVARIANCE=PASS")

# A5 axes are not mere copies of gates: all gates fixed PASS but profiles vary materially.
assert all(all(p["gates"][g]=="PASS" for g in ("C","E","P","R")) for p in packets)
unique={coords(p) for p in packets}
assert len(unique)>=4
print(f"A5_FIXED_GATES_UNIQUE_PROFILES={len(unique)}")
print("A5_PROFILE_NOT_LITERAL_GATE_DUPLICATION=PASS")
print("A5_INDEPENDENT_AXIS_CALIBRATION=HOLD")

# A6 Synthetic truth-oracle sandbox.
# True world: f(x)=x on 0..9.
def truth(x): return x
def h_true(x): return x
def h_false_mature(x): return x if x<9 else 100

def oracle_mae(h):
    return sum(abs(h(x)-truth(x)) for x in range(10))/10

# Mechanically derived process profile: each coordinate is evidential-process maturity,
# not access to the hidden oracle.
def proc_profile(test_coverage, independent_routes, rival_pressure, transport, defeat_routes):
    return (
        min(1.0,test_coverage),
        min(1.0,independent_routes),
        min(1.0,rival_pressure),
        min(1.0,transport),
        min(1.0,defeat_routes),
    )

young_true=proc_profile(0.25,0.25,0.50,0.25,0.75)
mature_false=proc_profile(1.00,0.75,0.75,0.75,0.75)
true_tpx=gm(young_true); false_tpx=gm(mature_false)
true_err=oracle_mae(h_true); false_err=oracle_mae(h_false_mature)
print(f"SYNTH_TRUE TPX={true_tpx:.6f} ORACLE_MAE={true_err:.6f}")
print(f"SYNTH_FALSE_MATURE TPX={false_tpx:.6f} ORACLE_MAE={false_err:.6f}")
assert true_err < false_err and true_tpx < false_tpx
print("SYNTHETIC_ORACLE_TRUTH_RANK_REVERSAL=PASS")
print("A6_TPX_AS_DIRECT_TRUTH_DISTANCE=FAIL")
print("A6_TPX_AS_EPISTEMIC_MATURITY_SUMMARY=CONSISTENT")

# Final adjudication.
print("TPX_TRUTH_PROXIMITY_CONSTRUCT_VALIDITY=FAIL")
print("TPX_UNIQUE_SCALAR_IDENTIFICATION=FAIL")
print("TPX_SCIENTIFIC_AUTHORITY_NECESSITY=FAIL")
print("PROFILE_DIAGNOSTIC_SEPARABILITY=PASS")
print("PARETO_ORDERING_WITHOUT_WEIGHT_CALIBRATION=PASS")
print("SCALAR_PROJECTION_DEFAULT=OFF")
print("FINAL_TRUTH_DISTANCE=UNIDENTIFIED")
print("REAL_LANGUAGE_V0_2_PROFILE_FIRST=RECOMMENDED")
