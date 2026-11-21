"""Native learner oracle isolation, control gates and held-out model predictions."""
import unittest
from native_bridge_active_learner_v54 import FrozenOracle, NativeLearner
from native_bridge_query_design_v54 import Probe
from native_composition_bootstrap_v54 import (
    ProposedBridge, TransferReceipt, all_alignments,
)


def oracle(p, exposed):
    return FrozenOracle(ProposedBridge(p), TransferReceipt(True, True, True), exposed)


class TestActiveLearner(unittest.TestCase):
    def test_all_six_blind_sensor_worlds_finish_at_two_residual_hypotheses(self):
        for p in all_alignments():
            learner = NativeLearner(False)
            history = learner.learn(oracle(p, False))
            self.assertEqual(learner.candidate_count, 2)
            self.assertLessEqual(len(history), 2)
            self.assertNotIn('alignment', repr(history))
            heldout = Probe(('B:shift', 'A:turn', 'B:shift'), 'A')
            self.assertEqual(learner.simulated_heldout_check(oracle(p, False), heldout),
                             'PASS_SIMULATOR')

    def test_all_six_visible_sensor_worlds_finish_at_two_residual_hypotheses(self):
        for p in all_alignments():
            learner = NativeLearner(True)
            history = learner.learn(oracle(p, True))
            self.assertEqual(learner.candidate_count, 2)
            self.assertLessEqual(len(history), 2)
            self.assertEqual(learner.simulated_heldout_check(
                oracle(p, True), Probe(('B:shift', 'A:turn', 'B:shift'), 'A')),
                'PASS_SIMULATOR')

    def test_first_query_is_independent_of_the_hidden_actual_alignment(self):
        first = NativeLearner(False).choose()
        self.assertEqual(first, Probe(('B:shift',), 'A'))
        self.assertEqual(NativeLearner(True).choose(), Probe((), 'B'))
        for p in all_alignments():
            learner = NativeLearner(False)
            self.assertEqual(learner.choose(), first)
            learner.record(first, oracle(p, False).ask(first))
            self.assertEqual(learner.candidate_count, 2 if p in ((1, 0, 2), (1, 2, 0)) else 4)

    def test_invalid_unexpected_outcome_is_transactional(self):
        learner = NativeLearner(False)
        first = learner.choose()
        with self.assertRaises(ValueError):
            learner.record(first, 'NOT_A_NATIVE_SENSOR_OUTPUT')
        self.assertEqual(learner.candidate_count, 6)
        self.assertEqual(learner.ledger, [])
        learner.record(first, 'low')
        with self.assertRaises(ValueError):
            learner.record(first, 'low')
        self.assertEqual(learner.candidate_count, 4)
        self.assertEqual(len(learner.ledger), 1)

    def test_fail_closed_if_custody_or_reset_missing(self):
        for flags in ((False, True, True), (True, False, True), (True, True, False)):
            blocked = FrozenOracle(ProposedBridge((0, 1, 2)), TransferReceipt(*flags), False)
            learner = NativeLearner(False)
            with self.assertRaises(RuntimeError):
                learner.learn(blocked)
            self.assertEqual(learner.candidate_count, 6)
            self.assertEqual(learner.ledger, [])
            with self.assertRaises(RuntimeError):
                blocked.ask(Probe(('B:shift',), 'A'))

    def test_native_valid_but_model_impossible_output_rejects_without_mutation(self):
        learner = NativeLearner(False)
        probe = Probe(('A:turn',), 'A')
        # A-native 'high' is a valid sensor symbol but impossible for every
        # frozen candidate under this A-only protocol.
        with self.assertRaises(ValueError):
            learner.record(probe, 'high')
        self.assertEqual(learner.candidate_count, 6)
        self.assertEqual(learner.ledger, [])

    def test_sensor_exposure_mismatch_is_not_silently_reinterpreted(self):
        learner = NativeLearner(False)
        with self.assertRaises(ValueError):
            learner.learn(oracle((0, 1, 2), True))
        self.assertEqual(learner.candidate_count, 6)
        self.assertEqual(learner.ledger, [])

    def test_heldout_query_must_not_be_reused(self):
        learner = NativeLearner(False)
        learner.learn(oracle((0, 1, 2), False))
        query = Probe(tuple(learner.ledger[0]['word']), learner.ledger[0]['reader'])
        with self.assertRaises(ValueError):
            learner.heldout_prediction(query)


if __name__ == '__main__':
    unittest.main()
