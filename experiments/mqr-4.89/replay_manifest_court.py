"""MQR-4.89: Bind a replay manifest to local artifact bytes.
Manifest consistency is NOT a trustworthy external execution attestation.
"""
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

@dataclass(frozen=True)
class Manifest:
    claim_id: str
    source_doi: str
    code_sha256: str
    data_sha256: str
    log_sha256: str
    run_claim_id: str

def sha(path:Path)->str:
    h=sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def verify(m:Manifest,code:Path,data:Path,log:Path)->str:
    if not m.claim_id or not m.source_doi or not m.run_claim_id:
        return "INVALID_MANIFEST"
    if m.run_claim_id != m.claim_id:
        return "RUN_CLAIM_MISMATCH"
    if not all(x.is_file() for x in (code,data,log)):
        return "MISSING_ARTIFACT"
    if sha(code)!=m.code_sha256 or sha(data)!=m.data_sha256:
        return "CODE_DATA_MISMATCH"
    if sha(log)!=m.log_sha256:
        return "RUN_LOG_MISMATCH"
    return "MANIFEST_BYTES_MATCH_UNVERIFIED_EXECUTION"

def tests():
    from tempfile import TemporaryDirectory
    from dataclasses import replace
    with TemporaryDirectory() as d:
        paths=[Path(d)/name for name in ("code","data","log")]
        for p,b in zip(paths,(b"synthetic-code",b"synthetic-data",b"synthetic-log")):p.write_bytes(b)
        m=Manifest("claim-A","10.24433/CO.4899453.v1",*(sha(x) for x in paths),"claim-A")
        cases=[
          (m,paths,"MANIFEST_BYTES_MATCH_UNVERIFIED_EXECUTION"),
          (replace(m,run_claim_id="claim-B"),paths,"RUN_CLAIM_MISMATCH"),
          (replace(m,code_sha256="0"*64),paths,"CODE_DATA_MISMATCH"),
          (replace(m,log_sha256="0"*64),paths,"RUN_LOG_MISMATCH"),
          (replace(m,source_doi=""),paths,"INVALID_MANIFEST"),
          (m,[paths[0],Path(d)/"missing",paths[2]],"MISSING_ARTIFACT"),
        ]
        for manifest,p,expected in cases:
            actual=verify(manifest,*p)
            assert actual==expected,(actual,expected)
    print("MQR489_MANIFEST_CONSISTENCY_PASS=6")
    print("MQR489_EXECUTION_AUTHENTICITY=UNVERIFIED")
if __name__=="__main__":tests()
