from __future__ import annotations

import json
import math
import random
import statistics
from collections import defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
BOOT_SEED = 4632026
BOOT_N = 2000
NONTRIVIAL = 0.08
MATCH_CONV = 0.05
MATCH_TYPED = 0.15

ORIENTATION = {
    "conventional_success": 1,
    "conventional_error": -1,
    "cost": -1,
    "ERR": 1,
    "FSR": 1,
    "RCR": 1,
    "RL": -1,
    "EAI": 1,
    "BOD": -1,
    "CSD": -1,
    "NED": -1,
    "BSI": -1,
}

COMPARISONS = {
    "OPR": [
        ("SCOUT-PARK", "mqr_full", "mqr_minus_opr", "BOD"),
        ("SAMPLE-RESERVE", "mqr_full", "mqr_minus_opr", "BOD"),
    ],
    "ARR": [
        ("SCOUT-PARK", "mqr_full", "mqr_minus_arr", "RCR"),
        ("THEORY-ECOLOGY", "mqr_full", "mqr_minus_arr", "RCR"),
        ("SAMPLE-RESERVE", "mqr_full", "mqr_minus_arr", "RCR"),
    ],
    "EAI": [
        ("THEORY-ECOLOGY", "mqr_full", "mqr_minus_eai", "EAI"),
    ],
    "NEDL": [
        ("SCOUT-PARK", "mqr_full", "mqr_minus_nedl", "NED"),
        ("THEORY-ECOLOGY", "mqr_full", "mqr_minus_nedl", "NED"),
        ("SAMPLE-RESERVE", "mqr_full", "mqr_minus_nedl", "NED"),
    ],
    "EXTERIOR": [
        ("SCOUT-PARK", "mqr_full", "mqr_minus_exterior", "ERR"),
        ("THEORY-ECOLOGY", "mqr_full", "mqr_minus_exterior", "ERR"),
    ],
}

ALL_METRICS = list(ORIENTATION)


