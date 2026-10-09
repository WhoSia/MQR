#!/usr/bin/env python3
"""MQR-4.99 P2 original Zenodo custody: metadata/CSV counts, not ecological inference."""
import csv, hashlib, io, json, pathlib, sys, zipfile
from collections import Counter
SHA="279a67cf8c763a1ba5166497ed223ac5feb656b5a6e7f110dae3c0d1a11e001d"
MD5="186026a0b887cb2ed953d9030dda836c"
FILES={
"amro_obsdetection.csv":("274a466d00b5eb58146515cbab76575a69e927c37dec48fdabc1dd1a16a3f208",2090),
"amro_sitecovs_simplified.csv":("ef047fd2c5ada813f42fbde8f4e5bd4a19ae52e9cb191454c43962df5ab84647",2912),
"amro_ebird_simplified.csv":("7505768fe88ac09d597a2ad590f85725c9e69586b3edbe855c566e8a61771307",1059),
"env_centroids.csv":("143473ef293852d79c7b1243cf0df8072924602ea545ca681c66a480af690ffc",7227)}
def sha(data,algorithm="sha256"):
 return hashlib.new(algorithm,data).hexdigest()
def run(archive,dest):
 dest=pathlib.Path(dest);dest.mkdir(parents=True,exist_ok=True)
 raw=pathlib.Path(archive).read_bytes()
 assert sha(raw)==SHA and sha(raw,"md5")==MD5,"ZIP fixity mismatch"
 frames={};inv={}
 ext=dest/"extracted";ext.mkdir(exist_ok=True)
 with zipfile.ZipFile(io.BytesIO(raw)) as z:
  paths=z.namelist()
  assert len(paths)==26,"Unexpected source archive entry count"
  for filename,(hash_expected,numrows) in FILES.items():
   matches=[p for p in paths if p.endswith("/data/"+filename)]
   assert len(matches)==1,("ambiguous",filename)
   blob=z.read(matches[0]);assert sha(blob)==hash_expected,(filename,"SHA mismatch")
   rec=list(csv.DictReader(io.StringIO(blob.decode("utf-8-sig")),delimiter=";"))
   assert len(rec)==numrows,(filename,len(rec))
   frames[filename]=rec;inv[filename]={"sha256":hash_expected,"rows":len(rec),"bytes":len(blob),"columns":list(rec[0])}
   (ext/filename).write_bytes(blob)
  readme=[p for p in paths if p.endswith("/README.md")]
  assert len(readme)==1
  (ext/"ORIGINAL_README.md").write_bytes(z.read(readme[0]))
 ds=frames["amro_obsdetection.csv"];site=frames["amro_sitecovs_simplified.csv"];eb=frames["amro_ebird_simplified.csv"]
 ids={r["Checklist_ID"] for r in site};counts=Counter(r["Checklist_ID"] for r in ds)
 missing=[r for r in ds if r["Checklist_ID"] not in ids]
 summary={
  "raw_ds_histories":len(ds),
  "ds_le_300m":sum(float(r["Distance"])<=300 for r in ds),
  "ds_gt_300m":sum(float(r["Distance"])>300 for r in ds),
  "site_visits":len(site),"site_count_sum":sum(int(r["Count"]) for r in site),
  "site_zero_rows":sum(int(r["Count"])==0 for r in site),
  "orphan_ds_rows":len(missing),"orphan_ds_years":dict(Counter(r["Year"] for r in missing)),
  "site_key_disagreements":sum(int(r["Count"])!=counts[r["Checklist_ID"]] for r in site),
  "ebird_visits":len(eb),"ebird_sum":sum(int(r["count"]) for r in eb),
  "ebird_positive_visits":sum(int(r["count"])>0 for r in eb)}
 expected={"raw_ds_histories":2090,"ds_le_300m":2020,"ds_gt_300m":70,"site_visits":2912,"site_count_sum":2076,"site_zero_rows":1498,"orphan_ds_rows":14,"orphan_ds_years":{"11":14},"site_key_disagreements":0,"ebird_visits":1059,"ebird_sum":819,"ebird_positive_visits":440}
 assert summary==expected,(summary,expected)
 result={"record_doi":"10.5281/zenodo.10666980","article_doi":"10.1002/ecy.4292","archive_sha256":SHA,"archive_md5":MD5,"source_role":"original independent collection; availability ground truth not directly observed","files":inv,"summary":summary}
 (dest/"source_audit.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,sort_keys=True))
if __name__=="__main__":
 assert len(sys.argv)==3,"Usage: source_audit.py ZIP OUT"
 run(sys.argv[1],sys.argv[2])
