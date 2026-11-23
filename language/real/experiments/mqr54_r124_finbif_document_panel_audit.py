"""MQR 5.4 R124: audit FinBIF Document IDs in the pinned original GBIF ZIP.

This reconstructs *form-level observation slots*, not certified fixed-site
visits, survey effort, or population occupancy. No observer/coordinate data
are printed. All original source roots and counts are pinned.
"""
from __future__ import annotations
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import sys
import zipfile

SHA256 = "5376aac7f12f981299bf0b4a964a4f6c453f501eb1b8ce29df1ce59f90b7b836"
SPRING = "acf9b46d-e71a-4ccb-91d2-a021ffda4dd4"


def audit(path: str) -> dict:
    p = Path(path)
    if hashlib.sha256(p.read_bytes()).hexdigest() != SHA256:
        raise ValueError("Not the pinned 2024 GBIF original ZIP")
    with zipfile.ZipFile(p) as z:
        names = z.namelist()
        if names != ["0031144-240626123714530.csv"]:
            raise ValueError("Unexpected original ZIP members")
        with z.open(names[0]) as raw:
            table = csv.DictReader((b.decode("utf-8-sig") for b in raw), delimiter="\t")
            needed = {"gbifID", "datasetKey", "catalogNumber", "occurrenceID",
                      "eventDate", "occurrenceStatus", "year", "decimalLatitude",
                      "decimalLongitude", "coordinateUncertaintyInMeters"}
            if not needed <= set(table.fieldnames or []):
                raise ValueError("Original source columns missing")
            groups = defaultdict(list)
            total = 0
            for row in table:
                total += 1
                if row["datasetKey"] != SPRING:
                    continue
                document = row["catalogNumber"]
                if not document or row["occurrenceID"].split("#", 1)[0] != document:
                    raise ValueError("Document and record URI do not agree")
                if row["occurrenceStatus"] not in ("PRESENT", "ABSENT"):
                    raise ValueError("Unknown status")
                groups[document].append(row)
    if total != 29543 or sum(len(v) for v in groups.values()) != 14651:
        raise ValueError("Original row counts mismatch")
    if len(groups) != 2272:
        raise ValueError("Unexpected Document ID count")
    doc_metrics = Counter()
    years = defaultdict(lambda: Counter())
    uncertainty = Counter()
    size = Counter()
    weekends = defaultdict(Counter)
    for rows in groups.values():
        yr = {r["year"] for r in rows}
        coords = {(r["decimalLatitude"], r["decimalLongitude"]) for r in rows}
        if len(yr) != 1 or len(coords) != 1:
            raise ValueError("Unexpected cross-year or within-document coordinate change")
        year = next(iter(yr))
        dates = {r["eventDate"] for r in rows}
        labels = {r["occurrenceStatus"] for r in rows}
        first = sum("/" not in r["eventDate"] and r["occurrenceStatus"] == "PRESENT" for r in rows)
        if first > 1:
            raise ValueError("Multiple non-interval positive records in a document")
        doc_metrics["multiple_date"] += len(dates) > 1
        doc_metrics["mixed_status"] += len(labels) > 1
        doc_metrics["first_sighting_timestamp_present"] += first == 1
        doc_metrics["no_first_sighting_timestamp_present"] += first == 0
        size[len(rows)] += 1
        uncertainty[str(int(float(rows[0]["coordinateUncertaintyInMeters"])))]+=1
        years[year]["documents"] += 1
        years[year]["rows"] += len(rows)
        for r in rows:
            if year == "2024" and "/" in r["eventDate"]:
                weekends[r["eventDate"]][r["occurrenceStatus"]] += 1
    expected_weekends = [131, 130, 130, 130, 128, 111, 77, 29]
    actual = [sum(v.values()) for _, v in sorted(weekends.items())]
    if actual != expected_weekends:
        raise ValueError(f"2024 scheduled period totals diverge actual={actual} expected={expected_weekends} keys={list(sorted(weekends))}")
    if doc_metrics["multiple_date"] != 2269 or doc_metrics["mixed_status"] != 2260:
        raise ValueError("Pinned original document statistics changed")
    return {
        "status": "PASS_SHA_PINNED_DOCUMENT_HIERARCHY_AUDIT",
        "all_original_rows": total,
        "spring_original_rows": 14651,
        "finbif_document_ids": len(groups),
        "documents_multiple_eventDate_values": doc_metrics["multiple_date"],
        "documents_mixed_recorded_labels": doc_metrics["mixed_status"],
        "documents_one_noninterval_positive": doc_metrics["first_sighting_timestamp_present"],
        "documents_without_noninterval_positive": doc_metrics["no_first_sighting_timestamp_present"],
        "document_size_counts": {str(k):v for k,v in sorted(size.items())},
        "coordinate_uncertainty_meters_by_document": dict(sorted(uncertainty.items(), key=lambda kv:int(kv[0]))),
        "yearly_document_and_row_counts": {str(k):dict(v) for k,v in sorted(years.items())},
        "year_2024_scheduled_weekend_slots": [
            {"date_range": k, "ABSENT": v["ABSENT"], "PRESENT": v["PRESENT"]}
            for k,v in sorted(weekends.items())],
        "actual_fixed_site_revisits_certified": None,
        "eventID_column_available": False,
        "source_first_hand_analysis": True,
        "semantic_limit": "FinBIF Document ID is not a fixed-site visit ID. A campaign form may span a municipality and scheduled but unvisited observation weekends."
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python mqr54_r124_finbif_document_panel_audit.py GBIF-2024-0031144.zip")
    print(json.dumps(audit(sys.argv[1]), sort_keys=True, indent=2, ensure_ascii=False))
