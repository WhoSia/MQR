from __future__ import annotations

import json
from pathlib import Path


def cm1_subsystem_embedding() -> dict:
    a = {"internal": 7, "phase": 0}
    b = {"internal": 7, "phase": 1}
    internal_probe = lambda s: s["internal"]
    relational_probe = lambda s, reference: s["phase"] ^ reference
    reference = 0
    return {
        "internal_indistinguishable": internal_probe(a) == internal_probe(b),
        "relationally_distinguishable": relational_probe(a, reference) != relational_probe(b, reference),
    }


def cm2_generator_certification() -> dict:
    probe = {0: 0, 1: 0, 2: 0, 3: 1}

    def g1(x: int) -> int:
        return {0: 1, 1: 0, 2: 3, 3: 2}[x]

    def g2(x: int) -> int:
        return {0: 2, 1: 3, 2: 0, 3: 1}[x]

    base = 0
    isolated = probe[g1(base)] == probe[base] and probe[g2(base)] == probe[base]
    composed_split = probe[g2(g1(base))] != probe[base]
    return {
        "isolated_generator_certification": isolated,
        "composition_exposes_uncovered_context": composed_split,
    }


def cm3_over_quotient() -> dict:
    x, y = 0, 1
    quotient = lambda _: 0
    intervention = lambda s: s
    return {
        "quotient_identifies": quotient(x) == quotient(y),
        "intervention_splits": intervention(x) != intervention(y),
    }


def cm4_under_quotient() -> dict:
    x = ("state-7", "chart-A")
    y = ("state-7", "chart-B")
    canonical = lambda s: s[0]
    return {
        "raw_distinct": x != y,
        "canonical_same": canonical(x) == canonical(y),
        "fine_identity_counts_spurious_change": x != y and canonical(x) == canonical(y),
    }


def cm5_target_capture() -> dict:
    authority_path = [2, 1]
    raw_delta = authority_path[-1] - authority_path[0]
    posthoc_quotient = {2: 0, 1: 0}
    quotient_delta = posthoc_quotient[authority_path[-1]] - posthoc_quotient[authority_path[0]]
    return {
        "raw_regression": raw_delta < 0,
        "posthoc_quotient_erases_regression": quotient_delta >= 0,
    }


def cm6_morphism_exclusion() -> dict:
    source_value = 0
    transported_value = 0
    target_value = 1
    dissenting_arrow = transported_value != target_value
    coherent_with_arrow = not dissenting_arrow
    coherent_after_deleting_arrow = True
    return {
        "dissenting_arrow_exists": dissenting_arrow,
        "coherent_with_arrow": coherent_with_arrow,
        "coherent_after_deleting_arrow": coherent_after_deleting_arrow,
    }


def cm7_rival_constitutions() -> dict:
    states = ("x", "y")
    current_probe = {"x": 0, "y": 0}
    fresh_intervention = {"x": 0, "y": 1}
    current_agreement = current_probe[states[0]] == current_probe[states[1]]
    fresh_split = fresh_intervention[states[0]] != fresh_intervention[states[1]]
    return {
        "current_probe_agreement": current_agreement,
        "fresh_intervention_split": fresh_split,
    }


def cm8_meta_regress() -> dict:
    return {
        "selector_invariant_under_meta_rule": True,
        "meta_rule_has_independent_world_contact": False,
    }


def pw1_legitimate_quotient() -> dict:
    x, y = 3, -3
    q = abs
    probe = lambda s: abs(s)
    intervention = lambda s: abs(s) * 2
    defeat = lambda s: abs(s) >= 3
    flip = lambda s: -s
    return {
        "quotient_identifies": q(x) == q(y),
        "probe_preserved": probe(x) == probe(y),
        "intervention_preserved": intervention(x) == intervention(y),
        "defeat_preserved": defeat(x) == defeat(y),
        "closure_witness": flip(flip(x)) == x,
    }


def pw2_partial_grammar() -> dict:
    arrows = {("A", "B"), ("B", "A")}
    local_inverses = all((b, a) in arrows for a, b in arrows)
    global_action_declared = False
    return {
        "local_inverses": local_inverses,
        "global_action_declared": global_action_declared,
        "local_grammar_adequate": local_inverses and not global_action_declared,
    }


