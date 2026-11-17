"""Design a drift-balanced comparison of two optical element orders."""

from fractions import Fraction


LINEAR_BLOCK = "ABBA"
QUADRATIC_BLOCK = "ABBABAAB"


def contrast(block: str, values) -> Fraction:
    """Difference of the condition means on a single matched block."""
    if set(block) != {"A", "B"} or len(block) != len(values):
        raise ValueError("provide one reading per A or B in a nonempty two-condition block")
    a = [Fraction(value) for label, value in zip(block, values) if label == "A"]
    b = [Fraction(value) for label, value in zip(block, values) if label == "B"]
    return sum(a) / len(a) - sum(b) / len(b)


def moment_imbalance(block: str, times, degree: int) -> Fraction:
    """Return the mean timestamp moment imbalance, using actual timestamps."""
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    return contrast(block, [Fraction(time) ** degree for time in times])


def optical_difference(
    parallel_transmission, orthogonal_transmission, mixing, *, vertical: bool
) -> Fraction:
    """Return A minus B. A is plate then polarizer, B the reverse order.

    Transmissions are intensity fractions, and the retarder is lossless.
    Mixing is the fraction of one input linear polarization transferred to
    the orthogonal component. The detector is polarization insensitive.
    """
    t_parallel, t_perpendicular, q = map(
        Fraction, (parallel_transmission, orthogonal_transmission, mixing)
    )
    if not 0 <= t_perpendicular <= t_parallel <= 1 or not 0 <= q <= 1:
        raise ValueError("transmissions and mixing must be within their physical ranges")
    difference = q * (t_parallel - t_perpendicular)
    return difference if vertical else -difference
