"""Finite alignment without presumed shared preparation identifiers.

An exact, *conditional* identifiability benchmark.
Never equate matching strings with physical co-reference unless a bridge
channel has been independently established.
"""
from dataclasses import dataclass
from itertools import permutations


@dataclass(frozen=True)
class SharedChannel:
    name: str
    a_results: tuple[str, ...]
    b_results: tuple[str, ...]


@dataclass(frozen=True)
class BridgeProblem:
    a_states: tuple[str, ...]
    b_states: tuple[str, ...]
    anchors: tuple[tuple[str, str], ...] = ()
    channels: tuple[SharedChannel, ...] = ()

    def __post_init__(self) -> None:
        n = len(self.a_states)
        if not (1 <= n <= 8) or len(self.b_states) != n:
            raise ValueError("Matching nonempty finite inventories, size <= 8")
        if (any(not s for s in self.a_states + self.b_states)
                or len(set(self.a_states)) != n or len(set(self.b_states)) != n):
            raise ValueError("State identifiers must be unique and nonempty")
        if (len({x for x, _ in self.anchors}) != len(self.anchors)
                or len({y for _, y in self.anchors}) != len(self.anchors)
                or any(x not in self.a_states or y not in self.b_states
                       for x, y in self.anchors)):
            raise ValueError("Anchors must be one-to-one valid labels")
        names = [c.name for c in self.channels]
        if (any(not name for name in names) or len(set(names)) != len(names)
                or any(len(c.a_results) != n or len(c.b_results) != n
                       for c in self.channels)):
            raise ValueError("Shared channels need unique names and complete results")

    def possible_bijections(
        self, additional: tuple[SharedChannel, ...] = ()
    ) -> tuple[tuple[str, ...], ...]:
        all_channels = self.channels + additional
        if len({c.name for c in all_channels}) != len(all_channels):
            raise ValueError("Channel names must be unique")
        n = len(self.a_states)
        if any(len(c.a_results) != n or len(c.b_results) != n
               for c in all_channels):
            raise ValueError("Each channel needs results for every state")
        a_pos = {x: i for i, x in enumerate(self.a_states)}
        b_pos = {x: i for i, x in enumerate(self.b_states)}
        result = []
        for assignment in permutations(self.b_states):
            if any(assignment[a_pos[x]] != y for x, y in self.anchors):
                continue
            if all(all(c.a_results[i] == c.b_results[b_pos[assignment[i]]]
                       for i in range(n)) for c in all_channels):
                result.append(assignment)
        return tuple(result)

    def best_proposed_channel(
        self, proposals: tuple[SharedChannel, ...]
    ) -> str | None:
        """Prefer a candidate with strictly fewer, nonzero possible bijections.

        Proposals already include both agents' predicted result signatures,
        a very strong assumption NOT automatically available to real agents.
        """
        start = len(self.possible_bijections())
        if start <= 1:
            return None
        best = None
        size = start
        for channel in proposals:
            after = len(self.possible_bijections((channel,)))
            if 0 < after < size:
                size, best = after, channel.name
        return best
