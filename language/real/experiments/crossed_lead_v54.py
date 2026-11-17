"""Exploratory deterministic check for a crossed frequency/lead comparison."""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class LeadPair:
    frequency_hz: int
    short: Fraction
    long: Fraction

    @property
    def gap(self) -> Fraction:
        return self.long - self.short


def held_out_gap_residual(
    first: LeadPair, second: LeadPair, held_out: LeadPair
) -> Fraction:
    """Test an affine-in-f² long-minus-short contrast at a fresh frequency.

    Readings are expressed in a common unit at the same reference plane.
    A residual tests the differential model; a frequency effect common to both
    lead conditions cancels, irrespective of its shape.
    """
    frequencies = (first.frequency_hz, second.frequency_hz, held_out.frequency_hz)
    if min(frequencies) <= 0 or len(set(frequencies)) != 3:
        raise ValueError("Use three distinct positive frequencies")
    weight = Fraction(
        held_out.frequency_hz**2 - first.frequency_hz**2,
        second.frequency_hz**2 - first.frequency_hz**2,
    )
    prediction = first.gap + weight * (second.gap - first.gap)
    return held_out.gap - prediction
