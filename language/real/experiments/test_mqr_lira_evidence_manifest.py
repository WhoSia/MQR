"""MQR 5.4 R97: audit current E/C/L/G manifests and shared evidentiary ancestry.

Read-only repo-root deterministic validator; all arithmetic uses Decimal.
Scores are declared research judgments, NOT objective probabilities.
No package imports outside the Python standard library.
"""
from __future__ import annotations
from decimal import Decimal as D
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "research" / "data"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def check():
    ledger = load("mqr_lira_evidence_claim_decision_scores_R95.json")
    family = load("mqr_lira_20261123_source_dependency_families_R95.json")
    macro = load("mqr_lira_20261123_seven_question_macro_evidence_audit.json")
    scope_split = load("mqr_lira_20261123_seven_question_scope_split_R96.json")
    metadata = load("mqr_faraday_second_series_dec1831_jan1832_version_paradox.json")
    assert ledger["schema"] == "MQR-LIRA-EVIDENCE-1.0"
    weights = {k: D(str(v)) for k, v in ledger["weights"].items()}
    assert sum(weights.values()) == 1
    source_ids = {s["id"] for s in ledger["evidence"]}
    assert len(source_ids) == len(ledger["evidence"]) == 27
    source_families = family["evidence_to_family"]
    assert set(source_families) == source_ids
    assert len(set(source_families.values())) == 21
    for source in ledger["evidence"]:
        assert source["source_uri"] and source["limitations"]
        score = sum((weights[k]*D(str(source["axes"][k])) for k in weights), D(0))
        assert D(0) <= score <= D(1)
        assert all(D(0) <= D(str(source["axes"][k])) <= D(1) for k in weights)
    ids = set()
    sharing = {}
    for claim in ledger["claims"]:
        assert claim["id"] not in ids
        ids.add(claim["id"])
        assert claim["evidence_ids"] and set(claim["evidence_ids"]) <= source_ids
        assert D(0) <= D(claim["support"]) <= D(1)
        assert D(0) <= D(claim["priority"]) <= D(1)
        assert claim["rationale"] and claim["falsifier"]
        assert claim["verdict"] in ("SUPPORTED_IN_SCOPE", "HOLD", "COUNTEREVIDENCE", "CONDITIONAL")
        if claim["verdict"] == "SUPPORTED_IN_SCOPE":
            assert D(claim["support"]) >= D(".7")
        if claim["requires_primary"]:
            assert any(next(e for e in ledger["evidence"] if e["id"] == src)["type"] == "PRIMARY_TEXT_READ"
                       for src in claim["evidence_ids"])
        groups = {source_families[src] for src in claim["evidence_ids"]}
        if len(groups) < len(claim["evidence_ids"]):
            sharing[claim["id"]] = {
                "citations": len(claim["evidence_ids"]),
                "conservative_families": len(groups)
            }
    assert len(ids) == len(ledger["claims"]) == 42
    assert set(sharing) >= {"C02"}
    assert sorted(row["question"] for row in macro["rows"]) == [f"Q{i}" for i in range(1,8)]
    mw = {k:D(str(v)) for k,v in macro["weights"].items()}
    assert sum(mw.values()) == 1
    for row in macro["rows"]:
        val = sum((mw[k]*D(str(row["evidence_dimensions"][k])) for k in mw), D(0))
        assert abs(val-D(row["declared_evidence_quality"])) <= D(".0005")
        assert all(D(0)<=D(row[x])<=D(1) for x in ("support","research_retention_priority"))
        assert row["evidence_ids"] and row["falsifier"] and row["limitation"]
    assert scope_split["schema"] == "MQR-LIRA-FOUNDING-SCOPE-SPLIT-1.0"
    assert len(scope_split["founding_questions"]) == 7
    split_ids = {x["question"] for x in scope_split["founding_questions"]}
    assert split_ids == {f"Q{i}" for i in range(1, 8)}
    for row in scope_split["founding_questions"]:
        assert row["source_ids"] and set(row["source_ids"]) <= source_ids
        assert row["scope_barrier"]
        for k in ("bounded_evidence_quality", "bounded_claim_support",
                  "generalized_answer_support", "continuation_priority"):
            assert D(0) <= D(row[k]) <= D(1)
        assert D(row["generalized_answer_support"]) <= D(row["bounded_claim_support"])
        assert row["independent_validation_status"] == "HOLD"
    assert not scope_split["general_theory_authority_transfer"]
    assert metadata["next_direct_test"]["access_status"].startswith("ARCHIVE_CATALOG")
    return {
        "status": "PASS_LIRA_MANIFEST_CONSISTENCY",
        "witness_records": len(source_ids),
        "source_families": len(set(source_families.values())),
        "claims_and_director_decisions": len(ids),
        "founding_questions": len(macro["rows"]),
        "scope_split_questions": len(scope_split["founding_questions"]),
        "general_theory_promoted": False,
        "overlapping_source_claims": sharing,
        "scientific_version": "5.4_OPEN",
        "promote_by_score": False,
        "real_world_data_newly_obtained": False,
    }


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, sort_keys=True, indent=2))
