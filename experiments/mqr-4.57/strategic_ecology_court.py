from __future__ import annotations
import json
from pathlib import Path
from countermodels import attacks, positives

ATTACK_KEYS = (
    "challenge_withholding",
    "challenge_stuffing",
    "cost_shading",
    "cost_inflation",
    "target_relabeling",
    "proxy_shopping",
    "metric_migration",
    "funding_contest_dissipation",
    "publication_selection_deterioration",
    "coalition_capture",
    "sybil_challenge_ecology",
    "performative_target_shift",
    "strategic_exterior_capture",
    "equilibrium_bad_science",
    "mechanism_switch_reversal",
    "counterfactual_hidden_challenge",
    "strategic_replication_suppression",
    "adaptive_wcepr_capture",
)
POSITIVE_KEYS = (
    "truthful_report_local_mechanism",
    "exterior_randomized_challenge",
    "mechanism_counterfactual_replay",
    "realized_cost_reconciliation",
    "target_change_ratification",
    "incentive_independent_convergence",
    "anti_sybil_ancestry_compression",
    "capture_triggered_reconstitution",
)

def main():
    a = attacks()
    p = positives()
    report = {
        "stage": "MQR-4.57",
        "preseal_commit": "fd1580bbc3709901f17eba0860bb882da684bff9",
        "attacks": a,
        "positives": p,
        "wcepr_incentive_robust_by_default": "REJECT",
        "equilibrium_implies_epistemic_adequacy": "REJECT",
        "nominal_agent_count_implies_independence": "REJECT",
        "universal_scientific_mechanism": "NOT_EARNED",
        "wcser": "CANDIDATE",
    }
    out = Path(__file__).parent / "results" / "strategic_ecology_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for k in ATTACK_KEYS:
        print(f"mqr457.{k}={'PASS' if a[k] else 'FAIL'}")
    for k in POSITIVE_KEYS:
        print(f"mqr457.{k}={'ADMIT' if p[k] else 'HOLD'}")
    print("mqr457.wcepr_incentive_robust_by_default=REJECT")
    print("mqr457.equilibrium_implies_epistemic_adequacy=REJECT")
    print("mqr457.nominal_agent_count_implies_independence=REJECT")
    print("mqr457.universal_scientific_mechanism=NOT_EARNED")
    print("mqr457.wcser=CANDIDATE")

if __name__ == "__main__":
    main()
