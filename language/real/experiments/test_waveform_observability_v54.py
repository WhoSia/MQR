"""Exact witnesses for the RMS and transition-time questions in MQR 5.4."""

from fractions import Fraction
import unittest


def transition_mean_square(coefficients):
    """Integrate the square of a polynomial over normalized time [0, 1]."""
    return sum(
        Fraction(a * b, left + right + 1)
        for left, a in enumerate(coefficients)
        for right, b in enumerate(coefficients)
    )


def read_transition(coefficients, time):
    return sum(coefficient * time**power for power, coefficient in enumerate(coefficients))


class WaveformObservabilityTests(unittest.TestCase):
    def test_complete_plateau_agreement_does_not_fix_period_rms(self):
        linear = (-1, 2)
        cubic = (-1, 6, -12, 8)
        transition_fraction = Fraction(3, 100)
        scores = []
        for ramp in (linear, cubic):
            self.assertEqual((read_transition(ramp, 0), read_transition(ramp, 1)), (-1, 1))
            scores.append(1 - transition_fraction + transition_fraction * transition_mean_square(ramp))
        self.assertEqual(scores, [Fraction(49, 50), Fraction(341, 350)])
        self.assertEqual(scores[0] - scores[1], Fraction(1, 175))

    def test_equal_rms_still_leaves_a_transition_time_disagreement(self):
        late = (-1, 0, 2)
        early = (-1, 4, -2)
        for ramp in (late, early):
            self.assertEqual((read_transition(ramp, 0), read_transition(ramp, 1)), (-1, 1))
            self.assertEqual(transition_mean_square(ramp), Fraction(7, 15))
        self.assertEqual(read_transition(late, Fraction(1, 2)), Fraction(-1, 2))
        self.assertEqual(read_transition(early, Fraction(1, 2)), Fraction(1, 2))
