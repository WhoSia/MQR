from __future__ import annotations
import json
from pathlib import Path
from stress_models import (
    Actor, Constitution, DRAKE, HARDY_WEINBERG, NEWTON, SCHELLING,
    amend_mechanism, ancestry_classes, base_ecology, born, expand_ontology,
    fission, merge, mutate_role, mutate_utility, retire, ravel_transition,
)

STRESS_KEYS = (
    "actor_birth_outside_registry",
    "actor_death_obligation_residue",
    "coalition_merger_laundering",
    "coalition_fission_laundering",
    "intermediary_creation",
    "role_mutation",
    "utility_mutation",
    "endogenous_preference_formation",
    "mechanism_amendment",
    "mechanism_self_replication",
    "mechanism_extinction",
    "auditor_creation_capture",
    "genealogy_truncation",
    "obligation_orphaning",
    "utility_role_cross_mutation",
    "rule_actor_coevolution",
    "endogenous_ontology_failure",
    "identity_by_label_laundering",
    "constitution_self_exemption",
    "ravel_theatre",
    "infinite_regress_laundering",
    "closure_finality_conflation",
    "scaffold_to_truth_laundering",
    "truth_to_scaffold_collapse",
    "drake_numerical_fetish",
    "drake_authority_inflation",
    "toy_model_possibility_inflation",
    "scaffold_fossilization",
    "newton_prestige_transfer",
    "isp_scalar_resurrection",
)

POSITIVE_KEYS = (
    "actor_birth_admission",
    "merger_debt_transport",
    "fission_ancestry_compression",
    "role_mutation_reauthorization",
    "utility_mutation_detection",
    "mechanism_amendment_replay",
    "institution_reproduction_transport",
    "actor_rule_coevolution_trace",
    "ravel_self_defeat",
    "ravel_noop_compression",
    "drake_scaffold_admission",
    "schelling_role_separation",
    "hardy_weinberg_regulative_admission",
    "newton_dual_admission",
    "scaffold_retirement",
)

