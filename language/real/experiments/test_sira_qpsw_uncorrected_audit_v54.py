import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from sira_qpsw_uncorrected_audit_v54 import audit_mat, matrix_scalar

SESSION = """samples count:: 4
sampling rate [Sa/s]:: 2
#startmatrix:: record samples counts
    4
#endmatrix:: record samples counts
#startmatrix:: record sample data gains [V]
    0.5
#endmatrix:: record sample data gains [V]
#startmatrix:: record sample data offsets [V]
    1.0
#endmatrix:: record sample data offsets [V]
"""


class RawTests(unittest.TestCase):
    def test_scalar_and_missing_metadata(self):
        self.assertEqual(matrix_scalar(SESSION, "record sample data gains [V]"), .5)
        with self.assertRaises(ValueError):matrix_scalar(SESSION,"not in file")

    def test_synthetic_integer_mat(self):
        import numpy as np
        from scipy.io import savemat
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); mat=root/"x.mat"; info=root/"session.info"
            savemat(mat, {"y":np.array([[0,2,-2,0]],dtype="int32")},format="4")
            info.write_text(SESSION)
            r=audit_mat(mat, info)
            self.assertEqual(r["raw_count"],4)
            self.assertEqual(r["duration_s"],2)
            self.assertAlmostEqual(r["mean_uncorrected_V"],1)
            self.assertAlmostEqual(r["rms_uncorrected_V"],1.224744871391589)

    def test_original_run_if_available(self):
        files=list(Path("/mnt/data/_mqr_sira_work").glob("*0015*G0001-A0001.mat"))
        if not files:self.skipTest("Original raw 7z not mounted")
        info=list(files[0].parent.glob("*0015*session.info"))[0]
        r=audit_mat(files[0],info)
        self.assertEqual(r["raw_count"],3420000)
        self.assertEqual(r["duration_s"],57)
        self.assertAlmostEqual(r["rms_uncorrected_V"],0.8126092926115207,places=9)

if __name__=="__main__":
    unittest.main()
