"""Exact calibration-transfer check for ratios of linear forms on a cone."""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


@dataclass(frozen=True)
class LinearRatio:
    """Responses to nonnegative mixtures of the declared basis probes."""

    numerator: tuple[Fraction, ...]
    denominator: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if not self.numerator or len(self.numerator) != len(self.denominator):
            raise ValueError("Numerator and denominator must share a nonempty basis")
        if any(value <= 0 for value in self.denominator):
            raise ValueError("Denominator must be positive on every basis probe")

    def probe(self, indices: tuple[int, ...]) -> Fraction:
        """Evaluate an equal-weight mixture, using each listed index once."""
        numerator = sum(self.numerator[i] for i in indices)
        denominator = sum(self.denominator[i] for i in indices)
        return Fraction(numerator) / denominator


def first_ratio_disagreement(
    reference: LinearRatio, candidate: LinearRatio
) -> tuple[int, ...] | None:
    """Return a basis probe or two-probe mixture witnessing non-transfer.

    If they agree on the singleton and pair probes, the two ratios agree
    on every nonzero nonnegative mixture in this linear response model.
    """
    size = len(reference.numerator)
    if size != len(candidate.numerator):
        raise ValueError("Both ratios must use the same basis size")

    for order in (1, 2):
        for indices in combinations(range(size), order):
            if reference.probe(indices) != candidate.probe(indices):
                return indices
    return None
