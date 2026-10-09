#!/usr/bin/env python3
"""MQR-4.100 P8 — PhysioNet QTDB two-expert, *annotation-conditional* pairing.

No independently observed QT ground truth is present. This audits actual original .q1c/.q2c
expert-labelled waveform-boundary files, benchmark beat indexes (.man), and 250Hz timestamps.
It does not infer medical diagnoses, independent reader errors, or population Bayes risk.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import statistics

EXPECTED_ROOT_HASHES = {
    'ANNOTATORS': '41b223ff076eb236d83e6795f7178967e99ca2f5e238c9ea8e43c6ef081b8b0a',
    'RECORDS': '29aeb9287007953f42ffc4da9419eff17d34f681c1c8e4f34992b94f252f9a71',
    'SHA256SUMS.txt': '50ddae2c0515df6f9711a098ba0cb7f4e35b6b25642f905bd423f7f390d18497',
}
EXTS = ('hea', 'dat', 'man', 'qt1', 'qt2', 'q1c', 'q2c')
SOURCE_URL='https://physionet.org/files/qtdb/1.0.0/'


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def publisher_index(folder: Path) -> dict[str, str]:
    for file, expected in EXPECTED_ROOT_HASHES.items():
        assert sha((folder/file).read_bytes()) == expected, ('provider root manifest drift', file)
    checks={}
    for ln in (folder/'SHA256SUMS.txt').read_text().splitlines():
        parts=ln.split()
        if len(parts)==2 and len(parts[0])==64:
            checks[parts[1].removeprefix('./')]=parts[0]
    assert len(checks)>1000, 'Expected full publisher-checksum inventory'
    return checks


def extract_waveform_qt(ann):
    """Return per-N anchors, QRS onset, T end, QT in native samples.

    Declare the parse rule: last '(' up to 80 native samples before N (within
    prior reference-N boundary), first 't' up to 200 samples after N, then first
    ')' after this 't' before the next N. Unknown/missing boundaries remain None.
    This is a transparent retrospective parser, NOT clinical boundary adjudication.
    """
    events=list(zip((int(x) for x in ann.sample), ann.symbol))
    marks=[i for i,(_,sym) in enumerate(events) if sym=='N']
    parsed=[]
    for j,i in enumerate(marks):
        n=events[i][0]
        lo=marks[j-1]+1 if j else 0
        hi=marks[j+1] if j+1<len(marks) else len(events)
        onset=[s for s,c in events[lo:i] if c=='(' and n-80<=s<=n]
        following=[(s,c) for s,c in events[i+1:hi] if s<=n+200]
        pk=next((idx for idx,(_,c) in enumerate(following) if c=='t'),None)
        tend=next((s for s,c in following[pk+1:] if c==')'),None) if pk is not None else None
        q=onset[-1] if onset else None
        parsed.append({'beat_N':n,'qrs_onset':q,'t_end':tend,
                       'qt_samples':tend-q if q is not None and tend is not None else None})
    return parsed


def link_to_reference(reference: list[int], observed: list[dict], tolerance: int):
    """One-to-one nearest benchmark-reference-N match; no phantom completion."""
    unassigned=set(range(len(observed)))
    rows={}
    for i,ref in enumerate(reference):
        cand=sorted((abs(obj['beat_N']-ref),j) for j,obj in enumerate(observed)
                    if j in unassigned and abs(obj['beat_N']-ref)<=tolerance)
        if cand:
            _,j=cand[0]
            rows[i]=observed[j]
            unassigned.remove(j)
    return rows


def audit(folder: Path, outdir: Path):
    import wfdb
    checks=publisher_index(folder)
    records=sorted({x[:-4] for x in checks if x.endswith('.q2c')})
    assert records==['sel100','sel102','sel103','sel114','sel116','sel117','sel123',
                     'sel213','sel221','sel223','sel230']
    outdir.mkdir(parents=True,exist_ok=True)
    checked=[];per_record=[];all_rows=[]
    for rec in records:
        header=(folder/(rec+'.hea')).read_text().splitlines()[0].split()
        fs=float(header[2].split('/')[0])
        assert fs==250, (rec,fs)
        for ext in EXTS:
            name=rec+'.'+ext
            blob=(folder/name).read_bytes()
            assert sha(blob)==checks[name],('publisher file changed',name)
            checked.append({'file':name,'bytes':len(blob),'sha256':checks[name]})
        a=lambda ext: wfdb.rdann(str(folder/rec),ext)
        beat_refs=[int(n) for n,s in zip(a('man').sample,a('man').symbol) if s=='N']
        e1=extract_waveform_qt(a('q1c'))
        e2=extract_waveform_qt(a('q2c'))
        one=link_to_reference(beat_refs,e1,10)
        two=link_to_reference(beat_refs,e2,10)
        assert len(one)==len(e1),('unmatched expert-1 anchor',rec)
        assert len(two)==len(e2),('unmatched expert-2 anchor',rec)
        dif=[]
        for j,ref in enumerate(beat_refs):
            v1=one.get(j);v2=two.get(j)
            complete=(v1 is not None and v2 is not None and v1['qt_samples'] is not None and v2['qt_samples'] is not None)
            d=(v2['qt_samples']-v1['qt_samples'])*1000/fs if complete else None
            if complete:dif.append(d)
            all_rows.append({'record':rec,'selected_beat_index':j,'reference_N_sample':ref,
                'q1_N_sample':v1['beat_N'] if v1 else '',
                'q2_N_sample':v2['beat_N'] if v2 else '',
                'q1_QRS_onset_sample':v1['qrs_onset'] if v1 and v1['qrs_onset'] is not None else '',
                'q1_T_end_sample':v1['t_end'] if v1 and v1['t_end'] is not None else '',
                'q2_QRS_onset_sample':v2['qrs_onset'] if v2 and v2['qrs_onset'] is not None else '',
                'q2_T_end_sample':v2['t_end'] if v2 and v2['t_end'] is not None else '',
                'q1_QT_ms':v1['qt_samples']*1000/fs if v1 and v1['qt_samples'] is not None else '',
                'q2_QT_ms':v2['qt_samples']*1000/fs if v2 and v2['qt_samples'] is not None else '',
                'paired_complete':int(complete),
                'q2_minus_q1_QT_ms':d if complete else '',
                'abs_disagreement_ge_40ms':int(abs(d)>=40) if complete else ''})
        per_record.append({'record':rec,'selected_reference_beats':len(beat_refs),
                           'q1_annotated_N':len(e1),'q2_annotated_N':len(e2),
                           'paired_complete_QT':len(dif),
                           'median_q2_minus_q1_QT_ms':statistics.median(dif) if dif else '',
                           'mean_absolute_QT_disagreement_ms':statistics.mean(map(abs,dif)) if dif else '',
                           'ge40_count':sum(abs(x)>=40 for x in dif)})
    # Independent tracking of missing/partial dual-reader annotation is an outcome.
    complete=[r for r in all_rows if r['paired_complete']]
    dif=[float(r['q2_minus_q1_QT_ms']) for r in complete]
    n=len(all_rows);nc=len(complete);unknown=n-nc
    exceed=sum(abs(x)>=40 for x in dif)
    assert (len(records),n,nc,unknown,exceed)==(11,487,402,85,88),(len(records),n,nc,unknown,exceed)
    for threshold in (20,40,80):
        count=sum(abs(x)>=threshold for x in dif)
        assert 0 <= count <= nc
    # Sharp finite-sample bounds for a potential complete 2-expert disagreement
    # indicator under *NO assumptions* on the 85 unobserved potential labels.
    lower=exceed/n;upper=(exceed+unknown)/n
    report={'official_title':'MQR-4.100 — Auxiliary Measurement Channels, Observation-Quotient Refinement & the Limits of Identifiability Transport',
        'source':SOURCE_URL,'source_version':'PhysioNet QT Database 1.0.0','doi':'10.13026/C24K53',
        'license':'Open Data Commons Attribution License v1.0',
        'publisher_root_hashes':EXPECTED_ROOT_HASHES,'record_names':records,
        'original_files_checked':len(checked),'source_file_sha256':checked,
        'sampling_frequency_hz':250,'beat_match_tolerance_samples':10,
        'expert_1':'q1c — manually determined waveform boundaries, second pass',
        'expert_2':'q2c — manually determined waveform boundaries, second pass, only 11 records',
        'reference':'man — selected beat anchors; N fiducials can derive from automatic QRS detection',
        'all_selected_reference_beats':n,'expert1_q1c_annotated_beats':sum(r['q1_annotated_N'] for r in per_record),
        'expert2_q2c_annotated_beats':sum(r['q2_annotated_N'] for r in per_record),
        'paired_complete_qt':nc,'unobserved_complete_pairs':unknown,
        'mean_abs_qt_difference_ms':statistics.mean(map(abs,dif)),
        'mean_signed_q2_minus_q1_qt_ms':statistics.mean(dif),
        'median_signed_q2_minus_q1_qt_ms':statistics.median(dif),
        'max_abs_qt_difference_ms':max(map(abs,dif)),
        'disagreement_threshold_40ms':{'exceed_count':exceed,'observed_pair_fraction':exceed/nc,
        'finite_reference_population_no_missingness_assumption_lower':lower,
        'finite_reference_population_no_missingness_assumption_upper':upper,
        'interpretation':'sharp worst-case completion bounds over 487 *selected reference beat opportunities*, positing potential human 2 ratings on missing pairs; not latent physical QT truth or patient outcome risk'},
        'per_record':per_record,
        'limitations':['Two separately named human annotators are not certified statistically independent or blinded',
        'Both judge same ECG; common waveform/QRS fiducial metadata and selection protocol',
        'No third-expert ground truth or medical outcome, no sensitivity/specificity of reader accuracy',
        'Mismatched/missing expert2 annotations; observed-only comparison selection-biased',
        'Reference samples and QT extraction follow explicit MQR parser, not clinical manual re-review',
        'Comparisons among selected 487 beats in 11 preselected records not population transport',
        'This limited source package preserves binary ECG signals but does not visually re-review them',
        '40 ms threshold is illustrative disagreement tolerance, not medical diagnostic guideline']}
    for fn,rows in [('p8_per_beat.csv',all_rows),('p8_per_record.csv',per_record),('p8_original_file_checksums.csv',checked)]:
        with (outdir/fn).open('w',newline='',encoding='utf-8') as fd:
            wr=csv.DictWriter(fd,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
    (outdir/'p8_receipt.json').write_text(json.dumps(report,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:report[k] for k in ('all_selected_reference_beats','expert1_q1c_annotated_beats','expert2_q2c_annotated_beats','paired_complete_qt','unobserved_complete_pairs','mean_abs_qt_difference_ms')},sort_keys=True))
    print(json.dumps(report['disagreement_threshold_40ms'],sort_keys=True))
    print('MQR4100_P8_AUTHENTICATED_PHYSIONET_DUAL_READER_SOURCE_PAIR_PASS; INDEPENDENT_TRUTH_AND_TRANSPORT_HOLD')
    return report


def selftest():
    from types import SimpleNamespace
    ann=SimpleNamespace(sample=[100,110,120,128,160,180,200,230,240,249,280,303],
                        symbol=['(','N',')','t',')','(','(','N',')','t',')',')'])
    rows=extract_waveform_qt(ann)
    assert rows[0]['qt_samples']==60
    assert link_to_reference([110,230],rows,10).keys()=={0,1}
    assert link_to_reference([110,230],rows,1).keys()=={0,1}
    assert not link_to_reference([1000],rows,10)
    print('P8_UNITTEST_SELFTEST_PASS')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--source-dir',type=Path)
    p.add_argument('--out',type=Path)
    p.add_argument('--selftest',action='store_true')
    a=p.parse_args()
    if a.selftest:selftest()
    else:
        assert a.source_dir and a.out
        audit(a.source_dir,a.out)
