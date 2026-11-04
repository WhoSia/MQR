"""Constructed identifiability witnesses for MQR 5.3 R35; no historical data."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ChannelChanges:
    liquid: float
    vapor: float

    def observed_contrast(self, gain: float = 1.0) -> float:
        if gain <= 0:
            raise ValueError("gain must be strictly positive")
        return gain * (self.liquid - self.vapor)


def equivalent_witnesses(d: float, free_parameter: float = 0.0) -> tuple[ChannelChanges, ChannelChanges]:
    """Two distinct narratives compatible with observed contrast D/a=d."""
    return ChannelChanges(d, 0.0), ChannelChanges(d + free_parameter, free_parameter)


def sign_of_relative_change(contrast: float) -> int:
    return (contrast > 0) - (contrast < 0)


def observed_with_offset_drift(changes: ChannelChanges, gain: float, offset_drift_liquid: float, offset_drift_vapor: float) -> float:
    return changes.observed_contrast(gain) + offset_drift_liquid - offset_drift_vapor
