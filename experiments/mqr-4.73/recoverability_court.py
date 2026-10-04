#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
with open(ROOT / "RECOVERABILITY-FREEZE.tsv", newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))

def verdict(r):
    w = r["witness"]
    indep = r["model_independent"] == "YES"
    sem = r["semantic_scope_preserved"] == "YES"

    if w == "LOSSLESS_INVERSE" and indep and sem:
        return "RECOVERABLE_EXACT"
    if w in {"CLAIM_SUFFICIENT_DECODER", "CALIBRATION_BRIDGE"} and indep and sem:
        return "RECOVERABLE_SCOPE"
    if w == "BLACKWELL_GARBLING" and indep and sem:
        return "RECOVERABLE_LOCAL_BASELINE"
    if w == "POSTHOC_PREDICTOR":
        return "NOT_RECOVERABLE_POSTHOC"
    if w == "PARTIAL_BRIDGE":
        return "NOT_RECOVERABLE_HIDDEN_LOSS"
    if w == "SUCCESSOR_SELF_MODEL" and not indep:
        return "HOLD_MODEL_DEPENDENT"
    if w == "LOWER_UNCERTAINTY_ONLY":
        return "NOT_RECOVERABLE_LOSSY"
    if w in {"CONSERVATIVE_EXTENSION", "CHECKED_CERTIFICATE"} and indep and sem:
        return "RECOVERABLE_RELATIVE"
    if w == "NONCONSERVATIVE_EXTENSION" or not sem:
        return "NOT_RECOVERABLE_SEMANTIC" if w == "NONCONSERVATIVE_EXTENSION" else "HOLD_UNEARNED"
    return "HOLD_UNEARNED"

bad=[]
for r in rows:
    got=verdict(r)
    if got!=r["expected"]:
        bad.append((r["case_id"],got,r["expected"]))

checks = {
    "POSTHOC_BLOCKED": verdict(next(r for r in rows if r["case_id"]=="R3"))=="NOT_RECOVERABLE_POSTHOC",
    "BLACKWELL_BASELINE": verdict(next(r for r in rows if r["case_id"]=="R5"))=="RECOVERABLE_LOCAL_BASELINE",
    "SELF_MODEL_HELD": verdict(next(r for r in rows if r["case_id"]=="R7"))=="HOLD_MODEL_DEPENDENT",
    "LOWER_UNCERTAINTY_NOT_ENOUGH": verdict(next(r for r in rows if r["case_id"]=="R8"))=="NOT_RECOVERABLE_LOSSY",
    "NONCONSERVATIVE_BLOCKED": verdict(next(r for r in rows if r["case_id"]=="R11"))=="NOT_RECOVERABLE_SEMANTIC"
}
ok = not bad and all(checks.values())
print("MQR473_RECOVERABILITY=" + ("PASS" if ok else "FAIL"))
print("MQR473_RECOVERABILITY_CASES=" + str(len(rows)))
for k,v in checks.items():
    print("MQR473_" + k + "=" + ("YES" if v else "NO"))
if bad:
    for b in bad: print("MISMATCH", *b)
raise SystemExit(0 if ok else 1)
