#!/usr/bin/env python3
"""MQR-4.100 P4: published UCI HAR paired accelerometer/gyroscope windows.
Retrospective, non-novel source audit. No instrument independence or risk transfer.
Python stdlib only. Source is the official double-ZIP, pinned by SHA-256.
"""
import collections
import hashlib
import io
import json
import math
import pathlib
import random
import statistics
import sys
import zipfile

URL = "https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip"
OUTER_SHA256 = "c00b803081a5c797cd5e4b83700a9810b38d53d9d84e01917e090e1fdbc81031"
INNER_SHA256 = "2045e435c955214b38145fb5fa00776c72814f01b203fec405152dac7d5bfeb0"
N = {"train": 7352, "test": 2947}
SENSORS = ("total_acc", "body_gyro")
AXES = ("x", "y", "z")
def sha(raw):
    return hashlib.sha256(raw).hexdigest()
def mean(a):
    return sum(a)/len(a)
def features(data):
    out=[]
    for line in io.BytesIO(data):
        row=[float(v) for v in line.split()]
        assert len(row)==128 and all(math.isfinite(v) for v in row), "Invalid 128-sample sensor window"
        m=mean(row)
        std=math.sqrt(mean([(x-m)**2 for x in row]))
        out.append((m,std))
    return out
def source(z,part):
    p="UCI HAR Dataset/"+part
    return z.read(p)
def signals(z,split):
    n=N[split]
    y=[int(v) for v in source(z,f"{split}/y_{split}.txt").splitlines()]
    subject=[int(v) for v in source(z,f"{split}/subject_{split}.txt").splitlines()]
    assert len(y)==len(subject)==n
    assert set(y)==set(range(1,7)), "Six activity labels expected in both splits"
    assert len(set(subject))==({"train":21,"test":9}[split])
    matrix=[[None]*12 for _ in range(n)]
    custody={}
    for sensor_i,sensor in enumerate(SENSORS):
        for axis_i,axis in enumerate(AXES):
            name=f"{split}/Inertial Signals/{sensor}_{axis}_{split}.txt"
            b=source(z,name)
            custody[name]={"sha256":sha(b),"bytes":len(b)}
            ff=features(b)
            assert len(ff)==n, f"Unequal window count: {name}"
            for i,(mu,sd) in enumerate(ff):
                matrix[i][sensor_i*6+axis_i*2]=mu
                matrix[i][sensor_i*6+axis_i*2+1]=sd
    assert all(all(v is not None for v in row) for row in matrix)
    return {"subjects":subject,"activity":y,"features":matrix,"custody":custody}
def cls(pred,correct):
    return sum(v==w for v,w in zip(pred,correct))
def classifier(train,test,include_gyro,gyro_override=None):
    xt=train["features"]
    train_y=train["activity"]
    class_ids=sorted(set(train_y))
    idx=list(range(12 if include_gyro else 6))
    stdev=[]
    for j in idx:
        vs=[v[j] for v in xt];avg=mean(vs)
        sd=math.sqrt(mean([(v-avg)**2 for v in vs]))
        assert sd>0,("constant train variable",j)
        stdev.append(sd)
    centers={}
    for c in class_ids:
        subset=[r for r,y in zip(xt,train_y) if y==c]
        centers[c]=[mean([row[j] for row in subset]) for j in idx]
    preds=[]
    for row_i,row in enumerate(test["features"]):
        if gyro_override is not None:
            vals=row[:6]+gyro_override[row_i][6:]
        else: vals=row
        preds.append(min(class_ids,key=lambda c:(
            sum(((vals[j]-centers[c][k])/stdev[k])**2 for k,j in enumerate(idx)),c)))
    return preds
