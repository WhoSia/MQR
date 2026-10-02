#!/usr/bin/env python3
import csv,itertools,pathlib
from collections import defaultdict
ROOT=pathlib.Path(__file__).resolve().parent
FEATURES=("current_envelope","generators","tech_state","budget_state","ethics_state","revision_state","ancestry_label")
TRIGGERS=("RIVAL_ENTRY","TECH_UNLOCK","ETHICS_REVIEW","BUDGET_UNLOCK")
def read(p):
    with open(p,newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def gs(s):return set(x for x in s["generators"].split(",") if x)
def tr(s,t):
    g=gs(s)
    if t=="RIVAL_ENTRY": return ("RIVAL_X","NEW_SEPARATOR","DOWNGRADE") if "RIVAL" in g else ("NONE","NO_NEW_CONTACT","UNCHANGED")
    if t=="TECH_UNLOCK":
        if "INSTRUMENT" not in g:return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        return ("INST_Z","NEW_SEPARATOR","DOWNGRADE") if s["tech_state"]=="T1" else ("NONE","RELEVANT_BUT_UNREALIZABLE","UNCHANGED")
    if t=="ETHICS_REVIEW":
        if "EXTERNAL" not in g:return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        return ("ETH_H","EXECUTION_PERMISSION_CHANGED","DOWNGRADE") if s["ethics_state"]=="E1" else ("NONE","ETH_H_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED")
    if t=="BUDGET_UNLOCK":
        if "EXTERNAL" not in g:return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        return ("COST_Q","EXECUTION_FEASIBILITY_CHANGED","DOWNGRADE") if s["budget_state"]=="HIGH" else ("NONE","COST_Q_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED")
def sig(s):return tuple(tr(s,t) for t in TRIGGERS)
def sufficient(S,sub):
    d=defaultdict(set)
    for s in S:d[tuple(s[x] for x in sub)].add(sig(s))
    return all(len(v)==1 for v in d.values())
def mins(S):
    for k in range(len(FEATURES)+1):
        m=[x for x in itertools.combinations(FEATURES,k) if sufficient(S,x)]
        if m:return m
    return []
S=read(ROOT/"PROXY-SEPARATION-FREEZE.tsv")
M=mins(S)
target=("generators","tech_state","budget_state","ethics_state")
ancestry_proxy=("tech_state","budget_state","ethics_state","ancestry_label")
leave={x:sufficient(S,tuple(y for y in target if y!=x)) for x in target}
out=ROOT/"results";out.mkdir(exist_ok=True)
with open(out/"proxy_separated_quotient.tsv","w",newline="") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n")
    w.writerow(["metric","value"])
    w.writerow(["RAW_STATES",len(S)])
    w.writerow(["PREDICTIVE_CLASSES",len(set(sig(s) for s in S))])
    w.writerow(["MINIMAL_FEATURE_COUNT",len(M[0]) if M else -1])
    w.writerow(["MINIMAL_FEATURE_SETS",";".join(",".join(x) for x in M)])
    w.writerow(["ANCESTRY_PROXY_STILL_SUFFICIENT",str(sufficient(S,ancestry_proxy)).upper()])
    for k,v in leave.items():w.writerow([f"DROP_{k}_STILL_SUFFICIENT",str(v).upper()])
ok=(len(S)==8 and len(set(sig(s) for s in S))==5 and M==[target] and not sufficient(S,ancestry_proxy) and all(not v for v in leave.values()))
print("MQR471_PHASE2_PROXY_SEPARATION="+("PASS" if ok else "FAIL"))
print("MQR471_PHASE2_RAW_STATES="+str(len(S)))
print("MQR471_PHASE2_PREDICTIVE_CLASSES="+str(len(set(sig(s) for s in S))))
print("MQR471_PHASE2_MINIMAL_FEATURE_COUNT="+str(len(M[0]) if M else -1))
print("MQR471_PHASE2_MINIMAL_FEATURE_SET="+";".join(",".join(x) for x in M))
print("MQR471_PHASE2_ANCESTRY_PROXY_BROKEN="+("YES" if not sufficient(S,ancestry_proxy) else "NO"))
raise SystemExit(0 if ok else 1)
