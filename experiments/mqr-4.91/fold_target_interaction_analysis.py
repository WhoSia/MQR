#!/usr/bin/env python3
"""MQR 4.91: bounded within-species external AUC fold×target decomposition.

Only descriptive algebra over source-reconstructed matched-target AUC values.
Folds and targets are NOT independent studies or experimental replicate roots.
Never infer spatial-CV optimism, causality, or population-level precision.
"""
import argparse
import json
from collections import defaultdict
from itertools import combinations
from math import isclose
from pathlib import Path

def decompose(data):
    cases=data["cases"]
    if len(cases)!=10 or any(c["state"]!="PASS" for c in cases):
        raise ValueError("complete ten-case source-verified PASS required; refuse partial aggregation")
    by_species=defaultdict(list)
    for case in cases:
        vals=case["original_fold_target_auc"]
        if len(vals)!=4 or any(not 0<=v<=1 for v in vals):
            raise ValueError("four bounded original fitted-model external AUC values required")
        if not (0 <= case["reconstructed_final_target_auc"] <= 1):
            raise ValueError("invalid original final model AUC")
        by_species[case["species"]].append(case)
    if sorted(map(len,by_species.values())) != [3,3,4]:
        raise ValueError("expected original three-source-family target structure 3+4+3")
    results=[]
    for species,entries in sorted(by_species.items()):
        t=len(entries)
        y=[e["original_fold_target_auc"] for e in entries]
        mean=sum(map(sum,y))/(4*t)
        target_means=[sum(z)/4 for z in y]
        fold_means=[sum(y[i][j] for i in range(t))/t for j in range(4)]
        ss_total=sum((v-mean)**2 for row in y for v in row)
        ss_target=4*sum((m-mean)**2 for m in target_means)
        ss_fold=t*sum((m-mean)**2 for m in fold_means)
        ss_interaction=sum(
            (y[i][j]-target_means[i]-fold_means[j]+mean)**2
            for i in range(t) for j in range(4))
        if not isclose(ss_total,ss_target+ss_fold+ss_interaction,
                       abs_tol=1e-12,rel_tol=1e-9):
            raise ValueError("two-way sum of squares identity failed")
        reversal_pairs=[]
        for j,k in combinations(range(4),2):
            signs=[1 if row[j]>row[k]+1e-12 else (-1 if row[j]<row[k]-1e-12 else 0) for row in y]
            if 1 in signs and -1 in signs:
                reversal_pairs.append([j,k])
        targets=[]
        for e in entries:
            z=e["original_fold_target_auc"]
            sens=e.get("boundary_blind_sensitivity")
            if not sens:raise ValueError("missing boundary-blind evaluation")
            if len(sens["interior_auc"])!=5:raise ValueError("missing matched interior scores")
            targets.append({
                "target":e["target"],"positives":e["positives"],
                "reference_negative_cells":e["negative_reference_cells"],
                "original_final_auc":e["reconstructed_final_target_auc"],
                "fold_auc":z,
                "fold_range":max(z)-min(z),
                "fold_mean":sum(z)/4,
                "fold_minus_separately_fitted_final": [
                    f-e["reconstructed_final_target_auc"] for f in z],
                "n_boundary_positive":sens["boundary_positive"],
                "n_boundary_negative":sens["boundary_negative"],
                "maximum_abs_boundary_exclusion_fold_delta":
                    max(abs(x) for x in sens["delta"][1:]),
                "source_score_ambiguity_resolution_count":
                    len(e["source_boundary_cell_resolutions"])})
        results.append({
            "species":species,"target_count":t,
            "grand_fold_auc_mean":mean,
            "fold_source_identity_means":fold_means,
            "sum_of_squares":{"total":ss_total,
                "target_main_effect":ss_target,
                "fitted_fold_model_main_effect":ss_fold,
                "descriptive_target_by_fold_interaction":ss_interaction},
            "sum_squares_identity_test":"PASS",
            "target_fold_rank_reversal_model_pairs":reversal_pairs,
            "rank_reversal_model_pair_count":len(reversal_pairs),
            "targets":targets})
    return {"status":"SOURCE_COMPLETE_ALGEBRA_ONLY",
        "original_publisher_study_roots":1,"biological_species":3,
        "source_target_cases":10,"original_source_fitted_fold_models_per_species":4,
        "scope":"descriptive original-target matched AUC for 3 within-paper calibration families",
        "forbidden_inferences":[
            "no between-study meta-analysis",
            "no signed spatial CV optimism",
            "no independent-fold p-values or cellwise iid uncertainty",
            "no causal attribution of AUC interaction to fitted model or target covariate shift"],
        "species_results":results}

def self_test():
    demo=[]
    for sp,count in (("A",3),("B",4),("C",3)):
        for ix in range(count):
            vals=[0.3+0.04*j+0.03*ix+(0.01 if j%2 else -0.01)*ix
                  for j in range(4)]
            demo.append({"state":"PASS","species":sp,"target":str(ix),
                "original_fold_target_auc":vals,
                "reconstructed_final_target_auc":0.5,
                "positives":10,"negative_reference_cells":20,
                "source_boundary_cell_resolutions":[],
                "boundary_blind_sensitivity":{"interior_auc":[0.5]+vals,
                    "delta":[0]*5,"boundary_positive":0,"boundary_negative":0}})
    x=decompose({"cases":demo})
    assert len(x["species_results"])==3
    for result in x["species_results"]:
        assert result["sum_squares_identity_test"]=="PASS"
    try:
        decompose({"cases":demo[:-1]})
        raise AssertionError("truncated original target allowed")
    except ValueError:
        pass
    print("MQR491_TARGET_FOLD_ALGEBRA_SYNTHETIC_TEST=PASS")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",type=Path)
    p.add_argument("--output",type=Path,default=Path("p491-ten-target-factorization.json"))
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    if args.self_test:self_test()
    if args.input:
        source=json.loads(args.input.read_text(encoding="utf8"))
        result=decompose(source)
        args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf8")
        for row in result["species_results"]:
            print("MQR491_TARGET_FOLD_INTERACTION="+json.dumps({
                "species":row["species"],"n_targets":row["target_count"],
                "ss":row["sum_of_squares"],
                "rank_reversed_fold_pairs":row["rank_reversal_model_pair_count"],
                "target_ranges":[{"target":v["target"],"fold_range":v["fold_range"],
                                  "max_edge_sensitivity":v["maximum_abs_boundary_exclusion_fold_delta"]}
                                 for v in row["targets"]]}))
        print("MQR491_TEN_TARGET_FACTOR_ANALYSIS=PASS")
    elif not args.self_test: p.error("input evidence or self-test required")
if __name__=="__main__":main()