def p4(a,out):
    raw=pathlib.Path(a).read_bytes()
    assert sha(raw)==OUTER_SHA256, "Outer UCI official ZIP drift"
    with zipfile.ZipFile(io.BytesIO(raw)) as outer:
        inner=outer.read("UCI HAR Dataset.zip")
    assert sha(inner)==INNER_SHA256, "Inner original UCI dataset ZIP drift"
    with zipfile.ZipFile(io.BytesIO(inner)) as z:
        tr=signals(z,"train");te=signals(z,"test")
        labels=z.read("UCI HAR Dataset/activity_labels.txt").decode("utf8")
        readme=z.read("UCI HAR Dataset/README.txt").decode("utf8",errors="replace")
    assert "WALKING" in labels and "LAYING" in labels
    assert "gyroscope" in readme and "accelerometer" in readme
    trainset=set(tr["subjects"]);testset=set(te["subjects"])
    assert not trainset.intersection(testset),"Subject-level leakage between two UCI splits"
    pred_a=classifier(tr,te,False)
    pred_j=classifier(tr,te,True)
    correct=te["activity"]
    ac=cls(pred_a,correct);jc=cls(pred_j,correct)
    gain=sum(x!=y and z==y for x,z,y in zip(pred_a,pred_j,correct))
    loss=sum(x==y and z!=y for x,z,y in zip(pred_a,pred_j,correct))
    assert jc-ac==gain-loss
    # Strictly a synthetic pairing disruption; does NOT hold P(Z|activity) fixed.
    perm=[te["features"][(i+17)%len(correct)] for i in range(len(correct))]
    perm_pred=classifier(tr,te,True,gyro_override=perm)
    subj=collections.defaultdict(list)
    for i,s in enumerate(te["subjects"]):
        subj[s].append(i)
    per_subj={}
    for s,ixs in sorted(subj.items()):
        per_subj[str(s)]={"n":len(ixs),
             "acc_correct":sum(pred_a[i]==correct[i] for i in ixs),
             "joint_correct":sum(pred_j[i]==correct[i] for i in ixs)}
    rng=random.Random(4100)
    unique=sorted(subj)
    reps=[]
    for _ in range(2000):
        sample=[rng.choice(unique) for j in unique]
        ids=[i for s in sample for i in subj[s]]
        reps.append(sum(int(pred_j[i]==correct[i])-int(pred_a[i]==correct[i]) for i in ids)/len(ids))
    reps.sort()
    output={
        "doi":"10.24432/C54S4K","url":URL,
        "original_source":"UCI HAR (Anguita/Reyes-Ortiz et al.), 2012 windowed inertial signals",
        "outer_bytes":len(raw),"outer_sha256":sha(raw),"inner_bytes":len(inner),"inner_sha256":sha(inner),
        "sensor_A":"total_acc x/y/z (accelerometer including gravity)",
        "sensor_B":"body_gyro x/y/z (gyroscope, rad/s)",
        "pairing_authority":"same split and window index in original UCI archive; subject ID and activity label",
        "not_independent_evidence":"two physical sensors but common smartphone collection, overlapping windows, video-derived labels and same preprocessing",
        "train_windows":len(tr["activity"]),"test_windows":len(te["activity"]),
        "train_subjects":sorted(trainset),"test_subjects":sorted(testset),
        "disjoint_subject_ids":True,
        "training_activity_counts":dict(sorted(collections.Counter(tr["activity"]).items())),
        "test_activity_counts":dict(sorted(collections.Counter(correct).items())),
        "signal_sha256_and_size":{**tr["custody"],**te["custody"]},
        "feature_method":"each axis window population mean and population std, 6 features per modality, no cross-window fitting",
        "fixed_estimator":"nearest activity centroid normalized by pooled TRAIN feature SD; 6 activity classes; retrospective, not blind",
        "accelerometer_only_correct":ac,"accelerometer_plus_gyro_correct":jc,
        "gain_count":gain,"loss_count":loss,
        "test_paired_accuracy_delta":(jc-ac)/len(correct),
        "synthetic_gyro_shift_17_correct":cls(perm_pred,correct),
        "subject_cluster_descriptive_bootstrap_delta_95pct":[reps[49],reps[1949]],
        "cluster_bootstrap_draws":2000,"seed":4100,
        "test_per_subject":per_subj,
        "scientific_hold":"NOT an independently measured per-theta experiment kernel, unbiased target risk, measured sup-TV epsilon or generalizable causal benefit"
    }
    target=pathlib.Path(out)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(output,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print(json.dumps({k:output[k] for k in [
        "train_windows","test_windows","disjoint_subject_ids",
        "accelerometer_only_correct","accelerometer_plus_gyro_correct",
        "gain_count","loss_count","synthetic_gyro_shift_17_correct",
        "subject_cluster_descriptive_bootstrap_delta_95pct"]},sort_keys=True))
    print("MQR4100_P4_UCI_SOURCE_NATIVE_TWO_SENSOR_PAIRING=PASS;PARAMETER_IDENTIFICATION=HOLD")
if __name__=="__main__":
    if len(sys.argv)!=3:raise SystemExit("Usage: python p4_uci_har.py UCI_OFFICIAL_OUTER_ZIP AUDIT_JSON")
    p4(sys.argv[1],sys.argv[2])
