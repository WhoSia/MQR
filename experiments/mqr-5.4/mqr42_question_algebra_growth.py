"""MQR 5.4: finite observable-vocabulary growth (Python standard library).

For comparing outputs of different action words, the same initial state must
be reproducibly prepared (or independently identified). Without this
assumption the operational signature is not jointly observable.
"""
from itertools import product

STATES = tuple(product((0, 1), repeat=3))

def swap_xy(s): return (s[1], s[0], s[2])
def swap_xz(s): return (s[2], s[1], s[0])
def flip_x(s): return (1 - s[0], s[1], s[2])
def flip_y(s): return (s[0], 1 - s[1], s[2])

def signature(s, protocol):
    for name, action in protocol:
        s = action(s)
    return s[0]

def words(actions, horizon):
    current = ((),)
    yielded = [()]
    for _ in range(horizon):
        current = tuple(w + ((name, action),) for w in current for name, action in actions.items())
        yielded.extend(current)
    return yielded

def classes(actions, horizon):
    protocols = words(actions, horizon)
    signatures = {s: tuple(signature(s, p) for p in protocols) for s in STATES}
    groups = {}
    for s, sig in signatures.items():
        groups.setdefault(sig, []).append(s)
    return sorted((tuple(g) for g in groups.values()), key=lambda group: group[0])

def predicates(groups):
    return 2**len(groups)

def check():
    action_sets = {
        'passive': {},
        'flip_x_negative': {'flip_x': flip_x},
        'flip_y_negative': {'flip_y': flip_y},
        'swap_xy': {'swap_xy': swap_xy},
        'swap_xz': {'swap_xz': swap_xz},
        'both_swaps': {'swap_xy': swap_xy, 'swap_xz': swap_xz},
    }
    expected = {
        'passive': (2, 2, 2),
        'flip_x_negative': (2, 2, 2),
        'flip_y_negative': (2, 2, 2),
        'swap_xy': (2, 4, 4),
        'swap_xz': (2, 4, 4),
        'both_swaps': (2, 8, 8),
    }
    for name, actions in action_sets.items():
        counts = tuple(len(classes(actions, h)) for h in (0, 1, 2))
        assert counts == expected[name], (name, counts)
        assert all(len(classes(actions, h+1)) >= len(classes(actions, h)) for h in range(3))
        assert sum(map(len, classes(actions, 2))) == len(STATES)
        print(f'{name:20s} depth0/1/2={counts}  predicates(depth2)={predicates(classes(actions,2))}')
    assert len(classes(action_sets['both_swaps'],2)) == 8
    print('ALL ASSERTIONS PASS')

if __name__ == '__main__':
    check()
