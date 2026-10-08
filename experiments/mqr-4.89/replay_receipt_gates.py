"""MQR 4.89 — deterministic research-receipt checks; not empirical reproduction."""
from dataclasses import dataclass
from hashlib import sha256

@dataclass(frozen=True)
class Evidence:
    doi:str
    claim:str
    data_digest:str|None
    code_digest:str|None
    executed:bool
    source_reported:bool
    attestation:str|None

def classify(r:Evidence):
    if not r.source_reported:
        return "UNKNOWN_SOURCE"
    if not r.data_digest or not r.code_digest:
        return "SOURCE_REPORTED_NOT_REPLAYED"
    if not r.executed:
        return "ARTIFACTS_IDENTIFIED_NOT_REPLAYED"
    if not r.attestation:
        return "REPLAY_UNATTESTED"
    return "REPLAY_RECEIPT_REQUIRES_EXTERNAL_REVIEW"

def test():
    base=dict(doi="10.24433/CO.4899453.v1",claim="civil-war leakage reanalysis",
              data_digest=None,code_digest=None,executed=False,
              source_reported=True,attestation=None)
    cases=[
      ({}, "SOURCE_REPORTED_NOT_REPLAYED"),
      ({"data_digest":"a"}, "SOURCE_REPORTED_NOT_REPLAYED"),
      ({"code_digest":"b"}, "SOURCE_REPORTED_NOT_REPLAYED"),
      ({"data_digest":"a","code_digest":"b"}, "ARTIFACTS_IDENTIFIED_NOT_REPLAYED"),
      ({"data_digest":"a","code_digest":"b","executed":True}, "REPLAY_UNATTESTED"),
      ({"data_digest":"a","code_digest":"b","executed":True,"attestation":"review"}, "REPLAY_RECEIPT_REQUIRES_EXTERNAL_REVIEW"),
      ({"source_reported":False}, "UNKNOWN_SOURCE"),
    ]
    for changes,expected in cases:
        assert classify(Evidence(**(base|changes)))==expected
    print("MQR489_REPLAY_GATES_PASS=7")
    print("MQR489_REPLAY_PERFORMED=NO")

if __name__=="__main__":
    test()
