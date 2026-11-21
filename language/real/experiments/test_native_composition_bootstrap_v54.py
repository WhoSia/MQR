"""MQR 43 exact finite receipts for native action-language bridge claims."""
import unittest
from fractions import Fraction
from itertools import product
from native_composition_bootstrap_v54 import (
    A_SENSOR, A_TURN, B_SHIFT, ProposedBridge, TransferReceipt,
    all_alignments, b_local_automorphism, candidate_partition, closure,
    compose, transported_operator_signature, unrecoverable_pairs,
)


class TestNativeBridge(unittest.TestCase):
    def test_native_only_traces_cannot_identify_alignment(self):
        bridges = [ProposedBridge(p) for p in all_alignments()]
        for n in range(6):
            a_word = ('A:turn',) * n
            b_word = ('B:shift',) * n
            self.assertEqual(len({x.native_a(a_word) for x in bridges}), 1)
            for b_recipe in ('B:clear', 'B:mixed'):
                self.assertEqual(len({tuple(sorted(x.native_b(b_word, b_recipe).items()))
                                      for x in bridges}), 1)
        self.assertEqual(bridges[0].native_b(recipe='B:mixed'),
                         {'x': Fraction(0), 'y': Fraction(1)})

    def test_composition_creates_A_observable_unreachable_locally(self):
        x = ProposedBridge((0, 1, 2))
        self.assertEqual(x.native_a(()), 'low')
        self.assertEqual(x.native_a(('A:turn',)), 'low')
        self.assertEqual(x.predicted_joint_output(('A:turn', 'B:shift')), 'high')
        self.assertEqual(x.predicted_joint_output(('B:shift', 'A:turn')), 'low')
        self.assertEqual(len(closure({'A:turn': A_TURN})), 2)
        self.assertEqual(len(x.joint_closure()), 6)
        self.assertNotIn(compose(x.translated_b_action(), A_TURN),
                         closure({'A:turn': A_TURN}))
        self.assertNotIn(compose(x.translated_b_action(), A_TURN),
                         closure({'B:shift': x.translated_b_action()}))

    def test_no_shared_dictionary_and_no_bridge_certify_are_distinct(self):
        x = ProposedBridge((0, 1, 2))
        good = TransferReceipt(True, True, True)
        for flags in product((False, True), repeat=3):
            receipt = TransferReceipt(*flags)
            actual = x.warranted_output(('A:turn', 'B:shift'), receipt)
            self.assertEqual(actual, 'high' if all(flags) else None)
        self.assertEqual(x.warranted_output(('B:shift', 'A:turn'), good), 'low')
        self.assertRaises(ValueError, x.warranted_output, ('A:turn',), None)

    def test_two_cross_queries_leave_three_size_two_alignment_classes(self):
        words = (('A:turn', 'B:shift'), ('B:shift', 'A:turn'))
        cells = candidate_partition(words)
        self.assertEqual(len(cells), 3)
        self.assertEqual(sorted(map(len, cells.values())), [2, 2, 2])
        self.assertEqual(set(cells), {('high', 'low'), ('low', 'high'), ('low', 'low')})
        self.assertEqual(len(candidate_partition(words[:1])), 2)

    def test_residual_B_automorphism_is_exact_operational_symmetry(self):
        self.assertEqual(b_local_automorphism(), B_SHIFT)
        pairs = unrecoverable_pairs()
        self.assertEqual(len(pairs), 3)
        for p, q in pairs:
            a, b = ProposedBridge(p), ProposedBridge(q)
            self.assertEqual(transported_operator_signature(a),
                             transported_operator_signature(b))
            for width in range(6):
                for word in product(('A:turn', 'B:shift'), repeat=width):
                    for reader in ('A', 'B'):
                        self.assertEqual(a.predicted_joint_output(word, reader),
                                         b.predicted_joint_output(word, reader))

    def test_unknown_alignment_changes_cross_laboratory_prediction(self):
        x = ProposedBridge((0, 1, 2))
        y = ProposedBridge((1, 0, 2))
        for sequence in (('A:turn', 'B:shift'), ('B:shift', 'A:turn')):
            self.assertNotEqual(x.predicted_joint_output(sequence),
                                y.predicted_joint_output(sequence))
        self.assertEqual(x.native_a(('A:turn',)), y.native_a(('A:turn',)))
        self.assertEqual(x.native_b(('B:shift',)), y.native_b(('B:shift',)))

    def test_nonproductive_alignment_control(self):
        x = ProposedBridge((2, 0, 1))
        self.assertEqual(x.translated_b_action(), A_TURN)
        self.assertEqual(len(x.joint_closure()), 2)
        self.assertEqual(x.predicted_joint_output(('A:turn', 'B:shift')), 'low')
        self.assertEqual(x.predicted_joint_output(('B:shift', 'A:turn')), 'low')

    def test_invalid_input_rejected(self):
        for bad in ((0, 0, 2), (0, 1), (0, 1, 3)):
            self.assertRaises(ValueError, ProposedBridge, bad)
        x = ProposedBridge((0, 1, 2))
        self.assertRaises(ValueError, x.native_a, ('B:shift',))
        self.assertRaises(ValueError, x.native_b, ('A:turn',))
        self.assertRaises(ValueError, x.predicted_joint_output, ('C:unknown',))
        self.assertRaises(ValueError, x.predicted_joint_output, (), 'C')


if __name__ == '__main__':
    unittest.main()
