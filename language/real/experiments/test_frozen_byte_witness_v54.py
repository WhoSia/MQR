"""Real-Lang frozen byte witness negative/positive tests; no network."""
import hashlib
import tempfile
import unittest
from pathlib import Path
from frozen_byte_witness_v54 import FrozenBytes,audit_bytes

class TestFrozenBytes(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory()
        self.addCleanup(self.t.cleanup)
        self.p=Path(self.t.name)/"source.dat"
        self.p.write_bytes(b"original\x00packet")
        self.b=self.p.read_bytes()
        self.w=FrozenBytes("demo:source",hashlib.sha256(self.b).hexdigest(),len(self.b))
    def test_valid_hash_is_byte_level_only(self):
        self.assertEqual(audit_bytes(self.p,self.w),"BYTES_MATCH_FROZEN_DIGEST_ONLY")
    def test_missing_file(self):
        self.p.unlink()
        self.assertEqual(audit_bytes(self.p,self.w),"HOLD_SOURCE_BYTES_ABSENT")
    def test_mutated_same_size(self):
        self.p.write_bytes(b"X"+self.b[1:])
        self.assertEqual(audit_bytes(self.p,self.w),"FAIL_SOURCE_HASH_MISMATCH")
    def test_truncated(self):
        self.p.write_bytes(self.b[:-1])
        self.assertEqual(audit_bytes(self.p,self.w),"FAIL_SOURCE_SIZE_MISMATCH")
    def test_appended(self):
        self.p.write_bytes(self.b+b"extra")
        self.assertEqual(audit_bytes(self.p,self.w),"FAIL_SOURCE_SIZE_MISMATCH")
    def test_malformed_expected_sha(self):
        with self.assertRaises(ValueError):FrozenBytes("x","abc",1)
    def test_uppercase_expected_sha_rejected(self):
        with self.assertRaises(ValueError):FrozenBytes("x","A"*64,1)
    def test_boolean_size_rejected(self):
        with self.assertRaises(ValueError):FrozenBytes("x",hashlib.sha256(b"").hexdigest(),True)
    def test_zero_size(self):
        self.p.write_bytes(b"")
        empty=FrozenBytes("empty",hashlib.sha256(b"").hexdigest(),0)
        self.assertEqual(audit_bytes(self.p,empty),"BYTES_MATCH_FROZEN_DIGEST_ONLY")
    def test_explicit_manifest_required(self):
        with self.assertRaises(ValueError):audit_bytes(self.p,None)

if __name__=="__main__":
    unittest.main(verbosity=2)
