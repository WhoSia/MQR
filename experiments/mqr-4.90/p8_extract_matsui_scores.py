#!/usr/bin/env python3
"""Extract a PINNED publicly published paired score stream for Rust's AUC court.

For first independent evidence repair we intentionally use only the
native-only Oxalis latifolia America-to-Oceania model. Source is
Matsui 2026, Zenodo 19970795, MD5 pinned in p8_source_probe.py.
No statistical bootstrap, no re-fitting, and no cross-design pooling.
"""
from pathlib import Path
from hashlib import sha256
import csv
import io
import json
import os
import sys
import zipfile
from p8_source_probe import ARTIFACT_DIR, download

BASE = "3_Maxent_predictions/2_Maxent_values"
CASE = "Oxalis_latifolia_America-Oceania.csv"


def select_entry(z, folder: str, name: str):
    group = [
        x for x in z.infolist()
        if x.filename.startswith(f"{BASE}/{folder}/")
        and x.filename.lower().endswith(".csv")
    ]
    candidate = [x for x in group if x.filename.rsplit("/", 1)[-1] == name]
    if not candidate:
        # The README only says an extra "2" is appended to avoid collision;
        # original archive filenames may vary in separators. Match exactly
        # one semantically pinned calibration→target stem, NEVER a different
        # species/target or an ambiguous source.
        key = Path(name).stem.removesuffix("2").lower().replace("_", "").replace("-", "")
        candidate = [
            x for x in group
            if Path(x.filename).stem.lower().replace("_", "").replace("-", "").startswith(key)
        ]
    if len(candidate) != 1:
        nearby = [x.filename for x in group if "Oxalis_latifolia_America" in x.filename][:30]
        raise RuntimeError(
            f"cannot identify unique {folder}/{name}: matches={len(candidate)}, "
            f"nearby={nearby}"
        )
    return candidate[0]


def read_scores(z, member, label):
    with z.open(member) as f:
        txt = io.TextIOWrapper(f, encoding="utf-8-sig", newline="")
        reader = csv.DictReader(txt)
        fields = set(reader.fieldnames or [])
        if "SAMPLE_1" not in fields:
            raise RuntimeError(f"missing Maxent cloglog score column {member.filename}: {fields}")
        values = []
        for row in reader:
            score = float(row["SAMPLE_1"])
            if not (0 <= score <= 1):
                raise RuntimeError("score outside cloglog [0,1], likely source mismatch")
            values.append((label, score))
    if not values:
        raise RuntimeError(f"empty target score set {member.filename}")
    return values


def main():
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    raw = ARTIFACT_DIR / "source-temporary.zip"
    receipt = download(raw)
    with zipfile.ZipFile(raw) as z:
        yes = select_entry(z, "1_Maxent_values_for_presence_cells", CASE)
        # README says an extra 2 is appended to absence-cell filenames.
        no = select_entry(z, "2_Maxent_values_for_absence_cells", "Oxalis_latifolia_America-Oceania2.csv")
        positives = read_scores(z, yes, 1)
        negatives = read_scores(z, no, 0)
        scores = ARTIFACT_DIR / "oxalis-america-oceania-reference-scores.csv"
        with scores.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(("label", "score"))
            writer.writerows(positives)
            writer.writerows(negatives)
        if scores.stat().st_size > 12_000_000:
            raise RuntimeError("selected raw score receipt too large for bounded artifact")
        provenance = {
            "upstream_doi": "10.5281/zenodo.19970795",
            "upstream_md5": receipt["md5"],
            "upstream_sha256": receipt["sha256"],
            "case": "Oxalis latifolia | calibration America | target Oceania",
            "reported_AUC_table_A1": 0.53,
            "presence_score_member": yes.filename,
            "absence_score_member": no.filename,
            "presence_records": len(positives),
            "absence_reference_cell_records": len(negatives),
            "score_stream_sha256": sha256(scores.read_bytes()).hexdigest(),
            "status": "EXTRACTED_NOT_YET_ADMITTED",
            "limitations": [
                "reference negatives are cells lacking recorded presence",
                "no matched CV background-negative distribution available in this stream",
                "do not infer causal spatial CV optimism"
            ],
        }
    raw.unlink()
    (ARTIFACT_DIR / "oxalis-provenance.json").write_text(
        json.dumps(provenance, indent=2), encoding="utf-8"
    )
    print("MQR490_P8_PRESENCE_COUNT=" + str(len(positives)))
    print("MQR490_P8_REFERENCE_NEGATIVE_COUNT=" + str(len(negatives)))
    print("MQR490_P8_SCORE_STREAM_SHA256=" + provenance["score_stream_sha256"])
    print("MQR490_P8_SCORE_EXTRACTION=PASS")


if __name__ == "__main__":
    main()
