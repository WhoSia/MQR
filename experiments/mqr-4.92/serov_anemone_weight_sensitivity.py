#!/usr/bin/env python3
"""MQR 4.92: source-only preregistered KMM sensitivity and balance diagnostics.

Not a published Serov replication, novel estimator, or causal attribution.
The original immutable anemone cohort, model and KMM are reconstructed without
changing the 2013–18 / 2019–20 / 2021–24 split or using target labels for design.
Only post-hoc target oracle evaluation is allowed. Weighted clipping variants
are DIAGNOSTIC, NOT the original author's KMM algorithm.
"""
import json
import math
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from serov_anemone_temporal_risk_pilot import arrays, sample_data, PARTS, DATA, PATH
from serov_active_source_species_audit import ACTIVE
from serov_author_function_replay import verified_original_code, source_functions, COMMIT

OUT=Path("mqr492-kmm-weight-sensitivity.json")
QUANTILES=(0.90,0.95)
FIT_EXPECT=512
HOLD_EXPECT=64
B=10.0

def ess(weights):
    w=np.asarray(weights,dtype=float).ravel()
    if not np.all(np.isfinite(w)) or np.any(w < 0) or np.sum(w)<=0:
        raise AssertionError("inadmissible weights")
    return float(np.sum(w)**2/np.dot(w,w))

def balance(weights,source_x,target_x):
    w=np.asarray(weights,dtype=float).ravel()
    if len(w)!=len(source_x): raise AssertionError("weight/data mismatch")
    mu_s=np.sum(source_x*w[:,None],axis=0)/np.sum(w)
    mu_t=np.mean(target_x,axis=0)
    sd=np.std(source_x,axis=0,ddof=1)
    fixed=np.where(sd>1e-12,sd,1.0)
    z=np.abs((mu_s-mu_t)/fixed)
    return {
      "mean_abs_source_sd":float(np.mean(z)),
      "max_abs_source_sd":float(np.max(z)),
      "zero_or_tiny_source_sd_features":int(np.sum(sd<=1e-12)),
      "per_bio_abs_source_sd":[float(k) for k in z]
    }

def proposed_diagnostics(raw_weights,source_x,target_x,source_losses):
    w=np.asarray(raw_weights,dtype=float).ravel()
    if len(w)!=HOLD_EXPECT or len(w)!=len(source_losses):
        raise AssertionError("unexpected source validation size")
    n=len(w)
    variants={"published_original_KMM_unmodified":w,"unweighted":np.ones(n)}
    caps={}
    for q in QUANTILES:
        cap=float(np.quantile(w,q))
        wcap=np.minimum(w,cap)
        if not np.sum(wcap)>0:raise AssertionError("zero clipped weights")
        wc=wcap*n/np.sum(wcap)
        name=f"diagnostic_source_only_clip_p{int(q*100)}_renormalized"
        variants[name]=wc
        caps[name]=cap
    results={}
    for k,v in variants.items():
        risk=float(np.dot(v,source_losses)/n)
        if not math.isfinite(risk):raise AssertionError("nonfinite risk")
        results[k]={
            "source_estimated_log_loss":risk,
            "ESS":ess(v),
            "weight_sum":float(np.sum(v)),
            "weight_max":float(np.max(v)),
            "top5_fraction_weight_mass":float(np.sum(np.sort(v)[-5:])/np.sum(v)),
            "weighted_feature_balance":balance(v,source_x,target_x)
        }
    for name in caps:
        v=variants[name]
        delta=float(np.abs(np.dot(w-v,source_losses))/n)
        l1_bound=float(np.max(np.abs(source_losses))*np.sum(np.abs(w-v))/n)
        if delta>l1_bound+1e-10:
            raise AssertionError("failed finite-sample holder inequality")
        results[name]["risk_change_vs_original_KMM"]=delta
        results[name]["upper_bound_maxloss_times_weight_L1"]=l1_bound
        results[name]["source_only_cap"]=caps[name]
    return results

