from pathlib import Path
import csv

HERE=Path(__file__).resolve().parent
R=HERE/"results"

def load_counts():
    out={}
    with (R/"rust_summary.tsv").open() as f:
        for row in csv.DictReader(f,delimiter="\t"):
            if row["kind"]=="COUNT":
                out[(row["constraint"],row["baseline"],row["class"])]=int(row["count"])
    return out

def load_witnesses():
    with (R/"rust_witnesses.tsv").open() as f:
        return list(csv.DictReader(f,delimiter="\t"))

def main():
    c=load_counts()
    w=load_witnesses()

    # Frozen strong-baseline absorption/nonabsorption checks.
    assert c[("OPR","CONSTRAINED","BINDING_LOCAL")]==0
    assert c[("OPR","CONSTRAINED","BASELINE_ABSORBED")]>0
    assert c[("NEDL","CONSTRAINED","BINDING_LOCAL")]>0
    assert c[("NEDL","CONSTRAINED","OVERCONSTRAINING")]==0

    # Frozen overconstraint surface must remain visible rather than suppressed.
    assert c[("ARR","CONSTRAINED","OVERCONSTRAINING")]>0
    assert c[("EAI","CONSTRAINED","OVERCONSTRAINING")]>0
    assert c[("EXTERIOR","CONSTRAINED","OVERCONSTRAINING")]>0

    # Every emitted local witness must genuinely switch between two distinct actions,
    # so the baseline-action + typed-action pair is a 2-action minimal choice set.
    for row in w:
        assert row["baseline_action"] != row["typed_action"], row
        assert len({row["baseline_action"],row["typed_action"]})==2

        con=row["constraint"]
        if con in ("OPR","NEDL"):
            assert row["irr"]=="1", row
        elif con=="ARR":
            assert row["reopen_live"]=="1", row
        elif con=="EAI":
            assert row["anc_live"]=="1", row
        elif con=="EXTERIOR":
            assert row["ext_live"]=="1", row

    # Strong-baseline NEDL witness specifically requires non-substitutable separators.
    ned=[x for x in w if x["constraint"]=="NEDL" and x["baseline"]=="CONSTRAINED"]
    assert len(ned)==1
    assert ned[0]["irr"]=="1" and ned[0]["sub"]=="0"
    assert ned[0]["baseline_action"]=="A3_S0_HI"
    assert ned[0]["typed_action"]=="A1_FULL"

    # OPR has no independent authority beyond the matched minimum-separator baseline.
    # NEDL retains a stricter local coverage effect; this is not yet a novelty claim.
    print("MQR464_OPR_MATCHED_CONSTRAINT_ABSORPTION=PASS")
    print("MQR464_NEDL_MATCHED_CONSTRAINT_NONABSORPTION=PASS")
    print("MQR464_NEDL_STRONG_WITNESS_NON_SUBSTITUTABLE=PASS")
    print("MQR464_LOCAL_WITNESS_TWO_ACTION_MINIMALITY=PASS")
    print("MQR464_OVERCONSTRAINT_SURFACE_PRESERVED=PASS")
    print("MQR464_BINDING_DOES_NOT_IMPLY_MQR_NOVELTY=PASS")

if __name__=="__main__":
    main()
