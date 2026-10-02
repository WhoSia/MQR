#!/usr/bin/env python3
import csv, pathlib
from collections import defaultdict

ROOT=pathlib.Path(__file__).resolve().parent

def read_tsv(path):
    with open(path,newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

CONTACTS={r["contact_id"]:r for r in read_tsv(ROOT/"CONTACT-FREEZE.tsv")}
STATES={r["state_id"]:r for r in read_tsv(ROOT/"STATE-FREEZE.tsv")}
CASES=read_tsv(ROOT/"TRIGGER-FREEZE.tsv")

def gens(state):
    return set(x for x in state["generators"].split(",") if x)

def transition(state,trigger):
    gs=gens(state)
    if trigger=="RIVAL_ENTRY":
        if "RIVAL" in gs:
            return ("RIVAL_X","NEW_SEPARATOR","DOWNGRADE")
        return ("NONE","NO_NEW_CONTACT","UNCHANGED")
    if trigger=="TECH_UNLOCK":
        if "INSTRUMENT" not in gs:
            return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        if state["tech_state"]=="T1":
            return ("INST_Z","NEW_SEPARATOR","DOWNGRADE")
        return ("NONE","RELEVANT_BUT_UNREALIZABLE","UNCHANGED")
    if trigger=="ETHICS_REVIEW":
        if "EXTERNAL" not in gs:
            return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        if state["ethics_state"]=="E1":
            return ("ETH_H","EXECUTION_PERMISSION_CHANGED","DOWNGRADE")
        return ("NONE","ETH_H_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED")
    if trigger=="BUDGET_UNLOCK":
        if "EXTERNAL" not in gs:
            return ("NONE","NO_NEW_CONTACT","UNCHANGED")
        if state["budget_state"]=="HIGH":
            return ("COST_Q","EXECUTION_FEASIBILITY_CHANGED","DOWNGRADE")
        return ("NONE","COST_Q_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED")
    raise ValueError(trigger)

def future_signature(state):
    return tuple(transition(state,t) for t in ["RIVAL_ENTRY","TECH_UNLOCK","ETHICS_REVIEW","BUDGET_UNLOCK"])

def compact_state(state):
    return (
        tuple(sorted(gens(state))),
        state["tech_state"],
        state["budget_state"],
        state["ethics_state"],
        state["revision_state"],
    )

def main():
    mismatches=[]
    rows=[]
    for c in CASES:
        s=STATES[c["state_id"]]
        got=transition(s,c["trigger"])
        exp=(c["expected_admission"],c["expected_scientific_status"],c["expected_closure_effect"])
        rows.append((c["case_id"],c["state_id"],c["trigger"],*got,*exp))
        if got!=exp:
            mismatches.append((c["case_id"],got,exp))

    current_envs={s["current_envelope"] for s in STATES.values()}
    same_current_envelope=(len(current_envs)==1)

    sig_theory=future_signature(STATES["S_THEORY"])
    sig_plural=future_signature(STATES["S_PLURAL"])
    current_envelope_insufficient=(sig_theory!=sig_plural)

    ancestry_null=(future_signature(STATES["S_PLURAL"])==future_signature(STATES["S_PLURAL_ALT"]))
    compact_equal=(compact_state(STATES["S_PLURAL"])==compact_state(STATES["S_PLURAL_ALT"]))
    compact_sufficiency_on_frozen_states=True
    by_compact=defaultdict(set)
    for s in STATES.values():
        by_compact[compact_state(s)].add(future_signature(s))
    if any(len(v)>1 for v in by_compact.values()):
        compact_sufficiency_on_frozen_states=False

    theory_self_seals=(transition(STATES["S_THEORY"],"RIVAL_ENTRY")[0]=="NONE")
    plural_admits_rival=(transition(STATES["S_PLURAL"],"RIVAL_ENTRY")[0]=="RIVAL_X")

    ethics_separation=(
        CONTACTS["ETH_H"]["scientific_split"]=="YES"
        and CONTACTS["ETH_H"]["permission"]=="BLOCKED_ETHICS"
        and transition(STATES["S_PLURAL"],"ETHICS_REVIEW")[0]=="NONE"
        and transition(STATES["S_PLURAL"],"ETHICS_REVIEW")[1]=="ETH_H_STILL_SCIENTIFICALLY_RELEVANT"
    )

    cost_separation=(
        CONTACTS["COST_Q"]["scientific_split"]=="YES"
        and CONTACTS["COST_Q"]["cost_state"]=="HIGH"
        and transition(STATES["S_PLURAL"],"BUDGET_UNLOCK")[0]=="NONE"
        and transition(STATES["S_PLURAL"],"BUDGET_UNLOCK")[1]=="COST_Q_STILL_SCIENTIFICALLY_RELEVANT"
    )

    tech_unlock=(
        transition(STATES["S_PLURAL"],"TECH_UNLOCK")[0]=="NONE"
        and transition(STATES["S_TECH1"],"TECH_UNLOCK")[0]=="INST_Z"
    )

    downgrade_cases=sum(1 for c in CASES if c["expected_closure_effect"]=="DOWNGRADE")

    out=ROOT/"results";out.mkdir(exist_ok=True)
    with open(out/"envelope_court.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["case_id","state_id","trigger","got_admission","got_status","got_closure","expected_admission","expected_status","expected_closure"])
        w.writerows(rows)

    with open(out/"envelope_summary.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["metric","value"])
        metrics=[
            ("CASE_MISMATCHES",len(mismatches)),
            ("SAME_CURRENT_ENVELOPE",same_current_envelope),
            ("CURRENT_ENVELOPE_INSUFFICIENT",current_envelope_insufficient),
            ("THEORY_ONLY_SELF_SEALS",theory_self_seals),
            ("PLURAL_GENERATOR_ADMITS_RIVAL",plural_admits_rival),
            ("ANCESTRY_NULL",ancestry_null),
            ("COMPACT_STATE_EQUAL_FOR_ANCESTRY_NULL",compact_equal),
            ("COMPACT_STATE_SUFFICIENT_ON_FROZEN_STATES",compact_sufficiency_on_frozen_states),
            ("ETHICS_EPISTEMIC_SEPARATION",ethics_separation),
            ("COST_EPISTEMIC_SEPARATION",cost_separation),
            ("TECHNOLOGY_UNLOCK",tech_unlock),
            ("DOWNGRADE_CASES",downgrade_cases),
        ]
        for k,v in metrics:w.writerow([k,str(v).upper() if isinstance(v,bool) else v])

    ok=(
        not mismatches and same_current_envelope and current_envelope_insufficient
        and theory_self_seals and plural_admits_rival
        and ancestry_null and compact_equal and compact_sufficiency_on_frozen_states
        and ethics_separation and cost_separation and tech_unlock
        and downgrade_cases>=4
    )

    print("MQR471_ENVELOPE_COURT="+("PASS" if ok else "FAIL"))
    print("MQR471_CURRENT_ENVELOPE_INSUFFICIENT="+("YES" if current_envelope_insufficient else "NO"))
    print("MQR471_THEORY_ONLY_SELF_SEALS="+("YES" if theory_self_seals else "NO"))
    print("MQR471_PLURAL_GENERATOR_ADMITS_RIVAL="+("YES" if plural_admits_rival else "NO"))
    print("MQR471_ANCESTRY_NULL="+("YES" if ancestry_null else "NO"))
    print("MQR471_COMPACT_STATE_SUFFICIENT="+("YES" if compact_sufficiency_on_frozen_states else "NO"))
    print("MQR471_ETHICS_EPISTEMIC_SEPARATION="+("YES" if ethics_separation else "NO"))
    print("MQR471_COST_EPISTEMIC_SEPARATION="+("YES" if cost_separation else "NO"))
    print("MQR471_TECHNOLOGY_UNLOCK="+("YES" if tech_unlock else "NO"))
    print("MQR471_DOWNGRADE_CASES="+str(downgrade_cases))
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
