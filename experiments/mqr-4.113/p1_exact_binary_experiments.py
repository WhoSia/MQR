#!/usr/bin/env python3
"""MQR-4.113 P1: EXACT 2×2 stochastic Blackwell / Le Cam comparison.

Finite binary-state, binary-output experiment A, B with each row a
probability distribution.  Directional deficiency is
δ(A→B) = min_{K row-stochastic} max_theta TV((A K)_theta, B_theta).
K=[[x,1-x],[y,1-y]]. For binary signal TV=|first-column delta|.
Solve the 3-variable rational linear program by exhaustive intersection
of constraint triples; exact Fraction arithmetic throughout. The boxed
feasible set is a nonempty bounded polytope, and a linear minimum is
attained at a vertex, so enumerating all feasible vertices is complete.
No statistical experiment constructed here is a measured instrument.
"""
from fractions import Fraction as F
from itertools import combinations
from json import dumps
import argparse
import unittest

ZERO=F(0)
ONE=F(1)

def matrix(rows):
    out=tuple(tuple(F(str(v)) for v in row) for row in rows)
    if len(out)!=2 or any(len(row)!=2 for row in out):
        raise ValueError("EXACT_BINARY_EXPERIMENT_ONLY")
    if any(v<0 or v>1 or sum(row)!=1 for row in out for v in row[:0]):
        raise ValueError("invalid probability")
    for row in out:
        if any(v<ZERO or v>ONE for v in row) or sum(row)!=ONE:
            raise ValueError("each experiment row must be a probability law")
    return out

def solve3(rows, constants):
    """Exact Gaussian elimination, returns None for linearly dependent planes."""
    t=[[F(x) for x in row]+[F(b)] for row,b in zip(rows,constants)]
    for c in range(3):
        pivot=next((r for r in range(c,3) if t[r][c]),None)
        if pivot is None:return None
        t[c],t[pivot]=t[pivot],t[c]
        u=t[c][c];t[c]=[v/u for v in t[c]]
        for r in range(3):
            if r!=c:
                u=t[r][c]
                t[r]=[a-u*b for a,b in zip(t[r],t[c])]
    return tuple(row[3] for row in t)

def constraints(A,B):
    # (coefficient of x,y,t), rhs: linear lhs <= rhs
    walls=[
      ((-ONE,ZERO,ZERO),ZERO), ((ONE,ZERO,ZERO),ONE),
      ((ZERO,-ONE,ZERO),ZERO), ((ZERO,ONE,ZERO),ONE),
      ((ZERO,ZERO,-ONE),ZERO), ((ZERO,ZERO,ONE),ONE),
    ]
    for a,b in zip(A,B):
        p,q=a[0],b[0]
        walls.append(((p,ONE-p,-ONE),q))
        walls.append(((-p,p-ONE,-ONE),-q))
    return walls

def deficiency(source,target):
    A=matrix(source);B=matrix(target);wall=constraints(A,B)
    candidates={}
    for triples in combinations(wall,3):
        xyz=solve3([row for row,_ in triples],[rhs for _,rhs in triples])
        if xyz is None:continue
        if all(sum(v*coef for v,coef in zip(xyz,row))<=rhs for row,rhs in wall):
            # optimize t then stable witness x,y; no floating tolerances
            candidates[xyz]=None
    if not candidates:raise AssertionError("nonempty bounded LP had no rational vertex")
    x,y,t=min(candidates,key=lambda u:(u[2],u[0],u[1]))
    K=((x,ONE-x),(y,ONE-y))
    approximation=tuple((a[0]*x+a[1]*y, ONE-(a[0]*x+a[1]*y)) for a in A)
    error=max(abs(approximation[i][0]-B[i][0]) for i in range(2))
    assert error==t
    assert all(sum(row)==1 and all(0<=z<=1 for z in row) for row in K)
    assert len(candidates)<=120
    return {"delta":t,"kernel":K,"approximation":approximation,"vertices":len(candidates)}

def label(A,B):
    ab=deficiency(A,B);ba=deficiency(B,A)
    if ab["delta"]==0 and ba["delta"]==0:
        tag="BLACKWELL_EQUIVALENT"
    elif ab["delta"]==0:
        tag="SOURCE_STRICTLY_DOMINATES_TARGET"
    elif ba["delta"]==0:
        tag="TARGET_STRICTLY_DOMINATES_SOURCE"
    else:
        tag="INCOMPARABLE_EXPERIMENTS"
    return ab,ba,tag

