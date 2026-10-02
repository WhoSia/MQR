from __future__ import annotations
import json
from pathlib import Path
from countermodels import attacks, positives

ATTACK_KEYS=(
"cheap_challenge_trap",
"information_relevance_divergence",
"novelty_drift",
"incumbent_proxy_goodhart",
"target_relevance_drift",
"adversarial_decoy_flood",
"common_evaluator_capture",
"cost_unit_rank_reversal",
"horizon_reversal",
"actionability_divergence",
"surprise_not_importance",
"sunk_yield_lockin",
"value_model_self_insulation",
"equal_current_value_unequal_option",
)
POSITIVE_KEYS=(
"declared_model_local_optimizer",
"partial_order_guidance",
"target_drift_reopening",
"adversarial_decoy_rejection",
"option_opening_value",
"value_model_revision",
)

def main():
    a=attacks(); p=positives()
    report={
      "stage":"MQR-4.56",
      "preseal_commit":"4f664412c74804b69546fe8259710e82c47328c4",
      "attacks":a,"positives":p,
      "universal_scientific_utility":"REJECT",
      "challenge_value_scalar_default":"OFF",
      "value_constitution_self_authorizes":"REJECT",
      "world_optimal_expansion_policy":"NOT_EARNED",
      "wcepr":"CANDIDATE",
    }
    out=Path(__file__).parent/"results"/"expansion_policy_report.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    for k in ATTACK_KEYS:
        print(f"mqr456.{k}={'PASS' if a[k] else 'FAIL'}")
    for k in POSITIVE_KEYS:
        print(f"mqr456.{k}={'ADMIT' if p[k] else 'HOLD'}")
    print("mqr456.universal_scientific_utility=REJECT")
    print("mqr456.challenge_value_scalar_default=OFF")
    print("mqr456.value_constitution_self_authorizes=REJECT")
    print("mqr456.world_optimal_expansion_policy=NOT_EARNED")
    print("mqr456.wcepr=CANDIDATE")

if __name__=="__main__":
    main()
