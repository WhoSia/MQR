#!/usr/bin/env python3
from __future__ import annotations
import csv,sys
from pathlib import Path

HEAD=["lane","id","w_success","w_total","w_repeat_decoy","n_lineages","n_replicate_decoy",
      "i_invariant","i_total","i_rival_count_decoy","t_success","t_total","t_train_decoy",
      "d_covered","d_total","d_challenge_decoy"]

def score(path:Path):
    with path.open(encoding="utf-8",newline="") as f:
        r=csv.DictReader(f,delimiter="\t")
        if r.fieldnames!=HEAD:
            raise SystemExit("unexpected header")
        yield "id\tW\tN\tI\tT\tD"
        for row in r:
            lane=row["lane"]
            nden=4.0 if lane=="exact" else 64.0 if lane=="noisy" else None
            if nden is None: raise SystemExit(f"{row['id']}: bad lane")
            vals=[
                float(row["w_success"])/float(row["w_total"]),
                float(row["n_lineages"])/nden,
                float(row["i_invariant"])/float(row["i_total"]),
                float(row["t_success"])/float(row["t_total"]),
                float(row["d_covered"])/float(row["d_total"]),
            ]
            yield row["id"]+"\t"+"\t".join(f"{v:.6f}" for v in vals)

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("usage: calibration_reference.py PUBLIC.tsv")
    print("\n".join(score(Path(sys.argv[1]))))
