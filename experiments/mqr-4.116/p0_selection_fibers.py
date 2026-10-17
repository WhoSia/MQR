from dataclasses import dataclass

@dataclass(frozen=True)
class World:
    name: str
    roots: tuple[str, str]
    cited: tuple[int, ...]
    authority: str

def observe(w: World, include_authority=False):
    data = (w.cited,)
    return (w.authority,) + data if include_authority else data

def judgment(w: World):
    # Deliberately stipulated toy roots, NOT empirical independence certification.
    return w.roots[0] != w.roots[1]

def identifiable(worlds, include_authority=False):
    fibers = {}
    for w in worlds:
        fibers.setdefault(observe(w, include_authority), set()).add(judgment(w))
    return all(len(v) == 1 for v in fibers.values())

def run():
    a = World('independent', ('r1','r2'), (21,93), 'A1')
    b = World('shared', ('r1','r1'), (21,93), 'A1')
    assert observe(a) == observe(b)
    assert judgment(a) != judgment(b)
    assert not identifiable([a,b])
    assert (observe(a), a.roots) != (observe(b), b.roots)
    assert not identifiable([a,b], include_authority=True)
    c = World('different-selection', ('r1','r2'), (21,), 'A2')
    assert a.roots == c.roots and observe(a) != observe(c)
    print('PASS 4 bounded selection/identification checks')

if __name__ == '__main__':
    run()
