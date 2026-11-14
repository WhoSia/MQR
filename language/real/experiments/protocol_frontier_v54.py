"""Compare two declared finite experiments by their admissible observation traces."""

from dataclasses import dataclass
from enum import Enum
from heapq import heappop, heappush
from itertools import count
from typing import Mapping


@dataclass(frozen=True)
class Machine:
    observations: tuple[str, ...]
    transitions: Mapping[str, tuple[int, ...]]
    initial: int = 0

    def __post_init__(self) -> None:
        size = len(self.observations)
        if not 0 <= self.initial < size:
            raise ValueError("initial state is outside the machine")
        for action, row in self.transitions.items():
            if not action or len(row) != size or any(not 0 <= state < size for state in row):
                raise ValueError(f"invalid transition row for {action!r}")

    def trace(self, actions: tuple[str, ...]) -> tuple[str, ...]:
        state = self.initial
        observations = [self.observations[state]]
        for action in actions:
            state = self.transitions[action][state]
            observations.append(self.observations[state])
        return tuple(observations)


class ResultKind(str, Enum):
    DISTINGUISHABLE = "distinguishable"
    BEYOND_BUDGET = "beyond_budget"
    EQUIVALENT_UNDER_PROTOCOL = "equivalent_under_protocol"


@dataclass(frozen=True)
class Witness:
    actions: tuple[str, ...]
    cost: int
    left_trace: tuple[str, ...]
    right_trace: tuple[str, ...]


@dataclass(frozen=True)
class Result:
    kind: ResultKind
    witness: Witness | None
    settled_states: int


def compare(
    left: Machine,
    right: Machine,
    protocol: tuple[Mapping[str, int], ...],
    costs: Mapping[str, int],
    *,
    budget: int | None = None,
) -> Result:
    """Find the minimum-cost distinguishing trace, starting protocol at state zero.

    A missing protocol edge forbids its action. Every prefix can be observed.
    A budget changes the verdict about affordability, not the exhaustive search.
    """
    if not protocol:
        raise ValueError("a protocol needs an initial state")
    if budget is not None and (type(budget) is not int or budget < 0):
        raise ValueError("budget must be a nonnegative integer")
    for row in protocol:
        for action, target in row.items():
            if not 0 <= target < len(protocol):
                raise ValueError(f"invalid protocol successor for {action!r}")
            if action not in left.transitions or action not in right.transitions:
                raise ValueError(f"both machines must support protocol action {action!r}")
            cost = costs.get(action)
            if type(cost) is not int or cost <= 0:
                raise ValueError(f"positive integer cost required for {action!r}")

    initial = (left.initial, right.initial, 0)
    order = count()
    queue = [(0, next(order), initial)]
    distances = {initial: 0}
    parents: dict[tuple[int, int, int], tuple[tuple[int, int, int], str]] = {}
    settled = 0
    while queue:
        cost, _, state = heappop(queue)
        if cost != distances[state]:
            continue
        settled += 1
        left_state, right_state, protocol_state = state
        if left.observations[left_state] != right.observations[right_state]:
            path = []
            while state != initial:
                state, action = parents[state]
                path.append(action)
            actions = tuple(reversed(path))
            witness = Witness(actions, cost, left.trace(actions), right.trace(actions))
            kind = ResultKind.DISTINGUISHABLE
            if budget is not None and cost > budget:
                kind = ResultKind.BEYOND_BUDGET
            return Result(kind, witness, settled)

        for action, protocol_target in sorted(protocol[protocol_state].items()):
            target = (
                left.transitions[action][left_state],
                right.transitions[action][right_state],
                protocol_target,
            )
            total = cost + costs[action]
            if target in distances and distances[target] <= total:
                continue
            distances[target] = total
            parents[target] = (state, action)
            heappush(queue, (total, next(order), target))
    return Result(ResultKind.EQUIVALENT_UNDER_PROTOCOL, None, settled)
