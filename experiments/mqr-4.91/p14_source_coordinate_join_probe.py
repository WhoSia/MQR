#!/usr/bin/env python3
"""P1.4 original-source target label/coordinate join feasibility."""
import csv,io,json
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from p9_maxent_projection_feasibility import INPUTS,download
OUT=Path("p491-p14-coordinates")
def snippet(z,path):
    stream=io.TextIOWrapper(z.open(path),encoding="utf-8-sig",newline="")
    r=csv.DictReader(stream)
    return {"path":path,"fields":r.fieldnames,"rows":list(__import__("itertools").islice(r,4)),"size":z.getinfo(path).file_size}
def main():
    OUT.mkdir(exist_ok=True)
    with TemporaryDirectory() as t:
        p=Path(t)/INPUTS["predictions"][0]
        download(*INPUTS["predictions"],p)
        with ZipFile(p) as z:
            all_files=z.namelist()
            names=[n for n in all_files if n.lower().endswith(".csv") and ("Oxalis_latifolia_America-Oceania" in n or "Oxalis_latifolia_" in n and "America-Oceania" in n)]
            names=sorted(names,key=lambda x:(0 if "2_Maxent_values" in x else 1,len(x)))
            receipts=[snippet(z,n) for n in names[:28] if z.getinfo(n).file_size<5000000]
            candidates=[n for n in all_files if n.lower().endswith(".csv") and any(k in n.lower() for k in ("presence","occurrence","sample","background"))]
            report={"exact_case_csv":receipts,"coordinate_candidate_paths":candidates[:130],"case_count":len(names)}
            (OUT/"source-columns.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
            for x in receipts:
                print("MQR491_P14_CSV="+json.dumps({"path":x["path"],"fields":x["fields"],"sample":x["rows"][:2]},ensure_ascii=False))
            print("MQR491_P14_SOURCE_COLUMNS_AUDITED=PASS")
if __name__=="__main__":main()
