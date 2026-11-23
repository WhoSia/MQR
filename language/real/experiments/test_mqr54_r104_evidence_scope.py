"""MQR R104: validate scoped LIRA evidence with complete provenance links.

No source citation is treated as an independent experiment merely because
multiple record IDs exist. All E, C, G, L entries are declared evaluations,
not scientific probabilities or confidence intervals. Standard library only.
"""
from __future__ import annotations
from decimal import Decimal as D, InvalidOperation
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
PATH=ROOT/"research"/"data"/"mqr54_r103_lira_q2_q5_crossbridge_evidence.json"
REQUIRED={"directness","independence","reproducibility","discrimination","scope_fit"}


def bounded(v):
    try:
        x=D(str(v))
    except (InvalidOperation,TypeError,ValueError) as err:
        raise ValueError("malformed score") from err
    if not x.is_finite() or not D(0)<=x<=D(1):
        raise ValueError("out-of-range/nonfinite score")
    return x


def validate(data:dict)->dict:
    if data.get("schema")!="MQR-LIRA-R99-R102-EVIDENCE-DECISIONS-1.0":
        raise ValueError("unexpected ledger version")
    weights=data["E_weights"]
    if set(weights)!=REQUIRED or sum((bounded(x) for x in weights.values()),D(0))!=1:
        raise ValueError("weight convention invalid")
    ev=data["evidence"]; claims=data["claims_and_director_decisions"]
    ids=[e["id"] for e in ev]
    if len(ids)!=len(set(ids)):
        raise ValueError("duplicate evidence id")
    by_id={e["id"]:e for e in ev}
    families=dict(data["dependencies"])
    if set(families)!=set(ids) or not all(families.values()):
        raise ValueError("source family map incomplete or duplicated")
    for e in ev:
        if set(e["axes"])!=REQUIRED or not all(e.get(x) for x in ("scope","uri","limitation","type")):
            raise ValueError("incomplete witness")
        score=sum((bounded(e["axes"][k])*bounded(weights[k]) for k in REQUIRED),D(0))
        if abs(score-bounded(e["quality"]))>D(".0005"):
            raise ValueError("E calculation mismatch")
    claim_ids=set()
    duplicate_source_groups={}
    for c in claims:
        if c["id"] in claim_ids:
            raise ValueError("duplicate claim")
        claim_ids.add(c["id"])
        if not c["evidence_ids"] or not set(c["evidence_ids"])<=set(ids):
            raise ValueError("claim cites missing evidence")
        if not c["rationale"] or not c["falsifier"]:
            raise ValueError("claim missing adversarial record")
        for axis in ("C","L","G"):
            bounded(c[axis])
        if c["verdict"] not in ("SUPPORTED_IN_SCOPE","HOLD","COUNTEREVIDENCE","CONDITIONAL"):
            raise ValueError("invalid verdict")
        if c["verdict"]=="SUPPORTED_IN_SCOPE" and bounded(c["C"])<D(".70"):
            raise ValueError("supported claim with weak declared support")
        overlap=len(c["evidence_ids"])-len(set(families[x] for x in c["evidence_ids"]))
        if overlap:
            duplicate_source_groups[c["id"]]=overlap
    if data.get("no_autopromotion") is not True or data["status"]!="5.4_OPEN":
        raise ValueError("evidence rating cannot promote the scientific version")
    return {"result":"PASS_MQR_R104_EVIDENCE_LEDGER",
            "witnesses":len(ev),"decisions":len(claims),
            "families":len(set(families.values())),
            "dependent_citation_overlap":duplicate_source_groups,
            "scientific_version":"5.4_OPEN"}


def test():
    data=json.loads(PATH.read_text(encoding="utf-8"))
    output=validate(data)
    assert (output["witnesses"],output["decisions"],output["families"])==(7,10,7)
    bad=json.loads(json.dumps(data));bad["evidence"][0]["axes"]["scope_fit"]="NaN"
    try:validate(bad)
    except ValueError:pass
    else:raise AssertionError("NaN accepted")
    bad=json.loads(json.dumps(data));bad["claims_and_director_decisions"][0]["evidence_ids"]=["unknown"]
    try:validate(bad)
    except ValueError:pass
    else:raise AssertionError("missing evidence accepted")
    bad=json.loads(json.dumps(data));bad["no_autopromotion"]=False
    try:validate(bad)
    except ValueError:pass
    else:raise AssertionError("unsourced promotion accepted")
    return {**output,"negative_controls":3}


if __name__=="__main__":
    print(json.dumps(test(),sort_keys=True))
