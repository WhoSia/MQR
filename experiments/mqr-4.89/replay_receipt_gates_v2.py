"""MQR-4.89 byte-bound replay gate. Synthetic gate validation, not empirical replay."""
from dataclasses import dataclass
from hashlib import sha256
@dataclass(frozen=True)
class Artifact:
    data:bytes
    claimed_sha256:str
    def verified(self)->bool:
        return len(self.claimed_sha256)==64 and sha256(self.data).hexdigest()==self.claimed_sha256
@dataclass(frozen=True)
class Evidence:
    source_reported:bool
    code:Artifact|None
    dataset:Artifact|None
    run_log:Artifact|None
    claim_id:str
    run_claim_id:str|None
    external_review_verified:bool=False
def classify(r:Evidence)->str:
    if not r.source_reported: return "UNKNOWN_SOURCE"
    if r.code is None or r.dataset is None: return "SOURCE_REPORTED_NOT_REPLAYED"
    if not r.code.verified() or not r.dataset.verified(): return "ARTIFACT_DIGEST_MISMATCH"
    if r.run_log is None: return "VERIFIED_ARTIFACT_BYTES_NOT_REPLAYED"
    if not r.run_log.verified() or r.run_claim_id!=r.claim_id: return "INVALID_RUN_RECEIPT"
    if not r.external_review_verified: return "RUN_RECEIPT_REQUIRES_EXTERNAL_REVIEW"
    return "REVIEW_FLAG_SUPPLIED_NOT_EXTERNALLY_VERIFIED"
def test():
    a=lambda b:Artifact(b,sha256(b).hexdigest())
    c,d,l=a(b"synthetic-code"),a(b"synthetic-data"),a(b"synthetic-log")
    base=dict(source_reported=True,code=c,dataset=d,run_log=l,claim_id="claim-A",run_claim_id="claim-A")
    cases=[
      (dict(code=None),"SOURCE_REPORTED_NOT_REPLAYED"),
      (dict(dataset=None),"SOURCE_REPORTED_NOT_REPLAYED"),
      (dict(code=Artifact(b"code","a")),"ARTIFACT_DIGEST_MISMATCH"),
      (dict(dataset=Artifact(b"changed",d.claimed_sha256)),"ARTIFACT_DIGEST_MISMATCH"),
      (dict(run_log=None),"VERIFIED_ARTIFACT_BYTES_NOT_REPLAYED"),
      (dict(run_log=Artifact(b"forged",l.claimed_sha256)),"INVALID_RUN_RECEIPT"),
      (dict(run_claim_id="claim-B"),"INVALID_RUN_RECEIPT"),
      (dict(),"RUN_RECEIPT_REQUIRES_EXTERNAL_REVIEW"),
      (dict(external_review_verified=True),"REVIEW_FLAG_SUPPLIED_NOT_EXTERNALLY_VERIFIED"),
      (dict(source_reported=False),"UNKNOWN_SOURCE"),
    ]
    for i,(patch,expected) in enumerate(cases,1):
        actual=classify(Evidence(**(base|patch)))
        assert actual==expected,(i,actual,expected)
    print("MQR489_BYTE_BOUND_TESTS=10/10 PASS")
    print("MQR489_REAL_DATA_REPLAY=NOT_PERFORMED")
    print("MQR489_EXTERNAL_ATTESTATION=NOT_VERIFIED")
if __name__=="__main__":test()
