#!/usr/bin/env python3
import csv, pathlib, sys

SEV = {"NONE":0,"BOUNDED":1,"MATERIAL":2,"FATAL":3}

def decision(r):
    if r["warrant_complete"] != "YES":
        return "HOLD_WARRANT_OPEN"
    if r["transport_valid"] != "YES":
        return "HOLD_TRANSPORT"
    if r["revision_requested"] == "YES":
        return "REVISION_AUTHORIZED" if r["revision_authorized"] == "YES" else "REVISION_FORBIDDEN"
    if r["loss_release"] == "FATAL":
        return "FORBID_MERGE"
    if r["reopening_trigger"] == "YES":
        return "REEXPAND_REQUIRED"
    ceilings = {
        "exploratory": {"sep":2,"reopen":1,"prov":1,"ext":2,"release":1},
        "audit": {"sep":1,"reopen":2,"prov":1,"ext":1,"release":1},
        "public_release": {"sep":1,"reopen":1,"prov":1,"ext":1,"release":0},
        "cross_domain": {"sep":1,"reopen":1,"prov":1,"ext":1,"release":1},
    }[r["context"]]
    vals = {
        "sep":SEV[r["loss_sep"]], "reopen":SEV[r["loss_reopen"]],
        "prov":SEV[r["loss_prov"]], "ext":SEV[r["loss_ext"]],
        "release":SEV[r["loss_release"]],
    }
    if vals["reopen"] == 3:
        return "REEXPAND_REQUIRED"
    if vals["prov"] == 3 or vals["ext"] == 3:
        return "REOPEN_REQUIRED"
    if any(vals[k] > ceilings[k] for k in vals):
        return "HOLD_CONTEXT_CEILING"
    return "ACCEPT_WITH_AUDIT" if any(v > 0 for v in vals.values()) else "ACCEPT_LOCAL"

def baseline(r):
    # Deliberately allows established decision theory to win.
    if r["scalar_warrant"] == "INDEPENDENT":
        return "UTILITY_RECOVERY_CONTROL"
    if r["revision_requested"] == "YES":
        return "PREFERENCE_REVISION_BASELINE"
    if r["loss_release"] == "FATAL" or r["reopening_trigger"] == "YES":
        return "HARD_CONSTRAINT_EQUIVALENT"
    if r["transport_valid"] != "YES":
        return "PARTIAL_ORDER_BASELINE"
    if r["scalar_representation"] == "YES":
        return "REPRESENTATION_ONLY"
    return "NO_BASELINE_MATCH"

def main():
    src = pathlib.Path(sys.argv[1] if len(sys.argv)>1 else "experiments/mqr-4.68/COURT-FREEZE.tsv")
    out = pathlib.Path("experiments/mqr-4.68/results/python_results.tsv")
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(src.open(), delimiter="\t"))
    got=[]
    mismatches=0
    with out.open("w", newline="") as f:
        w=csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["case","decision","baseline"])
        for r in rows:
            d=decision(r); b=baseline(r)
            w.writerow([r["case"],d,b])
            if d != r["expected_decision"] or b != r["expected_baseline"]:
                mismatches += 1
            got.append((r["case"],d,b))
    summary = pathlib.Path("experiments/mqr-4.68/results/python_summary.tsv")
    with summary.open("w", newline="") as f:
        w=csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["metric","value"])
        w.writerow(["CASES",len(rows)])
        w.writerow(["EXPECTATION_MISMATCHES",mismatches])
        w.writerow(["UTILITY_RECOVERY_CONTROLS",sum(b=="UTILITY_RECOVERY_CONTROL" for _,_,b in got)])
        w.writerow(["REPRESENTATION_ONLY_CASES",sum(b=="REPRESENTATION_ONLY" for _,_,b in got)])
        w.writerow(["HARD_CONSTRAINT_EQUIVALENT_CASES",sum(b=="HARD_CONSTRAINT_EQUIVALENT" for _,_,b in got)])
        w.writerow(["PREFERENCE_REVISION_BASELINE_CASES",sum(b=="PREFERENCE_REVISION_BASELINE" for _,_,b in got)])
        w.writerow(["TRANSPORT_HOLDS",sum(d=="HOLD_TRANSPORT" for _,d,_ in got)])
        w.writerow(["POSTHOC_REVISION_FORBIDDEN",sum(d=="REVISION_FORBIDDEN" for _,d,_ in got)])
    if mismatches:
        print(f"MQR468_PYTHON_COURT=FAIL mismatches={mismatches}")
        return 1
    print("MQR468_PYTHON_COURT=PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
