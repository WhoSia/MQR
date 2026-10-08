#!/usr/bin/env python3
"""MQR 4.93 Gate 0: immutable Serov original Finnish-coordinate semantics.

No target-label inspection by geographic group, no risk estimation and no model
training. Finland envelope is a *plausibility check*, not ground-truth geocoding.
Original active Anemone source is checked by Git blob before parsing.
"""
import csv
import io
import json
import math
from collections import Counter
from pathlib import Path
import numpy as np
from serov_active_source_species_audit import fetch_pinned, ACTIVE, read_notebook
from serov_author_function_replay import COMMIT

SOURCE="datasets/species/anemone.csv"
OUT=Path("mqr493-gate0-coordinate-inventory.json")
FINLAND_BOUNDS={"lat_min":59.0,"lat_max":71.5,"lon_min":19.0,"lon_max":32.5}
YEARS=(2013,2024)
FEATURE_NAMES=tuple(f"bio{i}" for i in range(1,20))

def within_finland(lat,lon):
    b=FINLAND_BOUNDS
    return b["lat_min"] <= lat <= b["lat_max"] and b["lon_min"] <= lon <= b["lon_max"]

def pct(xs,p):
    return float(np.quantile(np.asarray(xs,dtype=float),p))

def main():
    sha,limit=ACTIVE["anemone"]
    raw=fetch_pinned(SOURCE,sha,limit)
    notebook=read_notebook()  # separately pinned author notebook Git blob
    lines=notebook["source_axis_rename_lines"]
    if not any("'lat': 'decimalLongitude'" in z for z in lines) or not any("'long': 'decimalLatitude'" in z for z in lines):
        raise AssertionError("original notebook remap identity not verified")
    frame=[]
    statuses=Counter()
    for row_idx,row in enumerate(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"),newline="")),2):
        statuses["all_rows"]+=1
        try:
            year=int(float(row["year"]))
            rlat=float(row["lat"]);rlon=float(row["long"])
            if not math.isfinite(rlat) or not math.isfinite(rlon):
                raise ValueError("nonfinite coordinate")
        except (KeyError,ValueError,TypeError):
            statuses["invalid_or_nonfinite_coord_or_year"]+=1;continue
        if not YEARS[0]<=year<=YEARS[1]:
            statuses["outside_prespecified_year_range"]+=1;continue
        try:
            bios=[float(row[k]) for k in FEATURE_NAMES]
            if not all(math.isfinite(x) for x in bios):
                raise ValueError("nonfinite BIO")
        except (KeyError,ValueError,TypeError):
            statuses["missing_nonfinite_BIO"]+=1;continue
        statuses["geographic_frame_valid_year_bio_coordinates"]+=1
        frame.append((row_idx,year,rlat,rlon,row["presence"]))
    if len(frame)<100:raise AssertionError("too few pinned coordinate observations")
    raw_lats=np.array([z[2] for z in frame]);raw_longs=np.array([z[3] for z in frame])
    standard=[within_finland(a,b) for a,b in zip(raw_lats,raw_longs)]
    swapped=[within_finland(b,a) for a,b in zip(raw_lats,raw_longs)]
    standard_share=float(np.mean(standard));swapped_share=float(np.mean(swapped))
    if standard_share >= .95 and swapped_share <= .05:
        orientation="RAW_LAT_IS_PHYSICAL_LATITUDE"
        physical_lats=raw_lats;physical_lons=raw_longs
    elif swapped_share >= .95 and standard_share <= .05:
        orientation="RAW_LAT_IS_PHYSICAL_LONGITUDE"
        physical_lats=raw_longs;physical_lons=raw_lats
    else:
        orientation="AMBIGUOUS"
        physical_lats=None;physical_lons=None
    report={
        "source":"Serov et al 2026 Anemone original source; derived MQR inventory, not published-author geography validation",
        "original_repo":"egorser0v/Importance-reweighting",
        "upstream_commit":COMMIT,
        "original_source_file":SOURCE,"original_source_git_blob_sha1":sha,
        "notebook_git_blob_sha1":notebook["notebook_git_blob_sha1"],
        "upstream_notebook_renaming":lines,
        "finland_plausibility_envelope":FINLAND_BOUNDS,
        "geographic_completeness_frame":"All original records with finite 2013–2024 year, finite raw coordinates and all 19 BIO features; NOT target-label-filtered",
        "frame_counts":dict(statuses),
        "raw_lat_minmax":[float(np.min(raw_lats)),float(np.max(raw_lats))],
        "raw_long_minmax":[float(np.min(raw_longs)),float(np.max(raw_longs))],
        "raw_as_named_finland_share":standard_share,
        "raw_as_swapped_finland_share":swapped_share,
        "orientation":orientation,
        "spatial_assumptions":["Finland envelope is broad external geography constraint, not individual point independent geocoding","Original column-renaming semantics cannot alone demonstrate author model or published result error","No target labels or estimated risks were inspected by geographic group"]
    }
    if orientation != "AMBIGUOUS":
        positions=[(round(float(a),6),round(float(b),6)) for a,b in zip(physical_lats,physical_lons)]
        hist=Counter(positions)
        longitude_median=pct(physical_lons,.5)
        longitude_q75=pct(physical_lons,.75)
        west=[z for z,lon in zip(frame,physical_lons) if lon<=longitude_median]
        east=[z for z,lon in zip(frame,physical_lons) if lon>=longitude_q75]
        excluded=len(frame)-len(west)-len(east)
        source_labels=Counter(z[4] for z in west)
        report["coordinate_frame"]={
          "physical_lat_minmax":[float(np.min(physical_lats)),float(np.max(physical_lats))],
          "physical_lon_minmax":[float(np.min(physical_lons)),float(np.max(physical_lons))],
          "unique_rounded_6dp_coordinates":len(hist),
          "rows_on_repeated_positions":sum(n for n in hist.values() if n>1),
          "largest_identical_coordinate_multiplicity":max(hist.values()),
          "longitude_median":longitude_median,"longitude_q75":longitude_q75,
          "candidate_west_source_rows":len(west),
          "candidate_east_target_rows_unlabeled":len(east),
          "candidate_middle_buffer_rows":excluded,
          "strict_longitude_gap_degrees":max(0.,longitude_q75-longitude_median),
          "west_source_labels_counts_ONLY":dict(source_labels),
          "source_binary_feasible":source_labels["0"]>=64 and source_labels["1"]>=64,
          "target_labels_inspected":False
        }
        if not report["coordinate_frame"]["source_binary_feasible"] or len(east)<64 or len(west)<576 or longitude_q75<=longitude_median:
            report["state"]="SPATIAL_HOLDOUT_INFEASIBLE"
        else:
            report["state"]="SOURCE_COORDINATE_SEMANTICS_PLAUSIBLE_PASS_WITH_NOTEBOOK_REMAP_FLAG"
    else:
        report["state"]="COORDINATE_SEMANTICS_HOLD"
    OUT.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print("MQR493_GATE0_SUMMARY="+json.dumps({k:report[k] for k in ["orientation","raw_as_named_finland_share","raw_as_swapped_finland_share","raw_lat_minmax","raw_long_minmax","state"]},sort_keys=True))
    if "coordinate_frame" in report:
        print("MQR493_GATE0_SPATIAL_FRAME="+json.dumps(report["coordinate_frame"],sort_keys=True))
    print("MQR493_GATE0_STATUS="+report["state"])

if __name__=="__main__":main()
