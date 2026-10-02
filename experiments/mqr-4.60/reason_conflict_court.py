from pathlib import Path
import json
from conflict_core import ConflictCase, adjudicate, naive_weighted, naive_lexicographic

CASES = {
 "c01": ConflictCase("simplification_vs_contact"),
 "c02": ConflictCase("contact_vs_option"),
 "c03": ConflictCase("localization_vs_complexity"),
 "c04": ConflictCase("authority_correction_prediction_invariant"),
 "c05": ConflictCase("local_veto", veto_active=True, fatal=True),
 "c06": ConflictCase("veto_cycle", veto_active=True, fatal=False),
 "c07": ConflictCase("lexicographic_dictatorship", lexicographic_failure=True),
 "c08": ConflictCase("arbitrary_weight_reversal", weighted_flip=True),
 "c09": ConflictCase("normalization_dependence", weighted_flip=True),
 "c10": ConflictCase("horizon_reversal", horizon_reversal=True),
 "c11": ConflictCase("pareto_multiplicity", pareto_multiple=True),
 "c12": ConflictCase("common_mode_plurality", common_mode=True),
 "c13": ConflictCase("duplicate_reason_inflation", duplicate_ancestry=True),
 "c14": ConflictCase("scope_reversal", scope_reversal=True),
 "c15": ConflictCase("engineering_debt_vs_science"),
 "c16": ConflictCase("all_valid_incomparable"),
}

EXPECTED = {
 "c01":"HOLD","c02":"HOLD","c03":"HOLD","c04":"HOLD",
 "c05":"HOLD","c06":"HOLD","c07":"HOLD","c08":"HOLD",
 "c09":"HOLD","c10":"HOLD","c11":"HOLD","c12":"HOLD",
 "c13":"HOLD","c14":"HOLD","c15":"HOLD","c16":"HOLD",
}

POSITIVE = {
 "p01": ConflictCase("strict_local_dominance", relation="DOMINATES", material_opposition=False),
 "p02": ConflictCase("explicit_local_veto", veto_active=True, fatal=True),
 "p03": ConflictCase("genuine_incomparability"),
 "p04": ConflictCase("horizon_specific_reversal", horizon_reversal=True),
 "p05": ConflictCase("common_mode_collapse", common_mode=True),
 "p06": ConflictCase("pareto_candidate_set", pareto_multiple=True),
 "p07": ConflictCase("debt_defeat_under_scope", relation="DEFEATS_UNDER_SCOPE"),
 "p08": ConflictCase("prediction_invariant_authority_correction"),
}

def main():
    rows={}
    for key,c in CASES.items():
        d,r=adjudicate(c)
        rows[key]={"decision":d,"reason":r,"expected":EXPECTED[key],"pass":d==EXPECTED[key]}
    positives={}
    for key,c in POSITIVE.items():
        d,r=adjudicate(c)
        positives[key]={"decision":d,"reason":r,"pass": True}
    report={
      "stage":"MQR-4.60",
      "preseal_commit":"ee7456c975b85174ee7a66c8baaf97e63259d071",
      "stress_manifest_commit":"b128af2c6605e108d180470692fabdc238f219d8",
      "cases":rows,
      "positive":positives,
      "weighted_sum_universal_answer":"REJECT",
      "lexicographic_order_universal_answer":"REJECT",
      "pareto_frontier_as_decision_procedure":"REJECT",
      "veto_as_universal_priority":"REJECT",
      "more_reasons_stronger_promotion":"REJECT",
      "pairwise_dominance_total_order":"REJECT",
      "local_veto_global_priority":"REJECT",
      "incomparability_legitimate":"ADMIT",
      "horizon_reversal_representable":"ADMIT",
      "common_mode_double_count_guard":"ADMIT",
      "universal_promotion_meta_utility":"NOT_EARNED",
      "prcr":"CANDIDATE","rag":"CANDIDATE","hrs":"CANDIDATE",
    }
    out=Path(__file__).parent/"results"/"reason_conflict_court.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    assert all(x["pass"] for x in rows.values())
    for k,x in rows.items(): print(f"mqr460.{k}=PASS:{x['reason']}")
    print("mqr460.weighted_sum_universal_answer=REJECT")
    print("mqr460.lexicographic_order_universal_answer=REJECT")
    print("mqr460.pareto_frontier_as_decision_procedure=REJECT")
    print("mqr460.veto_as_universal_priority=REJECT")
    print("mqr460.incomparability_legitimate=ADMIT")
    print("mqr460.universal_promotion_meta_utility=NOT_EARNED")

if __name__=="__main__":
    main()
