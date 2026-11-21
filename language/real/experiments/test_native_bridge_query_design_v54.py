"""MQR 43 finite design-regression checks for passive/active protocols."""
import unittest
from itertools import product
from native_bridge_query_design_v54 import (
    Probe, classes, predict, optimal_basis, candidate_probes,
)
from native_composition_bootstrap_v54 import ProposedBridge, all_alignments


class TestQueryDesign(unittest.TestCase):
    def test_passive_B_readouts_alone_identify_three_operational_classes(self):
        passive = (Probe((), 'B'), Probe(('A:turn',), 'B'))
        self.assertEqual(len(classes(passive)), 3)
        self.assertEqual(sorted(map(len, classes(passive).values())), [2, 2, 2])
        self.assertEqual(sum(p.primitive_cost for p in passive), 1)
        self.assertEqual(optimal_basis(b_sensor_visible=True), passive)

    def test_passive_shortcut_is_removed_by_constant_B_sensor(self):
        passive = (Probe((), 'B'), Probe(('A:turn',), 'B'))
        self.assertEqual(len(classes(passive, b_sensor_visible=False)), 1)
        for align in all_alignments():
            model = ProposedBridge(align)
            self.assertEqual(predict(model, Probe(('A:turn',), 'B'), False), 'opaque')

    def test_active_composition_still_splits_classes_with_blind_B_sensor(self):
        active = (Probe(('B:shift',), 'A'), Probe(('A:turn', 'B:shift'), 'A'))
        results = classes(active, b_sensor_visible=False)
        self.assertEqual(len(results), 3)
        self.assertEqual(sorted(map(len, results.values())), [2, 2, 2])
        self.assertEqual(set(results), {('low', 'high'), ('high', 'low'), ('low', 'low')})
        self.assertEqual(optimal_basis(False), active)
        self.assertEqual(optimal_basis(False, allow_b=False), active)
        self.assertEqual(sum(p.primitive_cost for p in active), 3)

    def test_no_single_binary_A_query_can_resolve_three_classes(self):
        for p in candidate_probes(4, allow_b=False):
            self.assertLessEqual(len(classes((p,), False)), 2)
        best = optimal_basis(False, allow_b=False, max_word_length=1)
        self.assertIsNone(best)

    def test_explicit_exhaustion_no_two_A_probes_cost_below_three(self):
        # Every A-only pair with cost 0,1,2 fails to split all three classes.
        probes = candidate_probes(2, allow_b=False)
        for i, p in enumerate(probes):
            for q in probes[i + 1:]:
                if p.primitive_cost + q.primitive_cost < 3:
                    self.assertLess(len(classes((p, q), False)), 3)

    def test_symmetry_remains_under_all_short_combined_probes(self):
        all_probes = candidate_probes(3, allow_a=True, allow_b=True)
        for p in all_probes:
            self.assertLessEqual(len(classes((p,), True)), 3)
            self.assertLessEqual(len(classes((p,), False)), 3)

    def test_invalid_probes_fail_closed(self):
        self.assertRaises(ValueError, Probe, ('C:bad',), 'A')
        self.assertRaises(ValueError, Probe, (), 'Q')
        self.assertRaises(ValueError, candidate_probes, -1)
        self.assertRaises(ValueError, candidate_probes, 2, False, False)


if __name__ == '__main__':
    unittest.main()
