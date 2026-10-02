#!/usr/bin/env python3
import csv, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
with open(ROOT/"TRANSPORT-FREEZE.tsv",newline="") as f:
    rows=list(csv.DictReader(f,delimiter="\t"))

bad=[]
for r in rows:
    preserve=all(r[k]=="YES" for k in ["semantic_role_match","feasibility_match","permission_match"])
    got="PRESERVE" if preserve else "HOLD"
    if got!=r["expected"]:
        bad.append((r["transport_id"],got,r["expected"]))

label_only=next(r for r in rows if r["transport_id"]=="TR_SEMANTIC_BREAK")
label_laundering_blocked=(label_only["label_match"]=="YES" and label_only["expected"]=="HOLD")

ok=not bad and label_laundering_blocked
print("MQR471_TRANSPORT_COURT="+("PASS" if ok else "FAIL"))
print("MQR471_LABEL_ONLY_INSUFFICIENT="+("YES" if label_laundering_blocked else "NO"))
print("MQR471_TRANSPORT_CASES="+str(len(rows)))
raise SystemExit(0 if ok else 1)
