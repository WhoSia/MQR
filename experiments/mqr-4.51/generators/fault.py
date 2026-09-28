from __future__ import annotations

from .common import (
    FAMILIES, Trace, apply_reopen_episode, mk_steps, readiness_offset,
    replace_obs, seed_for,
)

DOMAIN = "FAULT"

def generate(family: str, split: str, replicate: int) -> Trace:
    if family not in FAMILIES:
        raise ValueError(f"unknown family {family}")
    seed = seed_for(DOMAIN, family, split, replicate)
    horizon = 11 + (seed % 2)
    cost = 1.0
    jitter = (seed >> 7) % 2

    base = {
        "INERT_TAIL": 2,
        "LATE_SEPARATOR": 6,
        "EARLY_SEPARATOR": 3,
        "REOPEN_AFTER_STOP": 2,
        "DECISION_CONTRACT_SHIFT": 2,
        "CRITERION_DISAGREEMENT": 5,
        "LIVE_DEBT": 5,
        "UPSTREAM_HOLD": 5,
        "NOISY_IRRELEVANT_EVENTS": 2,
        "MULTIPLE_REOPENINGS": 2,
        "BUDGET_PRESSURE": horizon + 1,
        "PATH_CONFLICT": 6,
    }[family]
    if family not in {
        "REOPEN_AFTER_STOP", "DECISION_CONTRACT_SHIFT",
        "MULTIPLE_REOPENINGS", "BUDGET_PRESSURE",
    }:
        base += jitter

    offset = readiness_offset(seed, 11 + FAMILIES.index(family))
    ready = horizon + 1 if base > horizon else max(1, base + offset)
    steps = mk_steps(horizon, cost, base, ready, projection_flip=base)

    if family == "CRITERION_DISAGREEMENT":
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(steps[t], criterion_invariant=False)

    if family in {"UPSTREAM_HOLD", "PATH_CONFLICT"}:
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(steps[t], upstream="HOLD")

    if family == "NOISY_IRRELEVANT_EVENTS":
        for t in range(horizon):
            # diagnostic chatter changes surface projection without changing gold safety
            steps[t] = replace_obs(steps[t], projection=f"N{t % 3}")

    if family == "BUDGET_PRESSURE":
        for t in range(horizon):
            steps[t] = replace_obs(steps[t], oqsc_pass=False, live_debt=True)

    if family == "REOPEN_AFTER_STOP":
        br = 6 + ((seed >> 13) % 2)
        apply_reopen_episode(steps, br, min(horizon, br + 2), decision=False)

    if family == "DECISION_CONTRACT_SHIFT":
        br = 6 + ((seed >> 17) % 2)
        apply_reopen_episode(steps, br, min(horizon, br + 2), decision=True)

    if family == "MULTIPLE_REOPENINGS":
        first = 5
        second = min(horizon - 2, 8 + ((seed >> 19) % 2))
        apply_reopen_episode(steps, first, min(horizon, first + 2), decision=False)
        if second > first + 2:
            apply_reopen_episode(steps, second, min(horizon, second + 2), decision=False)

    trace_id = f"{DOMAIN}-{family}-{split}-{replicate}"
    return Trace(trace_id, DOMAIN, family, split, replicate, seed, tuple(steps))
