from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"

WORLD_BUDGET = {
    "CAUSAL-SEP": 6,
    "SENSING-GRID": 12,
    "SCOUT-PARK": 20,
    "THEORY-ECOLOGY": 30,
    "SAMPLE-RESERVE": 10,
}

EXPECTED_POLICIES = {
    "CAUSAL-SEP": 4,
    "SENSING-GRID": 4,
    "SCOUT-PARK": 10,
    "THEORY-ECOLOGY": 11,
    "SAMPLE-RESERVE": 9,
}

EXPECTED_SEEDS = {
    "CAUSAL-SEP": 64,
    "SENSING-GRID": 64,
    "SCOUT-PARK": 96,
    "THEORY-ECOLOGY": 96,
    "SAMPLE-RESERVE": 96,
}


def c01(x):
    return max(0.0, min(1.0, float(x)))


def recompute(p, budget):
    pe = p["possible_exterior"]
    isep = p["initial_separators"]
    ir = p["initial_reopening_routes"]
    ma = p["max_ancestry_classes"]
    md = p["max_destroyable"]
    db = p["debt_bound"]
    bb = p["blind_bound"]
    return {
        "ERR": c01(p["recovered_exterior"] / pe) if pe > 0 else 0.0,
        "FSR": c01(p["retained_separators"] / isep) if isep > 0 else 1.0,
        "RCR": c01(p["reopening_routes"] / ir) if ir > 0 else 1.0,
        "RL": c01(p["reopening_latency"] / max(1, budget)),
        "EAI": c01(p["ancestry_classes"] / ma) if ma > 0 and p["nominal_evidence"] > 0 else 1.0,
        "BOD": c01(p["destroyed_options"] / md) if md > 0 else 0.0,
        "CSD": c01(p["contamination_events"] / max(1, budget)),
        "NED": c01(p["exploration_debt_raw"] / db) if db > 0 else 0.0,
        "BSI": c01(p["blind_mass"] / bb) if bb > 0 else 0.0,
    }


def main():
    rows = [json.loads(x) for x in (RESULTS / "raw_runs.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    seen = set()
    counts = {}
    for r in rows:
        key = (r["world"], r["seed"], r["policy"])
        assert key not in seen, ("duplicate", key)
        seen.add(key)
        counts[r["world"]] = counts.get(r["world"], 0) + 1
        rr = recompute(r["primitives"], WORLD_BUDGET[r["world"]])
        for k, v in rr.items():
            assert abs(v - r[k]) < 1e-12, (key, k, v, r[k])

    for w in EXPECTED_SEEDS:
        assert counts[w] == EXPECTED_SEEDS[w] * EXPECTED_POLICIES[w], (w, counts[w])

    # Negative-control audit is re-encoded independently.
    for r in rows:
        if r["world"] in ("CAUSAL-SEP", "SENSING-GRID"):
            assert r["BOD"] == 0
            assert r["CSD"] == 0
            assert r["NED"] == 0
        if r["world"] == "THEORY-ECOLOGY":
            assert r["BOD"] == 0
        if r["world"] == "SCOUT-PARK":
            assert r["CSD"] == 0

    manifest = json.loads((RESULTS / "run_manifest.json").read_text(encoding="utf-8"))
    assert manifest["scalar_mqr_score"] == "FORBIDDEN"
    assert manifest["run_count"] == len(rows)

    print(f"MQR463_INDEPENDENT_ROWS={len(rows)}")
    print("MQR463_INDEPENDENT_METRIC_RECOMPUTE=PASS")
    print("MQR463_INDEPENDENT_NEGATIVE_CONTROLS=PASS")
    print("MQR463_INDEPENDENT_PAIRED_COMPLETENESS=PASS")
    print("MQR463_INDEPENDENT_SCALAR_SCORE_GUARD=PASS")


if __name__ == "__main__":
    main()
