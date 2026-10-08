#!/usr/bin/env python3
"""MQR-4.91 P1: inspect pinned source rasters against Java projector output.

Diagnostic only: no score AUC, no biological inference, no re-fitting.
"""
import json, math, os, subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from p9_maxent_projection_feasibility import INPUTS, download
from p9_original_maxent_projection import (BIO, ENV, EXTERNAL, SPECIES,
                                            download_jar, project, read_asc)
OUT=Path("p491-grid-diagnostic")
def header_only(data):
    return {a.lower():float(b) for a,b in
            (line.split() for line in data.decode("utf8","replace").splitlines()[:6])}
def inspect_grid(header, numbers=None):
    n=int(header["ncols"])*int(header["nrows"])
    return {"width":int(header["ncols"]),"height":int(header["nrows"]),
      "left":header["xllcorner"],"bottom":header["yllcorner"],
      "right":header["xllcorner"]+int(header["ncols"])*header["cellsize"],
      "top":header["yllcorner"]+int(header["nrows"])*header["cellsize"],
      "cellsize":header["cellsize"],"nodata":header["nodata_value"],
      "total_cells":n,**({"valid_cells":sum(x!=header["nodata_value"] for x in numbers)}
                           if numbers is not None else {})}
def counts(published,replay):
    hp,ap=published;hr,ar=replay
    nx,ny=int(hp["ncols"]),int(hp["nrows"])
    rx,ry=int(hr["ncols"]),int(hr["nrows"])
    delta=(hp["xllcorner"]-hr["xllcorner"])/hr["cellsize"],(hp["yllcorner"]-hr["yllcorner"])/hr["cellsize"]
    result={"grid_offset_float":delta,"author_valid":0,"replay_valid":0,
            "both_valid":0,"author_only":0,"replay_only":0,"both_missing":0,
            "out_of_bounds_author_valid":0,"inside_bounds_author_only":0,
            "paired_abs_diff_max":0.0}
    if hp["cellsize"]!=hr["cellsize"] or any(abs(k-round(k))>1e-6 for k in delta):
        result["note"]="grid alignment unsupported";return result
    xo,yo=round(delta[0]),round(delta[1])
    for y in range(ny):
        yy=ry-yo-ny+y
        for x in range(nx):
            xx=xo+x
            aval=ap[y*nx+x];aok=aval!=hp["nodata_value"]
            if aok: result["author_valid"]+=1
            if xx<0 or yy<0 or xx>=rx or yy>=ry:
                if aok:result["out_of_bounds_author_valid"]+=1
                continue
            bval=ar[yy*rx+xx];bok=bval!=hr["nodata_value"]
            if bok:result["replay_valid"]+=1
            if aok and bok:
                result["both_valid"]+=1
                result["paired_abs_diff_max"]=max(result["paired_abs_diff_max"],abs(aval-bval))
            elif aok:
                result["author_only"]+=1
                result["inside_bounds_author_only"]+=1
            elif bok:result["replay_only"]+=1
            else:result["both_missing"]+=1
    return result

def main():
    OUT.mkdir(exist_ok=True)
    receipt={"purpose":"source-level geometry/mask diagnosis; zero claims about fold AUC"}
    with TemporaryDirectory() as t:
        t=Path(t); files={}
        for cat,(name,digest,limit) in INPUTS.items():
            f=t/name;files[cat]=f;download(name,digest,limit,f)
        with ZipFile(files["predictions"]) as z,ZipFile(files["environment"]) as e:
            env=t/"environment";env.mkdir()
            source={}
            for bio in BIO:
                b=e.read(ENV+bio+".asc")
                (env/(bio+".asc")).write_bytes(b)
                h,v=read_asc(env/(bio+".asc"))
                source[bio]=inspect_grid(h,v)
            model=t/"final.lambdas";model.write_bytes(z.read(EXTERNAL+SPECIES+".lambdas"))
            publ=t/"author.asc";publ.write_bytes(z.read(EXTERNAL+SPECIES+".asc"))
            jar=t/"maxent.jar";receipt["maxent_jar"]=download_jar(jar)
            fout=t/"independent.asc";receipt["projector"]=project(jar,model,env,fout)
            hp,ap=read_asc(publ);hr,ar=read_asc(fout)
            receipt["author"]=inspect_grid(hp,ap)
            receipt["replay"]=inspect_grid(hr,ar)
            receipt["source_input_rasters"]=source
            receipt["overlap"]=counts((hp,ap),(hr,ar))
            receipt["same_grid_all_bands"]=all(source[b]==source[BIO[0]] for b in BIO)
        (OUT/"geometry-mask.json").write_text(json.dumps(receipt,indent=2))
    print("MQR491_GRID_DIAGNOSTIC_WRITTEN=YES")
    print("MQR491_AUTHOR_ONLY="+str(receipt["overlap"]["author_only"]))
    print("MQR491_SOURCE_BAND_GRID_IDENTICAL="+str(receipt["same_grid_all_bands"]))
    print("MQR491_CAUSAL_OR_AUC_RESULT=NOT_CLAIMED")
if __name__=="__main__":main()
