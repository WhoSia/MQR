#!/usr/bin/env python3
"""MQR 4.94: frozen retrospective geographic risk-contract challenge.

ONE pinned Serov author source, 4 longitude contracts + 1 spatially blocked
source validation. All target labels are read only after computing estimators
and sharp unlabeled finite-site loss bounds. See 4.94 opening precommit.
"""
import csv
import io
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from serov_active_source_species_audit import ACTIVE, fetch_pinned
from serov_author_function_replay import source_functions, verified_original_code, COMMIT
from serov_geosite_original_risk import (
    FILE, build_unlabeled_frame, unique_sites, array_x, geo_min_km,
    read_selected_labels, mean_std_balance, summary, SIZES, digest
)

OUT=Path("mqr494-spatial-dependence-and-sharp-risk.json")
GRID=((.40,.75),(.40,.85),(.50,.75),(.50,.85))
ETA=(0.,.10,.25,.50,1.0)

def sharp_bound(prob):
    p=np.clip(np.asarray(prob,dtype=float).ravel(),1e-10,1-1e-10)
    a=-np.log1p(-p)
    b=-np.log(p)
    lo=float(np.mean(np.minimum(a,b)))
    hi=float(np.mean(np.maximum(a,b)))
    return a,b,{"lower":lo,"upper":hi,"width":hi-lo,
        "interpretation":"sharp convex-hull envelope over all finite binary label assignments, not entire attainable set"}

def prevalence_bound(a,b,k):
    d=np.sort(np.asarray(b)-np.asarray(a))
    n=len(d)
    if not isinstance(k,int) or not 0<=k<=n:raise ValueError("inadmissible k")
    base=float(np.sum(a))
    return {"lower":float((base+np.sum(d[:k]))/n),
            "upper":float((base+np.sum(d[n-k:]))/n),
            "known_positive_labels_used_posthoc":k}

def calibration_bands(prob,a,b):
    # Unverified assumption: the true conditional target positive probability
    # is within eta of the source model's prediction at each target site.
    d=b-a
    ans={}
    for eta in ETA:
        low=np.maximum(0.,prob-eta)
        high=np.minimum(1.,prob+eta)
        q_low=np.where(d>=0,low,high)
        q_high=np.where(d>=0,high,low)
        ans[str(eta)]={"expected_lower":float(np.mean(a+q_low*d)),
                       "expected_upper":float(np.mean(a+q_high*d))}
    return ans

def exact_small_checker():
    p=np.array([.03,.16,.32,.61,.83,.97])
    a,b,uncond=sharp_bound(p)
    all_risks=[]
    fixed=[]
    for bits in itertools.product((0,1),repeat=len(p)):
        bits=np.array(bits,dtype=int)
        loss=float(np.mean(np.where(bits,b,a)))
        all_risks.append(loss)
        if int(np.sum(bits))==3:fixed.append(loss)
    k_bound=prevalence_bound(a,b,3)
    if not(np.isclose(min(all_risks),uncond["lower"],atol=1e-13)
           and np.isclose(max(all_risks),uncond["upper"],atol=1e-13)
           and np.isclose(min(fixed),k_bound["lower"],atol=1e-13)
           and np.isclose(max(fixed),k_bound["upper"],atol=1e-13)):
        raise AssertionError("sharp extrema fail exhaustive independent small-label enumeration")
    return {"all_assignments_checked":64,"k3_assignments_checked":20,
        "sharp_unconditional_convex_hull_verified":True,
        "sharp_k_positive_envelope_verified":True}

