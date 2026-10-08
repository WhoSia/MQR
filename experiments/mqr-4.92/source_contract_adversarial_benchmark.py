#!/usr/bin/env python3
"""MQR 4.92: source-attested claim-contract regressions against two weak baselines.

All adversarial mutations are transparently CONSTRUCTED, not real published
independent study cases. This suite tests false admissions/false rejections
under stipulated contracts, not new scientific-method effectiveness.
"""
from dataclasses import dataclass, replace
import json
from pathlib import Path

@dataclass(frozen=True)
class EvidenceClaim:
    source_root: str
    source_commit: str
    dataset_token: str
    target_population: str
    metric_family: str
    target_metric: str
    source_reference: str
    target_reference: str
    model_fitted_root: str
    selection_policy: str
    inclusion_mask: str
    score_transform: str
    artifact_role: str
    target_labels_used_for_fit: bool = False
    comparison_role: str = "estimator"

SEROV = EvidenceClaim(
    source_root="Serov2026-SciRep",source_commit="46c4d011c9f0cd0614c08e7edb68ac2491f659c8",
    dataset_token="oxalis",target_population="serov:target-species-shift",
    metric_family="risk",target_metric="E_target[absolute_error]",
    source_reference="serov:g_test:source_observed_loss",
    target_reference="serov:p_test:target_covariates",
    model_fitted_root="serov:source_g_train_model",
    selection_policy="serov:source-vs-target-split-fixed",
    inclusion_mask="serov:common_spatial_partition",
    score_transform="log-lost-risk-exp",artifact_role="risk_estimator",comparison_role="estimator")

MATSUI = EvidenceClaim(
    source_root="Matsui2026-EcolEvol",source_commit="matsui:zenodo19970795:author-final-pinned",
    dataset_token="oxalis",target_population="matsui:oxalis:oceania",
    metric_family="auc",target_metric="AUC_tie_aware_Pplus_Qunrecorded",
    source_reference="matsui:Oceania:positive_coords_csv",
    target_reference="matsui:Oceania:negative_ref_coords_csv",
    model_fitted_root="matsui:America:CV-source-train",
    selection_policy="matsui:source-nonmissing-geographic-labels",
    inclusion_mask="matsui:fourfold-external-common-grid",
    score_transform="maxent-logistic-original",
    artifact_role="geographic_target_prediction",comparison_role="estimator")

def basic_file_baseline(a,b):
    # Deliberately weak *filename + metric family* precheck.
    return a.dataset_token==b.dataset_token and a.metric_family==b.metric_family

def metadata_baseline(a,b):
    # Competing baseline that already checks publication and target region;
    # cannot certify masks, references, selection, fitted artifacts or oracles.
    return (a.source_root==b.source_root and
            a.target_population==b.target_population and
            a.metric_family==b.metric_family)

def typed_decision(a,b):
    if a.artifact_role != b.artifact_role:
        return False, "artifact_role"
    if a.target_labels_used_for_fit or b.target_labels_used_for_fit:
        return False, "heldout_target_label_leakage"
    keys=("source_root","source_commit","target_population","metric_family",
          "target_metric","source_reference","target_reference","model_fitted_root",
          "selection_policy","inclusion_mask","score_transform")
    for field in keys:
        if getattr(a,field)!=getattr(b,field):
            return False,field
    if a.comparison_role not in ("estimator","validation_oracle") or b.comparison_role not in ("estimator","validation_oracle"):
        return False,"unknown_comparison_role"
    return True, ("validation_oracle_not_deployable" if
                  "validation_oracle" in (a.comparison_role,b.comparison_role)
                  else "source_root_matched_estimators")

