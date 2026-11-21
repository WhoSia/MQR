"""Real-Lang experimental source-byte integrity guard; NOT physical provenance.

Expected digest must come from an independently frozen trusted manifest.
Reading any file from a source path does not establish its scientific identity.
"""
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re

HEX = re.compile(r"^[0-9a-f]{64}$")

@dataclass(frozen=True)
class FrozenBytes:
    source_id: str
    sha256_lower: str
    expected_size: int

    def __post_init__(self):
        if (not isinstance(self.source_id,str) or not self.source_id.strip()
            or not isinstance(self.sha256_lower,str) or
            HEX.fullmatch(self.sha256_lower) is None or
            type(self.expected_size) is not int or self.expected_size < 0):
            raise ValueError("Malformed previously frozen byte witness")

def audit_bytes(path, frozen):
    """Fail closed, no write and no source identity inference."""
    if not isinstance(frozen,FrozenBytes):
        raise ValueError("Trusted frozen digest must be explicit")
    p=Path(path)
    if not p.is_file():
        return "HOLD_SOURCE_BYTES_ABSENT"
    digest=sha256()
    count=0
    try:
        with p.open("rb") as f:
            while chunk := f.read(1024*1024):
                count+=len(chunk)
                if count>frozen.expected_size:
                    return "FAIL_SOURCE_SIZE_MISMATCH"
                digest.update(chunk)
    except OSError:
        return "HOLD_SOURCE_BYTES_UNREADABLE"
    if count!=frozen.expected_size:
        return "FAIL_SOURCE_SIZE_MISMATCH"
    if digest.hexdigest()!=frozen.sha256_lower:
        return "FAIL_SOURCE_HASH_MISMATCH"
    return "BYTES_MATCH_FROZEN_DIGEST_ONLY"
