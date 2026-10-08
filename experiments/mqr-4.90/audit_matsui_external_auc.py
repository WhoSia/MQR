#!/usr/bin/env python3
"""MQR-4.90: Matsui (2026) source-reported geographically matched AUC scores.

Appendix C Table A4 (within-calibration 4-fold CV AUC) matched to Tables
A1–A3 (different-continent test AUC) under *native-region-only* model
calibration, with all available distinct targets selected without looking
at outcome values. Corrected article DOI 10.1002/ece3.73828 modifies
calibration COMBINATION count and data availability, not these native-
region-only rows.

Crucial design non-equivalence: article §2.4 Maxent cross-validation
uses presence vs Maxent background, while article §2.3 target AUC treats
climate cells lacking observed presence as absence. Hence a numerical
CV-minus-target AUC is a cross-design REPORTING GAP, not an identified
generalization optimism effect; each species shares a calibration family,
and covariance/precision is unavailable. The model fitting and scoring
are source-reported; we did NOT rerun Maxent or use raw predictions.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).with_name("matsui_2026_native_only_external_auc_pairs.csv")
EXPECTED = (
    "species", "calibration", "target", "internal_cv_auc",
    "external_region_auc", "source_cv_table", "source_external_table",
    "cv_negative_definition", "external_negative_definition",
    "extraction_scope",
)
SOURCES = {
    "Oxalis latifolia": ("America", "A1", 3, 0.87),
    "Digitaria sanguinalis": ("Europe", "A2", 4, 0.82),
    "Amaranthus retroflexus": ("North America", "A3", 3, 0.85),
}


def load(path=DATA_PATH):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != EXPECTED:
            raise ValueError("source fields changed")
        rows = list(reader)
    if len(rows) != 10:
        raise ValueError("all ten native-only external targets required")
    unique = set()
    counts = defaultdict(int)
    for row in rows:
        species = row["species"]
        if species not in SOURCES:
            raise ValueError("unregistered biological family")
        calibration, table, expected_n, cv = SOURCES[species]
        if (row["calibration"], row["source_external_table"]) != (calibration, table):
            raise ValueError("source genealogy mismatch")
        if row["source_cv_table"] != "A4" or row["extraction_scope"] != "native_only":
            raise ValueError("not prespecified native-only stratum")
        if row["target"] == calibration:
            raise ValueError("external target not disjoint")
        if float(row["internal_cv_auc"]) != cv:
            raise ValueError("source-printed CV AUC changed")
        if row["cv_negative_definition"] != "Maxent background":
            raise ValueError("source CV negative design mismatch")
        if row["external_negative_definition"] != "grid cells without recorded presences":
            raise ValueError("source external negative design mismatch")
        if not (0 <= float(row["external_region_auc"]) <= 1):
            raise ValueError("external AUC invalid")
        key = (species, calibration, row["target"])
        if key in unique:
            raise ValueError("duplicate region tuple")
        unique.add(key)
        counts[species] += 1
    for species, (_, _, n, _) in SOURCES.items():
        if counts[species] != n:
            raise ValueError("unmatched native-only targets")
    return rows


def within_species_profiles(rows):
    by_species = defaultdict(list)
    for row in rows:
        diff = round(float(row["internal_cv_auc"]) -
                     float(row["external_region_auc"]), 2)
        by_species[row["species"]].append((row["target"], diff))
    return {
        species: {
            "source_calibration": SOURCES[species][0],
            "contrast_cv_minus_external_by_target": [
                {"target": target, "gap": value} for target, value in pairs
            ],
            "minimum_reporting_gap": min(value for _, value in pairs),
            "maximum_reporting_gap": max(value for _, value in pairs),
            "signed_gap_reversals": any(x > 0 for _, x in pairs) and
                                    any(x < 0 for _, x in pairs),
        }
        for species, pairs in sorted(by_species.items())
    }


def admission(rows):
    """Do not pool nominally same AUC across mismatched reference designs."""
    negative_types = {
        (row["cv_negative_definition"], row["external_negative_definition"])
        for row in rows
    }
    fail = []
    if any(a != b for a, b in negative_types):
        fail.append("AUC_NEGATIVE_CLASS_SAMPLING_MISMATCH")
    # A4 table contains average CV AUC but no per-fold paired predictions;
    # A1–A3 scores have no per-row uncertainty/covariance reported.
    fail.append("PAIRED_PREDICTION_AND_COVARIANCE_UNAVAILABLE")
    fail.append("TRAINING_POLICY_REFIT_RELATION_NEEDS_RECONSTRUCTION")
    return {"meta_pool_eligible": False, "limitations": fail}


def audit():
    rows = load()
    profile = within_species_profiles(rows)
    out = {
        "paper": "Matsui (2026), DOI 10.1002/ece3.73534",
        "erratum": "10.1002/ece3.73828",
        "data_rows_source_reported": len(rows),
        "calibration_families": len(profile),
        "source_tables": ["A1", "A2", "A3", "A4"],
        "source_rule": "one native-only calibration per species; all external target regions",
        "score_type": "cross-design geographically linked AUC reporting difference",
        "families": profile,
        "admission": admission(rows),
        "confidence_interval": None,
        "pooled_estimate": None,
        "independent_model_reproduction": False,
    }
    ox = profile["Oxalis latifolia"]
    assert ox["contrast_cv_minus_external_by_target"] == [
        {"target": "Oceania", "gap": .34},
        {"target": "Africa", "gap": .06},
        {"target": "Europe", "gap": -.02},
    ]
    assert profile["Digitaria sanguinalis"]["maximum_reporting_gap"] == .26
    assert profile["Amaranthus retroflexus"]["minimum_reporting_gap"] == -.07
    assert ox["signed_gap_reversals"]
    assert profile["Amaranthus retroflexus"]["signed_gap_reversals"]
    assert len(profile) == 3 and len(rows) == 10
    assert out["admission"]["meta_pool_eligible"] is False
    return out


if __name__ == "__main__":
    result = audit()
    print("MQR490_MATSUI_MATCHED_SCORE_ROWS=10")
    print("MQR490_MATSUI_SOURCE_FAMILIES=3")
    print("MQR490_MATSUI_OXALIS_REVERSAL=PASS")
    print("MQR490_MATSUI_DESIGN_MISMATCH=CONFIRMED")
    print("MQR490_MATSUI_META_POOLING=HOLD")
    print("MQR490_MATSUI_ORIGINAL_MODEL_RERUN=NOT_PERFORMED")
    print(json.dumps(result, indent=2, sort_keys=True))
