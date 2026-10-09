#!/usr/bin/env python3
"""MQR-4.100 P3: *retrospective exploratory* audit of truly row-paired field measurements.
Original combined csv is previously published; no independent instrument or novelty asserted.
Only Python standard library. Native original bytes never overwritten.
"""
import csv
import hashlib
import json
import math
import pathlib
import random
import sys
from collections import Counter

SOURCE_GIT_BLOB = "ba99fbd527f0bb983b3d9615ef5c81a5917ab7d9"
SOURCE_COMMIT = "8957207b78d6ccd1b4654a9dd9c9041b657478ab"
FIELDS = ("studyName", "Species", "Individual ID", "Sample Number",
          "Culmen Length (mm)", "Flipper Length (mm)")
def blob_hash(raw):
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()
def complete(r):
    return all(r[k] not in ("", "NA") for k in FIELDS[-2:])
def mean(xs):
    return sum(xs) / len(xs)
def quantile_sorted(xs, p):
    a = (len(xs) - 1) * p
    lo = int(a)
    hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (a - lo)
def evaluate(rows):
    paired = [r for r in rows if complete(r)]
    assert len(rows) == 344 and len(paired) == 342
    assert len({(r["studyName"], r["Individual ID"]) for r in rows}) == len(rows)
    assert len({(r["studyName"], r["Sample Number"]) for r in rows}) == 220
    train = [r for r in paired if r["studyName"] in ("PAL0708", "PAL0809")]
    test = [r for r in paired if r["studyName"] == "PAL0910"]
    assert len(train) == 223 and len(test) == 119
    labels = sorted({r["Species"] for r in train})
    assert {r["Species"] for r in test} == set(labels) and len(labels) == 3
    cols = FIELDS[-2:]
    pooled_sd = []
    for col in cols:
        v = [float(r[col]) for r in train]
        mu = mean(v)
        sd = math.sqrt(mean([(x - mu) ** 2 for x in v]))
        assert sd > 0
        pooled_sd.append(sd)
    centroids = {c: [mean([float(r[col]) for r in train if r["Species"] == c])
                     for col in cols] for c in labels}
    def predict(row, use_flipper=True):
        return min(labels,
                   key=lambda c: (sum(((float(row[col]) - centroids[c][i]) / pooled_sd[i])**2
                                   for i, col in enumerate(cols) if use_flipper or i == 0), c))
    old = [predict(r, False) for r in test]
    joint = [predict(r, True) for r in test]
    actual = [r["Species"] for r in test]
    a = [int(p == y) for p, y in zip(old, actual)]
    b = [int(p == y) for p, y in zip(joint, actual)]
    difference = [v - u for u, v in zip(a, b)]
    assert (sum(a),sum(b), difference.count(1), difference.count(-1)) == (83,113,32,2)
    seed = 4100
    rng = random.Random(seed)
    boot = sorted(mean([difference[rng.randrange(len(difference))] for _ in test])
                  for _ in range(2000))
    seen = {r["Individual ID"] for r in train}
    repeat = [i for i,r in enumerate(test) if r["Individual ID"] in seen]
    unseen = [i for i,r in enumerate(test) if r["Individual ID"] not in seen]
    assert len(repeat) == 75 and len(unseen) == 44
    def subset(indices):
        return {"n":len(indices), "bill_correct":sum(a[i] for i in indices),
                "paired_correct":sum(b[i] for i in indices),
                "net_gain":sum(difference[i] for i in indices),
                "by_species":dict(Counter(actual[i] for i in indices))}
    # Deterministic within-year cyclic reassignment destroys row pairing, retaining
    # the marginal distribution of flipper length. NOT a causal instrument control.
    shams = []
    for i,r in enumerate(test):
        x = dict(r)
        x["Flipper Length (mm)"] = test[(i+17) % len(test)]["Flipper Length (mm)"]
        shams.append(x)
    sham_correct = sum(predict(r, True) == y for r,y in zip(shams,actual))
    return {
        "original_source_commit":SOURCE_COMMIT, "original_git_blob":SOURCE_GIT_BLOB,
        "evidence_role":"real same-record paired morphometrics, ONE reused field study; not two independent sensors",
        "disclosure":"retrospective exploratory on widely published data; outcomes inspected during design; no blind preregistration",
        "all_rows":len(rows), "paired_rows":len(paired), "source_rows_with_missing_pair":2,
        "source_studyName_plus_sampleNumber_duplicates":124,
        "source_studyName_plus_individualId_duplicates":0,
        "raw_individualId_duplicates":len(rows) - len({r["Individual ID"] for r in rows}),
        "year_counts_all":dict(Counter(r["studyName"] for r in rows)),
        "year_counts_complete_pair":dict(Counter(r["studyName"] for r in paired)),
        "training_years":["PAL0708","PAL0809"],"test_year":"PAL0910",
        "training_n":len(train),"test_n":len(test),"classes":labels,
        "model":"single or 2-feature nearest class centroid, training-pooled population SD, no library and no fitting to 2009 labels",
        "bill_only_correct":sum(a), "paired_bill_flipper_correct":sum(b),
        "pair_gain_count":difference.count(1),"pair_loss_count":difference.count(-1),
        "delta_accuracy":mean(difference),
        "retrospective_row_bootstrap_delta_95pct":[quantile_sorted(boot,0.025),quantile_sorted(boot,0.975)],
        "bootstrap_seed":seed,"bootstrap_resamples":len(boot),
        "nonoverlap_raw_id_string":subset(unseen),
        "repeat_raw_id_string":subset(repeat),
        "sham_rotation":17,"sham_year_marginal_preserved_correct":sham_correct,
        "scientific_limit":"Year split shares original sampling program and potentially repeated identifier strings; row bootstrap ignores clustering; label-specific composition shifts; NO target-population generalization, identifiable theta-kernel or Le Cam epsilon estimate"
    }

def main():
    if len(sys.argv)!=3:
        raise SystemExit("Usage: python3 p3_paired_original.py ORIGINAL_CSV RECEIPT_JSON")
    data = pathlib.Path(sys.argv[1]).read_bytes()
    assert blob_hash(data)==SOURCE_GIT_BLOB, "Not the pinned original author bundle byte sequence"
    text = data.decode("utf-8-sig")
    rows=list(csv.DictReader(text.splitlines()))
    assert len(rows)==344 and rows[0].keys() >= set(FIELDS)
    assert all(None not in r for r in rows), "Malformed quoted-source CSV"
    receipt=evaluate(rows)
    receipt["original_byte_count"]=len(data)
    receipt["original_sha256"]=hashlib.sha256(data).hexdigest()
    path=pathlib.Path(sys.argv[2])
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(receipt,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print(json.dumps(receipt,sort_keys=True,ensure_ascii=False))
    print("MQR4100_P3_SOURCE_INDEXED_PAIRS=LOCAL_ACCOUNTING_PASS;EXTERNAL_TRANSPORT=HOLD")
if __name__=="__main__":
    main()
