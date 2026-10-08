#!/usr/bin/env python3
"""MQR-4.90: source-reported oracle AUC reanalysis, not a pooled meta-analysis.

Source: Koldasbayeva & Zaytsev, Ecological Informatics 92 (2025) 103521,
DOI 10.1016/j.ecoinf.2025.103521, Tables 2–3.
Each cell is the reported maximum external-test AUC over hyperparameter runs.
The development-only chosen model's validation-minus-test bias is NOT present.
No species, algorithm, CV configuration, or fold is an independent study.
"""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

SOURCE = Path(__file__).with_name("koldasbayeva_2025_tables_2_3_oracle_auc.csv")
EXPECTED_FIELDS = (
    "dataset", "training_policy", "cv_method", "GBM", "RF", "XGB",
    "LGB", "reported_mean", "source_table", "selection_type",
)
ALGORITHMS = ("GBM", "RF", "XGB", "LGB")
DATASETS = ("Gentianella campestris", "Thaleichthys pacificus")
POLICIES = ("RETRAIN", "LAST FOLD")


def read_source(path=SOURCE):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != EXPECTED_FIELDS:
            raise ValueError("source schema/version mismatch")
        rows = list(reader)
    if len(rows) != 36:
        raise ValueError("expected exactly 36 printed table rows")
    seen = set()
    for row in rows:
        key = (row["dataset"], row["training_policy"], row["cv_method"])
        if key in seen:
            raise ValueError("duplicated source comparison: " + str(key))
        seen.add(key)
        if row["dataset"] not in DATASETS or row["training_policy"] not in POLICIES:
            raise ValueError("unrecognized dataset or deployment policy")
        if row["source_table"] != ("Table 2" if key[0] == DATASETS[0] else "Table 3"):
            raise ValueError("source table genealogy mismatch")
        if row["selection_type"] != "oracle_test_max":
            raise ValueError("the published tables are not CV-chosen test scores")
        vals = [float(row[a]) for a in ALGORITHMS]
        score = float(row["reported_mean"])
        if any(not 0 <= x <= 1 for x in vals + [score]):
            raise ValueError("AUC outside [0,1]")
        # Printed means can differ by rounding of the four printed AUCs.
        if abs(sum(vals) / 4 - score) > .001:
            raise ValueError("reported mean and printed AUCs disagree: " + str(key))
    counts = Counter((r["dataset"], r["training_policy"]) for r in rows)
    if set(counts.values()) != {9} or len(counts) != 4:
        raise ValueError("missing or unbalanced CV/source rows")
    return rows


def primary_admission(record):
    """Typed gate: do not upgrade descriptive/oracle values into effect estimates."""
    reasons = []
    if record.get("selection_type") != "development_only":
        reasons.append("TEST_ORACLE_OR_SELECTION_UNVERIFIED")
    if record.get("reference_origin") != "independent_target":
        reasons.append("EXTERNAL_TARGET_NOT_WARRANTED")
    if record.get("metric_validation") != record.get("metric_external"):
        reasons.append("METRIC_MISMATCH")
    if not record.get("matched_deployment_policy"):
        reasons.append("MODEL_POLICY_MISMATCH")
    if not record.get("external_target_defined"):
        reasons.append("TARGET_DESIGN_UNDEFINED")
    if not record.get("paired_uncertainty_available"):
        reasons.append("PRECISION_OR_COVARIANCE_UNAVAILABLE")
    if not record.get("raw_family_id"):
        reasons.append("COHORT_GENEALOGY_UNVERIFIED")
    return {"admit": not reasons, "reasons": reasons}


def contrast(rows, dataset, policy, cv):
    subset = {(r["dataset"], r["training_policy"], r["cv_method"]): r
              for r in rows}
    key = (dataset, policy, cv)
    reference = (dataset, policy, "Random")
    return round(float(subset[key]["reported_mean"]) -
                 float(subset[reference]["reported_mean"]), 3)


def summarize(rows):
    cases = (
        (DATASETS[0], "LAST FOLD", "SP 600"),
        (DATASETS[0], "RETRAIN", "SP 600"),
        (DATASETS[1], "RETRAIN", "SPT 85"),
        (DATASETS[1], "LAST FOLD", "SPT 85"),
    )
    contrasts = [
        {"dataset": dataset, "policy": policy, "cv": cv, "vs": "Random",
         "delta_reported_oracle_auc": contrast(rows, dataset, policy, cv)}
        for dataset, policy, cv in cases
    ]
    return {
        "source": "Koldasbayeva & Zaytsev (2025), Tables 2 and 3",
        "doi": "10.1016/j.ecoinf.2025.103521",
        "source_rows": len(rows),
        "source_algorithm_auc_cells": len(rows) * len(ALGORITHMS),
        "raw_dataset_families": len(DATASETS),
        "measure": "reported external-test oracle-max ROC AUC",
        "contrasts": contrasts,
        "temporal_target_scope": directional_scope(),
        "primary_validation_optimism_effects": 0,
        "pooled_effect": None,
        "limits": [
            "Test-oracle maxima cannot substitute for untouched test performance",
            "No row contains the matched validation AUC for the same selected model",
            "Two datasets are not 36 independent research families",
            "Descriptive contrasts do not establish statistical significance or causality",
        ],
    }