def nearest_stats(fit,g):
    X=np.radians(np.array([[r["lat"],r["lon"]] for r in fit]))
    Y=np.radians(np.array([[r["lat"],r["lon"]] for r in g]))
    lat1=X[:,0,None];lat2=Y[None,:,0]
    hav=np.sin((lat1-lat2)/2)**2+np.cos(lat1)*np.cos(lat2)*np.sin((X[:,1,None]-Y[None,:,1])/2)**2
    dist=6371.0088*2*np.arcsin(np.sqrt(np.clip(hav,0,1)))
    nearest_km=np.min(dist,axis=0)
    return {"min_km":float(np.min(nearest_km)),
        "median_validation_to_train_nearest_km":float(np.median(nearest_km)),
        "validation_fraction_within_100m":float(np.mean(nearest_km<=.1)),
        "validation_fraction_within_1km":float(np.mean(nearest_km<=1.)),
        "validation_fraction_within_5km":float(np.mean(nearest_km<=5.))}

def contracts(frame):
    longitude=np.array([r["lon"] for r in frame])
    groups=[]
    for wq,eq in GRID:
        wcut=float(np.quantile(longitude,wq))
        ecut=float(np.quantile(longitude,eq))
        west=unique_sites([r for r in frame if r["lon"]<=wcut],"WEST")
        east=unique_sites([r for r in frame if r["lon"]>=ecut],"EAST")
        if len(west)<576 or len(east)<64:raise ValueError(f"source-locked geographic infeasibility q{wq}/{eq}")
        groups.append({"name":f"west_q{int(wq*100)}_east_q{int(eq*100)}",
           "fit":west[:512],"g":west[512:576],"p":east[:64],
           "w_cut":wcut,"e_cut":ecut,
           "west_unique_available":len(west),"east_unique_available":len(east),
           "g_style":"site_hash_unblocked"})
    west=unique_sites([r for r in frame if r["lon"]<=np.quantile(longitude,.50)],"WEST")
    east=unique_sites([r for r in frame if r["lon"]>=np.quantile(longitude,.75)],"EAST")
    west_lat=np.array([r["lat"] for r in west])
    f_cut=float(np.quantile(west_lat,.65))
    g_cut=float(np.quantile(west_lat,.80))
    fit_pool=[r for r in west if r["lat"]<=f_cut]
    g_pool=[r for r in west if r["lat"]>=g_cut]
    fit=sorted(fit_pool,key=lambda r:(digest("mqr494-blockFIT|"+r["site"]),r["site"]))[:512]
    g=sorted(g_pool,key=lambda r:(digest("mqr494-blockG|"+r["site"]),r["site"]))[:64]
    if len(fit)!=512 or len(g)!=64 or len(east)<64:raise ValueError("BLOCK_FEASIBILITY_HOLD")
    groups.append({"name":"west_q50_east_q75_latitude_blocked_G",
        "fit":fit,"g":g,"p":east[:64],
        "w_cut":float(np.quantile(longitude,.50)),
        "e_cut":float(np.quantile(longitude,.75)),
        "f_lat_cut":f_cut,"g_lat_cut":g_cut,
        "west_unique_available":len(west),"east_unique_available":len(east),
        "g_style":"distinct_geographic_northern_source_block"})
    for z in groups:
        sites=[r["site"] for r in z["fit"]+z["g"]+z["p"]]
        if len(set(sites))!=640:raise AssertionError("coordinate site duplicate across cohorts")
        if geo_min_km(z["fit"]+z["g"],z["p"])<=0:raise AssertionError("target/source geographic overlap")
    return groups

