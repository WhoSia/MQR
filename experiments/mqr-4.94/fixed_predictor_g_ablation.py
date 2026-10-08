#!/usr/bin/env python3
"""MQR 4.94 second-stage retrospective G ablation, fixed FIT and target P.

Designed after original five-run outcomes; reduces model-fit confounding
but does not identify causal impact of spatial proximity.
"""
import json, math
from collections import Counter
from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from serov_active_source_species_audit import ACTIVE, fetch_pinned
from serov_author_function_replay import source_functions, verified_original_code, COMMIT
from serov_geosite_original_risk import (FILE,build_unlabeled_frame,unique_sites,array_x,
    read_selected_labels,summary,digest,geo_min_km)
from spatial_risk_identification import contracts,nearest_stats

OUT=Path("mqr494-fixed-predictor-validation-ablation.json")

def main():
    sha,cap=ACTIVE["anemone"]
    raw=fetch_pinned(FILE,sha,cap)
    frame,drops=build_unlabeled_frame(raw)
    if len(frame)!=2905:raise AssertionError("source frame drift")
    block=next(g for g in contracts(frame) if g["name"]=="west_q50_east_q75_latitude_blocked_G")
    fit=block["fit"]
    far=block["g"]
    target=block["p"]
    west=unique_sites([r for r in frame if r["lon"]<=block["w_cut"]],"WEST")
    fit_sites={r["site"] for r in fit}
    near_candidates=[r for r in west if r["lat"]<=block["f_lat_cut"] and r["site"] not in fit_sites]
    near=sorted(near_candidates,key=lambda r:(digest("mqr494-blockG-near|"+r["site"]),r["site"]))[:64]
    if len(near)!=64:raise AssertionError("NEAR_G_INFEASIBLE")
    if len({r["site"] for r in fit+far+near+target})!=512+64+64+64:
        raise AssertionError("unexpected shared geographic site")
    source_labels=read_selected_labels(raw,{r["row"] for r in fit+far+near})
    yfit=np.array([source_labels[r["row"]] for r in fit])
    if len(np.unique(yfit))!=2:raise AssertionError("source FIT classes missing")
    scale=StandardScaler().fit(array_x(fit))
    clf=LogisticRegression(C=1.0,max_iter=2000,random_state=493)
    clf.fit(scale.transform(array_x(fit)),yfit)
    xp=scale.transform(array_x(target))
    probs=np.clip(clf.predict_proba(xp)[:,1],1e-10,1-1e-10)
    author=source_functions(verified_original_code())
    estimators={}
    for key,items in (("G_near_southern",near),("G_far_northern",far)):
        xg=scale.transform(array_x(items))
        yg=np.array([source_labels[r["row"]] for r in items])
        pg=np.clip(clf.predict_proba(xg)[:,1],1e-10,1-1e-10)
        loss=-yg*np.log(pg)-(1-yg)*np.log1p(-pg)
        def loss_closure(x):
            if not np.array_equal(x,xg):raise AssertionError("G loss closure mismatch")
            return np.log(loss)
        nw=float(np.exp(author["MCE"](loss_closure,xg)))
        kmm=float(np.exp(author["KMM_error"](loss_closure,xp,xg,10.0)))
        weights=np.asarray(author["kernel_mean_matching"](xp,xg,kern="rbf",B=10.0)).ravel()
        if not math.isclose(nw,float(np.mean(loss)),rel_tol=1e-9,abs_tol=1e-10):raise AssertionError("NW mismatch")
        if not math.isclose(kmm,float(np.dot(weights,loss)/64),rel_tol=1e-9,abs_tol=1e-10):raise AssertionError("KMM mismatch")
        estimators[key]={"source_G":summary(items,source_labels),
            "G_nearest_FIT":nearest_stats(fit,items),
            "NW_risk":nw,"KMM_risk":kmm,
            "KMM_ESS":float(np.sum(weights)**2/np.dot(weights,weights)),
            "KMM_weight_sum":float(np.sum(weights))}
    baseline=estimators["G_far_northern"]
    if not math.isclose(baseline["NW_risk"],1.1030750271157368,rel_tol=1e-9,abs_tol=1e-10):
        raise AssertionError("previous same-fit far-G NW not identical")
    if not math.isclose(baseline["KMM_risk"],.7958976661740039,rel_tol=1e-9,abs_tol=1e-10):
        raise AssertionError("previous same-fit far-G KMM not identical")
    # target labels accessed only after both G-based estimators and all sites frozen
    target_labels=read_selected_labels(raw,{r["row"] for r in target})
    yp=np.array([target_labels[r["row"]] for r in target])
    oracle=float(np.mean(-yp*np.log(probs)-(1-yp)*np.log1p(-probs)))
    if not math.isclose(oracle,.89985903200522,rel_tol=1e-9,abs_tol=1e-10):
        raise AssertionError("fixed predictor/target original oracle disagrees")
    for item in estimators.values():
        item["NW_oracle_gap"]=abs(item["NW_risk"]-oracle)
        item["KMM_oracle_gap"]=abs(item["KMM_risk"]-oracle)
        item["closer"]="NW" if item["NW_oracle_gap"]<item["KMM_oracle_gap"] else "KMM"
    report={"status":"RETROSPECTIVE_FIXED_PREDICTOR_G_VALIDATION_ABLATION_PASS",
        "source":"Serov2026 pinned original Anemone source, one publication root",
        "commit":COMMIT,"original_blob":sha,
        "timing":"Designed AFTER original 4.94 winner reversal: hypothesis-challenging only",
        "same_source_FIT":summary(fit,source_labels),
        "same_target":summary(target,target_labels),
        "target_oracle_posthoc":oracle,
        "same_fixed_predictor_training":True,
        "source_g_eligibility":{"near_southern_available":len(near_candidates),
                                "far_northern_available":len([r for r in west if r["lat"]>=block["g_lat_cut"]])},
        "source_g_diagnostics":estimators,
        "limitations":["Distance, validation site composition, validation label prevalence and sampling years change together",
          "One retrospective same-publisher geographic target; not independent prospective replication",
          "Reweighting method performance cannot be causally assigned to geographic distance alone",
          "Source FIT model is fixed but geographical source G is not a randomized intervention"]}
    OUT.write_text(json.dumps(report,indent=2),encoding="utf-8")
    for k,v in estimators.items():
        print("MQR494_FIXED_G="+json.dumps({"group":k,**v},sort_keys=True))
    print("MQR494_FIXED_PREDICTOR_ABLATION=PASS")

if __name__=="__main__":main()
