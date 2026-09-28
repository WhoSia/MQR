from __future__ import annotations

from .common import (
    FAMILIES, Trace, apply_reopen_episode, mk_steps, readiness_offset,
    replace_obs, seed_for,
)

DOMAIN = "SEARCH"

def generate(family: str, split: str, replicate: int) -> Trace:
    if family not in FAMILIES:
        raise ValueError(f"unknown family {family}")
    seed = seed_for(DOMAIN, family, split, replicate)
    horizon = 15 + ((seed >> 5) % 2)
    cost = 2.0
    jitter = (seed >> 11) % 3

    safe = {
        "INERT_TAIL": 3,
        "LATE_SEPARATOR": 9,
        "EARLY_SEPARATOR": 4,
        "REOPEN_AFTER_STOP": 3,
        "DECISION_CONTRACT_SHIFT": 3,
        "CRITERION_DISAGREEMENT": 7,
        "LIVE_DEBT": 7,
        "UPSTREAM_HOLD": 6,
        "NOISY_IRRELEVANT_EVENTS": 3,
        "MULTIPLE_REOPENINGS": 3,
        "BUDGET_PRESSURE": horizon + 1,
        "PATH_CONFLICT": 8,
    }[family]
    if family not in {
        "REOPEN_AFTER_STOP", "DECISION_CONTRACT_SHIFT",
        "MULTIPLE_REOPENINGS", "BUDGET_PRESSURE",
    }:
        safe += (1 if jitter == 2 else 0)

    offset = readiness_offset(seed, 73 + FAMILIES.index(family))
    ready = horizon + 1 if safe > horizon else max(1, safe + offset)
    steps = mk_steps(horizon, cost, safe, ready, projection_flip=max(1, safe - 2))

    if family == "CRITERION_DISAGREEMENT":
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(steps[t], criterion_invariant=False)

    if family == "UPSTREAM_HOLD":
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(
                steps[t], upstream="HOLD", projection=f"FRONTIER-{t // 2}"
            )

    if family == "PATH_CONFLICT":
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(
                steps[t], upstream="HOLD",
                projection="ROUTE-A" if t % 3 else "ROUTE-B",
            )

    if family == "NOISY_IRRELEVANT_EVENTS":
        for t in range(horizon):
            # search activity can be high while authority-relevant information is unchanged
            steps[t] = replace_obs(steps[t], projection=f"QUERY-{(t * 7 + replicate) % 5}")

    if family == "BUDGET_PRESSURE":
        for t in range(horizon):
            steps[t] = replace_obs(
                steps[t], oqsc_pass=False, live_debt=True,
                projection=f"OPEN-{t % 4}",
            )

    if family == "REOPEN_AFTER_STOP":
        br = 9 + ((seed >> 16) % 2)
        apply_reopen_episode(steps, br, min(horizon, br + 3), decision=False)

    if family == "DECISION_CONTRACT_SHIFT":
        br = 10 + ((seed >> 20) % 2)
        apply_reopen_episode(steps, br, min(horizon, br + 2), decision=True)

    if family == "MULTIPLE_REOPENINGS":
        first = 7
        second = min(horizon - 3, 11 + ((seed >> 23) % 2))
        apply_reopen_episode(steps, first, min(horizon, first + 2), decision=False)
        if second > first + 2:
            apply_reopen_episode(steps, second, min(horizon, second + 3), decision=False)

    trace_id = f"{DOMAIN}-{family}-{split}-{replicate}"
    return Trace(trace_id, DOMAIN, family, split, replicate, seed, tuple(steps))
