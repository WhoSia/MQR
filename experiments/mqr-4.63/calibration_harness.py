from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"

WORLD_SPECS = {
    "CAUSAL-SEP": {"seeds": 64, "budget": 6},
    "SENSING-GRID": {"seeds": 64, "budget": 12},
    "SCOUT-PARK": {"seeds": 96, "budget": 20},
    "THEORY-ECOLOGY": {"seeds": 96, "budget": 30},
    "SAMPLE-RESERVE": {"seeds": 96, "budget": 10},
}

POLICIES = {
    "CAUSAL-SEP": [
        "causal_identifiability", "expected_elimination", "random", "mqr_full"
    ],
    "SENSING-GRID": [
        "entropy_greedy", "horizon2", "random", "mqr_full"
    ],
    "SCOUT-PARK": [
        "current_information", "information_per_bandwidth", "high_rate_scout",
        "fixed_park", "random_mix", "mqr_full", "mqr_minus_opr",
        "mqr_minus_arr", "mqr_minus_nedl", "mqr_minus_exterior"
    ],
    "THEORY-ECOLOGY": [
        "confirmation", "falsification", "disagreement", "random",
        "representative", "robust_multifactor", "mqr_full", "mqr_minus_arr",
        "mqr_minus_eai", "mqr_minus_nedl", "mqr_minus_exterior"
    ],
    "SAMPLE-RESERVE": [
        "immediate_information", "information_per_cost", "fixed_preserve",
        "nondestructive_first", "random", "mqr_full", "mqr_minus_opr",
        "mqr_minus_arr", "mqr_minus_nedl"
    ],
}

