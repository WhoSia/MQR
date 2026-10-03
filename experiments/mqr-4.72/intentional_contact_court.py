#!/usr/bin/env python3
import csv, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
with open(ROOT/"COURT-FREEZE.tsv",newline="") as f:
    rows=list(csv.DictReader(f,delimiter="\t"))

def verdict(r):
    d=r["domain"]
    t=r["target_mode"]
    indep=r["independent_check"]=="YES"
    defeat=r["defeat_route_preserved"]=="YES"
    sem=r["semantic_transport"]

    if d=="NATSCI":
        if t=="EXPLORATORY":
            return "ADMIT_EXPLORATORY" if indep and defeat else "HOLD"
        if t=="DIFFERENT_TARGET":
            return "DISTINCT_OUTCOME_SEMANTICS"
        if r["calibration_or_framework"]=="THEORY_SELF_GATED" and not indep:
            return "HOLD_CIRCULAR"
        if r["calibration_or_framework"]=="THEORY_GUIDED" and indep and defeat:
            return "ADMIT_WITH_DEPENDENCE_RECEIPT"
        if not defeat:
            return "DOWNGRADE_INHERITED_AUTHORITY"
        return "ADMIT_LOCAL"

    if d=="MATH":
        if r["calibration_or_framework"]=="COUNTERMODEL_TARGET":
            return "HOLD_TRANSPORT"
        if t=="SEMANTIC_REINTERPRETATION" and sem=="NO":
            return "HOLD_SEMANTIC_DRIFT"
        if r["calibration_or_framework"]=="VALID_EMBEDDING" and defeat and sem=="YES":
            return "CERTIFY_TRANSPORT_RELATIVE"
        if r["calibration_or_framework"] in {"VALID_PROOF","CHECKED_KERNEL"} and defeat:
            return "CERTIFY_RELATIVE"
        return "HOLD"

    raise ValueError(d)

bad=[]
for r in rows:
    g=verdict(r)
    if g!=r["expected"]:
        bad.append((r["case_id"],g,r["expected"]))

exploratory=verdict(next(r for r in rows if r["case_id"]=="N3"))=="ADMIT_EXPLORATORY"
self_gate=verdict(next(r for r in rows if r["case_id"]=="N4"))=="HOLD_CIRCULAR"
lost_defeat=verdict(next(r for r in rows if r["case_id"]=="N6"))=="DOWNGRADE_INHERITED_AUTHORITY"
math_transport=verdict(next(r for r in rows if r["case_id"]=="M2"))=="HOLD_TRANSPORT"
checked_kernel=verdict(next(r for r in rows if r["case_id"]=="M5"))=="CERTIFY_RELATIVE"

out=ROOT/"results";out.mkdir(exist_ok=True)
with open(out/"intentional_contact_court.tsv","w",newline="") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n")
    w.writerow(["case_id","got","expected"])
    for r in rows:w.writerow([r["case_id"],verdict(r),r["expected"]])

ok=not bad and exploratory and self_gate and lost_defeat and math_transport and checked_kernel
print("MQR472_INTENTIONAL_CONTACT="+("PASS" if ok else "FAIL"))
print("MQR472_CASES="+str(len(rows)))
print("MQR472_EXPLORATORY_WITHOUT_FULL_TARGET="+("YES" if exploratory else "NO"))
print("MQR472_THEORY_SELF_GATE_BLOCKED="+("YES" if self_gate else "NO"))
print("MQR472_DEFEAT_ROUTE_LOSS_DOWNGRADES="+("YES" if lost_defeat else "NO"))
print("MQR472_MATH_FRAMEWORK_LABEL_NOT_ENOUGH="+("YES" if math_transport else "NO"))
print("MQR472_CHECKED_KERNEL_RELATIVE_AUTHORITY="+("YES" if checked_kernel else "NO"))
raise SystemExit(0 if ok else 1)
