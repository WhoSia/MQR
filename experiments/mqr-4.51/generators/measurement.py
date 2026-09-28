from __future__ import annotations

from .common import (
    FAMILIES, Trace, apply_reopen_episode, mk_steps, readiness_offset,
    replace_obs, seed_for,
)

DOMAIN = "MEASUREMENT"

def generate(family: str, split: str, replicate: int) -> Trace:
    if family not in FAMILIES:
        raise ValueError(f"unknown family {family}")
    seed = seed_for(DOMAIN, family, split, replicate)
    horizon = 13 + ((seed >> 3) % 2)
    cost = 1.5
    jitter = (seed >> 9) % 2

    safe = {
        "INERT_TAIL": 3,
        "LATE_SEPARATOR": 8,
        "EARLY_SEPARATOR": 4,
        "REOPEN_AFTER_STOP": 3,
        "DECISION_CONTRACT_SHIFT": 3,
        "CRITERION_DISAGREEMENT": 6,
        "LIVE_DEBT": 6,
        "UPSTREAM_HOLD": 5,
        "NOISY_IRRELEVANT_EVENTS": 3,
        "MULTIPLE_REOPENINGS": 3,
        "BUDGET_PRESSURE": horizon + 1,
        "PATH_CONFLICT": 7,
    }[family]
    if family not in {
        "REOPEN_AFTER_STOP", "DECISION_CONTRACT_SHIFT",
        "MULTIPLE_REOPENINGS", "BUDGET_PRESSURE",
    }:
        safe += jitter

    offset = readiness_offset(seed, 37 + FAMILIES.index(family))
    ready = horizon + 1 if safe > horizon else max(1, safe + offset)
    steps = mk_steps(horizon, cost, safe, ready, projection_flip=max(1, safe - 1))

    if family == "CRITERION_DISAGREEMENT":
        # competing calibration interpretations remain live until the receipt resolves
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(steps[t], criterion_invariant=False)

    if family == "UPSTREAM_HOLD":
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(steps[t], upstream="HOLD")

    if family == "PATH_CONFLICT":
        for t in range(min(ready, horizon)):
            steps[t] = replace_obs(
                steps[t], upstream="HOLD",
                projection="DIRECT" if t % 2 == 0 else "COMPOSED",
            )

    if family == "NOISY_IRRELEVANT_EVENTS":
        for t in range(horizon):
            # readout noise is intentionally projection-visible but gold-inert
            steps[t] = replace_obs(steps[t], projection=f"CAL{(t * 5 + replicate) % 4}")

    if family == "BUDGET_PRESSURE":
        for t in range(horizon):
            steps[t] = replace_obs(
                steps[t], oqsc_pass=False, live_debt=True,
                criterion_invariant=(t % 4 != 0),
            )

    if family == "REOPEN_AFTER_STOP":
        br = 8 + ((seed >> 15) % 2)
        apply_reopen_episode(steps, br, min(horizon, br + 2), decision=False)

    if family == "DECISION_CONTRACT_SHIFT":
        br = 8 + ((seed >> 18) % 2)
        apply_reopen_episode(steps, br, min(horizon, br + 2), decision=True)

    if family == "MULTIPLE_REOPENINGS":
        first = 6
        second = min(horizon - 2, 10 + ((seed >> 21) % 2))
        apply_reopen_episode(steps, first, min(horizon, first + 2), decision=False)
        if second > first + 2:
            apply_reopen_episode(steps, second, min(horizon, second + 2), decision=False)

    trace_id = f"{DOMAIN}-{family}-{split}-{replicate}"
    return Trace(trace_id, DOMAIN, family, split, replicate, seed, tuple(steps))
