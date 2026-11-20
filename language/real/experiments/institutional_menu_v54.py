"""Finite physical vs institutionally admitted experiment menus.

A stylized counterexample, NOT a measured model of academic institutions.
The institutional admission set is externally stipulated, not inferred.
"""
from dataclasses import dataclass
from itertools import combinations

from active_observable_v54 import ObservationTable


@dataclass(frozen=True)
class InstitutionalMenu:
    physical: ObservationTable
    sanctioned: tuple[str, ...]

    def __post_init__(self) -> None:
        available = {experiment.name for experiment in self.physical.experiments}
        if (len(set(self.sanctioned)) != len(self.sanctioned)
                or any(name not in available for name in self.sanctioned)):
            raise ValueError("Sanctioned experiments must be distinct declared physical actions")

    def hidden_distinctions(self) -> tuple[tuple[str, str], ...]:
        """Pairs distinguishable by the physical menu, not by sanctioned work."""
        full_ambiguous = set(self.physical.unresolved_pairs())
        return tuple(pair for pair in self.physical.unresolved_pairs(self.sanctioned)
                     if pair not in full_ambiguous)

    def smallest_readmission(self) -> tuple[str, ...]:
        """Smallest set of excluded physical tests restoring full distinctions."""
        excluded = tuple(e.name for e in self.physical.experiments
                         if e.name not in self.sanctioned)
        target = self.physical.partition()
        for count in range(len(excluded) + 1):
            for subset in combinations(excluded, count):
                if self.physical.partition(self.sanctioned + subset) == target:
                    return subset
        raise AssertionError("Re-admitting all tests always restores the full partition")