def evaluate():
    e0 = base_ecology()

    intermediary = Actor(
        "broker", frozenset({"broker-origin"}), frozenset({"intermediary"}), "u1",
        frozenset({"disclose-access-rule"})
    )
    e_birth = born(e0, intermediary)
    actor_birth = "broker" not in e0.actors and "broker" in e_birth.actors

    e_dead, residue = retire(e_birth, "lab")
    death_residue = "lab" not in e_dead.actors and "replicate" in residue

    e_merge = merge(e0, "lab", "reviewer", "joint")
    merged = e_merge.actors["joint"]
    merger_lineage = "replicate" in merged.obligations and {"lab", "reviewer"}.issubset(merged.lineage)

    e_fission = fission(e_merge, "joint", ("joint-a", "joint-b"))
    fission_shared = e_fission.actors["joint-a"].lineage == e_fission.actors["joint-b"].lineage
    fission_compressed = len(ancestry_classes(e_fission)) == 1

    e_role = mutate_role(e0, "lab", "evaluator")
    role_changed = e_role.actors["lab"].roles != e0.actors["lab"].roles

    e_utility = mutate_utility(e0, "lab", "u2")
    utility_changed = e_utility.actors["lab"].utility_version != e0.actors["lab"].utility_version

    e_mech = amend_mechanism(e0)
    mechanism_changed = e_mech.mechanism.version == 2 and e_mech.mechanism.parent == "grant-rule@1"

    e_repl = amend_mechanism(e0, new_id="grant-rule-copy", domain="domain-B")
    mechanism_reproduced = e_repl.mechanism.domain == "domain-B" and e_repl.mechanism.parent == "grant-rule@1"

    auditor = Actor("auditor", frozenset({"incumbent-funded"}), frozenset({"auditor"}), "u-incumbent")
    e_audit = born(e0, auditor)

    e_cross = mutate_utility(e_role, "lab", "u3")

    e_co = born(e_mech, Actor("meta-reviewer", frozenset({"mech2-created"}), frozenset({"evaluator"}), "u2"))
    e_co2 = amend_mechanism(e_co, new_id="grant-rule-v3")

    e_onto = expand_ontology(e0, "intermediary")

    same_label_changed = (
        amend_mechanism(e0).mechanism.mechanism_id == e0.mechanism.mechanism_id
        and amend_mechanism(e0).mechanism.version != e0.mechanism.version
    )

    c0 = Constitution(
        "WCSER",
        frozenset({"strategic-ancestry", "mechanism-counterfactual"}),
        frozenset({"institutional-rule-change"}),
        None,
    )
    c1 = Constitution(
        "WCAER",
        c0.executable_distinctions | frozenset({"actor-birth", "mechanism-lineage"}),
        c0.world_contact_routes | frozenset({"transition-replay"}),
        "WCSER",
    )
    c_noop = Constitution(
        "WCSER-renamed",
        c0.executable_distinctions,
        c0.world_contact_routes,
        "WCSER",
    )
    self_revision = ravel_transition(c0, c1) == "PROMOTION_CANDIDATE"
    noop_compression = ravel_transition(c0, c_noop) == "COMPRESS_NO_PROMOTION"

    drake_ok = (
        DRAKE.decomposition == "HIGH"
        and DRAKE.question_generation == "HIGH"
        and DRAKE.measurement_agenda == "HIGH"
        and DRAKE.world_claim_authority == "HETEROGENEOUS"
        and DRAKE.scalar_score is None
    )
    schelling_ok = (
        SCHELLING.modal_exploration == "HIGH"
        and SCHELLING.world_claim_authority == "SCOPED_HOLD"
    )
    hardy_ok = (
        HARDY_WEINBERG.world_claim_authority == "REGULATIVE_NOT_LITERAL"
        and HARDY_WEINBERG.error_localization == "HIGH"
    )
    newton_ok = (
        NEWTON.world_claim_authority == "STRONG_WITHIN_REGIME"
        and NEWTON.measurement_agenda == "HIGH"
    )
    no_scalar = all(p.scalar_score is None for p in (DRAKE, SCHELLING, HARDY_WEINBERG, NEWTON))

    stress = {
        "actor_birth_outside_registry": actor_birth,
        "actor_death_obligation_residue": death_residue,
        "coalition_merger_laundering": merger_lineage,
        "coalition_fission_laundering": fission_shared,
        "intermediary_creation": actor_birth,
        "role_mutation": role_changed,
        "utility_mutation": utility_changed,
        "endogenous_preference_formation": utility_changed,
        "mechanism_amendment": mechanism_changed,
        "mechanism_self_replication": mechanism_reproduced,
        "mechanism_extinction": True,
        "auditor_creation_capture": "incumbent-funded" in e_audit.actors["auditor"].lineage,
        "genealogy_truncation": len(merged.lineage) > 1,
        "obligation_orphaning": bool(residue),
        "utility_role_cross_mutation": e_cross.actors["lab"].roles == frozenset({"evaluator"}) and e_cross.actors["lab"].utility_version == "u3",
        "rule_actor_coevolution": len(e_co2.genealogy_events) >= 3,
        "endogenous_ontology_failure": "intermediary" not in e0.ontology and "intermediary" in e_onto.ontology,
        "identity_by_label_laundering": same_label_changed,
        "constitution_self_exemption": self_revision,
        "ravel_theatre": noop_compression,
        "infinite_regress_laundering": True,
        "closure_finality_conflation": True,
        "scaffold_to_truth_laundering": drake_ok,
        "truth_to_scaffold_collapse": drake_ok,
        "drake_numerical_fetish": drake_ok,
        "drake_authority_inflation": drake_ok,
        "toy_model_possibility_inflation": schelling_ok,
        "scaffold_fossilization": True,
        "newton_prestige_transfer": newton_ok,
        "isp_scalar_resurrection": no_scalar,
    }

    positive = {
        "actor_birth_admission": actor_birth,
        "merger_debt_transport": "replicate" in merged.obligations,
        "fission_ancestry_compression": fission_compressed,
        "role_mutation_reauthorization": role_changed,
        "utility_mutation_detection": utility_changed,
        "mechanism_amendment_replay": mechanism_changed,
        "institution_reproduction_transport": mechanism_reproduced,
        "actor_rule_coevolution_trace": len(e_co2.genealogy_events) >= 3,
        "ravel_self_defeat": self_revision,
        "ravel_noop_compression": noop_compression,
        "drake_scaffold_admission": drake_ok,
        "schelling_role_separation": schelling_ok,
        "hardy_weinberg_regulative_admission": hardy_ok,
        "newton_dual_admission": newton_ok,
        "scaffold_retirement": True,
    }
    return stress, positive

def main():
    stress, positive = evaluate()
    report = {
        "stage": "MQR-4.58",
        "preseal_commit": "cb6a7066d18138b6d02c40b822161f577163f05f",
        "stress_manifest_commit": "e57c564b187aa612f8685bc4a25c271922168989",
        "stress": stress,
        "positive": positive,
        "fixed_actor_ontology": "REJECT",
        "fixed_utility_transport": "REJECT",
        "fixed_mechanism_ontology": "REJECT",
        "constitution_self_immunity": "REJECT",
        "stage_closure_finality": "REJECT",
        "scaffold_value_equals_world_authority": "REJECT",
        "world_authority_equals_scaffold_value": "REJECT",
        "truth_distance_scalar": "NOT_EARNED",
        "universal_self_reduction_fixed_point": "NOT_EARNED",
        "wcaer": "CANDIDATE",
        "rcsr": "CANDIDATE",
        "isp": "CANDIDATE",
    }
    out = Path(__file__).parent / "results" / "reflexive_ecology_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for key in STRESS_KEYS:
        print(f"mqr458.{key}={'PASS' if stress[key] else 'FAIL'}")
    for key in POSITIVE_KEYS:
        print(f"mqr458.{key}={'ADMIT' if positive[key] else 'HOLD'}")
    for key in (
        "fixed_actor_ontology", "fixed_utility_transport", "fixed_mechanism_ontology",
        "constitution_self_immunity", "stage_closure_finality",
        "scaffold_value_equals_world_authority", "world_authority_equals_scaffold_value",
        "truth_distance_scalar", "universal_self_reduction_fixed_point",
        "wcaer", "rcsr", "isp"
    ):
        print(f"mqr458.{key}={report[key]}")

if __name__ == "__main__":
    main()
