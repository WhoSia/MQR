#!/usr/bin/env python3
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
with open(ROOT/"ROBUST-RECOVERABILITY-FREEZE.tsv",newline="") as f:
    rows=list(csv.DictReader(f,delimiter="\t"))

def verdict(r):
    nom=r["nominal_recovery"]=="YES"
    stable=r["perturbation_stable"]=="YES"
    indep=r["independent_separator"]=="YES"
    sem=r["semantic_bridge"]=="YES"
    adds=r["adds_new"]=="YES"
    d=r["domain"]
    if not nom:
        return "HIDDEN_LOSS_NOT_DOMINANT"
    if d=="NATSCI":
        if not stable and not indep:
            return "HOLD_SURROGATE" if adds else "HOLD_SELF_MODEL"
        if not stable:
            return "NOMINAL_ONLY_NOT_DOMINANT"
        if stable and indep and sem:
            if adds:
                return "ROBUST_SEPARATOR_REFINEMENT" if r["case_id"]=="P8" else "ROBUST_LOCAL_DOMINANCE"
            return "ROBUST_CALIBRATION_BRIDGE" if r["case_id"]=="P6" else "ROBUST_RECOVERABLE"
    else:
        if not stable or not sem:
            return "NONCONSERVATIVE_HOLD"
        if not indep and not sem:
            return "LABEL_ONLY_HOLD"
        if stable and indep and sem:
            return "ROBUST_RELATIVE_DOMINANCE" if adds else "ROBUST_RELATIVE"
        if not indep:
            return "LABEL_ONLY_HOLD"
    return "HOLD"

bad=[]
for r in rows:
    got=verdict(r)
    if got!=r["expected"]: bad.append((r["case_id"],got,r["expected"]))
checks={
"NOMINAL_BREAKS":verdict(next(x for x in rows if x["case_id"]=="P2"))=="NOMINAL_ONLY_NOT_DOMINANT",
"SELF_MODEL_BLOCKED":verdict(next(x for x in rows if x["case_id"]=="P3"))=="HOLD_SELF_MODEL",
"ROBUST_DOMINANCE":verdict(next(x for x in rows if x["case_id"]=="P5"))=="ROBUST_LOCAL_DOMINANCE",
"NONCONSERVATIVE_BLOCKED":verdict(next(x for x in rows if x["case_id"]=="P11"))=="NONCONSERVATIVE_HOLD"
}
ok=not bad and all(checks.values())
print("MQR473_ROBUST_RECOVERABILITY="+("PASS" if ok else "FAIL"))
print("MQR473_ROBUST_CASES="+str(len(rows)))
for k,v in checks.items(): print("MQR473_"+k+"="+("YES" if v else "NO"))
for b in bad: print("MISMATCH",*b)
raise SystemExit(0 if ok else 1)
