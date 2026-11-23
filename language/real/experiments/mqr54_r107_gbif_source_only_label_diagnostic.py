"""MQR 5.4 R107 — source-only label diagnostic on the audited 4.95 2024 GBIF 3x2 receipt.

Original data are NOT downloaded by this module. All six counts are transcribed
from docs/MQR-4.95-FINAL-BOUNDED-SCIENTIFIC-CLOSEOUT.md. The first contributor
is Finnish Nature League Spring monitoring; the second Kastikka Floristic
Archives; third the remaining 25 original contributing dataset IDs.

All metrics are IN-SAMPLE descriptive properties of recorded labels and source
memberships; they do not estimate true ecological absence or demonstrate a
model's learned leakage, causal source effect, or predictive transport.
"""
from fractions import Fraction as F
import json

TABLE = ((11165, 3486), (0, 9686), (1, 5205))  # ABSENT, PRESENT


def analyze(table=TABLE):
    if len(table) != 3 or any(len(row) != 2 for row in table):
        raise ValueError("exact 3x2 contingency required")
    if any(type(v) is not int or v < 0 for row in table for v in row):
        raise ValueError("nonnegative integer counts required")
    n = sum(map(sum, table))
    neg = sum(row[0] for row in table)
    pos = sum(row[1] for row in table)
    if min(n,neg,pos) <= 0 or any(sum(row) == 0 for row in table):
        raise ValueError("nondegenerate cases required")
    # Retrospectively chosen simple source-only classifier:
    # A=source 0 -> ABSENT, the other 26 provider IDs -> PRESENT.
    tp = table[1][1]+table[2][1]
    tn = table[0][0]
    fp = table[1][0]+table[2][0]
    fn = table[0][1]
    acc = F(tp+tn,n)
    baseline = F(max(pos,neg),n)
    bacc = (F(tp,pos)+F(tn,neg))/2
    chi2 = sum((F((o*n-sum(row)*col_total)**2,
                   sum(row)*col_total*n)
                for row in table
                for o,col_total in zip(row,(neg,pos))),F(0))
    v2 = chi2/n  # Cramer's V squared: min(r-1,c-1)=1
    outside_neg_rate = F(table[1][0]+table[2][0],
                         sum(table[1])+sum(table[2]))
    source_neg_rate = F(table[0][0],sum(table[0]))
    assert (tp+fn == pos and tn+fp == neg)
    return {
        "status":"PASS_EXACT_IN_SAMPLE_SOURCE_LABEL_DIAGNOSTIC",
        "n":n,"absent":neg,"present":pos,
        "source_only_confusion":{"TP":tp,"TN":tn,"FP":fp,"FN":fn},
        "source_only_accuracy_exact":str(acc),
        "source_only_accuracy":round(float(acc),7),
        "all_majority_label_accuracy":round(float(baseline),7),
        "accuracy_gain_percentage_points":round(100*float(acc-baseline),4),
        "source_only_balanced_accuracy":round(float(bacc),7),
        "pearson_chi_square":round(float(chi2),5),
        "cramers_v":round(float(v2)**.5,7),
        "source_absent_rate_exact":str(source_neg_rate),
        "other_sources_absent_rate_exact":str(outside_neg_rate),
        "original_raw_record_retrieval_in_this_step":False,
        "source_only_rule_selected_outcome_informed":True,
        "held_out_geographic_accuracy_estimated":False,
        "true_ecological_absence_estimated":False,
        "source_causal_effect_identified":False,
        "original_author_model_executed":False
    }


def test():
    r=analyze()
    assert (r["n"],r["absent"],r["present"])==(29543,11166,18377)
    assert r["source_only_accuracy_exact"]=="26056/29543"
    assert r["source_only_confusion"]=={"TP":14891,"TN":11165,"FP":1,"FN":3486}
    assert F(r["source_absent_rate_exact"]) == F(11165,14651)
    assert F(r["other_sources_absent_rate_exact"]) == F(1,14892)
    assert 0 < r["cramers_v"] < 1
    for bad in (((-1,1),(1,1),(1,1)), ((1,0),(0,0),(0,1))):
        try: analyze(bad)
        except ValueError: pass
        else: raise AssertionError("invalid contingency accepted")
    return {**r, "negative_input_controls":2}


if __name__=="__main__":
    print(json.dumps(test(),sort_keys=True,ensure_ascii=False))
