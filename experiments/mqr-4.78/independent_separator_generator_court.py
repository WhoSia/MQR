import csv,sys,collections

def b(x): return x=="1"

def classify(r):
    if b(r["reopen_ancestry"]): return "REOPEN_GENERATOR_ANCESTRY"
    if b(r["postoutcome"]) or not b(r["prospective"]): return "DIAGNOSTIC_FAMILY_ONLY"
    if r["split_merge"]=="split": return "SPLIT_REQUIRED"
    if r["split_merge"]=="merge": return "MERGE_COLLAPSE"
    if not b(r["separator_found"]): return "NO_SEPARATOR_AUTHORITY"
    if (b(r["ontology_common"]) or b(r["grammar_common"])) and not b(r["ancestry_diverse"]):
        return "COMMON_MODE_GENERATOR"
    if b(r["ancestry_diverse"]) and b(r["coverage_warrant"]) and b(r["separates_live"]):
        return "ANCESTRY_DIVERSE_LOCAL_AUTHORITY"
    return "FAMILY_RELATIVE_SEPARATION"

rows=list(csv.DictReader(open(sys.argv[1],encoding="utf-8"),delimiter="\t"))
counts=collections.Counter(); ok=0
for r in rows:
    got=classify(r); counts[got]+=1; ok += got==r["expected"]
    if got!=r["expected"]: print(f'{r["id"]} expected={r["expected"]} got={got}',file=sys.stderr)
print(f"MQR478_CASES={len(rows)}")
print(f"MQR478_PASS={ok}")
for k in sorted(counts): print(f"{k}={counts[k]}")
print("MQR478_PYTHON_COURT=" + ("PASS" if ok==len(rows) else "FAIL"))
sys.exit(0 if ok==len(rows) else 1)
