#!/usr/bin/env python3
import csv, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
with open(ROOT/"SCOPE-TERMINATION-FREEZE.tsv",newline="") as f:
    rows=list(csv.DictReader(f,delimiter="\t"))

def verdict(r):
    src=r["scope_source"]
    known=r["universe_known"]=="YES"
    comp=r["generator_complete_relative_to_scope"]=="YES"
    if src=="GENERATOR_OUTPUT_ONLY":
        return "HOLD_CIRCULAR"
    if src=="EXECUTION_CONTRACT" and known and comp:
        return "CERTIFY_EXECUTION_ONLY"
    if src in {"EXTERNAL_FINITE","PROVED_GRAMMAR"} and known and comp:
        return "CERTIFY_RELATIVE"
    return "HOLD"

bad=[]
for r in rows:
    g=verdict(r)
    if g!=r["expected"]: bad.append((r["case_id"],g,r["expected"]))
rel=sum(verdict(r)=="CERTIFY_RELATIVE" for r in rows)
circ=sum(verdict(r)=="HOLD_CIRCULAR" for r in rows)
exec_only=sum(verdict(r)=="CERTIFY_EXECUTION_ONLY" for r in rows)
ok=(not bad and rel==2 and circ==1 and exec_only==1)
print("MQR471_SCOPE_TERMINATION="+("PASS" if ok else "FAIL"))
print("MQR471_RELATIVE_CERTIFICATES="+str(rel))
print("MQR471_EXECUTION_ONLY_CERTIFICATES="+str(exec_only))
print("MQR471_CIRCULAR_HOLDS="+str(circ))
print("MQR471_RELATIVE_NE_OPEN_WORLD=YES")
raise SystemExit(0 if ok else 1)
