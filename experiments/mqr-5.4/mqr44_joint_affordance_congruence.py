"""MQR 5.4: joint-action affordance and observation congruence.
Synthetic four-state toy, not a physical docking experiment or novel automata theorem.
"""
from itertools import product

STATES = tuple(product((0, 1), repeat=2))

def flip_a(s):
    return (1-s[0], s[1])

def flip_b(s):
    return (s[0], 1-s[1])

def controlled_port(s):
    return (s[0] ^ s[1], s[1])

def placebo(s):
    return s

def read_a(s):
    return s[0]

def read_b(s):
    return s[1]

def steps(s, word):
    for op in word:
        s = op(s)
    return s

def signature(s, actions, depth):
    return tuple(read_a(steps(s, word)) for k in range(depth+1)
                 for word in product(actions, repeat=k))

def classes(actions, depth=3):
    return len({signature(s, actions, depth) for s in STATES})

def equiv_by_words(actions, depth):
    return {(s,t) for s in STATES for t in STATES
            if signature(s, actions, depth) == signature(t, actions, depth)}

def preserves_equiv(op, eq):
    return all((op(s), op(t)) in eq for s,t in eq)

def run_tests():
    old = (flip_a,)
    eq = equiv_by_words(old, 3)
    assert len(eq) == 8
    assert classes(old) == 2
    assert preserves_equiv(flip_a, eq)
    assert preserves_equiv(flip_b, eq)
    assert preserves_equiv(placebo, eq)
    assert not preserves_equiv(controlled_port, eq)
    assert classes((flip_a, flip_b)) == 2
    assert classes((flip_a, placebo)) == 2
    assert classes((flip_a, controlled_port)) == 4
    assert classes((flip_a, controlled_port), 1) == 4
    assert [read_a(controlled_port(s)) for s in STATES] == [0, 1, 1, 0]
    assert [read_b(s) for s in STATES] == [0, 1, 0, 1]
    for s in STATES:
        assert read_a(controlled_port(s)) == (s[0] ^ s[1])
    return True

if __name__ == '__main__':
    assert run_tests()
    print('PASS: 13 exact assertions over all four states')
    print('A only:', classes((flip_a,)))
    print('A + B independent local flips:', classes((flip_a, flip_b)))
    print('A + B joint controlled coupling:', classes((flip_a, controlled_port)))
