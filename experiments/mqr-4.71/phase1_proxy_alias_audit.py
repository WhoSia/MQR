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
S=read(ROOT/"STATE-FREEZE.tsv")
M=mins(S)
expected={
 ("generators","tech_state","budget_state","ethics_state"),
 ("tech_state","budget_state","ethics_state","ancestry_label"),
}
ok=len(S)==6 and len(set(sig(s) for s in S))==5 and set(M)==expected
print("MQR471_PHASE1_ALIAS_AUDIT="+("PASS" if ok else "FAIL"))
print("MQR471_PHASE1_MINIMAL_COUNT="+str(len(M)))
print("MQR471_PHASE1_MINIMAL_SETS="+";".join(",".join(x) for x in M))
print("MQR471_PHASE1_ANCESTRY_PROXY="+("YES" if any("ancestry_label" in x for x in M) else "NO"))
raise SystemExit(0 if ok else 1)
