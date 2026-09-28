from __future__ import annotations

import argparse
import inspect
import json
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

from generators import fault, measurement, search
from generators.common import (
    FAMILIES,
    PRESEAL,
    MetricVector,
    Observable,
    HiddenGold,
    aggregate,
    calibration_key,
    continue_all_policy,
    fixed_policy,
    lag_policy,
    oqsc_policy,
    pareto_dominates,
    patience_policy,
    score_trace,
    simulate,
    stop_now_policy,
)

ADAPTERS = (fault, measurement, search)
REPLICATES = {
    "DISCOVERY": 3,
    "CALIBRATION": 4,
    "HOLDOUT": 6,
}

def build_traces():
    traces = []
    for adapter in ADAPTERS:
        for family in FAMILIES:
            for split, n in REPLICATES.items():
                for replicate in range(n):
                    traces.append(adapter.generate(family, split, replicate))
    return traces

def select_parameter(traces, candidates):
    scored = []
    for parameter, policy in candidates:
        metric = aggregate(traces, policy)
        scored.append((calibration_key(metric, parameter), parameter, metric))
    scored.sort(key=lambda x: x[0])
    return scored[0][1], scored

def metrics_by_domain(traces, policy):
    out = {}
    for adapter in ADAPTERS:
        domain = adapter.DOMAIN
        out[domain] = aggregate((t for t in traces if t.domain == domain), policy)
    return out

def metric_dict(m: MetricVector):
    return {
        "PSE_live": m.pse_live,
        "PD_live": m.pd_live,
        "AE_live": m.ae_live,
        "OIW": m.oiw,
        "RL_max": m.rl_max,
        "MISSED_REOPEN": m.missed_reopen,
        "BER": m.ber,
    }

def family_metrics(traces, policy):
    out = {}
    for family in FAMILIES:
        out[family] = metric_dict(
            aggregate((t for t in traces if t.family == family), policy)
        )
    return out

def ccsr_audit(traces, policy):
    material = inert = no_stop = 0
    for trace in traces:
        actions = simulate(trace, policy)
        stop = next((i for i, a in enumerate(actions) if a == "STOP"), None)
        if stop is None:
            no_stop += 1
            continue
        end = len(trace.steps)
        for j in range(stop + 1, len(trace.steps)):
            o = trace.steps[j].obs
            if o.active_break or o.decision_change or o.upstream == "REOPEN":
                end = j
                break
        # Current-episode replay only. Novel post-stop contact starts a new clock.
        if any(trace.steps[j].gold.live_unsafe for j in range(stop, end)):
            material += 1
        else:
            inert += 1
    return {
        "material_continue": material,
        "inert_continue": inert,
        "no_stop": no_stop,
    }

def anti_leakage_audit():
    observable = set(Observable.__dataclass_fields__)
    hidden = set(HiddenGold.__dataclass_fields__)
    forbidden = {"live_unsafe", "action_wrong_if_stop"}
    src = "\n".join(
        inspect.getsource(f)
        for f in (oqsc_policy, lag_policy)
    )
    return (
        observable.isdisjoint(forbidden)
        and hidden == forbidden
        and "step.gold" not in src
        and ".gold" not in src
    )

def domain_criteria(candidate, stop_now, continue_all, fixed, patience):
    result = {}
    for domain in candidate:
        c = candidate[domain]
        sn = stop_now[domain]
        ca = continue_all[domain]
        fx = fixed[domain]
        pt = patience[domain]
        c1 = c.pse_live < sn.pse_live and c.ae_live <= min(fx.ae_live, pt.ae_live)
        c2 = c.oiw < ca.oiw
        c3 = not pareto_dominates(pt, c)
        c4 = not pareto_dominates(fx, c)
        c5 = c.rl_max <= 1 and c.missed_reopen == 0
        result[domain] = {
            "C1_premature_stop_competence": c1,
            "C2_over_inquiry_competence": c2,
            "C3_patience_not_dominating": c3,
            "C4_fixed_not_dominating": c4,
            "C5_reopening_competence": c5,
            "PASS": all((c1, c2, c3, c4, c5)),
        }
    return result

