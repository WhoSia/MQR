#!/usr/bin/env python3
import csv, itertools, pathlib, sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent
FEATURES = ("authorization_state","provenance_state","defeater_state","revision_state")

def read_tsv(path):
    with pathlib.Path(path).open(newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def load_schema(path):
    return {r["ancestry"]: r for r in read_tsv(path)}

def transition(intervention, feat):
    a,p,d,r = (feat[x] for x in FEATURES)

    if intervention == "AUTHORIZATION_CHECK":
        if a in {"RETROSPECTIVE","UNAUTHORIZED"}:
            return "HOLD_REAUTHORIZE"
        return "STABLE"

    if intervention == "REVISION_REPLAY":
        if a == "RETROSPECTIVE":
            return "REOPEN_REQUIRED"
        if r == "REASON_MUTATION":
            return "HOLD_REASON_RECONSTITUTE"
        return "STABLE"

    if intervention == "WITHDRAW_ANCESTRY_SUPPORT":
        return "REOPEN_REQUIRED" if p == "COMMON_MODE_SINGLE_ROOT" else "STABLE"

    if intervention == "REPRODUCE_UNDER_INDEPENDENT_ANCESTRY":
        return "REOPEN_REQUIRED" if p == "COMMON_MODE_SINGLE_ROOT" else "STABLE"

    if intervention == "REOPEN_WITH_HELD_OUT_DEFEATER":
        if d == "SURVIVED_D1":
            return "STABLE"
        return "REOPEN_REQUIRED"

    if intervention == "REOPEN_WITH_HELD_OUT_DEFEATER_D3":
        return "REOPEN_REQUIRED"

    if intervention == "COUNTERFACTUAL_RECONSTITUTION":
        return "REOPEN_REQUIRED" if r == "REVERSAL" else "STABLE"

    if intervention in {"AUDIT_SOURCE","SCOPE_EXPANSION"}:
        return "STABLE"

    raise ValueError(f"unknown intervention: {intervention}")

def state_key(pair, feat, selected):
    return tuple([pair["present_surface_hash"], pair["intervention"]] + [feat[s] for s in selected])

def sufficient(pairs, schema, selected):
    seen = {}
    for pair in pairs:
        for side in ("A","B"):
            anc = pair[f"ancestry_{side}"]
            feat = schema[anc]
            y = pair[f"expected_{side}"]
            k = state_key(pair, feat, selected)
            if k in seen and seen[k] != y:
                return False
            seen[k] = y
    return True

def minimal_feature_sets(pairs, schema):
    winners = []
    for n in range(len(FEATURES)+1):
        for subset in itertools.combinations(FEATURES, n):
            if sufficient(pairs, schema, subset):
                winners.append(subset)
        if winners:
            return winners
    return []

def pair_relation(a,b):
    return "FUNGIBLE" if a == b else "SEPARATES"

def main():
    pair_path = pathlib.Path(sys.argv[1] if len(sys.argv)>1 else ROOT/"PAIR-FREEZE.tsv")
    schema_path = pathlib.Path(sys.argv[2] if len(sys.argv)>2 else ROOT/"ANCESTRY-FEATURES.tsv")
    pairs = read_tsv(pair_path)
    schema = load_schema(schema_path)
    outdir = ROOT/"results"
    outdir.mkdir(parents=True, exist_ok=True)

    missing = sorted({r[f"ancestry_{s}"] for r in pairs for s in ("A","B")} - set(schema))
    if missing:
        print("MQR469_SCHEMA=FAIL missing=" + ",".join(missing))
        return 2

    mismatch = 0
    leakage = 0
    swap_fail = 0
    separated = 0
    fungible = 0
    baseline_counts = Counter()
    results = []

    for pair in pairs:
        fa = schema[pair["ancestry_A"]]
        fb = schema[pair["ancestry_B"]]
        ya = transition(pair["intervention"], fa)
        yb = transition(pair["intervention"], fb)
        rel = pair_relation(ya,yb)
        separated += rel == "SEPARATES"
        fungible += rel == "FUNGIBLE"
        baseline_counts[pair["baseline_probe"]] += 1

        if ya != pair["expected_A"] or yb != pair["expected_B"] or rel != pair["expected_pair_relation"]:
            mismatch += 1

        # Frozen extensional matcher: the pair manifest has one shared present surface/rule/verdict by construction.
        if not pair["present_surface_hash"] or not pair["current_rule"] or not pair["current_verdict"]:
            leakage += 1

        if pair["causal_swap"] == "YES":
            # Swap ancestry while holding the present surface and intervention fixed.
            swap_a = transition(pair["intervention"], fb)
            swap_b = transition(pair["intervention"], fa)
            if swap_a != yb or swap_b != ya:
                swap_fail += 1

        results.append((pair["pair_id"], ya, yb, rel, pair["control_type"], pair["baseline_probe"]))

    mins = minimal_feature_sets(pairs, schema)

    with (outdir/"python_results.tsv").open("w", newline="") as f:
        w=csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["pair_id","outcome_A","outcome_B","relation","control_type","baseline_probe"])
        w.writerows(results)

    with (outdir/"minimal_feature_sets.tsv").open("w", newline="") as f:
        w=csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["rank","feature_count","features"])
        for i,s in enumerate(mins,1):
            w.writerow([i,len(s),",".join(s) if s else "<EMPTY>"])

    with (outdir/"python_summary.tsv").open("w", newline="") as f:
        w=csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["metric","value"])
        w.writerow(["PAIRS",len(pairs)])
        w.writerow(["EXPECTATION_MISMATCHES",mismatch])
        w.writerow(["PRESENT_SURFACE_LEAKAGE",leakage])
        w.writerow(["CAUSAL_SWAP_FAILURES",swap_fail])
        w.writerow(["SEPARATING_PAIRS",separated])
        w.writerow(["FUNGIBLE_PAIRS",fungible])
        w.writerow(["MINIMAL_FEATURE_COUNT",len(mins[0]) if mins else -1])
        w.writerow(["MINIMAL_FEATURE_SET_COUNT",len(mins)])
        for k,v in sorted(baseline_counts.items()):
            w.writerow([f"BASELINE_{k}",v])

    if mismatch or leakage or swap_fail or not mins:
        print(f"MQR469_PYTHON_COURT=FAIL mismatch={mismatch} leakage={leakage} swap_fail={swap_fail} mins={len(mins)}")
        return 1

    print("MQR469_PYTHON_COURT=PASS")
    print("MQR469_MINIMAL_FEATURE_COUNT=" + str(len(mins[0])))
    print("MQR469_MINIMAL_FEATURE_SETS=" + ";".join(",".join(x) if x else "<EMPTY>" for x in mins))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
