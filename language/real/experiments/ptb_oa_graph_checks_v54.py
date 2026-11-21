"""Process PTB optical-JAWS figure-export tables without calling them raw ADC logs.

Publisher data DOI 10.7795/720.20250210, CC BY 4.0. Times are exported
graph x-coordinates; equal coordinates are NOT evidence of a common run.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
from statistics import fmean
from zipfile import ZipFile


def load_time_voltage(archive: str, member: str) -> tuple[tuple[float, float], ...]:
    if member not in {"fig3b.txt", "fig3d.txt", "fig3f.txt"}:
        raise ValueError("Only known 2-column time-voltage exports accepted")
    with ZipFile(archive) as z:
        body = z.read("Opto-JAWS/" + member).decode("utf-8-sig")
    lines = body.splitlines()
    if len(lines) < 4 or lines[0].split() != ["t", "V"] or lines[1].split() != ["ms", "mV"]:
        raise ValueError("Unexpected quantity/unit header")
    rows = []
    for line in lines[2:]:
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != 2:
            raise ValueError("Unexpected data row width")
        x, y = map(float, fields)
        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError("Nonfinite data")
        if rows and x <= rows[-1][0]:
            raise ValueError("Time index not increasing")
        rows.append((x, y))
    if not rows:
        raise ValueError("Missing measurements")
    return tuple(rows)


def summarize_closure(positive, negative, whole) -> dict:
    """A+B-C graph-export closure, not an instrument-level superposition."""
    if not positive or len(positive) != len(negative) or len(negative) != len(whole):
        raise ValueError("Same nonempty sample count required")
    if any((a[0] != b[0] or a[0] != c[0]) for a, b, c in zip(positive, negative, whole)):
        raise ValueError("Identical export time grids required (not proof of a common run)")
    residual = [a[1] + b[1] - c[1] for a, b, c in zip(positive, negative, whole)]
    n = len(residual)
    k = n // 2
    if k == 0:
        raise ValueError("At least two readings for holdout")
    offset_training = fmean(residual[:k])
    holdout = residual[k:]
    return {
        "n": n,
        "units": "mV",
        "mean_unadjusted": fmean(residual),
        "rms_unadjusted": math.sqrt(fmean([v*v for v in residual])),
        "fitted_offset_first_half": offset_training,
        "holdout_mean": fmean(holdout),
        "holdout_rmse_after_offset": math.sqrt(fmean([(v-offset_training)**2 for v in holdout])),
        "holdout_max_abs_after_offset": max(abs(v-offset_training) for v in holdout),
        "interpretation": "Graph-export arithmetic only; no dark calibration, same-run identity, or quantified uncertainty asserted",
    }


def analyze(archive: str) -> dict:
    data = [load_time_voltage(archive, name) for name in ("fig3b.txt", "fig3d.txt", "fig3f.txt")]
    return summarize_closure(*data)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(str(args.archive)), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
