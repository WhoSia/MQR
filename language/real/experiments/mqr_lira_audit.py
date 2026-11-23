"""MQR LIRA 1.0: localized iterative recommendation audit.

Operational 0..1 priority/retention score, NOT a truth probability.
All dimension ratings are declared analyst judgments, not independently
measured physical quantities. Missing prior assessments remain null.
No average can override hard evidence gates for theory promotion.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal as D
from typing import Optional
import json
import sys

DIMENSIONS = ("expected_discrimination", "source_access", "rival_severity",
              "novelty_headroom", "execution_feasibility")
WEIGHTS = tuple(map(D, ("0.30", "0.25", "0.20", "0.15", "0.10")))
PENALTY = D("0.20")
RELEASE_GATES = ("primary_source_read", "reproduction_verified",
                 "independent_real_data", "strong_rival_compared",
                 "independent_external_review")


@dataclass(frozen=True)
class Assessment:
    task_id: str
    dimensions: tuple[D, D, D, D, D]
    risk: D
    prior: Optional[D]
    evidence_ids: tuple[str, ...]
    gates: dict[str, Optional[str]]

    def __post_init__(self):
        if not self.task_id:
            raise ValueError("empty task id")
        if len(self.dimensions) != 5 or any(not x.is_finite() or x < 0 or x > 1 for x in self.dimensions):
            raise ValueError("dimensions must be finite 0..1")
        if not self.risk.is_finite() or not D(0) <= self.risk <= D(1):
            raise ValueError("risk must be finite 0..1")
        if self.prior is not None and (not self.prior.is_finite() or not D(0) <= self.prior <= D(1)):
            raise ValueError("prior must be null or finite 0..1")
        if set(self.gates) != set(RELEASE_GATES):
            raise ValueError("missing/extra release gates")
        if any(x is not None and (not isinstance(x, str) or not x.strip()) for x in self.gates.values()):
            raise ValueError("passed gate requires nonempty evidence identifier")

    def priority(self) -> D:
        raw = sum((w*d for w, d in zip(WEIGHTS, self.dimensions)), D(0))
        return max(D(0), raw - PENALTY*self.risk)

    def recommendation(self) -> str:
        value = self.priority()
        if value >= D("0.80"):
            return "PRIORITIZE_PILOT"
        if value >= D("0.60"):
            return "CONDITIONAL_PILOT"
        return "DEFER_OR_REVISE"

    def release(self) -> dict:
        missing = sorted(k for k, v in self.gates.items() if v is None)
        return {
            "status": "HOLD" if missing else "ELIGIBLE_FOR_EXTERNAL_REVIEW_NOT_ACCEPTED",
            "missing": missing,
            "noncompensatory": True,
            "originality_inferred": False,
        }

    def record(self) -> dict:
        value = self.priority()
        return {
            "task_id": self.task_id,
            "dimensions": {key: str(v) for key, v in zip(DIMENSIONS, self.dimensions)},
            "risk": str(self.risk),
            "previous": None if self.prior is None else str(self.prior),
            "current": str(value),
            "delta": None if self.prior is None else str(value-self.prior),
            "status": self.recommendation(),
            "evidence_ids": list(self.evidence_ids),
            "promotion": self.release(),
            "score_is_probability": False,
        }


def load_and_audit(payload: dict) -> dict:
    if payload.get("schema") != "MQR-LIRA-1.0":
        raise ValueError("wrong schema")
    assessed = []
    seen = set()
    for entry in payload["assessments"]:
        task_id = entry["task_id"]
        if task_id in seen:
            raise ValueError("duplicate task")
        seen.add(task_id)
        assessed.append(Assessment(
            task_id,
            tuple(D(str(entry["dimensions"][key])) for key in DIMENSIONS),
            D(str(entry["risk"])),
            None if entry["previous"] is None else D(str(entry["previous"])),
            tuple(entry["evidence_ids"]), dict(entry["gates"])
        ))
    ranked = sorted(assessed, key=lambda a: (-a.priority(), a.task_id))
    return {
        "schema": "MQR-LIRA-1.0",
        "weights": {k: str(v) for k, v in zip(DIMENSIONS, WEIGHTS)},
        "risk_penalty": str(PENALTY),
        "ranking": [item.record() for item in ranked],
        "meaning": "operational recommendation; NOT truth probability",
        "version_promotion": "NEVER_BY_SCORE_ALONE",
    }


def self_test() -> dict:
    g = {k: None for k in RELEASE_GATES}
    a = Assessment("high-no-evidence", (D(1),)*5, D(0), None, (), g)
    assert a.priority() == 1
    assert a.release()["status"] == "HOLD"
    assert a.record()["delta"] is None
    b = Assessment("same-target", (D("0.8"),)*5, D("0.25"), D("0.70"), ("R67",),
                   {**g, "primary_source_read": "R67"})
    assert b.priority() == D("0.75")
    assert b.record()["delta"] == "0.05"
    assert b.recommendation() == "CONDITIONAL_PILOT"
    all_pass = Assessment("external-passed-synthetic", (D(1),)*5, D(0), None, (),
                          {k: "synthetic-id-"+k for k in RELEASE_GATES})
    assert all_pass.release()["status"] == "ELIGIBLE_FOR_EXTERNAL_REVIEW_NOT_ACCEPTED"
    for malformed in [
        lambda: Assessment("bad", (D("1.01"),)*5, D(0), None, (), g),
        lambda: Assessment("bad", (D("NaN"),)*5, D(0), None, (), g),
        lambda: Assessment("bad", (D(1),)*5, D(0), None, (), {}),
        lambda: Assessment("bad", (D(1),)*5, D(0), None, (), {**g, "primary_source_read": ""}),
        lambda: load_and_audit({"schema": "MQR-LIRA-1.0", "assessments": [
            {"task_id": "duplicated", "dimensions": {k: "1" for k in DIMENSIONS},
             "risk": "0", "previous": None, "evidence_ids": [], "gates": g}
        ]*2}),
    ]:
        try:
            malformed()
        except (ValueError, KeyError, TypeError):
            continue
        raise AssertionError("malformed input wrongly accepted")
    return {"result": "PASS_LIRA_1_0", "negative_controls": 5,
            "high_score_cannot_release_without_evidence": True}


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        print(json.dumps(self_test(), sort_keys=True))
    elif len(sys.argv) == 2:
        with open(sys.argv[1], encoding="utf-8") as f:
            print(json.dumps(load_and_audit(json.load(f)), ensure_ascii=False, indent=2))
    else:
        raise SystemExit("usage: python mqr_lira_audit.py --self-test | assessments.json")
