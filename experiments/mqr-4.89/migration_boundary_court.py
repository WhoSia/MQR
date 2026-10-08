"""MQR-4.89: bounded migration checks across legacy and byte-bound gates.
These are synthetic fixtures and DO NOT validate an external reviewer's identity.
"""
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name, file):
    spec=spec_from_file_location(name,ROOT/file)
    m=module_from_spec(spec)
    import sys
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

v1=load("mqr489_legacy","replay_receipt_gates.py")
v2=load("mqr489_v2","replay_receipt_gates_v2.py")

def a(b):
    return v2.Artifact(b,sha256(b).hexdigest())

def test():
    legacy_common=dict(doi="10.24433/CO.4899453.v1",claim="synthetic",
                       data_digest="a",code_digest="b",executed=True,
                       source_reported=True,attestation="review")
    strong_common=dict(source_reported=True,code=a(b"code"),dataset=a(b"data"),
                       run_log=a(b"log"),claim_id="c",run_claim_id="c")
    expected=[
        (v1.classify(v1.Evidence(**legacy_common)), "LEGACY_METADATA_UNVERIFIED"),
        (v2.classify(v2.Evidence(**strong_common)), "RUN_RECEIPT_REQUIRES_EXTERNAL_REVIEW"),
        (v2.classify(v2.Evidence(**(strong_common|{"external_review_verified":True}))),"REVIEW_FLAG_SUPPLIED_NOT_EXTERNALLY_VERIFIED"),
        (v2.classify(v2.Evidence(**(strong_common|{"run_claim_id":"different"}))),"INVALID_RUN_RECEIPT"),
        (v2.classify(v2.Evidence(**(strong_common|{"dataset":v2.Artifact(b"changed",a(b"data").claimed_sha256)}))),"ARTIFACT_DIGEST_MISMATCH"),
    ]
    for outcome, expected_verdict in expected: assert outcome==expected_verdict,(outcome,expected_verdict)
    print("MQR489_MIGRATION_BOUNDARY_PASS=5")
    print("MQR489_INDEPENDENT_REPLICATION=NOT_PERFORMED")
if __name__=="__main__":test()
