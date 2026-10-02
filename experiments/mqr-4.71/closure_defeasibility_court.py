#!/usr/bin/env python3
import csv, pathlib

ROOT=pathlib.Path(__file__).resolve().parent

with open(ROOT/"CLOSURE-DEFEASIBILITY-FREEZE.tsv", newline="") as f:
    rows=list(csv.DictReader(f, delimiter="\t"))

def executable(r):
    return (
        r["feasibility"]=="AVAILABLE"
        and r["permission"]=="PERMITTED"
        and r["budget"]=="LOW"
    )

def verdict(r):
    if r["scientific_split"]!="YES":
        return "STABLE"
    if r["scope_kind"]=="SCIENTIFIC_RELEVANCE":
        return "DOWNGRADE" if executable(r) else "DOWNGRADE_DEBT"
    if r["scope_kind"]=="CURRENT_EXECUTION":
        return "DOWNGRADE" if executable(r) else "STABLE_SCOPED"
    raise ValueError(r["scope_kind"])

mismatches=[]
out=[]
for r in rows:
    got=verdict(r)
    out.append((r["case_id"],got,r["expected"]))
    if got!=r["expected"]:
        mismatches.append((r["case_id"],got,r["expected"]))

pairs={}
for r in rows:
    base=r["case_id"].split("_")[0]
    pairs.setdefault(base,{})[r["scope_kind"]]=verdict(r)

scope_separation=sum(
    1 for x in pairs.values()
    if x.get("SCIENTIFIC_RELEVANCE")!=x.get("CURRENT_EXECUTION")
)

outdir=ROOT/"results";outdir.mkdir(exist_ok=True)
with open(outdir/"closure_defeasibility.tsv","w",newline="") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n")
    w.writerow(["case_id","got","expected"])
    w.writerows(out)

ok=(not mismatches and scope_separation==3)
print("MQR471_CLOSURE_DEFEASIBILITY="+("PASS" if ok else "FAIL"))
print("MQR471_CASES="+str(len(rows)))
print("MQR471_SCOPE_SEPARATION_CASES="+str(scope_separation))
print("MQR471_EXECUTION_COMPLETE_NE_SCIENTIFIC_COMPLETE="+("YES" if scope_separation==3 else "NO"))
raise SystemExit(0 if ok else 1)
