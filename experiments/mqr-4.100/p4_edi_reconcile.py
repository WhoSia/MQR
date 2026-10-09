#!/usr/bin/env python3
"""EDI v5/v5/v6 => published palmerpenguins combined-row lineage audit.
REQUIRES actually acquired original three EDI files. NOT run on merely
DOI-matched or reconstructed/palmerpenguins-partitioned surrogate files.
Exit nonzero and do not produce a fake PASS if any original is absent.
"""
import csv,hashlib,json,pathlib,sys,collections,decimal
DOIS={
 "Adelie":("knb-lter-pal.219.5","10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f"),
 "Gentoo":("knb-lter-pal.220.5","10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689"),
 "Chinstrap":("knb-lter-pal.221.6","10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e"),
}
NUMERIC={"Sample Number","Culmen Length (mm)","Culmen Depth (mm)",
         "Flipper Length (mm)","Body Mass (g)","Delta 15 N (o/oo)","Delta 13 C (o/oo)"}
def read(path):
    data=pathlib.Path(path).read_bytes()
    rows=list(csv.DictReader(data.decode("utf-8-sig").splitlines()))
    assert rows and all(None not in r for r in rows),f"Malformed CSV: {path}"
    return rows,hashlib.sha256(data).hexdigest(),len(data)
def canon(k,v):
    v=(v or "").strip()
    if v in ("NA","N/A",".",""):return None
    if k in NUMERIC:
        try:return str(decimal.Decimal(v).normalize())
        except decimal.InvalidOperation:return v
    return v
def key(r):
    return (r["studyName"],r["Individual ID"])
def main():
    if len(sys.argv)!=6:raise SystemExit(
      "Usage: edi_reconcile.py ORIGINAL_PENGUINS_RAW_CSV ORIGINAL_EDI_ADELIE_V5 ORIGINAL_EDI_GENTOO_V5 ORIGINAL_EDI_CHINSTRAP_V6 RECEIPT_JSON"
    )
    combined,csha,cbytes=read(sys.argv[1])
    assert len(combined)==344,"Not expected pinned 344-row combined target"
    fields=list(combined[0])
    assert len(fields)==17
    combined_species={}
    for row in combined:
        name=row["Species"].split(" ")[0].capitalize()
        combined_species.setdefault(name,[]).append(row)
    results={}
    for sp,p in zip(["Adelie","Gentoo","Chinstrap"],sys.argv[2:5]):
        if not pathlib.Path(p).exists():raise FileNotFoundError(f"ORIGINAL EDI VERSION REQUIRED, not a reconstructed surrogate: {sp} {p}")
        rows,sha,size=read(p)
        assert all(r["Species"].split(" ")[0].capitalize()==sp for r in rows),"Incorrect species source"
        combined_subset=combined_species[sp]
        cols=set(fields)&set(rows[0])
        if set(fields)!=set(rows[0]):
            results[sp]={"status":"SCHEMA_MISMATCH","orig_columns":list(rows[0]),"combined_columns":fields}
            continue
        def bucket(rr):
            return collections.defaultdict(list,{
              k:[r for r in rr if key(r)==k] for k in set(map(key,rr))
            })
        lhs=bucket(rows);rhs=bucket(combined_subset)
        missing=sorted(set(lhs)-set(rhs));extra=sorted(set(rhs)-set(lhs))
        diffs=[]
        for ident in set(lhs)&set(rhs):
            if len(lhs[ident])!=1 or len(rhs[ident])!=1:
                diffs.append({"id":ident,"reason":"DUPLICATE_KEY","edi":len(lhs[ident]),"combined":len(rhs[ident])});continue
            a,b=lhs[ident][0],rhs[ident][0]
            fields_bad=[f for f in fields if canon(f,a[f])!=canon(f,b[f])]
            if fields_bad:diffs.append({"id":ident,"mismatched_fields":fields_bad})
        results[sp]={"package":DOIS[sp][0],"doi":DOIS[sp][1],
                     "edi_file_sha256":sha,"edi_bytes":size,"edi_rows":len(rows),
                     "combined_species_rows":len(combined_subset),
                     "missing_edi_keys_in_combined":len(missing),
                     "combined_keys_not_in_edi":len(extra),
                     "same_key_cell_disagreements":len(diffs),
                     "examples":diffs[:12],"status":"EXACT_NORMALIZED_LINEAGE_PASS" if
                     not missing and not extra and not diffs and len(rows)==len(combined_subset)
                     else "LINEAGE_MISMATCH_REQUIRES_REVIEW"}
    receipt={"combined_rows":len(combined),"combined_sha256":csha,"combined_bytes":cbytes,
             "source_type":"THREE ORIGINAL EDI FILES MUST BE OBTAINED DIRECTLY WITH VERSION PROVENANCE",
             "method":"same species + studyName + Individual ID; compare 17 attributes, numeric Decimal normalized",
             "results":results}
    pathlib.Path(sys.argv[5]).write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({sp:r.get("status") for sp,r in results.items()}))
    if any(r["status"]!="EXACT_NORMALIZED_LINEAGE_PASS" for r in results.values()):
        raise SystemExit("EDI_ORIGINAL_LINEAGE_HOLD: inspect all mismatches; no automatic source correction")
    print("EDI_THREE_VERSION_ORIGINAL_LINEAGE_PASS")
if __name__=="__main__":main()
