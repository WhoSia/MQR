"""Tests for finite measurement/representation distinction, not neural data."""
import unittest
from fractions import Fraction
from itertools import permutations
from temporal_representation_v54 import (
    channel_totals, activity_center_trajectory, one_hot_record,
    finite_profile_census, old_profile_language_indistinguishable,
    readout_status,
)


class TestTemporalRepresentation(unittest.TestCase):
    def test_equal_histogram_with_distinct_temporal_trajectory(self):
        left = one_hot_record((0, 1, 2, 3))
        right = one_hot_record((0, 2, 1, 3))
        self.assertEqual(channel_totals(left), (1, 1, 1, 1))
        self.assertTrue(old_profile_language_indistinguishable(left, right))
        self.assertNotEqual(activity_center_trajectory(left),
                            activity_center_trajectory(right))
        self.assertEqual(activity_center_trajectory(left),
                         tuple(map(Fraction, range(4))))

    def test_temporal_permutation_obstruction_to_histogram_only_definability(self):
        original = one_hot_record((0, 1, 2, 3))
        variants = [one_hot_record(perm) for perm in permutations(range(4))]
        self.assertEqual(len(variants), 24)
        self.assertEqual(len({channel_totals(v) for v in variants}), 1)
        self.assertEqual(len({activity_center_trajectory(v) for v in variants}), 24)
        self.assertTrue(all(old_profile_language_indistinguishable(original, v)
                            for v in variants))

    def test_finite_census_by_independent_combinatorics(self):
        counts = finite_profile_census()
        self.assertEqual(counts['raw_sequences'], 256)
        self.assertEqual(counts['summary_classes'], 35) # C(7,3)
        self.assertEqual(counts['collided_pairs'], 1230)
        self.assertEqual(counts['largest_class'], 24)

    def test_same_trajectory_different_micro_records(self):
        left = ((1, 0, 1), (0, 2, 0))
        right = ((0, 2, 0), (1, 0, 1))
        self.assertNotEqual(left, right)
        self.assertEqual(activity_center_trajectory(left),
                         activity_center_trajectory(right))
        self.assertEqual(activity_center_trajectory(left),
                         (Fraction(1), Fraction(1)))
        # A trajectory cannot uniquely reconstruct which channels fired.
        self.assertNotEqual(left[0], right[0])

    def test_empty_time_bin_is_explicitly_undefined(self):
        record = ((0, 0, 0), (0, 1, 0))
        self.assertEqual(activity_center_trajectory(record), (None, Fraction(1)))
        self.assertEqual(channel_totals(record), (0, 1, 0))

    def test_nonuniform_channel_geometry(self):
        record = ((1, 1, 0), (0, 1, 1))
        self.assertEqual(activity_center_trajectory(record, (0, 10, 100)),
                         (Fraction(5), Fraction(55)))

    def test_data_provenance_gates(self):
        self.assertEqual(readout_status(True, False),
                         'NEW_DERIVED_REPRESENTATION_NOT_NEW_BITS')
        self.assertEqual(readout_status(False, True),
                         'NEW_ACQUISITION_REQUIRED_AND_PROVIDED_AS_ASSUMPTION')
        self.assertEqual(readout_status(False, False),
                         'TRAJECTORY_UNRECOVERABLE_FROM_TOTALS')
        with self.assertRaises(ValueError):
            readout_status('yes', True)

    def test_reject_nonrectangular_negative_and_boolean_data(self):
        for record in ((), ((0, 1), (1,)), ((-1, 2),), ((True, 1),),
                       ((0,),), ((1, 1), (-1, 1))):
            with self.assertRaises(ValueError):
                channel_totals(record)
        with self.assertRaises(ValueError):
            activity_center_trajectory(((1, 0),), (0,))
        with self.assertRaises(ValueError):
            one_hot_record((0, 9))


if __name__ == '__main__':
    unittest.main()
