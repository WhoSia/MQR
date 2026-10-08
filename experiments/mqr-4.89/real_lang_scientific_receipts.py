"""MQR-4.89 Real Lang empirical-contact prototype.

Typed evidence state, NOT a scientific claim validator.
Reports from Kapoor and Narayanan (2023) are separately labeled
SOURCE_REPORTED; synthetic test fixtures are SYNTHETIC.
"""
from dataclasses import dataclass
from enum import Enum

class Origin(str, Enum):
    SYNTHETIC = "SYNTHETIC"
    SOURCE_REPORTED = "SOURCE_REPORTED"
    INDEPENDENTLY_REPLICATED = "INDEPENDENTLY_REPLICATED"

class Verdict(str, Enum):
    HOLD = "HOLD"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    DENIED_SCOPE = "DENIED_SCOPE"
    WARRANTED_WITHIN_RECEIPT = "WARRANTED_WITHIN_RECEIPT"

@dataclass(frozen=True)
class Receipt:
    claim: str
    origin: Origin
    split_audited: bool
    leakage_found: bool
    defect_resolved: bool
    scope_authorized: bool
    independently_replicated: bool
    previously_relied_on: bool

@dataclass(frozen=True)
class Judgment:
    verdict: Verdict
    review_required: bool
    evidence_origin: Origin
    reason: str

def adjudicate(r: Receipt) -> Judgment:
    if not r.scope_authorized:
        return Judgment(Verdict.DENIED_SCOPE, r.previously_relied_on,
                        r.origin, "Requested use lacks scope authorization")
    if r.leakage_found and not r.defect_resolved:
        return Judgment(Verdict.REVIEW_REQUIRED, True, r.origin,
                        "Uncorrected leakage defeats the supplied evaluation receipt")
    if not r.split_audited:
        return Judgment(Verdict.HOLD, r.previously_relied_on, r.origin,
                        "Data-split / leakage controls unverified")
    if r.origin != Origin.INDEPENDENTLY_REPLICATED or not r.independently_replicated:
        return Judgment(Verdict.HOLD, r.previously_relied_on, r.origin,
                        "Audit cannot infer independent validation from a paper report")
    return Judgment(Verdict.WARRANTED_WITHIN_RECEIPT, False,
                    r.origin, "Independently replicated within stated evaluation scope")

def run_tests():
    base = dict(claim="model generalization",origin=Origin.SYNTHETIC,
                split_audited=True, leakage_found=False, defect_resolved=False,
                scope_authorized=True, independently_replicated=False,
                previously_relied_on=False)
    cases = [
        ("S1_missing_audit", {"split_audited":False}, Verdict.HOLD,False),
        ("S2_report_only", {}, Verdict.HOLD,False),
        ("S3_leakage_detected", {"leakage_found":True}, Verdict.REVIEW_REQUIRED,True),
        ("S4_leakage_on_reliance", {"leakage_found":True,"previously_relied_on":True},Verdict.REVIEW_REQUIRED,True),
        ("S5_corrected_but_unreplicated", {"leakage_found":True,"defect_resolved":True},Verdict.HOLD,False),
        ("S6_scope_denied", {"scope_authorized":False},Verdict.DENIED_SCOPE,False),
        ("S7_replicated", {"origin":Origin.INDEPENDENTLY_REPLICATED,"independently_replicated":True},Verdict.WARRANTED_WITHIN_RECEIPT,False),
        ("S8_claimed_replication_unattested", {"independently_replicated":True},Verdict.HOLD,False),
        ("S9_reported_paper", {"origin":Origin.SOURCE_REPORTED},Verdict.HOLD,False),
        ("S10_unaudited_replicate", {"origin":Origin.INDEPENDENTLY_REPLICATED,"independently_replicated":True,"split_audited":False},Verdict.HOLD,False),
    ]
    for name, edits, verdict, review in cases:
        outcome=adjudicate(Receipt(**(base|edits)))
        assert (outcome.verdict,outcome.review_required)==(verdict,review),(name,outcome)
    print("MQR489_SYNTHETIC_FIXTURES=10")
    print("MQR489_SYNTHETIC_PASS=10")
    print("MQR489_EMPIRICAL_REPLICATION=NOT_PERFORMED")

if __name__=="__main__":
    run_tests()
