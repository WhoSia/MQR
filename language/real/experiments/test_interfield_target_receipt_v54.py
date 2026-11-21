"""Regression suite for interfield target receipts, no external factual witnesses."""
import unittest
from dataclasses import replace
from interfield_target_receipt_v54 import EvidenceReceipt, Claim, assess

def make(**kw):
    base=dict(receipt_id="r1",target="NMR_Q_RDC",source_kind="PUBLISHED_SUMMARY",
              source_id="Rinaldelli2014:Table1",specimen_id="1EXR",
              regime_id="PUBLISHED_REFINEMENT",lineage_id="paper:2014",
              original_scope_retained=True,paired_target_verified=False,
              calibration_verified=False,independently_replayed=False,
              reported_pass=True)
    base.update(kw)
    return EvidenceReceipt(**base)

CLAIM=Claim("nmr_fit_1exr","NMR_Q_RDC","1EXR","PUBLISHED_REFINEMENT",("paper:2014",))

class TestInterfieldEvidence(unittest.TestCase):
    def test_absent_claim_evidence(self):
        self.assertEqual(assess(CLAIM,()),"HOLD_TARGET_RECEIPT_ABSENT")
    def test_wrong_protein_not_matching(self):
        self.assertEqual(assess(CLAIM,(make(specimen_id="1IGD"),)),"HOLD_TARGET_RECEIPT_ABSENT")
    def test_cross_target_leakage_blocked(self):
        self.assertEqual(assess(CLAIM,(make(target="X_RAY_R_FREE"),)),"HOLD_TARGET_RECEIPT_ABSENT")
    def test_reported_table_lacks_sample_pairing(self):
        self.assertEqual(assess(CLAIM,(make(),)),"HOLD_PHYSICAL_PAIRING_UNVERIFIED")
    def test_calibration_required(self):
        self.assertEqual(assess(CLAIM,(make(paired_target_verified=True),)),"HOLD_CALIBRATION_UNVERIFIED")
    def test_published_no_replay(self):
        self.assertEqual(assess(CLAIM,(make(paired_target_verified=True,calibration_verified=True),)),
                         "PUBLISHED_COMPATIBILITY_NOT_REPLAYED")
    def test_raw_input_not_mislabeled_as_published_or_replayed(self):
        r=make(source_kind="SOURCE_RAW",paired_target_verified=True,calibration_verified=True)
        self.assertEqual(assess(CLAIM,(r,)),"RAW_SOURCE_BYTES_CLAIMED_NOT_REPLAYED")

    def test_preservation_gate(self):
        self.assertEqual(assess(CLAIM,(make(original_scope_retained=False),)),
                         "HOLD_ORIGINAL_SCOPE_NOT_PRESERVED")
    def test_adverse_report_not_averaged_away(self):
        a=make(paired_target_verified=True,calibration_verified=True)
        b=replace(a,receipt_id="r2",reported_pass=False)
        self.assertEqual(assess(CLAIM,(a,b)),
                         "REPORTED_CONTRADICTION_NEEDS_INDEPENDENT_ADJUDICATION")
    def test_missing_declared_lineage(self):
        claim=replace(CLAIM,declared_lineages=("paper:2014","independent:B"))
        self.assertEqual(assess(claim,(make(paired_target_verified=True,calibration_verified=True),)),
                         "HOLD_DECLARED_LINEAGE_UNSUPPORTED")
    def test_invalid_duplicate_receipt(self):
        with self.assertRaises(ValueError):assess(CLAIM,(make(),make()))
    def test_fake_replay_flag_rejected(self):
        with self.assertRaises(ValueError):make(independently_replayed=True)
    def test_synthetic_flag_never_promoted(self):
        r=make(source_kind="SYNTHETIC",paired_target_verified=True,calibration_verified=True)
        self.assertEqual(assess(CLAIM,(r,)),"SYNTHETIC_COMPATIBILITY_ONLY")
    def test_replay_does_not_prove_physical_independence(self):
        r=make(source_kind="INDEPENDENT_REPLAY",independently_replayed=True,
               paired_target_verified=True,calibration_verified=True)
        self.assertEqual(assess(CLAIM,(r,)),"HOLD_NONCOMMON_ANCESTRY_UNVERIFIED")
    def test_two_nominal_lineages_not_ontology_pass(self):
        r=make(source_kind="INDEPENDENT_REPLAY",independently_replayed=True,
               paired_target_verified=True,calibration_verified=True)
        s=replace(r,receipt_id="r2",lineage_id="external:claimed")
        self.assertEqual(assess(CLAIM,(r,s)),
                         "BOUNDED_REPLAY_REPORTED_ANCESTRY_NOT_EXTERNALLY_CERTIFIED")
    def test_strict_boolean(self):
        with self.assertRaises(ValueError):make(calibration_verified=1)
    def test_claim_duplicate_lineage_rejected(self):
        with self.assertRaises(ValueError):replace(CLAIM,declared_lineages=("a","a"))

if __name__=="__main__":
    unittest.main(verbosity=2)
