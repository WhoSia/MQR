#!/usr/bin/env python3
"""P8 source-acquisition receipt for the corrected Matsui (2026) dataset.

READ-ONLY. Downloads a *public* Zenodo archive into the ephemeral CI runner.
Verifies the upstream publisher's MD5; exposes source filenames, sizes, and
bounded CSV header previews as a small provenance artifact. No source files
are committed or automatically uploaded to GitHub/Drive.
"""
from collections import Counter
from hashlib import md5, sha256
from pathlib import Path, PurePosixPath
from urllib.request import Request, urlopen
import csv
import io
import json
import os
import zipfile

RECORD = "https://zenodo.org/records/19970795"
URL = RECORD + "/files/3_Maxent_predictions.zip?download=1"
UPSTREAM_MD5 = "aa9c99dd43b3060589fa31dddf8501a4"
MAX_DOWNLOAD = 140_000_000
MAX_MEMBER_PROBE = 3_000_000
ARTIFACT_DIR = Path(os.environ.get("MQR490_P8_OUTPUT", "p8-materialization"))


def download(destination: Path) -> dict:
    req = Request(URL, headers={"User-Agent": "MQR-4.90-public-source-audit/1.0"})
    h1, h2, count = md5(), sha256(), 0
    with urlopen(req, timeout=85) as response, destination.open("wb") as out:
        if response.status != 200:
            raise RuntimeError(f"source download failed HTTP {response.status}")
        while True:
            block = response.read(1 << 20)
            if not block:
                break
            count += len(block)
            if count > MAX_DOWNLOAD:
                raise RuntimeError("pinned public archive unexpectedly too large")
            h1.update(block)
            h2.update(block)
            out.write(block)
    if h1.hexdigest() != UPSTREAM_MD5:
        raise RuntimeError("upstream Zenodo MD5 mismatch; do not inspect")
    return {"download_bytes": count, "md5": h1.hexdigest(), "sha256": h2.hexdigest()}


def source_preview(zipfile_obj, item) -> dict:
    meta = {"path": item.filename, "uncompressed_bytes": item.file_size,
            "crc32": format(item.CRC, "08x")}
    if item.file_size > MAX_MEMBER_PROBE or not item.filename.lower().endswith(".csv"):
        return meta
    with zipfile_obj.open(item, "r") as fp:
        preview = fp.read(min(item.file_size, 16384))
    text = preview.decode("utf-8-sig", errors="replace")
    rows = list(csv.reader(io.StringIO(text)))
    meta["csv_header"] = rows[0][:20] if rows else []
    meta["first_row"] = rows[1][:12] if len(rows) > 1 else []
    return meta


def main():
    ARTIFACT_DIR.mkdir(exist_ok=True, parents=True)
    archive = ARTIFACT_DIR / "source-temporary.zip"
    provenance = download(archive)
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise RuntimeError("CRC or ZIP content error")
        entries = [x for x in z.infolist() if not x.is_dir()]
        if len(entries) < 100:
            raise RuntimeError("unexpectedly few source files")
        counts = Counter(
            "/".join(PurePosixPath(x.filename).parts[:3]) for x in entries
        )
        # Every source item is inventoried, with contents only for bounded,
        # identifiable Oxalis and CV-related CSV metadata.
        interesting = [
            x for x in entries
            if x.filename.lower().endswith(".csv")
            and (
                "oxalis" in x.filename.lower()
                or "4-fold" in x.filename.lower()
                or "presence" in x.filename.lower()
                or "absence" in x.filename.lower()
                or "auc" in x.filename.lower()
            )
        ]
        previews = [source_preview(z, x) for x in interesting[:500]]
        manifest = {
            "source_doi": "10.5281/zenodo.19970795",
            "record_url": RECORD,
            "published_upstream_md5": UPSTREAM_MD5,
            "archive": provenance,
            "entries": len(entries),
            "top_level_paths": dict(counts.most_common(20)),
            "csv_candidates": len(interesting),
            "candidate_inventory": previews,
            "claims_not_made": [
                "matched CV/external AUC not yet reconstructed",
                "species predictions not yet rerun with Maxent",
                "independent external test design is not certified by a ZIP",
            ],
        }
    # The archive is not persisted with the receipt; upstream Zenodo and
    # SHA256 uniquely preserve raw provenance.
    archive.unlink()
    target = ARTIFACT_DIR / "matsui-zenodo-source-inventory.json"
    target.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print("MQR490_P8_ZENODO_MD5=" + provenance["md5"])
    print("MQR490_P8_ZENODO_FILES=" + str(len(entries)))
    print("MQR490_P8_CSV_CANDIDATES=" + str(len(interesting)))
    print("MQR490_P8_SOURCE_INVENTORY=PASS")
    print("MQR490_P8_REFERENCE_NORMALIZATION=NOT_YET_RECONSTRUCTED")


if __name__ == "__main__":
    main()
