#!/usr/bin/env python3
"""MQR-4.102: finite-source adjudication allocation value, not acquired truth.
Compare binary h1/h2 on existing P8-derived 487-row PhysioNet QTDB receipt.
All validation outcomes are symbolic: no external T observed, clinical inference HOLD.
"""
import argparse
import collections
import csv
import hashlib
import itertools
import json
from pathlib import Path

SOURCE_SHA="d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842"
CUTOFF=440
N=487
M=402
D=76
U=85
BUDGET=10

def exact_diff_interval(d:int, signed_verified:int, reviewed_disagreements:int):
    """For unverified discordant cases, each contributes independently ±1."""
    if not(0<=reviewed_disagreements<=d): raise ValueError("invalid audit")
    remaining=d-reviewed_disagreements
    if abs(signed_verified)>reviewed_disagreements or (signed_verified-reviewed_disagreements)%2:
        raise ValueError("invalid signed audit observation")
    return signed_verified-remaining,signed_verified+remaining

def fallible_audit_interval(d:int, review_signs, max_errors:int):
    """At most max_errors review labels faulty among externally checked discordant cases.
    This is an *assumption*, NOT established by the QTDB two annotators.
    """
    signs=list(review_signs)
    if not(0<=len(signs)<=d and 0<=max_errors<=len(signs)):
        raise ValueError("bad reviewer certificate")
    if any(v not in (-1,1) for v in signs): raise ValueError("not a sign")
    pos=sum(v==1 for v in signs)
    neg=len(signs)-pos
    observed=sum(signs)
    other=d-len(signs)
    return observed-2*min(max_errors,pos)-other,observed+2*min(max_errors,neg)+other

def exhaustive():
    checked=0
    for d in range(0,9):
        for m in range(d+1):
            for signs in itertools.product((-1,1),repeat=m):
                got=exact_diff_interval(d,sum(signs),m)
                actual=[sum(signs)+sum(z) for z in itertools.product((-1,1),repeat=d-m)]
                assert got==(min(actual),max(actual)),(d,m,signs)
                for k in range(m+1):
                    got2=fallible_audit_interval(d,signs,k)
                    poss=[]
                    for positions in itertools.combinations(range(m),0): pass
                    for true_signs in itertools.product((-1,1),repeat=m):
                        if sum(v!=w for v,w in zip(signs,true_signs))<=k:
                            poss.extend(sum(true_signs)+sum(z) for z in itertools.product((-1,1),repeat=d-m))
                    assert got2==(min(poss),max(poss)),(d,m,k,signs)
                checked+=1
    return checked

