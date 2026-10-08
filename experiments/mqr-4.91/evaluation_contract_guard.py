#!/usr/bin/env python3
"""MQR 4.91 evaluation-comparability type guard.

An executable *restricted* evidence precheck, not a general causal
transportability theorem or a universal optimal repair algorithm.
Original study source domains and spatial CV estimands remain distinct.
"""
import argparse
import json
from dataclasses import dataclass,asdict
from pathlib import Path

@dataclass(frozen=True)
class AUCIdentity:
    species: str
    target: str
    positive_reference: str
    negative_reference: str
    inclusion_mask: str
    source_study_root: str
    model_artifact: str
    metric: str = "tie_aware_target_auc"
    setting: str = "fixed_external_target"
    selection_policy: str = "source_nonmissing_same_common_fold_mask"

def compare_claims(a,b):
    core_fields=("species","target","positive_reference","negative_reference",
                 "inclusion_mask","metric","selection_policy","setting")
    disagreements=[k for k in core_fields if getattr(a,k)!=getattr(b,k)]
    if a.source_study_root!=b.source_study_root:
        disagreements.append("source_study_root_requires_external_provenance")
    if disagreements:
        return {"status":"REJECT_COMMON_ESTIMAND",
                "required_repair_obligations":disagreements,
                "is_minimum_cost_repair_proven":False}
    if a.model_artifact==b.model_artifact:
        kind="REPEATED_MEASUREMENT_SAME_MODEL"
    else:
        kind="SAME_TARGET_DIFFERENT_FITTED_MODELS"
    return {"status":"ADMIT_TYPED_COMPARISON","kind":kind,
            "evidence_limitation":"comparability does not imply independence, transport or unbiased source CV"}

def source_claims_for_case(case):
    if case.get("state")!="PASS":raise ValueError("case must pass original source replay")
    s=case["species"]; cal=case["calibration"];t=case["target"]
    stem=f"{s}_{cal}-{t}"
    base="3_Maxent_predictions/2_Maxent_values/"
    pos=base+f"1_Maxent_values_for_presence_cells/{stem}.csv"
    neg=base+f"2_Maxent_values_for_absence_cells/{stem}_2.csv"
    mask=f"common_fold_and_final_scored_cells:{stem}"
    root="Matsui2026:Zenodo19970795"
    fmt=lambda model:AUCIdentity(s,t,pos,neg,mask,root,model)
    cvroot=f"3_Maxent_predictions/1_Maxent_output/4-fold_cross-validation/{s}_{cal}/"
    folds=[fmt(cvroot+s+f"_{k}.lambdas") for k in range(4)]
    return folds,fmt(case["source_final_lambda_path"] if "source_final_lambda_path" in case
                      else f"3_Maxent_predictions/1_Maxent_output/56_predictions/{stem}/{s}.lambdas")

def audit_source_matrix(data):
    cases=data.get("cases",[])
    if len(cases)!=10 or any(c.get("state")!="PASS" for c in cases):
        raise ValueError("ten complete source-replayed target cases required")
    source_roots=set()
    certificates=[]
    for c in cases:
        folds,final=source_claims_for_case(c)
        root=final.source_study_root;source_roots.add(root)
        decisions=[compare_claims(f,final) for f in folds]
        if any(d.get("kind")!="SAME_TARGET_DIFFERENT_FITTED_MODELS" for d in decisions):
            raise ValueError("source-matched model evaluation contract not certified")
        source_cv=AUCIdentity(
            c["species"],"NativeCalibration:"+c["calibration"],
            "native_held_out_CV_occurrences",
            "source_region_Maxent_background",
            "native_fold_specific_validation_mask",
            root,folds[0].model_artifact,setting="original_native_region_cv")
        mismatch=compare_claims(source_cv,folds[0])
        if mismatch["status"]!="REJECT_COMMON_ESTIMAND":
            raise AssertionError("native CV AUC promoted to external target estimand")
        certificates.append({
            "case":c["species"]+"_"+c["calibration"]+"-"+c["target"],
            "source_root":root,"comparison_count":len(decisions),
            "admission":"SAME_TARGET_DIFFERENT_FITTED_MODELS",
            "source_native_cv_comparison":"REJECT_COMMON_ESTIMAND",
            "source_native_cv_missing_contracts":mismatch["required_repair_obligations"],
            "no_claim_of_global_minimal_repair":True})
    if len(source_roots)!=1:
        raise AssertionError("source roots not preserved")
    return {"status":"TEN_TARGET_TYPED_AUDIT_PASS",
            "published_study_roots":len(source_roots),
            "original_target_cases":len(certificates),
            "certified_model_contrasts":sum(c["comparison_count"] for c in certificates),
            "method_novelty":"UNDETERMINED",
            "spatial_cv_optimism":"NOT_MEASURED_BY_THIS_CONTRAST",
            "cases":certificates}

def self_test():
    a=AUCIdentity("s","r","p","q","mask","root","f0")
    b=AUCIdentity("s","r","p","q","mask","root","final")
    assert compare_claims(a,b)["kind"]=="SAME_TARGET_DIFFERENT_FITTED_MODELS"
    assert compare_claims(a,a)["kind"]=="REPEATED_MEASUREMENT_SAME_MODEL"
    alt=AUCIdentity("s","r","p","other_reference","mask","root","final")
    assert "negative_reference" in compare_claims(a,alt)["required_repair_obligations"]
    alt=AUCIdentity("s","other_target","p","q","mask","root","f0")
    assert compare_claims(a,alt)["status"]=="REJECT_COMMON_ESTIMAND"
    print("MQR491_CONTRACT_SYNTHETIC_REJECTION_TEST=PASS")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--input",type=Path)
    p.add_argument("--output",type=Path,default=Path("mqr491-comparability.json"))
    args=p.parse_args()
    if args.self_test:self_test()
    if args.input:
        result=audit_source_matrix(json.loads(args.input.read_text(encoding="utf8")))
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf8")
        print("MQR491_TYPED_SOURCE_CONTRACTS="+str(result["certified_model_contrasts"]))
        print("MQR491_TYPED_SOURCE_GUARD=PASS")
    elif not args.self_test:p.error("need input or self-test")
if __name__=="__main__":main()
