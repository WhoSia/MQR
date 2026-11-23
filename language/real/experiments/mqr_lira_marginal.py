"""MQR LIRA marginal-opportunity correction, 2026-11-23.

Runs on a valid MQR-LIRA-1.0 result and a separate declared assessment
of remaining information gain. It does NOT treat a subjective priority as
probability or override evidence/feasibility gates. Never auto-releases
a paper or a physical experiment.
"""
from __future__ import annotations
from decimal import Decimal as D
import json
import sys

VALID_ACTIONS = {"ANALYZE_HELD_SOURCE", "ACQUIRE_MISSING_SOURCE",
                 "DESIGN_PROSPECTIVE_PROTOCOL"}
REQUIRED = {"task_id", "remaining_gain", "action", "justification", "evidence_refs"}


def marginal_audit(lira_output: dict, opportunities: dict) -> dict:
    if lira_output.get("schema") != "MQR-LIRA-1.0":
        raise ValueError("wrong LIRA schema")
    if opportunities.get("schema") != "MQR-LIRA-MARGINAL-1.0":
        raise ValueError("wrong marginal schema")
    base_rows = lira_output["ranking"]
    base_ids = [x["task_id"] for x in base_rows]
    if len(base_ids) != len(set(base_ids)):
        raise ValueError("duplicate base task")
    out = []
    seen = set()
    for item in opportunities["tasks"]:
        if not isinstance(item, dict) or not REQUIRED.issubset(item):
            raise ValueError("incomplete item")
        task_id = item["task_id"]
        if task_id in seen:
            raise ValueError("duplicate opportunity")
        seen.add(task_id)
        rem = D(str(item["remaining_gain"]))
        if not rem.is_finite() or not D(0) <= rem <= D(1):
            raise ValueError("remaining gain must be finite 0..1")
        if item["action"] not in VALID_ACTIONS:
            raise ValueError("invalid action")
        if not item["justification"] or not item["evidence_refs"]:
            raise ValueError("unsupported opportunity")
    if seen != set(base_ids):
        raise ValueError("task mismatch")
    by_id = {x["task_id"]: x for x in opportunities["tasks"]}
    for base in base_rows:
        task = by_id[base["task_id"]]
        current = D(base["current"])
        rem = D(str(task["remaining_gain"]))
        score = current*rem
        out.append({
            "task_id": base["task_id"],
            "base_priority": str(current),
            "declared_remaining_gain": str(rem),
            "marginal_opportunity": str(score),
            "next_action": task["action"],
            "evidence_refs": task["evidence_refs"],
            "justification": task["justification"],
            "release": base["promotion"]["status"],
        })
    out.sort(key=lambda x: (-D(x["marginal_opportunity"]), x["task_id"]))
    return {
        "schema": "MQR-LIRA-MARGINAL-1.0",
        "ranking": out,
        "warnings": ["subjective remaining-gain multiplier",
                     "unready source-acquisition and experiments are NOT execution-ready",
                     "model is an adversarial correction, not a new discovered scientific law"],
        "auto_authority_transfer": False,
    }


def self_test() -> dict:
    def base(id, score):
        return {"task_id": id, "current": score,
                "promotion": {"status": "HOLD"}}
    lira = {"schema": "MQR-LIRA-1.0", "ranking":
            [base("already-covered", "0.9"), base("new-gap", "0.6")]}
    opp = {"schema": "MQR-LIRA-MARGINAL-1.0", "tasks": [
        {"task_id":"already-covered","remaining_gain":"0.1",
         "action":"ANALYZE_HELD_SOURCE","evidence_refs":["A"],
         "justification":"most of this is already known"},
        {"task_id":"new-gap","remaining_gain":"0.9",
         "action":"ACQUIRE_MISSING_SOURCE","evidence_refs":["B"],
         "justification":"original data not yet available"}]}
    result = marginal_audit(lira,opp)
    assert result["ranking"][0]["task_id"] == "new-gap"
    assert result["ranking"][0]["marginal_opportunity"] == "0.54"
    assert all(x["release"]=="HOLD" for x in result["ranking"])
    for update in [
        lambda x: x["tasks"].append(dict(x["tasks"][0])),
        lambda x: x["tasks"][0].update(remaining_gain="1.1"),
        lambda x: x["tasks"][0].update(action="EXECUTE_UNAUTHORIZED"),
        lambda x: x["tasks"][1].update(evidence_refs=[]),
    ]:
        case=json.loads(json.dumps(opp))
        update(case)
        try:
            marginal_audit(lira,case)
        except ValueError:
            continue
        raise AssertionError("invalid opportunity accepted")
    return {"result":"PASS_MARGINAL_AUDIT", "negative_controls":4,
            "release_unchanged":"HOLD"}


if __name__ == "__main__":
    if len(sys.argv)==2 and sys.argv[1]=="--self-test":
        print(json.dumps(self_test(),sort_keys=True))
    elif len(sys.argv)==3:
        with open(sys.argv[1],encoding="utf-8") as f: base=json.load(f)
        with open(sys.argv[2],encoding="utf-8") as f: opp=json.load(f)
        print(json.dumps(marginal_audit(base,opp),ensure_ascii=False,indent=2))
    else:
        raise SystemExit("usage: mqr_lira_marginal.py --self-test | base-output.json opportunities.json")
