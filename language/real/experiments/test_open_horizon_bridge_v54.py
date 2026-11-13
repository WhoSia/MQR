"""Run: python -m unittest -v test_open_horizon_bridge_v54.py"""
import unittest
from open_horizon_bridge_v54 import PairedReceipt, State, audit


def receipt(id='case', a='1', b='1', common=True, cal=True, ancestry=True, comparable=True):
    return PairedReceipt(id, a, b, comparable, common, cal, ancestry)


class OpenHorizonBridgeTests(unittest.TestCase):
    def test_output_match_not_grounding(self):
        self.assertEqual(audit([receipt(common=False)]).state, State.HOLD_NO_COMMON_OPERATION)

    def test_uncalibrated_map_is_held(self):
        self.assertEqual(audit([receipt(cal=False)]).state, State.HOLD_UNVERIFIED_ANCHOR)

    def test_common_source_not_independent(self):
        self.assertEqual(audit([receipt(ancestry=False)]).state, State.HOLD_SHARED_ANCESTRY)

    def test_scoped_contradiction(self):
        result = audit([receipt(a='1', b='0'), receipt(id='ok')])
        self.assertEqual((result.state, result.mismatched, result.matched),
                         (State.FAIL_SCOPED_MISMATCH, 1, 1))

    def test_positive_is_bounded_not_ontic(self):
        result = audit([receipt(), receipt(id='2', a='0', b='0')])
        self.assertEqual(result.state, State.BOUNDED_OPERATIONAL_MATCH)
        self.assertIn('Never infer complete translation', result.caveat)

    def test_conflict_does_not_disappear_with_more_matches(self):
        cases = [receipt(a='a', b='b')] + [receipt(id=str(i)) for i in range(100)]
        self.assertEqual(audit(cases).state, State.FAIL_SCOPED_MISMATCH)

    def test_unresolved_case_prevents_all_pass(self):
        self.assertEqual(audit([receipt(), receipt(id='untested', cal=False)]).state,
                         State.HOLD_UNVERIFIED_ANCHOR)

    def test_duplicate_or_empty_ids_rejected(self):
        for cases in ([receipt(), receipt()], [receipt(id='')]):
            with self.assertRaises(ValueError):
                audit(cases)

    def test_no_cases(self):
        self.assertEqual(audit([]).state, State.HOLD_NO_CASES)


if __name__ == '__main__':
    unittest.main()
