#!/usr/bin/env python3
"""MQR-4.101 P1: finite binary risk bounds with a selectively available, fallible reference.

Source-native reanalysis of previously audited PhysioNet QTDB P8 per-beat observations.
Decision cutoffs are arbitrary NON-CLINICAL threshold probes; no truth labels exist.
Any finite reference-error budget is a hypothetical external certificate, not data-derived.
"""
import argparse
import collections
import csv
import hashlib
import io
import itertools
import json
import pathlib
import statistics
import zipfile

N_EXPECT, M_EXPECT = 487, 402
CUTS_MS = (400, 420, 440, 460, 480)


def sharp_risk(n:int, m:int, observed_errors:int, max_fallible_reference_errors:int):
    """Sharp count endpoints for real truth risk of fully observed binary h.

    Only m reference ratings are supplied. Among those m, true binary reference
    errors are at most k; no restriction on missing n-m truth labels. This
    requires an *external k certificate*. No dependence assumptions needed.
    """
    assert isinstance(n,int) and isinstance(m,int) and isinstance(observed_errors,int)
    assert isinstance(max_fallible_reference_errors,int)
    assert 0 <= observed_errors <= m <= n
    assert 0 <= max_fallible_reference_errors <= m
    k=max_fallible_reference_errors
    lo=max(0,observed_errors-k)
    hi=observed_errors+min(k,m-observed_errors)+(n-m)
    return lo,hi


def brute_force_endpoints(prediction, observed, k):
    """Exhaustive truth assignments for small vectors; observed=None if missing."""
    n=len(prediction)
    mask=[i for i,v in enumerate(observed) if v is not None]
    outcomes=[]
    for truth in itertools.product((0,1),repeat=n):
        if sum(truth[i]!=observed[i] for i in mask)<=k:
            outcomes.append(sum(truth[i]!=prediction[i] for i in range(n)))
    assert outcomes
    return min(outcomes),max(outcomes)


def test_small_exhaustive():
    cases=0
    for n in range(1,6):
        for labels in itertools.product((None,0,1),repeat=n):
            m=sum(x is not None for x in labels)
            for pred in itertools.product((0,1),repeat=n):
                e=sum(a!=b for a,b in zip(pred,labels) if b is not None)
                for k in range(m+1):
                    assert sharp_risk(n,m,e,k)==brute_force_endpoints(pred,labels,k)
                    cases+=1
    assert sharp_risk(487,402,76,0)==(76,161)
    assert sharp_risk(487,402,76,10)==(66,171)
    assert sharp_risk(487,402,76,402)==(0,487)
    print('MQR4101_P1_EXHAUSTIVE_SHARPNESS_PASS',cases,'BRUTEFORCE_CASES')


def extract_p8_csv(archive: pathlib.Path):
    """Read original P8 audit CSV, supporting Drive outer artifact + inner ZIP."""
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        names=z.namelist()
        candidates=[name for name in names if name.endswith('p8_per_beat.csv')]
        if candidates:
            return z.read(candidates[0]),{'archive_layers':1,'row_member':candidates[0]}
        nested=[name for name in names if name.endswith('.zip')]
        assert len(nested)==1, names
        inner=z.read(nested[0])
        with zipfile.ZipFile(io.BytesIO(inner)) as zin:
            assert zin.testzip() is None
            matches=[name for name in zin.namelist() if name.endswith('p8_per_beat.csv')]
            assert len(matches)==1
            return zin.read(matches[0]),{'archive_layers':2,'row_member':matches[0],
                'nested_zip_sha256':hashlib.sha256(inner).hexdigest()}


