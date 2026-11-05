"""MQR R46-Q: a finite, purely illustrative measurement-causality witness.

This is a Python research fixture, NOT production Real Lang syntax.
It formalizes an elementary counterexample to observational identification,
not a novel mathematical theorem or an actual psychological experiment.
"""
from collections import Counter
from typing import Callable, Optional, Tuple

Triple = Tuple[int, int, int]
Model = Callable[[int, Optional[int]], Triple]


def attribute_causes_scores(u: int, force_x: Optional[int] = None) -> Triple:
    """Graph U -> X -> (Y1,Y2), with structural setting of X."""
    x = u if force_x is None else force_x
    return (x, x, x)


def common_cause_only(u: int, force_x: Optional[int] = None) -> Triple:
    """Graph U -> X and U -> (Y1,Y2), without X -> score arrows."""
    x = u if force_x is None else force_x
    return (x, u, u)


def law(model: Model, force_x: Optional[int] = None) -> dict[Triple, float]:
    """Exact finite distribution for a fair binary exogenous variable."""
    if force_x not in (None, 0, 1):
        raise ValueError("Interventions must be None, 0, or 1")
    count = Counter(model(u, force_x) for u in (0, 1))
    return {outcome: multiplicity / 2 for outcome, multiplicity in count.items()}


def observationally_equivalent() -> bool:
    return law(attribute_causes_scores) == law(common_cause_only)


def separated_by_setting_x(value: int) -> bool:
    if value not in (0, 1):
        raise ValueError("Binary intervention only")
    return law(attribute_causes_scores, value) != law(common_cause_only, value)
