"""Compare candidate dictionaries between declared finite experiment models."""

from dataclasses import dataclass
from itertools import permutations
from typing import Mapping

from protocol_frontier_v54 import Machine, Result, compare


Protocol = tuple[Mapping[str, int], ...]
Dictionary = tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class TranslationCandidate:
    dictionary: Dictionary
    comparison: Result


def _validate_protocol(machine: Machine, protocol: Protocol) -> None:
    if not protocol:
        raise ValueError("a protocol needs an initial state")
    for row in protocol:
        for action, target in row.items():
            if action not in machine.transitions or not 0 <= target < len(protocol):
                raise ValueError(f"invalid native protocol edge for {action!r}")


def common_protocol(
    left: Protocol, right: Protocol, dictionaries: tuple[Dictionary, ...]
) -> Protocol:
    """Allow a word only if it is executable under every candidate dictionary."""
    if not dictionaries:
        raise ValueError("the common protocol needs at least one dictionary")
    maps = tuple(dict(dictionary) for dictionary in dictionaries)
    initial = (0,) * (len(maps) + 1)
    states = [initial]
    indices = {initial: 0}
    rows = []
    for left_state, *right_states in states:
        row = {}
        for action, left_target in sorted(left[left_state].items()):
            targets = tuple(
                right[state].get(mapping[action])
                for state, mapping in zip(right_states, maps)
            )
            if None in targets:
                continue
            target = (left_target, *targets)
            if target not in indices:
                indices[target] = len(states)
                states.append(target)
            row[action] = indices[target]
        rows.append(row)
    return tuple(rows)


def assess(
    left: Machine,
    right: Machine,
    left_protocol: Protocol,
    right_protocol: Protocol,
    costs: Mapping[str, int],
    *,
    budget: int | None = None,
) -> tuple[TranslationCandidate, ...]:
    """Screen bijections on initial and single-action traces, then seek later mismatches.

    Each initially available left action must have a matching, initially
    executable right counterpart. Later comparisons use only words executable
    under all surviving dictionaries. Costs are shared and in left units.
    """
    _validate_protocol(left, left_protocol)
    _validate_protocol(right, right_protocol)
    left_labels = sorted(left.transitions)
    right_labels = sorted(right.transitions)
    if len(left_labels) != len(right_labels):
        raise ValueError("this analysis requires equal-size action alphabets")
    if budget is not None and (type(budget) is not int or budget < 0):
        raise ValueError("budget must be a nonnegative integer")
    for action in {action for row in left_protocol for action in row}:
        cost = costs.get(action)
        if type(cost) is not int or cost <= 0:
            raise ValueError(f"positive integer cost required for {action!r}")
    if left.trace(()) != right.trace(()):
        return ()

    left_single = {a: left.trace((a,)) for a in left_protocol[0]}
    right_single = {a: right.trace((a,)) for a in right_protocol[0]}
    dictionaries = []
    for labels in permutations(right_labels):
        dictionary = tuple(zip(left_labels, labels))
        if all(right_single.get(b) == left_single[a] for a, b in dictionary if a in left_single):
            dictionaries.append(dictionary)
    if not dictionaries:
        return ()

    protocol = common_protocol(left_protocol, right_protocol, tuple(dictionaries))
    return tuple(
        TranslationCandidate(
            dictionary,
            compare(
                left,
                Machine(right.observations, {
                    a: right.transitions[b] for a, b in dictionary
                }, right.initial),
                protocol,
                costs,
                budget=budget,
            ),
        )
        for dictionary in dictionaries
    )
