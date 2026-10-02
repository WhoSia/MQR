from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class AcquisitionCase:
    name: str
    expected_information_high: bool = False
    myopic_best: bool = False
    option_loss: bool = False
    unique_future_separator: bool = False
    identifiability_gain: bool = False
    live_claim_relevance: bool = False
    prior_sensitive: bool = False
    model_sensitive: bool = False
    representation_sensitive: bool = False
    sampling_blind_spot: bool = False
    common_mode: bool = False
    confirmation_loop: bool = False
    reopening_reserve: bool = True
    fixed_exploration_rule: bool = False
    order_sensitive: bool = False
    outcome_contingent_loss: bool = False
    exploration_debt: bool = False
    cost_proxy_only: bool = False
    causal_decisive: bool = False
    randomization: bool = False
    hidden_rival: bool = False
    generator_closed: bool = False
    intervention_drift: bool = False
    contamination: bool = False
    pareto_multiple: bool = False
    scalar_weight_sensitive: bool = False
    destructive: bool = False
    reversible_stage: bool = False

def option_preservation_required(c):
    return c.option_loss and c.unique_future_separator

def policy_blind_spot(c):
    return c.sampling_blind_spot or c.confirmation_loop or c.generator_closed

def relation_anticipation_material(c):
    return any((
        c.unique_future_separator,
        c.causal_decisive,
        c.hidden_rival,
        c.identifiability_gain and c.live_claim_relevance,
    ))

def selection_state(c):
    if c.destructive and option_preservation_required(c):
        return "FORBIDDEN_BY_DESTRUCTIVE_CONTRACT"
    if option_preservation_required(c):
        return "OPTION_PRESERVE"
    if c.hidden_rival or c.generator_closed:
        return "REOPEN_REQUIRED"
    if c.exploration_debt:
        return "DEBT_CARRY"
    if c.prior_sensitive or c.model_sensitive or c.representation_sensitive or c.pareto_multiple:
        return "HOLD_INCOMPARABLE"
    if c.randomization:
        return "BOUNDED_EXTERIOR_PROBE"
    if c.identifiability_gain and c.live_claim_relevance:
        return "LOCAL_ADMISSIBLE"
    if c.causal_decisive:
        return "LOCAL_ADMISSIBLE"
    return "LOCAL_ADMISSIBLE"

def evaluate(c):
    opt_req = option_preservation_required(c)
    blind = policy_blind_spot(c)
    local_id = c.identifiability_gain and c.live_claim_relevance
    return {
        "case": asdict(c),
        "selection_state": selection_state(c),
        "expected_information_universal_selector": False,
        "myopic_sequence_optimal": not (c.myopic_best and opt_req),
        "option_preservation_required": opt_req,
        "identifiability_local_value": local_id,
        "identifiability_universal_value": False,
        "query_order_commutative": not c.order_sensitive,
        "policy_blind_spot": blind,
        "evidence_independence": not c.common_mode,
        "reopening_reserve_active": c.reopening_reserve,
        "reopening_required": c.hidden_rival or c.generator_closed or blind,
        "exploration_debt": "ACTIVE" if c.exploration_debt else "INACTIVE",
        "outcome_contingent_option_loss": c.outcome_contingent_loss,
        "randomization_oracle": False,
        "fixed_exploration_universal": False,
        "pareto_unique_selector": False if c.pareto_multiple else None,
        "cost_ratio_universal": False,
        "relation_anticipation_material": relation_anticipation_material(c),
        "intervention_semantics_stable": not c.intervention_drift,
        "baseline_preserved": not c.contamination,
        "history_scalarization": "OFF",
        "universal_expected_epistemic_utility_optimizer": "NOT_EARNED",
        "easr": "CANDIDATE",
        "raer": "CANDIDATE",
        "opr": "CANDIDATE",
        "idr": "CANDIDATE",
        "arr": "CANDIDATE",
        "nedl": "CANDIDATE",
    }