def self_test(rows):
    assert len(rows) == 36
    assert sum(len([r for r in rows if r["dataset"] == d]) for d in DATASETS) == 36
    cases = {
        (DATASETS[0], "LAST FOLD", "SP 600"): .032,
        (DATASETS[0], "RETRAIN", "SP 600"): .003,
        (DATASETS[1], "RETRAIN", "SPT 85"): .008,
        (DATASETS[1], "LAST FOLD", "SPT 85"): -.010,
    }
    for case, expected in cases.items():
        assert abs(contrast(rows, *case) - expected) < 1e-12, case
    assert contrast(rows, DATASETS[1], "RETRAIN", "SPT 85") > 0
    assert contrast(rows, DATASETS[1], "LAST FOLD", "SPT 85") < 0
    oracle = {
        "selection_type": "oracle_test_max",
        "reference_origin": "independent_target",
        "metric_validation": "AUC", "metric_external": "AUC",
        "matched_deployment_policy": True, "external_target_defined": True,
        "paired_uncertainty_available": True, "raw_family_id": "one_cohort",
    }
    assert not primary_admission(oracle)["admit"]
    valid_synthetic = dict(oracle, selection_type="development_only")
    assert primary_admission(valid_synthetic)["admit"]
    for field, replacement in (
        ("reference_origin", "synthetic_proxy"),
        ("metric_external", "RMSE"),
        ("matched_deployment_policy", False),
        ("external_target_defined", False),
        ("paired_uncertainty_available", False),
        ("raw_family_id", ""),
    ):
        corrupted = dict(valid_synthetic)
        corrupted[field] = replacement
        assert not primary_admission(corrupted)["admit"], field
    assert summarize(rows)["pooled_effect"] is None
    assert temporal_transfer(2006, 2012, 2003, 2005) == "RETROSPECTIVE_TRANSFER"
    assert temporal_transfer(2003, 2005, 2006, 2012) == "PROSPECTIVE_TRANSFER"
    assert temporal_transfer(2003, 2007, 2006, 2009) == "OVERLAPPING_OR_INTERLEAVED"
    assert all(x["orientation"] == "RETROSPECTIVE_TRANSFER"
               for x in directional_scope().values())


def temporal_transfer(train_start, train_end, test_start, test_end):
    """Classify a target-year holdout; out-of-time does not imply forecasting."""
    values = (train_start, train_end, test_start, test_end)
    if not all(isinstance(value, int) for value in values):
        raise ValueError("years must be integers")
    if train_start > train_end or test_start > test_end:
        raise ValueError("invalid temporal intervals")
    if test_end < train_start:
        return "RETROSPECTIVE_TRANSFER"
    if test_start > train_end:
        return "PROSPECTIVE_TRANSFER"
    return "OVERLAPPING_OR_INTERLEAVED"


def directional_scope():
    """Document published years, distinguishing label years from climate years.

    G. campestris: paper §2.2.1 models 2003–2018; upstream public
    main.R loads historical test labels from gen_1994_2002.csv.
    T. pacificus: paper §2.2.2 states train 2006–2012, test 2003–2005.
    """
    intervals = {
        DATASETS[0]: (2003, 2018, 1994, 2002),
        DATASETS[1]: (2006, 2012, 2003, 2005),
    }
    return {
        name: {
            "train_years": [span[0], span[1]],
            "external_years": [span[2], span[3]],
            "orientation": temporal_transfer(*span),
            "prospective_forecast_authority": "NOT_ESTABLISHED",
            "year_source": (
                "article §2.2.1 and upstream GitHub source filenames/main.R"
                if name == DATASETS[0] else "article §2.2.2"
            ),
        }
        for name, span in intervals.items()
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    rows = read_source()
    if args.self_test:
        self_test(rows)
        print("MQR490_TESTS=PASS")
    if args.json:
        print(json.dumps(summarize(rows), indent=2, ensure_ascii=False, sort_keys=True))
    elif not args.self_test:
        result = summarize(rows)
        print("MQR490_ORACLE_ROWS=" + str(result["source_rows"]))
        print("MQR490_SOURCE_CELLS=" + str(result["source_algorithm_auc_cells"]))
        print("MQR490_PRIMARY_EFFECTS_ADMITTED=0")
        print("MQR490_POOLED_ESTIMATE=HOLD")


if __name__ == "__main__":
    main()
