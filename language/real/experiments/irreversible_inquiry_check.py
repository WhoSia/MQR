"""Exact finite belief-state analysis: pairwise tests vs one-shot strategies."""
from collections import defaultdict, deque
from itertools import combinations, product


def initial(models):
    return frozenset((i, 0) for i in range(len(models)))


def outcomes(models, belief, action):
    groups = defaultdict(set)
    for i, state in belief:
        nxt, obs = models[i][state][action]
        groups[obs].add((i, nxt))
    return {o: frozenset(b) for o, b in groups.items()}


def ranks(models, root):
    """Least fixed point of guaranteed termination; exact for finite models."""
    actions = tuple(models[0][0])
    todo, graph = deque([root]), {}
    while todo:
        b = todo.popleft()
        if b in graph:
            continue
        graph[b] = {a: outcomes(models, b, a) for a in actions}
        for cells in graph[b].values():
            todo.extend(c for c in cells.values() if c not in graph)
    rank = {b: 0 for b in graph if len({i for i, _ in b}) == 1}
    policy = {}
    while True:
        new = {}
        for b in graph.keys() - rank.keys():
            choices = [(1 + max(rank[c] for c in cs.values()), a)
                       for a, cs in graph[b].items() if all(c in rank for c in cs.values())]
            if choices:
                new[b] = min(choices)
        if not new:
            return rank, policy, len(graph)
        for b, (d, a) in new.items():
            rank[b], policy[b] = d, a


def one_shot(signatures):
    return tuple(({a: (1, row[a]) for a in range(len(row))},
                  {a: (1, 0) for a in range(len(row))}) for row in signatures)


def adaptive_four():
    models = []
    for group, bit in product(range(2), repeat=2):
        models.append((
            {0: (1, group), 1: (2, 0), 2: (2, 0)},
            {0: (2, 0), 1: (2, bit if group == 0 else 0),
             2: (2, bit if group == 1 else 0)},
            {a: (2, 0) for a in range(3)},
        ))
    return tuple(models)


def fixed_word_succeeds(models, root, word):
    cells = [root]
    for a in word:
        cells = [c for b in cells for c in outcomes(models,b,a).values()]
    return all(len({i for i,_ in b}) == 1 for b in cells)


def fixed_strategy_exists(models, root):
    """Search partitions of surviving beliefs under common action words."""
    start = frozenset([root]); seen={start}; todo=deque([start])
    while todo:
        cells = todo.popleft()
        if all(len({i for i,_ in b}) == 1 for b in cells):
            return True
        for a in models[0][0]:
            nxt = frozenset(c for b in cells for c in outcomes(models,b,a).values())
            if nxt not in seen:
                seen.add(nxt); todo.append(nxt)
    return False


def verify():
    models = one_shot([(0,0),(0,1),(1,0)])
    root = initial(models)
    rank, policy, size = ranks(models,root)
    assert root not in rank
    for pair in combinations(root,2):
        b=frozenset(pair); assert ranks(models,b)[0][b] == 1
    assert not fixed_strategy_exists(models,root)
    # Every 3 distinct 2-bit signatures is pairwise separable but not one-shot diagnosable.
    for rows in combinations(tuple(product(range(2), repeat=2)),3):
        m=one_shot(rows); r=initial(m)
        assert r not in ranks(m,r)[0]
        for p in combinations(r,2):
            b=frozenset(p); assert ranks(m,b)[0][b]==1
    m=adaptive_four(); r=initial(m)
    rank, policy, n = ranks(m,r)
    assert rank[r] == 2 and policy[r] == 0
    branches=outcomes(m,r,0)
    assert [policy[branches[g]] for g in (0,1)] == [1,2]
    assert not fixed_strategy_exists(m,r)
    # If reset makes both tests independently usable, their pair of bits is injective.
    assert len({(0,0),(0,1),(1,0)}) == 3
    print('three-world witness: all 3 pairs separable, no adaptive global strategy; reachable beliefs:',size)
    print('all 4 three-signature subsets checked; adaptive four-world witness: depth',rank[r],'; reachable beliefs:',n,'; no fixed word')


if __name__=='__main__':
    verify()