def audit(source: pathlib.Path, outdir: pathlib.Path, is_raw_csv: bool=False):
    if is_raw_csv:
        data=source.read_bytes()
        archive_info={'archive_layers':0,'row_member':'p8_per_beat.csv',
            'provenance':'byte-for-byte P8 source-checked original receipt (NOT new publisher raw waveforms)'}
    else:
        data,archive_info=extract_p8_csv(source)
    raw=list(csv.DictReader(io.StringIO(data.decode('utf-8'))))
    assert len(raw)==N_EXPECT
    rec_order=sorted(set(r['record'] for r in raw))
    assert len(rec_order)==11
    assert sum(int(r['paired_complete']) for r in raw)==M_EXPECT
    # Check consistency of the recorded pair-completeness with actually parsed values.
    for row in raw:
        assert row['paired_complete'] in ('0','1')
        if row['paired_complete']=='1':
            assert row['q1_QT_ms'] and row['q2_QT_ms']
        else:
            assert not (row['q1_QT_ms'] and row['q2_QT_ms'])
    details=[];summaries=[]
    for cut in CUTS_MS:
        e=0;m=0;by_rec=[]
        for rec in rec_order:
            rows=[r for r in raw if r['record']==rec]
            paired=[r for r in rows if r['paired_complete']=='1']
            n_g=len(rows);m_g=len(paired)
            disagree=sum((float(r['q1_QT_ms'])>=cut)!=(float(r['q2_QT_ms'])>=cut) for r in paired)
            by_rec.append({'cutoff_ms':cut,'record':rec,'n':n_g,'m':m_g,
                           'missing':n_g-m_g,'reference_disagreement':disagree,
                           'perfect_reference_lower_count':disagree,
                           'perfect_reference_upper_count':disagree+n_g-m_g})
            e+=disagree;m+=m_g
        assert m==402
        bound_k={str(k):{'lower_count':sharp_risk(len(raw),m,e,k)[0],
                          'upper_count':sharp_risk(len(raw),m,e,k)[1],
                          'lower_rate':sharp_risk(len(raw),m,e,k)[0]/len(raw),
                          'upper_rate':sharp_risk(len(raw),m,e,k)[1]/len(raw),
                          'reference_error_budget_status':'hypothetical, NOT verified by source'}
                for k in (0,5,10,20,m)}
        equal_weight_lb=sum(g['perfect_reference_lower_count']/g['n'] for g in by_rec)/len(by_rec)
        equal_weight_ub=sum(g['perfect_reference_upper_count']/g['n'] for g in by_rec)/len(by_rec)
        summaries.append({'cutoff_ms':cut,'source_reference_beats':len(raw),
           'complete_qt_pairs':m,'unpaired':len(raw)-m,'paired_binary_disagreements':e,
           'observed_paired_reference_disagreement_rate':e/m,
           'pooled_hypothetical_external_reference_mistake_budget':bound_k,
           'equal_record_weight_under_perfect_external_reference':{'lower':equal_weight_lb,'upper':equal_weight_ub},
           'truth_unconstrained_risk_bounds':[0,1],
           'sampling_inference':'NONE; fixed eleven available recordings, selected beats only',
           'diagnosis':'NONE; cutoffs are methodological stress probes'})
        details.extend(by_rec)
    assert [(x['cutoff_ms'],x['paired_binary_disagreements']) for x in summaries]==[(400,88),(420,76),(440,76),(460,66),(480,42)]
    # Distinct real-world counters: 40ms difference is a continuous reader discrepancy;
    # it is NOT the same event as a pair crossing the 400ms threshold (both happen to count 88).
    assert summaries[0]['paired_binary_disagreements']==88
    assert sum(int(r['abs_disagreement_ge_40ms']) for r in raw if r['paired_complete']=='1')==88
    output={'official_name':'MQR-4.101 — Fallible Reference Standards, Selective Adjudication & Dependence-Robust Risk Identifiability',
       'stage':'P1 OPEN; source-conditional operational binary contrast',
       'source':'PhysioNet QTDB 1.0.0 / P8 publisher-hash-pinned per-beat receipt; not new human judgement',
       'input_source_file_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
       'input_csv_sha256':hashlib.sha256(data).hexdigest(),
       'archive':archive_info,'number_of_ecg_records':11,'records':rec_order,
       'sources_not_available':['independent truth', 'reference error budget', 'external population target weights',
                                'reader blinding documentation', 'adjudicator-protocol exchangeability'],
       'core_math':{'truth_free_risk_interval':[0,1],
           'external_certified_k_reference_error_bound':'[max(0,e-k), e+min(k,m-e)+(n-m)]/n sharp',
           'no_missing_and_perfect_reference':'risk=e/n when n=m and k=0',
           'reader_agreement_is_not_truth':'the same 2 ratings permit latent truth = either reader or opposite prediction',
           'transport_caveat':'equal-record pooling and beat-weight pooling different functionals; neither is population transfer'},
       'sensitivity':summaries,'by_record':details}
    outdir.mkdir(parents=True,exist_ok=True)
    (outdir/'p1_source_risk_receipt.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    with (outdir/'p1_per_record_binary_crossings.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(details[0]));writer.writeheader();writer.writerows(details)
    print(json.dumps({'rows':len(raw),'m':m,'cutoff_disagreements':{str(z['cutoff_ms']):z['paired_binary_disagreements'] for z in summaries},
         'cut440_k0':summaries[2]['pooled_hypothetical_external_reference_mistake_budget']['0'],
         'cut440_k10':summaries[2]['pooled_hypothetical_external_reference_mistake_budget']['10']},sort_keys=True))
    print('MQR4101_P1_AUTHENTIC_P8_RECEIPT_BINARY_REFERENCE_RISK_GATE_PASS;TRUE_RISK_AND_TRANSPORT_HOLD')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source-archive',type=pathlib.Path)
    p.add_argument('--source-csv',type=pathlib.Path)
    p.add_argument('--out',type=pathlib.Path);p.add_argument('--selftest',action='store_true')
    args=p.parse_args();
    if args.selftest:test_small_exhaustive()
    else:
        assert args.out and (bool(args.source_archive) != bool(args.source_csv))
        audit(args.source_csv or args.source_archive,args.out,bool(args.source_csv))
