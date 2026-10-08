#!/usr/bin/env python3
"""MQR 4.93: hash-frozen, site-disjoint WEST/EAST original-data risk pilot.

Run ONLY after coordinate Gate0. The source-only original MCE/KMM functions
are unmodified. Target presence labels are read in a SECOND pass only after
site selection, fitted predictor and source-only risk estimates are frozen.
Precommit: docs/MQR-4.93-PREOUTCOME-GEOSITE-RISK-PRESEAL.md.
"""
import csv
import hashlib
import io
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from serov_active_source_species_audit import fetch_pinned, ACTIVE
from serov_author_function_replay import verified_original_code, source_functions, COMMIT

FILE="datasets/species/anemone.csv"
OUT=Path("mqr493-geographic-original-risk.json")
LAT_RANGE=(59.0,71.5)
LON_RANGE=(19.0,32.5)
LOW_CUT=24.720692
HIGH_CUT=25.278482
SALT="mqr493-geosite-v1"
SIZES={"FIT":512,"G":64,"P":64}
FEATURES=tuple(f"bio{i}" for i in range(1,20))

def digest(key):
    return hashlib.sha256(key.encode("utf-8")).hexdigest()

def site_key(lat,lon):
    return f"{lat:.6f}|{lon:.6f}"

def build_unlabeled_frame(raw):
    result=[]
    drop=Counter()
    rows=csv.DictReader(io.StringIO(raw.decode("utf-8-sig"),newline=""))
    for row_number,row in enumerate(rows,2):
        drop["total_raw"]+=1
        try:
            year=int(float(row["year"]))
            lat=float(row["lat"])
            lon=float(row["long"])
        except (KeyError,TypeError,ValueError):
            drop["unparseable_year_or_coordinates"]+=1
            continue
        if not(2013<=year<=2024):
            drop["other_year"]+=1;continue
        if not (math.isfinite(lat) and math.isfinite(lon) and LAT_RANGE[0]<=lat<=LAT_RANGE[1] and LON_RANGE[0]<=lon<=LON_RANGE[1]):
            drop["coordinate_outside_verified_Finland"]+=1;continue
        try:
            x=np.array([float(row[name]) for name in FEATURES],dtype=float)
            if not np.all(np.isfinite(x)):raise ValueError("nonfinite features")
        except (KeyError,TypeError,ValueError):
            drop["missing_bio"]+=1;continue
        result.append({"row":row_number,"year":year,"lat":lat,"lon":lon,
                       "site":site_key(lat,lon),"x":x})
    drop["eligible_nonlabel_frame"]=len(result)
    return result,drop

def unique_sites(rows,role):
    by_site={}
    for row in rows:
        s=row["site"]
        candidate=digest(f"{SALT}|row|{row['row']}|{s}")
        if s not in by_site or candidate<by_site[s][0]:
            by_site[s]=(candidate,row)
    ordered=sorted((r for h,r in by_site.values()),key=lambda r:(digest(f"{SALT}|{role}|{r['site']}"),r["site"]))
    return ordered

