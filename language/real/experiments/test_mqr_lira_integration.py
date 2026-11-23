"""MQR LIRA integration regression checks; no network, standard library only.

Run from repository root:
    python language/real/experiments/test_mqr_lira_integration.py
Does NOT infer that analytical score estimates are empirical probabilities.
"""
from decimal import Decimal as D
from itertools import product
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "research" / "data"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from mqr_lira_audit import load_and_audit, self_test as lira_self_test, DIMENSIONS, WEIGHTS
from mqr_lira_marginal import marginal_audit, self_test as marginal_self_test


def read(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


def run():
    assert lira_self_test()["result"] == "PASS_LIRA_1_0"
    assert marginal_self_test()["result"] == "PASS_MARGINAL_AUDIT"
    first = load_and_audit(read("mqr_lira_20261123_initial_assessments.json"))
    revised = load_and_audit(read("mqr_lira_20261123_revised_assessments.json"))
    opp = read("mqr_lira_20261123_remaining_gain.json")
    marginal = marginal_audit(revised, opp)
    original = {r["task_id"]: D(r["current"]) for r in first["ranking"]}
    for row in revised["ranking"]:
        assert D(row["previous"]) == original[row["task_id"]]
        assert D(row["delta"]) == D(row["current"]) - original[row["task_id"]]
        assert row["promotion"]["status"] == "HOLD"
    assert len(revised["ranking"]) == 6
    assert revised["ranking"][0]["task_id"] == "hoagland1958_biochemical-functional-rival-audit"
    assert D(revised["ranking"][0]["current"]) == D("0.737")
    assert marginal["ranking"][0]["task_id"] == "paired-assay-same-specimen-measurement"
    assert D(marginal["ranking"][0]["marginal_opportunity"]) == D("0.50350")
    assert marginal["ranking"][0]["next_action"] == "DESIGN_PROSPECTIVE_PROTOCOL"
    assert all(row["release"] == "HOLD" for row in marginal["ranking"])

    # Not confidence intervals: bounded, deterministic perturbation of analyst weights.
    rows = read("mqr_lira_20261123_revised_assessments.json")["assessments"]
    winner_count = 0
    scenario_count = 0
    for offsets in product((D("-.05"), D(0), D(".05")), repeat=5):
        weights = tuple(w+o for w, o in zip(WEIGHTS, offsets))
        total = sum(weights)
        normalized = tuple(w/total for w in weights)
        for penalty in (D(".15"), D(".20"), D(".25")):
            ranked = sorted(rows, key=lambda r: -(
                sum(w*D(r["dimensions"][k]) for w,k in zip(normalized,DIMENSIONS))
                -penalty*D(r["risk"])))
            scenario_count += 1
            winner_count += ranked[0]["task_id"] == "hoagland1958_biochemical-functional-rival-audit"
    assert (scenario_count, winner_count) == (729, 729)

    claims = read("mqr_lira_20261123_high_risk_claim_audit.json")
    assert claims["schema"] == "MQR-LIRA-CLAIMS-1.0"
    assert len(claims["claims"]) == 10
    counts = {p: sum(c["severity"] == p for c in claims["claims"]) for p in ("P0","P1","P2","P3")}
    assert counts == {"P0":2,"P1":7,"P2":1,"P3":0}
    assert len({c["claim_id"] for c in claims["claims"]}) == 10
    assert all(c["accepted_narrow_claim"] and c["evidence_refs"]
               and D(c["urgency"]) >= 0 and D(c["urgency"]) <= 1
               for c in claims["claims"])

    return {"result": "PASS_MQR_LIRA_INTEGRATION",
            "tasks": 6, "claim_audits": 10,
            "P0":2,"P1":7,"P2":1,
            "weight_scenarios":scenario_count,
            "initial_winner_robust_scenarios":winner_count,
            "after_marginal_top":"paired-assay-same-specimen-measurement",
            "no_auto_promotion":True}


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, sort_keys=True))
