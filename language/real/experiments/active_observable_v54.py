"""Finite exact observation classes under explicitly named experiments.

A bounded epistemic benchmark, not a claim that the experiment space or
the physical world's state inventory has already been exhausted.
"""

from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Experiment:
    name: str
    outcomes: tuple[str, ...]


@dataclass(frozen=True)
class ObservationTable:
    worlds: tuple[str, ...]
    experiments: tuple[Experiment, ...]

    def __post_init__(self) -> None:
        if not self.worlds or any(not world for world in self.worlds) or len(set(self.worlds)) != len(self.worlds):
            raise ValueError("World labels must be nonempty and distinct")
        names = [experiment.name for experiment in self.experiments]
        if len(set(names)) != len(names) or any(not name for name in names):
            raise ValueError("Experiment names must be nonempty and distinct")
        if any(len(experiment.outcomes) != len(self.worlds) for experiment in self.experiments):
            raise ValueError("Every experiment needs one result per world")

    def partition(self, selected: tuple[str, ...] | None = None) -> tuple[tuple[str, ...], ...]:
        """Indistinguishability classes in the fixed input order of worlds.

        selected=None uses all available experiments; selected=() uses none.
        Observed values are compared for equality, never ordered.
        """
        if selected is None:
            chosen = self.experiments
        else:
            lookup = {experiment.name: experiment for experiment in self.experiments}
            if len(set(selected)) != len(selected) or any(x not in lookup for x in selected):
                raise ValueError("Selected experiment names must be unique and available")
            chosen = tuple(lookup[name] for name in selected)
        groups: dict[tuple[str, ...], list[str]] = {}
        for i, world in enumerate(self.worlds):
            signature = tuple(experiment.outcomes[i] for experiment in chosen)
            groups.setdefault(signature, []).append(world)
        return tuple(tuple(group) for group in groups.values())

    def smallest_sufficient_set(self) -> tuple[str, ...]:
        """An exact smallest subset preserving ALL available distinctions.

        Exhaustive enumeration has worst-case exponential cost in the number
        of experiments. This is a small finite benchmark, not a scalable solver.
        """
        target = self.partition()
        names = tuple(experiment.name for experiment in self.experiments)
        for count in range(len(names) + 1):
            for subset in combinations(names, count):
                if self.partition(subset) == target:
                    return subset
        raise AssertionError("The full experiment family always preserves its own partition")

    def add(self, experiment: Experiment) -> "ObservationTable":
        return ObservationTable(self.worlds, self.experiments + (experiment,))

    def unresolved_pairs(self, selected: tuple[str, ...] | None = None) -> tuple[tuple[str, str], ...]:
        """Pairs of worlds still observationally indistinguishable."""
        classes = self.partition(selected)
        return tuple(pair for group in classes for pair in combinations(group, 2))


def pairs_separated_by_new_observable(
    before: ObservationTable, additional: Experiment
) -> tuple[tuple[str, str], ...]:
    """Pairs separated by the extra observable under the same world indexing."""
    after = before.add(additional)
    unresolved_after = set(after.unresolved_pairs())
    return tuple(pair for pair in before.unresolved_pairs() if pair not in unresolved_after)
