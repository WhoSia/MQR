from __future__ import annotations
import json
from dataclasses import asdict
from pathlib import Path
from naturalistic_cases import CASES, PRIMARY_COUNT, SENSITIVITY_CASES, REJECTED_CASES

PRESEAL = "1602d39612374a26969d4f7c1498905eb134841e"
POOL_FREEZE = "6a54dfff94ae5007dcb37c85b19ba6980e44eabc"

AUTHORITATIVE_MAPPING = {"EXACT", "BOUNDED"}

def policy_stop(case, lag: int):
    streak = 0
    for i, cp in enumerate(case.checkpoints):
        if cp.eligible is True:
            streak += 1
            if streak >= lag + 1:
                return i
        else:
            streak = 0
    return None

def score(case, stop_index):
    if case.stop_window is None or stop_index is None:
        if case.stop_window is None:
            return "INDETERMINATE"
        return "NO_STOP_WITHIN_EPISODE"
    lo, hi = case.stop_window
    if stop_index < lo:
        return "N_PSE"
    if stop_index > hi:
        return "N_OIW"
    return "WITHIN_WINDOW"

def case_transportable(case):
    # Primary timing comparison requires load-bearing checkpoints through the
    # identified stop window to be exact/bounded rather than proxy/unknown.
    if case.stop_window is None:
        return False
    hi = case.stop_window[1]
    return all(cp.mapping in AUTHORITATIVE_MAPPING for cp in case.checkpoints[:hi+1])

def duplicate_first_eligible_lag_one(case):
    first = next((i for i,c in enumerate(case.checkpoints) if c.eligible is True), None)
    if first is None:
        return None
    # Inserting an observationally inert duplicate immediately after the first
    # eligible checkpoint changes the event-count lag-1 stopping index to the
    # duplicate, without changing world state.
    return first + 1

def natural_lag_one(case):
    return policy_stop(case, 1)

def granularity_sensitive(case):
    dup = duplicate_first_eligible_lag_one(case)
    natural = natural_lag_one(case)
    if dup is None:
        return None
    # If the natural trace's second eligible report occurs at a different
    # checkpoint (or not at all), the same world-state path yields a different
    # lag-1 decision under inert checkpoint refinement.
    return natural != dup

