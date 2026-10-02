from __future__ import annotations
import json
from pathlib import Path
from countermodels import attacks, positives

ATTACK_KEYS=(
"many_probes_one_ancestry",
"probe_saturation_intervention_escape",
"intervention_saturation_morphism_escape",
"target_generated_defeat_blindness",
"serialization_inflation",
"generator_closure_world_escape",
"expert_headcount_common_mode",
"productive_intuition_generator",
"seductive_intuition_not_oracle",
"formal_completeness_primitive_omission",
"protocol_not_competence",
"same_family_different_expansion_capacity",
)
POSITIVE_KEYS=(
"rigor_repairs_intuition",
"intuition_generate_world_adjudicate",
"cross_channel_convergence",
"tacit_competence_reconstructible",
"open_family_local_adequacy",
)

def main():
    a=attacks(); p=positives()
    verdicts={**a,**p}
    report={
      "stage":"MQR-4.55",
      "preseal_commit":"f422889cca5afb52223b0ff5518e27c0b0f24dae",
      "verdicts":verdicts,
      "self_certifying_consequence_family":"REJECT",
      "formal_rigor_implies_family_completeness":"REJECT",
      "intuition_self_authorizes":"REJECT",
      "world_consequence_family_complete":"NO",
      "more_tests_implies_more_authority":"REJECT",
      "wccfr":"CANDIDATE",
    }
    out=Path(__file__).parent/"results"/"consequence_family_report.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    for k in ATTACK_KEYS:
        print(f"mqr455.{k}={'PASS' if a[k] else 'FAIL'}")
    for k in POSITIVE_KEYS:
        print(f"mqr455.{k}={'ADMIT' if p[k] else 'HOLD'}")
    print("mqr455.self_certifying_consequence_family=REJECT")
    print("mqr455.formal_rigor_implies_family_completeness=REJECT")
    print("mqr455.intuition_self_authorizes=REJECT")
    print("mqr455.world_consequence_family_complete=NO")
    print("mqr455.more_tests_implies_more_authority=REJECT")
    print("mqr455.wccfr=CANDIDATE")

if __name__=="__main__":
    main()