METRIC_ORIENTATION = {
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


def stable_seed(world: str, seed: int, policy: str) -> int:
    x = seed * 1000003 + sum((i + 1) * ord(c) for i, c in enumerate(world + "|" + policy))
    return x & 0xFFFFFFFF


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def shannon(ps: List[float]) -> float:
    out = 0.0
    for p in ps:
        if p > 0:
            out -= p * math.log(p, 2)
    return out


def metric_receipt(pr: Dict[str, float], budget: int) -> Dict[str, float]:
    possible_exterior = pr.get("possible_exterior", 0.0)
    initial_sep = pr.get("initial_separators", 0.0)
    initial_routes = pr.get("initial_reopening_routes", 0.0)
    nominal = pr.get("nominal_evidence", 0.0)
    max_ancestry = pr.get("max_ancestry_classes", 0.0)
    max_destroyable = pr.get("max_destroyable", 0.0)
    debt_bound = pr.get("debt_bound", 0.0)
    blind_bound = pr.get("blind_bound", 0.0)

    return {
        "ERR": clamp01(pr.get("recovered_exterior", 0.0) / possible_exterior) if possible_exterior > 0 else 0.0,
        "FSR": clamp01(pr.get("retained_separators", initial_sep) / initial_sep) if initial_sep > 0 else 1.0,
        "RCR": clamp01(pr.get("reopening_routes", initial_routes) / initial_routes) if initial_routes > 0 else 1.0,
        "RL": clamp01(pr.get("reopening_latency", 0.0) / max(1, budget)),
        "EAI": clamp01(pr.get("ancestry_classes", 0.0) / max_ancestry) if max_ancestry > 0 and nominal > 0 else 1.0,
        "BOD": clamp01(pr.get("destroyed_options", 0.0) / max_destroyable) if max_destroyable > 0 else 0.0,
        "CSD": clamp01(pr.get("contamination_events", 0.0) / max(1, budget)),
        "NED": clamp01(pr.get("exploration_debt_raw", 0.0) / debt_bound) if debt_bound > 0 else 0.0,
        "BSI": clamp01(pr.get("blind_mass", 0.0) / blind_bound) if blind_bound > 0 else 0.0,
    }


# ---------------- CAUSAL-SEP ----------------

CAUSAL_ACTION_MASKS = {
    "I0": 0b0001,
    "I1": 0b0010,
    "I2": 0b0100,
    "I3": 0b1000,
    "I01": 0b0011,
    "I23": 0b1100,
    "I02": 0b0101,
    "I13": 0b1010,
}


def causal_partition_gain(posterior: List[int], mask: int) -> float:
    buckets: Dict[int, int] = {}
    for h in posterior:
        outcome = h & mask
        buckets[outcome] = buckets.get(outcome, 0) + 1
    before = math.log(max(1, len(posterior)), 2)
    exp_after = 0.0
    n = len(posterior)
    for count in buckets.values():
        p = count / n
        exp_after += p * math.log(count, 2)
    return before - exp_after


def run_causal(seed: int, policy: str) -> Dict:
    budget = WORLD_SPECS["CAUSAL-SEP"]["budget"]
    true_h = random.Random(seed + 463).randrange(16)
    posterior = list(range(16))
    used = []
    rng = random.Random(stable_seed("CAUSAL-SEP", seed, policy))

    for _ in range(budget):
        if len(posterior) == 1:
            break
        gains = {a: causal_partition_gain(posterior, m) for a, m in CAUSAL_ACTION_MASKS.items()}
        if policy == "random":
            action = rng.choice(sorted(CAUSAL_ACTION_MASKS))
        else:
            # causal_identifiability, expected_elimination, and mqr_full intentionally coincide
            action = max(sorted(gains), key=lambda a: gains[a])
        used.append(action)
        mask = CAUSAL_ACTION_MASKS[action]
        obs = true_h & mask
        posterior = [h for h in posterior if (h & mask) == obs]

    success = 1.0 if posterior == [true_h] else 0.0
    error = (len(posterior) - 1) / 15.0
    primitives = {
        "possible_exterior": 0,
        "recovered_exterior": 0,
        "initial_separators": 1,
        "retained_separators": 1,
        "initial_reopening_routes": 1,
        "reopening_routes": 1,
        "reopening_latency": 0,
        "nominal_evidence": len(used),
        "ancestry_classes": len(set(used)),
        "max_ancestry_classes": len(CAUSAL_ACTION_MASKS),
        "destroyed_options": 0,
        "max_destroyable": 0,
        "contamination_events": 0,
        "exploration_debt_raw": 0,
        "debt_bound": budget,
        "blind_mass": 0,
        "blind_bound": 1,
    }
    row = {
        "world": "CAUSAL-SEP", "seed": seed, "policy": policy,
        "steps": len(used), "actions": used,
        "conventional_success": success,
        "conventional_error": error,
        "cost": len(used) / budget,
        "primitives": primitives,
    }
    row.update(metric_receipt(primitives, budget))
    return row


# ---------------- SENSING-GRID ----------------

N_SENSE = 7


def sensing_transition(p: List[float]) -> List[float]:
    out = [0.0] * N_SENSE
    for i, mass in enumerate(p):
        out[i] += 0.5 * mass
        out[(i - 1) % N_SENSE] += 0.25 * mass
        out[(i + 1) % N_SENSE] += 0.25 * mass
    return out


def sensor_likelihood(obs: int, target: int, node: int) -> float:
    at = target == node
    return 0.90 if (obs == 1 and at) or (obs == 0 and not at) else 0.10


def expected_sensor_entropy(belief: List[float], node: int) -> float:
    p_yes = sum(b * (0.90 if i == node else 0.10) for i, b in enumerate(belief))
    out = 0.0
    for obs, po in [(1, p_yes), (0, 1 - p_yes)]:
        if po <= 0:
            continue
        post = [belief[i] * sensor_likelihood(obs, i, node) for i in range(N_SENSE)]
        z = sum(post)
        post = [x / z for x in post]
        out += po * shannon(post)
    return out


def run_sensing(seed: int, policy: str) -> Dict:
    budget = WORLD_SPECS["SENSING-GRID"]["budget"]
    world_rng = random.Random(seed + 1463)
    target = world_rng.randrange(N_SENSE)
    trajectory = []
    noise = []
    for t in range(budget):
        move = world_rng.random()
        if move < 0.25:
            target = (target - 1) % N_SENSE
        elif move < 0.50:
            target = (target + 1) % N_SENSE
        trajectory.append(target)
        noise.append([world_rng.random() for _ in range(N_SENSE)])

    belief = [1.0 / N_SENSE] * N_SENSE
    used = []
    true_mass = []
    rng = random.Random(stable_seed("SENSING-GRID", seed, policy))

    for t in range(budget):
        belief = sensing_transition(belief)
        if policy == "random":
            node = rng.randrange(N_SENSE)
        else:
            scores = {}
            for n in range(N_SENSE):
                immediate = shannon(belief) - expected_sensor_entropy(belief, n)
                if policy == "horizon2":
                    novelty = 0.02 if n not in used[-3:] else 0.0
                    scores[n] = immediate + novelty
                else:  # entropy_greedy and mqr_full intentionally coincide
                    scores[n] = immediate
            node = max(sorted(scores), key=lambda n: scores[n])
        used.append(node)

        truth = trajectory[t] == node
        obs = 1 if (noise[t][node] < (0.90 if truth else 0.10)) else 0
        post = [belief[i] * sensor_likelihood(obs, i, node) for i in range(N_SENSE)]
        z = sum(post)
        belief = [x / z for x in post]
        true_mass.append(belief[trajectory[t]])

    success = statistics.mean(true_mass)
    primitives = {
        "possible_exterior": 0,
        "recovered_exterior": 0,
        "initial_separators": 1,
        "retained_separators": 1,
        "initial_reopening_routes": 1,
        "reopening_routes": 1,
        "reopening_latency": 0,
        "nominal_evidence": budget,
        "ancestry_classes": len(set(used)),
        "max_ancestry_classes": N_SENSE,
        "destroyed_options": 0,
        "max_destroyable": 0,
        "contamination_events": 0,
        "exploration_debt_raw": 0,
        "debt_bound": budget,
        "blind_mass": 0,
        "blind_bound": 1,
    }
    row = {
        "world": "SENSING-GRID", "seed": seed, "policy": policy,
        "steps": budget, "actions": used,
        "conventional_success": success,
        "conventional_error": 1.0 - success,
        "cost": 1.0,
        "primitives": primitives,
    }
    row.update(metric_receipt(primitives, budget))
    return row


# ---------------- SCOUT-PARK ----------------

SCOUT_MODES = {
    "FULL": {"n": 2, "rich": True, "raw": True, "compute": 0.0},
    "SCOUT": {"n": 10, "rich": False, "raw": False, "compute": 0.0},
    "PARK": {"n": 2, "rich": True, "raw": True, "compute": 0.12},
}


def scout_policy(policy: str, t: int, stratum: str, raw_by_stratum: Dict[str, int], debt: int, rng: random.Random) -> str:
    if policy in ("current_information", "information_per_bandwidth", "high_rate_scout"):
        return "SCOUT"
    if policy == "fixed_park":
        return "PARK" if t % 4 == 3 else "SCOUT"
    if policy == "random_mix":
        return rng.choice(["FULL", "SCOUT", "PARK"])

    # MQR family: baseline is SCOUT; typed guards only constrain/reserve routes.
    use_opr = policy != "mqr_minus_opr"
    use_arr = policy != "mqr_minus_arr"
    use_ned = policy != "mqr_minus_nedl"
    use_ext = policy != "mqr_minus_exterior"

    if use_opr and stratum == "LOW" and raw_by_stratum["LOW"] == 0:
        return "PARK"
    if use_ned and debt >= 2:
        return "PARK"
    if use_arr and (t % 5 == 4) and sum(raw_by_stratum.values()) < 3:
        return "PARK"
    if use_ext and t % 7 == 6:
        return "FULL"
    return "SCOUT"


def run_scout(seed: int, policy: str) -> Dict:
    budget = WORLD_SPECS["SCOUT-PARK"]["budget"]
    world_rng = random.Random(seed + 2463)
    rounds = []
    for t in range(budget):
        stratum = "LOW" if world_rng.random() < 0.45 else "HIGH"
        events = []
        for _ in range(12):
            r = world_rng.random()
            kind = "HIDDEN" if r < (0.09 if stratum == "LOW" else 0.02) else ("KNOWN" if r < 0.24 else "BG")
            events.append(kind)
        rounds.append((stratum, events))

    rng = random.Random(stable_seed("SCOUT-PARK", seed, policy))
    raw_by_stratum = {"LOW": 0, "HIGH": 0}
    modes = []
    nominal = 0
    known_detected = 0
    hidden_total = 0
    hidden_recovered = 0
    hidden_first_recovery = None
    reveal = budget // 2
    debt = 0
    debt_sum = 0
    low_rounds = 0
    low_no_raw = 0
    destroyed = 0
    compute_debt = 0.0

    # Count all exterior opportunities in the fixed world.
    for _, events in rounds[reveal:]:
        hidden_total += sum(1 for e in events if e == "HIDDEN")

    for t, (stratum, events) in enumerate(rounds):
        if stratum == "LOW":
            low_rounds += 1
        action = scout_policy(policy, t, stratum, raw_by_stratum, debt, rng)
        modes.append(action)
        spec = SCOUT_MODES[action]
        kept = events[:spec["n"]]
        nominal += len(kept)
        compute_debt += spec["compute"]

        known_detected += sum(1 for e in kept if e == "KNOWN")

        if spec["raw"]:
            raw_by_stratum[stratum] += len(kept)
            if t >= reveal:
                hr = sum(1 for e in kept if e == "HIDDEN")
                hidden_recovered += hr
                if hr > 0 and hidden_first_recovery is None:
                    hidden_first_recovery = t

        if t >= reveal:
            # Hidden events in the full incoming batch not retained in raw form are future options lost.
            raw_hidden = sum(1 for e in kept if e == "HIDDEN") if spec["raw"] else 0
            destroyed += max(0, sum(1 for e in events if e == "HIDDEN") - raw_hidden)

        if stratum == "LOW" and not spec["raw"]:
            low_no_raw += 1
            debt += 1
        elif spec["raw"] and stratum == "LOW":
            debt = max(0, debt - 2)
        debt_sum += debt

    max_known = sum(sum(1 for e in ev[:10] if e == "KNOWN") for _, ev in rounds)
    success = known_detected / max(1, max_known)
    retained_strata = sum(1 for v in raw_by_stratum.values() if v > 0)
    latency = budget - reveal if hidden_first_recovery is None else max(0, hidden_first_recovery - reveal)
    primitives = {
        "possible_exterior": hidden_total,
        "recovered_exterior": hidden_recovered,
        "initial_separators": 2,
        "retained_separators": retained_strata,
        "initial_reopening_routes": 2,
        "reopening_routes": retained_strata,
        "reopening_latency": latency,
        "nominal_evidence": nominal,
        "ancestry_classes": len(set(modes)),
        "max_ancestry_classes": 3,
        "destroyed_options": destroyed,
        "max_destroyable": hidden_total,
        "contamination_events": 0,
        "exploration_debt_raw": debt_sum,
        "debt_bound": max(1, budget * max(1, low_rounds)),
        "blind_mass": low_no_raw,
        "blind_bound": max(1, low_rounds),
    }
    row = {
        "world": "SCOUT-PARK", "seed": seed, "policy": policy,
        "steps": budget, "actions": modes,
        "conventional_success": clamp01(success),
        "conventional_error": clamp01(1.0 - success),
        "cost": clamp01((20 * budget + compute_debt * 20) / (24 * budget)),
        "primitives": primitives,
    }
    row.update(metric_receipt(primitives, budget))
    return row


# ---------------- THEORY-ECOLOGY ----------------

XGRID = [(-1.0 + i * 0.1) for i in range(21)]


def true_theory_label(x: float) -> int:
    # Current-family rule in the center, hidden reversal at the exterior.
    if abs(x) <= 0.6:
        return 1 if x >= 0 else 0
    return 0 if x >= 0 else 1


def model_pred(model: str, x: float) -> int:
    if model == "SIGN":
        return 1 if x >= 0 else 0
    if model == "PLUS":
        return 1
    if model == "MINUS":
        return 0
    if model == "PIECEWISE":
        return true_theory_label(x)
    raise ValueError(model)


def bin_id(x: float) -> int:
    if x < -0.6:
        return 0
    if x < -0.2:
        return 1
    if x <= 0.2:
        return 2
    if x <= 0.6:
        return 3
    return 4


def model_errors(data: List[Tuple[float, int]], models: List[str]) -> Dict[str, float]:
    out = {}
    for m in models:
        if not data:
            out[m] = 0.5
        else:
            out[m] = sum(model_pred(m, x) != y for x, y in data) / len(data)
    return out


def choose_theory_action(policy: str, data: List[Tuple[float, int]], counts: Dict[int, int],
                         current_models: List[str], debt: int, t: int, rng: random.Random) -> float:
    errs = model_errors(data, current_models)
    dominant = min(current_models, key=lambda m: (errs[m], m))

    def disagreement_score(x: float) -> float:
        preds = [model_pred(m, x) for m in current_models]
        p = sum(preds) / len(preds)
        return 4 * p * (1 - p)

    def represent_score(x: float) -> float:
        return 1.0 / (1.0 + counts[bin_id(x)])

    def deamp_score(x: float) -> float:
        b = bin_id(x)
        if not data:
            return 1.0
        local = [(xx, yy) for xx, yy in data if bin_id(xx) == b]
        if not local:
            return 1.0
        return sum(model_pred(dominant, xx) != yy for xx, yy in local) / len(local)

    if policy == "random":
        return rng.choice(XGRID)
    if policy == "confirmation":
        # Prefer regions where the current family agrees and already looks successful.
        return min(XGRID, key=lambda x: (disagreement_score(x), -counts[bin_id(x)], abs(x)))
    if policy == "falsification":
        # Stress the dominant theory where an alternative disagrees most.
        return max(XGRID, key=lambda x: (disagreement_score(x), abs(x)))
    if policy == "disagreement":
        return max(XGRID, key=lambda x: (disagreement_score(x), represent_score(x)))
    if policy == "representative":
        return max(XGRID, key=lambda x: (represent_score(x), abs(x)))
    if policy == "robust_multifactor":
        return max(XGRID, key=lambda x: (0.45 * disagreement_score(x) + 0.35 * represent_score(x) + 0.20 * deamp_score(x), abs(x)))

    use_arr = policy != "mqr_minus_arr"
    use_eai = policy != "mqr_minus_eai"
    use_ned = policy != "mqr_minus_nedl"
    use_ext = policy != "mqr_minus_exterior"

    # Base policy is robust_multifactor.
    scores = {}
    for x in XGRID:
        s = 0.45 * disagreement_score(x) + 0.35 * represent_score(x) + 0.20 * deamp_score(x)
        if use_eai and data and bin_id(x) == bin_id(data[-1][0]):
            s -= 0.18
        scores[x] = s

    exterior = [x for x in XGRID if abs(x) > 0.6]
    if use_arr and t % 6 == 5:
        return max(exterior, key=lambda x: (represent_score(x), abs(x)))
    if use_ned and debt >= 3:
        return max(exterior, key=lambda x: (represent_score(x), abs(x)))
    if use_ext and sum(counts[b] for b in (0, 4)) == 0 and t >= 4:
        return max(exterior, key=lambda x: (represent_score(x), abs(x)))
    return max(XGRID, key=lambda x: (scores[x], abs(x)))


def run_theory(seed: int, policy: str) -> Dict:
    budget = WORLD_SPECS["THEORY-ECOLOGY"]["budget"]
    world_rng = random.Random(seed + 3463)
    # Pre-generated observation noise for every step/context: paired latent world across policies.
    noise = [[world_rng.random() for _ in XGRID] for _ in range(budget)]
    idx_of = {round(x, 1): i for i, x in enumerate(XGRID)}

    rng = random.Random(stable_seed("THEORY-ECOLOGY", seed, policy))
    data: List[Tuple[float, int]] = []
    counts = {i: 0 for i in range(5)}
    current_models = ["SIGN", "PLUS", "MINUS"]
    detected_bins = set()
    detection_step = None
    debt = 0
    debt_sum = 0

    for t in range(budget):
        x = choose_theory_action(policy, data, counts, current_models, debt, t, rng)
        ix = idx_of[round(x, 1)]
        y_true = true_theory_label(x)
        y = y_true if noise[t][ix] >= 0.08 else 1 - y_true
        data.append((x, y))
        b = bin_id(x)
        counts[b] += 1

        if b in (0, 4):
            # Exterior contradiction against the central SIGN family.
            if model_pred("SIGN", x) != y:
                detected_bins.add(b)

        if len(detected_bins) >= 2 and "PIECEWISE" not in current_models:
            current_models.append("PIECEWISE")
            detection_step = t

        # Debt is skipped exterior discriminating capacity while policy remains interior-heavy.
        if b not in (0, 4) and min(counts[0], counts[4]) == 0:
            debt += 1
        elif b in (0, 4):
            debt = max(0, debt - 1)
        debt_sum += debt

    errs = model_errors(data, current_models)
    best = min(current_models, key=lambda m: (errs[m], m))
    global_error = sum(model_pred(best, x) != true_theory_label(x) for x in XGRID) / len(XGRID)
    blind_contexts = sum(1 for x in XGRID if abs(x) > 0.6 and counts[bin_id(x)] == 0)
    exterior_contexts = sum(1 for x in XGRID if abs(x) > 0.6)
    sampled_bins = sum(1 for c in counts.values() if c > 0)
    latency = budget if detection_step is None else detection_step
    primitives = {
        "possible_exterior": 2,
        "recovered_exterior": len(detected_bins),
        "initial_separators": 2,
        "retained_separators": 2,  # contexts are not physically destroyed
        "initial_reopening_routes": 2,
        "reopening_routes": sum(1 for b in (0, 4) if counts[b] > 0),
        "reopening_latency": latency,
        "nominal_evidence": len(data),
        "ancestry_classes": sampled_bins,
        "max_ancestry_classes": 5,
        "destroyed_options": 0,
        "max_destroyable": 0,
        "contamination_events": 0,
        "exploration_debt_raw": debt_sum,
        "debt_bound": budget * budget,
        "blind_mass": blind_contexts,
        "blind_bound": max(1, exterior_contexts),
    }
    row = {
        "world": "THEORY-ECOLOGY", "seed": seed, "policy": policy,
        "steps": budget, "actions": [x for x, _ in data],
        "conventional_success": clamp01(1.0 - global_error),
        "conventional_error": clamp01(global_error),
        "cost": 1.0,
        "primitives": primitives,
        "best_model": best,
    }
    row.update(metric_receipt(primitives, budget))
    return row


# ---------------- SAMPLE-RESERVE ----------------

STRATA = ["A", "B", "C", "D"]


def choose_sample_action(policy: str, t: int, pristine: Dict[str, int], current_resolved: Dict[str, bool],
                         future_available: bool, future_resolved: Dict[str, bool], debt: int,
                         rng: random.Random) -> Tuple[str, str]:
    unresolved_current = [s for s in STRATA if not current_resolved[s]]
    unresolved_future = [s for s in STRATA if future_available and not future_resolved[s] and pristine[s] > 0]

    if future_available and unresolved_future:
        # All policies may exploit the new assay if a route survived.
        return ("FUTURE", sorted(unresolved_future, key=lambda s: (pristine[s], s))[0])

    target = (unresolved_current or STRATA)[0]
    if policy == "immediate_information":
        return ("DESTRUCTIVE", target)
    if policy == "information_per_cost":
        return ("NONDESTRUCTIVE", target)
    if policy == "fixed_preserve":
        if pristine[target] <= 1:
            return ("NONDESTRUCTIVE", target)
        return ("DESTRUCTIVE", target)
    if policy == "nondestructive_first":
        return ("NONDESTRUCTIVE", target)
    if policy == "random":
        s = rng.choice(STRATA)
        return (rng.choice(["DESTRUCTIVE", "NONDESTRUCTIVE"]), s)

    use_opr = policy != "mqr_minus_opr"
    use_arr = policy != "mqr_minus_arr"
    use_ned = policy != "mqr_minus_nedl"

    if use_opr and pristine[target] <= 1:
        return ("NONDESTRUCTIVE", target)
    if use_arr and sum(1 for s in STRATA if pristine[s] > 0) <= 2:
        return ("NONDESTRUCTIVE", target)
    if use_ned and debt >= 2:
        return ("NONDESTRUCTIVE", target)
    return ("DESTRUCTIVE", target)


def run_sample(seed: int, policy: str) -> Dict:
    budget = WORLD_SPECS["SAMPLE-RESERVE"]["budget"]
    world_rng = random.Random(seed + 4463)
    current_truth = {s: world_rng.choice([0, 1]) for s in STRATA}
    future_truth = {s: world_rng.choice([0, 1]) for s in STRATA}
    # Noisy nondestructive observations pre-generated.
    nond_noise = {(t, s): world_rng.random() for t in range(budget) for s in STRATA}

    pristine = {s: 3 for s in STRATA}
    current_resolved = {s: False for s in STRATA}
    future_resolved = {s: False for s in STRATA}
    current_votes = {s: [] for s in STRATA}
    destroyed_last = set()
    debt = 0
    debt_sum = 0
    actions = []
    rng = random.Random(stable_seed("SAMPLE-RESERVE", seed, policy))
    reveal = budget // 2
    retained_at_reveal = None
    cost_raw = 0.0

    for t in range(budget):
        future_available = t >= reveal
        if t == reveal:
            retained_at_reveal = sum(1 for s in STRATA if pristine[s] > 0)

        kind, s = choose_sample_action(policy, t, pristine, current_resolved, future_available,
                                       future_resolved, debt, rng)
        actions.append(f"{kind}:{s}")

        if kind == "DESTRUCTIVE":
            if pristine[s] <= 0:
                kind = "NONDESTRUCTIVE"
            else:
                pristine[s] -= 1
                cost_raw += 1.0
                current_resolved[s] = True
                current_votes[s] = [current_truth[s]]
                if pristine[s] == 0 and t < reveal:
                    destroyed_last.add(s)
                    debt += 1
        if kind == "NONDESTRUCTIVE":
            cost_raw += 0.35
            p_correct = 0.72
            obs = current_truth[s] if nond_noise[(t, s)] < p_correct else 1 - current_truth[s]
            current_votes[s].append(obs)
            if len(current_votes[s]) >= 3:
                current_resolved[s] = True
        elif kind == "FUTURE":
            if pristine[s] > 0:
                pristine[s] -= 1
                cost_raw += 0.8
                future_resolved[s] = True
                debt = max(0, debt - 1)

        debt_sum += debt

    if retained_at_reveal is None:
        retained_at_reveal = sum(1 for s in STRATA if pristine[s] > 0)

    current_score = sum(1 for s in STRATA if current_resolved[s]) / len(STRATA)
    future_score = sum(1 for s in STRATA if future_resolved[s]) / len(STRATA)
    # Conventional target is current inquiry; future score remains an exterior-recovery coordinate.
    success = current_score
    primitives = {
        "possible_exterior": len(STRATA),
        "recovered_exterior": sum(1 for s in STRATA if future_resolved[s]),
        "initial_separators": len(STRATA),
        "retained_separators": retained_at_reveal,
        "initial_reopening_routes": len(STRATA),
        "reopening_routes": retained_at_reveal,
        "reopening_latency": 0 if future_score > 0 else (budget - reveal),
        "nominal_evidence": len(actions),
        "ancestry_classes": len(set(a.split(":")[0] for a in actions)),
        "max_ancestry_classes": 3,
        "destroyed_options": len(destroyed_last),
        "max_destroyable": len(STRATA),
        "contamination_events": 0,
        "exploration_debt_raw": debt_sum,
        "debt_bound": budget * len(STRATA),
        "blind_mass": 0,
        "blind_bound": 1,
    }
    row = {
        "world": "SAMPLE-RESERVE", "seed": seed, "policy": policy,
        "steps": budget, "actions": actions,
        "conventional_success": clamp01(success),
        "conventional_error": clamp01(1.0 - success),
        "cost": clamp01(cost_raw / budget),
        "future_success": future_score,
        "primitives": primitives,
    }
    row.update(metric_receipt(primitives, budget))
    return row


RUNNERS = {
    "CAUSAL-SEP": run_causal,
    "SENSING-GRID": run_sensing,
    "SCOUT-PARK": run_scout,
    "THEORY-ECOLOGY": run_theory,
    "SAMPLE-RESERVE": run_sample,
}


def run_all() -> List[Dict]:
    rows = []
    for world, spec in WORLD_SPECS.items():
        runner = RUNNERS[world]
        for seed in range(spec["seeds"]):
            for policy in POLICIES[world]:
                rows.append(runner(seed, policy))
    return rows


def structural_checks(rows: List[Dict]) -> None:
    by_world = {}
    for r in rows:
        by_world.setdefault(r["world"], []).append(r)
        for k in METRIC_ORIENTATION:
            if not (0.0 <= r[k] <= 1.0):
                raise AssertionError((r["world"], r["policy"], k, r[k]))

    # Frozen negative-control invariants.
    for world in ("CAUSAL-SEP", "SENSING-GRID"):
        for r in by_world[world]:
            assert r["BOD"] == 0.0, (world, "BOD", r)
            assert r["CSD"] == 0.0, (world, "CSD", r)
            assert r["NED"] == 0.0, (world, "NED", r)
    for r in by_world["THEORY-ECOLOGY"]:
        assert r["BOD"] == 0.0, ("THEORY-ECOLOGY", "BOD", r)
    for r in by_world["SCOUT-PARK"]:
        assert r["CSD"] == 0.0, ("SCOUT-PARK", "CSD", r)

    # Paired completeness.
    for world, spec in WORLD_SPECS.items():
        got = {(r["seed"], r["policy"]) for r in by_world[world]}
        exp = {(s, p) for s in range(spec["seeds"]) for p in POLICIES[world]}
        assert got == exp, (world, len(got), len(exp))


def write_rows(rows: List[Dict]) -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    with (RESULTS / "raw_runs.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")

    summary = {
        "stage": "MQR-4.63",
        "preseal_commit": "a0dcb1605dbc691cca414d5b27b4fcdf8dc5e910",
        "manifest_commit": "d114f87ba2e295a6a838c74989f12173f213d312",
        "analysis_plan_commit": "818798005b9e02ec73c03ef98cfa1b0e98c8efed",
        "worlds": {w: {"seeds": WORLD_SPECS[w]["seeds"], "budget": WORLD_SPECS[w]["budget"], "policies": POLICIES[w]} for w in WORLD_SPECS},
        "run_count": len(rows),
        "scalar_mqr_score": "FORBIDDEN",
    }
    (RESULTS / "run_manifest.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", choices=list(WORLD_SPECS))
    ap.add_argument("--seed", type=int)
    ap.add_argument("--policy")
    args = ap.parse_args()

    if args.world is not None:
        if args.seed is None or args.policy is None:
            ap.error("--world requires --seed and --policy")
        if args.policy not in POLICIES[args.world]:
            ap.error("invalid policy for world")
        row = RUNNERS[args.world](args.seed, args.policy)
        print(json.dumps(row, sort_keys=True))
        return

    rows = run_all()
    structural_checks(rows)
    write_rows(rows)
    print(f"MQR463_WORLD_COUNT={len(WORLD_SPECS)}")
    print(f"MQR463_RUN_COUNT={len(rows)}")
    print("MQR463_NEGATIVE_CONTROL_INVARIANTS=PASS")
    print("MQR463_PAIRED_REPLAY_COMPLETENESS=PASS")
    print("MQR463_SCALAR_MQR_SCORE=FORBIDDEN")


if __name__ == "__main__":
    main()
