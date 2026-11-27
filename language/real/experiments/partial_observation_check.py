"""Exhaustive reset-controlled three-state Moore machines (synthetic)."""
from collections import Counter, deque
from itertools import combinations, product

WORLDS = tuple(product(range(3), repeat=6))
COARSE, FINE = (0, 0, 1), (0, 1, 2)
A, B = (0, 1, 0, 2, 0, 0), (0, 1, 0, 2, 0, 1)


def endpoint(w, word, labels):
    s = 0
    for p in word:
        s = w[2*s+p]
    return labels[s]


def shortest(a, b, labels):
    queue = deque([(0, 0, ())])
    seen = {(0, 0)}
    while queue:
        s, t, word = queue.popleft()
        for p in (0, 1):
            x, y = a[2*s+p], b[2*t+p]
            new = word + (p,)
            if labels[x] != labels[y]:
                return new
            if (x, y) not in seen:
                seen.add((x, y))
                queue.append((x, y, new))
    return None


def census(labels):
    c = Counter()
    for a, b in combinations(WORLDS, 2):
        word = shortest(a, b, labels)
        c[None if word is None else len(word)] += 1
    return c


def classes(labels, depth):
    words = tuple(w for n in range(1, depth+1)
                  for w in product((0, 1), repeat=n))
    groups = Counter(tuple(endpoint(w, p, labels) for p in words) for w in WORLDS)
    return len(groups), sum(n*(n-1)//2 for n in groups.values())


def verify():
    coarse, fine = census(COARSE), census(FINE)
    assert coarse == {1:183708, 2:58496, 3:3928, 4:230, None:18994}
    assert sum(coarse.values()) == sum(fine.values()) == 265356
    for labels, counts in ((COARSE,coarse),(FINE,fine)):
        max_depth = max(k for k in counts if k is not None)
        for d in range(max_depth+1):
            _, indist = classes(labels,d)
            assert indist == sum(n for k,n in counts.items() if k is None or k>d)
    assert shortest(A,B,COARSE) == (1,1,1,1)
    assert shortest(A,B,FINE) == (1,1,1)
    assert classes(COARSE,4) == (384,18994)
    assert all(endpoint(A,w,FINE) == endpoint(B,w,FINE)
               for n in range(3) for w in product((0,1),repeat=n))
    print('coarse:', coarse, 'fine:', fine)
    print('coarse classes by depth:', [classes(COARSE,d)[0] for d in range(5)])
    print('fine classes by depth:', [classes(FINE,d)[0] for d in range(4)])
    print('witness: coarse 1111; fine 111')


if __name__ == '__main__':
    verify()