def print_metric(prefix, metric):
    d = metric_dict(metric)
    for key, value in d.items():
        print(f"{prefix}.{key}={value}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-out")
    args = ap.parse_args()

    traces = build_traces()
    discovery = [t for t in traces if t.split == "DISCOVERY"]
    calibration = [t for t in traces if t.split == "CALIBRATION"]
    holdout = [t for t in traces if t.split == "HOLDOUT"]

    expected = len(ADAPTERS) * len(FAMILIES) * sum(REPLICATES.values())
    assert len(traces) == expected
    assert len({t.trace_id for t in traces}) == len(traces)
    assert {t.domain for t in traces} == {a.DOMAIN for a in ADAPTERS}
    assert {t.family for t in traces} == set(FAMILIES)

    fixed_k, fixed_grid = select_parameter(
        calibration,
        ((k, fixed_policy(k)) for k in range(1, 13)),
    )
    patience_h, patience_grid = select_parameter(
        calibration,
        ((h, patience_policy(h)) for h in range(1, 7)),
    )
    lag_lambda, lag_grid = select_parameter(
        calibration,
        ((lam, lag_policy(lam)) for lam in range(0, 4)),
    )

    policies = {
        "RAW_OQSC": oqsc_policy,
        "CALIBRATED_OQSC": lag_policy(lag_lambda),
        "STOP_NOW": stop_now_policy,
        "CONTINUE_ALL": continue_all_policy,
        "FIXED": fixed_policy(fixed_k),
        "PATIENCE": patience_policy(patience_h),
    }

    holdout_domain = {
        name: metrics_by_domain(holdout, policy)
        for name, policy in policies.items()
    }
    holdout_total = {
        name: aggregate(holdout, policy)
        for name, policy in policies.items()
    }

    raw_criteria = domain_criteria(
        holdout_domain["RAW_OQSC"],
        holdout_domain["STOP_NOW"],
        holdout_domain["CONTINUE_ALL"],
        holdout_domain["FIXED"],
        holdout_domain["PATIENCE"],
    )
    calibrated_criteria = domain_criteria(
        holdout_domain["CALIBRATED_OQSC"],
        holdout_domain["STOP_NOW"],
        holdout_domain["CONTINUE_ALL"],
        holdout_domain["FIXED"],
        holdout_domain["PATIENCE"],
    )

    c7 = anti_leakage_audit()
    c8 = (
        all(t.seed != 0 for t in holdout)
        and all(t.split == "HOLDOUT" for t in holdout)
        and PRESEAL == "c61c9516a4e38ee1241a30ca3d09186bc58b53e8"
    )

    raw_pass = all(v["PASS"] for v in raw_criteria.values()) and c7 and c8
    calibrated_pass = (
        all(v["PASS"] for v in calibrated_criteria.values()) and c7 and c8
    )

    report = {
        "stage": "MQR-4.51",
        "preseal": PRESEAL,
        "trace_count": len(traces),
        "split_counts": {
            split: sum(t.split == split for t in traces)
            for split in REPLICATES
        },
        "domains": [a.DOMAIN for a in ADAPTERS],
        "family_count": len(FAMILIES),
        "calibration_selection": {
            "fixed_k": fixed_k,
            "patience_h": patience_h,
            "lag_lambda": lag_lambda,
            "fixed_grid": [
                {"parameter": p, "metrics": metric_dict(m)}
                for _, p, m in fixed_grid
            ],
            "patience_grid": [
                {"parameter": p, "metrics": metric_dict(m)}
                for _, p, m in patience_grid
            ],
            "lag_grid": [
                {"parameter": p, "metrics": metric_dict(m)}
                for _, p, m in lag_grid
            ],
        },
        "holdout_total": {
            name: metric_dict(m) for name, m in holdout_total.items()
        },
        "holdout_by_domain": {
            name: {d: metric_dict(m) for d, m in dm.items()}
            for name, dm in holdout_domain.items()
        },
        "holdout_by_family": {
            "RAW_OQSC": family_metrics(holdout, policies["RAW_OQSC"]),
            "CALIBRATED_OQSC": family_metrics(
                holdout, policies["CALIBRATED_OQSC"]
            ),
        },
        "criteria": {
            "RAW_OQSC": raw_criteria,
            "CALIBRATED_OQSC": calibrated_criteria,
            "C7_anti_self_scoring": c7,
            "C8_holdout_integrity": c8,
        },
        "ccsr": {
            "RAW_OQSC": ccsr_audit(holdout, policies["RAW_OQSC"]),
            "CALIBRATED_OQSC": ccsr_audit(
                holdout, policies["CALIBRATED_OQSC"]
            ),
        },
        "verdict": {
            "raw_oqsc": "PASS" if raw_pass else "FAIL",
            "calibrated_successor": "PASS" if calibrated_pass else "FAIL",
            "external_calibration": "HOLD",
            "universal_optimality": "FORBIDDEN",
        },
        "guards": {
            "primary_scalar_score": "OFF",
            "future_oracle": "FORBIDDEN",
            "post_holdout_policy_repair": "FORBIDDEN",
            "novel_post_stop_contact_charged_as_pse": "NO",
            "same_kernel_cross_domain": "YES",
        },
    }

    print(f"mqr451.trace_count={len(traces)}")
    for split, count in report["split_counts"].items():
        print(f"mqr451.split.{split}={count}")
    print("mqr451.domain_count=3")
    print(f"mqr451.family_count={len(FAMILIES)}")
    print(f"mqr451.calibration.fixed_k={fixed_k}")
    print(f"mqr451.calibration.patience_h={patience_h}")
    print(f"mqr451.calibration.lag_lambda={lag_lambda}")
    print(f"mqr451.anti_self_scoring={'PASS' if c7 else 'FAIL'}")
    print(f"mqr451.holdout_integrity={'PASS' if c8 else 'FAIL'}")
    for name in policies:
        print_metric(f"mqr451.holdout.{name}", holdout_total[name])
    for domain in [a.DOMAIN for a in ADAPTERS]:
        print(
            f"mqr451.domain.{domain}.raw={'PASS' if raw_criteria[domain]['PASS'] else 'FAIL'}"
        )
        print(
            f"mqr451.domain.{domain}.calibrated={'PASS' if calibrated_criteria[domain]['PASS'] else 'FAIL'}"
        )
    print(f"mqr451.raw_oqsc_verdict={'PASS' if raw_pass else 'FAIL'}")
    print(
        f"mqr451.calibrated_successor_verdict={'PASS' if calibrated_pass else 'FAIL'}"
    )
    print("mqr451.external_calibration=HOLD")
    print("mqr451.universal_optimality=FORBIDDEN")
    print("mqr451.primary_scalar_score=OFF")
    print("mqr451.future_oracle=FORBIDDEN")
    print("mqr451.novel_post_stop_contact_charged_as_pse=NO")
    print("mqr451.same_kernel_cross_domain=YES")
    print("MQR451_REPORT_JSON=" + json.dumps(report, sort_keys=True))

    if args.json_out:
        p = Path(args.json_out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

if __name__ == "__main__":
    main()
