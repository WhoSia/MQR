"""Fail-closed reference-log / correction hash lineage tests."""
import tempfile
import unittest
from pathlib import Path
from reference_lineage_v54 import (
    CORRECTION_RELPATHS, correction_families, read_reference_log, time_brackets,
)


def fake_reference(path):
    path.write_text('device\n\nTimestamp\tMeasurement [V]\tTimestamp\tMeasurement [V]\tTimestamp\tMeasurement [V]\n\n' +
                    'A\t60\t0.8\tDifferential\t2023-03-10 16:22:05\t0.799998157\n'+
                    'A\t60\t0.8\tDifferential\t2023-03-10 17:15:13\t0.799998529\n',encoding='latin1')

class TestReferenceLineage(unittest.TestCase):
    def test_clock_assumption_required_even_if_reference_logs_exist(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); session=root/'session.info'
            session.write_text('record absolute timestamps\n 2023-03-10T16:50:40.167183+01:00\n')
            ref=root/'ref.txt';fake_reference(ref)
            r=time_brackets(session,[read_reference_log(ref)])
            self.assertEqual(r['status'],'HOLD_CLOCK_SYNC_UNVERIFIED')
            self.assertIsNone(r['before'])
            self.assertIsNone(r['after'])

    def test_time_bracketing_with_explicit_unvalidated_clock_hypothesis(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);session=root/'session.info'
            session.write_text('record absolute timestamps\n 2023-03-10T16:50:40.167183+01:00\n')
            ref=root/'ref.txt';fake_reference(ref)
            r=time_brackets(session,[read_reference_log(ref)],assume_common_local_clock=True)
            self.assertEqual(r['status'],'CANDIDATE_TEMPORAL_BRACKET_CLOCK_ASSUMED_NOT_CERTIFIED')
            self.assertAlmostEqual(r['before']['delta_seconds_from_qpsw'],-1715.167183)
            self.assertAlmostEqual(r['after']['delta_seconds_from_qpsw'],1472.832817)

    def test_references_missing_one_side_are_not_conjured(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);session=root/'session.info'
            session.write_text('record absolute timestamps\n 2023-03-10T20:00:00+01:00\n')
            ref=root/'ref.txt';fake_reference(ref)
            r=time_brackets(session,[read_reference_log(ref)],True)
            self.assertIsNone(r['after'])
            self.assertIsNotNone(r['before'])

    def test_equal_correction_sha_is_not_claimed_if_one_file_differs(self):
        with tempfile.TemporaryDirectory() as d:
            base=Path(d);runs=[base/'runA',base/'runB']
            for run in runs:
                for rel in CORRECTION_RELPATHS:
                    file=(base/'cal'/run.name/rel);file.parent.mkdir(parents=True,exist_ok=True)
                    file.write_bytes(rel.encode())
            fam=correction_families(runs,base/'cal')
            self.assertTrue(all(v['shared_bytes_all_runs'] for v in fam.values()))
            (base/'cal'/'runB'/CORRECTION_RELPATHS[0]).write_text('changed')
            fam=correction_families(runs,base/'cal')
            self.assertFalse(fam[CORRECTION_RELPATHS[0]]['shared_bytes_all_runs'])
            self.assertEqual(fam[CORRECTION_RELPATHS[0]]['unique_sha256_count'],2)

    def test_missing_correction_refuses_to_invent_data(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                correction_families((Path(d)/'a',Path(d)/'b'),Path(d))

    def test_duplicate_run_identity_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                correction_families((Path(d)/'a',Path(d)/'a'),Path(d))

    def test_reference_schema_invalid_and_missing_measurements_fail(self):
        with tempfile.TemporaryDirectory() as d:
            ref=Path(d)/'ref.txt';ref.write_text('not a reference log')
            with self.assertRaises(ValueError):read_reference_log(ref)

    def test_session_without_timezone_offset_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            session=Path(d)/'session.info'
            session.write_text('record absolute timestamps\n 2023-03-10T16:50:40\n')
            with self.assertRaises(ValueError):time_brackets(session,[],True)

if __name__=='__main__':unittest.main()