def load_rows():
    rows = []
    with (RESULTS / "raw_runs.jsonl").open(encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def bootstrap_ci(diffs, seed_offset=0):
    if not diffs:
        return [0.0, 0.0]
    rng = random.Random(BOOT_SEED + seed_offset)
    n = len(diffs)
    means = []
    for _ in range(BOOT_N):
        means.append(sum(diffs[rng.randrange(n)] for _ in range(n)) / n)
    means.sort()
    lo = means[int(0.025 * (BOOT_N - 1))]
    hi = means[int(0.975 * (BOOT_N - 1))]
    return [lo, hi]


def paired_stats(rows, world, a, b, metric, seed_offset):
    by = {(r["world"], r["policy"], r["seed"]): r for r in rows}
    seeds = sorted({r["seed"] for r in rows if r["world"] == world})
    orient = ORIENTATION[metric]
    diffs = []
    for s in seeds:
        ra = by[(world, a, s)]
        rb = by[(world, b, s)]
        diffs.append(orient * (ra[metric] - rb[metric]))
    mean = statistics.mean(diffs)
    median = statistics.median(diffs)
    sd = statistics.stdev(diffs) if len(diffs) > 1 else 0.0
    std = mean / sd if sd > 0 else (math.inf if mean > 0 else (-math.inf if mean < 0 else 0.0))
    ci = bootstrap_ci(diffs, seed_offset)
    sign = sum(d > 0 for d in diffs) / len(diffs)
    nontrivial = ci[0] > 0 and mean >= NONTRIVIAL
    reverse_nontrivial = ci[1] < 0 and mean <= -NONTRIVIAL
    return {
        "world": world,
        "policy_a": a,
        "policy_b": b,
        "metric": metric,
        "n": len(diffs),
        "mean_benefit_delta": mean,
        "median_benefit_delta": median,
        "standardized_paired_effect": std,
        "bootstrap95": ci,
        "positive_sign_fraction": sign,
        "nontrivial_predicted_direction": nontrivial,
        "nontrivial_reverse_direction": reverse_nontrivial,
    }


def policy_means(rows):
    groups = defaultdict(list)
    for r in rows:
        groups[(r["world"], r["policy"])].append(r)
    out = {}
    for key, rs in groups.items():
        out[key] = {m: statistics.mean(r[m] for r in rs) for m in ALL_METRICS}
    return out


def nonreducibility_witnesses(means, metric, worlds):
    out = []
    for world in worlds:
        policies = sorted(p for (w, p) in means if w == world)
        for a, b in combinations(policies, 2):
            ma, mb = means[(world, a)], means[(world, b)]
            cd = abs(ma["conventional_success"] - mb["conventional_success"])
            td = abs(ma[metric] - mb[metric])
            if cd <= MATCH_CONV and td >= MATCH_TYPED:
                out.append({
                    "world": world,
                    "policy_a": a,
                    "policy_b": b,
                    "conventional_success_gap": cd,
                    "typed_metric": metric,
                    "typed_gap": td,
                })
    return out


def classify_coordinate(coord, effects, witnesses):
    surviving_worlds = sorted({e["world"] for e in effects if e["nontrivial_predicted_direction"]})
    reverse_worlds = sorted({e["world"] for e in effects if e["nontrivial_reverse_direction"]})
    if reverse_worlds:
        return {
            "classification": "RETIRE_OR_REDESIGN",
            "surviving_worlds": surviving_worlds,
            "reverse_worlds": reverse_worlds,
            "witness_count": len(witnesses),
        }
    if len(surviving_worlds) >= 2 and witnesses:
        c = "SURVIVES_CROSS_DOMAIN"
    elif len(surviving_worlds) == 1:
        c = "SURVIVES_LOCAL"
    else:
        c = "COLLAPSES_TO_BASELINE"
    return {
        "classification": c,
        "surviving_worlds": surviving_worlds,
        "reverse_worlds": reverse_worlds,
        "witness_count": len(witnesses),
    }


def main():
    rows = load_rows()
    means = policy_means(rows)
    report = {
        "stage": "MQR-4.63",
        "analysis_plan_commit": "818798005b9e02ec73c03ef98cfa1b0e98c8efed",
        "bootstrap_seed": BOOT_SEED,
        "bootstrap_resamples": BOOT_N,
        "nontrivial_threshold": NONTRIVIAL,
        "matched_conventional_threshold": MATCH_CONV,
        "matched_typed_threshold": MATCH_TYPED,
        "scalar_mqr_score": "FORBIDDEN",
        "effects": {},
        "classifications": {},
        "policy_means": {
            f"{w}|{p}": v for (w, p), v in sorted(means.items())
        },
    }

    offset = 0
    for coord, specs in COMPARISONS.items():
        effects = []
        primary_metric = specs[0][3]
        worlds = []
        for world, a, b, metric in specs:
            effects.append(paired_stats(rows, world, a, b, metric, offset))
            offset += 10007
            worlds.append(world)
        witnesses = nonreducibility_witnesses(means, primary_metric, worlds)
        report["effects"][coord] = {
            "primary_metric": primary_metric,
            "paired": effects,
            "nonreducibility_witnesses": witnesses,
        }
        report["classifications"][coord] = classify_coordinate(coord, effects, witnesses)

    # IDR/control report: mqr_full vs strongest conventional baseline in negative controls.
    controls = []
    controls.append(paired_stats(rows, "CAUSAL-SEP", "mqr_full", "causal_identifiability", "conventional_success", offset)); offset += 10007
    controls.append(paired_stats(rows, "SENSING-GRID", "mqr_full", "entropy_greedy", "conventional_success", offset)); offset += 10007
    report["negative_control_comparisons"] = controls

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "analysis.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    matrix = {}
    for coord, rec in report["classifications"].items():
        matrix[coord] = rec["classification"]
    (RESULTS / "coordinate_matrix.json").write_text(json.dumps(matrix, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("MQR463_ANALYSIS_COMPLETE=PASS")
    print("MQR463_SCALAR_MQR_SCORE=FORBIDDEN")
    for coord in sorted(matrix):
        print(f"MQR463_{coord}_CLASS={matrix[coord]}")
    print("MQR463_RESULT_DEPENDENT_THRESHOLD_MUTATION=FORBIDDEN")


if __name__ == "__main__":
    main()
