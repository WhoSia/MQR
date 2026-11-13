"""Verify a task-specific calibration transfer example with exact arithmetic."""

from fractions import Fraction


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def apply(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def main():
    # B's forward map, expressed in the coordinates of A's corrected output.
    response_b = (
        (1, 0, Fraction(2, 25)),
        (0, 1, Fraction(1, 25)),
        (0, 0, 1),
    )
    probes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    contrast = (1, -2, 0)
    second_band = (0, 1, 0)

    assert all(apply(response_b, probe) == probe for probe in probes[:2])
    errors = tuple(
        tuple(observed - expected for observed, expected in zip(
            apply(response_b, probe), probe, strict=True
        ))
        for probe in probes
    )
    assert errors[2] == (Fraction(2, 25), Fraction(1, 25), 0)
    assert all(dot(contrast, error) == 0 for error in errors)
    assert dot(second_band, errors[2]) == Fraction(1, 25)
    print("Old probes: no change. Third probe: channel errors", errors[2])
    print("Contrast bias: 0. Second-band bias on the third probe: 1/25.")


if __name__ == "__main__":
    main()
