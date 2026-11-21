"""MQR 5.4, chat 43: representation versus acquisition in time-resolved readout.

A finite abstract electrode-channel toy, NOT empirical neural recordings or
an implementation of Nersessian's specific CAT analysis.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict


def validate(record):
    if not isinstance(record, (tuple, list)) or not record:
        raise ValueError('Nonempty sequence of time bins required')
    channels = len(record[0]) if isinstance(record[0], (tuple, list)) else 0
    if channels < 2:
        raise ValueError('At least two sensor channels required')
    for row in record:
        if (not isinstance(row, (tuple, list)) or len(row) != channels or
            any(type(x) is not int or x < 0 for x in row)):
            raise ValueError('Rectangular nonnegative integer event counts required')
    return channels


def channel_totals(record):
    n = validate(record)
    return tuple(sum(row[i] for row in record) for i in range(n))


def activity_center_trajectory(record, positions=None):
    n = validate(record)
    if positions is None:
        positions = tuple(range(n))
    if len(positions) != n:
        raise ValueError('A fixed position per sensor channel required')
    try:
        positions = tuple(Fraction(x) for x in positions)
    except (ValueError, TypeError, ZeroDivisionError) as exc:
        raise ValueError('Positions must be rational quantities') from exc
    trajectory = []
    for row in record:
        count = sum(row)
        trajectory.append(None if count == 0 else
                          sum((Fraction(counts)*position for counts, position
                               in zip(row, positions)), Fraction(0)) / count)
    return tuple(trajectory)


def one_hot_record(sequence, channels=4):
    if not sequence or channels < 2 or any(type(x) is not int or
        x not in range(channels) for x in sequence):
        raise ValueError('Expected nonempty sequence of valid channel indices')
    return tuple(tuple(int(i == hit) for i in range(channels)) for hit in sequence)


def finite_profile_census(channels=4, bins=4):
    if channels < 2 or bins < 1:
        raise ValueError('Invalid finite census domain')
    groups = defaultdict(int)
    for word in product(range(channels), repeat=bins):
        groups[channel_totals(one_hot_record(word, channels))] += 1
    return dict(
        raw_sequences=channels ** bins,
        summary_classes=len(groups),
        collided_pairs=sum(k*(k-1)//2 for k in groups.values()),
        largest_class=max(groups.values()),
    )


def old_profile_language_indistinguishable(left, right):
    """All functions of the released old summary agree iff summaries agree."""
    return channel_totals(left) == channel_totals(right)


def readout_status(raw_retained, time_resolved_acquisition):
    """A conditional epistemic label, not a verdict on a physical discovery."""
    if type(raw_retained) is not bool or type(time_resolved_acquisition) is not bool:
        raise ValueError('Explicit data provenance flags required')
    if raw_retained:
        return 'NEW_DERIVED_REPRESENTATION_NOT_NEW_BITS'
    if time_resolved_acquisition:
        return 'NEW_ACQUISITION_REQUIRED_AND_PROVIDED_AS_ASSUMPTION'
    return 'TRAJECTORY_UNRECOVERABLE_FROM_TOTALS'