def calculate(input_file:Path):
    data=input_file.read_bytes()
    if hashlib.sha256(data).hexdigest()!=SOURCE_SHA: raise ValueError("P8 derived source-byte drift")
    rows=list(csv.DictReader(data.decode("utf-8").splitlines()))
    assert len(rows)==N
    groups=collections.defaultdict(lambda:dict(total=0,paired=0,discord=0))
    paired=[]
    for r in rows:
        t=groups[r["record"]]
        t["total"]+=1
        if r["paired_complete"]=="1":
            t["paired"]+=1
            a=int(float(r["q1_QT_ms"])>=CUTOFF)
            b=int(float(r["q2_QT_ms"])>=CUTOFF)
            discord=a!=b
            t["discord"]+=int(discord)
            paired.append((r,discord))
    assert len(groups)==11 and len(paired)==M
    d=sum(is_discord for _,is_discord in paired)
    assert d==D and sum(x["total"]-x["paired"] for x in groups.values())==U
    assert groups["sel102"]==dict(total=85,paired=2,discord=0)
    assert groups["sel223"]==dict(total=31,paired=31,discord=26)
    by_record=[{"record":rec,**v,"unpaired":v["total"]-v["paired"],"max_equal_record_delta_contribution":v["discord"]/(11*v["paired"])}
               for rec,v in sorted(groups.items())]
    disagreement_cases=[(r["record"],int(r["selected_beat_index"])) for r,diff in paired if diff]
    assert len(set(disagreement_cases))==D
    # The 10 audit targets selected from OBSERVED disagreement, never using truth.
    target10=sorted(disagreement_cases)[:BUDGET]
    # Record-equally weighted target: maximize worst-case identification-width reduction
    # by taking discordant cases in the smallest *observed pair count* records.
    weighted10=sorted(disagreement_cases,key=lambda v:(groups[v[0]]["paired"],v[0],v[1]))[:BUDGET]
    assert len(target10)==len(weighted10)==BUDGET
    equal_record_r0=sum(v["discord"]/v["paired"] for v in groups.values())/11
    weighted_gain=sum(2/(11*groups[rec]["paired"]) for rec,_ in weighted10)
    result={
      "project":"MQR-4.102 — Adjudication Allocation, Decision-Contrast Identification & Selection-Robust Verification Value",
      "source":"P8-derived authentic-PhysioNet two-reader observations only",
      "sha256":SOURCE_SHA,"nonclinical_threshold_ms":CUTOFF,
      "full_receipt_size":N,"paired_target_size":M,"unpaired_second_reader":U,
      "source_selected_beats_not_a_random_population":True,
      "truth_relabels_acquired":0,
      "observed_pair_agreement":M-D,"observed_pair_disagreement":D,
      "per_record":by_record,
      "truth_unconstrained":{
         "absolute_risk_h1_count_interval":[0,M],
         "absolute_risk_h1_rate_interval":[0,1],
         "decision_difference_count_interval":[-D,D],
         "decision_difference_rate_interval":[-D/M,D/M]},
      "hypothetical_perfect_external_review_of_ten_disagreements":{
         "candidate_addresses":target10,
         "true_difference_count_interval_symbolic":["S_10-66","S_10+66"],
         "S_10_is_not_observed":True,
         "decision_difference_interval_total_width":2*(D-BUDGET)/M,
         "absolute_risk_interval_total_width":(M-BUDGET)/M,
         "fraction_that_is_idealized_not_empirically_certified":1},
      "hypothetical_review_of_ten_agreements":{
         "difference_interval_unshrunk":[-D,D],
         "difference_interval_total_width":2*D/M,
         "absolute_risk_interval_total_width":(M-BUDGET)/M},
      "uniform_random_ten_without_replacement_expected_discordances":BUDGET*D/M,
      "uniform_random_ten_expected_difference_width":2*(D-BUDGET*D/M)/M,
      "equal_record_average_difference_bounds":[-equal_record_r0,equal_record_r0],
      "equal_record_optimal_ten_discordant_addresses":weighted10,
      "equal_record_optimal_ten_full_width_reduction":weighted_gain,
      "equal_record_optimally_reviewed_resulting_full_width":2*equal_record_r0-weighted_gain,
      "missing_second_expert_in_85_prevents_defining_h2_on_full_487_without_a_declared_extension":True,
      "bounds_source":"sharp finite sums of independent free binary truth assignments; pre-existing Hamming/Fréchet logic",
      "authority":"MATHEMATICAL_VERIFICATION_ONLY;THIRD_PARTY_TRUTH=HOLD;RISK_TRANSPORT=HOLD",
    }
    assert abs(result["hypothetical_perfect_external_review_of_ten_disagreements"]["decision_difference_interval_total_width"]-132/402)<1e-12
    assert abs(result["uniform_random_ten_without_replacement_expected_discordances"]-760/402)<1e-12
    assert abs(weighted_gain-2/33)<1e-12
    return result

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--csv",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    count=exhaustive()
    result=calculate(args.csv)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    result["exhaustive_small_model_cases"]=count
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    print("MQR4102_FINITE_SELECTION_VALUE_SOURCE_AUDIT=PASS;INDEPENDENT_TRUTH=HOLD", "N",M,"D",D,"cases",count)
