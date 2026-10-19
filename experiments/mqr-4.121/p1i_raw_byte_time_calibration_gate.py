"""MQR P1I: fail-closed local-byte, UTC/time, calibration validity gate.

Structural truth != provenance truth: checks only bytes and declared timestamps on
a caller-supplied manifest; cannot authenticate device clocks or laboratories.
"""
import argparse
import hashlib
import json
import tempfile
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, unquote

from p1h_instrument_raw_intake import fixture, validate

def stamp(s):
    if not isinstance(s,str) or not s: raise ValueError("missing ISO time")
    try: d=datetime.fromisoformat(s.replace("Z","+00:00"))
    except (ValueError,TypeError): raise ValueError("invalid ISO time")
    if d.tzinfo is None or d.utcoffset() is None: raise ValueError("naive time rejected")
    return d.astimezone(timezone.utc)

def physical_file(uri, root):
    if not isinstance(uri,str) or not uri.startswith("file://"): raise ValueError("only local file:// originals supported")
    u=urlparse(uri)
    if u.netloc not in ("","localhost") or u.params or u.query or u.fragment:
        raise ValueError("nonlocal file URI rejected")
    p=Path(unquote(u.path))
    resolved=p.resolve(strict=True)
    boundary=root.resolve(strict=True)
    if not resolved.is_relative_to(boundary): raise ValueError("file outside admission root")
    if p.is_symlink() or not resolved.is_file(): raise ValueError("symlink/nonregular file")
    return resolved

def file_hash(path):
    sha=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1<<16),b""): sha.update(block)
    return sha.hexdigest()

def validate_bytes_and_times(data, root, tolerance_seconds=120):
    result=validate(data)
    if data["provenance"]["kind"]!="physical": raise ValueError("physical record required")
    if not (isinstance(tolerance_seconds,(int,float)) and 0<=tolerance_seconds<=3600):
        raise ValueError("invalid tolerance")
    cal={c["id"]:c for c in data["calibrations"]}
    hashes={}
    for c in cal.values():
        a=stamp(c["valid_from_iso"]);b=stamp(c["valid_until_iso"])
        if b<=a: raise ValueError("invalid calibration validity interval")
        stamp(c["measured_at_iso"])
        if stamp(c["measured_at_iso"])>a: raise ValueError("calibration acquired after validity began")
    for rec in data["records"]:
        c=cal[rec["calibration_id"]]
        lo=stamp(c["valid_from_iso"]);hi=stamp(c["valid_until_iso"])
        times=[stamp(rec[k]) for k in ("sample_at_iso","reference_at_iso","sample_dark_at_iso","reference_dark_at_iso")]
        if any(not (lo<=t<=hi) for t in times):raise ValueError("calibration expired or not yet valid")
        if (max(times)-min(times)).total_seconds()>tolerance_seconds:
            raise ValueError("unmatched sample/reference/dark acquisition time")
        if data["instrument"]["response_architecture"]=="scanning":
            ch=[stamp(v) for key in ("sample_channel_times_iso","reference_channel_times_iso") for v in rec[key]]
            if any(not (lo<=t<=hi) for t in ch): raise ValueError("scan outside calibration validity")
            if any((max(times+[t])-min(times+[t])).total_seconds()>tolerance_seconds for t in ch):
                raise ValueError("scan channel not time-aligned")
        path=physical_file(rec["raw_file_uri"],root)
        if path.stat().st_size<1: raise ValueError("empty raw file")
        actual=file_hash(path);declared=rec["raw_file_sha256"].lower()
        if actual!=declared:raise ValueError("original SHA256 mismatch")
        hashes[rec["id"]]=actual
    return {**result,"byte_integrity":"LOCAL_SHA256_VERIFIED","time_consistency":"DECLARED_TIMES_CONSISTENT","calibration_validity":"DECLARED_PERIOD_CONSISTENT","device_provenance":"UNAUTHENTICATED","files":len(hashes)}

def tests():
    with tempfile.TemporaryDirectory(prefix="mqr-p1i-") as tmp:
        root=Path(tmp);raw=root/"original.bin";raw.write_bytes(b"MQR SYNTHETIC DEVICE BLOB\n")
        d=fixture()
        d["provenance"]["kind"]="physical"
        d["calibrations"][0].update({
            "measured_at_iso":"2026-01-01T00:00:00+00:00",
            "valid_from_iso":"2026-01-02T00:00:00+00:00",
            "valid_until_iso":"2026-07-01T00:00:00+00:00"})
        d["records"][0].update({
            "raw_file_sha256":file_hash(raw),"raw_file_uri":raw.as_uri(),
            "sample_at_iso":"2026-03-01T00:00:30Z",
            "reference_at_iso":"2026-03-01T00:00:40+00:00",
            "sample_dark_at_iso":"2026-03-01T00:00:10Z",
            "reference_dark_at_iso":"2026-03-01T00:00:15Z"})
        assert validate_bytes_and_times(d,root)["files"]==1
        def reject(mutator):
            v=deepcopy(d);mutator(v)
            try:validate_bytes_and_times(v,root)
            except (ValueError,FileNotFoundError):return
            raise AssertionError("invalid physical record admitted")
        reject(lambda x:x["records"][0].update(raw_file_sha256="a"*64))
        reject(lambda x:x["records"][0].update(sample_at_iso="2026-08-01T00:00:30Z"))
        reject(lambda x:x["records"][0].update(sample_at_iso="2026-03-01T01:00:30Z"))
        reject(lambda x:x["records"][0].update(sample_at_iso="2026-03-01T00:00:30"))
        reject(lambda x:x["calibrations"][0].update(valid_until_iso="2026-01-01T00:00:00Z"))
        reject(lambda x:x["records"][0].update(raw_file_uri=(root.parent/"outside.bin").as_uri()))
        reject(lambda x:x["calibrations"][0].update(measured_at_iso="2026-01-03T00:00:00Z"))
        raw.write_bytes(b"tampered original\n")
        try:validate_bytes_and_times(d,root)
        except ValueError as e: assert "SHA256 mismatch" in str(e)
        else: raise AssertionError("tampering undetected")
    print("MQR_P1I_RAW_BYTE_AND_TIME_GATES=PASS_SYNTHETIC")
    print("MQR_P1I_DEVICE_AUTHENTICITY=HOLD")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path)
    p.add_argument("--root",type=Path)
    args=p.parse_args()
    tests()
    if args.manifest:
        if not args.root:raise SystemExit("--root required")
        print(json.dumps(validate_bytes_and_times(json.loads(args.manifest.read_text()),args.root),indent=2))
