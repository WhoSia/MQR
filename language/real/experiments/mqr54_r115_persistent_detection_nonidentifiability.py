"""MQR 5.4 R115 — repeated site visits alone need not identify occupancy.

Exact counterexample to naive 'repetition always identifies q/p'. Two worlds
have the same k-visit *joint* detection histories for every k:
A: latent occupancy Z ~ Bernoulli(r), perfect detection at occupied sites.
B: all sites occupied, but persistent detector availability H ~ Bernoulli(r),
   shared across every within-site visit: Y_j=H for all j.

A genuinely exogenous, independently redrawn detection mechanism on a later
visit distinguishes these worlds, but its physical feasibility is UNPROVEN.
r is only a previously audited publisher-record fraction, NOT certified
independent site prevalence. Standard occupancy/detection prior art applies.
"""
from fractions import Fraction as F
from itertools import product
import json

R = F(3486, 14651)


def probability(world, history, reset=False):
    if world not in ("A", "B"): raise ValueError("unknown world")
    if not history or any(y not in (0,1) for y in history):
        raise ValueError("binary nonempty history required")
    # reset denotes independently changed detection on the LAST visit only,
    # with a certified non-disturbing physical state.
    first = history[:-1] if reset else history
    last = history[-1]
    if not reset:
        return R if all(first) else (1-R if not any(first) else F(0))
    # A: perfect detection of fixed site occupancy; repeat remains its state.
    if world == "A":
        return R if all(history) else (1-R if not any(history) else F(0))
    # B: initial device availability H persists until an independent
    # reset H' on final occasion.
    prefix_probability = R if all(first) else (1-R if not any(first) else F(0))
    return prefix_probability * (R if last else 1-R)


def test():
    checked=0
    for k in range(1,11):
        a=b=F(0)
        for path in product((0,1), repeat=k):
            pa=probability("A",path)
            pb=probability("B",path)
            assert pa==pb
            a+=pa;b+=pb;checked+=1
        assert a==b==1
    # Given an earlier negative observation, independent measurement reset
    # gives possible rescue in B but none in A.
    assert probability("A",(0,1),True)==0
    assert probability("B",(0,1),True)==(1-R)*R
    assert probability("A",(0,0),True)==1-R
    assert probability("B",(0,0),True)==(1-R)**2
    # Ordinary independent repeated detection produces mixed histories and
    # is therefore a DIFFERENT assumption from persistent availability.
    assert (1-R)*R>0
    for bad in ("C",):
        try: probability(bad,(0,1))
        except ValueError: pass
        else: raise AssertionError("unknown world accepted")
    return {"result":"PASS_EXACT_CORRELATED_REVISIT_NONIDENTIFICATION",
            "original_observed_publisher_fraction":str(R),
            "binary_joint_patterns_checked":checked,
            "worlds_equal_without_reset_for_all_tested_k":True,
            "P_B_01_after_intervention":str((1-R)*R),
            "P_A_01_after_intervention":"0",
            "field_reset_or_revisit_experiment_performed":False,
            "site_level_q_p_identified_from_original_data":False,
            "new_theorem":False}


if __name__=="__main__":
    print(json.dumps(test(),sort_keys=True))
