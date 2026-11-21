"""MQR 43: audit QWTB's published segmentation geometry, not PSFE replication.

Uses actual session metadata and raw digitizer MAT samples. Alternating M
values are labels from the metadata, NOT a demonstrated physical sign effect.
"""
import argparse
import json
import re
from pathlib import Path
import numpy as np
from scipy.io import loadmat
from metrology_source_audit_v54 import _session_scalar, sha256


def qwtb_vector(text, name):
    pattern=r'#startmatrix:: '+re.escape(name)+r'\s*\n\s*"(\[[^\n]+\])"\s*\n\s*#endmatrix:: '+re.escape(name)
    m=re.search(pattern,text)
    if m is None:
        raise ValueError('Missing typed QWTB vector '+name)
    values=json.loads(m.group(1))
    if not isinstance(values,list) or any(type(x) is not int for x in values):
        raise ValueError('QWTB vector must contain only integral entries')
    return tuple(values)


def segment_energy_profile(voltage, starts, marker=None):
    x=np.asarray(voltage,dtype=np.float64)
    if x.ndim!=1 or len(x)<2 or not np.isfinite(x).all():
        raise ValueError('Requires finite one-dimensional samples')
    breaks=np.asarray(starts)
    if breaks.ndim!=1 or len(breaks)<2 or any(type(int(z)) is not int or z!=int(z) for z in breaks):
        raise ValueError('Malformed segment bounds')
    if int(breaks[0])!=0 or int(breaks[-1])!=len(x) or np.any(np.diff(breaks)<=0):
        raise ValueError('Segments must partition the entire trace exactly once')
    rms=[]
    for a,b in zip(breaks[:-1],breaks[1:]):
        segment=x[int(a):int(b)]
        rms.append(float(np.sqrt(np.mean(segment*segment))))
    widths=np.diff(breaks)
    reconstruction=float(np.sqrt(np.dot(np.square(rms),widths)/len(x)))
    direct=float(np.sqrt(np.mean(x*x)))
    if not np.isclose(reconstruction,direct,rtol=1e-12,atol=1e-13):
        raise AssertionError('The interval energy identity failed')
    return dict(segment_rms_V=rms,segment_widths=widths.astype(int).tolist(),
                direct_all_sample_rms_V=direct,
                weighted_segment_reconstruction_rms_V=reconstruction)


def audit_qwtb_segmented_run(mat_path):
    path=Path(mat_path)
    info=(path.parent.parent/'RESULTS/TWM-QPSW-G0001-A0001.info').read_text(errors='replace')
    sess=(path.parent.parent/'session.info').read_text(errors='replace')
    starts=np.asarray(qwtb_vector(info,'S'),dtype=np.int64)
    marker=qwtb_vector(info,'M')
    if (len(starts)!=61 or len(marker)!=60 or starts[0]!=1 or starts[-1]!=3420001 or
        any(x not in (-1,1) for x in marker) or
        any(marker[i]!=(-1 if i%2==0 else 1) for i in range(60))):
        raise ValueError('Unknown QWTB S/M acquisition layout')
    expected = [12000 if i%2==0 else 102000 for i in range(60)]
    widths=np.diff(starts)
    if np.max(np.abs(widths-expected))>1 or int(widths.sum())!=3420000:
        raise ValueError('Changed or incompatible QWTB segment width pattern')
    gain=float(_session_scalar(sess,'record sample data gains [V]'))
    raw=np.asarray(loadmat(path,variable_names=['y'])['y']).reshape(-1)
    if raw.size!=3420000 or not np.issubdtype(raw.dtype,np.integer):
        raise ValueError('MAT and segmented sample count inconsistent')
    x=raw.astype(np.float64)*gain
    prof=segment_energy_profile(x,starts-1,marker)
    short=np.asarray(prof['segment_rms_V'][::2]);long=np.asarray(prof['segment_rms_V'][1::2]);
    return {'run':path.parent.parent.name,'mat_sha256':sha256(path),
            'segments':60,'short_segments':30,'long_segments':30,
            'segment_sample_counts':dict(short_11999=int(np.sum(widths[::2]==11999)),
                                          short_12000=int(np.sum(widths[::2]==12000)),
                                          long_102000=int(np.sum(widths[1::2]==102000)),
                                          long_102001=int(np.sum(widths[1::2]==102001))),
            'mean_short_segment_rms_V':float(short.mean()),
            'mean_long_segment_rms_V':float(long.mean()),
            'full_trace_rms_V':prof['direct_all_sample_rms_V'],
            'reconstructed_rms_V':prof['weighted_segment_reconstruction_rms_V'],
            'meaning':'Energy partition identity only; neither QWTB U_t nor TWM-PSFE reproduced'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('extracted_root',type=Path)
    args=parser.parse_args()
    files=sorted(args.extracted_root.rglob('RAW/G0001-A0001.mat'))
    if not files:
        parser.error('No MAT files in extracted root')
    print(json.dumps([audit_qwtb_segmented_run(p) for p in files],ensure_ascii=False,indent=2))
