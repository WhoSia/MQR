"""MQR 43: quantify passive-readout shortcuts versus active cross-lab probes.

Oracle predictions only. Cost counts primitive actions, NOT custody transfers,
reset operations, calibration time or physical reliability. A B-sensor ablation
models a native readout with a single outcome; it does not disable B's action.
"""
from dataclasses import dataclass
from itertools import combinations, product

from native_composition_bootstrap_v54 import ProposedBridge, all_alignments


ALPHABET = ('A:turn', 'B:shift')


@dataclass(frozen=True)
class Probe:
    word: tuple[str, ...]
    reader: str

    def __post_init__(self):
        if self.reader not in ('A', 'B') or any(a not in ALPHABET for a in self.word):
            raise ValueError('Unknown probe action or reader')

    @property
    def primitive_cost(self):
        return len(self.word)


def predict(bridge, probe, b_sensor_visible=True):
    if not isinstance(bridge, ProposedBridge) or not isinstance(probe, Probe):
        raise ValueError('Well-formed bridge and probe required')
    if probe.reader == 'B' and not b_sensor_visible:
        return 'opaque'  # constant sensor; nontrivial B action still enabled
    return bridge.predicted_joint_output(probe.word, probe.reader)


def classes(probes, b_sensor_visible=True):
    result = {}
    for permutation in all_alignments():
        model = ProposedBridge(permutation)
        signature = tuple(predict(model, p, b_sensor_visible) for p in probes)
        result.setdefault(signature, []).append(permutation)
    return {s: tuple(v) for s, v in result.items()}


def candidate_probes(max_word_length=3, allow_a=True, allow_b=True):
    if max_word_length < 0 or not (allow_a or allow_b):
        raise ValueError('Nonnegative length and at least one reader required')
    readers = tuple(r for r, enabled in (('A', allow_a), ('B', allow_b)) if enabled)
    return tuple(Probe(tuple(word), r) for n in range(max_word_length + 1)
                 for word in product(ALPHABET, repeat=n) for r in readers)


def optimal_basis(b_sensor_visible=True, allow_a=True, allow_b=True,
                  max_word_length=3, max_probes=2):
    """Smallest total action-count basis resolving 3 observable bridge classes."""
    probes = candidate_probes(max_word_length, allow_a, allow_b)
    candidates = []
    for count in range(1, max_probes + 1):
        for chosen in combinations(probes, count):
            if len(classes(chosen, b_sensor_visible)) == 3:
                candidates.append(chosen)
    if not candidates:
        return None
    return min(candidates, key=lambda chosen:
               (sum(p.primitive_cost for p in chosen), len(chosen),
                tuple((p.word, p.reader) for p in chosen)))