CASES={
 "fully_revealing_vs_noisy":{
    "source":[["1","0"],["0","1"]],
    "target":[["3/4","1/4"],["1/4","3/4"]],
    "quantity_source":"ABSTRACT_STATE_ID",
    "quantity_target":"ABSTRACT_STATE_ID",
    "operation_source":"SYNTHETIC_FULL_ID",
    "operation_target":"SYNTHETIC_NOISY_ID",
    "calibration":"NONE_SYNTHETIC",
 },
 "unequal_precision":{
    "source":[["4/5","1/5"],["1/5","4/5"]],
    "target":[["3/5","2/5"],["2/5","3/5"]],
    "quantity_source":"ABSTRACT_STATE_ID",
    "quantity_target":"ABSTRACT_STATE_ID",
    "operation_source":"SYNTHETIC_HIGH_PRECISION",
    "operation_target":"SYNTHETIC_LOW_PRECISION",
    "calibration":"NONE_SYNTHETIC",
 },
 "signal_label_permutation":{
    "source":[["1","0"],["0","1"]],
    "target":[["0","1"],["1","0"]],
    "quantity_source":"ABSTRACT_STATE_ID",
    "quantity_target":"ABSTRACT_STATE_ID",
    "operation_source":"ABSTRACT_SAME_OPERATION",
    "operation_target":"ABSTRACT_SAME_OPERATION",
    "calibration":"NONE_SYNTHETIC",
 },
 "erased_state_signal":{
    "source":[["1/2","1/2"],["1/2","1/2"]],
    "target":[["1","0"],["0","1"]],
    "quantity_source":"ABSTRACT_STATE_ID",
    "quantity_target":"ABSTRACT_STATE_ID",
    "operation_source":"SYNTHETIC_UNINFORMATIVE",
    "operation_target":"SYNTHETIC_FULL_ID",
    "calibration":"NONE_SYNTHETIC",
 },
 "two_incomparable_discriminators":{
    "source":[["1","0"],["1/2","1/2"]],
    "target":[["1/2","1/2"],["0","1"]],
    "quantity_source":"ABSTRACT_STATE_ID",
    "quantity_target":"ABSTRACT_STATE_ID",
    "operation_source":"SYNTHETIC_STATE0_BIASED",
    "operation_target":"SYNTHETIC_STATE1_BIASED",
    "calibration":"NONE_SYNTHETIC",
 },
 "same_statistics_different_measurand":{
    "source":[["3/4","1/4"],["1/4","3/4"]],
    "target":[["3/4","1/4"],["1/4","3/4"]],
    "quantity_source":"TEMPERATURE",
    "quantity_target":"DOSE",
    "operation_source":"SYNTHETIC_THERMOMETER",
    "operation_target":"SYNTHETIC_DOSIMETER",
    "calibration":"INCOMPARABLE_INSTRUMENT_LINEAGES_UNVERIFIED",
 },
 "same_statistics_shared_calibration":{
    "source":[["3/4","1/4"],["1/4","3/4"]],
    "target":[["3/4","1/4"],["1/4","3/4"]],
    "quantity_source":"DOSE",
    "quantity_target":"DOSE",
    "operation_source":"SYNTHETIC_DEVICE_A",
    "operation_target":"SYNTHETIC_DEVICE_B",
    "calibration":"SHARED_UNVERIFIED_STANDARD",
 },
}

