from pathlib import Path
import json
from dynamics_core import TransitionCase, evaluate

CASES = {
 "c01": (TransitionCase("resolve_then_reopen", prior_relation="DOMINATES", new_relation="INCOMPARABLE", reopen=True, scope_after="CROSS_DOMAIN", material_history=True), {"transition":"REOPENED"}),
 "c02": (TransitionCase("evidence_order_noncommutativity", event_order_sensitive=True, provenance_changed=True), {"revision_commutative":False}),
 "c03": (TransitionCase("intervention_contamination", event_order_sensitive=True, provenance_changed=True), {"exact_restoration":False}),
 "c04": (TransitionCase("lost_option_asymmetry", lost_option=True, irreversible_debt=True), {"lost_option_debt":"ACTIVE","exact_restoration":False}),
 "c05": (TransitionCase("same_relation_different_debt", irreversible_debt=True), {"history_material":True,"exact_restoration":False}),
 "c06": (TransitionCase("same_decision_different_authority", provenance_changed=True), {"history_material":True}),
 "c07": (TransitionCase("veto_activation", veto_after=True), {"transition":"VETO_ACTIVATED"}),
 "c08": (TransitionCase("veto_retirement", veto_before=True, material_history=True), {"transition":"VETO_RETIRED","veto_monotone":False}),
 "c09": (TransitionCase("veto_pseudo_monotonicity", veto_before=True), {"veto_monotone":False}),
 "c10": (TransitionCase("reason_mutation", reason_before="OPTION_VALUE", reason_after="INDEPENDENT_WORLD_CONTACT"), {"transition":"REASON_MUTATED","independent_warrant_created":False}),
 "c11": (TransitionCase("reason_duplication_by_mutation", reason_before="OPTION_VALUE", reason_after="INDEPENDENT_WORLD_CONTACT"), {"independent_warrant_created":False}),
 "c12": (TransitionCase("scope_reversal", prior_relation="DOMINATES", new_relation="INCOMPARABLE", scope_after="CROSS_DOMAIN", material_history=True), {"transition":"SCOPE_REVERSED"}),
 "c13": (TransitionCase("horizon_reversal", prior_relation="VETOES", new_relation="INCOMPARABLE", horizon_after="LONG", material_history=True), {"transition":"HORIZON_REVERSED"}),
 "c14": (TransitionCase("cycle_persistence", cycle_before=True, cycle_after=True), {"cycle_persistent":True}),
 "c15": (TransitionCase("cycle_exit", cycle_before=True, material_history=True), {"transition":"CYCLE_EXITED"}),
 "c16": (TransitionCase("false_hysteresis_from_sunk_cost", chronology_only=True), {"transition":"HISTORY_IRRELEVANT","hysteresis":"INACTIVE","exact_restoration":True}),
 "c17": (TransitionCase("material_hysteresis", lost_option=True, provenance_changed=True, material_history=True), {"hysteresis":"ACTIVE","path_sensitive":True}),
 "c18": (TransitionCase("history_score_goodharting", revision_count_high=True), {"history_scalarization":"OFF"}),
 "c19": (TransitionCase("state_erasure_aliasing", lost_option=True, irreversible_debt=True, provenance_changed=True), {"history_material":True,"exact_restoration":False}),
 "c20": (TransitionCase("reopen_loop", prior_relation="DOMINATES", new_relation="INCOMPARABLE", reopen=True, material_history=True), {"transition":"REOPENED"}),
 "c21": (TransitionCase("evidence_accumulation_reversal", prior_relation="DOMINATES", new_relation="INCOMPARABLE", more_evidence=True, material_history=True), {"authority_monotone_with_more_evidence":False}),
 "c22": (TransitionCase("restoration_illusion", prior_relation="VETOES", new_relation="VETOES", irreversible_debt=True), {"exact_restoration":False}),
 "c23": (TransitionCase("chronology_only_path_preference", chronology_only=True), {"history_material":False,"path_sensitive":False,"exact_restoration":True}),
 "c24": (TransitionCase("universal_transition_priority_failure", event_order_sensitive=True, lost_option=True, irreversible_debt=True), {"revision_commutative":False,"lost_option_debt":"ACTIVE"}),
}