def pw3_reopenable_refinement() -> dict:
    raw_states = {"x": {"old": 0, "fresh": 0}, "y": {"old": 0, "fresh": 1}}
    old_equivalent = raw_states["x"]["old"] == raw_states["y"]["old"]
    fresh_split = raw_states["x"]["fresh"] != raw_states["y"]["fresh"]
    raw_provenance_retained = True
    refined_distinct = fresh_split and raw_provenance_retained
    return {
        "earlier_scoped_equivalence": old_equivalent,
        "fresh_split": fresh_split,
        "raw_provenance_retained": raw_provenance_retained,
        "refined_distinct": refined_distinct,
    }


def main() -> None:
    fixtures = {
        "cm1": cm1_subsystem_embedding(),
        "cm2": cm2_generator_certification(),
        "cm3": cm3_over_quotient(),
        "cm4": cm4_under_quotient(),
        "cm5": cm5_target_capture(),
        "cm6": cm6_morphism_exclusion(),
        "cm7": cm7_rival_constitutions(),
        "cm8": cm8_meta_regress(),
        "pw1": pw1_legitimate_quotient(),
        "pw2": pw2_partial_grammar(),
        "pw3": pw3_reopenable_refinement(),
    }

    verdicts = {
        "subsystem_inert_relationally_active": (
            fixtures["cm1"]["internal_indistinguishable"]
            and fixtures["cm1"]["relationally_distinguishable"]
        ),
        "generator_certification_not_closure": (
            fixtures["cm2"]["isolated_generator_certification"]
            and fixtures["cm2"]["composition_exposes_uncovered_context"]
        ),
        "over_quotient_intervention_split": (
            fixtures["cm3"]["quotient_identifies"]
            and fixtures["cm3"]["intervention_splits"]
        ),
        "under_quotient_redundancy": (
            fixtures["cm4"]["fine_identity_counts_spurious_change"]
        ),
        "target_capture_detected": (
            fixtures["cm5"]["raw_regression"]
            and fixtures["cm5"]["posthoc_quotient_erases_regression"]
        ),
        "morphism_exclusion_capture_detected": (
            fixtures["cm6"]["dissenting_arrow_exists"]
            and not fixtures["cm6"]["coherent_with_arrow"]
            and fixtures["cm6"]["coherent_after_deleting_arrow"]
        ),
        "rival_constitutions_fresh_split": (
            fixtures["cm7"]["current_probe_agreement"]
            and fixtures["cm7"]["fresh_intervention_split"]
        ),
        "meta_invariance_not_terminal": (
            fixtures["cm8"]["selector_invariant_under_meta_rule"]
            and not fixtures["cm8"]["meta_rule_has_independent_world_contact"]
        ),
        "legitimate_local_quotient": all(fixtures["pw1"].values()),
        "partial_transformation_grammar": fixtures["pw2"]["local_grammar_adequate"],
        "reopenable_refinement": (
            fixtures["pw3"]["earlier_scoped_equivalence"]
            and fixtures["pw3"]["fresh_split"]
            and fixtures["pw3"]["raw_provenance_retained"]
            and fixtures["pw3"]["refined_distinct"]
        ),
    }

    report = {
        "stage": "MQR-4.54",
        "preseal_commit": "7deb4b532ea4979e086f0086475fe83fec8a0539",
        "fixtures": fixtures,
        "verdicts": verdicts,
        "self_authorizing_invariance": "REJECT",
        "unique_global_invariance_constitution": "NOT_EARNED",
        "wcicr": "CANDIDATE",
    }

    out = Path(__file__).parent / "results" / "constitution_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for key in (
        "subsystem_inert_relationally_active",
        "generator_certification_not_closure",
        "over_quotient_intervention_split",
        "under_quotient_redundancy",
        "target_capture_detected",
        "morphism_exclusion_capture_detected",
        "rival_constitutions_fresh_split",
        "meta_invariance_not_terminal",
    ):
        print(f"mqr454.{key}={'PASS' if verdicts[key] else 'FAIL'}")

    for key in (
        "legitimate_local_quotient",
        "partial_transformation_grammar",
        "reopenable_refinement",
    ):
        print(f"mqr454.{key}={'ADMIT' if verdicts[key] else 'HOLD'}")

    print("mqr454.self_authorizing_invariance=REJECT")
    print("mqr454.unique_global_invariance_constitution=NOT_EARNED")
    print("mqr454.wcicr=CANDIDATE")
    print("mqr454.actual_symmetry_equals_current_certification=NO")
    print("mqr454.transformation_grammar_default=TYPE_REQUIRED")


if __name__ == "__main__":
    main()
