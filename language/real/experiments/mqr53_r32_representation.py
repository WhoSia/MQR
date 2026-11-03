"""MQR-5.3 R32: representation and calibration mechanisms (synthetic examples).

No historical physical measurements are represented here.
"""
from __future__ import annotations
from itertools import product
from math import log2, sqrt


def parity(a: int, b: int) -> int:
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError("Binary inputs required")
    return a ^ b


def best_affine_parity_accuracy(*, enriched: bool = False) -> float:
    """Finite check of an affine threshold family on a uniform XOR truth table.

    Coefficients and intercept range over {-2,-1,0,1,2}.  This finite
    search is a regression witness, not a proof over all real parameters.
    The paper note contains the algebraic impossibility proof.
    """
    cases = tuple(product((0, 1), repeat=2))
    best = 0.0
    dimensions = 4 if enriched else 3
    for coefficients in product(range(-2, 3), repeat=dimensions):
        predictions = []
        for a, b in cases:
            features = (1, a, b, a ^ b) if enriched else (1, a, b)
            score = sum(c * f for c, f in zip(coefficients, features))
            predictions.append(int(score >= 0))
        accuracy = sum(p == (a ^ b) for p, (a, b) in zip(predictions, cases)) / 4
        best = max(best, accuracy)
    return best


def binary_entropy(p: float) -> float:
    if not 0 <= p <= 1:
        raise ValueError("Probability must be in [0,1]")
    if p in (0, 1):
        return 0.0
    return -p * log2(p) - (1 - p) * log2(1 - p)


def new_sensor_mutual_information(error_rate: float) -> float:
    """I(W; A,C) in bits, W=A XOR B, C=B XOR E, fair independent A,B.

    E is independent Bernoulli(error_rate); the observation A alone is
    independent of W.  A,C are *new physical observations*, not a
    deterministic re-encoding of A alone.
    """
    if not 0 <= error_rate <= 0.5:
        raise ValueError("Require calibrated error rate in [0,1/2]")
    return 1 - binary_entropy(error_rate)


def independent_sensor_disagreement(error_rate: float) -> float:
    """P(C1 != C2) given Cj=B XOR Ej and iid Bernoulli errors."""
    if not 0 <= error_rate <= 0.5:
        raise ValueError("Require error rate in [0,1/2]")
    return 2 * error_rate * (1 - error_rate)


def infer_independent_error_rate(disagreement_rate: float) -> float:
    """Invert disagreement assuming *independent identical* sensor errors.

    It is intentionally not valid under shared latent error.
    """
    if not 0 <= disagreement_rate <= 0.5:
        raise ValueError("Disagreement probability outside model range")
    return (1 - sqrt(1 - 2 * disagreement_rate)) / 2


def shared_error_disagreement(error_rate: float) -> float:
    """C1=C2=B XOR E with one shared error E: zero disagreement at all rates."""
    if not 0 <= error_rate <= 0.5:
        raise ValueError("Require error rate in [0,1/2]")
    return 0.0


def fair_latent_observable_joint(*, shared_error_rate: float) -> dict[tuple[int, int], float]:
    """Observed joint P(C1,C2) under a fair hidden B and one shared error.

    Same joint as two perfect sensors: {(0,0):1/2, (1,1):1/2}.
    This does not claim the joint with *observed B* is identical.
    """
    if not 0 <= shared_error_rate <= 0.5:
        raise ValueError("Require error rate in [0,1/2]")
    return {(0, 0): 0.5, (1, 1): 0.5, (0, 1): 0.0, (1, 0): 0.0}
