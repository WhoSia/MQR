"""MQR 5.4 R112 — GBIF original-ZIP event metadata screen.

Input: downloaded original occurrence ZIP or single tab-separated CSV.
An eventID is an event, not a verified repeated visit. No inference from
identical coordinates/years. Candidate site IDs require explicit site/event,
dated independent occasions, same protocol and nonblank effort metadata.
Output contains only counts and field coverage; biological inference HOLD.
"""
from __future__ import annotations
import argparse,csv,io,json,re,zipfile
from pathlib import Path
from collections import Counter,defaultdict

FIELDS=("gbifID","occurrenceID","datasetKey","eventID","locationID",
        "eventDate","samplingProtocol","samplingEffort","sampleSizeValue",
        "sampleSizeUnit","decimalLatitude","decimalLongitude","year",
        "occurrenceStatus")
REQUIRED={"gbifID","datasetKey","occurrenceStatus"}

def audit(reader,expect=None):
    absent=set(FIELDS)-set(reader.fieldnames or [])
    if absent & REQUIRED: raise ValueError("missing required raw columns")
    observed=Counter();labels=Counter();providers=Counter()
    site_events=defaultdict(dict);owner={};conflicts=set();ids=set();n=0
    for row in reader:
        n+=1
        v={k:(row.get(k) or "").strip() for k in FIELDS}
        if not v["gbifID"] or v["gbifID"] in ids:
            raise ValueError("missing/duplicate original gbifID")
        ids.add(v["gbifID"])
        if not v["datasetKey"]: raise ValueError("missing datasetKey")
        providers[v["datasetKey"]]+=1
        labels[v["occurrenceStatus"].upper()]+=1
        observed.update(k for k in FIELDS if v[k])
        if (all(v[k] for k in ("locationID","eventID","eventDate",
                              "samplingProtocol")) and
            (v["samplingEffort"] or
             (v["sampleSizeValue"] and v["sampleSizeUnit"])) and
            re.fullmatch(r"\d{4}-\d{2}-\d{2}",v["eventDate"])):
            site=(v["datasetKey"],v["locationID"],v["samplingProtocol"])
            ev=(v["datasetKey"],v["eventID"])
            prior=owner.get(ev)
            if prior is not None and prior!=site:
                conflicts.update((prior,site))
            owner[ev]=site
            prev=site_events[site].get(v["eventID"])
            if prev is not None and prev!=v["eventDate"]:
                conflicts.add(site)
            site_events[site][v["eventID"]]=v["eventDate"]
    if expect is not None and n!=expect:
        raise ValueError("original row count differs from expected original")
    candidates=sum(len(d)>1 and len(set(d.values()))>1 and site not in conflicts
                   for site,d in site_events.items())
    return {"status":"CANDIDATE_ONLY_NOT_CERTIFIED","rows":n,
            "source_count":len(providers),"status_counts":dict(sorted(labels.items())),
            "nonempty_fields":{k:observed[k] for k in FIELDS},
            "missing_columns":sorted(absent),
            "strict_candidate_sites":candidates,
            "event_site_or_date_conflicts":len(conflicts),
            "certified_repeated_site_count":None,
            "sample_independence_verified":False,
            "ecological_occupancy_identified":False,
            "requires_external_site_and_protocol_validation":True}

def inspect(path,expect=None):
    path=Path(path)
    if path.suffix.lower()==".zip":
        with zipfile.ZipFile(path) as z:
            candidates=[k for k in z.namelist()
                        if k.lower().endswith((".csv",".tsv",".txt"))]
            if len(candidates)!=1: raise ValueError("ambiguous ZIP tabular members")
            with z.open(candidates[0]) as raw:
                with io.TextIOWrapper(raw,encoding="utf-8-sig",newline="") as txt:
                    return audit(csv.DictReader(txt,delimiter="\t"),expect)
    with path.open(encoding="utf-8-sig",newline="") as txt:
        return audit(csv.DictReader(txt,delimiter="\t"),expect)

def test():
    keys=("gbifID","datasetKey","occurrenceStatus","eventID",
          "locationID","eventDate","samplingProtocol","samplingEffort")
    rows=(("1","A","PRESENT","E1","S","2024-04-01","scan","5m"),
          ("2","A","ABSENT","E2","S","2024-04-15","scan","5m"),
          ("3","A","ABSENT","E3","T","2024","scan","5m"),
          ("4","B","PRESENT","E4","S","2024-04-18","scan","5m"))
    txt="\t".join(keys)+"\n"+"".join("\t".join(r)+"\n" for r in rows)
    out=audit(csv.DictReader(io.StringIO(txt),delimiter="\t"),4)
    assert out["strict_candidate_sites"]==1
    assert out["certified_repeated_site_count"] is None
    for payload,expected in ((txt+"\t".join(rows[0])+"\n",None),(txt,29543)):
        try: audit(csv.DictReader(io.StringIO(payload),delimiter="\t"),expected)
        except ValueError: pass
        else: raise AssertionError("negative input failed to reject")
    return {"result":"PASS_SYNTHETIC_FIXTURE","candidate_sites":1,
            "negative_controls":2,"original_2024_archive_opened":False}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("file",nargs="?")
    p.add_argument("--expect-original-29543",action="store_true")
    args=p.parse_args()
    result=inspect(args.file,29543 if args.expect_original_29543 else None) if args.file else test()
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
