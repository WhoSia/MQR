"""MQR 5.4: a non-promoting, bounded cross-science bridge audit.

This is NOT canonical Real-Language syntax and never certifies ontology.
Inputs are declared evidence receipts; their physical truth is not verified here.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class State(str, Enum):
    HOLD_NO_COMMON_OPERATION = "HOLD_NO_COMMON_OPERATION"
    HOLD_UNVERIFIED_ANCHOR = "HOLD_UNVERIFIED_ANCHOR"
    HOLD_SHARED_ANCESTRY = "HOLD_SHARED_ANCESTRY"
    HOLD_NO_CASES = "HOLD_NO_CASES"
    FAIL_SCOPED_MISMATCH = "FAIL_SCOPED_MISMATCH"
    BOUNDED_OPERATIONAL_MATCH = "BOUNDED_OPERATIONAL_MATCH"


@dataclass(frozen=True)
class PairedReceipt:
    case_id: str
    left_output: str
    right_output: str
    comparable: bool
    common_operation_witness: bool
    independent_calibration_witness: bool
    ancestry_divergence_witness: bool


@dataclass(frozen=True)
class Audit:
    state: State
    matched: int
    mismatched: int
    unresolved: int
    scope: tuple[str, ...]
    caveat: str = "Never infer complete translation or shared ontology from this result."


def audit(receipts: Iterable[PairedReceipt]) -> Audit:
    """Evaluate a *declared*, finite correspondence, without creating evidence."""
    seen: set[str] = set()
    records = list(receipts)
    for r in records:
        if not r.case_id or r.case_id in seen:
            raise ValueError("case IDs must be distinct and nonempty")
        seen.add(r.case_id)
    if not records:
        return Audit(State.HOLD_NO_CASES, 0, 0, 0, ())

    matched = mismatched = unresolved = 0
    missing_operation = missing_calibration = shared_ancestry = False
    for r in records:
        if not r.common_operation_witness or not r.comparable:
            unresolved += 1
            missing_operation = True
        elif not r.independent_calibration_witness:
            unresolved += 1
            missing_calibration = True
        elif not r.ancestry_divergence_witness:
            unresolved += 1
            shared_ancestry = True
        elif r.left_output != r.right_output:
            mismatched += 1
        else:
            matched += 1

    if mismatched:
        state = State.FAIL_SCOPED_MISMATCH
    elif missing_operation:
        state = State.HOLD_NO_COMMON_OPERATION
    elif missing_calibration:
        state = State.HOLD_UNVERIFIED_ANCHOR
    elif shared_ancestry:
        state = State.HOLD_SHARED_ANCESTRY
    else:
        state = State.BOUNDED_OPERATIONAL_MATCH
    return Audit(state, matched, mismatched, unresolved, tuple(r.case_id for r in records))
