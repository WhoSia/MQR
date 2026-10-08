#!/usr/bin/env python3
"""P1.2 inspect publisher-prediction ZIP paths and raster extents without fitting."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from collections import defaultdict
import json
from p9_maxent_projection_feasibility import INPUTS, download
from p9_original_maxent_projection import EXTERNAL, SPECIES, ENV, read_asc
OUT=Path("p491-original-prediction-inventory")
def headline(z,name):
    with z.open(name) as stream:
        h={}
        for _ in range(6):
            t=stream.readline().decode("utf8","replace").split()
            if len(t)!=2:return None
            h[t[0].lower()]=float(t[1])
    if not all(k in h for k in ("ncols","nrows","xllcorner","yllcorner","cellsize")):return None
    return {"ncols":int(h["ncols"]),"nrows":int(h["nrows"]),"xll":h["xllcorner"],"yll":h["yllcorner"],
      "xmax":h["xllcorner"]+h["ncols"]*h["cellsize"],"ymax":h["yllcorner"]+h["nrows"]*h["cellsize"],
      "bytes":z.getinfo(name).file_size}
def main():
    OUT.mkdir(exist_ok=True)
    with TemporaryDirectory() as tmp:
        src=Path(tmp)/INPUTS["predictions"][0]
        download(*INPUTS["predictions"],src)
        with ZipFile(src) as z:
            matched=[n for n in z.namelist() if SPECIES.lower() in n.lower() and
                     n.lower().endswith((".asc",".lambdas",".csv",".html"))]
            prediction_dir=[n for n in z.namelist() if n.startswith(EXTERNAL) and not n.endswith("/")]
            rasters=[{"path":n,**(headline(z,n) or {})} for n in matched if n.lower().endswith(".asc")]
            receipt={"species":SPECIES,"claimed_external_model_directory":EXTERNAL,
              "external_directory_members":prediction_dir[:100],
              "species_asc_raster_candidates":rasters[:150],
              "source_zip_entries_matching_species":len(matched),
              "source_zip_entries_matching_external_dir":len(prediction_dir)}
            (OUT/"prediction-candidates.json").write_text(json.dumps(receipt,indent=2))
            print("MQR491_P12_SPECIES_ASC_COUNT="+str(len(rasters)))
            print("MQR491_P12_EXTERNAL_DIRECTORY_MEMBERS="+json.dumps(prediction_dir[:35]))
            print("MQR491_P12_ASC_BBOX_LIST="+json.dumps(rasters[:45]))
            print("MQR491_P12_CANDIDATE_RECEIPT_WRITTEN=YES")
if __name__=="__main__":main()
