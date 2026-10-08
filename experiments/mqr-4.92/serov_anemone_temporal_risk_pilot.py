#!/usr/bin/env python3
"""MQR 4.92: PRECOMMITTED tiny real-data source-risk pilot on independent Serov data.

2026-10-08 design fixed BEFORE observed outcomes:
- original Git-blob-pinned 'anemone.csv' source, all 19 bio features,
- source fit on years 2000–2012, source validation on 2013–2016,
  temporal target evaluation on 2017–2024,
- no model/weight/metric tuning on target y,
- deterministic outcome-blind subsampling up to 1200/64/64,
- author-original NW and KMM estimator function code pinned and unmodified.
This differs from Serov et al.'s reported paper experimental protocol, so
the result is a bounded independent-source pipeline pilot, NOT replication
of published performance or a spatial shift effect.
"""
import csv,hashlib,io,json,math
from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from serov_active_source_species_audit import fetch_pinned, ACTIVE
from serov_author_function_replay import verified_original_code, source_functions, COMMIT

DATA="anemone"
PATH="datasets/species/anemone.csv"
PARTS={"fit":(2000,2012,1200),"source_holdout":(2013,2016,64),"target_holdout":(2017,2024,64)}
OUT=Path("mqr492-anemone-predeclared-real-source-risk.json")

def sample_data():
    digest,limit=ACTIVE[DATA]
    raw=fetch_pinned(PATH,digest,limit)
    reader=csv.DictReader(io.StringIO(raw.decode("utf-8-sig"),newline=""))
    cohorts={k:[] for k in PARTS}
    dropped={"invalid_label":0,"missing_bio":0,"outside_period":0}
    feature_names=[f"bio{i}" for i in range(1,20)]
    for row_number,row in enumerate(reader,2):
        ystr=(row.get("presence") or "").strip()
        if ystr not in ("0","1"):
            dropped["invalid_label"]+=1;continue
        try:
            year=int(float(row["year"]))
            x=np.array([float(row[k]) for k in feature_names],dtype="float64")
            if not bool(np.all(np.isfinite(x))):raise ValueError("nonfinite climate")
        except (ValueError,KeyError,TypeError):
            dropped["missing_bio"]+=1;continue
        group=next((k for k,(a,b,_) in PARTS.items() if a<=year<=b),None)
        if group is None:
            dropped["outside_period"]+=1;continue
        sortkey=hashlib.sha256(f"mqr492-p0-fixed|{PATH}|{row_number}|{group}".encode()).digest()
        cohorts[group].append((sortkey,x,int(ystr),year))
    counts={k:len(v) for k,v in cohorts.items()}
    chosen={}
    for group,items in cohorts.items():
        n=PARTS[group][2]
        if len(items)<n:raise ValueError(f"insufficient original source rows for predeclared cohort {group}")
        chosen[group]=sorted(items,key=lambda z:z[0])[:n]
    return counts,chosen,dropped

def arrays(records):
    X=np.stack([v[1] for v in records]);y=np.array([v[2] for v in records],dtype="int64")
    return X,y

def main():
    original_sha=ACTIVE[DATA][0]
    cohorts,chosen,dropped=sample_data()
    train_x,train_y=arrays(chosen["fit"])
    val_x,val_y=arrays(chosen["source_holdout"])
    target_x,target_y=arrays(chosen["target_holdout"])
    if len(np.unique(train_y))!=2:
        raise ValueError("predeclared fitting slice has no two supervised classes")
    scale=StandardScaler().fit(train_x)
    xs=scale.transform(train_x);g=scale.transform(val_x);p=scale.transform(target_x)
    clf=LogisticRegression(C=1.0,max_iter=2000,random_state=492)
    clf.fit(xs,train_y)
    eps=1e-10
    def loss(x,y):
        pred=np.clip(clf.predict_proba(x)[:,1],eps,1-eps)
        return -y*np.log(pred)-(1-y)*np.log(1-pred)
    l_g=loss(g,val_y);l_p=loss(p,target_y)
    if any(not np.all(np.isfinite(x)) for x in (l_g,l_p)):
        raise ValueError("nonfinite original-data logloss")
    upstream=source_functions(verified_original_code())
    def source_error(x):
        if not np.array_equal(x,g):raise ValueError("loss closure must use only source heldout labels")
        return np.log(l_g)
    source_risk=float(np.exp(upstream["MCE"](source_error,g)))
    B=10.0
    kmm_risk=float(np.exp(upstream["KMM_error"](source_error,p,g,B)))
    target_oracle=float(np.mean(l_p))
    w=upstream["kernel_mean_matching"](p,g,kern="rbf",B=B)
    if not math.isclose(float(np.dot(w,l_g)/len(g)),kmm_risk,rel_tol=1e-9,abs_tol=1e-10):
        raise AssertionError("source function estimator and author original weights numerically disagree")
    if not math.isclose(float(np.mean(l_g)),source_risk,rel_tol=1e-10):
        raise AssertionError("source NW estimator vs independent source validation loss mismatch")
    result={
      "status":"BOUNDED_REAL_ORIGINAL_DATA_ESTIMATOR_PILOT_PASS",
      "original_study":"Serov-Koldasbayeva-Zaytsev 2026 Scientific Reports",
      "repo":"egorser0v/Importance-reweighting","upstream_commit":COMMIT,
      "source_data_file":PATH,"source_data_git_blob_sha1":original_sha,
      "source_estimator_file":"source/estimations.py",
      "design":"year-based non-spatial heldout; 19 original BIO features, binary presence",
      "periods":{k:list(v[:2]) for k,v in PARTS.items()},
      "original_eligible_row_counts":cohorts,
      "chosen_sizes":{k:len(v) for k,v in chosen.items()},
      "class_positive_by_chosen_group":{
        "fit":int(np.sum(train_y)),"source_holdout":int(np.sum(val_y)),
        "target_holdout":int(np.sum(target_y))},
      "excluded_source_rows":dropped,
      "risk_metrics":{"source_NW_unweighted_log_loss":source_risk,
         "source_KMM_reweighted_log_loss":kmm_risk,
         "target_oracle_log_loss_evaluation_only":target_oracle,
         "NW_absolute_target_error":abs(source_risk-target_oracle),
         "KMM_absolute_target_error":abs(kmm_risk-target_oracle)},
      "kmm_weight_summary":{"min":float(np.min(w)),"max":float(np.max(w)),
          "sum":float(np.sum(w))},
      "provenance_guard":{
        "target_Y_used_for_training":False,
        "target_Y_used_for_reweighting":False,
        "target_Y_used_only_for_final_oracle":True,
        "target_X_used_to_compute_weights":True,
        "source_Y_used_for_fitting_and_source_validation":True},
      "nonadmissions":[
        "Temporal holdout is not a spatial generalization benchmark",
        "Subsampled new experimental design is not the original author reported risk experiment",
        "A single 64+64 holdout yields no independent population-level confidence interval",
        "The same study's target labels are available solely for post-hoc oracle evaluation",
        "This does not establish KMM is superior to NW or a novel MQR method"
      ]}
    OUT.write_text(json.dumps(result,indent=2),encoding="utf8")
    print("MQR492_REAL_SOURCE_COHORTS="+json.dumps(result["chosen_sizes"]))
    print("MQR492_REAL_SOURCE_RISK="+json.dumps(result["risk_metrics"],sort_keys=True))
    print("MQR492_SEROV_REAL_ORIGINAL_DATA_PILOT=PASS")

if __name__=="__main__":main()
