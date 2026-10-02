#!/usr/bin/env python3
import csv, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
with open(ROOT/"THREE-LAYER-CONTACT-FREEZE.tsv",newline="") as f:
    rows=list(csv.DictReader(f,delimiter="\t"))

def transition(r):
    tr=r["transition"]
    if tr=="NONE": return ("SAME","SAME","SAME")
    if tr=="TECH_UNLOCK": return ("SAME","SAME","EXPAND")
    if tr=="ETHICS_RESTRICT": return ("SAME","SAME","CONTRACT")
    if tr=="RIVAL_ARRIVAL": return ("EXPAND","EXPAND","SAME")
    if tr=="GENERATOR_NULL_ENTRY": return ("EXPAND","SAME","SAME")
    raise ValueError(tr)

def inclusion_ok(r):
    c=r["candidate"]=="YES"; s=r["scientific"]=="YES"; x=r["executable"]=="YES"
    return (not x or s) and (not s or c)

bad=[]
for r in rows:
    got=transition(r)
    exp=(r["expected_C"],r["expected_S"],r["expected_X"])
    if got!=exp or not inclusion_ok(r):
        bad.append((r["case_id"],got,exp,inclusion_ok(r)))

technology_layer_specific = transition(next(r for r in rows if r["case_id"]=="T_UNLOCK"))==("SAME","SAME","EXPAND")
candidate_null_specific = transition(next(r for r in rows if r["case_id"]=="G_NULL"))==("EXPAND","SAME","SAME")
rival_scientific_without_execution = transition(next(r for r in rows if r["case_id"]=="R_ARRIVE"))==("EXPAND","EXPAND","SAME")
nonmonotone_execution = any(r["expected_X"]=="EXPAND" for r in rows) and any(r["expected_X"]=="CONTRACT" for r in rows)

out=ROOT/"results";out.mkdir(exist_ok=True)
with open(out/"three_layer_contact.tsv","w",newline="") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n")
    w.writerow(["case_id","got_C","got_S","got_X","inclusion_ok"])
    for r in rows:
        g=transition(r);w.writerow([r["case_id"],*g,str(inclusion_ok(r)).upper()])

ok=not bad and technology_layer_specific and candidate_null_specific and rival_scientific_without_execution and nonmonotone_execution
print("MQR471_THREE_LAYER_CONTACT="+("PASS" if ok else "FAIL"))
print("MQR471_CASES="+str(len(rows)))
print("MQR471_TECH_UNLOCK_X_ONLY="+("YES" if technology_layer_specific else "NO"))
print("MQR471_GENERATOR_NULL_C_ONLY="+("YES" if candidate_null_specific else "NO"))
print("MQR471_RIVAL_C_S_WITHOUT_X="+("YES" if rival_scientific_without_execution else "NO"))
print("MQR471_EXECUTION_NONMONOTONE="+("YES" if nonmonotone_execution else "NO"))
raise SystemExit(0 if ok else 1)
