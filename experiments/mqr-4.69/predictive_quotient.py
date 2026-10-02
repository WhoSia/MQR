#!/usr/bin/env python3
import csv, pathlib, sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent
FEATURES = ("authorization_state","provenance_state","defeater_state","revision_state")

def read_tsv(path):
    with pathlib.Path(path).open(newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def load_schema(path):
    return {r["ancestry"]: r for r in read_tsv(path)}

def transition(intervention, feat):
    a,p,d,r = (feat[x] for x in FEATURES)
    if intervention == "AUTHORIZATION_CHECK":
        return "HOLD_REAUTHORIZE" if a in {"RETROSPECTIVE","UNAUTHORIZED"} else "STABLE"
    if intervention == "REVISION_REPLAY":
        if a == "RETROSPECTIVE": return "REOPEN_REQUIRED"
        if r == "REASON_MUTATION": return "HOLD_REASON_RECONSTITUTE"
        return "STABLE"
    if intervention in {"WITHDRAW_ANCESTRY_SUPPORT","REPRODUCE_UNDER_INDEPENDENT_ANCESTRY"}:
        return "REOPEN_REQUIRED" if p == "COMMON_MODE_SINGLE_ROOT" else "STABLE"
    if intervention == "REOPEN_WITH_HELD_OUT_DEFEATER":
        return "STABLE" if d == "SURVIVED_D1" else "REOPEN_REQUIRED"
    if intervention == "REOPEN_WITH_HELD_OUT_DEFEATER_D3":
        return "REOPEN_REQUIRED"
    if intervention == "COUNTERFACTUAL_RECONSTITUTION":
        return "REOPEN_REQUIRED" if r == "REVERSAL" else "STABLE"
    if intervention in {"AUDIT_SOURCE","SCOPE_EXPANSION"}:
        return "STABLE"
    raise ValueError(intervention)

def main():
    pair_path = pathlib.Path(sys.argv[1] if len(sys.argv)>1 else ROOT/"PAIR-FREEZE.tsv")
    schema_path = pathlib.Path(sys.argv[2] if len(sys.argv)>2 else ROOT/"ANCESTRY-FEATURES.tsv")
    pairs = read_tsv(pair_path)
    schema = load_schema(schema_path)
    interventions = sorted({r["intervention"] for r in pairs})

    by_signature = defaultdict(list)
    for anc, feat in schema.items():
        sig = tuple(transition(u, feat) for u in interventions)
        by_signature[sig].append(anc)

    typed_states = {tuple(feat[k] for k in FEATURES) for feat in schema.values()}
    classes = sorted(by_signature.items(), key=lambda kv: (kv[0], sorted(kv[1])))

    class_of = {}
    for i,(sig, members) in enumerate(classes):
        cid=f"Q{i:02d}"
        for m in members: class_of[m]=cid

    # Verify the quotient predicts every frozen side outcome.
    mismatch=0
    for pair in pairs:
        for side in ("A","B"):
            anc=pair[f"ancestry_{side}"]
            got=transition(pair["intervention"],schema[anc])
            if got != pair[f"expected_{side}"]:
                mismatch += 1

    outdir=ROOT/"results"; outdir.mkdir(parents=True,exist_ok=True)
    with (outdir/"predictive_quotient.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["class_id","member_count","members"]+interventions)
        for i,(sig,members) in enumerate(classes):
            w.writerow([f"Q{i:02d}",len(members),",".join(sorted(members))]+list(sig))

    with (outdir/"predictive_quotient_summary.tsv").open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["metric","value"])
        w.writerow(["RAW_ANCESTRY_LABELS",len(schema)])
        w.writerow(["DISTINCT_TYPED_FOUR_AXIS_STATES",len(typed_states)])
        w.writerow(["PREDICTIVE_EQUIVALENCE_CLASSES",len(classes)])
        w.writerow(["FROZEN_OUTCOME_MISMATCHES",mismatch])
        w.writerow(["INTERVENTION_COUNT",len(interventions)])
        w.writerow(["FOUR_AXIS_OVERRETENTION", "YES" if len(classes) < len(typed_states) else "NO"])

    if mismatch:
        print(f"MQR469_PREDICTIVE_QUOTIENT=FAIL mismatches={mismatch}")
        return 1
    print("MQR469_PREDICTIVE_QUOTIENT=PASS")
    print(f"MQR469_RAW_ANCESTRY_LABELS={len(schema)}")
    print(f"MQR469_TYPED_FOUR_AXIS_STATES={len(typed_states)}")
    print(f"MQR469_PREDICTIVE_CLASSES={len(classes)}")
    print("MQR469_FOUR_AXIS_OVERRETENTION=" + ("YES" if len(classes)<len(typed_states) else "NO"))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
