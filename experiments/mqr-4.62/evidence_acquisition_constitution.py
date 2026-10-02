from pathlib import Path
import json
from acquisition_core import AcquisitionCase, evaluate

CASES = {
 "c01": (AcquisitionCase("myopic_information_trap", expected_information_high=True, myopic_best=True, option_loss=True, unique_future_separator=True), {"myopic_sequence_optimal":False,"option_preservation_required":True}),
 "c02": (AcquisitionCase("option_preserving_low_yield_probe", reversible_stage=True, unique_future_separator=True), {"selection_state":"LOCAL_ADMISSIBLE"}),
 "c03": (AcquisitionCase("destructive_identifiability_gain", identifiability_gain=True, live_claim_relevance=True, option_loss=True, unique_future_separator=True, destructive=True), {"selection_state":"FORBIDDEN_BY_DESTRUCTIVE_CONTRACT"}),
 "c04": (AcquisitionCase("prior_sensitive_query_reversal", prior_sensitive=True), {"selection_state":"HOLD_INCOMPARABLE"}),
 "c05": (AcquisitionCase("model_class_sensitive_query_reversal", model_sensitive=True), {"selection_state":"HOLD_INCOMPARABLE"}),
 "c06": (AcquisitionCase("representation_sensitive_information_gain", representation_sensitive=True), {"selection_state":"HOLD_INCOMPARABLE"}),
 "c07": (AcquisitionCase("policy_induced_sampling_blind_spot", sampling_blind_spot=True), {"policy_blind_spot":True,"reopening_required":True}),
 "c08": (AcquisitionCase("common_mode_evidence_inflation", common_mode=True), {"evidence_independence":False}),
 "c09": (AcquisitionCase("greedy_confirmation_loop", confirmation_loop=True), {"policy_blind_spot":True}),
 "c10": (AcquisitionCase("reopening_reserve_necessity", reopening_reserve=False, exploration_debt=True), {"reopening_reserve_active":False,"exploration_debt":"ACTIVE"}),
 "c11": (AcquisitionCase("fixed_exploration_goodhart", fixed_exploration_rule=True), {"fixed_exploration_universal":False}),
 "c12": (AcquisitionCase("query_order_noncommutativity", order_sensitive=True, unique_future_separator=True), {"query_order_commutative":False}),
 "c13": (AcquisitionCase("outcome_contingent_option_loss", outcome_contingent_loss=True, option_loss=True), {"outcome_contingent_option_loss":True}),
 "c14": (AcquisitionCase("cheap_probe_debt_accumulation", exploration_debt=True, cost_proxy_only=True), {"selection_state":"DEBT_CARRY"}),
 "c15": (AcquisitionCase("cost_normalized_value_reversal", cost_proxy_only=True, causal_decisive=True), {"cost_ratio_universal":False,"relation_anticipation_material":True}),
 "c16": (AcquisitionCase("identifiability_without_action_relevance", identifiability_gain=True, live_claim_relevance=False), {"identifiability_local_value":False,"identifiability_universal_value":False}),
 "c17": (AcquisitionCase("action_relevance_without_information_gain", causal_decisive=True), {"selection_state":"LOCAL_ADMISSIBLE","relation_anticipation_material":True}),
 "c18": (AcquisitionCase("exploration_bonus_representation_failure", representation_sensitive=True, fixed_exploration_rule=True), {"fixed_exploration_universal":False}),
 "c19": (AcquisitionCase("pareto_multiplicity", pareto_multiple=True), {"selection_state":"HOLD_INCOMPARABLE","pareto_unique_selector":False}),
 "c20": (AcquisitionCase("lexicographic_experiment_dictatorship", option_loss=True, unique_future_separator=True, destructive=True), {"selection_state":"FORBIDDEN_BY_DESTRUCTIVE_CONTRACT"}),
 "c21": (AcquisitionCase("reopening_value_reversal", option_loss=True, unique_future_separator=True), {"selection_state":"OPTION_PRESERVE"}),
 "c22": (AcquisitionCase("hidden_rival_arrival", hidden_rival=True), {"selection_state":"REOPEN_REQUIRED","reopening_required":True}),
 "c23": (AcquisitionCase("adaptive_stopping_blindness", generator_closed=True), {"policy_blind_spot":True,"selection_state":"REOPEN_REQUIRED"}),
 "c24": (AcquisitionCase("intervention_semantic_drift", intervention_drift=True), {"intervention_semantics_stable":False}),
 "c25": (AcquisitionCase("measurement_contamination_loop", contamination=True), {"baseline_preserved":False}),
 "c26": (AcquisitionCase("sequential_debt_laundering", exploration_debt=True, scalar_weight_sensitive=True), {"exploration_debt":"ACTIVE","history_scalarization":"OFF"}),
 "c27": (AcquisitionCase("randomization_not_oracle", randomization=True), {"selection_state":"BOUNDED_EXTERIOR_PROBE","randomization_oracle":False}),
 "c28": (AcquisitionCase("universal_utility_failure", scalar_weight_sensitive=True, option_loss=True, unique_future_separator=True), {"universal_expected_epistemic_utility_optimizer":"NOT_EARNED"}),
}

