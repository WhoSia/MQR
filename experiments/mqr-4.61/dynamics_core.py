from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class TransitionCase:
    name: str
    prior_relation: str = "INCOMPARABLE"
    new_relation: str = "INCOMPARABLE"
    scope_before: str = "LOCAL"
    scope_after: str = "LOCAL"
    horizon_before: str = "MEDIUM"
    horizon_after: str = "MEDIUM"
    reason_before: str = "INDEPENDENT_WORLD_CONTACT"
    reason_after: str = "INDEPENDENT_WORLD_CONTACT"
    same_ancestry: bool = True
    veto_before: bool = False
    veto_after: bool = False
    reopen: bool = False
    cycle_before: bool = False
    cycle_after: bool = False
    material_history: bool = False
    lost_option: bool = False
    irreversible_debt: bool = False
    provenance_changed: bool = False
    chronology_only: bool = False
    event_order_sensitive: bool = False
    more_evidence: bool = False
    revision_count_high: bool = False

def history_material(c):
    return any((c.material_history, c.lost_option, c.irreversible_debt, c.provenance_changed))

def classify_transition(c):
    if c.chronology_only and not history_material(c):
        return "HISTORY_IRRELEVANT"
    if c.reason_before != c.reason_after:
        return "REASON_MUTATED"
    if not c.veto_before and c.veto_after:
        return "VETO_ACTIVATED"
    if c.veto_before and not c.veto_after:
        return "VETO_RETIRED"
    if c.reopen:
        return "REOPENED"
    if c.scope_before != c.scope_after:
        return "SCOPE_REVERSED"
    if c.horizon_before != c.horizon_after:
        return "HORIZON_REVERSED"
    if not c.cycle_before and c.cycle_after:
        return "CYCLE_ENTERED"
    if c.cycle_before and not c.cycle_after:
        return "CYCLE_EXITED"
    if c.prior_relation == "INCOMPARABLE" and c.new_relation == "DOMINATES":
        return "INCOMPARABLE_TO_DOMINATES"
    if c.prior_relation == "DOMINATES" and c.new_relation == "INCOMPARABLE":
        return "DOMINATES_TO_INCOMPARABLE"
    if c.prior_relation != c.new_relation:
        return "RELATION_REVISED"
    return "STABLE"

def exact_restoration(c):
    return (
        c.prior_relation == c.new_relation
        and c.scope_before == c.scope_after
        and c.horizon_before == c.horizon_after
        and c.reason_before == c.reason_after
        and c.veto_before == c.veto_after
        and c.cycle_before == c.cycle_after
        and not c.lost_option
        and not c.irreversible_debt
        and not c.provenance_changed
    )

def evaluate(c):
    material = history_material(c)
    mutated = c.reason_before != c.reason_after
    return {
        "case": asdict(c),
        "transition": classify_transition(c),
        "history_material": material,
        "path_sensitive": material or c.event_order_sensitive,
        "revision_commutative": not c.event_order_sensitive,
        "hysteresis": "ACTIVE" if (c.lost_option or c.irreversible_debt or c.provenance_changed) else "INACTIVE",
        "lost_option_debt": "ACTIVE" if (c.lost_option or c.irreversible_debt) else "INACTIVE",
        "exact_restoration": exact_restoration(c),
        "reason_mutation": f"{c.reason_before}_TO_{c.reason_after}" if mutated else "NONE",
        "independent_warrant_created": False if (mutated and c.same_ancestry) else None,
        "veto_monotone": not (c.veto_before and not c.veto_after),
        "authority_monotone_with_more_evidence": not (
            c.more_evidence and c.prior_relation == "DOMINATES" and c.new_relation != "DOMINATES"
        ),
        "cycle_persistent": c.cycle_before and c.cycle_after,
        "history_scalarization": "OFF",
        "universal_historical_meta_utility": "NOT_EARNED",
    }
