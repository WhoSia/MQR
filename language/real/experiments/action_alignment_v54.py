"""Enumerate action correspondences compatible with finite shared-world probes.

World-case correspondence is supplied by the analyst. This model does NOT
infer how two agents identify the same physical preparation in the first place.
"""

from itertools import permutations

from active_observable_v54 import ObservationTable


def equality_pattern(values: tuple[str, ...]) -> tuple[int, ...]:
    """Canonical code for the equality relation on observed symbols."""
    ids: dict[str, int] = {}
    pattern: list[int] = []
    for value in values:
        if value not in ids:
            ids[value] = len(ids)
        pattern.append(ids[value])
    return tuple(pattern)


def compatible_action_alignments(
    first: ObservationTable,
    second: ObservationTable,
    shared_worlds: tuple[str, ...] | None = None,
) -> tuple[tuple[tuple[str, str], ...], ...]:
    """All action bijections matching outcome-equality patterns.

    Assumes paired and identically ordered physical preparations, a bijection
    between listed actions, and arbitrary one-to-one re-encoding of outputs.
    Multiple surviving alignments mean action translation is unresolved.
    """
    if first.worlds != second.worlds:
        raise ValueError("The physical world preparations must be aligned first")
    if len(first.experiments) != len(second.experiments):
        raise ValueError("This bounded model requires equally many actions")
    if len(first.experiments) > 8:
        raise ValueError("Factorial enumeration is capped at eight actions")
    if shared_worlds is None:
        shared_worlds = first.worlds
    if len(set(shared_worlds)) != len(shared_worlds) or any(w not in first.worlds for w in shared_worlds):
        raise ValueError("Shared probes must be a unique subset of known preparations")
    indices = tuple(first.worlds.index(w) for w in shared_worlds)

    def action_signature(experiment):
        return equality_pattern(tuple(experiment.outcomes[i] for i in indices))

    first_patterns = tuple(map(action_signature, first.experiments))
    results = []
    for arrangement in permutations(second.experiments):
        if tuple(map(action_signature, arrangement)) == first_patterns:
            results.append(tuple((a.name, b.name) for a, b in zip(first.experiments, arrangement)))
    return tuple(results)