def read_selected_labels(raw,row_numbers):
    found={}
    for rownum,row in enumerate(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"),newline="")),2):
        if rownum not in row_numbers:continue
        label=(row.get("presence") or "").strip()
        if label not in ("0","1"):
            raise ValueError(f"selected label invalid at frozen row {rownum}")
        found[rownum]=int(label)
    if set(found)!=set(row_numbers):
        raise AssertionError("selected pinned source rows missing from original")
    return found

def array_x(group):
    return np.stack([r["x"] for r in group])

def geo_min_km(a,b):
    a1=np.radians(np.array([[r["lat"],r["lon"]] for r in a],dtype=float))
    b1=np.radians(np.array([[r["lat"],r["lon"]] for r in b],dtype=float))
    lat1=a1[:,0,None];lat2=b1[None,:,0]
    dlat=lat1-lat2
    dlon=a1[:,1,None]-b1[None,:,1]
    hav=np.sin(dlat/2)**2+np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    distance=6371.0088*2*np.arcsin(np.sqrt(np.clip(hav,0,1)))
    return float(np.min(distance))

def mean_std_balance(g,p):
    denom=np.std(g,axis=0,ddof=1)
    score=np.abs((np.mean(g,axis=0)-np.mean(p,axis=0))/np.where(denom>1e-12,denom,1.0))
    return {"mean_abs_standardized_BIO_mean_gap":float(np.mean(score)),
            "max_abs_standardized_BIO_mean_gap":float(np.max(score)),
            "tiny_standard_deviation_BIO_features":int(np.sum(denom<=1e-12))}

def summary(records,labels=None):
    result={"n":len(records),"n_unique_sites":len(set(z["site"] for z in records)),
            "year_histogram":dict(sorted(Counter(str(z["year"]) for z in records).items())),
            "physical_lat_extent":[min(z["lat"] for z in records),max(z["lat"] for z in records)],
            "physical_lon_extent":[min(z["lon"] for z in records),max(z["lon"] for z in records)]}
    if labels is not None:
        result["positive_count"]=int(sum(labels[z["row"]] for z in records))
        result["negative_count"]=len(records)-result["positive_count"]
    return result

def main():
    sha,limit=ACTIVE["anemone"]
    raw=fetch_pinned(FILE,sha,limit)
    frame,drops=build_unlabeled_frame(raw)
    if len(frame)!=2905:raise AssertionError("coordinate-gate non-label frame changed")
    lons=np.array([z["lon"] for z in frame])
    if not(np.isclose(np.quantile(lons,.5),LOW_CUT,atol=1e-10) and np.isclose(np.quantile(lons,.75),HIGH_CUT,atol=1e-10)):
        raise AssertionError("pinned pre-gate source longitude cut changed")
    west=unique_sites([z for z in frame if z["lon"]<=LOW_CUT],"WEST")
    east=unique_sites([z for z in frame if z["lon"]>=HIGH_CUT],"EAST")
    if len(west)<SIZES["FIT"]+SIZES["G"] or len(east)<SIZES["P"]:
        raise AssertionError(f"SPATIAL_HOLDOUT_INFEASIBLE unique WEST={len(west)}, EAST={len(east)}")
    fit=west[:SIZES["FIT"]]
    g=west[SIZES["FIT"]:SIZES["FIT"]+SIZES["G"]]
    p=east[:SIZES["P"]]
    if len(set(z["site"] for z in fit+g+p)) != sum(SIZES.values()):
        raise AssertionError("source/target duplicates or sample site overlap")
    min_km=geo_min_km(fit+g,p)
    if min_km<=0:raise AssertionError("not geographically separated")
    # Source-only label extraction; target labels are NOT read.
    source_labels=read_selected_labels(raw,{z["row"] for z in fit+g})
    fit_y=np.array([source_labels[z["row"]] for z in fit],dtype=int)
    g_y=np.array([source_labels[z["row"]] for z in g],dtype=int)
    if len(np.unique(fit_y))!=2:
        raise AssertionError("SPATIAL_HOLDOUT_INFEASIBLE frozen source fitted cohort lacks two labels")
    scaler=StandardScaler().fit(array_x(fit))
    xf=scaler.transform(array_x(fit))
    xg=scaler.transform(array_x(g))
    xp=scaler.transform(array_x(p))
    model=LogisticRegression(C=1.0,max_iter=2000,random_state=493)
    model.fit(xf,fit_y)
    def loss(x,y):
        prob=np.clip(model.predict_proba(x)[:,1],1e-10,1-1e-10)
        return -y*np.log(prob)-(1-y)*np.log(1-prob)
    lg=loss(xg,g_y)
    if not np.all(np.isfinite(lg)):raise AssertionError("nonfinite source errors")
    author=source_functions(verified_original_code())
    def source_logloss_closure(x):
        if not np.array_equal(x,xg):raise AssertionError("source-only closure violated")
        return np.log(lg)
    nw=float(np.exp(author["MCE"](source_logloss_closure,xg)))
    kmm=float(np.exp(author["KMM_error"](source_logloss_closure,xp,xg,10.0)))
    weights=np.asarray(author["kernel_mean_matching"](xp,xg,kern="rbf",B=10.0),dtype=float).ravel()
    if not math.isclose(nw,float(np.mean(lg)),rel_tol=1e-9,abs_tol=1e-10):
        raise AssertionError("upstream MCE source mismatch")
    if not math.isclose(kmm,float(np.dot(weights,lg)/len(lg)),rel_tol=1e-9,abs_tol=1e-10):
        raise AssertionError("upstream KMM source mismatch")
    ess=float(np.sum(weights)**2/np.dot(weights,weights))
    if not 0<ess<=64.000001:raise AssertionError("invalid weight ESS")
    # The only post-outcome step: read the 64 frozen target labels.
    target_labels=read_selected_labels(raw,{z["row"] for z in p})
    yp=np.array([target_labels[z["row"]] for z in p],dtype=int)
    oracle=float(np.mean(loss(xp,yp)))
    result={
      "state":"REAL_PINNED_GEOGRAPHIC_HOLDOUT_EXECUTED",
      "research_scope":"New MQR authored, site-disjoint Finnish WEST/EAST geographic holdout on one Serov publisher source; NOT author paper-table replay",
      "source_repo":"egorser0v/Importance-reweighting","source_commit":COMMIT,
      "original_species_csv":FILE,"original_species_blob_sha1":sha,
      "source_time_window":[2013,2024],
      "source_longitude_median":LOW_CUT,"target_longitude_q75":HIGH_CUT,
      "source_buffer_longitude_degrees":HIGH_CUT-LOW_CUT,
      "source_frame_counts":drops,
      "eligible_unique_sites_all":len(set(z["site"] for z in frame)),
      "west_source_unique_sites_available":len(west),
      "east_target_unique_sites_available":len(east),
      "site_duplication_policy":"One row per original source geographic site, deterministic row SHA; no identical site across FIT, G, P",
      "source_and_target_selection":"SHA256 ranked distinct sites, no labels involved in site ranking or frame partition",
      "fit":summary(fit,source_labels),
      "source_validation":summary(g,source_labels),
      "target_posthoc":summary(p,target_labels),
      "minimum_source_to_target_site_haversine_km":min_km,
      "source_fit_to_source_validation_min_haversine_km":geo_min_km(fit,g),
      "risk":{
        "NW_author_original_source_estimate":nw,
        "KMM_author_original_source_estimate":kmm,
        "target_oracle_logloss_posthoc":oracle,
        "NW_absolute_oracle_gap":abs(nw-oracle),
        "KMM_absolute_oracle_gap":abs(kmm-oracle)
      },
      "KMM_weights":{
        "effective_sample_size":ess,
        "min":float(np.min(weights)),
        "max":float(np.max(weights)),
        "sum":float(np.sum(weights)),
        "top5_fraction":float(np.sum(np.sort(weights)[-5:])/np.sum(weights))
      },
      "feature_gap_unweighted":mean_std_balance(xg,xp),
      "claim_guard":{
        "target_label_available_for_model_selection":False,
        "target_label_available_for_importance_weights":False,
        "target_label_used_for_posthoc_oracle_only":True,
        "source_and_target_site_disjoint":True,
        "same_publisher_paper_root":True,
        "original_author_spatial_split_replication":False,
        "spatial_independence_proved":False,
        "covariate_shift_conditional_invariance_proved":False,
        "source_target_spatial_buffer_indicates_independence":False
      },
      "limits":[
        "One finite original-data geographical partition and one source publication root",
        "Site deduplication eliminates exact same-point reuse, not nearby spatial dependence or year/selection bias",
        "Coordinate validity supported by Finnish geographic plausibility not independent GBIF record-level geocoding",
        "Original Serov paper ecological source-target split is primarily temporal, not our direct west/east geographic split",
        "Training/model selected on WEST source, target labels withheld until oracle, not population-level inference",
        "Single geographic target cannot identify whether covariate/conditional shift or sampling mechanism caused disagreement",
        "Reported gaps are descriptive one-split errors; no iid/spatial CI, algorithm dominance or method novelty promoted"
      ]
    }
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
    print("MQR493_GEOSITE_COUNTS="+json.dumps({k:result[k] for k in ["eligible_unique_sites_all","west_source_unique_sites_available","east_target_unique_sites_available","minimum_source_to_target_site_haversine_km","source_fit_to_source_validation_min_haversine_km"]},sort_keys=True))
    print("MQR493_GEOSITE_CLASSES="+json.dumps({k:result[k] for k in ["fit","source_validation","target_posthoc"]},sort_keys=True))
    print("MQR493_GEOSITE_RISK="+json.dumps(result["risk"],sort_keys=True))
    print("MQR493_GEOSITE_KMM="+json.dumps(result["KMM_weights"],sort_keys=True))
    print("MQR493_GEOSITE_RISK=PASS")

if __name__=="__main__":main()