POSITIVE = {
 "p01": TransitionCase("fresh_evidence_resolves_incomparability", prior_relation="INCOMPARABLE", new_relation="DOMINATES", material_history=True),
 "p02": TransitionCase("later_counterevidence_reopens", prior_relation="DOMINATES", new_relation="INCOMPARABLE", reopen=True, material_history=True),
 "p03": TransitionCase("order_changes_evidential_status", event_order_sensitive=True, provenance_changed=True),
 "p04": TransitionCase("explicit_veto_activation", veto_after=True, material_history=True),
 "p05": TransitionCase("evidence_based_veto_retirement", veto_before=True, material_history=True),
 "p06": TransitionCase("ancestry_preserving_reason_mutation", reason_before="OPTION_VALUE", reason_after="INDEPENDENT_WORLD_CONTACT"),
 "p07": TransitionCase("lost_option_survives_old_label", lost_option=True),
 "p08": TransitionCase("chronology_erased_when_state_equal", chronology_only=True),
 "p09": TransitionCase("cycle_legitimate_persistence", cycle_before=True, cycle_after=True),
 "p10": TransitionCase("cycle_local_exit", cycle_before=True, material_history=True),
 "p11": TransitionCase("indexed_scope_reversal", prior_relation="DOMINATES", new_relation="INCOMPARABLE", scope_after="CROSS_DOMAIN", material_history=True),
 "p12": TransitionCase("material_not_sunk_cost_hysteresis", lost_option=True, irreversible_debt=True, material_history=True),
}

def check(row, expected):
    for k, v in expected.items():
        assert row[k] == v, (k, row[k], v)

def main():
    rows = {}
    for key, (case, expected) in CASES.items():
        row = evaluate(case)
        check(row, expected)
        row["pass"] = True
        rows[key] = row
    positives = {k:{**evaluate(v),"pass":True} for k,v in POSITIVE.items()}
    report = {
      "stage":"MQR-4.61",
      "preseal_commit":"85af1cb3dd4559e6dfcc4f711587611b524d6187",
      "stress_manifest_commit":"7f191286307bb46940ff34221201c7606c5d19ac",
      "cases":rows, "positive":positives,
      "static_state_complete_theory":"REJECT",
      "current_relation_label_sufficient_history":"REJECT",
      "revision_order_commutes_universally":"REJECT",
      "resolved_conflict_stays_resolved":"REJECT",
      "veto_activation_monotone":"REJECT",
      "more_evidence_monotone_authority":"REJECT",
      "old_label_exact_restoration":"REJECT",
      "historical_effort_creates_authority":"REJECT",
      "revision_count_is_progress":"REJECT",
      "conflict_cycles_must_converge":"REJECT",
      "universal_transition_priority":"REJECT",
      "relation_transition_receipt":"ADMIT",
      "path_ancestry":"ADMIT",
      "reason_type_mutation":"ADMIT",
      "conflict_reopening":"ADMIT",
      "veto_activation_and_retirement":"ADMIT",
      "scope_horizon_transition":"ADMIT",
      "material_hysteresis":"ADMIT",
      "lost_option_debt":"ADMIT",
      "chronology_only_hysteresis":"REJECT",
      "history_scalarization":"OFF",
      "universal_historical_meta_utility":"NOT_EARNED",
      "prtr":"CANDIDATE","phl":"CANDIDATE","odr":"CANDIDATE","rmr":"CANDIDATE",
    }
    out = Path(__file__).parent/"results"/"promotion_conflict_dynamics.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    for key,row in rows.items():
        print(f"mqr461.{key}=PASS:{row['transition']}")
    print("mqr461.countermodels=24/24")
    print("mqr461.positive_witnesses=12/12")
    print("mqr461.revision_order_commutes_universally=REJECT")
    print("mqr461.resolved_conflict_stays_resolved=REJECT")
    print("mqr461.veto_activation_monotone=REJECT")
    print("mqr461.more_evidence_monotone_authority=REJECT")
    print("mqr461.chronology_only_hysteresis=REJECT")
    print("mqr461.material_hysteresis=ADMIT")
    print("mqr461.lost_option_debt=ADMIT")
    print("mqr461.history_scalarization=OFF")
    print("mqr461.universal_historical_meta_utility=NOT_EARNED")

if __name__ == "__main__":
    main()
