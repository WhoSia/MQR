"""MQR 5.4 / chat MQR 41 — compositional protocol discovery.

Standard library. Synthetic truth-table model, not an empirical experiment.
States can be perfectly re-prepared across mutually exclusive protocols.
An operation's marginal information gain need not measure its usefulness in a
future composition. Composition search assumes the primitive alphabet is given.
"""
from itertools import product

STATES = tuple(product((0, 1), repeat=3))
ACTIONS = {
    "swap_xy": lambda s: (s[1], s[0], s[2]),
    "swap_yz": lambda s: (s[0], s[2], s[1]),
    "flip_x": lambda s: (1-s[0], s[1], s[2]),
}

def observed(state, protocol):
    for name in protocol:
        state = ACTIONS[name](state)
    return state[0]

def signatures(protocols):
    return {state: tuple(observed(state, word) for word in protocols)
            for state in STATES}

def class_count(protocols):
    return len(set(signatures(protocols).values()))

def words_up_to(horizon):
    result = [()]
    for depth in range(1, horizon+1):
        result += list(product(ACTIONS, repeat=depth))
    return result

def greedy_atomic():
    available = [()]
    selected = []
    while True:
        n = class_count(available)
        gains = [(class_count(available + [(a,)])-n, a) for a in ACTIONS
                 if a not in selected]
        best_gain, best = max(gains, default=(0, None))
        if best_gain <= 0:
            return selected, n
        selected.append(best)
        available.append((best,))

def run_tests():
    assert len(STATES) == 8
    assert class_count([()]) == 2
    assert class_count([(), ("swap_yz",)]) == 2
    assert class_count([(), ("flip_x",)]) == 2
    assert class_count([(), ("swap_xy",)]) == 4
    assert class_count([(), ("swap_xy",), ("swap_yz",)]) == 4
    assert class_count([(), ("swap_xy",), ("swap_yz","swap_xy")]) == 8
    assert [class_count(words_up_to(h)) for h in range(3)] == [2, 4, 8]
    choice, plateau = greedy_atomic()
    assert choice == ["swap_xy"] and plateau == 4, (choice, plateau)
    for s in STATES:
        assert observed(s, ("swap_yz","swap_xy")) == s[2]
    assert class_count(words_up_to(2)) == 8
    assert 2 ** class_count(words_up_to(2)) == 256
    print("atomic greedy: selected=%s, classes=%s" % (choice, plateau))
    print("compositional BFS: horizons=0,1,2; classes=2,4,8")
    print("successful word: swap_yz -> swap_xy -> observed z")
    print("Boolean-algebra cardinalities: 4,16,256")
    print("PASS: all exhaustive assertions")

if __name__ == "__main__":
    run_tests()