def main():
    cohorts,chosen,dropped=sample_data()
    fit_x,fit_y=arrays(chosen["fit"])
    val_x,val_y=arrays(chosen["source_holdout"])
    target_x,target_y=arrays(chosen["target_holdout"])
    if (len(fit_x),len(val_x),len(target_x)) != (FIT_EXPECT,HOLD_EXPECT,HOLD_EXPECT):
        raise AssertionError("frozen source cohort sizes changed")
    if set(np.unique(fit_y))!={0,1}:
        raise AssertionError("no two training classes")
    scaler=StandardScaler().fit(fit_x)
    fit_scaled=scaler.transform(fit_x)
    val_scaled=scaler.transform(val_x)
    target_scaled=scaler.transform(target_x)
    clf=LogisticRegression(C=1.0,max_iter=2000,random_state=492).fit(fit_scaled,fit_y)
    def logloss(x,y):
        pred=np.clip(clf.predict_proba(x)[:,1],1e-10,1-1e-10)
        return -y*np.log(pred)-(1-y)*np.log(1-pred)
    source_losses=logloss(val_scaled,val_y)
    author=source_functions(verified_original_code())
    raw_w=author["kernel_mean_matching"](target_scaled,val_scaled,kern="rbf",B=B)
    raw_w=np.asarray(raw_w,dtype=float).ravel()
    def source_log_loss(x):
        if not np.array_equal(x,val_scaled):
            raise AssertionError("loss closure must use source only")
        return np.log(source_losses)
    published_mce=float(np.exp(author["MCE"](source_log_loss,val_scaled)))
    published_kmm=float(np.exp(author["KMM_error"](source_log_loss,target_scaled,val_scaled,B)))
    variants=proposed_diagnostics(raw_w,val_scaled,target_scaled,source_losses)
    orig=variants["published_original_KMM_unmodified"]["source_estimated_log_loss"]
    if not math.isclose(orig,published_kmm,rel_tol=1e-9,abs_tol=1e-10):
        raise AssertionError("original KMM function disagreement")
    if not math.isclose(float(np.mean(source_losses)),published_mce,rel_tol=1e-10):
        raise AssertionError("original MCE function disagreement")
    if not math.isclose(ess(raw_w),5.4858,rel_tol=5e-4):
        raise AssertionError("previous pinned-run ESS mismatch")
    # ONLY NOW reveal/evaluate post-hoc target labels; no oracle-tuned caps.
    oracle=float(np.mean(logloss(target_scaled,target_y)))
    for record in variants.values():
        record["posthoc_oracle_absolute_gap"]=abs(record["source_estimated_log_loss"]-oracle)
    report={
      "status":"BOUNDED_ORIGINAL_DATA_DIAGNOSTIC",
      "source":"Serov 2026 author original estimators and immutable anemone data",
      "upstream_commit":COMMIT,
      "source_dataset":PATH,
      "source_blob_sha1":ACTIVE[DATA][0],
      "frozen_periods":{k:list(v[:2]) for k,v in PARTS.items()},
      "source_eligible_rows":cohorts,"source_drops":dropped,
      "chosen_sizes":{k:len(v) for k,v in chosen.items()},
      "design_and_leakage":"Target labels prohibited until posthoc oracle evaluation; clips use original source KMM weights only; features may use unlabeled target X; caps p90,p95 fixed before running",
      "author_MCE_risk":published_mce,
      "author_KMM_risk":published_kmm,
      "heldout_target_oracle_posthoc":oracle,
      "variants":variants,
      "limits":[
        "Single nonspatial temporal sample cannot identify spatial transport",
        "Clipped estimator is research sensitivity not original published KMM",
        "No oracle-based optimization, no confidence interval, no causal claim",
        "Source-scaled feature mean balance is a proxy, not proof of covariate density ratio",
        "Same publisher source, not a second independent publication",
        "ESS does not account for space-time dependence, conditional loss shift or target y mechanism",
        "No tuned higher-performance method is admitted even if clipping improves one oracle gap",
      ],
    }
    OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    for k,d in variants.items():
        print("MQR492_VARIANT="+json.dumps({"variant":k,"risk":d["source_estimated_log_loss"],"ess":d["ESS"],"gap":d["posthoc_oracle_absolute_gap"],"balance":d["weighted_feature_balance"]["mean_abs_source_sd"]},sort_keys=True))
    print("MQR492_WEIGHT_DIAGNOSTIC=PASS")

if __name__=="__main__": main()
