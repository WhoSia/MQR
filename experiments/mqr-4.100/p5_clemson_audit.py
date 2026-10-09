#!/usr/bin/env python3
"""MQR-4.100 internal P5: publisher-hosted synchronized triple-IMU stream / manually video-labelled event data.
This is DATA CUSTODY and CONSISTENCY only, NOT independent biological ground-truth verification.
Requires exact publisher Data.zip. Does not download credential-gated EDI data.
"""
import collections
import hashlib
import io
import json
import pathlib
import sys
import zipfile

SOURCE = "https://cecas.clemson.edu/tracking/Pedometer/Data.zip"
SHA256 = "ce37832d5e234f6f014193a3a2af2f3162ab90905f303d473849512d690885da"
SIZE = 31_661_301
PARTICIPANTS = tuple(f"P{i:03d}" for i in range(1,31))
CONDITIONS = ("Irregular", "Regular", "SemiRegular")
EVENTS = ("right", "left", "rightshift", "leftshift")
EXPECTED = {"Irregular":(7058,424608),"Regular":(31528,266802),"SemiRegular":(22215,260015)}
def check(path, output):
    b=pathlib.Path(path).read_bytes()
    assert len(b)==SIZE and hashlib.sha256(b).hexdigest()==SHA256, "Source fixture drift"
    with zipfile.ZipFile(io.BytesIO(b)) as z:
        assert len(z.namelist())==180, "Expected 90 data+90 video-ground-truth pairs"
        assert z.testzip() is None, "Corrupt ZIP members"
        count=collections.Counter()
        kinds=collections.Counter()
        lengths=collections.Counter()
        errors=[]
        dup_trials=[]
        per={}
        for condition in CONDITIONS:
            counts=0;rows_total=0
            for participant in PARTICIPANTS:
                prefix=f"{participant}/{condition}/"
                files=[n for n in z.namelist() if n.startswith(prefix)]
                datafile=[n for n in files if n.endswith(".txt") and not n.endswith("/steps.txt")]
                gtfile=[n for n in files if n.endswith("/steps.txt")]
                assert len(datafile)==len(gtfile)==1,(prefix,files)
                data=z.read(datafile[0])
                sample_lines=data.splitlines()
                assert sample_lines and all(len(line.split())==9 for line in sample_lines),datafile[0]
                assert all(len(line.split())==2 for line in z.read(gtfile[0]).splitlines() if line.strip())
                events=[line.split() for line in z.read(gtfile[0]).splitlines() if line.strip()]
                indices=[]
                for record in events:
                    idx=int(record[0]);event=record[1].decode("utf8")
                    assert event in EVENTS,(prefix,event)
                    kinds[event]+=1
                    count[condition]+=1
                    indices.append(idx)
                    if not (0<=idx<len(sample_lines)):
                        errors.append({"participant":participant,"condition":condition,"event_index":idx,
                            "sensor_rows":len(sample_lines),"event_type":event})
                if len(set(indices))!=len(indices):dup_trials.append((participant,condition))
                counts+=len(indices)
                rows_total+=len(sample_lines)
                lengths[(participant,condition)]=len(sample_lines)
            assert (counts,rows_total)==EXPECTED[condition],(condition,counts,rows_total)
            per[condition]={"annotated_event_records":counts,"sensor_sample_rows":rows_total}
        assert sum(count.values())==60801
        assert kinds==collections.Counter({"left":28319,"right":28349,"leftshift":2104,"rightshift":2029})
        assert len(errors)==2 and not dup_trials,errors
        assert {(e["participant"],e["condition"],e["event_index"]) for e in errors} == {
            ("P010","Regular",9233),("P019","Irregular",10092)}
        receipt={
            "source_url":SOURCE,"source_sha256":SHA256,"source_bytes":len(b),
            "archive_entries":len(z.namelist()),"participants":30,"conditions":list(CONDITIONS),
            "trial_data_groundtruth_pairs":90,"sensor_per_sample_columns":9,
            "column_semantics":"wrist xyz, hip xyz, ankle xyz; source says post synchronized to 15 Hz",
            "video_ground_truth_semantics":"annotations of left/right steps and left/right shifts; not independently re-annotated from video",
            "per_condition":per,"event_classes":dict(kinds),"events_in_archive":sum(count.values()),
            "ordinary_steps":kinds["right"]+kinds["left"],
            "shifts":kinds["rightshift"]+kinds["leftshift"],
            "out_of_range_ground_truth_events":errors,
            "duplicate_index_trials":dup_trials,
            "known_source_discrepancy":"Mattfeld 2018 describes 60,853 manually marked steps while this hosted Data.zip has 60,801 left/right/shift annotations. Source versions/definition may differ; cause NOT established.",
            "original_unsynchronized_sensor_streams":"separate RawData.zip at official project URL, 277 MB; not included",
            "original_video_review":"11GB Videos.zip available from publisher; NO manual re-annotation done",
            "security_contract":"only CI-authenticated TLS plus fixed SHA validates current GitHub retrieval; initial external interactive research used unverified TLS and cannot alone certify server identity",
            "scientific_limits":"two modalities are physical accelerometers across devices and manually reviewed video-derived labels; shared research workflow; annotation source not independently audited, some event IDs outside data rows; NO new causal sensor value or population risk inference"
        }
    target=pathlib.Path(output)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(receipt,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print(json.dumps({"source_bytes":len(b),"paired_trials":90,"n_records":receipt["events_in_archive"],
        "n_steps":receipt["ordinary_steps"],"n_shifts":receipt["shifts"],"n_out_of_range":len(errors),
        "error_examples":errors},sort_keys=True))
    print("MQR4100_CLEMSON_SOURCE_INDEXED_VIDEO_ANNOTATION_AUDIT_PASS;EVENT_VALIDITY_AND_REANNOTATION_HOLD")
if __name__=="__main__":
    if len(sys.argv)!=3:raise SystemExit("Usage: p5_clemson_audit.py DATA_ZIP RECEIPT")
    check(sys.argv[1],sys.argv[2])
