"""MQR: original FinBIF first-observation/fortnightly-monitoring coherence.
Actual 2024 GBIF ZIP contains 2013–2024 records; 2024 denotes archive year.
The first sighting timestamp and each positive weekend interval are
different observation modes, not independent fixed-site occupancy visits.
"""
from __future__ import annotations
import csv, hashlib, json, sys, zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

SHA = "5376aac7f12f981299bf0b4a964a4f6c453f501eb1b8ce29df1ce59f90b7b836"
SOURCE = "acf9b46d-e71a-4ccb-91d2-a021ffda4dd4"

def audit(filename):
    p = Path(filename)
    if hashlib.sha256(p.read_bytes()).hexdigest() != SHA:
        raise ValueError("wrong historical ZIP source")
    groups = defaultdict(list)
    with zipfile.ZipFile(p) as z:
        if z.namelist() != ["0031144-240626123714530.csv"]:
            raise ValueError("unrecognized original member")
        with z.open(z.namelist()[0]) as file:
            lines = (line.decode("utf-8-sig") for line in file)
            records = csv.DictReader(lines, delimiter="\t")
            total = 0
            for row in records:
                total += 1
                if row["datasetKey"] == SOURCE:
                    doc = row["catalogNumber"]
                    if not doc or row["occurrenceID"].split("#")[0] != doc:
                        raise ValueError("inconsistent document/record ancestry")
                    groups[doc].append(row)
    if total != 29543 or len(groups) != 2272 or sum(map(len, groups.values())) != 14651:
        raise ValueError("unexpected sample/data ancestry")
    counts, by_year = Counter(), defaultdict(Counter)
    for rows in groups.values():
        years = {r["year"] for r in rows}
        if len(years) != 1: raise ValueError("mixed document observation years")
        year = years.pop()
        first = [r for r in rows if "/" not in r["eventDate"] and r["occurrenceStatus"] == "PRESENT"]
        periods = [r for r in rows if "/" in r["eventDate"] and r["occurrenceStatus"] == "PRESENT"]
        if len(first)>1: raise ValueError("multiple first-positive instants")
        if first and periods:
            first_day = date.fromisoformat(first[0]["eventDate"][:10])
            bounds = [(date.fromisoformat(r["eventDate"].split("/")[0][:10]),
                       date.fromisoformat(r["eventDate"].split("/")[1][:10])) for r in periods]
            if first_day < min(x[0] for x in bounds):
                category = "first_before_all_positive_weekends"
            elif first_day > max(x[1] for x in bounds):
                category = "first_after_all_positive_weekends"
            elif any(a <= first_day <= b for a,b in bounds):
                category = "first_within_a_positive_weekend"
            else:
                category = "first_between_positive_weekends"
        elif first:
            category = "first_timestamp_no_positive_weekend"
        elif periods:
            category = "positive_weekend_without_first_timestamp"
        else:
            category = "neither_positive_mode"
        counts[category] += 1
        by_year[year][category] += 1
    if sum(counts.values()) != 2272:
        raise AssertionError("document partition lost")
    EXPECTED = {
      "first_timestamp_no_positive_weekend":1178,
      "first_before_all_positive_weekends":478,
      "first_within_a_positive_weekend":217,
      "positive_weekend_without_first_timestamp":391,
      "neither_positive_mode":8
    }
    if dict(counts) != EXPECTED:
        raise AssertionError("results drifted from historically pinned source")
    if counts["first_after_all_positive_weekends"] or counts["first_between_positive_weekends"]:
        raise AssertionError("temporal semantics contradictory")
    return {"status":"PASS_HISTORICAL_SOURCE_PINNED",
            "source_rows":14651,
            "document_ids":2272,
            "document_mode_relationship":dict(sorted(counts.items())),
            "year_2024":dict(sorted(by_year["2024"].items())),
            "observation_years":sorted(by_year),
            "same_fixed_site_revisit_authenticated":False,
            "observation_effort_authenticated":False,
            "scientific_novelty_proven":False}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python finbif_mode_coherence.py original-2024.zip")
    print(json.dumps(audit(sys.argv[1]), ensure_ascii=False, sort_keys=True, indent=2))
