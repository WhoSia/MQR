"""Uncorrected audit of original QPSW MAT streams (Zenodo 10046413).

The reported quantities are raw integer counts times the recording gain.
No traceable voltage, multiplexer processing or uncertainty is inferred.
"""
from __future__ import annotations
import argparse
import json
import math
import re
from pathlib import Path


def matrix_scalar(info: str, key: str) -> float:
    pattern = r"#startmatrix::\s*" + re.escape(key) + r"\s*\n\s*([-+0-9.eE]+)\s*\n\s*#endmatrix::"
    m = re.search(pattern, info)
    if not m:
        raise ValueError("Required metadata matrix missing: " + key)
    value = float(m.group(1))
    if not math.isfinite(value):
        raise ValueError("Nonfinite metadata " + key)
    return value


def audit_mat(mat_path: Path, session_path: Path) -> dict:
    """Descriptions only. Corrections/calibration intentionally excluded."""
    import numpy as np
    from scipy.io import loadmat
    info = session_path.read_text(encoding="utf-8-sig")
    n = int(matrix_scalar(info, "record samples counts"))
    gain = matrix_scalar(info, "record sample data gains [V]")
    offset = matrix_scalar(info, "record sample data offsets [V]")
    match = re.search(r"sampling rate \[Sa/s\]::\s*([-+0-9.eE]+)", info)
    if not match:
        raise ValueError("Missing sampling rate")
    fs = float(match.group(1))
    if fs <= 0 or n <= 0 or gain == 0 or not math.isfinite(fs):
        raise ValueError("Invalid sample specification")
    data = loadmat(mat_path)
    if "y" not in data:
        raise ValueError("No expected y stream")
    y = np.asarray(data["y"])
    if y.size != n or not np.issubdtype(y.dtype, np.integer):
        raise ValueError("Sample count or integer raw format mismatch")
    v = y.ravel().astype("float64") * gain + offset
    mean = float(np.mean(v))
    rms = float(np.sqrt(np.mean(v * v)))
    return {"raw_count": n, "rate_Sa_s": fs, "duration_s": n / fs,
            "mean_uncorrected_V": mean, "rms_uncorrected_V": rms,
            "ac_rms_uncorrected_V": float(np.sqrt(np.mean((v - mean)**2))),
            "status": "UNCALIBRATED: no QWTB corrections, reference deconvolution or method comparison"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("mat", type=Path)
    p.add_argument("session_info", type=Path)
    a = p.parse_args()
    print(json.dumps(audit_mat(a.mat, a.session_info), indent=2))


if __name__ == "__main__":
    main()
