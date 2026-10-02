from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Callable, Iterable

PRESEAL = "c61c9516a4e38ee1241a30ca3d09186bc58b53e8"

FAMILIES = (
    "INERT_TAIL",
    "LATE_SEPARATOR",
    "EARLY_SEPARATOR",
    "REOPEN_AFTER_STOP",
    "DECISION_CONTRACT_SHIFT",
    "CRITERION_DISAGREEMENT",
    "LIVE_DEBT",
    "UPSTREAM_HOLD",
    "NOISY_IRRELEVANT_EVENTS",
    "MULTIPLE_REOPENINGS",
    "BUDGET_PRESSURE",
    "PATH_CONFLICT",
)

@dataclass(frozen=True)
class Observable:
    t: int
    upstream: str
    oqsc_pass: bool
    live_debt: bool
    criterion_invariant: bool
    active_break: bool
    decision_change: bool
    projection: str
    step_cost: float

@dataclass(frozen=True)
class HiddenGold:
    live_unsafe: bool
    action_wrong_if_stop: bool

@dataclass(frozen=True)
class Step:
    obs: Observable
    gold: HiddenGold

@dataclass(frozen=True)
class Trace:
    trace_id: str
    domain: str
    family: str
    split: str
    replicate: int
    seed: int
    steps: tuple[Step, ...]

@dataclass(frozen=True)
class MetricVector:
    pse_live: int = 0
    pd_live: int = 0
    ae_live: int = 0
    oiw: float = 0.0
    rl_max: int = 0
    missed_reopen: int = 0
    ber: int = 0

    def add(self, other: "MetricVector") -> "MetricVector":
        return MetricVector(
            self.pse_live + other.pse_live,
            self.pd_live + other.pd_live,
            self.ae_live + other.ae_live,
            round(self.oiw + other.oiw, 6),
            max(self.rl_max, other.rl_max),
            self.missed_reopen + other.missed_reopen,
            self.ber + other.ber,
        )

    def tuple(self) -> tuple[float, ...]:
        return (
            self.pse_live,
            self.pd_live,
            self.ae_live,
            self.oiw,
            self.rl_max,
            self.missed_reopen,
            self.ber,
        )

def seed_for(domain: str, family: str, split: str, replicate: int) -> int:
    material = f"MQR-4.51|{PRESEAL}|{domain}|{family}|{split}|{replicate}".encode()
    return int.from_bytes(sha256(material).digest()[:8], "big")

def readiness_offset(seed: int, salt: int) -> int:
    # Deliberately independent of hidden gold construction.
    # About 2/7 early, 1/7 late, otherwise aligned.
    x = (seed ^ (salt * 0x9E3779B97F4A7C15)) % 7
    if x in (0, 1):
        return -1
    if x == 2:
        return 1
    return 0

def mk_steps(
    horizon: int,
    cost: float,
    gold_safe: int,
    observed_ready: int,
    projection_flip: int | None = None,
) -> list[Step]:
    steps: list[Step] = []
    for t in range(horizon):
        gold_unsafe = t < gold_safe
        obs_ready = t >= observed_ready
        projection = "P1" if projection_flip is None or t < projection_flip else "P2"
        steps.append(
            Step(
                Observable(
                    t=t,
                    upstream="PASS",
                    oqsc_pass=obs_ready,
                    live_debt=not obs_ready,
                    criterion_invariant=True,
                    active_break=False,
                    decision_change=False,
                    projection=projection,
                    step_cost=cost,
                ),
                HiddenGold(
                    live_unsafe=gold_unsafe,
                    action_wrong_if_stop=gold_unsafe,
                ),
            )
        )
    return steps

def replace_obs(step: Step, **kw) -> Step:
    d = step.obs.__dict__.copy()
    d.update(kw)
    return Step(Observable(**d), step.gold)

def replace_gold(step: Step, **kw) -> Step:
    d = step.gold.__dict__.copy()
    d.update(kw)
    return Step(step.obs, HiddenGold(**d))

def apply_reopen_episode(
    steps: list[Step],
    break_t: int,
    recovery_t: int,
    decision: bool = False,
) -> None:
    if break_t >= len(steps):
        return
    steps[break_t] = replace_obs(
        steps[break_t],
        active_break=not decision,
        decision_change=decision,
        oqsc_pass=False,
        live_debt=True,
    )
    for t in range(break_t, min(recovery_t, len(steps))):
        steps[t] = replace_obs(steps[t], oqsc_pass=False, live_debt=True)
        steps[t] = replace_gold(steps[t], live_unsafe=True, action_wrong_if_stop=True)
    for t in range(recovery_t, len(steps)):
        steps[t] = replace_obs(steps[t], oqsc_pass=True, live_debt=False)
        steps[t] = replace_gold(steps[t], live_unsafe=False, action_wrong_if_stop=False)

def is_eligible(obs: Observable) -> bool:
    return (
        obs.upstream == "PASS"
        and obs.oqsc_pass
        and not obs.live_debt
        and obs.criterion_invariant
        and not obs.active_break
        and not obs.decision_change
    )

Policy = Callable[[Observable, tuple[tuple[Observable, str], ...]], str]

def oqsc_policy(obs: Observable, history: tuple[tuple[Observable, str], ...]) -> str:
    if obs.active_break or obs.decision_change or obs.upstream == "REOPEN":
        return "REOPEN"
    return "STOP" if is_eligible(obs) else "CONTINUE"

