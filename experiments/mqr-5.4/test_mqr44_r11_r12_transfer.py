"""Independent regression checks for MQR44 R11/R12, stdlib unittest only."""
import unittest
from fractions import Fraction as Q
import mqr44_r11_cross_field_transfer_gate as gate
import mqr44_r12_frozen_bridge_transport as transfer

class ScientificTransferRegressions(unittest.TestCase):
    def test_each_original_distribution_normalized(self):
        for d in ('aligned','anti','independent'):
            self.assertEqual(sum(gate.joint(d).values()),1)

    def test_pass_is_target_relative(self):
        self.assertEqual(gate.profile(gate.joint('independent'),lambda s:s[0]),('PASS','FAIL'))
        self.assertEqual(gate.profile(gate.joint('independent'),lambda s:s[1]),('FAIL','PASS'))

    def test_refitting_is_not_transport(self):
        # Under an anti-correlated target, in-domain refitting can succeed,
        # but the frozen identity mapping learned in the source fails entirely.
        self.assertEqual(gate.acc(gate.joint('anti'),lambda s:s[0],1),1)
        self.assertEqual(transfer.accuracy('anti',lambda s:s[0]),0)

    def test_equal_marginals_do_not_license_pairing(self):
        for d in ('aligned','anti','independent'):
            self.assertEqual(gate.cond_prob(gate.joint(d),lambda s:s[0]==0),Q(1,2))
            self.assertEqual(gate.cond_prob(gate.joint(d),lambda s:s[1]==0),Q(1,2))
        self.assertEqual(gate.cond_prob(gate.joint('aligned'),lambda s:s[0]==s[1]),1)
        self.assertEqual(gate.cond_prob(gate.joint('anti'),lambda s:s[0]==s[1]),0)

    def test_independent_source_task_survives(self):
        for d in ('aligned','anti','independent'):
            self.assertEqual(transfer.accuracy(d,lambda s:s[0],target=0),1)

    def test_external_evidence_is_not_populated(self):
        self.assertEqual(len(gate.STATES),4)
        self.assertEqual(len(transfer.S),4)

if __name__=='__main__':
    unittest.main(verbosity=2)