def suite():
    S=SEROV;M=MATSUI
    return [
      ("serov_NW_vs_KMM_source_target_risk",S,replace(S),True),
      ("serov_KMM_vs_target_loss_oracle",S,replace(S,comparison_role="validation_oracle"),True),
      ("matsui_fold0_vs_final_same_target",M,replace(M),True),
      ("serov_github_alias_redirect_same_immutable_sha",S,replace(S),True),
      ("serov_wrong_target_population",S,replace(S,target_population="serov:different-target-region"),False),
      ("serov_wrong_metric_L1_vs_squared_loss",S,replace(S,target_metric="E_target[squared_error]"),False),
      ("serov_target_label_used_to_train",S,replace(S,target_labels_used_for_fit=True),False),
      ("serov_different_source_fitted_model",S,replace(S,model_fitted_root="other-fitted-model"),False),
      ("serov_shift_selection_screen",S,replace(S,selection_policy="AUC_ROC_greater_0_7_selected_pairs"),False),
      ("serov_spatial_mask_changed",S,replace(S,inclusion_mask="serov:clipped-spatial-mask"),False),
      ("serov_source_repo_commit_changed",S,replace(S,source_commit="unverified-new-head"),False),
      ("serov_model_score_log_raw_transform",S,replace(S,score_transform="raw-squared-loss"),False),
      ("matsui_native_vs_target_map",M,replace(M,artifact_role="calibration_native_prediction"),False),
      ("matsui_other_target_positive_reference",M,replace(M,source_reference="matsui:Africa:positive_coords_csv"),False),
      ("matsui_negative_reference_replaced",M,replace(M,target_reference="matsui:Europe:negative_ref_coords_csv"),False),
      ("matsui_other_fold_mask",M,replace(M,inclusion_mask="matsui:fold-specific-scored-only"),False),
      ("matsui_native_cv_mistaken_deployment",M,replace(M,target_population="matsui:America:native-CV"),False),
      ("matsui_4fold_source_versus_unrelated_model",M,replace(M,model_fitted_root="unrelated-training-root"),False),
      ("cross_root_same_token_oxalis_different_paper_metric",M,S,False),
      ("cross_root_fake_same_metric",S,replace(S,source_root="Matsui2026-EcolEvol"),False),
    ]

def classification_stats(predicted,expected):
    return {"TP":sum(a and b for a,b in zip(predicted,expected)),
      "TN":sum(not a and not b for a,b in zip(predicted,expected)),
      "FP":sum(a and not b for a,b in zip(predicted,expected)),
      "FN":sum(not a and b for a,b in zip(predicted,expected))}

def main():
    examples=suite()
    labels=[x[3] for x in examples]
    decisions=[typed_decision(a,b) for _,a,b,_ in examples]
    typed=[d[0] for d in decisions]
    filename=[basic_file_baseline(a,b) for _,a,b,_ in examples]
    metadata=[metadata_baseline(a,b) for _,a,b,_ in examples]
    if any(x!=y for x,y in zip(typed,labels)):
        raise AssertionError("typed guard admitted/rejected a constructed claim contrary to explicit expected contract")
    stats={"weak_filename_metric":classification_stats(filename,labels),
           "publication_target_metadata":classification_stats(metadata,labels),
           "source_typed_contract":classification_stats(typed,labels)}
    if stats["source_typed_contract"]["FP"] or stats["source_typed_contract"]["FN"]:
        raise AssertionError("typed fixture false decision")
    report={"state":"ADVERSARIAL_CONTRACT_REGRESSION_ONLY",
      "independent_paper_roots":["Matsui2026-EcolEvol","Serov2026-SciRep"],
      "benchmark_type":"SOURCE-GROUNDED SCHEMA WITH CONSTRUCTED MUTATIONS",
      "n_cases":len(examples),"n_valid":sum(labels),"n_invalid":len(examples)-sum(labels),
      "methods":stats,
      "adversarial_cases":[{"case":name,"expected_valid":want,
           "filename_baseline":filename[i],
           "metadata_baseline":metadata[i],
           "typed_admitted":decisions[i][0],"typed_reason":decisions[i][1]}
           for i,(name,_,_,want) in enumerate(examples)],
      "limits":[
         "These are manually designed source-type perturbations, not natural error frequency",
         "Correctness labels are stipulated by the declared contract, not independently judged",
         "The two weak comparators are NOT published scientific baseline systems",
         "Zero false admission on this tiny suite cannot establish real-world superiority",
         "Cross-study metric incompatibility is demonstrated only as a typed negative control"]}
    Path("mqr492-source-contract-benchmark.json").write_text(
        json.dumps(report,indent=2),encoding="utf8")
    print("MQR492_SOURCE_CONTRACT_FIXTURE_MATRIX="+json.dumps(stats,sort_keys=True))
    print("MQR492_SOURCE_CONTRACT_ADVERSARIAL_TEST=PASS")

if __name__=="__main__": main()
