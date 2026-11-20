"""Prospective test selection among models with identical past observations.

Formal model only. It does not generate concepts or establish theory truth.
"""
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Theory:
    name: str
    predictions: tuple[tuple[str, str], ...]

    def __post_init__(self) -> None:
        names = [experiment for experiment, _ in self.predictions]
        if not self.name or not names or len(names) != len(set(names)) or any(not n for n in names):
            raise ValueError("Theory requires a unique name and unique nonempty experiment names")

    def predict(self, experiment: str) -> str:
        for name, value in self.predictions:
            if name == experiment:
                return value
        raise ValueError(f"Unknown experiment: {experiment}")


@dataclass(frozen=True)
class TheoryFamily:
    theories: tuple[Theory, ...]

    def __post_init__(self) -> None:
        if not self.theories or len({t.name for t in self.theories}) != len(self.theories):
            raise ValueError("Requires nonempty theories with unique names")
        domains = [set(e for e, _ in t.predictions) for t in self.theories]
        if any(d != domains[0] for d in domains[1:]):
            raise ValueError("Each theory must predict the same experiment menu")

    @property
    def menu(self) -> tuple[str, ...]:
        return tuple(name for name, _ in self.theories[0].predictions)

    def viable(self, observed: tuple[tuple[str, str], ...]) -> tuple[Theory, ...]:
        names = [e for e, _ in observed]
        if len(names) != len(set(names)) or any(e not in self.menu for e in names):
            raise ValueError("Observations must reference unique known experiments")
        return tuple(t for t in self.theories if all(t.predict(e) == v for e, v in observed))

    def discrimination_scores(self, observed: tuple[tuple[str, str], ...]) -> tuple[tuple[str, int], ...]:
        """Count unordered pairs of viable models separated by each unmeasured probe."""
        live = self.viable(observed)
        used = {name for name, _ in observed}
        return tuple((e, sum(t.predict(e) != u.predict(e) for t, u in combinations(live, 2)))
                     for e in self.menu if e not in used)

    def next_probe(self, observed: tuple[tuple[str, str], ...]) -> str | None:
        """Maximize pairwise splits; stable first-on-tie, abstain at zero."""
        scored = self.discrimination_scores(observed)
        if not scored:
            return None
        best_name, best_score = max(scored, key=lambda pair: pair[1])
        return best_name if best_score > 0 else None

    def revise(self, observed: tuple[tuple[str, str], ...],
               experiment: str, outcome: str) -> tuple[tuple[tuple[str, str], ...], tuple[str, ...]]:
        if experiment not in self.menu or experiment in {e for e, _ in observed}:
            raise ValueError("New observation requires an unused declared experiment")
        next_observed = observed + ((experiment, outcome),)
        return next_observed, tuple(t.name for t in self.viable(next_observed))
