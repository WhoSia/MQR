"""Audit archived QWTB outputs and switching schedules from Šíra (2023).

Archived RESULTS are outputs computed by the publisher's processing chain.
This script DOES NOT reproduce TWM-QPSW calibration, certify accuracy,
or compare sequential/experimentally unmatched runs causally.
"""
from __future__ import annotations
from collections import Counter
import math
import re


def _matrix(text: str, label: str) -> str:
    pattern = (r"^[ \t]*#startmatrix::[ \t]*" + re.escape(label)
               + r"[ \t]*\r?\n(.*?)^[ \t]*#endmatrix::[ \t]*(?:"
               + re.escape(label) + r")?[ \t]*(?:\r?\n|$)")
    found = re.search(pattern, text, re.S | re.M)
    if not found:
        raise ValueError("Missing named matrix: " + label)
    return found.group(1).strip()


def _section(text: str, name: str) -> str:
    pattern = (r"^[ \t]*#startsection::[ \t]*" + re.escape(name)
               + r"[ \t]*\r?\n(.*?)^[ \t]*#endsection::[ \t]*"
               + re.escape(name) + r"[ \t]*(?:\r?\n|$)")
    found = re.search(pattern, text, re.S | re.M)
    if not found:
        raise ValueError("Missing named section: " + name)
    return found.group(1)


def _finite_numbers(raw: str, separator: str) -> tuple[float, ...]:
    vals = tuple(float(s.strip()) for s in raw.split(separator) if s.strip())
    if not vals or any(not math.isfinite(v) for v in vals):
        raise ValueError("Missing or nonfinite numeric field")
    return vals


def _bracketed(text: str, name: str) -> tuple[float, ...]:
    raw = _matrix(text, name).strip().strip('"')
    if not (raw.startswith('[') and raw.endswith(']')):
        raise ValueError("Expected bracket vector")
    return _finite_numbers(raw[1:-1], ',')


def audit(qwtb: str, results: str, sample_count: int) -> dict:
    """Classify structure and value summaries, not physical traceability."""
    if sample_count <= 0:
        raise ValueError("Invalid sample count")
    M = _bracketed(qwtb, 'M')
    rawS = _bracketed(qwtb, 'S')
    S = tuple(int(z) for z in rawS)
    Uref = _bracketed(qwtb, 'Uref')
    if not (len(M) == 60 and len(S) == 61 and len(Uref) == 20):
        raise ValueError("Unexpected QWTB array dimensions")
    if any(v not in (-1., 1.) for v in M) or any(M[i] == M[i+1] for i in range(len(M)-1)):
        raise ValueError("Invalid QWTB switch labels")
    if any(z != int(z) for z in rawS):
        raise ValueError("Noninteger sample boundary")
    if any(S[i] >= S[i+1] for i in range(len(S)-1)) or S[0] != 1 or S[-1] != sample_count + 1:
        raise ValueError("Misaligned one-based sample boundaries")
    if 'uncertainty mode:: none' not in results:
        raise ValueError("Unexpected uncertainty status")
    output = _section(results,'U_t')
    series = _finite_numbers(_matrix(output,'value'),';')
    summary = _finite_numbers(_matrix(_section(results,'U'),'value'),';')
    if len(series) != 30 or len(summary) != 1:
        raise ValueError("Unexpected dimensions of archived result")
    calc = sum(series)/len(series)
    if abs(calc-summary[0]) > 1e-8:
        raise ValueError("Stored aggregate inconsistent with source time-series")
    window_lengths = [S[i+1]-S[i] for i in range(60)]
    sd = math.sqrt(sum((x-calc)**2 for x in series)/(len(series)-1))
    return {
      'segments':len(M), 'boundaries':len(S), 'reference_levels':len(Uref),
      'window_lengths':dict(sorted(Counter(window_lengths).items())),
      'total_count':sum(window_lengths), 'paired_window_cycles':len(series),
      'U_processed_archive_V':summary[0],
      'U_t_mean_V':calc, 'U_t_sample_sd_V':sd,
      'U_t_min_V':min(series), 'U_t_max_V':max(series),
      'semantic_warning':'U described as RMS although near 0.8*sqrt(2) V; physical meaning unverified',
      'causal_warning':'Sequential sessions, correlated windows, uncertainty mode none; no certified accuracy or method effect',
    }
