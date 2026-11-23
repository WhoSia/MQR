"""MQR 5.4 R108 — observed absence does not identify occupancy vs detection.

The counts are an EXISTING 4.95 source-specific contingency table, not raw
survey histories. The three scientific worlds below are hypothetical causal
models under strong assumptions (fixed sites, no false positives, independent
repeat detections conditional on stable occupancy, no reporting selection).
They exactly agree on a *single* observation's marginal distribution but
predict different next detections conditional on a first non-detection.
This is standard occupancy-detection theory, NOT an original theorem.
"""
from fractions import Fraction as F
import json

PRESENT = 3486
ABSENT = 11165
R = F(PRESENT, PRESENT + ABSENT)


def world(name, occupied, detected_given_occupied):
    q = F(occupied)
    d = F(detected_given_occupied)
    if not (0 <= q <= 1 and 0 <= d <= 1 and q*d == R):
        raise ValueError("model invalid or not single-visit observationally equivalent")
    # Site stable; no false positives; first and second attempts independent given Z.
    conditional_resurvey = q * (1-d) * d / (1-q*d)
    return {"world":name,
            "occupancy_q":str(q),
            "detection_d":str(d),
            "single_visit_recorded_present":str(q*d),
            "next_positive_given_first_negative":str(conditional_resurvey),
            "next_positive_float":round(float(conditional_resurvey),8)}


def test():
    models=(
        world("low_occupancy_perfect_detection",R,F(1)),
        world("intermediate",F(1,2),2*R),
        world("all_occupied_imperfect_detection",F(1),R),
    )
    assert len(set(m["single_visit_recorded_present"] for m in models)) == 1
    assert len(set(m["next_positive_given_first_negative"] for m in models)) == 3
    assert models[0]["next_positive_given_first_negative"] == "0"
    assert models[-1]["next_positive_given_first_negative"] == str(R)
    try: world("bad",F(1,2),F(1))
    except ValueError: pass
    else: raise AssertionError("unequal first-visit marginals accepted")
    return {"result":"PASS_EXACT_THREE_WORLDS_ONE_MARGINAL",
            "existing_source_4_95_spring":{"present":PRESENT,"absent":ABSENT},
            "hypothetical_models":models,
            "key_caveat":"4.95 one-row per reported record is NOT certified as a closed-site independent-revisit survey design",
            "actual_revisit_data_added":False,
            "new_mathematical_theorem":False,
            "physical_cross_science_translation_proven":False,
            "negative_controls":1}


if __name__=="__main__":
    print(json.dumps(test(),ensure_ascii=False,sort_keys=True))
