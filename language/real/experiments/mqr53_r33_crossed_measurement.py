"""MQR-5.3 R33: crossed preparation/detector structural counterexample.

Only deterministic model means are treated; replicates and noise matter in practice.
"""
from __future__ import annotations
from dataclasses import dataclass


Matrix2 = tuple[tuple[float, float], tuple[float, float]]


@dataclass(frozen=True)
class CrossedMeasurement:
    """Two preparation routes × two detectors, additive shared/relative biases."""
    measurand: float
    global_bias: float
    preparation_bias: tuple[float, float]
    detector_bias: tuple[float, float]
    interaction: float = 0.0

    def expected_readings(self) -> Matrix2:
        # Interaction is a +/- checkerboard perturbation of amplitude kappa.
        s = (-1.0, 1.0)
        return tuple(
            tuple(
                self.measurand + self.global_bias
                + self.preparation_bias[i] + self.detector_bias[j]
                + self.interaction * s[i] * s[j]
                for j in range(2)
            )
            for i in range(2)
        )


@dataclass(frozen=True)
class Contrasts:
    mean: float
    preparation_difference: float
    detector_difference: float
    interaction_difference: float


def contrasts(y: Matrix2) -> Contrasts:
    a, b = y[0]
    c, d = y[1]
    return Contrasts(
        mean=(a + b + c + d) / 4,
        preparation_difference=(a + b - c - d) / 2,
        detector_difference=(a + c - b - d) / 2,
        interaction_difference=a - b - c + d,
    )


def gauge_shift(model: CrossedMeasurement, amount: float) -> CrossedMeasurement:
    """An observationally invisible shift: theta->theta+t, g->g-t."""
    return CrossedMeasurement(
        measurand=model.measurand + amount,
        global_bias=model.global_bias - amount,
        preparation_bias=model.preparation_bias,
        detector_bias=model.detector_bias,
        interaction=model.interaction,
    )


def reference_adjusted_measurand(mean: float, known_global_bias: float) -> float:
    """Only valid after independent zero-centering of both relative effects."""
    return mean - known_global_bias
