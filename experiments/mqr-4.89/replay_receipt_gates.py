"""Deprecated MQR-4.89 v1 API. Fail closed: metadata is not an execution receipt.

Use replay_receipt_gates_v2.py for actual byte-backed artifacts.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    doi: str
    claim: str
    data_digest: str | None
    code_digest: str | None
    executed: bool
    source_reported: bool
    attestation: str | None

def classify(r: Evidence) -> str:
    if not r.source_reported:
        return "UNKNOWN_SOURCE"
    if not r.data_digest or not r.code_digest:
        return "SOURCE_REPORTED_NOT_REPLAYED"
    # Metadata alone cannot validate bytes, execution or attestation.
    return "LEGACY_METADATA_UNVERIFIED"

def test():
    base = dict(doi="10.24433/CO.4899453.v1", claim="civil-war leakage reanalysis",
                data_digest=None, code_digest=None, executed=False,
                source_reported=True, attestation=None)
    cases = [
        ({}, "SOURCE_REPORTED_NOT_REPLAYED"),
        ({"data_digest":"a"}, "SOURCE_REPORTED_NOT_REPLAYED"),
        ({"code_digest":"b"}, "SOURCE_REPORTED_NOT_REPLAYED"),
        ({"data_digest":"a","code_digest":"b"}, "LEGACY_METADATA_UNVERIFIED"),
        ({"data_digest":"a","code_digest":"b","executed":True}, "LEGACY_METADATA_UNVERIFIED"),
        ({"data_digest":"a","code_digest":"b","executed":True,"attestation":"review"}, "LEGACY_METADATA_UNVERIFIED"),
        ({"source_reported":False}, "UNKNOWN_SOURCE"),
    ]
    for patch, expected in cases:
        assert classify(Evidence(**(base | patch))) == expected
    print("MQR489_LEGACY_FAIL_CLOSED_PASS=7")
    print("MQR489_REAL_DATA_REPLAY=NOT_PERFORMED")

if __name__ == "__main__":
    test()
