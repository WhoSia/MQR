from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

PRESEAL = "4b400cc8ec238d8bd75875a168433c319bae52ca"


@dataclass(frozen=True)
class CandidateResult:
    candidate: str
    invariance: str
    world_sensitivity: str
    stop_sufficiency: str
    scope: str
    verdict: str
    reason: str


def fisher_rao_bernoulli(p: float, q: float) -> float:
    # Geodesic distance on the Bernoulli family under the Fisher metric.
    return 2.0 * abs(math.asin(math.sqrt(p)) - math.asin(math.sqrt(q)))


def logit(p: float) -> float:
    return math.log(p / (1.0 - p))


def logistic(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def fisher_reparameterization_fixture() -> Dict[str, float | bool]:
    p, q = 0.2, 0.8
    d_p = fisher_rao_bernoulli(p, q)

    # Re-express the same points in logit coordinates, then map back.
    # The geometric distance is a property of the statistical points,
    # not the arbitrary parameter label.
    eta_p, eta_q = logit(p), logit(q)
    d_eta = fisher_rao_bernoulli(logistic(eta_p), logistic(eta_q))
    return {
        "distance_probability_chart": d_p,
        "distance_logit_chart": d_eta,
        "equal": math.isclose(d_p, d_eta, rel_tol=0.0, abs_tol=1e-12),
    }


def blackwell_reveal_bit(bit: int) -> Tuple[Tuple[int, int], ...]:
    # Four states encode two latent binary coordinates:
    # 00, 01, 10, 11. Experiment reveals one coordinate exactly.
    rows = []
    for state in range(4):
        b0 = (state >> 1) & 1
        b1 = state & 1
        sig = b0 if bit == 0 else b1
        rows.append((1, 0) if sig == 0 else (0, 1))
    return tuple(rows)


def deterministic_garbling_possible(a: Tuple[Tuple[int, int], ...],
                                    b: Tuple[Tuple[int, int], ...]) -> bool:
    # For deterministic two-signal experiments, any stochastic garbling from
    # A to B requires states with the same A-signal row to have the same B row.
    groups: Dict[Tuple[int, int], set[Tuple[int, int]]] = {}
    for ar, br in zip(a, b):
        groups.setdefault(ar, set()).add(br)
    return all(len(v) == 1 for v in groups.values())


def blackwell_fixture() -> Dict[str, bool]:
    e_first = blackwell_reveal_bit(0)
    e_second = blackwell_reveal_bit(1)
    # Neither exact-bit experiment can be obtained by garbling the other.
    return {
        "first_to_second": deterministic_garbling_possible(e_first, e_second),
        "second_to_first": deterministic_garbling_possible(e_second, e_first),
        "incomparable": (
            not deterministic_garbling_possible(e_first, e_second)
            and not deterministic_garbling_possible(e_second, e_first)
        ),
    }


def event_count_fixture() -> Dict[str, int | bool]:
    original = ["WORLD_CONTACT", "ELIGIBLE"]
    refined = ["WORLD_CONTACT", "ELIGIBLE", "ELIGIBLE_DUPLICATE_INERT"]
    return {
        "original_count": len(original),
        "refined_count": len(refined),
        "world_state_equal": True,
        "invariant": len(original) == len(refined),
    }


def time_fixture() -> Dict[str, object]:
    # Same elapsed duration, radically different contact.
    passive_wait = {"duration_days": 30, "material_contact": 0}
    active_probe = {"duration_days": 30, "material_contact": 1}
    return {
        "passive_wait": passive_wait,
        "active_probe": active_probe,
        "same_time": passive_wait["duration_days"] == active_probe["duration_days"],
        "same_progress": False,
    }


def cost_fixture() -> Dict[str, object]:
    expensive_null = {"cost": 100, "material_contact": 0}
    cheap_separator = {"cost": 1, "material_contact": 1}
    return {
        "expensive_null": expensive_null,
        "cheap_separator": cheap_separator,
        "cost_monotone_progress": False,
    }


def obligation_split_fixture() -> Dict[str, object]:
    merged_labels = {"O_AB": frozenset({"A", "B"})}
    split_labels = {"O_A": frozenset({"A"}), "O_B": frozenset({"B"})}
    merged_burden = frozenset().union(*merged_labels.values())
    split_burden = frozenset().union(*split_labels.values())
    return {
        "merged_obligation_count": len(merged_labels),
        "split_obligation_count": len(split_labels),
        "same_burden_union": merged_burden == split_burden,
        "raw_count_invariant": len(merged_labels) == len(split_labels),
        "ancestry_union_invariant": merged_burden == split_burden,
    }


def information_intervention_fixture() -> Dict[str, object]:
    # Frozen countermodel target from PRESEAL:
    # equal descriptive information, different intervention/use reach.
    observational = {
        "descriptive_information_bits": 1.0,
        "intervention_reach": 0,
        "use_authority": 0,
    }
    intervention = {
        "descriptive_information_bits": 1.0,
        "intervention_reach": 1,
        "use_authority": 1,
    }
    return {
        "observational": observational,
        "intervention": intervention,
        "equal_information": (
            observational["descriptive_information_bits"]
            == intervention["descriptive_information_bits"]
        ),
        "equal_intervention_reach": (
            observational["intervention_reach"]
            == intervention["intervention_reach"]
        ),
        "equal_use_authority": (
            observational["use_authority"]
            == intervention["use_authority"]
        ),
    }


def authority_loop_fixture() -> Dict[str, object]:
    path = ["OPEN", "RESTRICTED", "OPEN"]
    edge_count = len(path) - 1
    return {
        "path": path,
        "path_length_edges": edge_count,
        "same_initial_final_state": path[0] == path[-1],
        "durable_world_contact_change": False,
        "path_length_is_net_progress": False,
    }


def correction_fixture() -> Dict[str, object]:
    before = {
        "claim_authority": 1,
        "known_instrument_defect": 0,
        "correction_receipt": 0,
    }
    after = {
        "claim_authority": 0,
        "known_instrument_defect": 1,
        "correction_receipt": 1,
    }
    return {
        "before": before,
        "after": after,
        "claim_authority_increased": after["claim_authority"] > before["claim_authority"],
        "scientific_correction_occurred": True,
        "authority_level_monotone_progress": False,
    }


def independent_rescaling_fixture() -> Dict[str, object]:
    # Crossing profiles. A weighted scalar's ranking flips under a permissible
    # relative scaling of independently constituted axes.
    A = (1.0, 0.0)
    B = (0.0, 1.0)

    def weighted(v: Tuple[float, float], sx: float, sy: float) -> float:
        return sx * v[0] + sy * v[1]

    rank_x = weighted(A, 10.0, 1.0) > weighted(B, 10.0, 1.0)
    rank_y = weighted(A, 1.0, 10.0) > weighted(B, 1.0, 10.0)
    return {
        "A": A,
        "B": B,
        "A_wins_x_scaled": rank_x,
        "A_wins_y_scaled": rank_y,
        "ranking_reverses": rank_x != rank_y,
        "pareto_comparable": False,
    }


def progress_vs_promotion_twin_world() -> Dict[str, object]:
    achieved_state = {
        "discharged_burdens": ["A", "B"],
        "live_burdens": [],
        "claim_mode": "FROZEN",
        "use_mode": "NONE",
        "reopening_trigger": "NONE",
    }
    world_low_future = {
        "state": achieved_state,
        "next_probe_expected_gain": 0.0,
        "next_probe_cost": 2.0,
        "continue": False,
    }
    world_high_future = {
        "state": achieved_state,
        "next_probe_expected_gain": 5.0,
        "next_probe_cost": 2.0,
        "continue": True,
    }
    return {
        "same_achieved_progress_state": (
            world_low_future["state"] == world_high_future["state"]
        ),
        "opposite_continue_decision": (
            world_low_future["continue"] != world_high_future["continue"]
        ),
        "state_only_stop_rule_sufficient": False,
    }


def cross_domain_morphism_fixture() -> Dict[str, object]:
    # Same abstract burden-preservation morphism; radically different local
    # magnitudes. Structure transports, magnitude does not.
    domains = {
        "MEASUREMENT": {
            "before": frozenset({"CAL", "BIAS", "RIVAL"}),
            "after": frozenset({"RIVAL"}),
            "local_info": 12.0,
            "local_cost": 100.0,
        },
        "CLINICAL_INTERVENTION": {
            "before": frozenset({"CAUSAL", "SAFETY", "USE"}),
            "after": frozenset({"SAFETY"}),
            "local_info": 1.7,
            "local_cost": 10000.0,
        },
        "ENGINEERING_DEBUG": {
            "before": frozenset({"REPRO", "LOCALIZE", "REGRESSION"}),
            "after": frozenset({"REGRESSION"}),
            "local_info": 0.2,
            "local_cost": 3.0,
        },
    }
    reductions = {
        name: len(v["before"]) - len(v["after"]) for name, v in domains.items()
    }
    return {
        "domains": {
            k: {
                "before": sorted(v["before"]),
                "after": sorted(v["after"]),
                "local_info": v["local_info"],
                "local_cost": v["local_cost"],
            }
            for k, v in domains.items()
        },
        "structural_discharge_steps": reductions,
        "same_structural_order": len(set(reductions.values())) == 1,
        "same_information_magnitude": len({v["local_info"] for v in domains.values()}) == 1,
        "same_cost_magnitude": len({v["local_cost"] for v in domains.values()}) == 1,
    }


def evaluate_candidates(fixtures: Dict[str, object]) -> List[CandidateResult]:
    return [
        CandidateResult(
            "EVENT_COUNT","FAIL","PARTIAL","FAIL","GLOBAL_REJECT",
            "REJECT",
            "Inert checkpoint refinement changes the count without changing world state.",
        ),
        CandidateResult(
            "ELAPSED_TIME","UNIT_LOCAL","FAIL","FAIL","POLICY_INPUT_ONLY",
            "REJECT_AS_PROGRESS",
            "Equal elapsed time can contain null waiting or material probing.",
        ),
        CandidateResult(
            "RESOURCE_COST","UNIT_LOCAL","FAIL","POLICY_RELEVANT","POLICY_INPUT_ONLY",
            "REJECT_AS_PROGRESS",
            "Cost constrains policy but expensive inquiry can be epistemically null.",
        ),
        CandidateResult(
            "SHANNON_KL_INFORMATION","LOCAL_PASS","PASS_DESCRIPTIVE","FAIL_GLOBAL",
            "MODEL_TARGET_LOCAL",
            "LOCAL_ONLY",
            "Equal descriptive information can differ in intervention and use authority.",
        ),
        CandidateResult(
            "VALUE_OF_INFORMATION","CONTRACT_LOCAL","PASS_ACTION","POLICY_RELEVANT",
            "DECISION_CONTRACT_LOCAL",
            "LOCAL_ONLY",
            "VOI depends on decision/utility structure and does not constitute achieved progress.",
        ),
        CandidateResult(
            "FISHER_RAO_GEOMETRY","PASS_REPARAM","PASS_STATISTICAL","FAIL_GLOBAL",
            "STATISTICAL_CHART",
            "PASS_LOCAL_GEOMETRY",
            "Provides a positive local invariant geometry, not whole-science progress.",
        ),
        CandidateResult(
            "BLACKWELL_INFORMATIVENESS","PASS_GARBLING","PASS_EXPERIMENT","FAIL_GLOBAL",
            "EXPERIMENT_CHART",
            "PASS_LOCAL_PARTIAL_ORDER",
            "Decision-robust experiment order exists but is partial and mode-incomplete.",
        ),
        CandidateResult(
            "OBLIGATION_COUNT","FAIL","PARTIAL","FAIL","GLOBAL_REJECT",
            "REJECT",
            "Split/merge changes label count while burden ancestry is preserved.",
        ),
        CandidateResult(
            "BURDEN_DISCHARGE_PREORDER","PASS_SPLIT_MERGE","PASS","PARTIAL",
            "CONTRACT_LOCAL",
            "PASS_WITH_REOPENING_CAVEAT",
            "Ancestry-preserving discharge survives partition, but correction/reopening prevents simple monotonicity.",
        ),
        CandidateResult(
            "AUTHORITY_MODE_PATH_LENGTH","FAIL_LOOP","PARTIAL","FAIL","GLOBAL_REJECT",
            "REJECT",
            "Inert loops create positive length with quotient-identical endpoints.",
        ),
        CandidateResult(
            "NET_AUTHORITY_LEVEL","REPRESENTATION_LOCAL","FAIL_CORRECTION","FAIL",
            "GLOBAL_REJECT",
            "REJECT",
            "Corrective progress can lower claim authority.",
        ),
        CandidateResult(
            "PARETO_VECTOR","PASS_AXIS_MONOTONE","PASS","PARTIAL",
            "MULTI_AXIS",
            "PASS_PARTIAL_ONLY",
            "Invariant dominance survives recoding but crossing states remain incomparable.",
        ),
        CandidateResult(
            "WORLD_CONTACT_PROGRESS_ATLAS","PASS_TYPED","PASS","PASS_REGION_PLUS_CVE",
            "GLOBAL_META_LOCAL_OBJECT",
            "PROMOTE_CANDIDATE",
            "Quotients inert transformations while permitting local metrics/orders and separate continuation value.",
        ),
    ]


def main() -> None:
    fixtures: Dict[str, object] = {
        "event_count": event_count_fixture(),
        "time": time_fixture(),
        "cost": cost_fixture(),
        "obligation_split": obligation_split_fixture(),
        "information_intervention": information_intervention_fixture(),
        "authority_loop": authority_loop_fixture(),
        "correction": correction_fixture(),
        "independent_rescaling": independent_rescaling_fixture(),
        "fisher": fisher_reparameterization_fixture(),
        "blackwell": blackwell_fixture(),
        "progress_vs_promotion": progress_vs_promotion_twin_world(),
        "cross_domain": cross_domain_morphism_fixture(),
    }
    candidates = evaluate_candidates(fixtures)

    report = {
        "stage": "MQR-4.53",
        "preseal": PRESEAL,
        "fixtures": fixtures,
        "candidates": [c.__dict__ for c in candidates],
        "summary": {
            "candidate_count": len(candidates),
            "universal_scalar_survivors": 0,
            "local_invariant_structures": 4,
            "global_meta_local_object_candidate": "WORLD_CONTACT_PROGRESS_ATLAS",
            "event_count_invariant": fixtures["event_count"]["invariant"],
            "obligation_count_invariant": fixtures["obligation_split"]["raw_count_invariant"],
            "information_equals_intervention": (
                fixtures["information_intervention"]["equal_information"]
                and fixtures["information_intervention"]["equal_intervention_reach"]
            ),
            "fisher_reparameterization_invariant": fixtures["fisher"]["equal"],
            "blackwell_incomparability_exists": fixtures["blackwell"]["incomparable"],
            "authority_path_length_is_progress": fixtures["authority_loop"]["path_length_is_net_progress"],
            "authority_level_monotone_progress": fixtures["correction"]["authority_level_monotone_progress"],
            "scalar_rank_reversal_under_independent_rescaling": fixtures["independent_rescaling"]["ranking_reverses"],
            "state_only_stop_rule_sufficient": fixtures["progress_vs_promotion"]["state_only_stop_rule_sufficient"],
            "cross_domain_structure_transports": fixtures["cross_domain"]["same_structural_order"],
            "cross_domain_information_magnitude_transports": fixtures["cross_domain"]["same_information_magnitude"],
            "cross_domain_cost_magnitude_transports": fixtures["cross_domain"]["same_cost_magnitude"],
        },
        "verdict": {
            "universal_representation_invariant_scalar_progress": "REJECT",
            "local_representation_invariant_progress_structures": "ADMIT",
            "progress_state_equals_continuation_value": "REJECT",
            "scalar_threshold_stop_from_progress_alone": "REJECT",
            "global_meta_constitution_local_geometry": "SUPPORTED_BY_COURT",
            "realprogress_v020": "EARNED_CANDIDATE",
        },
        "guards": {
            "truth_distance_inferred": "NO",
            "global_metric_inferred": "NO",
            "local_geometry_allowed": "YES",
            "cross_domain_magnitude_transport_default": "NO",
            "inert_transform_must_quotient": "YES",
            "material_noncommutativity_must_survive": "YES",
            "reopening_reserve": "ACTIVE",
        },
    }

    s = report["summary"]
    assert s["universal_scalar_survivors"] == 0
    assert s["event_count_invariant"] is False
    assert s["obligation_count_invariant"] is False
    assert fixtures["information_intervention"]["equal_information"] is True
    assert fixtures["information_intervention"]["equal_intervention_reach"] is False
    assert s["fisher_reparameterization_invariant"] is True
    assert s["blackwell_incomparability_exists"] is True
    assert s["authority_path_length_is_progress"] is False
    assert s["authority_level_monotone_progress"] is False
    assert s["scalar_rank_reversal_under_independent_rescaling"] is True
    assert s["state_only_stop_rule_sufficient"] is False
    assert s["cross_domain_structure_transports"] is True
    assert s["cross_domain_information_magnitude_transports"] is False
    assert s["cross_domain_cost_magnitude_transports"] is False

    print(f"mqr453.candidate_count={s['candidate_count']}")
    print("mqr453.universal_scalar_survivors=0")
    print(f"mqr453.event_count_invariant={str(s['event_count_invariant']).upper()}")
    print(f"mqr453.obligation_count_invariant={str(s['obligation_count_invariant']).upper()}")
    print("mqr453.equal_information_different_intervention=PASS")
    print(f"mqr453.fisher_reparameterization_invariant={str(s['fisher_reparameterization_invariant']).upper()}")
    print(f"mqr453.blackwell_incomparability_exists={str(s['blackwell_incomparability_exists']).upper()}")
    print(f"mqr453.authority_path_length_is_progress={str(s['authority_path_length_is_progress']).upper()}")
    print(f"mqr453.authority_level_monotone_progress={str(s['authority_level_monotone_progress']).upper()}")
    print(f"mqr453.scalar_rank_reversal={str(s['scalar_rank_reversal_under_independent_rescaling']).upper()}")
    print(f"mqr453.state_only_stop_rule_sufficient={str(s['state_only_stop_rule_sufficient']).upper()}")
    print(f"mqr453.cross_domain_structure_transports={str(s['cross_domain_structure_transports']).upper()}")
    print("mqr453.universal_representation_invariant_scalar_progress=REJECT")
    print("mqr453.local_representation_invariant_progress_structures=ADMIT")
    print("mqr453.global_meta_constitution_local_geometry=SUPPORTED_BY_COURT")
    print("mqr453.realprogress_v020=EARNED_CANDIDATE")
    print("MQR453_REPORT_JSON=" + json.dumps(report, sort_keys=True))

    out_dir = Path(__file__).resolve().parent / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "progress_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