def report():
    output=[]
    for name,case in CASES.items():
        ab,ba,category=label(case["source"],case["target"])
        # A stochastic kernel alone never certifies an operation, instrument
        # measurand or causal source ancestry. This remains HOLD even if tags
        # match. Explicit quantity mismatch is a definite declared failure.
        quantity="DECLARED_MISMATCH" if case["quantity_source"]!=case["quantity_target"] else "DECLARED_MATCH_UNVERIFIED"
        out={
            "case":name,"model_source":"SYNTHETIC_RATIONAL_BINARY_EXPERIMENTS_ONLY",
            "mathematical_relation":category,"delta_A_to_B":str(ab["delta"]),
            "delta_B_to_A":str(ba["delta"]),
            "le_cam_distance":str(max(ab["delta"],ba["delta"])),
            "witness_K_A_to_B":[[str(z) for z in row] for row in ab["kernel"]],
            "witness_K_B_to_A":[[str(z) for z in row] for row in ba["kernel"]],
            "A_to_B_vertex_count":ab["vertices"],"B_to_A_vertex_count":ba["vertices"],
            "declared_quantity_equality":quantity,
            "declared_calibration_ancestry":case["calibration"],
            "external_operation_warrant":"HOLD",
            "real_world_measurand_identity":"HOLD",
            "statistical_world_data_provenance":"NO_REAL_MEASUREMENT_ADMITTED",
            "historical_FER_4_112_source_gate":"FULL_AUTHOR_BIN_BINX_AND_ROSTER_HOLD",
            "Real_Lang_0_43_promotion":"NOT_AUTOMATIC",
        }
        output.append(out)
    return output

class ExactBinaryExperimentTests(unittest.TestCase):
 def test_fraction_onto_more_noisy(self):
    a,b,_=label(CASES["fully_revealing_vs_noisy"]["source"],CASES["fully_revealing_vs_noisy"]["target"])
    self.assertEqual(a["delta"],0);self.assertEqual(b["delta"],F(1,4))
 def test_unequal_precision(self):
    a,b,_=label(CASES["unequal_precision"]["source"],CASES["unequal_precision"]["target"])
    self.assertEqual(a["delta"],0);self.assertEqual(b["delta"],F(1,5))
 def test_source_erased(self):
    a,b,_=label(CASES["erased_state_signal"]["source"],CASES["erased_state_signal"]["target"])
    self.assertEqual(a["delta"],F(1,2));self.assertEqual(b["delta"],0)
 def test_permutation_both_directions(self):
    a,b,t=label(CASES["signal_label_permutation"]["source"],CASES["signal_label_permutation"]["target"])
    self.assertEqual((a["delta"],b["delta"]),(0,0));self.assertEqual(t,"BLACKWELL_EQUIVALENT")
 def test_incomparable(self):
    a,b,t=label(CASES["two_incomparable_discriminators"]["source"],CASES["two_incomparable_discriminators"]["target"])
    self.assertGreater(a["delta"],0);self.assertGreater(b["delta"],0)
    self.assertEqual(t,"INCOMPARABLE_EXPERIMENTS")
 def test_same_stats_not_same_physical_quantity(self):
    r={x["case"]:x for x in report()}
    self.assertEqual(r["same_statistics_different_measurand"]["le_cam_distance"],"0")
    self.assertEqual(r["same_statistics_different_measurand"]["declared_quantity_equality"],"DECLARED_MISMATCH")
    self.assertEqual(r["same_statistics_different_measurand"]["real_world_measurand_identity"],"HOLD")
 def test_incorrect_probability_rejected(self):
    with self.assertRaises(ValueError):matrix([["1/2","1/4"],["0","1"]])
    with self.assertRaises(ValueError):matrix([["-1","2"],["0","1"]])
 def test_exact_row_stochastic_witness(self):
    for c in CASES.values():
      a,b=matrix(c["source"]),matrix(c["target"]); w=deficiency(a,b)
      for row in w["kernel"]:
        self.assertEqual(sum(row),1)
      self.assertEqual(max(abs(w["approximation"][i][0]-b[i][0]) for i in range(2)),w["delta"])
 def test_no_claim_real_measurement(self):
    self.assertTrue(all(x["statistical_world_data_provenance"]=="NO_REAL_MEASUREMENT_ADMITTED" for x in report()))
 def test_singular_source_is_supported(self):
    a=[["1/3","2/3"],["1/3","2/3"]]
    b=[["1/2","1/2"],["1/2","1/2"]]
    self.assertEqual(deficiency(a,b)["delta"],0)

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--test",action="store_true")
 p.add_argument("--output",default=None)
 args=p.parse_args()
 if args.test:
    unittest.main(argv=["binary_blackwell_2113"],exit=False,verbosity=2)
 else:
    text=dumps({"science_version":"MQR-4.113-P1-EXACT_BINARY_STOCHASTIC",
      "claim_scope":"FINITE_ABSTRACT_CHANNELS_ONLY","comparisons":report()},
      indent=2,ensure_ascii=False)
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f:f.write(text+"\n")
    print(text)
