#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
with open(ROOT / "COURT-FREEZE.tsv", newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))

def verdict(r):
    old = set(filter(None, r["old_exposure"].split(",")))
    new = set(filter(None, r["new_exposure"].split(",")))
    recover = r["old_distinction_recoverable"] == "YES"
    adds = r["new_distinction"] == "YES"
    bridge = r["bridge"]
    indep = r["independent_support"] == "YES"

    if bridge == "TRACEABLE_ONLY" and not indep:
        return "HOLD_TRACEABILITY_NOT_ENOUGH"
    if bridge == "LABEL_ONLY" and not indep:
        return "HOLD_BRIDGE_UNEARNED"
    if bridge == "NONCONSERVATIVE_UNKNOWN" and not indep:
        return "HOLD_STRENGTH_UNEARNED"
    if bridge == "MERGE_LOSSY" and not recover:
        return "HOLD_MERGE_LOSS"
    if not recover and adds:
        return "INCOMPARABLE_HIDDEN_LOSS" if r["domain"] == "NATSCI" else "INCOMPARABLE_SEMANTIC_LOSS"
    if not recover:
        return "INCOMPARABLE"
    if bridge in {"REFINEMENT_UNION", "OBLIGATION_REFINEMENT"} and adds and indep:
        return "REFINEMENT_DOMINANCE_LOCAL" if r["domain"] == "NATSCI" else "REFINEMENT_DOMINANCE_RELATIVE"
    if adds and indep and old.issubset(new):
        return "STRICT_DOMINANCE_LOCAL" if r["domain"] == "NATSCI" else "STRICT_DOMINANCE_RELATIVE"
    if recover and not adds and indep:
        return "EQUIVALENT_LOCAL" if r["domain"] == "NATSCI" else "EQUIVALENT_RELATIVE"
    return "HOLD"

bad = []
for r in rows:
    got = verdict(r)
    if got != r["expected"]:
        bad.append((r["case_id"], got, r["expected"]))

hidden_loss = verdict(next(r for r in rows if r["case_id"] == "N3")) == "INCOMPARABLE_HIDDEN_LOSS"
strict = verdict(next(r for r in rows if r["case_id"] == "N4")) == "STRICT_DOMINANCE_LOCAL"
trace = verdict(next(r for r in rows if r["case_id"] == "N8")) == "HOLD_TRACEABILITY_NOT_ENOUGH"
math_loss = verdict(next(r for r in rows if r["case_id"] == "M2")) == "INCOMPARABLE_SEMANTIC_LOSS"
kernel = verdict(next(r for r in rows if r["case_id"] == "M1")) == "EQUIVALENT_RELATIVE"

out = ROOT / "results"
out.mkdir(exist_ok=True)
with open(out / "capability_court.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["case_id", "got", "expected"])
    for r in rows:
        w.writerow([r["case_id"], verdict(r), r["expected"]])

ok = not bad and hidden_loss and strict and trace and math_loss and kernel
print("MQR473_CAPABILITY_COURT=" + ("PASS" if ok else "FAIL"))
print("MQR473_CASES=" + str(len(rows)))
print("MQR473_HIDDEN_LOSS_BLOCKS_DOMINANCE=" + ("YES" if hidden_loss else "NO"))
print("MQR473_STRICT_DOMINANCE_REQUIRES_RECOVERY=" + ("YES" if strict else "NO"))
print("MQR473_TRACEABILITY_ALONE_NOT_ENOUGH=" + ("YES" if trace else "NO"))
print("MQR473_MATH_SEMANTIC_LOSS_BLOCKS_DOMINANCE=" + ("YES" if math_loss else "NO"))
print("MQR473_CHECKED_KERNEL_RELATIVE_EQUIVALENCE=" + ("YES" if kernel else "NO"))
if bad:
    for item in bad:
        print("MISMATCH", *item)
raise SystemExit(0 if ok else 1)
