"""Scope-restricted test for evidence custody and adversarial rival predictions."""
import unittest
from itertools import permutations, product
from open_world_anomaly_v54 import (
    A_SENSOR, B_SWAP, B_CYCLE, ClaimedReceipt, ReportedTrial,
    AnomalyRegister, frozen_predictions, native_predict, rival_outputs,
    prospective_discriminant,
)

GOOD = ClaimedReceipt(True, True, True, True)
WORD = ('B:shift', 'B:shift')
CONTROL = ('A:turn',)


def trial(i, lineage, word=WORD, observed='high', control='low', receipt=GOOD):
    return ReportedTrial(i, lineage, tuple(word), observed, control, receipt)


class TestOpenWorldAnomaly(unittest.TestCase):
    def test_two_B_operations_produce_low_for_all_six_frozen_alignments(self):
        self.assertEqual(frozen_predictions(WORD), frozenset({'low'}))
        for p in permutations(range(3)):
            self.assertEqual(native_predict(WORD, alignment=p), 'low')

    def test_constructed_new_operator_changes_prediction_on_same_word(self):
        self.assertEqual(native_predict(WORD, B_SWAP), 'low')
        self.assertEqual(native_predict(WORD, B_CYCLE), 'high')
        self.assertEqual(native_predict(CONTROL, B_CYCLE), 'low')

    def test_report_preserves_anomaly_without_updating_model(self):
        log = AnomalyRegister()
        self.assertEqual(log.add(trial('t1','lab_a')),
                         'MODEL_CLASS_MISMATCH_RECORDED')
        self.assertEqual(log.assess(WORD), 'HOLD_SINGLE_DECLARED_LINEAGE')
        self.assertEqual(frozen_predictions(WORD), frozenset({'low'}))
        self.assertEqual(len(log.reports), 1)

    def test_two_distinct_claimed_lineages_are_still_conditional_hold(self):
        log = AnomalyRegister()
        log.add(trial('t1','lab_a'))
        log.add(trial('t2','lab_b'))
        self.assertEqual(log.assess(WORD),
                         'HOLD_CONDITIONAL_FROZEN_CLASS_REFUTATION')

    def test_repeated_same_lineage_does_not_masquerade_as_independence(self):
        log = AnomalyRegister()
        for i in range(5):
            log.add(trial('repeat_'+str(i), 'same_lab'))
        self.assertEqual(log.assess(WORD), 'HOLD_SINGLE_DECLARED_LINEAGE')

    def test_failed_provenance_is_recorded_but_not_used(self):
        for flags in product((False, True), repeat=4):
            if all(flags):
                continue
            log = AnomalyRegister()
            result = log.add(trial('t1', 'A', receipt=ClaimedReceipt(*flags)))
            self.assertEqual(result, 'QUARANTINED_DECLARED_GATE_FAILED')
            self.assertEqual(log.assess(WORD), 'HOLD_NO_QUALIFYING_REPORTS')
            self.assertEqual(len(log.reports), 1)

    def test_negative_control_excludes_globally_inverted_sensor_but_no_ontology(self):
        log = AnomalyRegister()
        log.add(trial('t1','A',control='high'))
        log.add(trial('t2','B',control='high'))
        self.assertEqual(log.assess(WORD), 'HOLD_NO_QUALIFYING_REPORTS')
        self.assertEqual(rival_outputs(CONTROL)['global_sensor_inversion'], 'high')
        self.assertEqual(rival_outputs(CONTROL)['three_cycle'], 'low')

    def test_conflicting_native_readouts_block_simple_refutation(self):
        log = AnomalyRegister()
        log.add(trial('t1','A',observed='high'))
        log.add(trial('t2','B',observed='low'))
        self.assertEqual(log.assess(WORD), 'HOLD_INCONSISTENT_RESULTS')

    def test_duplicate_trial_id_does_not_change_state(self):
        log = AnomalyRegister()
        log.add(trial('t1','A'))
        before = log.reports
        with self.assertRaises(ValueError):
            log.add(trial('t1','B'))
        self.assertEqual(log.reports, before)
        self.assertEqual(log.assess(WORD), 'HOLD_SINGLE_DECLARED_LINEAGE')

    def test_native_but_frozen_compatible_result_does_not_indicate_anomaly(self):
        log = AnomalyRegister()
        self.assertEqual(log.add(trial('t1','A',observed='low')),
                         'FROZEN_MODEL_COMPATIBLE')
        self.assertEqual(log.assess(WORD), 'HOLD_COMPATIBLE_WITH_FROZEN_MODEL')

    def test_prospective_untrained_five_shift_word_separates_some_rivals(self):
        word = ('B:shift',)*5
        self.assertEqual(rival_outputs(word)['old_involution'], 'low')
        self.assertEqual(rival_outputs(word)['three_cycle'], 'high')
        self.assertIn(('old_involution','three_cycle'), prospective_discriminant(word))

    def test_query_dependent_sensor_artifact_is_observationally_indistinguishable(self):
        for length in range(7):
            for word in product(('A:turn','B:shift'), repeat=length):
                results = rival_outputs(word)
                self.assertEqual(results['three_cycle'],
                                 results['query_dependent_sensor_artifact'])
        self.assertNotIn(('query_dependent_sensor_artifact','three_cycle'),
                         prospective_discriminant(WORD))

    def test_bad_reports_rejected_before_mutation(self):
        log = AnomalyRegister()
        with self.assertRaises(ValueError):
            log.add('not_a_report')
        for kwargs in ({'i': '', 'lineage': 'A'},
                       {'i': 't1', 'lineage': ''},
                       {'i': 't1', 'lineage': 'A', 'word': ('OTHER',)},
                       {'i': 't1', 'lineage': 'A', 'observed': 'Z'},
                       {'i': 't1', 'lineage': 'A', 'control': 'Z'}):
            with self.assertRaises(ValueError):
                log.add(trial(**kwargs))
        with self.assertRaises(ValueError):
            ClaimedReceipt(1,True,True,True)
        self.assertEqual(len(log.reports), 0)


if __name__=='__main__':
    unittest.main()
