#!/usr/bin/env python3
"""MQR-4.90 P9: immutable publisher source geometry and model-projection feasibility probe.

Reads ORIGINAL Matsui 2026 Zenodo 19970795 prediction and environment archives,
verifies both upstream MD5s; records each source field needed for projecting
four trained Maxent CV fold models into each native-only external target.

NO statistical effect estimated; NO fitting; NO target labels loaded.
Only metadata/header excerpts of selected original published files are written.
"""
from pathlib import Path
from zipfile import ZipFile
from hashlib import md5, sha256
from urllib.request import Request, urlopen
from collections import Counter
import json, os, re, tempfile
OUTPUT=Path(os.getenv("MQR490_P9_OUTPUT","p9-feasibility"))
INPUTS={
  "predictions":("3_Maxent_predictions.zip","aa9c99dd43b3060589fa31dddf8501a4",140_000_000),
  "environment":("2_Environmental_data.zip","0be43edc9cd88307bcee95307bbcb06e",70_000_000),
}
UPSTREAM="https://zenodo.org/records/19970795/files/"
TARGETS=[
 ("Oxalis_latifolia_America","Oxalis_latifolia","Oceania"),
 ("Digitaria_sanguinalis_Europe","Digitaria_sanguinalis","Africa"),
 ("Amaranthus_retroflexus_NorthAmerica","Amaranthus_retroflexus","Europe"),
]
def download(name,expected,limit,dest):
  request=Request(UPSTREAM+name+"?download=1",headers={"User-Agent":"MQR-490-source-feasibility/1.0"})
  sha=sha256(); m=md5();size=0
  with urlopen(request,timeout=100) as response,dest.open("wb") as stream:
    if response.status!=200:raise RuntimeError(f"HTTP {response.status}")
    while buf:=response.read(1024*1024):
      size+=len(buf)
      if size>limit:raise RuntimeError("bounded acquisition ceiling exceeded")
      m.update(buf);sha.update(buf);stream.write(buf)
  if m.hexdigest()!=expected:raise RuntimeError(f"ZENODO {name} digest mismatch")
  return {"bytes":size,"md5":m.hexdigest(),"sha256":sha.hexdigest()}
def excerpt(z,member,limit=4000):
  return z.read(member)[:limit].decode("utf-8",errors="replace").replace("\x00","\\0")
def main():
  OUTPUT.mkdir(parents=True,exist_ok=True)
  with tempfile.TemporaryDirectory(prefix="mqr490p9-") as temporary:
    paths={}; hashes={}
    for category,(name,digest,limit) in INPUTS.items():
      path=Path(temporary)/name;hashes[category]=download(name,digest,limit,path);paths[category]=path
    with ZipFile(paths["predictions"]) as models,ZipFile(paths["environment"]) as env:
      if models.testzip() or env.testzip():raise RuntimeError("ZIP CRC rejection")
      mnames=models.namelist(); enames=env.namelist()
      manifest={
        "publication":"Matsui 2026 DOI 10.1002/ece3.73534; corrected DOI 10.1002/ece3.73828",
        "zenodo":"https://zenodo.org/records/19970795",
        "original_source_hashes":hashes,
        "archive_member_counts":{"predictions":len(mnames),"environment":len(enames)},
        "environment_extensions":dict(Counter(Path(s).suffix.lower() for s in enames if not s.endswith("/"))),
        "environment_top_folders":dict(Counter("/".join(s.split("/")[:3]) for s in enames if not s.endswith("/")).most_common(30)),
        "environment_target_examples":{},
        "native_only_models":[],
      }
      for calibration,species,target in TARGETS:
        native=f"3_Maxent_predictions/1_Maxent_output/4-fold_cross-validation/{calibration}/"
        fold_files=[]
        for i in range(4):
          fname=f"{native}{species}_{i}.lambdas"
          if fname not in mnames:
            raise RuntimeError(f"Missing precisely addressable native CV fold .lambdas {fname}")
          txt=excerpt(models,fname,3800)
          variables=re.findall(r"(?:bio\\d+|BIO\\d+)",txt)
          fold_files.append({"member":fname,"byte_size":models.getinfo(fname).file_size,
            "head_lines":txt.splitlines()[:12],"climate_variable_tokens":sorted(set(variables))})
        full=[s for s in mnames if s.endswith(f"/{species}.lambdas") and target.lower() in s.lower()
              and "4-fold" not in s]
        matching=[s for s in enames if species.lower() in s.lower() and target.lower() in s.lower()]
        manifest["native_only_models"].append({"calibration":calibration,"species":species,"target":target,
          "cv_fold_models":fold_files,
          "external_full_model_lambda_candidates":full[:20],
          "environment_target_candidates":matching[:35],
          "full_count":len(full),"environment_matches":len(matching)})
      manifest["environment_target_examples"]={
        "sample_raster_paths":[s for s in enames if s.lower().endswith((".asc",".tif",".bil",".grd"))][:18],
        "first_paths":enames[:25]
      }
      if any(x["environment_matches"]==0 for x in manifest["native_only_models"]):
        manifest["state"]="HOLD_ENV_TARGET_NAMING"
      else:manifest["state"]="SOURCE_COMPONENTS_VISIBLE_NOT_YET_PROJECTED"
      (OUTPUT/"p9-original-model-feasibility.json").write_text(json.dumps(manifest,indent=2),encoding="utf8")
      print("MQR490_P9_MODEL_FOLD_LAMBDAS="+str(sum(len(s["cv_fold_models"]) for s in manifest["native_only_models"])))
      for x in manifest["native_only_models"]:
        print(f"MQR490_P9_COMPONENT={x['calibration']}→{x['target']} MODEL_CANDIDATES={x['full_count']} ENV_MATCHES={x['environment_matches']}")
      print("MQR490_P9_ENVIRONMENT_BYTES="+str(hashes["environment"]["bytes"]))
      print("MQR490_P9_SOURCE_COMPONENT_AUDIT="+manifest["state"])
      print("MQR490_P9_RAW_COMMON_PREDICTIONS=NOT_YET_OBTAINED")
if __name__=="__main__":main()
