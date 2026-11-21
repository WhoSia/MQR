"""Exact rational comparison of Galilean and Lorentz event separations.

This verifies standard special-relativity algebra. It is not a physical
experiment, theorem discovery, or evidence for historical interpretive claims.
Set c=1 by choice of units. Provide rational v and rational gamma satisfying
gamma^2(1-v^2)=1; this restricts the examples but prevents rounding error.
"""
from fractions import Fraction


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError('Exact integer or Fraction inputs only, no floats')
    return Fraction(value)


def validate_boost(v, gamma):
    v, gamma = rational(v), rational(gamma)
    if abs(v) >= 1 or gamma < 1 or gamma * gamma * (1 - v * v) != 1:
        raise ValueError('Require |v|<1 and positive exact Lorentz factor')
    return v, gamma


def lorentz(dt, dx, v, gamma):
    """Event separation, 1+1 spacetime, c=1 and standard synchronization."""
    dt, dx = rational(dt), rational(dx)
    v, gamma = validate_boost(v, gamma)
    return gamma * (dt - v * dx), gamma * (dx - v * dt)


def galilean(dt, dx, v):
    dt, dx, v = rational(dt), rational(dx), rational(v)
    return dt, dx - v * dt


def interval_sq(dt, dx):
    dt, dx = rational(dt), rational(dx)
    return dt * dt - dx * dx


def separation_type(dt, dx):
    s2 = interval_sq(dt, dx)
    return 'timelike' if s2 > 0 else ('spacelike' if s2 < 0 else 'null')


def all_verified_examples():
    """Small, explicit rational fixtures—not an exhaustive set of boosts."""
    boosts = ((Fraction(3, 5), Fraction(5, 4)),
              (Fraction(-3, 5), Fraction(5, 4)),
              (Fraction(4, 5), Fraction(5, 3)),
              (Fraction(5, 13), Fraction(13, 12)))
    separations = ((0, 1), (3, 5), (5, 3), (1, 1), (-5, 3))
    for v, gamma in boosts:
        for dt, dx in separations:
            t2, x2 = lorentz(dt, dx, v, gamma)
            if interval_sq(dt, dx) != interval_sq(t2, x2):
                raise AssertionError('Invariant did not survive boost')
            yield {'initial': (str(dt), str(dx)),
                   'boost': (str(v), str(gamma)),
                   'transformed': (str(t2), str(x2)),
                   'causal_class': separation_type(dt, dx)}


if __name__ == '__main__':
    import json
    print(json.dumps(list(all_verified_examples()), ensure_ascii=False, indent=2))