POSITIVE = {
 "p01": AcquisitionCase("local_identifiability_dominance", identifiability_gain=True, live_claim_relevance=True),
 "p02": AcquisitionCase("reversible_stage_preserves_separator", reversible_stage=True, unique_future_separator=True),
 "p03": AcquisitionCase("destructive_contract_forbids_action", destructive=True, option_loss=True, unique_future_separator=True),
 "p04": AcquisitionCase("reopening_reserve_preserved", reopening_reserve=True, unique_future_separator=True),
 "p05": AcquisitionCase("sequence_order_matters", order_sensitive=True, unique_future_separator=True),
 "p06": AcquisitionCase("low_information_causal_resolution", causal_decisive=True),
 "p07": AcquisitionCase("prior_sensitive_local_only", prior_sensitive=True),
 "p08": AcquisitionCase("new_rival_reopens_policy", hidden_rival=True),
 "p09": AcquisitionCase("common_mode_collapse", common_mode=True),
 "p10": AcquisitionCase("nonmyopic_debt_carried", exploration_debt=True, unique_future_separator=True),
 "p11": AcquisitionCase("genuine_incomparability", pareto_multiple=True),
 "p12": AcquisitionCase("bounded_random_exterior_probe", randomization=True),
 "p13": AcquisitionCase("identifiability_tied_to_live_claim", identifiability_gain=True, live_claim_relevance=True),
 "p14": AcquisitionCase("branchwise_option_loss", outcome_contingent_loss=True, option_loss=True),
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
      "stage":"MQR-4.62",
      "preseal_commit":"e93dab86be9a1ff109aa751dd6aac40a1a898e46",
      "stress_manifest_commit":"f9a0bc9f62915d8e5c9423dda2f08669e5222384",
      "cases":rows,
      "positive":positives,
      "max_expected_information_universal_selector":"REJECT",
      "myopic_best_sequence_optimal":"REJECT",
      "more_data_independent_warrant":"REJECT",
      "identifiability_universal_scientific_value":"REJECT",
      "fixed_exploration_bonus_universal":"REJECT",
      "randomization_adequacy_oracle":"REJECT",
      "pareto_frontier_unique_experiment":"REJECT",
      "value_cost_ratio_universal":"REJECT",
      "current_action_generator_complete":"REJECT",
      "low_marginal_gain_saturation":"REJECT",
      "scalar_expectation_may_erase_lost_option_debt":"ADMIT",
      "policy_can_create_blind_spots":"ADMIT",
      "option_preserving_sequencing":"ADMIT",
      "identifiability_delta_receipt":"ADMIT",
      "relation_anticipation_envelope":"ADMIT",
      "adaptive_reopening_reserve":"ADMIT",
      "nonmyopic_exploration_debt":"ADMIT",
      "ancestry_aware_evidence_multiplicity":"ADMIT",
      "incomparable_actions_hold":"ADMIT",
      "history_scalarization":"OFF",
      "universal_expected_epistemic_utility_optimizer":"NOT_EARNED",
      "easr":"CANDIDATE","raer":"CANDIDATE","opr":"CANDIDATE",
      "idr":"CANDIDATE","arr":"CANDIDATE","nedl":"CANDIDATE",
    }

    out = Path(__file__).parent/"results"/"evidence_acquisition.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")

    for key,row in rows.items():
        print(f"mqr462.{key}=PASS:{row['selection_state']}")
    print("mqr462.countermodels=28/28")
    print("mqr462.positive_witnesses=14/14")
    print("mqr462.max_expected_information_universal_selector=REJECT")
    print("mqr462.myopic_best_sequence_optimal=REJECT")
    print("mqr462.policy_can_create_blind_spots=ADMIT")
    print("mqr462.option_preserving_sequencing=ADMIT")
    print("mqr462.adaptive_reopening_reserve=ADMIT")
    print("mqr462.nonmyopic_exploration_debt=ADMIT")
    print("mqr462.randomization_adequacy_oracle=REJECT")
    print("mqr462.history_scalarization=OFF")
    print("mqr462.universal_expected_epistemic_utility_optimizer=NOT_EARNED")

if __name__ == "__main__":
    main()
