import csv,sys
def b(x):return x=="1"
def cls(r):
 if b(r["off_target_escape"]):return "OFF_TARGET_ESCAPE"
 if r["split_merge"]=="split":return "SPLIT_REQUIRED"
 if r["split_merge"]=="merge":return "MERGE_REQUIRED"
 if b(r["postoutcome"]) or not b(r["prospective"]):return "PROVISIONAL_TARGET"
 if b(r["institution_only"]) and not b(r["independent_warrant"]):return "UNWARRANTED_TARGET"
 if b(r["finite_contract"]) and b(r["independent_warrant"]):return "FINITE_CONTRACT_CLOSED"
 if b(r["competing_constitutions"]) and b(r["independent_warrant"]):return "COMPETING_CONSTITUTIONS"
 if b(r["independent_warrant"]):return "LOCALLY_WARRANTED_TARGET"
 return "PROVISIONAL_TARGET"
rows=list(csv.DictReader(open(sys.argv[1],encoding="utf-8"),delimiter="\t"))
ok=0
for r in rows:
 g=cls(r); ok+=g==r["expected"]
 if g!=r["expected"]:print(r["id"],r["expected"],g,file=sys.stderr)
print("MQR479_CASES="+str(len(rows)));print("MQR479_PASS="+str(ok));print("MQR479_PYTHON_COURT="+("PASS" if ok==len(rows) else "FAIL"))
sys.exit(0 if ok==len(rows) else 1)
