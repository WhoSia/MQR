"""MQR 5.4: source-audited analysis of TWO public, distinct metrology datasets.

No independent cross-source calibration is implied. Kraus exports are processed
figure data; Sira MAT files are raw digitizer counts with separate QWTB outputs.
Works on downloaded dataset contents and never bundles private/user source bytes.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path
import numpy as np
from scipy.io import loadmat

KRAUS_FIG6 = 'Opto-JAWS/fig6a+b.txt'
KRAUS_README = 'Opto-JAWS/README.txt'


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def lag1(series: np.ndarray) -> float:
    x = np.asarray(series, dtype=float)
    if len(x) < 3 or np.std(x[:-1]) == 0 or np.std(x[1:]) == 0:
        raise ValueError('At least three nonconstant observations needed')
    return float(np.corrcoef(x[:-1], x[1:])[0, 1])


def moving_block_difference(early, late, block=60, repetitions=2000, seed=43):
    """Exploratory within-window dependence sensitivity, NOT metrological CI."""
    a, b = np.asarray(early, dtype=float), np.asarray(late, dtype=float)
    if (a.ndim != 1 or b.ndim != 1 or len(a) != len(b) or
        not 1 <= block <= len(a) or repetitions < 100 or
        not np.isfinite(a).all() or not np.isfinite(b).all()):
        raise ValueError('Invalid equal-duration windows or bootstrap settings')
    rng = np.random.default_rng(seed)
    def resample_means(x):
        n = len(x); n_blocks = (n + block - 1) // block
        starts = rng.integers(0, n - block + 1, size=(repetitions, n_blocks))
        indices = (starts[:, :, None] + np.arange(block)).reshape(repetitions, -1)[:, :n]
        return x[indices].mean(axis=1)
    difference = resample_means(b) - resample_means(a)
    return [float(v) for v in np.quantile(difference, [0.025, 0.975])]


def kraus_audit(path, early_late_seconds=300, block=60):
    path = Path(path)
    with zipfile.ZipFile(path) as z:
        if len(z.namelist()) != len(set(z.namelist())):
            raise ValueError('Ambiguous duplicate ZIP member names')
        names = set(z.namelist())
        if not {KRAUS_README, KRAUS_FIG6}.issubset(names):
            raise ValueError('Missing README or Figure 6')
        readme = z.read(KRAUS_README).decode('utf-8')
        if '10.7795/720.20250210' not in readme or 'Processed data' not in readme:
            raise ValueError('Unexpected dataset provenance or processing description')
        raw = z.read(KRAUS_FIG6)
    lines = raw.decode('latin-1').splitlines()
    if len(lines) < 4 or len(lines[0].split('\t')) != 10:
        raise ValueError('Unexpected Figure 6 header')
    rows = list(csv.reader(io.StringIO('\n'.join(lines[2:])), delimiter='\t'))
    if any(len(row) != 10 for row in rows):
        raise ValueError('Unequal column counts or trailing non-numeric columns')
    try:
        data = np.array([[float(v) for v in row] for row in rows], dtype=float)
    except ValueError as exc:
        raise ValueError('Non-numeric figure record') from exc
    if not np.isfinite(data).all():
        raise ValueError('Non-finite figure value')
    n = len(data)
    if n != 2101 or not np.array_equal(data[:, 0], np.arange(n)):
        raise ValueError('This Figure 6 run is not 2101 consecutive 1-s observations')
    if np.max(np.abs(data[:, 5] - data[:, 0] / 60)) > 4e-6:
        raise ValueError('Second/minute time columns do not agree after rounding')
    if not 2 <= early_late_seconds <= n//2:
        raise ValueError('Time window must fit both ends')
    nwin = early_late_seconds
    def compare(index):
        x=data[:, index]; before=x[:nwin]; after=x[-nwin:]
        return {'unit': ('microV/V' if index in (6, 8) else 'dB' if index in (7, 9) else 'dBV'),
                'mean_first': float(before.mean()), 'mean_last': float(after.mean()),
                'last_minus_first': float(after.mean()-before.mean()),
                'lag1': lag1(x),
                'bootstrap_95_exploratory': moving_block_difference(before, after, block=block)}
    return {'dataset': 'Kraus 2025 PTB DOI 10.7795/720.20250210',
            'source_kind': 'processed figure exports, not raw ADC waveform',
            'zip_sha256': sha256(path), 'fig6_sha256': hashlib.sha256(raw).hexdigest(),
            'rows': n, 'duration_minutes': float(data[-1, 5]),
            'time_window_seconds': nwin, 'block_seconds': block,
            'deviation_microV_per_V': compare(6), 'thd_dB': compare(7),
            'adc_channel_0_dBV': compare(1), 'adc_channel_1_dBV': compare(3),
            'same_row_channel1_minus_channel0_mean_dBV': float(np.mean(data[:, 3]-data[:, 1])),
            'moving_average_lag1': {'amplitude': lag1(data[:, 8]), 'thd': lag1(data[:, 9])},
            'limits': ['not device-independent evidence', 'bootstrap is exploratory',
                       'published moving averages are derived columns',
                       'no raw ADC waveform samples or randomized pairing in this ZIP']}


def _read_info_section(text, key):
    found = re.search(r'#startsection:: '+re.escape(key)+r'\s*\n(.*?)\n\s*#endsection:: '+re.escape(key), text, flags=re.S)
    if not found:
        raise ValueError('Missing QWTB '+key+' result section')
    val = re.search(r'#startmatrix:: value\s*\n(.*?)\n\s*#endmatrix:: value', found.group(1), flags=re.S)
    if not val:
        raise ValueError('Missing QWTB value vector')
    return np.array([float(x.strip()) for x in val.group(1).split(';') if x.strip()], dtype=float)


def _session_scalar(text, label):
    match = re.search(re.escape(label) + r'::\s*(\S+)', text)
    if not match:
        match = re.search(re.escape(label) + r'\s*\n\s*(\S+)', text)
    if not match:
        raise ValueError('Missing session scalar: '+label)
    return match.group(1)


def sira_run_audit(mat_path):
    path = Path(mat_path)
    if not path.is_file():
        raise FileNotFoundError(f'Raw MAT does not exist: {path}')
    parent = path.parent.parent
    session = (parent / 'session.info').read_text(encoding='utf-8', errors='replace')
    results = (parent / 'RESULTS' / 'TWM-QPSW-G0001-A0001.info').read_text(encoding='utf-8', errors='replace')
    if path.name != 'G0001-A0001.mat' or 'sample data format:: mat-v4' not in session:
        raise ValueError('Unexpected MAT file or data encoding')
    count = int(_session_scalar(session, 'samples count'))
    rate = float(_session_scalar(session, 'sampling rate [Sa/s]'))
    gain = float(_session_scalar(session, 'record sample data gains [V]'))
    offset = float(_session_scalar(session, 'record sample data offsets [V]'))
    timestamp = _session_scalar(session, 'record absolute timestamps')
    if count != 3420000 or rate != 60000 or not 0 < gain < 1e-6 or offset != 0:
        raise ValueError('Unexpected acquisition schema; manual review required')
    variables = loadmat(path, variable_names=['y'])
    if 'y' not in variables:
        raise ValueError('Digitizer variable y absent')
    y = np.asarray(variables['y'])
    if y.size != count or not np.issubdtype(y.dtype, np.integer):
        raise ValueError('Digitizer counts schema mismatch')
    x = y.reshape(-1).astype(np.float64)*gain+offset
    processed = _read_info_section(results, 'U_t')
    if len(processed) != 30 or not np.isfinite(x).all() or not np.isfinite(processed).all():
        raise ValueError('Invalid raw counts or processed segment results')
    raw_rms = float(np.sqrt(np.mean(x*x)))
    return {'run_directory': parent.name, 'source_kind': 'raw digitizer MAT plus processed QWTB output',
            'mat_sha256': sha256(path), 'timestamp_from_session': timestamp,
            'sample_count': int(count), 'sample_rate_sps': float(rate),
            'duration_seconds_nominal': float(count/rate), 'gain_volts_per_count': float(gain),
            'raw_full_trace_rms_V': raw_rms,
            'processed_U_t_n': int(len(processed)), 'processed_U_t_mean_V': float(processed.mean()),
            'processed_minus_full_trace_rms_V': float(processed.mean()-raw_rms),
            'processing_uncertainty_mode': 'none',
            'limits': ['full-record RMS and algorithm-selected QWTB RMS need not share estimand',
                       '30 within-run values are not 30 independent experimental replications',
                       'session text/processed output do not independently certify calibration']}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--kraus-zip', type=Path)
    p.add_argument('--sira-extracted-root', type=Path)
    p.add_argument('--output', type=Path)
    a=p.parse_args()
    result={'protocol':'MQR_5_4_43_real_metrology_v1'}
    if a.kraus_zip:
        result['kraus']=kraus_audit(a.kraus_zip)
    if a.sira_extracted_root:
        files=sorted(a.sira_extracted_root.rglob('RAW/G0001-A0001.mat'))
        if not files:
            raise ValueError('No raw MAT extracted from Šíra archive')
        result['sira_runs']=[sira_run_audit(v) for v in files]
    if 'kraus' not in result and 'sira_runs' not in result:
        p.error('At least one input dataset required')
    out=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(out,encoding='utf-8')
    else:
        print(out,end='')

if __name__=='__main__':
    main()
