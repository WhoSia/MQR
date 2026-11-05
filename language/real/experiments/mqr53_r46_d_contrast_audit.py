"""R46-D: observational contrasts are not automatically causal estimates."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Observation:
    id: int
    regime: str
    supplement: bool
    extra: bool
    response: float


DATA = (
    Observation(1, "short-wide", False, False, 8.0),
    Observation(2, "short-wide", True, False, 64.0),
    Observation(3, "short-wide", True, True, 0.8),
    Observation(4, "long-narrow", False, False, 9.0),
    Observation(5, "long-narrow", True, False, 21.0),
)


def comparison(a: Observation, b: Observation) -> tuple[float, tuple[str, ...]]:
    """Report a descriptive difference and every changed input axis."""
    if a.id == b.id:
        raise ValueError("Distinct observations required")
    columns = ("regime", "supplement", "extra")
    changed = tuple(c for c in columns if getattr(a, c) != getattr(b, c))
    return b.response - a.response, changed


def interaction() -> float:
    """A descriptive contrast across *bundled* regimes, not a causal parameter."""
    return comparison(DATA[3], DATA[4])[0] - comparison(DATA[0], DATA[1])[0]
