"""MQR 5.4 chat43: native-operation composition without shared state names.

Finite analyst oracle. Native scientists see only recipes, owned action labels,
final native sensor symbols and physical-token transfer receipts. The alignment
between their hidden state coordinates is NOT known to either native scientist.
Boolean custody flags encode EXTERNAL assumptions, not physical validation.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product


N = 3
A_SENSOR = ("low", "low", "high")
B_SENSOR = ("x", "y", "y")
A_TURN = (1, 0, 2)  # swaps 0<->1, analyst indices only
B_SHIFT = (0, 2, 1)  # swaps 1<->2, B-local indices only
IDENTITY = (0, 1, 2)
B_RECIPES = {
    "B:clear": (Fraction(1), Fraction(0), Fraction(0)),
    "B:mixed": (Fraction(0), Fraction(1, 2), Fraction(1, 2)),
}


def compose(after, before):
    if len(after) != N or len(before) != N:
        raise ValueError("Mismatched operator domains")
    return tuple(after[before[i]] for i in range(N))


def closure(generators):
    """Return transformation->shortest native word in an explicitly scoped alphabet."""
    words = {IDENTITY: ()}
    frontier = [IDENTITY]
    for before in frontier:
        for name, action in generators.items():
            successor = compose(action, before)
            if successor not in words:
                words[successor] = words[before] + (name,)
                frontier.append(successor)
    return words


def all_alignments():
    return tuple(permutations(range(N)))


@dataclass(frozen=True)
class TransferReceipt:
    authenticated_token: bool
    stable_preparation: bool
    reset_reproduced: bool

    @property
    def admissible(self):
        return self.authenticated_token and self.stable_preparation and self.reset_reproduced


@dataclass(frozen=True)
class ProposedBridge:
    b_to_a: tuple[int, ...]

    def __post_init__(self):
        if tuple(sorted(self.b_to_a)) != IDENTITY:
            raise ValueError("Alignment must be a three-state permutation")

    def translated_b_action(self):
        p = self.b_to_a
        reverse = tuple(p.index(i) for i in range(N))
        return tuple(p[B_SHIFT[reverse[s]]] for s in range(N))

    def translated_b_sensor(self):
        p = self.b_to_a
        reverse = tuple(p.index(i) for i in range(N))
        return tuple(B_SENSOR[reverse[s]] for s in range(N))

    def native_a(self, sequence=(), recipe="A:seed"):
        if recipe != "A:seed" or any(action != "A:turn" for action in sequence):
            raise ValueError("Unrecognized A recipe/action")
        s = 0
        for action in sequence:
            s = A_TURN[s]
        return A_SENSOR[s]

    def native_b(self, sequence=(), recipe="B:clear"):
        if recipe not in B_RECIPES or any(action != "B:shift" for action in sequence):
            raise ValueError("Unrecognized B recipe/action")
        weights = B_RECIPES[recipe]
        for action in sequence:
            weights = tuple(sum(weights[j] for j in range(N) if B_SHIFT[j] == i)
                            for i in range(N))
        return {label: sum((w for s, w in enumerate(weights) if B_SENSOR[s] == label),
                           Fraction(0)) for label in ("x", "y")}

    def mixed_action_word(self, sequence):
        s = 0  # A's native recipe A:seed, analyst coordinate; no public state key
        g = self.translated_b_action()
        for action in sequence:
            if action == "A:turn":
                s = A_TURN[s]
            elif action == "B:shift":
                s = g[s]
            else:
                raise ValueError("Unknown native action")
        return s

    def predicted_joint_output(self, sequence, reader="A"):
        s = self.mixed_action_word(sequence)
        if reader == "A":
            return A_SENSOR[s]
        if reader == "B":
            return self.translated_b_sensor()[s]
        raise ValueError("Reader must be A or B")

    def warranted_output(self, sequence, receipt, reader="A"):
        """A reported hypothetical outcome conditional on external certificate flags."""
        if not isinstance(receipt, TransferReceipt):
            raise ValueError("Explicit custody receipt required")
        if not receipt.admissible:
            return None
        return self.predicted_joint_output(sequence, reader)

    def joint_closure(self):
        return closure({"A:turn": A_TURN, "B:shift": self.translated_b_action()})


def candidate_partition(words, reader="A"):
    """Classify hypotheses using ONLY proposed mixed-output words, not latent keys."""
    signatures = {}
    for permutation in all_alignments():
        bridge = ProposedBridge(permutation)
        signature = tuple(bridge.predicted_joint_output(w, reader) for w in words)
        signatures.setdefault(signature, []).append(permutation)
    return {key: tuple(value) for key, value in signatures.items()}


def transported_operator_signature(bridge):
    """Operational B action/readout on shared analyst domain; not native knowledge."""
    return bridge.translated_b_action(), bridge.translated_b_sensor()


def b_local_automorphism():
    """An unobservable B-local exchange preserving action, sensor and recipes."""
    h = B_SHIFT
    assert compose(h, B_SHIFT) == compose(B_SHIFT, h)
    assert tuple(B_SENSOR[h[i]] for i in range(N)) == B_SENSOR
    assert all(tuple(recipe[h[i]] for i in range(N)) == recipe
               for recipe in B_RECIPES.values())
    return h


def unrecoverable_pairs():
    h = b_local_automorphism()
    return tuple((p, compose(p, h)) for p in all_alignments() if p < compose(p, h))