def main():
    rows=[]
    for case in CASES:
        raw=policy_stop(case,0)
        lag=policy_stop(case,1)
        rows.append({
            "case_id":case.case_id,
            "domain":case.domain,
            "target":case.target,
            "projection":case.projection,
            "window_kind":case.window_kind,
            "stop_window":case.stop_window,
            "transportable":case_transportable(case),
            "raw_stop_index":raw,
            "lag1_stop_index":lag,
            "raw_score":score(case,raw),
            "lag1_score":score(case,lag),
            "granularity_sensitive":granularity_sensitive(case),
            "mapping_counts":{
                g:sum(cp.mapping==g for cp in case.checkpoints)
                for g in ("EXACT","BOUNDED","PROXY","UNKNOWN")
            },
            "historical_modes":sorted({cp.mode for cp in case.checkpoints}),
        })

    transportable=[r for r in rows if r["transportable"]]
    gs=[r for r in rows if r["granularity_sensitive"] is not None]
    report={
        "stage":"MQR-4.52",
        "preseal":PRESEAL,
        "candidate_pool_freeze":POOL_FREEZE,
        "primary_cases":PRIMARY_COUNT,
        "sensitivity_cases":len(SENSITIVITY_CASES),
        "rejected_cases":len(REJECTED_CASES),
        "transportable_primary_cases":len(transportable),
        "multi_mode_cases":sum(r["projection"]!="UNIQUE" for r in rows),
        "identified_or_bounded_windows":sum(r["stop_window"] is not None for r in rows),
        "right_or_contract_censored":sum(r["stop_window"] is None for r in rows),
        "raw":{
            "within_window":sum(r["raw_score"]=="WITHIN_WINDOW" for r in rows),
            "definite_premature":sum(r["raw_score"]=="N_PSE" for r in rows),
            "definite_over_inquiry":sum(r["raw_score"]=="N_OIW" for r in rows),
            "indeterminate":sum(r["raw_score"]=="INDETERMINATE" for r in rows),
        },
        "lag1":{
            "within_window":sum(r["lag1_score"]=="WITHIN_WINDOW" for r in rows),
            "definite_premature":sum(r["lag1_score"]=="N_PSE" for r in rows),
            "definite_over_inquiry":sum(r["lag1_score"]=="N_OIW" for r in rows),
            "indeterminate":sum(r["lag1_score"]=="INDETERMINATE" for r in rows),
        },
        "granularity":{
            "eligible_cases":len(gs),
            "sensitive_cases":sum(r["granularity_sensitive"] is True for r in gs),
            "invariant_cases":sum(r["granularity_sensitive"] is False for r in gs),
            "fixed_event_count_transport":"REJECT",
        },
        "verdict":{
            "v18_claim_freeze_timing_partial_transport":"SUPPORTED_WITHOUT_DEFINITE_ERROR_ON_IDENTIFIED_WINDOWS",
            "v18_binary_naturalistic_ontology":"FAIL",
            "lag1_external_calibration":"NOT_ESTABLISHED",
            "realtrace_v019_revision":"EARNED",
            "prospective_external_validation":"NOT_CLAIMED",
        },
        "guards":{
            "naturalistic_retuning_lambda":"NO",
            "lambda_used":1,
            "historical_action_is_gold":"NO",
            "unique_gold_stop_time_inferred":"NO",
            "primary_scalar_score":"OFF",
            "popperian_master_semantics":"REJECT",
        },
        "cases":rows,
    }

    assert report["primary_cases"]==7
    assert report["sensitivity_cases"]==1
    assert report["rejected_cases"]==1
    assert report["transportable_primary_cases"]==5
    assert report["multi_mode_cases"]==6
    assert report["identified_or_bounded_windows"]==5
    assert report["right_or_contract_censored"]==2
    assert report["raw"]["within_window"]==5
    assert report["lag1"]["within_window"]==5
    assert report["raw"]["definite_premature"]==0
    assert report["lag1"]["definite_premature"]==0
    assert report["granularity"]["eligible_cases"]==6
    assert report["granularity"]["sensitive_cases"]==6

    print(f"mqr452.primary_cases={report['primary_cases']}")
    print(f"mqr452.sensitivity_cases={report['sensitivity_cases']}")
    print(f"mqr452.rejected_cases={report['rejected_cases']}")
    print(f"mqr452.transportable_primary_cases={report['transportable_primary_cases']}")
    print(f"mqr452.multi_mode_cases={report['multi_mode_cases']}")
    print(f"mqr452.identified_windows={report['identified_or_bounded_windows']}")
    print(f"mqr452.raw.within_window={report['raw']['within_window']}")
    print(f"mqr452.lag1.within_window={report['lag1']['within_window']}")
    print(f"mqr452.raw.definite_premature={report['raw']['definite_premature']}")
    print(f"mqr452.lag1.definite_premature={report['lag1']['definite_premature']}")
    print(f"mqr452.granularity.eligible_cases={report['granularity']['eligible_cases']}")
    print(f"mqr452.granularity.sensitive_cases={report['granularity']['sensitive_cases']}")
    print("mqr452.v18_binary_naturalistic_ontology=FAIL")
    print("mqr452.lag1_external_calibration=NOT_ESTABLISHED")
    print("mqr452.realtrace_v019_revision=EARNED")
    print("mqr452.popperian_master_semantics=REJECT")
    print("MQR452_REPORT_JSON="+json.dumps(report,sort_keys=True))

    Path("experiments/mqr-4.52/results").mkdir(parents=True,exist_ok=True)
    Path("experiments/mqr-4.52/results/naturalistic_report.json").write_text(
        json.dumps(report,indent=2,sort_keys=True),encoding="utf-8"
    )

if __name__=="__main__":
    main()
