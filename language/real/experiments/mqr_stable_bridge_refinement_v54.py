"""Compute the coarsest stable refinement of an observational partition.

Finite deterministic thought experiment for MQR 5.4, not empirical physics.
"""
from collections import defaultdict
from itertools import product


def normalise(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def refine(states, initial, actions):
    """Refine until states in each block have same successor block for each action."""
    states = set(states)
    blocks = normalise(initial)
    assert set().union(*map(set, blocks)) == states
    assert sum(map(len, blocks)) == len(states)
    assert all(set(T) == states and set(T.values()) <= states for T in actions)
    history = [blocks]
    while True:
        lookup = {state: i for i, block in enumerate(blocks) for state in block}
        groups = defaultdict(list)
        for state in sorted(states):
            signature = (lookup[state],) + tuple(lookup[T[state]] for T in actions)
            groups[signature].append(state)
        nxt = normalise(groups.values())
        if nxt == blocks:
            return blocks, tuple(history)
        assert len(nxt) > len(blocks)
        blocks = nxt
        history.append(blocks)


def stable(partition, actions):
    lookup = {s: i for i, b in enumerate(partition) for s in b}
    return all(len({lookup[T[s]] for s in block}) == 1 for block in partition for T in actions)


def verify():
    initial = ((0, 1, 2), (3,))
    identity = {i: i for i in range(4)}
    shift = {0:1, 1:2, 2:3, 3:3}
    p0, h0 = refine(range(4), initial, (identity,))
    assert p0 == normalise(initial) and len(h0) == 1
    p1, history = refine(range(4), initial, (shift,))
    assert history == (
        ((0, 1, 2), (3,)),
        ((0, 1), (2,), (3,)),
        ((0,), (1,), (2,), (3,)),
    ), history
    assert stable(p1, (shift,))
    assert not stable(initial, (shift,))
    swap = {0:1,1:0,2:2,3:3}
    p2, _ = refine(range(4), initial, (swap,))
    assert p2 == normalise(initial)
    for f in product(range(3), repeat=3):
        T={i:f[i] for i in range(3)}
        source=((0,1),(2,))
        _, path=refine(range(3),source,(T,))
        assert stable(path[-1],(T,))
    return 'PASS: 4-world refinement 2->3->4; harmless swap retains 2; all 27 three-world actions stable after refinement'


if __name__ == '__main__':
    print(verify())
