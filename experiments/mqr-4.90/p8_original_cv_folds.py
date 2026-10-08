#!/usr/bin/env python3
"""P8 late source court: extract the ORIGINAL Maxent fourfold CV fold results.

Three native-only calibration cohorts, each four Maxent separately fitted
fold models, retained by Matsui 2026 in Zenodo 19970795 prediction ZIP.
The fold Test AUC uses the Maxent background-reference design, not the
same negative-reference used for cross-continent external AUC.
"""
import csv
import io
from pathlib import Path
from p8_source_probe import ARTIFACT_DIR, download
import zipfile

COHORTS = [
    ("Oxalis_latifolia_America", "Oxalis_latifolia", .87),
    ("Digitaria_sanguinalis_Europe", "Digitaria_sanguinalis", .82),
    ("Amaranthus_retroflexus_NorthAmerica", "Amaranthus_retroflexus", .85),
]
PREFIX = "3_Maxent_predictions/1_Maxent_output/4-fold_cross-validation"


def extract(z, folder, taxon, published):
    path = f"{PREFIX}/{folder}/maxentResults.csv"
    try:
        member = z.getinfo(path)
    except KeyError:
        raise RuntimeError(f"missing exact upstream Maxent file {path}")
    with z.open(member) as original:
        reader = csv.DictReader(io.TextIOWrapper(original,encoding="utf-8-sig"))
        selected = []
        for row in reader:
            label = row.get("Species", "")
            if label in {f"{taxon}_{i}" for i in range(4)}:
                auc = float(row["Test AUC"])
                train = int(row["#Training samples"])
                test = int(row["#Test samples"])
                background = int(row["#Background points"])
                if not 0 <= auc <= 1 or min(train,test,background) <= 0:
                    raise RuntimeError("source Maxent fold invalid")
                selected.append((label,train,test,background,auc))
        if len(selected)!=4 or {x[0] for x in selected}!={f"{taxon}_{i}" for i in range(4)}:
            raise RuntimeError("incomplete published 4fold source")
        mean=sum(x[-1] for x in selected)/4
        if abs(mean-published)>0.005001:
            raise RuntimeError(f"{folder}: printed CV={published} vs raw fold {mean:.8f}")
        return selected, mean, path


def main():
    ARTIFACT_DIR.mkdir(exist_ok=True,parents=True)
    archive=ARTIFACT_DIR/"source-temporary.zip"
    download(archive)
    dest=ARTIFACT_DIR/"p8-publisher-cv-folds.csv"
    with zipfile.ZipFile(archive) as z, dest.open("w",newline="",encoding="utf-8") as f:
        csvw=csv.writer(f)
        csvw.writerow(("source_calibration","fold","training_count","test_count",
                      "background_points","reported_fold_test_auc","original_cv_a4_mean"))
        for name,taxon,published in COHORTS:
            folds,mean,path=extract(z,name,taxon,published)
            for fold,train,test,bg,auc in folds:
                csvw.writerow((name,fold,train,test,bg,f"{auc:.4f}",f"{published:.2f}"))
            print(f"MQR490_P8_CV_CALIBRATION={name} FOLD_MEAN={mean:.8f} PUBLISHED={published:.2f} BACKGROUND_POINTS={[x[3] for x in folds]} FILE={path}")
    archive.unlink()
    print("MQR490_P8_CV_FOLD_MODELS=12")
    print("MQR490_P8_CV_SOURCE_FAMILIES=3")
    print("MQR490_P8_CV_ORIGINAL_RESULTS=PASS")
    print("MQR490_P8_CV_EXTERNAL_REFERENCE_MATCHED=NO")


if __name__=="__main__":
    main()
