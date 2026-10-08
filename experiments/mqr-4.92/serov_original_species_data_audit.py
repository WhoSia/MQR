#!/usr/bin/env python3
"""MQR 4.92: exact independent publisher species-CSV source inventory.

Read one original Serov/Koldasbayeva/Zaytsev Git blob, without downloading the
large biomedical-cell source corpus or inferring labels not given by the data.
This is a dataset source audit, not a reproduction of the article's risk plots.
"""
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.request import Request,urlopen

REPO="egorser0v/Importance-reweighting"
COMMIT="46c4d011c9f0cd0614c08e7edb68ac2491f659c8"
PATH="datasets/species/oxalis.csv"
GIT_BLOB="b083688856e2cc8376df9e83cca42160450f469d"
OUT=Path("mqr492-serov-original-species-csv-audit.json")

def read_frozen():
    url=f"https://raw.githubusercontent.com/{REPO}/{COMMIT}/{PATH}"
    with urlopen(Request(url,headers={"User-Agent":"MQR492-pinned-data-audit/1.0"}),timeout=35) as r:
        data=r.read(3_000_000)
    if not 100_000<len(data)<2_500_000:
        raise ValueError("source CSV byte count outside expected bounds")
    blob=hashlib.sha1(b"blob "+str(len(data)).encode()+bytes([0])+data).hexdigest()
    if blob!=GIT_BLOB:
        raise ValueError(f"source species CSV identity mismatch: {blob}")
    return data

def main():
    raw=read_frozen()
    text=raw.decode("utf-8-sig")
    stream=csv.reader(io.StringIO(text,newline=""))
    header=next(stream,None)
    if not header or len(header)<2:raise ValueError("source CSV missing columns")
    width=len(header)
    if len(set(header))!=width:raise ValueError("duplicate source CSV column names")
    total=0;malformed=0;blank_per_column=[0]*width
    for row in stream:
        if len(row)!=width:
            malformed+=1
            continue
        total+=1
        for j,value in enumerate(row):
            if not value.strip():blank_per_column[j]+=1
    if total<10 or malformed:raise ValueError("source CSV invalid row-width or too few data rows")
    result={"source_root":"Serov-Koldasbayeva-Zaytsev-2026",
      "repo":REPO,"commit":COMMIT,"source_original_file":PATH,
      "source_git_blob_sha1":GIT_BLOB,"bytes":len(raw),
      "column_count":width,"column_names":header,
      "row_count":total,"malformed_rows":malformed,
      "blank_per_column":dict(zip(header,blank_per_column)),
      "scientific_status":"SOURCE_DATA_IDENTITY_AND_COLUMNS_PASS_ONLY",
      "not_identified":["target risk labels","training vs deployment splits",
        "model predictions","population source/target transfer success","cross-paper common estimand"],
      "noncomparability":"Matsui original Oxalis latifolia source is distinct; matching string oxalis does not prove same sample universe"}
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf8")
    print("MQR492_SEROV_ORIGINAL_CSV_SCHEMA="+json.dumps({
      "rows":total,"cols":width,"headers":header},ensure_ascii=False))
    print("MQR492_INDEPENDENT_ORIGINAL_DATA_IDENTITY=PASS")

if __name__=="__main__":main()
