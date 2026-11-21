"""MQR 5.4 Real-Language experimental bridge: typed interfield evidence.
NOT an authority-bearing Real-Packet executor or Real-Lang grammar release.
All receipts are externally supplied assertions, NOT authenticated by this module.
"""
from dataclasses import dataclass

ALLOWED = frozenset(("SYNTHETIC","PUBLISHED_SUMMARY","SOURCE_RAW","INDEPENDENT_REPLAY"))
TARGETS = frozenset(("X_RAY_R_FREE","NMR_Q_RDC","LOCAL_TASK","CROSS_FIELD_TRANSPORT"))

@dataclass(frozen=True)
class EvidenceReceipt:
    receipt_id: str
    target: str
    source_kind: str
    source_id: str
    specimen_id: str
    regime_id: str
    lineage_id: str
    original_scope_retained: bool
    paired_target_verified: bool
    calibration_verified: bool
    independently_replayed: bool
    reported_pass: bool

    def __post_init__(self):
        if (not all(isinstance(x,str) and x.strip() for x in
                    (self.receipt_id,self.source_id,self.specimen_id,
                     self.regime_id,self.lineage_id)) or
            self.target not in TARGETS or self.source_kind not in ALLOWED or
            any(type(x) is not bool for x in
                (self.original_scope_retained,self.paired_target_verified,
                 self.calibration_verified,self.independently_replayed,
                 self.reported_pass))):
            raise ValueError("Malformed typed evidence receipt")
        if self.independently_replayed and self.source_kind != "INDEPENDENT_REPLAY":
            raise ValueError("Independent replay flag requires matching source type")

@dataclass(frozen=True)
class Claim:
    claim_id: str
    target: str
    specimen_id: str
    regime_id: str
    declared_lineages: tuple[str, ...]

    def __post_init__(self):
        if (not self.claim_id or self.target not in TARGETS or
            not self.specimen_id or not self.regime_id or
            not isinstance(self.declared_lineages, tuple) or
            not self.declared_lineages or
            any(not isinstance(s,str) or not s.strip()
                for s in self.declared_lineages) or
            len(set(self.declared_lineages)) != len(self.declared_lineages)):
            raise ValueError("Malformed claim or declared lineages")

def assess(claim, receipts):
    """Return an evidence-level description; never scientific truth PASS."""
    if not isinstance(claim, Claim):
        raise ValueError("Claim required")
    seen = set()
    rows = tuple(receipts)
    for r in rows:
        if not isinstance(r,EvidenceReceipt):
            raise ValueError("Receipt required")
        if r.receipt_id in seen:
            raise ValueError("Duplicate receipt ID")
        seen.add(r.receipt_id)
    relevant = tuple(r for r in rows
                     if r.target==claim.target and
                        r.specimen_id==claim.specimen_id and
                        r.regime_id==claim.regime_id)
    if not relevant:
        return "HOLD_TARGET_RECEIPT_ABSENT"
    if any(not r.original_scope_retained for r in relevant):
        return "HOLD_ORIGINAL_SCOPE_NOT_PRESERVED"
    if any(not r.paired_target_verified for r in relevant):
        return "HOLD_PHYSICAL_PAIRING_UNVERIFIED"
    if any(not r.calibration_verified for r in relevant):
        return "HOLD_CALIBRATION_UNVERIFIED"
    # Reported disagreements remain visible rather than allowing majority vote.
    if any(not r.reported_pass for r in relevant):
        return "REPORTED_CONTRADICTION_NEEDS_INDEPENDENT_ADJUDICATION"
    actual = set(r.lineage_id for r in relevant)
    if not set(claim.declared_lineages).issubset(actual):
        return "HOLD_DECLARED_LINEAGE_UNSUPPORTED"
    if any(r.source_kind=="SYNTHETIC" for r in relevant):
        return "SYNTHETIC_COMPATIBILITY_ONLY"
    if not any(r.independently_replayed for r in relevant):
        if any(r.source_kind=="SOURCE_RAW" for r in relevant):
            return "RAW_SOURCE_BYTES_CLAIMED_NOT_REPLAYED"
        return "PUBLISHED_COMPATIBILITY_NOT_REPLAYED"
    if len(actual) < 2:
        return "HOLD_NONCOMMON_ANCESTRY_UNVERIFIED"
    # The independence of a lineage *name* is not authenticated by code.
    return "BOUNDED_REPLAY_REPORTED_ANCESTRY_NOT_EXTERNALLY_CERTIFIED"
