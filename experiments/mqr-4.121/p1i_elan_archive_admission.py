"""MQR P1I: offline verification/staging of a caller-supplied elan release archive.

Never downloads or installs anything into global paths. SHA-256 must match the
GitHub release asset digest from a reviewed manifest. Optional smoke only runs
the staged elan-init --version; it is NOT a secure network sandbox.
"""
import argparse
import hashlib
import io
import json
import os
import subprocess
import tarfile
import tempfile
from pathlib import Path, PurePosixPath

def sha256(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for part in iter(lambda:f.read(65536),b''):h.update(part)
    return h.hexdigest()

def stage(archive,expected,destination):
    if len(expected)!=64 or any(z not in '0123456789abcdef' for z in expected.lower()):
        raise ValueError('invalid reviewed digest')
    if sha256(archive)!=expected.lower():raise ValueError('SHA256 mismatch: no execution')
    destination.mkdir(parents=True,exist_ok=False)
    names=[]
    with tarfile.open(archive,'r:gz') as t:
        for m in t.getmembers():
            p=PurePosixPath(m.name)
            if m.issym() or m.islnk() or m.isdev() or m.isfifo() or not (m.isfile() or m.isdir()):
                raise ValueError('archive special member rejected')
            if p.is_absolute() or '..' in p.parts or len(p.parts)>3:
                raise ValueError('archive traversal rejected')
            if m.isfile():
                if m.size>50_000_000:raise ValueError('file too large')
                buf=t.extractfile(m)
                if buf is None:raise ValueError('missing member data')
                target=destination.joinpath(*p.parts)
                target.parent.mkdir(parents=True,exist_ok=True)
                with target.open('wb') as f:
                    for b in iter(lambda:buf.read(65536),b''):f.write(b)
                if m.name.endswith('elan-init'):target.chmod(0o700)
                names.append(str(p))
    return names

def smoke_version(binary,root):
    if not binary.is_file():raise ValueError('elan-init binary not found')
    env={'HOME':str(root/'home'),'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C'}
    (root/'home').mkdir(exist_ok=True)
    r=subprocess.run([str(binary),'--version'],cwd=str(root),env=env,
                     text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                     timeout=6,check=False)
    if r.returncode!=0:raise ValueError('offline --version smoke failed')
    return r.stdout.strip()[:240]

def tests():
    with tempfile.TemporaryDirectory(prefix='mqr-p1i-archive-') as temp:
        root=Path(temp);archive=root/'fixture.tar.gz'
        with tarfile.open(archive,'w:gz') as t:
            b=b'FAKE SYNTHETIC FIXTURE; NEVER RUN\n'
            m=tarfile.TarInfo('elan-init');m.size=len(b);m.mode=0o700;t.addfile(m,io.BytesIO(b))
        good=sha256(archive)
        assert stage(archive,good,root/'ok')==['elan-init']
        try:stage(archive,'0'*64,root/'bad')
        except ValueError as e:assert 'SHA256 mismatch' in str(e)
        else:raise AssertionError('bad digest admitted')
        traversal=root/'traversal.tar.gz'
        with tarfile.open(traversal,'w:gz') as t:
            b=b'bad';m=tarfile.TarInfo('../escape');m.size=len(b);t.addfile(m,io.BytesIO(b))
        try:stage(traversal,sha256(traversal),root/'escape-test')
        except ValueError as e:assert 'traversal' in str(e)
        else:raise AssertionError('path traversal admitted')
    print('MQR_P1I_INSTALLER_ARCHIVE_GATE=PASS_SYNTHETIC')
    print('MQR_P1I_LIVE_ELAN_BINARY_SHA_AND_RUN=HOLD')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--archive',type=Path)
    p.add_argument('--manifest',type=Path)
    p.add_argument('--stage-to',type=Path)
    p.add_argument('--smoke-version',action='store_true')
    a=p.parse_args()
    tests()
    if a.archive:
        if not a.manifest or not a.stage_to:raise SystemExit('manifest and stage-to required')
        m=json.loads(a.manifest.read_text())
        assert m['scope']=='ADVISORY_NOT_DEPLOYED'
        expected=m['linux_x86_64_elan_binary_candidate']['sha256']
        names=stage(a.archive,expected,a.stage_to)
        print(json.dumps({'sha256_match':True,'staged_names':names,'installed_globally':False}))
        if a.smoke_version:
            # This does NOT force network isolation. Use only in an explicitly
            # externally isolated machine/VM already configured by the operator.
            print('ELAN_VERSION_SMOKE='+smoke_version(a.stage_to/'elan-init',a.stage_to))