def main():
    sha,cap=ACTIVE["anemone"]
    raw=fetch_pinned(FILE,sha,cap)
    frame,drops=build_unlabeled_frame(raw)
    if len(frame)!=2905:raise AssertionError("4.93 pinned source-frame count mismatch")
    choices=contracts(frame)
    check=exact_small_checker()
    src_ids={r["row"] for z in choices for r in z["fit"]+z["g"]}
    src_labels=read_selected_labels(raw,src_ids)
    author=source_functions(verified_original_code())
    # Every source estimator and every target-prediction risk envelope is computed
    # before reading any of the selected target labels for this 4.94 run.
    provisional=[]
    for z in choices:
        fit,g,p=z["fit"],z["g"],z["p"]
        fy=np.array([src_labels[r["row"]] for r in fit])
        gy=np.array([src_labels[r["row"]] for r in g])
        if len(set(fy))!=2:raise AssertionError("SOURCE_CLASS_INFEASIBLE")
        scale=StandardScaler().fit(array_x(fit))
        xf=scale.transform(array_x(fit))
        xg=scale.transform(array_x(g))
        xp=scale.transform(array_x(p))
        clf=LogisticRegression(C=1.0,max_iter=2000,random_state=493).fit(xf,fy)
        def pred(x):
            return np.clip(clf.predict_proba(x)[:,1],1e-10,1-1e-10)
        ps=pred(xg); pt=pred(xp)
        gl=-gy*np.log(ps)-(1-gy)*np.log1p(-ps)
        def lsrc(x):
            if not np.array_equal(x,xg):raise AssertionError("source-loss closure broken")
            return np.log(gl)
        nw=float(np.exp(author["MCE"](lsrc,xg)))
        kmm=float(np.exp(author["KMM_error"](lsrc,xp,xg,10.0)))
        weight=np.asarray(author["kernel_mean_matching"](xp,xg,kern="rbf",B=10.0),dtype=float).ravel()
        if not math.isclose(nw,float(np.mean(gl)),rel_tol=1e-9,abs_tol=1e-10):raise AssertionError("original NW mismatch")
        if not math.isclose(kmm,float(np.dot(weight,gl)/64),rel_tol=1e-9,abs_tol=1e-10):raise AssertionError("original KMM mismatch")
        a,b,unconditional=sharp_bound(pt)
        bands=calibration_bands(pt,a,b)
        audit={"fit":summary(fit,src_labels),"g":summary(g,src_labels),
            "target_unlabeled_sites":len(p),
            "source_G_nearest_FIT":nearest_stats(fit,g),
            "source_to_target_min_km":geo_min_km(fit+g,p),
            "feature_mean_balance":mean_std_balance(xg,xp),
            "KMM_ESS":float(np.sum(weight)**2/np.dot(weight,weight)),
            "KMM_weight_sum":float(np.sum(weight)),
            "sharp_unlabeled_target_loss_convex_hull":unconditional,
            "calibration_assumption_expected_risk_sensitivity":bands,
            "source_estimated_NW":nw,"source_estimated_KMM":kmm}
        provisional.append({"contract":{k:v for k,v in z.items() if k not in ("fit","g","p")},
                            "target_selected_records":p,"target_prediction":pt,
                            "loss_if_zero":a,"loss_if_one":b,"audit":audit})
    base=next(x for x in provisional if x["contract"]["name"]=="west_q50_east_q75")
    if not(all(math.isclose(base["audit"][k],v,rel_tol=1e-9,abs_tol=1e-9) for k,v in
        (("source_estimated_NW",.4587061383023344),("source_estimated_KMM",.41023871824198993)))):
        raise AssertionError("original 4.93 baseline not reproduced under its same source site contract")
    # Post-estimation target-label reveal; fixed selection and risks never adapt.
    tgt_ids={r["row"] for z in choices for r in z["p"]}
    tgt_labels=read_selected_labels(raw,tgt_ids)
    final=[]
    for item in provisional:
        records=item.pop("target_selected_records")
        pt=item.pop("target_prediction")
        a=item.pop("loss_if_zero")
        b=item.pop("loss_if_one")
        y=np.array([tgt_labels[r["row"]] for r in records],dtype=int)
        oracle=float(np.mean(np.where(y==1,b,a)))
        k=int(np.sum(y))
        pbound=prevalence_bound(a,b,k)
        ul=item["audit"]["sharp_unlabeled_target_loss_convex_hull"]
        if not(ul["lower"]-1e-12<=oracle<=ul["upper"]+1e-12):raise AssertionError("oracle outside sharp unlabeled envelope")
        if not(pbound["lower"]-1e-12<=oracle<=pbound["upper"]+1e-12):raise AssertionError("oracle outside sharp prevalence envelope")
        nw=item["audit"]["source_estimated_NW"]
        kw=item["audit"]["source_estimated_KMM"]
        ng=abs(nw-oracle); kg=abs(kw-oracle)
        item["audit"].update({"target_posthoc":summary(records,tgt_labels),
            "posthoc_target_oracle":oracle,
            "NW_absolute_oracle_gap":ng,"KMM_absolute_oracle_gap":kg,
            "source_risk_estimator_closer":"NW" if ng<kg else ("KMM" if kg<ng else "TIE"),
            "sharp_prevalence_conditioned_posthoc_only":pbound})
        final.append(item)
    base=next(x for x in final if x["contract"]["name"]=="west_q50_east_q75")
    if not math.isclose(base["audit"]["posthoc_target_oracle"],.7495034100861271,rel_tol=1e-9,abs_tol=1e-9):
        raise AssertionError("original 4.93 target oracle changed")
    verdicts=Counter(x["audit"]["source_risk_estimator_closer"] for x in final)
    result={"status":"FROZEN_RETROSPECTIVE_SPATIAL_ROBUSTNESS_AND_SHARP_FINITE_TARGET_BOUNDS_PASS",
        "original_publication_root":"Serov 2026 Scientific Reports, one original paper",
        "upstream_commit":COMMIT,"original_data_git_blob_sha1":sha,
        "original_source_file":FILE,
        "precommit_file":"docs/MQR-4.94-OPENING-CONSTITUTION-AND-PRECOMMIT.md",
        "temporal_honesty":"Grid fixed before running 4.94 variants but 4.93 outcomes had already been revealed; not independent blinded confirmation",
        "source_eligible_frame_count":len(frame),"source_frame_drops":drops,
        "small_n_math_exhaustive_check":check,
        "contract_winner_counts":dict(verdicts),
        "contract_winner_invariant":len(verdicts)==1,
        "contracts":final,
        "nonadmissions":[
           "Changing geographical target region changes its estimand; rows are not independent publication roots",
           "Latitude blocking G is diagnostic and does not establish independence absent spatial autocorrelation estimation",
           "Source original logloss risk and posthoc target oracle cannot diagnose causal conditional label shift",
           "The convex-hull bound endpoints are sharp but attainable risk set is discrete",
           "Prevalence-bound k is target label information available only after oracle reveal",
           "Calibration eta bands are EXPECTED target risk under unverified assumptions, not realized loss prediction intervals",
           "No statistical significance, iid confidence interval, method novelty or KMM generalization"]
    }
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf8")
    for x in final:
        d=x["audit"]
        print("MQR494_RESULT="+json.dumps({"contract":x["contract"]["name"],
            "source_to_target_min_km":d["source_to_target_min_km"],
            "source_g_fit_nearest":d["source_G_nearest_FIT"],
            "nw":d["source_estimated_NW"],"kmm":d["source_estimated_KMM"],
            "oracle":d["posthoc_target_oracle"],"nw_gap":d["NW_absolute_oracle_gap"],
            "kmm_gap":d["KMM_absolute_oracle_gap"],"winner":d["source_risk_estimator_closer"],
            "ess":d["KMM_ESS"],
            "sharp_unlabeled":d["sharp_unlabeled_target_loss_convex_hull"],
            "sharp_posthoc_k":d["sharp_prevalence_conditioned_posthoc_only"],
            "target_positive_count":d["target_posthoc"]["positive_count"]},sort_keys=True))
    print("MQR494_EXACT_SMALL_CHECK="+json.dumps(check,sort_keys=True))
    print("MQR494_WINNER_COUNTS="+json.dumps(dict(verdicts),sort_keys=True))
    print("MQR494_SPATIAL_ID_BOUNDS=PASS")

if __name__=="__main__":main()
