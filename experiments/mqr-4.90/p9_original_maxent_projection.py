#!/usr/bin/env python3
"""P9: source-verified Maxent 3.4.4 reference projection pilot.

This runs the ORIGINAL published final fitted Maxent .lambdas and all
four original CV-fold .lambdas on the SAME originally published target
environment rasters. Before interpreting fold outputs, compare a freshly
projected final-model raster to the original author-published external
raster. Fails closed on source, jar, projection or reference mismatch.

This is a source-model replay, not a new training run and not proof
of causal CV optimism, cohort independence or transport generality.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlopen, Request
from zipfile import ZipFile
from hashlib import md5, sha256, sha1
from collections import Counter
import json, os, subprocess, math
from p9_maxent_projection_feasibility import INPUTS, download as source_download

ROOT=Path(os.getenv("MQR490_P9_OUTPUT","p9-projection"))
JAR_URL=("https://raw.githubusercontent.com/mrmaxent/Maxent/v3.4.4/"
    "ArchivedReleases/3.4.4/maxent.jar")
JAR_SHA1_GIT_BLOB="1a0a1826cbefdaf551463ed20e3a41944801955a"
SPECIES="Oxalis_latifolia"
CALIBRATION="America"
TARGET="Oceania"
CV_DIR="3_Maxent_predictions/1_Maxent_output/4-fold_cross-validation/Oxalis_latifolia_America/"
EXTERNAL="3_Maxent_predictions/1_Maxent_output/56_predictions/Oxalis_latifolia_America-Oceania/"
ENV="2_Environmental_data/Oxalis_latifolia_Oceania/"
BIO=("Bio01","Bio04","Bio10","Bio11","Bio15","Bio16","Bio28","Bio31")

def download_jar(destination):
    req=Request(JAR_URL,headers={"User-Agent":"MQR-490-projection-source-court/1.0"})
    with urlopen(req,timeout=60) as res: raw=res.read(800000)
    if len(raw)!=675926 or raw[:2]!=b"PK":
        raise RuntimeError("Maxent 3.4.4 archive bytes mismatch")
    calculated=sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    if calculated!=JAR_SHA1_GIT_BLOB:
        raise RuntimeError("Maxent 3.4.4 pinned git blob hash mismatch")
    destination.write_bytes(raw)
    return {"official_tag":"v3.4.4","git_blob_sha1":calculated,"sha256":sha256(raw).hexdigest(),"bytes":len(raw)}

def read_asc(path):
    with path.open("r",encoding="utf8",errors="replace") as stream:
        header={}
        for i in range(6):
            line=stream.readline()
            fields=line.split()
            if len(fields)!=2:
                raise RuntimeError(f"invalid grid header at {i}: {line}")
            header[fields[0].lower()]=float(fields[1])
        if set(("ncols","nrows","xllcorner","yllcorner","cellsize","nodata_value"))-set(header):
            raise RuntimeError(f"not a standard square Maxent ASC raster: {header}")
        nx,ny=int(header["ncols"]),int(header["nrows"])
        if nx*ny>2_000_000:raise RuntimeError("target grid oversized")
        values=[]
        for row in stream:
            if row.strip():
                values.extend(float(cell) for cell in row.split())
        if len(values)!=nx*ny:
            raise RuntimeError(f"target grid incomplete: {len(values)} != {nx*ny}")
    return header,values

def compare(original,reprojected):
    h1,a=read_asc(original)
    h2,b=read_asc(reprojected)
    # Original author publication can be an explicitly cropped target grid.
    # Reprojected climates are the entire ecoregion extent. Never compare
    # different raster columns or assume identical data array origin.
    size=h1["cellsize"]
    if not math.isclose(size,h2["cellsize"],abs_tol=1e-10,rel_tol=0):
        raise RuntimeError("different source and replay cell sizes")
    dx=(h1["xllcorner"]-h2["xllcorner"])/size
    dy=(h1["yllcorner"]-h2["yllcorner"])/size
    if abs(dx-round(dx))>1e-6 or abs(dy-round(dy))>1e-6:
        raise RuntimeError(f"target raster does not align with climate grid: dx={dx}, dy={dy}")
    xoff,yoff=round(dx),round(dy)
    w1,hgt1=int(h1["ncols"]),int(h1["nrows"])
    w2,hgt2=int(h2["ncols"]),int(h2["nrows"])
    diffs=[]; missing=0; uncovered=0
    for row1 in range(hgt1):
        # ASCII grids begin at the northern boundary, yllcorner at south.
        row2=hgt2-yoff-hgt1+row1
        for col1 in range(w1):
            col2=xoff+col1
            a_val=a[row1*w1+col1]
            if row2<0 or row2>=hgt2 or col2<0 or col2>=w2:
                if a_val!=h1["nodata_value"]:uncovered+=1
                continue
            b_val=b[row2*w2+col2]
            if a_val==h1["nodata_value"] and b_val==h2["nodata_value"]:
                missing+=1;continue
            if a_val==h1["nodata_value"] or b_val==h2["nodata_value"]:
                uncovered+=1;continue
            diffs.append(abs(a_val-b_val))
    if uncovered:
        raise RuntimeError(f"published scored target extent or mask has {uncovered} uncovered cells")
    if len(diffs)<250:raise RuntimeError("insufficient shared scored cells")
    return {"n_scored":len(diffs),"n_missing":missing,"n_uncovered":uncovered,
            "max_abs_diff":max(diffs),"mean_abs_diff":sum(diffs)/len(diffs),
            "grid_geometry":h1,"replay_full_grid_geometry":h2,
            "aligned_integer_offset":{"x":xoff,"y":yoff}}


def project(jar,lam,envdir,out):
    cmd=["java","-Djava.awt.headless=true","-Xmx2g","-cp",str(jar),
         "density.Project",str(lam),str(envdir),str(out)]
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=130,check=False)
    if r.returncode!=0 or not out.exists():
        raise RuntimeError(f"Maxent failed code={r.returncode}: {r.stdout[-2500:]} {r.stderr[-2500:]}")
    return {"command_class":"density.Project","stdout_tail":r.stdout[-650:],
            "stderr_tail":r.stderr[-650:],"output_bytes":out.stat().st_size,
            "output_sha256":sha256(out.read_bytes()).hexdigest()}

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    with TemporaryDirectory(prefix="mqr490-p9-") as folder:
        home=Path(folder)
        original_paths={}; hashes={}
        for category,(name,digest,limit) in INPUTS.items():
            path=home/name
            hashes[category]=source_download(name,digest,limit,path)
            original_paths[category]=path
        with ZipFile(original_paths["predictions"]) as z,ZipFile(original_paths["environment"]) as e:
            envdir=home/"env";envdir.mkdir()
            for name in BIO:
                member=ENV+name+".asc"
                envbytes=e.read(member)
                (envdir/(name+".asc")).write_bytes(envbytes)
            final_lam=home/"final.lambdas"
            final_lam.write_bytes(z.read(EXTERNAL+SPECIES+".lambdas"))
            published=home/"published.asc"
            published.write_bytes(z.read(EXTERNAL+SPECIES+".asc"))
            folds=[]
            for i in range(4):
                f=home/f"fold{i}.lambdas"
                f.write_bytes(z.read(CV_DIR+SPECIES+f"_{i}.lambdas"))
                folds.append(f)
            jar=home/"maxent.jar"
            jar_receipt=download_jar(jar)
            projected=home/"fresh_final.asc"
            final_run=project(jar,final_lam,envdir,projected)
            consistency=compare(published,projected)
            # The current source output uses cloglog Maxent 3.4.4.
            # Assert actual numeric agreement instead of trusting that description.
            if consistency["max_abs_diff"]>1e-4:
                raise RuntimeError(f"original Maxent source model did not replay: {consistency}")
            fold_runs=[]
            for i,lam in enumerate(folds):
                fout=home/f"projected_fold{i}.asc"
                receipt=project(jar,lam,envdir,fout)
                fh,data=read_asc(fout)
                if not math.isclose(fh["ncols"],consistency["grid_geometry"]["ncols"]):
                    raise RuntimeError("CV fold target map geometry changed")
                fold_runs.append({"fold":i,**receipt})
            receipt={
                "source_doi":"10.5281/zenodo.19970795",
                "archive_hashes":hashes,
                "maxent_software":jar_receipt,
                "case":"Oxalis latifolia | train America | external target Oceania",
                "source_final_lambda_path":EXTERNAL+SPECIES+".lambdas",
                "source_cv_fold_lambdas":[CV_DIR+SPECIES+f"_{i}.lambdas" for i in range(4)],
                "environment_source_members":[ENV+n+".asc" for n in BIO],
                "source_original_published_target_raster":EXTERNAL+SPECIES+".asc",
                "final_project":final_run,
                "final_vs_original":consistency,
                "fold_projected":fold_runs,
                "scope":"common external raster projection feasibility; no AUC until score-to-label alignment",
                "policy":"independent target, no new model fit, no target-label selection"
            }
        (ROOT/"maxent-projection-pilot.json").write_text(json.dumps(receipt,indent=2),encoding="utf8")
        print("MQR490_P9_AUTHOR_FINAL_RASTER_REPLAY_MAX_ABS_ERROR="+str(consistency["max_abs_diff"]))
        print("MQR490_P9_AUTHOR_FINAL_RASTER_REPLAY_VALID_CELLS="+str(consistency["n_scored"]))
        print("MQR490_P9_FOLD_PREDICTION_MAPS="+str(len(fold_runs)))
        print("MQR490_P9_MAXENT_344_GIT_BLOB="+jar_receipt["git_blob_sha1"])
        print("MQR490_P9_SAME_TARGET_FOLD_MODEL_PROJECTIONS=PASS")
        print("MQR490_P9_MATCHED_TARGET_FOLD_AUC=NOT_YET_IDENTIFIED")
if __name__=="__main__":main()
