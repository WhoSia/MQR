"""MQR54 Real-Lang bridge regression on published REFMAC5 summary fixtures.

The quoted metrics are Rinaldelli et al. (2014) author Table 1.
This is NOT an independent run of REFMAC5, NMR acquisition or crystallography.
"""
import unittest
from decimal import Decimal as D
from interfield_target_receipt_v54 import Claim, EvidenceReceipt, assess

TABLE = (
    ("3SHI",".414",".160",".264",".267"),
    ("3NHE",".360",".121",".158",".160"),
    ("1IGD",".146",".081",".132",".134"),
    ("1EXR",".398",".308",".142",".147"),
    ("1YR5",".540",".201",".304",".307"),
)

def published_receipt(pdb,target):
    return EvidenceReceipt(
        receipt_id=f"Rinaldelli2014:{pdb}:{target}",target=target,
        source_kind="PUBLISHED_SUMMARY",source_id="doi:10.1107/S1399004713034160:Table1",
        specimen_id=pdb,regime_id="AUTHOR_REFINEMENT_SUMMARY",
        lineage_id="Rinaldelli2014:Table1",original_scope_retained=True,
        paired_target_verified=False,calibration_verified=False,
        independently_replayed=False,reported_pass=True)

class TestPublishedCaseBoundary(unittest.TestCase):
    def test_all_five_cases_have_both_distinct_typed_targets(self):
        for pdb, *_ in TABLE:
            receipts=(published_receipt(pdb,"NMR_Q_RDC"),published_receipt(pdb,"X_RAY_R_FREE"))
            for target in ("NMR_Q_RDC","X_RAY_R_FREE"):
                claim=Claim(f"{pdb}:{target}",target,pdb,"AUTHOR_REFINEMENT_SUMMARY",
                            ("Rinaldelli2014:Table1",))
                self.assertEqual(assess(claim,receipts),"HOLD_PHYSICAL_PAIRING_UNVERIFIED")

    def test_foreign_specimen_is_not_substituted(self):
        claim=Claim("1EXR:NMR","NMR_Q_RDC","1EXR","AUTHOR_REFINEMENT_SUMMARY",
                    ("Rinaldelli2014:Table1",))
        self.assertEqual(assess(claim,(published_receipt("1IGD","NMR_Q_RDC"),)),
                         "HOLD_TARGET_RECEIPT_ABSENT")

    def test_the_two_metrics_may_disagree_directionally(self):
        for _,qa,qb,ra,rb in TABLE:
            self.assertLess(D(qb),D(qa))
            self.assertGreater(D(rb),D(ra))

    def test_borderline_calmodulin_not_rounded_to_agreement(self):
        m={entry[0]:entry for entry in TABLE}
        self.assertGreater(D(m["1YR5"][2]),D(".2"))
        self.assertGreater(D(m["1EXR"][2]),D(".2"))
        self.assertLess(D(m["1IGD"][2]),D(".2"))

if __name__=="__main__":
    unittest.main(verbosity=2)
