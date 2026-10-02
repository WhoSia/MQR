from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class ConflictCase:
    name: str
    relation: str = "INCOMPARABLE"
    scope_match: bool = True
    horizon_match: bool = True
    veto_active: bool = False
    fatal: bool = False
    duplicate_ancestry: bool = False
    common_mode: bool = False
    weighted_flip: bool = False
    lexicographic_failure: bool = False
    pareto_multiple: bool = False
    horizon_reversal: bool = False
    scope_reversal: bool = False
    material_support: bool = True
    material_opposition: bool = True

def naive_weighted(c: ConflictCase) -> str:
    if c.weighted_flip:
        return "UNSTABLE"
    return "PROMOTE" if c.material_support else "REJECT"

def naive_lexicographic(c: ConflictCase) -> str:
    if c.lexicographic_failure:
        return "DICTATORSHIP_FAILURE"
    return "PROMOTE" if c.material_support else "REJECT"

def adjudicate(c: ConflictCase) -> Tuple[str, str]:
    if c.duplicate_ancestry or c.common_mode:
        return ("HOLD", "ANCESTRY_COLLAPSE_REQUIRED")
    if c.horizon_reversal:
        return ("HOLD", "HORIZON_RELATION_REOPEN")
    if c.scope_reversal:
        return ("HOLD", "SCOPE_RELATION_REOPEN")
    if c.veto_active:
        if c.fatal and c.scope_match and c.horizon_match:
            return ("HOLD", "LOCAL_VETO_ACTIVE")
        return ("HOLD", "VETO_NOT_UNIVERSAL")
    if c.relation == "DOMINATES":
        return ("PROMOTE", "LOCAL_DOMINANCE")
    if c.relation == "DEFEATS_UNDER_SCOPE":
        return ("HOLD", "LOCAL_DEFEAT")
    if c.relation == "INCOMPARABLE":
        return ("HOLD", "INCOMPARABLE")
    return ("HOLD", "UNRESOLVED")
