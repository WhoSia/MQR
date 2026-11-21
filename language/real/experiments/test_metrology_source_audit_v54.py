"""Unit-level safeguards for real data audit. No large published data required."""
import io
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from unittest.mock import patch
import numpy as np
from scipy.io import savemat

from metrology_source_audit_v54 import (
    kraus_audit, lag1, moving_block_difference, sira_run_audit, sha256,
)


def make_kraus_zip(path, *, bad_time=False, missing=False, duplicate=False):
    rows = ['t\tCh0\tTHD0\tCh1\tTHD1\tminutes\tdeviation\tTHD\tmovingdev\tmovingTHD',
            's\tdBV\tdB\tdBV\tdB\tmin\tmicroV/V\tdB\tmicroV/V\tdB']
    for t in range(2101):
        second = t+1 if (bad_time and t == 10) else t
        rows.append(f'{second}\t{-21.4 + t*.00001:.6f}\t{-104+t*.00001:.6f}\t{-21.3 + t*.00001:.6f}\t{-103+t*.00001:.6f}\t{t/60:.5f}\t{-99+0.001*t:.6f}\t{-103.7+t*.00001:.6f}\t{-98.5+t*.00001:.6f}\t{-103.7+t*.00001:.6f}')
    with zipfile.ZipFile(path, 'w') as z:
        z.writestr('Opto-JAWS/README.txt',
                   'DOI 10.7795/720.20250210 ; Processed data; not raw digitizer samples')
        if not missing:
            z.writestr('Opto-JAWS/fig6a+b.txt', '\n'.join(rows)+'\n')
        if duplicate:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore',UserWarning)
                z.writestr('Opto-JAWS/README.txt', 'duplicate value')


def make_sira_fixture(root, *, declared_count=3420000, u_n=30):
    run = root/'synthetic_run'
    (run/'RAW').mkdir(parents=True)
    (run/'RESULTS').mkdir(parents=True)
    text = ('sample data format:: mat-v4\n'
            f'samples count:: {declared_count}\n'
            'sampling rate [Sa/s]:: 60000.0000000000\n'
            '#startmatrix:: record sample data gains [V]\n    5.0000000E-9\n'
            '#endmatrix:: record sample data gains [V]\n'
            '#startmatrix:: record sample data offsets [V]\n    0.0000000\n'
            '#endmatrix:: record sample data offsets [V]\n'
            '#startmatrix:: record absolute timestamps\n'
            '    2023-03-10T16:50:40.167183+01:00\n'
            '#endmatrix:: record absolute timestamps\n')
    (run/'session.info').write_text(text)
    vec = '; '.join('1.25' for _ in range(u_n))
    (run/'RESULTS/TWM-QPSW-G0001-A0001.info').write_text(
        '#startsection:: U_t\n#startmatrix:: value\n'+vec+
        '\n#endmatrix:: value\n#endsection:: U_t\n')
    y=np.tile(np.array([100000000,-100000000],dtype=np.int32),3420000//2)
    savemat(run/'RAW/G0001-A0001.mat', {'y': y.reshape(1,-1)})
    return run/'RAW/G0001-A0001.mat'


class TestMetrologySourceAudit(unittest.TestCase):
    def test_true_bootstrap_difference_for_constant_groups(self):
        a=[3.]*300; b=[5.]*300
        self.assertEqual(moving_block_difference(a,b,block=60),[2.,2.])

    def test_block_bootstrap_reproducible_but_sensitive_to_block_size(self):
        a=np.sin(np.linspace(0,20,300));b=np.cos(np.linspace(0,20,300))
        x=moving_block_difference(a,b,block=10,seed=42)
        self.assertEqual(x,moving_block_difference(a,b,block=10,seed=42))
        self.assertNotEqual(x,moving_block_difference(a,b,block=100,seed=42))

    def test_block_bootstrap_bad_windows_fail_closed(self):
        for x,y,block in [([1,2],[1],1),([1],[3],0),([1],[4],2),
                          ([1,float('nan')],[3,4],1)]:
            with self.assertRaises(ValueError): moving_block_difference(x,y,block=block)

    def test_lag1_reject_constant(self):
        with self.assertRaises(ValueError):lag1(np.array([1.,1.,1.]))

    def test_processed_fig6_synthetic_provenance_and_timestamps(self):
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'p.zip'; make_kraus_zip(file)
            receipt=kraus_audit(file)
            self.assertEqual(receipt['rows'],2101)
            self.assertEqual(receipt['duration_minutes'],35.)
            self.assertEqual(receipt['zip_sha256'],sha256(file))
            self.assertAlmostEqual(receipt['deviation_microV_per_V']['last_minus_first'],1.801,places=3)
            self.assertAlmostEqual(receipt['same_row_channel1_minus_channel0_mean_dBV'],.1)

    def test_shifted_times_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/'b.zip'; make_kraus_zip(f,bad_time=True)
            with self.assertRaises(ValueError):kraus_audit(f)

    def test_figure_missing_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/'b.zip'; make_kraus_zip(f,missing=True)
            with self.assertRaises(ValueError):kraus_audit(f)

    def test_duplicate_member_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/'b.zip'; make_kraus_zip(f,duplicate=True)
            with self.assertRaises(ValueError):kraus_audit(f)

    def test_mat_counts_and_processing_not_equated(self):
        with tempfile.TemporaryDirectory() as d:
            f=make_sira_fixture(Path(d)); receipt=sira_run_audit(f)
            self.assertEqual(receipt['sample_count'],3420000)
            self.assertAlmostEqual(receipt['raw_full_trace_rms_V'],.5,places=8)
            self.assertAlmostEqual(receipt['processed_U_t_mean_V'],1.25)
            self.assertAlmostEqual(receipt['processed_minus_full_trace_rms_V'],.75)
            self.assertEqual(receipt['mat_sha256'],sha256(f))

    def test_wrong_session_count_rejected_without_claim(self):
        with tempfile.TemporaryDirectory() as d:
            f=make_sira_fixture(Path(d),declared_count=57)
            with self.assertRaises(ValueError):sira_run_audit(f)

    def test_wrong_qwtb_output_count_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f=make_sira_fixture(Path(d),u_n=29)
            with self.assertRaises(ValueError):sira_run_audit(f)

    def test_missing_raw_file_is_not_invented(self):
        with tempfile.TemporaryDirectory() as d:
            f=make_sira_fixture(Path(d)); f.unlink()
            with self.assertRaises(FileNotFoundError):sira_run_audit(f)


if __name__=='__main__':unittest.main()
