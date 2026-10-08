#!/usr/bin/env python3
"""MQR-4.90: exact, null-model AUC selection counterexample.

For two positive and two negative test observations, enumerate all six
equally likely rank labelings under random independent continuous scores.
This is a generic mathematical fixture, NOT an effect extracted from the
Serov et al. (2026) data. Its source-facing motivation is the reported
filter "target test ROC AUC > 0.7" in Serov et al. Scientific Reports
16:6921 (2026), and the public authors' notebook datasets.ipynb.

Conditioning eligibility on the held-out target performance changes the
estimand and may create postselection optimism when the same target
observations are used for summary. It does not negate valid conditional
comparisons under the explicitly filtered model population.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

N = 4
N_POS = 2
THRESHOLD = Fraction(7, 10)


def all_null_test_auc():
    """Exact finite AUC distribution; scores strictly increase with rank."""
    scores = range(N)
    results = []
    for positives in combinations(scores, N_POS):
        negatives = set(scores).difference(positives)
        wins = sum(p > n for p in positives for n in negatives)
        results.append(Fraction(wins, N_POS * (N - N_POS)))
    return results


def summarize():
    auc = all_null_test_auc()
    admitted = [x for x in auc if x > THRESHOLD]
    assert auc and admitted
    unconditioned = sum(auc) / len(auc)
    conditioned = sum(admitted) / len(admitted)
    return {
        "unfiltered_null_auc": unconditioned,
        "target_selected_null_auc": conditioned,
        "postselection_gap": conditioned - unconditioned,
        "admission_fraction": Fraction(len(admitted), len(auc)),
        "counts": Counter(auc),
    }


def validate():
    data = summarize()
    assert len(all_null_test_auc()) == 6
    assert data["counts"] == {
        Fraction(0): 1,
        Fraction(1, 4): 1,
        Fraction(1, 2): 2,
        Fraction(3, 4): 1,
        Fraction(1): 1,
    }
    assert data["unfiltered_null_auc"] == Fraction(1, 2)
    assert data["target_selected_null_auc"] == Fraction(7, 8)
    assert data["admission_fraction"] == Fraction(1, 3)
    assert data["postselection_gap"] == Fraction(3, 8)
    # Changing the target criterion changes what is being summarized.
    assert any(x <= THRESHOLD for x in all_null_test_auc())


if __name__ == "__main__":
    validate()
    data = summarize()
    print("MQR490_TARGET_CONDITIONED_NULL_AUC=0.875")
    print("MQR490_UNFILTERED_NULL_AUC=0.5")
    print("MQR490_POSTSELECTION_GAP=0.375")
    print("MQR490_ADMISSION_FRACTION=1/3")
    print("MQR490_ORIGINAL_SEROv_REPLICATION=NOT_PERFORMED")
    print("MQR490_NULL_AUC_EXACT_TEST=PASS")
