#!/usr/bin/env python3
"""MQR 4.91 — rank-based spatial stability of ORIGINAL fitted fold maps.

This is a descriptive rival check prompted by Grimmett, Whitsed & Horta 2020.
Spearman correlations on common valid external raster cells are NOT their
binary Fleiss' kappa; neither alone measures label-dependent external AUC.
Pixel correlations do NOT license iid inference.
"""
from itertools import combinations
from math import sqrt, isfinite

def average_rank(values):
    order=sorted(range(len(values)),key=lambda k:values[k])
    ans=[0.0]*len(values)
    k=0
    while k<len(order):
        e=k+1
        while e<len(order) and values[order[e]]==values[order[k]]:
            e+=1
        r=(k+1+e)/2.0
        for v in order[k:e]:ans[v]=r
        k=e
    return ans

def correlation(x,y):
    if len(x)!=len(y) or len(x)<3:raise ValueError("insufficient common raster pixels")
    mx=sum(x)/len(x);my=sum(y)/len(y)
    cov=sum((a-mx)*(b-my) for a,b in zip(x,y))
    ssx=sum((a-mx)**2 for a in x);ssy=sum((b-my)**2 for b in y)
    if ssx<=0 or ssy<=0:raise ValueError("constant map or zero spatial rank variance")
    return cov/sqrt(ssx*ssy)

def pairwise_spatial_stability(fold_grids,final_grid):
    if len(fold_grids)!=4:raise ValueError("four original fitted-fold maps required")
    main_h,main_v=final_grid
    shape_keys=("ncols","nrows","xllcorner","yllcorner","cellsize")
    rows=[]
    for h, v in fold_grids:
        if any(h[k]!=main_h[k] for k in shape_keys):
            raise ValueError("raster identity / geometry mismatch")
        if len(v)!=len(main_v):
            raise ValueError("array length mismatch")
        rows.append(v)
    mask=[i for i in range(len(main_v)) if main_v[i]!=main_h["nodata_value"]
          and all(grids[i]!=h["nodata_value"] for (h,grids) in fold_grids)]
    if len(mask)<200:raise ValueError("too few original common scored cells")
    ranks=[average_rank([v[i] for i in mask]) for v in rows]
    out=[]
    for a,b in combinations(range(4),2):
        sr=correlation(ranks[a],ranks[b])
        plain=correlation([rows[a][i] for i in mask],[rows[b][i] for i in mask])
        mae=sum(abs(rows[a][i]-rows[b][i]) for i in mask)/len(mask)
        if any(not isfinite(v) for v in (sr,plain,mae)):
            raise ValueError("nonfinite diagnostic")
        out.append({"original_fold_pair":[a,b],"spearman_map_rank":sr,
                    "pearson_raw_scores":plain,"mean_absolute_score_gap":mae})
    return {"source_common_scored_pixels":len(mask),
            "n_original_fold_pairs":6,
            "spatial_rank_mean":sum(p["spearman_map_rank"] for p in out)/6,
            "spatial_rank_min":min(p["spearman_map_rank"] for p in out),
            "spatial_rank_max":max(p["spearman_map_rank"] for p in out),
            "pairwise":out,
            "comparison_to_prior_art":"Grimmett et al. 2020 measures thresholded map agreement with Fleiss kappa; these diagnostics use continuous source score map ranks, not the same metric",
            "target_scope":"original full target raster intersection of four fold and final masks",
            "inference":"descriptive, spatial pixels correlated, no iid precision"}

def self_test():
    h={"ncols":4.0,"nrows":2.0,"xllcorner":0.0,"yllcorner":0.0,
       "cellsize":1.0,"nodata_value":-9999.0}
    v=[0.1,0.3,0.3,0.4,0.5,0.7,0.8,0.9]
    assert average_rank([3,1,1,5])==[3,1.5,1.5,4]
    # Test rank-invariant nonlinear transform and one tie.
    assert abs(correlation(average_rank(v),average_rank([n**3 for n in v]))-1)<1e-12
    try:
        pairwise_spatial_stability([(h,v)]*4,(h,v))
        raise AssertionError("accepted 8 cells as sufficient")
    except ValueError:pass
    try:
        correlation([1,1,1],[3,2,1])
        raise AssertionError("accepted constant map")
    except ValueError:pass
    print("MQR491_SPATIAL_MAP_RANK_TEST=PASS")

if __name__=="__main__":self_test()
