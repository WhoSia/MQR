#!/usr/bin/env python3
from __future__ import annotations
import csv,math,sys
from pathlib import Path

AX=["W","N","I","T","D"]
LV=["L_W","L_N","L_I","L_T","L_D"]

def rows(path):
    with Path(path).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def pearson(x,y):
    mx=sum(x)/len(x); my=sum(y)/len(y)
    dx=[a-mx for a in x]; dy=[b-my for b in y]
    den=math.sqrt(sum(a*a for a in dx)*sum(b*b for b in dy))
    return sum(a*b for a,b in zip(dx,dy))/den if den else float("nan")

if len(sys.argv)!=5:
    raise SystemExit("usage: evaluate_calibration.py HIDDEN.tsv PRED.tsv DECOY_PRED.tsv PUBLIC.tsv")

key=rows(sys.argv[1]); pred=rows(sys.argv[2]); dpred=rows(sys.argv[3]); pub=rows(sys.argv[4])
K={r["id"]:r for r in key}; P={r["id"]:r for r in pred}; DP={r["id"]:r for r in dpred}; U={r["id"]:r for r in pub}
assert K.keys()==P.keys()==DP.keys()==U.keys()

# S1 exact recovery
exact=[i for i,r in K.items() if r["lane"]=="exact"]
for i in exact:
    for a in AX:
        if abs(float(P[i][a])-float(K[i][a]))>5e-7:
            raise AssertionError(f"S1 fail {i} {a}")
print(f"S1_EXACT_RECOVERY=PASS rows={len(exact)}")

# S2/S3 exact matched interventions and no leakage
emap={}
for i in exact:
    combo=tuple(int(K[i][l]) for l in LV)
    emap[combo]=P[i]
leaks=0; monotonic_checks=0
for target in range(5):
    others=[j for j in range(5) if j!=target]
    for fixed in __import__("itertools").product(range(3),repeat=4):
        combos=[]
        for lev in range(3):
            c=[None]*5
            c[target]=lev
            for j,v in zip(others,fixed):c[j]=v
            combos.append(tuple(c))
        rr=[emap[c] for c in combos]
        vals=[float(r[AX[target]]) for r in rr]
        if not (vals[0]<vals[1]<vals[2]):
            raise AssertionError(f"S3 exact monotonic fail axis={AX[target]} fixed={fixed} vals={vals}")
        monotonic_checks+=1
        for other in others:
            ov=[float(r[AX[other]]) for r in rr]
            if max(ov)-min(ov)>5e-7:
                leaks+=1
if leaks: raise AssertionError(f"S2 leakage count={leaks}")
print(f"S2_AXIS_INTERVENTION_SEPARATION=PASS leakage={leaks}")
print(f"S3_EXACT_MONOTONICITY=PASS checks={monotonic_checks}")

# S4/S5 noisy hidden recovery and cross-axis leakage
noisy=[i for i,r in K.items() if r["lane"]=="noisy"]
own={}
maxcross=0.0
for ai,a in enumerate(AX):
    measured=[float(P[i][a]) for i in noisy]
    latent=[float(K[i][a]) for i in noisy]
    own[a]=pearson(measured,latent)
    if own[a]<0.90:
        raise AssertionError(f"S4 {a} correlation={own[a]}")
    for bi,b in enumerate(AX):
        if ai==bi:continue
        c=abs(pearson(measured,[float(K[i][b]) for i in noisy]))
        maxcross=max(maxcross,c)
        if c>0.10:
            raise AssertionError(f"S5 leakage measured={a} latent={b} r={c}")
    print(f"NOISY_SELF_CORR_{a}={own[a]:.6f}")
print(f"S4_NOISY_CRITERION_RECOVERY=PASS min_r={min(own.values()):.6f}")
print(f"S5_CROSS_AXIS_DISCRIMINANT_STRESS=PASS max_abs_r={maxcross:.6f}")

# measured-measured redundancy diagnostic under orthogonal factorial design
max_mm=0.0
for i,a in enumerate(AX):
    for b in AX[i+1:]:
        c=abs(pearson([float(P[x][a]) for x in noisy],[float(P[x][b]) for x in noisy]))
        max_mm=max(max_mm,c)
print(f"NOISY_MEASURED_AXIS_MAX_ABS_CORR={max_mm:.6f}")

# noisy monotone means
for a,l in zip(AX,LV):
    means=[]
    for lev in range(3):
        vv=[float(P[i][a]) for i in noisy if int(K[i][l])==lev]
        means.append(sum(vv)/len(vv))
    if not (means[0]<means[1]<means[2]):
        raise AssertionError(f"S3 noisy monotonic fail {a} {means}")
    print(f"NOISY_LEVEL_MEANS_{a}="+",".join(f"{x:.6f}" for x in means))
print("S3_NOISY_MEAN_MONOTONICITY=PASS")

# diagnostic absolute error
mae={}
for a in AX:
    mae[a]=sum(abs(float(P[i][a])-float(K[i][a])) for i in noisy)/len(noisy)
    print(f"NOISY_MAE_{a}={mae[a]:.6f}")

# S6 decoy invariance
changed=0
for i in P:
    for a in AX:
        if P[i][a]!=DP[i][a]:changed+=1
if changed:raise AssertionError(f"S6 decoy changed cells={changed}")
print(f"S6_DECOY_INVARIANCE=PASS changed_profile_cells={changed}")

# Explicitly show decoys themselves changed
decoy_cols=["w_repeat_decoy","n_replicate_decoy","i_rival_count_decoy","t_train_decoy","d_challenge_decoy"]
decoy_changed=sum(1 for i in U for col in decoy_cols if U[i][col] != UD[i][col])
expected=len(U)*len(decoy_cols)
if decoy_changed!=expected:
    raise AssertionError(f"not all decoys changed: {decoy_changed}/{expected}")
print(f"DECOY_FIELDS_MUTATED=PASS cells={decoy_changed}")
print("DECOY_FIELDS_NONCONSTITUTIVE=PASS")

print("LEVEL2_INTERNAL_CALIBRATION_CRITERIA_S1_TO_S6=PASS")
print("LEVEL3_EXTERNAL_CALIBRATION=HOLD")
print("LEVEL4_TRUTH_DISTANCE_METRIC=NOT_TARGETED")
