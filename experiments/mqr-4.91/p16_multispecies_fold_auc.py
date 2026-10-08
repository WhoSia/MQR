#!/usr/bin/env python3
"""MQR 4.91 P1.6: source-identified fold target projection for two further species.

No cross-paper pooling or spatial-CV optimism claims.
"""
import csv,json,math
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from p15_original_fold_matched_target_auc import (INPUTS,source_download,download_jar,project,read_asc,
    compare,score_join as legacy_score_join,BIO)
from p9_original_maxent_projection import CV_DIR as OXALIS_CV
from p14_source_coordinate_join_probe import snippet
from bisect import bisect_left,bisect_right
from io import TextIOWrapper
ROOT=Path("p491-p16-multispecies")
BASE="3_Maxent_predictions/1_Maxent_output/"
CASES=[
 ("Digitaria_sanguinalis","Europe","Africa",0.56),
 ("Amaranthus_retroflexus","NorthAmerica","Europe",0.81)]
def auc(p,n):
    neg=sorted(n); return sum(bisect_left(neg,x)+.5*(bisect_right(neg,x)-bisect_left(neg,x)) for x in p)/(len(p)*len(n))
def main():
    ROOT.mkdir(exist_ok=True)
    report={"cases":[],"source":"10.5281/zenodo.19970795","interpretation":"same-original-external-target comparison across fitted models; not CV optimism"}
    with TemporaryDirectory() as d:
        t=Path(d);paths={}
        for cat,(name,digest,limit) in INPUTS.items():
            p=t/name;source_download(name,digest,limit,p);paths[cat]=p
        jar=t/"maxent.jar";report["java"]=download_jar(jar)
        with ZipFile(paths["predictions"]) as z, ZipFile(paths["environment"]) as e:
            zfiles=set(z.namelist());efiles=set(e.namelist())
            for species,cal,target,published_auc in CASES:
                stem=f"{species}_{cal}-{target}"
                external=BASE+f"56_predictions/{stem}/"
                envpath=f"2_Environmental_data/{species}_{target}/"
                cvpath=BASE+f"4-fold_cross-validation/{species}_{cal}/"
                entry={"species":species,"calibration":cal,"target":target,
                       "published_two_decimal_auc":published_auc}
                available=[f for f in zfiles if f.startswith(external) and f.endswith(".asc")
                           and not any(t in f for t in ("_clamping","_novel"))]
                entry["published_asc_candidates"]=sorted(available)
                source_model=external+species+".lambdas"
                # Read output plot names and determine target map by geographic metadata.
                candidate_meta=[]
                for f in sorted(available):
                    with z.open(f) as fh:
                        h={}
                        for _ in range(6):
                            k,v=fh.readline().decode("utf8","replace").split()
                            h[k.lower()]=float(v)
                    candidate_meta.append({"path":f,"grid":h})
                entry["source_raster_candidates"]=candidate_meta
                target_candidates=[q for q in candidate_meta if q["path"]!=external+species+".asc"]
                if len(target_candidates)!=1:
                    entry["state"]="HOLD_AMBIGUOUS_TARGET_RASTER";report["cases"].append(entry);continue
                targetpath=target_candidates[0]["path"]
                if source_model not in zfiles:
                    entry["state"]="HOLD_MODEL_NOT_FOUND";report["cases"].append(entry);continue
                missing=[envpath+b+".asc" for b in BIO if envpath+b+".asc" not in efiles]
                if missing:
                    entry["state"]="HOLD_ENV_MISSING";entry["missing"]=missing;report["cases"].append(entry);continue
                env=t/f"env-{species}";env.mkdir()
                for b in BIO:(env/(b+".asc")).write_bytes(e.read(envpath+b+".asc"))
                lam=t/f"{species}.lambdas";lam.write_bytes(z.read(source_model))
                original=t/f"{species}-published.asc";original.write_bytes(z.read(targetpath))
                fresh=t/f"{species}-fresh.asc";project(jar,lam,env,fresh)
                entry["final_raster_replay"]=compare(original,fresh)
                if entry["final_raster_replay"]["max_abs_diff"]>1e-4:
                    entry["state"]="HOLD_FINAL_RASTER_NUMERIC";report["cases"].append(entry);continue
                folds=[]
                for i in range(4):
                    x=cvpath+species+f"_{i}.lambdas"
                    if x not in zfiles:raise RuntimeError(f"missing original model {x}")
                    l=t/f"{species}-{i}.lambdas";l.write_bytes(z.read(x))
                    output=t/f"{species}-{i}.asc";project(jar,l,env,output)
                    folds.append(read_asc(output))
                h,base=read_asc(fresh);w=int(h["ncols"]);height=int(h["nrows"])
                positives=[];negatives=[]
                bad=0;excluded=0;maxerror=0;examples=[]
                for label,sub,suffix,out in [
                    (1,"1_Maxent_values_for_presence_cells","",positives),
                    (0,"2_Maxent_values_for_absence_cells","_2",negatives)]:
                    name=f"3_Maxent_predictions/2_Maxent_values/{sub}/{stem}{suffix}.csv"
                    if name not in zfiles:raise RuntimeError("missing exact source CSV "+name)
                    with TextIOWrapper(z.open(name),encoding="utf-8-sig",newline="") as f:
                        for row in csv.DictReader(f):
                            score=row.get("SAMPLE_1","").strip()
                            if not score or score.upper() in ("NA","N/A","NULL"):
                                excluded+=1;continue
                            x,y=float(row["X"]),float(row["Y"])
                            c=math.floor((x-h["xllcorner"])/h["cellsize"])
                            r=height-1-math.floor((y-h["yllcorner"])/h["cellsize"])
                            if not(0<=c<w and 0<=r<height):raise RuntimeError("source point outside grid")
                            ix=r*w+c
                            if base[ix]==h["nodata_value"]:raise RuntimeError("unexpected source score masked")
                            original_score=float(score)
                            delta=abs(original_score-base[ix]);maxerror=max(maxerror,delta)
                            if delta>1e-4:
                                bad+=1
                                if len(examples)<12:examples.append({"X":x,"Y":y,"source_score":original_score,"replay_score":base[ix],"delta":delta,"grid_col":c,"grid_row":r})
                            if any(v[ix]==hh["nodata_value"] for hh,v in folds):raise RuntimeError("fold missing source point")
                            out.append([original_score]+[v[ix] for _,v in folds])
                if bad:
                    entry.update(state="HOLD_COORDINATE_JOIN",bad_count=bad,examples=examples,max_error=maxerror,
                        positives_before_hold=len(positives),negatives_before_hold=len(negatives))
                    report["cases"].append(entry)
                    print("MQR491_P16_COORDINATE_HOLD="+json.dumps(entry,ensure_ascii=False),flush=True)
                    continue
                if min(len(positives),len(negatives))<2:raise RuntimeError("too few scored cases")
                results=[auc([p[j] for p in positives],[n[j] for n in negatives]) for j in range(5)]
                entry.update(state="PASS",published_source_target_raster=targetpath,
                    positives=len(positives),negative_reference_cells=len(negatives),
                    source_score_blanks=excluded,source_score_max_abs_replay_error=maxerror,
                    reconstructed_final_target_auc=results[0],original_fold_target_auc=results[1:],
                    original_published_external_auc_rounded=round(results[0],2)==published_auc)
                report["cases"].append(entry)
                print("MQR491_P16_CASE="+json.dumps({k:v for k,v in entry.items()
                      if k in ("species","target","state","positives","negative_reference_cells",
                      "reconstructed_final_target_auc","original_fold_target_auc","source_score_max_abs_replay_error")}))
    (ROOT/"p16-results.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
    if any(x["state"]!="PASS" for x in report["cases"]):
        raise RuntimeError("source-identity or exact replay gate not cleared: "+str([(x["species"],x["state"]) for x in report["cases"]]))
    print("MQR491_P16_TWO_SPECIES_SOURCE_MATCHED_AUC=PASS")
if __name__=="__main__":main()
