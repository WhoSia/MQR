#!/usr/bin/env python3
"""MQR 4.92: verify the *active* Serov 2026 original species training data.

The paper's repository notebook comments out oxalis, while using other species.
This program cross-checks the frozen notebook and Git blobs, then profiles
original class/coordinate/year fields WITHOUT training a new model.
"""
import csv
import hashlib
import io
import json
import math
import math
from pathlib import Path
from urllib.request import Request, urlopen

ROOT="egorser0v/Importance-reweighting"
COMMIT="46c4d011c9f0cd0614c08e7edb68ac2491f659c8"
NOTEBOOK=("notebooks/datasets.ipynb","5d9dc434b2bf7d070f44501b2e97f8ce3abd9ec0",140000)
ACTIVE={
  "anemone":("0e1c83dda391229ffd3cb69573d184eebf1c7bdd",8200000),
  "caltha":("48cb935dbfb7c05c07a3919e38b26f46530f2237",7100000),
  "tussilago":("d0b5f44dea32e80a148d501b91682c941b63551b",12800000),
}
OUT=Path("mqr492-serov-active-source-data.json")

def fetch_pinned(path,expected_sha,max_bytes):
    url=f"https://raw.githubusercontent.com/{ROOT}/{COMMIT}/{path}"
    with urlopen(Request(url,headers={"User-Agent":"MQR492-independent-dataset-audit/1.0"}),timeout=50) as response:
        data=response.read(max_bytes+1)
    if len(data)>max_bytes:raise ValueError("original source bounded size exceeded")
    actual=hashlib.sha1(b"blob "+str(len(data)).encode()+bytes([0])+data).hexdigest()
    if actual!=expected_sha:raise ValueError(f"immutable source hash mismatch: {path}")
    return data

def read_notebook():
    path,sha,cap=NOTEBOOK
    data=fetch_pinned(path,sha,cap)
    obj=json.loads(data)
    content=["".join(c.get("source",[])) for c in obj["cells"] if c.get("cell_type")=="code"]
    refs=[s for s in content if "datasets_dict" in s and "../datasets/species" in s]
    if not refs:raise ValueError("original study's species entrypoint not found")
    block=refs[0]
    for name in ACTIVE:
        if not any(line.lstrip().startswith(("'"+name+"'","\""+name+"\"")) and not line.lstrip().startswith("#")
                   for line in block.splitlines()):
            raise ValueError(f"expected active original notebook species missing: {name}")
    if not any(line.lstrip().startswith("#") and "'oxalis':" in line for line in block.splitlines()):
        raise ValueError("original notebook no longer documents excluded oxalis")
    spatial=[s for s in content if "decimalLongitude" in s and "decimalLatitude" in s]
    if not spatial:raise ValueError("original axis rename code unavailable")
    return {"source_notebook":path,"notebook_git_blob_sha1":sha,
      "source_species_block":block,
      "source_axis_rename_lines":[line.strip() for s in spatial for line in s.splitlines()
                                 if "'lat': 'decimalLongitude'" in line or "'long': 'decimalLatitude'" in line][:6]}

def summarize(name):
    sha,cap=ACTIVE[name]
    path=f"datasets/species/{name}.csv"
    raw=fetch_pinned(path,sha,cap)
    stream=csv.DictReader(io.StringIO(raw.decode("utf-8-sig"),newline=""))
    cols=stream.fieldnames or []
    required={"lat","long","presence","year"}|{f"bio{i}" for i in range(1,20)}
    if not required.issubset(set(cols)):
        raise ValueError(f"missing original expected science columns: {name}")
    labels={};complete_label_hist={};complete_label_years={};year_hist={};complete_year_hist={};incomplete_year_hist={};year_bounds=[float("inf"),float("-inf")]
    lat=[float("inf"),float("-inf")];lon=[float("inf"),float("-inf")]
    missing=0;total=0
    for row in stream:
        total+=1
        label=(row.get("presence") or "").strip()
        labels[label]=labels.get(label,0)+1
        raw_year=(row.get("year") or "").strip()
        if raw_year:
            year_hist[raw_year]=year_hist.get(raw_year,0)+1
            try:
                bios=[float(row[f"bio{i}"]) for i in range(1,20)]
                is_complete=all(math.isfinite(q) for q in bios) and (label in ("0","1"))
            except (TypeError,ValueError,KeyError):
                is_complete=False
            target=complete_year_hist if is_complete else incomplete_year_hist
            target[raw_year]=target.get(raw_year,0)+1
            if is_complete:
                complete_label_hist[label]=complete_label_hist.get(label,0)+1
                annual=complete_label_years.setdefault(raw_year,{})
                annual[label]=annual.get(label,0)+1
        for key,b in (("lat",lat),("long",lon),("year",year_bounds)):
            try:
                x=float(row[key])
                if not math.isfinite(x):missing+=1;continue
                b[0]=min(b[0],x);b[1]=max(b[1],x)
            except (TypeError,ValueError):missing+=1
    if total<100:raise ValueError("unexpected tiny publisher dataset")
    return {"source_file":path,"git_blob_sha1":sha,"bytes":len(raw),
            "rows":total,"cols":len(cols),"presence_raw_counts":labels,
            "year_count_histogram":year_hist,
            "complete_bioclim_and_label_per_year":complete_year_hist,
            "complete_case_presence_counts":complete_label_hist,
            "complete_case_presence_by_year":complete_label_years,
            "incomplete_bioclim_or_label_per_year":incomplete_year_hist,
            "lat_bounds":lat,"long_bounds":lon,"year_bounds":year_bounds,
            "nonfinite_or_missing_core_cells":missing,
            "binary_labels_available":all(v in labels for v in ("0","1"))}

def main():
    notebook=read_notebook()
    entries={name:summarize(name) for name in ACTIVE}
    result={"status":"ACTIVE_SOURCE_DATA_PINS_CHECKED","study":"Serov2026",
      "repo":ROOT,"commit":COMMIT,"notebook":notebook,"datasets":entries,
      "source_scope":"original active species data inventory, NOT full published risk result replication",
      "axis_remap_flag":"Notebook converts lat into decimalLongitude and long into decimalLatitude; inspect geographic use before trusting coordinates",
      "original_oxalis_file_only_zero_labels":"Prior separately pinned oxalis.csv audit: 7507/7507 presence=0 and file commented out from active data",
      "risk_nonadmission":"CSV availability alone does not establish held-out target risk estimands"}
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf8")
    for name,z in entries.items():
        print("MQR492_ACTIVE_SOURCE_SPECIES="+json.dumps({"species":name,
           "rows":z["rows"],"presence":z["presence_raw_counts"],
           "year_bounds":z["year_bounds"],"binary_labels":z["binary_labels_available"],"year_count_histogram":z["year_count_histogram"],"complete_bioclim_and_label_per_year":z["complete_bioclim_and_label_per_year"],"complete_case_presence_counts":z["complete_case_presence_counts"],
      "complete_case_presence_by_year":z["complete_case_presence_by_year"]}))
    print("MQR492_SEROV_ACTIVE_ORIGINAL_DATA_AUDIT=PASS")

if __name__=="__main__": main()
