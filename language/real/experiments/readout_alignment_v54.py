"""Check finite intensity predictions with an unknown monotone detector."""

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True)
class Reading:
    intensity: Fraction
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("response interval must be nonempty")


def compatible(
    readings: Iterable[Reading],
    *,
    strict: bool,
) -> bool:
    """Return whether one response function can meet all recorded intervals.

    A distinct intensity can share a noiseless response only in weak mode.
    Repeats at the same intensity always refer to a single noiseless value.
    """
    groups: dict[Fraction, tuple[Fraction, Fraction]] = {}
    for reading in readings:
        lower, upper = groups.get(reading.intensity, (reading.lower, reading.upper))
        intersection = max(lower, reading.lower), min(upper, reading.upper)
        if intersection[0] > intersection[1]:
            return False
        groups[reading.intensity] = intersection

    max_lower = None
    for _, (lower, upper) in sorted(groups.items()):
        if max_lower is not None:
            if max_lower > upper or (strict and max_lower == upper):
                return False
        max_lower = lower if max_lower is None else max(max_lower, lower)
    return True
