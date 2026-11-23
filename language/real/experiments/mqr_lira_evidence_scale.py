"""MQR 5.4 R84: evidence-scale LIRA, distinct from task priority.

These are auditable *declared expert ratings*, not probabilities, Bayesian
posteriors, independent refereeing or empirical calibrations. A missing
witness stays null, never silently counted as 0.5.
"""
from __future__ import annotations
import json
from decimal import Decimal as D, InvalidOperation

WEIGHTS = {"directness": D(".30"), "independence": D(".20"),
           "reproducibility": D(".20"), "discrimination": D(".20"),
           "scope_fit": D(".10")}
CLAIM_DIMENSIONS = ("support", "priority")
VERDICTS = {"SUPPORTED_IN_SCOPE", "CONDITIONAL", "HOLD", "COUNTEREVIDENCE"}


def number(value):
    try:
        v = D(str(value))
    except (ValueError, TypeError, InvalidOperation) as e:
        raise ValueError("invalid rating") from e
    if not v.is_finite() or not D(0) <= v <= D(1):
        raise ValueError("rating not finite 0..1")
    return v


def grade_evidence(item):
    if not item.get("id") or not item.get("source_uri"):
        raise ValueError("each witness requires id and source URI")
    if not set(WEIGHTS).issubset(item.get("axes", {})):
        raise ValueError("all evidence axes required")
    quality = sum((w*number(item["axes"][axis]) for axis,w in WEIGHTS.items()), D(0))
    return {"id": item["id"], "quality": str(quality),
            "raw_axes": item["axes"], "type": item["type"],
            "claim_scope": item["claim_scope"], "source_uri": item["source_uri"],
            "limitations": item["limitations"]}


def audit(payload):
    if payload.get("schema") != "MQR-LIRA-EVIDENCE-1.0":
        raise ValueError("wrong schema")
    evidence = payload["evidence"]
    claims = payload["claims"]
    evidence_ids = [r["id"] for r in evidence]
    if len(evidence_ids) != len(set(evidence_ids)):
        raise ValueError("duplicate evidence id")
    scores = {r["id"]: grade_evidence(r) for r in evidence}
    output = []
    ids = set()
    for c in claims:
        if c["id"] in ids:
            raise ValueError("duplicate claim")
        ids.add(c["id"])
        refs = c.get("evidence_ids", [])
        if not refs or any(r not in scores for r in refs):
            raise ValueError("missing concrete evidence")
        if not c.get("rationale") or not c.get("falsifier"):
            raise ValueError("unsupported decision narrative")
        if c["verdict"] not in VERDICTS:
            raise ValueError("invalid verdict")
        support = number(c["support"])
        priority = number(c["priority"])
        if c["verdict"] == "SUPPORTED_IN_SCOPE" and support < D(".7"):
            raise ValueError("unsupported verdict overstates declared support")
        if c.get("requires_primary") and not any(
            scores[r]["type"] == "PRIMARY_TEXT_READ" for r in refs):
            raise ValueError("primary evidence missing")
        output.append({
            "id": c["id"], "support": str(support),
            "priority": str(priority), "verdict": c["verdict"],
            "evidence_ids": refs,
            "evidence_qualities": {r: scores[r]["quality"] for r in refs},
            "rationale": c["rationale"], "falsifier": c["falsifier"],
            "claim_not_inferred_from_weighted_mean": True
        })
    return {"schema": payload["schema"], "evidence": list(scores.values()),
            "claims": output, "meaning": "declared audit ratings, not probability",
            "automatic_promotion": False}


def test():
    source = {"id":"P","source_uri":"urn:source","type":"PRIMARY_TEXT_READ",
              "claim_scope":"text says X","limitations":"no raw data",
              "axes":{k:"1" for k in WEIGHTS}}
    claim = {"id":"C","evidence_ids":["P"],"support":"0.90",
             "priority":"0.80","verdict":"SUPPORTED_IN_SCOPE",
             "requires_primary":True,"rationale":"direct quote","falsifier":"opposing first person text"}
    good = {"schema":"MQR-LIRA-EVIDENCE-1.0","evidence":[source],"claims":[claim]}
    assert audit(good)["evidence"][0]["quality"] == "1.00"
    assert audit(good)["claims"][0]["support"] == "0.90"
    invalids = [
        {**good,"evidence":[{**source,"axes":{**source["axes"],"directness":"NaN"}}]},
        {**good,"evidence":[{**source,"axes":{**source["axes"],"scope_fit":"1.1"}}]},
        {**good,"claims":[{**claim,"evidence_ids":["unknown"]}]},
        {**good,"claims":[{**claim,"support":"0.4"}]},
        {**good,"evidence":[source,source]},
        {**good,"claims":[{**claim,"requires_primary":True}],
         "evidence":[{**source,"type":"SECONDARY_ANALYSIS"}]},
    ]
    for payload in invalids:
        try:
            audit(payload)
        except ValueError:
            continue
        raise AssertionError("invalid evidence ledger passed")
    return {"result":"PASS_LIRA_EVIDENCE_1_0","negative_controls":len(invalids)}


if __name__=="__main__":
    print(test())
