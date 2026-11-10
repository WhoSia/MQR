"""MQR 5.4 reproducible operational-translation toy witness (stdlib only)."""
from itertools import permutations, product
STATES = tuple(product((0, 1), repeat=2))
ACTIONS = {
    "flip_first": lambda s: (1-s[0], s[1]),
    "swap": lambda s: (s[1], s[0]),
}
def structural_maps():
    """All state and independently renamed action bijections preserving transitions."""
    for images in permutations(STATES):
        phi = dict(zip(STATES, images))
        for names in permutations(ACTIONS):
            psi = dict(zip(ACTIONS, names))
            if all(phi[f(s)] == ACTIONS[psi[name]](phi[s])
                   for s in STATES for name, f in ACTIONS.items()):
                yield phi, psi

def candidates(observation=False, anchor=False):
    for phi, psi in structural_maps():
        for flip in ((0, 1) if observation else (None,)):
            if observation and any(phi[s][0] != (s[0] ^ flip) for s in STATES):
                continue
            if anchor and phi[(0, 0)] != (0, 0):
                continue
            yield phi, psi, flip

def test():
    structural = list(structural_maps())
    assert len(structural) == 2
    assert len(list(candidates(True))) == 2
    assert len(list(candidates(True, True))) == 1
    assert len([c for c in candidates(True) if c[2] == 0]) == 1
    print("state-action structure:", len(structural))
    print("unknown binary readout convention:", len(list(candidates(True))))
    print("shared readout convention:", len([c for c in candidates(True) if c[2] == 0]))
    print("one matched state:", len(list(candidates(True, True))))
    print("state permutations:", [tuple(phi[s] for s in STATES) for phi, _ in structural])

if __name__ == "__main__":
    test()
