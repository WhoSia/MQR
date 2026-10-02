#!/usr/bin/env python3
import csv, itertools, pathlib
from collections import defaultdict

ROOT=pathlib.Path(__file__).resolve().parent
FEATURES=("current_envelope","generators","tech_state","budget_state","ethics_state","revision_state","ancestry_label")
TRIGGERS=("RIVAL_ENTRY","TECH_UNLOCK","ETHICS_REVIEW","BUDGET_UNLOCK")

def read_tsv(path):
    with open(path,newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

STATES=read_tsv(ROOT/"STATE-FREEZE.tsv")

def gens(s):
    return set(x for x in s["generators"].split(",") if x)

def transition(s,t):
    g=gens(s)
    if t=="RIVAL_ENTRY":
        return ("RIVAL_X","NEW_SEPARATOR","DOWNGRADE") if "RIVAL" in g else ("NONE","NO_NEW_CONTACT","UNCHANGED")
    if t=="TECH_UNLOCK":
        if "INSTRUMENT" not in g:return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        return ("INST_Z","NEW_SEPARATOR","DOWNGRADE") if s["tech_state"]=="T1" else ("NONE","RELEVANT_BUT_UNREALIZABLE","UNCHANGED")
    if t=="ETHICS_REVIEW":
        if "EXTERNAL" not in g:return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        return ("ETH_H","EXECUTION_PERMISSION_CHANGED","DOWNGRADE") if s["ethics_state"]=="E1" else ("NONE","ETH_H_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED")
    if t=="BUDGET_UNLOCK":
        if "EXTERNAL" not in g:return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        return ("COST_Q","EXECUTION_FEASIBILITY_CHANGED","DOWNGRADE") if s["budget_state"]=="HIGH" else ("NONE","COST_Q_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED")
    raise ValueError(t)

def future_sig(s):
    return tuple(transition(s,t) for t in TRIGGERS)

def partition_by_signature():
    d=defaultdict(list)
    for s in STATES:d[future_sig(s)].append(s["state_id"])
    return d

def feature_key(s,subset):
    return tuple(s[f] for f in subset)

def subset_sufficient(subset):
    groups=defaultdict(set)
    for s in STATES:groups[feature_key(s,subset)].add(future_sig(s))
    return all(len(v)==1 for v in groups.values())

def main():
    sig_classes=partition_by_signature()
    sufficient=[]
    for k in range(len(FEATURES)+1):
        for sub in itertools.combinations(FEATURES,k):
            if subset_sufficient(sub):
                sufficient.append(sub)
        if sufficient:break

    minimal_size=len(sufficient[0]) if sufficient else -1
    minimal=[s for s in sufficient if len(s)==minimal_size]

    # Necessity under the named four-state candidate G/T/B/E.
    candidate=("generators","tech_state","budget_state","ethics_state")
    candidate_ok=subset_sufficient(candidate)
    leave_one={}
    for f in candidate:
        sub=tuple(x for x in candidate if x!=f)
        leave_one[f]=subset_sufficient(sub)

    out=ROOT/"results";out.mkdir(exist_ok=True)
    with open(out/"generative_predictive_quotient.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["class_id","members"]+[f"trigger_{t}" for t in TRIGGERS])
        for i,(sig,members) in enumerate(sorted(sig_classes.items(),key=lambda kv:sorted(kv[1]))):
            flat=[" / ".join(x) for x in sig]
            w.writerow([f"Q{i:02d}",",".join(sorted(members))]+flat)

    with open(out/"generative_state_minimality.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["metric","value"])
        w.writerow(["RAW_STATES",len(STATES)])
        w.writerow(["PREDICTIVE_CLASSES",len(sig_classes)])
        w.writerow(["MINIMAL_FEATURE_COUNT",minimal_size])
        w.writerow(["MINIMAL_FEATURE_SETS",";".join(",".join(x) for x in minimal)])
        w.writerow(["CANDIDATE_G_T_B_E_SUFFICIENT",str(candidate_ok).upper()])
        for k,v in leave_one.items():w.writerow([f"DROP_{k}_STILL_SUFFICIENT",str(v).upper()])

    # Frozen facts expected from the current state table.
    expected_min={("generators","tech_state","budget_state","ethics_state")}
    ok=(
        len(STATES)==6
        and len(sig_classes)==5
        and minimal_size==4
        and set(minimal)==expected_min
        and candidate_ok
        and all(not v for v in leave_one.values())
    )

    print("MQR471_GENERATIVE_QUOTIENT="+("PASS" if ok else "FAIL"))
    print("MQR471_RAW_STATES="+str(len(STATES)))
    print("MQR471_PREDICTIVE_CLASSES="+str(len(sig_classes)))
    print("MQR471_MINIMAL_FEATURE_COUNT="+str(minimal_size))
    print("MQR471_MINIMAL_FEATURE_SET="+";".join(",".join(x) for x in minimal))
    print("MQR471_CURRENT_ENVELOPE_DROPPED="+("YES" if all("current_envelope" not in x for x in minimal) else "NO"))
    print("MQR471_REVISION_STATE_DROPPED="+("YES" if all("revision_state" not in x for x in minimal) else "NO"))
    print("MQR471_ANCESTRY_DROPPED="+("YES" if all("ancestry_label" not in x for x in minimal) else "NO"))
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
