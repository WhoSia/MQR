"""Exact toy of a polarization observation outside a single-wavelength context.

Finite phase alphabet {0, pi/2, pi, 3pi/2}; unitary diagonal Jones
matrices diag(1, i**k). Not a physical dispersion-fit or device design.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class RetarderHypothesis:
    name: str
    phase_quarters: tuple[tuple[str, int], ...]

    def __post_init__(self):
        names = [label for label, _ in self.phase_quarters]
        if not self.name or not names or len(set(names)) != len(names) or any(not x for x in names):
            raise ValueError("Unique nonempty labels are required")
        if any(not isinstance(q, int) or q not in (0,1,2,3) for _,q in self.phase_quarters):
            raise ValueError("Quarter-turn phase must be an integer from zero to three")

    def _phase(self, wavelength: str) -> int:
        for label, phase in self.phase_quarters:
            if label == wavelength:
                return phase
        raise ValueError("Wavelength not declared")

    def jones_diagonal(self, wavelength: str) -> tuple[complex, complex]:
        return 1+0j, (1j)**self._phase(wavelength)

    def total_intensity(self, wavelength: str) -> Fraction:
        self._phase(wavelength)
        return Fraction(1)

    def analyzer_45_intensity(self, wavelength: str) -> Fraction:
        """For normalized 45-degree input and 45-degree projection."""
        cos_quarters = (1, 0, -1, 0)
        return Fraction(1 + cos_quarters[self._phase(wavelength)], 2)


def first_discriminating_wavelength(a: RetarderHypothesis,
                                   b: RetarderHypothesis,
                                   wavelengths: tuple[str,...],
                                   readout: str = "analyzer_45") -> str | None:
    if len(wavelengths) != len(set(wavelengths)):
        raise ValueError("Repeated wavelength")
    if readout not in ("analyzer_45", "total"):
        raise ValueError("Unknown readout")
    for wavelength in wavelengths:
        if readout == "total":
            av,bv = a.total_intensity(wavelength),b.total_intensity(wavelength)
        else:
            av,bv = a.analyzer_45_intensity(wavelength),b.analyzer_45_intensity(wavelength)
        if av != bv:
            return wavelength
    return None
