"""MQR LIRA 2: constitutional research portfolio guard.

LIRA numeric recommendations may reorder local *tasks* but may not remove
coverage of founding questions or protected cross-branch case studies.

This is research-governance code, NOT a measurement of scientific truth.
Deterministic, fail-closed, standard-library-only.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Iterable

FOUNDING = tuple(f"Q{i}" for i in range(1, 8))
REQUIRED_CASES = frozenset({
    "faraday-1831-1832",
    "bell-chsh-1969-1972",
    "cross-science-bridge",
})
VALID_STATES = frozenset({"ACTIVE", "DOCUMENTED_HOLD", "CLOSED_BY_EVIDENCE"})
VALID_ACTIONS = frozenset({
    "READ_PRIMARY",
    "COMPARE_RIVALS",
    "BUILD_TEST",
    "DESIGN_PROTOCOL_ONLY",
    "SOURCE_ACQUISITION",
    "SOURCE_HOLD",
})


@dataclass(frozen=True)
class WorkItem:
    id: str
    questions: tuple[str, ...]
    case_id: str
    state: str
    action: str
    source_ids: tuple[str, ...]
    rationale: str
    local_priority: str | None = None

    def __post_init__(self):
        if not self.id or not self.rationale or not self.case_id:
            raise ValueError("item requires identity, case and rationale")
        if not self.questions or set(self.questions) - set(FOUNDING):
            raise ValueError("missing or invalid founding questions")
        if self.state not in VALID_STATES or self.action not in VALID_ACTIONS:
            raise ValueError("invalid state/action")
        if self.state == "CLOSED_BY_EVIDENCE" and not self.source_ids:
            raise ValueError("closure requires direct documented evidence")
        if self.state == "DOCUMENTED_HOLD" and not self.source_ids:
            raise ValueError("hold requires at least a blocker/attempt record")
        if self.local_priority is not None:
            try:
                value = Decimal(self.local_priority)
            except (InvalidOperation, TypeError) as e:
                raise ValueError("invalid operational score") from e
            if not value.is_finite() or not 0 <= value <= 1:
                raise ValueError("score out of bounds")


def audit_portfolio(items: Iterable[WorkItem]) -> dict:
    entries = list(items)
    if len({item.id for item in entries}) != len(entries):
        raise ValueError("duplicate item IDs")
    covered = {
        q: sorted(item.id for item in entries
                  if q in item.questions and item.state != "CLOSED_BY_EVIDENCE")
        for q in FOUNDING
    }
    missing_q = sorted(q for q in FOUNDING if not covered[q])
    cases = {
        c: sorted(item.id for item in entries
                  if item.case_id == c and item.state != "CLOSED_BY_EVIDENCE")
        for c in REQUIRED_CASES
    }
    missing_case = sorted(c for c in REQUIRED_CASES if not cases[c])
    unsupported_closure = [
        item.id for item in entries
        if item.state == "CLOSED_BY_EVIDENCE"
        and any(q not in FOUNDING for q in item.questions)
    ]
    return {
        "constitutional_status": "HOLD" if missing_q or missing_case or unsupported_closure else "COVERED",
        "question_coverage": covered,
        "protected_case_coverage": cases,
        "missing_questions": missing_q,
        "missing_protected_cases": missing_case,
        "release_authority": "NEVER_BY_LIRA_SCORE",
        "does_not_prove_independent_novelty": True,
    }


def test() -> dict:
    items = [
        WorkItem("f", ("Q3", "Q4", "Q7"), "faraday-1831-1832",
                 "ACTIVE", "READ_PRIMARY", ("1831-publication",), "chronology"),
        WorkItem("b", ("Q5", "Q6"), "bell-chsh-1969-1972",
                 "ACTIVE", "COMPARE_RIVALS", ("CHSH-1969",), "measurement bridge"),
        WorkItem("a", ("Q1", "Q2", "Q6"), "cross-science-bridge",
                 "DOCUMENTED_HOLD", "SOURCE_HOLD",
                 ("paired-original-not-acquired",), "empirical bridge pending"),
        WorkItem("m", ("Q5", "Q7"), "math-selection",
                 "ACTIVE", "COMPARE_RIVALS", ("Wigner-1960",), "math applicability"),
    ]
    assert audit_portfolio(items)["constitutional_status"] == "COVERED"
    assert audit_portfolio([x for x in items if x.id != "f"])["constitutional_status"] == "HOLD"
    assert audit_portfolio([x for x in items if x.id != "a"])["constitutional_status"] == "HOLD"
    assert audit_portfolio([x for x in items if x.id != "b"])["constitutional_status"] == "HOLD"
    assert audit_portfolio([*items, WorkItem("x", ("Q1",), "extra", "ACTIVE",
                                            "BUILD_TEST", (), "unrated", "1.0")])["constitutional_status"] == "COVERED"
    try:
        WorkItem("bad", ("Q1",), "faraday-1831-1832", "CLOSED_BY_EVIDENCE",
                 "READ_PRIMARY", (), "unsupported")
    except ValueError:
        pass
    else:
        raise AssertionError("unsupported closure accepted")
    return {"status": "PASS_PORTFOLIO_GUARD", "fail_closed_negative_controls": 4,
            "founding_questions": 7, "protected_cases": 3}


if __name__ == "__main__":
    print(test())
