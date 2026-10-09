#!/usr/bin/env python3
"""MQR-4.101 P2: exact source-native selection / dependence-robust bounds.
No clinical diagnosis, independent truth or missing-at-random premise. Stdlib only.
"""
import argparse
import collections
import csv
import hashlib
import io
import itertools
import json
from pathlib import Path
import zipfile

INPUT_SHA = 'd441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842'
CUTS = (400,420,440,460,480)


def partition_bound(disag:int, agree:int, missing:int, k_disag:int, k_agree:int):
    """Sharp bound under separate EXTERNALLY certified per-group reference-error caps.
    All observed cases have known h and fallible B; no independence required.
    """
    if min(disag,agree,missing,k_disag,k_agree) < 0 or k_disag>disag or k_agree>agree:
        raise ValueError('bad table / reference error caps')
    return (disag - k_disag, disag + k_agree + missing)


def pooled_bound(disag:int, agree:int, missing:int, k:int):
    if not 0<=k<=disag+agree:raise ValueError('bad k')
    return max(0,disag-k), disag+min(k,agree)+missing


def finite_exhaustive():
    cases=0
    # independent truth assignments to observed paired agreement/disagreement and missing.
    for n in range(1,7):
        for cells in itertools.product(('D','G','U'),repeat=n):
            d=cells.count('D');g=cells.count('G');u=cells.count('U')
            for kd in range(d+1):
                for kg in range(g+1):
                    attainable=[]
                    for errors in itertools.product((0,1),repeat=n):
                        err_d=sum(v for z,v in zip(cells,errors) if z=='D')
                        err_g=sum(v for z,v in zip(cells,errors) if z=='G')
                        # On D: B error = 1 if h error 0. On G: B error = 1 if h error 1.
                        if d-err_d <=kd and err_g <=kg:
                            attainable.append(sum(errors))
                    bound=partition_bound(d,g,u,kd,kg)
                    assert (min(attainable),max(attainable))==bound,(cells,kd,kg,bound)
                    cases+=1
    return cases


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--csv',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    original=args.csv.read_bytes()
    assert hashlib.sha256(original).hexdigest()==INPUT_SHA, 'P8 SHA-256 source drift'
    rows=list(csv.DictReader(io.StringIO(original.decode('utf-8'))))
    assert len(rows)==487
    counts=collections.defaultdict(lambda:dict(n=0,paired=0,missing=0,disagreement=0,agreement=0))
    details=[]
    for cutoff in CUTS:
        byrec=collections.defaultdict(lambda:dict(n=0,paired=0,missing=0,disagreement=0,agreement=0))
        for r in rows:
            a=byrec[r['record']]
            a['n']+=1
            if r['paired_complete']=='1':
                assert r['q1_QT_ms'] and r['q2_QT_ms']
                d=(float(r['q1_QT_ms'])>=cutoff)!=(float(r['q2_QT_ms'])>=cutoff)
                a['paired']+=1;a['disagreement']+=int(d);a['agreement']+=int(not d)
            else:
                assert r['paired_complete']=='0'
                assert not (r['q1_QT_ms'] and r['q2_QT_ms'])
                a['missing']+=1
        for rec in sorted(byrec):
            a=byrec[rec];assert a['n']==a['paired']+a['missing']
            details.append(dict(cutoff=cutoff,record=rec,**a))
        if cutoff==440:counts=byrec
    assert sum(x['n'] for x in counts.values())==487
    assert sum(x['paired'] for x in counts.values())==402
    assert sum(x['disagreement'] for x in counts.values())==76
    assert sorted((k,v['missing']) for k,v in counts.items() if v['missing'])==[('sel102',83),('sel213',2)]
    assert counts['sel223']['disagreement']==26 and counts['sel223']['paired']==31
    paired=402;d=76;agree=326;u=85
    tests=finite_exhaustive()
    scenarios={
      'NO_EXTERNAL_CERTIFICATE': {'truth_error_counts':[0,487], 'status':'ACTUAL_AUTHORITY_HOLD'},
      'HYPOTHETICAL_P1_POOLED_K10':{'truth_error_counts':list(pooled_bound(d,agree,u,10)),'status':'UNVERIFIED_SENSITIVITY'},
      'HYPOTHETICAL_PAIR_GROUP_KD7_KG3':{'truth_error_counts':list(partition_bound(d,agree,u,7,3)),'status':'UNVERIFIED_SENSITIVITY'},
      'HYPOTHETICAL_PAIR_GROUP_KD10_KG0':{'truth_error_counts':list(partition_bound(d,agree,u,10,0)),'status':'UNVERIFIED_SENSITIVITY'},
      'HYPOTHETICAL_PAIR_GROUP_KD0_KG10':{'truth_error_counts':list(partition_bound(d,agree,u,0,10)),'status':'UNVERIFIED_SENSITIVITY'},
      'HYPOTHETICAL_PAIRED_PERFECT_B_10_MISSING_TRUTH_AUDITED':{'truth_error_counts_if_10_new_truth_labels_include_v_errors':[76,151,'+ v with 0<=v<=10'], 'status':'FUTURE_DESIGN_ONLY'}
    }
    assert scenarios['HYPOTHETICAL_PAIR_GROUP_KD7_KG3']['truth_error_counts']==[69,164]
    assert scenarios['HYPOTHETICAL_PAIR_GROUP_KD10_KG0']['truth_error_counts']==[66,161]
    assert scenarios['HYPOTHETICAL_PAIR_GROUP_KD0_KG10']['truth_error_counts']==[76,171]
    assert scenarios['HYPOTHETICAL_P1_POOLED_K10']['truth_error_counts']==[66,171]
    result={
      'project':'MQR-4.101 — Fallible Reference Standards, Selective Adjudication & Dependence-Robust Risk Identifiability',
      'stage':'P2 BOUNDED SOURCE AUDIT, EXTERNAL TRUTH HOLD',
      'source_sha256':INPUT_SHA,'source_records':11,'n':487,'complete_qt_pairs':402,'incomplete_qt_pairs':85,
      'probe_cutoff_ms':440,'nonclinical_probe':True,
      'agreement':326,'disagreement':76,
      'missing_by_record':{'sel102':83,'sel213':2},
      'sel102':counts['sel102'],'sel223':counts['sel223'],
      'observed_review_selection_not_mar_proof':True,
      'no_independent_truth_no_error_independence':True,
      'scenarios':scenarios,'stratified_bound_formula':'[D-k_D,D+k_G+U] where D disagreements, G agreements, U missing, and external reference-error caps k_D<=D, k_G<=G; sharp finite Hamming result; not a novel theorem',
      'external_certificates_acquired':0,
      'method':'exact 487-row source-native grouping; no resampling or latent truth imputation',
      'finite_exhaustive_cases':tests,
      'per_record_all_cutoffs':details,
      'selection_caveat':'Even fully audited selected sample does NOT transport to unobserved target persons without sampling/coverage contract; selected 11 records and expert reading are not randomized.',
      'evidence_gate':'MQR4101_P2_SOURCE_SELECTIVE_COVERAGE=PASS;REFERENCE_TRUTH_DEPENDENCE_RISK=HOLD'
    }
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/'p2_source_and_bounds.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
    with (args.out/'p2_per_record_selection.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(details[0]));w.writeheader();w.writerows(details)
    print('P2_487_SOURCE_ROWS',len(rows),'P2_PAIR_D_G_U',(d,agree,u),'P2_MISSING_BY_RECORD',result['missing_by_record'])
    print('P2_SHARP_EXHAUSTIVE_CASES',tests)
    print('P2_OBSERVED_TRUTH_RISK_IDENTIFIED=NO;EXTERNAL_CERTIFICATES=NONE')
    print(result['evidence_gate'])

if __name__=='__main__':main()
