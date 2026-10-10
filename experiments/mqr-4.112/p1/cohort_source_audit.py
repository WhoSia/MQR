#!/usr/bin/env python3
"""Audit selected grains against the official 2021 author supplement."""
import csv, hashlib, io, json, pathlib, sys, zipfile

zip_path = pathlib.Path(sys.argv[1])
raw = zip_path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == "25d1129d2eea403dfd5f622dae74721420de223c03542d4e367ca2331bfb9228"
root = "PracticalGuideToBayLum_Data/"
with zipfile.ZipFile(io.BytesIO(raw)) as z:
    rmd = z.read(root+"PracticalGuideToBayLum.Rmd")
    assert hashlib.sha256(rmd).hexdigest() == "3b744bc5d069e111d742d8d20a331252c984bd834a3b3240756cb2d39e8603d8"
    text = rmd.decode("utf-8-sig")
    assert "example datasets have been considerably shortened" in text
    assert "do not include the full dataset of the samples FER1 and FER3" in text
    assert "Iter = 5000" in text and "n.chains = 3" in text
    selection = {}
    for fer in ("FER1","FER3"):
        b = z.read(root+"data/"+fer+"/DiscPos.csv")
        rows = list(csv.DictReader(io.StringIO(b.decode())))
        ids = [(int(row["position"]),int(row["grain"])) for row in rows]
        assert len(ids)==49 and len(set(ids))==49
        selection[fer] = {"example_grains":len(ids),"selection_sha256":hashlib.sha256(b).hexdigest()}
report = {"original_zip_sha256":hashlib.sha256(raw).hexdigest(),
          "author_rmd_sha256":hashlib.sha256(rmd).hexdigest(),
          "public_example":selection,"example_is_shortened":True,
          "published_full_cohort_same_as_example":"HOLD_UNPROVEN",
          "2021_author_parameters":{"iter":5000,"thin":5,"chains":3},
          "publication_FER3_HPD95_ka":[36.6,47.8]}
pathlib.Path("p1g_out").mkdir(exist_ok=True)
pathlib.Path("p1g_out/cohort.json").write_text(json.dumps(report,indent=2)+"\n")
print("P1G_SOURCE_CUSTODY_PASS; PUBLISHED_COHORT_IDENTITY_HOLD")
