"""P5 synthetic appeal capacity contract. No real-world remedial authority inferred."""
def audit(c):
    required=("id","origin","receives_objection","can_reopen_question","can_require_evidence","can_revise_rule","remedy_recorded","outcome_observed","mandate_source","dissent_preserved")
    required=tuple(x.replace(" ","") for x in required)
    missing=[x for x in required if x not in c]
    if missing:return "HOLD_MISSING_FIELDS"
    if c["origin"]!="CONSTRUCTED":return "HOLD_UNVERIFIED_ORIGIN"
    if not c["receives_objection"]:return "NO_ACCESS"
    if not c["dissent_preserved"]:return "HOLD_DISSENT_ERASED"
    if not c["mandate_source"]:return "HOLD_MANDATE"
    if not c["can_reopen_question"]:return "HEARING_WITHOUT_REOPENING"
    if not (c["can_require_evidence"] or c["can_revise_rule".replace(" ","")]):return "REOPENING_WITHOUT_REMEDY_POWER"
    if not c["remedy_recorded"]:return "REMEDY_POSSIBLE_NOT_EXERCISED"
    if not c["outcome_observed"]:return "REMEDY_RECORDED_OUTCOME_UNVERIFIED"
    return "CONDITIONAL_REMEDY_OBSERVED_IN_FIXTURE"

def make(**changes):
    x=dict(id="test",origin="CONSTRUCTED",receives_objection=True,can_reopen_question=True,
      can_require_evidence=True,can_revise_rule=True,remedy_recorded=True,outcome_observed=True,
      mandate_source="assumed hypothetical external mandate",dissent_preserved=True)
    x.update(changes);return x

def test():
    scenarios=[
        (make(),"CONDITIONAL_REMEDY_OBSERVED_IN_FIXTURE"),
        (make(receives_objection=False),"NO_ACCESS"),
        (make(can_reopen_question=False),"HEARING_WITHOUT_REOPENING"),
        (make(can_require_evidence=False,can_revise_rule=False),"REOPENING_WITHOUT_REMEDY_POWER"),
        (make(remedy_recorded=False),"REMEDY_POSSIBLE_NOT_EXERCISED"),
        (make(outcome_observed=False),"REMEDY_RECORDED_OUTCOME_UNVERIFIED"),
        (make(dissent_preserved=False),"HOLD_DISSENT_ERASED"),
        (make(mandate_source=""),"HOLD_MANDATE"),
    ]
    for i,(record,expected) in enumerate(scenarios,1):
        got=audit(record)
        assert got==expected,(i,got,expected)
        print(i,got)
    print("PASS: 8 synthetic remedial-capacity fixtures, not institutional validation")
if __name__=="__main__":test()
