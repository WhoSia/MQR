"""MQR 5.4 real archive lineage audit: hash-sharing and *candidate* time brackets.

No reference log is certified to calibrate any QPSW run merely by proximity.
Assume clock comparability explicitly; QPSW has +01:00 offset and PJVS text
logs have naive local wall time. Never silently attach reference measurements.
"""
from __future__ import annotations
from datetime import datetime
import hashlib
from pathlib import Path
from metrology_source_audit_v54 import _session_scalar

CORRECTION_RELPATHS=(
    'DIGITIZER/Digitizer correction with MX.info',
    'DIGITIZER/chn1/dummy_chn1.info',
    'DIGITIZER/chn1/csv/SFDR.csv',
    'DIGITIZER/chn1/csv/Y_inp.csv',
    'TRANSDUCERS/T01/dummy.info',
    'TRANSDUCERS/T01/csv/Z_low.csv',
)


def digest_file(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for piece in iter(lambda:f.read(1024*1024),b''):
            h.update(piece)
    return h.hexdigest()


def correction_families(run_directories, calibration_root):
    roots=tuple(sorted(Path(p) for p in run_directories))
    if len(roots)<2:
        raise ValueError('Need at least two distinct run directories')
    if len(set(map(str,roots)))!=len(roots):
        raise ValueError('Duplicate run directory')
    parent=Path(calibration_root)
    families={}
    for rel in CORRECTION_RELPATHS:
        digests=[]
        for run in roots:
            file=parent/run.name/rel
            if not file.is_file():
                raise FileNotFoundError(file)
            digests.append(digest_file(file))
        families[rel]={'sha256_by_run':digests,'unique_sha256_count':len(set(digests)),
                       'shared_bytes_all_runs':len(set(digests))==1}
    return families


def read_reference_log(path):
    path=Path(path)
    lines=path.read_text(encoding='latin1').splitlines()
    if len(lines)<6 or 'Timestamp' not in lines[2] or 'Measurement [V]' not in lines[2]:
        raise ValueError('Unknown original PJVS reference-log schema')
    observations=[]
    for line in lines[4:]:
        fields=[x.strip() for x in line.split('\t')]
        if len(fields)<6 or not fields[4] or fields[4]=='-':
            continue
        try:
            t=datetime.strptime(fields[4],'%Y-%m-%d %H:%M:%S')
            v=float(fields[5]) if fields[5]!='-' else None
        except ValueError as e:
            raise ValueError('Malformed reference timestamp/value') from e
        if v is not None:
            if not 0.7<v<0.9:
                raise ValueError('Reference log no longer has expected 0.8 V scope')
            observations.append((t,v))
    if not observations or len(set(t for t,_ in observations))!=len(observations):
        raise ValueError('No reference observations or repeated timestamps')
    return {'file_name':path.name,'file_sha256':digest_file(path),
            'observations':tuple(observations)}


def time_brackets(session_path, reference_logs, assume_common_local_clock=False):
    """Return only candidate nearby events, NEVER a certified pairing."""
    stamp=_session_scalar(Path(session_path).read_text(), 'record absolute timestamps')
    run=datetime.fromisoformat(stamp)
    if run.tzinfo is None:
        raise ValueError('QPSW session timestamp must have declared UTC offset')
    if not assume_common_local_clock:
        return {'session_timestamp':stamp,'status':'HOLD_CLOCK_SYNC_UNVERIFIED',
                'before':None,'after':None}
    # DO NOT convert naive PJVS local timestamps to UTC. Same-local-clock
    # hypothesis is explicit and remains UNVALIDATED by this archive alone.
    run_wall=run.replace(tzinfo=None)
    combined=[]
    for record in reference_logs:
        for t,v in record['observations']:
            combined.append((t,v,record['file_name']))
    if len(combined)==0 or len(set((t,name) for t,_,name in combined))!=len(combined):
        raise ValueError('No distinct reference observations')
    before=[(t,v,name) for t,v,name in combined if t<=run_wall]
    after=[(t,v,name) for t,v,name in combined if t>=run_wall]
    def item(rec):
        if rec is None:return None
        t,v,name=rec
        return {'reference_file':name,'time_local_without_tz':t.isoformat(' '),
                'delta_seconds_from_qpsw':(t-run_wall).total_seconds(),
                'voltage_V':v}
    return {'session_timestamp':stamp,
            'status':'CANDIDATE_TEMPORAL_BRACKET_CLOCK_ASSUMED_NOT_CERTIFIED',
            'before':item(max(before,key=lambda x:x[0]) if before else None),
            'after':item(min(after,key=lambda x:x[0]) if after else None)}
