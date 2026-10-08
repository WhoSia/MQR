#!/usr/bin/env python3
"""MQR 4.90 P8: materialize all ten native-only cross-continent AUC references.

Input: publisher tables A1–A4 transcribed and source-court verified;
       original Zenodo 19970795 Maxent scores, pinned MD5/SHA256.
Output: ephemeral pairwise score streams to be recomputed by Rust,
        compact SHA256/row-count genealogical audit receipts.

No absent score is converted to zero. No confidence interval or pooled
external-validation effect is inferred from spatially dependent grid cells.
"""
import csv
import json
from hashlib import sha256
from pathlib import Path
import zipfile
from p8_source_probe import ARTIFACT_DIR, download
from p8_extract_matsui_scores import read_scores, select_entry

TABLE=Path(__file__).with_name("matsui_2026_native_only_external_auc_pairs.csv")
PREF="3_Maxent_predictions/2_Maxent_values"


def case_path(row):
    return (
        row["species"].replace(" ", "_") + "_" +
        row["calibration"].replace(" ", "") + "-" +
        row["target"].replace(" ", "")
    )


def main():
    ARTIFACT_DIR.mkdir(exist_ok=True,parents=True)
    with TABLE.open(newline="", encoding="utf-8") as fh:
        source=list(csv.DictReader(fh))
    if len(source)!=10 or len({(x["species"],x["target"]) for x in source})!=10:
        raise RuntimeError("10 distinct source target rows required")
    archive=ARTIFACT_DIR/"source-temporary.zip"
    receipt=download(archive)
    score_dir=ARTIFACT_DIR/"scores"
    score_dir.mkdir(exist_ok=True)
    all_receipts=[]
    with zipfile.ZipFile(archive) as zin, \
         (ARTIFACT_DIR/"p8-all-targets.tsv").open("w",encoding="utf-8") as tsv:
        for entry in source:
            stem=case_path(entry)
            source_yes=select_entry(zin,"1_Maxent_values_for_presence_cells",stem+".csv")
            source_no=select_entry(zin,"2_Maxent_values_for_absence_cells",stem+"_2.csv")
            positive,p_missing=read_scores(zin,source_yes,1)
            negative,n_missing=read_scores(zin,source_no,0)
            path=score_dir/(stem+".csv")
            with path.open("w",newline="",encoding="utf-8") as out:
                csvw=csv.writer(out)
                csvw.writerow(["label","score"])
                csvw.writerows(positive)
                csvw.writerows(negative)
            if path.stat().st_size>12_000_000:
                raise RuntimeError("one source target stream exceeds bounded limit")
            prior=float(entry["external_region_auc"])
            all_receipts.append({
                "model_calibration_target":stem,
                "source_species":entry["species"],
                "source_table":entry["source_external_table"],
                "source_reported_external_auc":prior,
                "positive_count":len(positive),
                "negative_grid_count":len(negative),
                "missing_positive_predictions":p_missing,
                "missing_negative_predictions":n_missing,
                "prediction_reference_definition":"unrecorded source grid cells",
                "positive_source_path":source_yes.filename,
                "negative_source_path":source_no.filename,
                "score_stream_sha256":sha256(path.read_bytes()).hexdigest(),
            })
            tsv.write(f"{stem}\t{path.as_posix()}\t{prior:.2f}\n")
    archive.unlink()
    info={
        "doi":"10.5281/zenodo.19970795",
        "publisher_source_md5":receipt["md5"],
        "publisher_source_sha256":receipt["sha256"],
        "input_table_sha256":sha256(TABLE.read_bytes()).hexdigest(),
        "case_count":len(all_receipts),
        "independent_biological_families":3,
        "comparison_type":"score re-evaluation within publisher's own target negative-reference design",
        "common_cv_and_target_reference":"NOT_VERIFIED",
        "spatial_cell_independence":"NOT_ASSUMED",
        "cases":all_receipts,
    }
    (ARTIFACT_DIR/"p8-all-targets-provenance.json").write_text(
        json.dumps(info,indent=2),encoding="utf-8"
    )
    print("MQR490_P8_NATIVE_SOURCE_ROWS=10")
    print("MQR490_P8_NATIVE_BIOLOGICAL_FAMILIES=3")
    print("MQR490_P8_ALL_TARGETS_EXTRACTED=PASS")


if __name__=="__main__":
    main()