def stop_now_policy(obs: Observable, history: tuple[tuple[Observable, str], ...]) -> str:
    if obs.active_break or obs.decision_change or obs.upstream == "REOPEN":
        return "REOPEN"
    return "STOP"

def continue_all_policy(obs: Observable, history: tuple[tuple[Observable, str], ...]) -> str:
    if obs.active_break or obs.decision_change or obs.upstream == "REOPEN":
        return "REOPEN"
    return "CONTINUE"

def fixed_policy(k: int) -> Policy:
    def policy(obs: Observable, history: tuple[tuple[Observable, str], ...]) -> str:
        if obs.active_break or obs.decision_change or obs.upstream == "REOPEN":
            return "REOPEN"
        return "STOP" if obs.t >= k else "CONTINUE"
    return policy

def patience_policy(h: int) -> Policy:
    def policy(obs: Observable, history: tuple[tuple[Observable, str], ...]) -> str:
        if obs.active_break or obs.decision_change or obs.upstream == "REOPEN":
            return "REOPEN"
        streak = 1
        for prev, _ in reversed(history):
            if (
                prev.projection == obs.projection
                and not prev.active_break
                and not prev.decision_change
            ):
                streak += 1
            else:
                break
        return "STOP" if streak >= h else "CONTINUE"
    return policy

def lag_policy(lam: int) -> Policy:
    def policy(obs: Observable, history: tuple[tuple[Observable, str], ...]) -> str:
        if obs.active_break or obs.decision_change or obs.upstream == "REOPEN":
            return "REOPEN"
        if not is_eligible(obs):
            return "CONTINUE"
        streak = 1
        for prev, _ in reversed(history):
            if is_eligible(prev):
                streak += 1
            else:
                break
        return "STOP" if streak >= lam + 1 else "CONTINUE"
    return policy

def simulate(trace: Trace, policy: Policy) -> tuple[str, ...]:
    history: list[tuple[Observable, str]] = []
    actions: list[str] = []
    inquiry_active = True
    for step in trace.steps:
        obs = step.obs
        if not inquiry_active and not (
            obs.active_break or obs.decision_change or obs.upstream == "REOPEN"
        ):
            action = "IDLE"
        else:
            action = policy(obs, tuple(history))
            if action == "STOP":
                inquiry_active = False
            elif action == "REOPEN":
                inquiry_active = True
        actions.append(action)
        history.append((obs, action))
    return tuple(actions)

def _next_novel_break(trace: Trace, start: int) -> int:
    for i in range(start + 1, len(trace.steps)):
        o = trace.steps[i].obs
        if o.active_break or o.decision_change or o.upstream == "REOPEN":
            return i
    return len(trace.steps)

def score_trace(trace: Trace, actions: tuple[str, ...]) -> MetricVector:
    pse = pd = ae = missed = 0
    oiw = 0.0
    rl_values: list[int] = []

    episode_start = 0
    stopped_in_episode = False
    had_any_stop = False

    for i, (step, action) in enumerate(zip(trace.steps, actions)):
        obs, gold = step.obs, step.gold

        if action == "STOP":
            had_any_stop = True
            stopped_in_episode = True
            if gold.live_unsafe:
                pse += 1
                end = _next_novel_break(trace, i)
                safe = next(
                    (j for j in range(i + 1, end) if not trace.steps[j].gold.live_unsafe),
                    end,
                )
                pd += max(0, safe - i)
            if gold.action_wrong_if_stop:
                ae += 1

            earliest_safe = next(
                (
                    j
                    for j in range(episode_start, i + 1)
                    if not trace.steps[j].gold.live_unsafe
                ),
                None,
            )
            if earliest_safe is not None and i > earliest_safe:
                oiw += sum(
                    trace.steps[j].obs.step_cost
                    for j in range(earliest_safe + 1, i + 1)
                )

        novel_break = obs.active_break or obs.decision_change or obs.upstream == "REOPEN"
        if novel_break:
            if stopped_in_episode:
                reopened = next(
                    (j for j in range(i, len(actions)) if actions[j] == "REOPEN"),
                    None,
                )
                if reopened is None:
                    missed += 1
                else:
                    rl_values.append(reopened - i)
            episode_start = min(i + 1, len(trace.steps) - 1)
            stopped_in_episode = False

    if not had_any_stop:
        earliest_safe = next(
            (i for i, s in enumerate(trace.steps) if not s.gold.live_unsafe),
            None,
        )
        if earliest_safe is not None:
            oiw += sum(
                trace.steps[j].obs.step_cost
                for j in range(earliest_safe + 1, len(trace.steps))
            )

    return MetricVector(
        pse_live=pse,
        pd_live=pd,
        ae_live=ae,
        oiw=round(oiw, 6),
        rl_max=max(rl_values, default=0),
        missed_reopen=missed,
        ber=0 if had_any_stop else 1,
    )

def aggregate(traces: Iterable[Trace], policy: Policy) -> MetricVector:
    total = MetricVector()
    for trace in traces:
        total = total.add(score_trace(trace, simulate(trace, policy)))
    return total

def pareto_dominates(a: MetricVector, b: MetricVector) -> bool:
    av, bv = a.tuple(), b.tuple()
    return all(x <= y for x, y in zip(av, bv)) and any(
        x < y for x, y in zip(av, bv)
    )

def calibration_key(m: MetricVector, parameter: int) -> tuple[float, ...]:
    return (
        m.pse_live,
        m.ae_live,
        m.missed_reopen,
        m.oiw,
        m.ber,
        m.pd_live,
        m.rl_max,
        parameter,
    )
