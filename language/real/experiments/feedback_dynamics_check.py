"""Exhaustive check of fully observed deterministic binary-state worlds."""
from itertools import product, combinations
from collections import Counter, deque

WORLDS = tuple(product(range(2), repeat=4))


def trace(world, word):
    state = 0
    out = []
    for action in word:
        state = world[2 * state + action]
        out.append(state)
    return tuple(out)


def shortest_separator(a, b):
    queue = deque([(0, 0, ())])
    seen = {(0, 0)}
    while queue:
        x, y, word = queue.popleft()
        for p in (0, 1):
            nx, ny = a[2*x+p], b[2*y+p]
            new = word + (p,)
            if nx != ny:
                return new
            if (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append((nx, ny, new))
    return None


def verify():
    lengths = Counter()
    for a, b in combinations(WORLDS, 2):
        word = shortest_separator(a, b)
        lengths[None if word is None else len(word)] += 1
        short = [w for n in (1, 2) for w in product(range(2), repeat=n)
                 if trace(a, w) != trace(b, w)]
        assert (word is None) == (not short)
        if word is not None:
            assert len(word) == min(map(len, short))
    assert lengths == {1: 96, 2: 18, None: 6}, lengths
    groups = Counter(tuple(trace(w, p) for p in product(range(2), repeat=2))
                     for w in WORLDS)
    assert sorted(groups.values()) == [1]*12 + [4]
    # Full observed constant sequences, not just final output.
    a, b = (0, 1, 0, 1), (0, 1, 1, 1)
    for n in range(9):
        for p in (0, 1):
            assert trace(a, (p,)*n) == trace(b, (p,)*n)
    assert shortest_separator(a, b) == (1, 0)
    constant_candidates = [w for w in WORLDS
        if trace(w, (0,0)) == (0,0) and trace(w,(1,1)) == (1,1)]
    assert constant_candidates == [a,b]
    print('120 pairs:', dict(lengths), '; 13 observational classes')
    print('constant-policy candidates:', constant_candidates,
          '; shortest separator:', shortest_separator(a,b))


if __name__ == '__main__':
    verify()
