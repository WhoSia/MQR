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
ROOT=Path("p491-ten-target-matrix")
BASE="3_Maxent_predictions/1_Maxent_output/"
TABLE=Path(__file__).resolve().parents[1]/"mqr-4.90"/"matsui_2026_native_only_external_auc_pairs.csv"
def source_cases():
    with TABLE.open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=10 or len({(r["species"],r["target"]) for r in rows})!=10 or len({r["species"] for r in rows})!=3:
        raise RuntimeError("source table no longer has exactly ten targets from three species")
    return [(r["species"].replace(" ","_"),r["calibration"].replace(" ",""),
             r["target"].replace(" ",""),float(r["external_region_auc"])) for r in rows]
CASES=source_cases()
def auc(p,n):
    neg=sorted(n); return sum(bisect_left(neg,x)+.5*(bisect_right(neg,x)-bisect_left(neg,x)) for x in p)/(len(p)*len(n))
def main():
    ROOT.mkdir(exist_ok=True)
    report={"cases":[],"source":"10.5281/zenodo.19970795","interpretation":"ten cases nested within three species and one paper, not independent studies or signed CV optimism"}
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
                bad=0;excluded=0;maxerror=0;examples=[];boundary_repairs=[];interior_pos=[];interior_neg=[];boundary_counts=[0,0]
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
                                # Generate alternative cells ONLY for source points that
                                # lie exactly on ASCII-grid cell boundaries. The source
                                # score is used to TEST uniqueness, not pick the best AUC.
                                xfloat=(x-h["xllcorner"])/h["cellsize"]
                                yfloat=(y-h["yllcorner"])/h["cellsize"]
                                onx=abs(xfloat-round(xfloat))<1e-5
                                ony=abs(yfloat-round(yfloat))<1e-5
                                cols=[c]+([c-1] if onx else [])
                                rows=[r]+([r+1] if ony else [])
                                solutions=[]
                                for rr in rows:
                                    for cc in cols:
                                        if 0<=cc<w and 0<=rr<height:
                                            j=rr*w+cc
                                            if base[j]!=h["nodata_value"] and abs(base[j]-original_score)<=1e-4:
                                                solutions.append((rr,cc,j))
                                if len(solutions)==1 and (onx or ony):
                                    r,c,ix=solutions[0]
                                    boundary_repairs.append({"X":x,"Y":y,"source_score":original_score,
                                      "chosen_row":r,"chosen_col":c,"edge_x":onx,"edge_y":ony,
                                      "delta_original":delta})
                                else:
                                    bad+=1
                                    if len(examples)<12:examples.append({"X":x,"Y":y,"source_score":original_score,
                                      "replay_score":base[ix],"delta":delta,"grid_col":c,"grid_row":r,
                                      "on_vertical_edge":onx,"on_horizontal_edge":ony,
                                      "candidate_matches":len(solutions)})
                            if any(v[ix]==hh["nodata_value"] for hh,v in folds):raise RuntimeError("fold missing source point")
                            values_for_point=[original_score]+[v[ix] for _,v in folds]
                            out.append(values_for_point)
                            xx=(x-h["xllcorner"])/h["cellsize"]
                            yy=(y-h["yllcorner"])/h["cellsize"]
                            on_boundary=abs(xx-round(xx))<1e-5 or abs(yy-round(yy))<1e-5
                            if on_boundary:
                                boundary_counts[1-label]+=1
                            else:
                                (interior_pos if label else interior_neg).append(values_for_point)
                if bad:
                    entry.update(state="HOLD_COORDINATE_JOIN",bad_count=bad,examples=examples,max_error=maxerror,
                        positives_before_hold=len(positives),negatives_before_hold=len(negatives),
                        boundary_repairs=boundary_repairs)
                    report["cases"].append(entry)
                    print("MQR491_P16_COORDINATE_HOLD="+json.dumps(entry,ensure_ascii=False),flush=True)
                    continue
                if min(len(positives),len(negatives))<2:raise RuntimeError("too few scored cases")
                results=[auc([p[j] for p in positives],[n[j] for n in negatives]) for j in range(5)]
                if min(len(interior_pos),len(interior_neg))<2:
                    raise RuntimeError("no interior paired evaluation")
                interior_auc=[auc([p[j] for p in interior_pos],[n[j] for n in interior_neg]) for j in range(5)]
                sensitivity={"interior_positive":len(interior_pos),"interior_negative":len(interior_neg),
                    "boundary_positive":boundary_counts[0],"boundary_negative":boundary_counts[1],
                    "interior_auc":interior_auc,"full_auc":results,
                    "delta":[x-y for x,y in zip(interior_auc,results)],
                    "policy":"exclude all boundary points using only X,Y and grid, not score"}
                if round(results[0],2)!=published_auc:
                    entry.update(state="HOLD_PUBLISHED_AUC_MISMATCH",replayed_auc=results[0])
                    report["cases"].append(entry)
                    continue
                entry.update(state="PASS",published_source_target_raster=targetpath,
                    positives=len(positives),negative_reference_cells=len(negatives),
                    source_score_blanks=excluded,source_score_max_abs_replay_error=maxerror,
                    source_boundary_cell_resolutions=boundary_repairs,boundary_blind_sensitivity=sensitivity,
                    reconstructed_final_target_auc=results[0],original_fold_target_auc=results[1:],
                    original_published_external_auc_rounded=round(results[0],2)==published_auc)
                report["cases"].append(entry)
                print("MQR491_TEN_TARGET_CASE="+json.dumps({"species":species,"target":target,"positive":len(positives),"negative":len(negatives),"folds":results[1:],"final":results[0],"fold_range":max(results[1:])-min(results[1:]),"boundary_pos":boundary_counts[0],"boundary_neg":boundary_counts[1],"boundary_resolutions":len(boundary_repairs),"interior_folds":interior_auc[1:]}),flush=True)
                print("MQR491_P16_CASE="+json.dumps({k:v for k,v in entry.items()
                      if k in ("species","target","state","positives","negative_reference_cells",
                      "reconstructed_final_target_auc","original_fold_target_auc","source_score_max_abs_replay_error")}))
    (ROOT/"ten-target-matrix.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
    if any(x["state"]!="PASS" for x in report["cases"]):
        raise RuntimeError("source-identity or exact replay gate not cleared: "+str([(x["species"],x["state"]) for x in report["cases"]]))
    print("MQR491_TEN_TARGET_MATCHED_CASES="+str(len(report["cases"])))
    print("MQR491_TEN_TARGETS_MATCHED_FOLD_AUC=PASS")
if __name__=="__main__":main()
