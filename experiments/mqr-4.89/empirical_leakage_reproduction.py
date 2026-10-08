"""MQR-4.89 reproducible synthetic leakage experiments.

NOT a replay of Kapoor and Narayanan (2023) civil-war data or models.
Four deliberately designed leakage mechanisms, paired with controlled alternatives.
"""
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from hashlib import sha256
from statistics import mean
import numpy as np
from scipy.special import expit
from sklearn.model_selection import train_test_split, GroupShuffleSplit
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

@dataclass(frozen=True)
class Result:
    mechanism: str
    seed: int
    invalid_auc: float
    controlled_auc: float
    category: str

def auc(y, m, X):
    return float(roc_auc_score(y, m.predict_proba(X)[:,1]))

def proxy_case(seed):
    rng=np.random.default_rng(seed)
    X=rng.normal(size=(1100,12))
    y=rng.binomial(1,expit(X[:,0]-.7*X[:,1]+.65*X[:,2]+.6*rng.normal(size=1100)))
    proxy=y.copy();flip=rng.random(len(y))<.025;proxy[flip]=1-proxy[flip]
    tr,te=train_test_split(np.arange(len(y)),test_size=.3,stratify=y,random_state=seed)
    badX=np.column_stack((X,proxy))
    good=LogisticRegression(max_iter=800).fit(X[tr],y[tr])
    bad=LogisticRegression(max_iter=800).fit(badX[tr],y[tr])
    return Result("target_proxy",seed,auc(y[te],bad,badX[te]),auc(y[te],good,X[te]),"L2")

def full_selection_case(seed):
    rng=np.random.default_rng(seed+35000)
    n,p=180,1400
    y=rng.integers(0,2,n); X=rng.standard_normal((n,p))
    tr,te=train_test_split(np.arange(n),test_size=.45,stratify=y,random_state=seed)
    def features(rows):
        yy=y[rows]*2-1
        return np.argsort(np.abs(X[rows].T@yy))[-7:]
    bad_cols,good_cols=features(np.arange(n)),features(tr)
    bad=LogisticRegression(max_iter=1000).fit(X[tr][:,bad_cols],y[tr])
    good=LogisticRegression(max_iter=1000).fit(X[tr][:,good_cols],y[tr])
    return Result("whole_data_feature_selection",seed,auc(y[te],bad,X[te][:,bad_cols]),
                  auc(y[te],good,X[te][:,good_cols]),"L1.3")

def group_case(seed):
    rng=np.random.default_rng(seed+70000)
    groups=np.repeat(np.arange(160),7)
    gy=np.array([0,1]*80);rng.shuffle(gy);y=gy[groups]
    X=OneHotEncoder(handle_unknown='ignore').fit_transform(groups.reshape(-1,1))
    tr,te=train_test_split(np.arange(len(y)),test_size=.3,stratify=y,random_state=seed)
    gtr,gte=next(GroupShuffleSplit(n_splits=1,test_size=.3,random_state=seed).split(X,y,groups))
    assert not (set(groups[gtr])&set(groups[gte]))
    def eval_(a,b):
        model=LogisticRegression(C=30,max_iter=2000).fit(X[a],y[a])
        return auc(y[b],model,X[b])
    return Result("repeated_entity_rows",seed,eval_(tr,te),eval_(gtr,gte),"L3.2")

def future_case(seed):
    rng=np.random.default_rng(seed+123456)
    n=1100
    t=np.arange(n)
    future=t>=880
    x=rng.standard_normal(n)
    y=rng.binomial(1,expit(2.6*np.where(future,-x,x)))
    X=np.column_stack((x,future.astype(float)))
    tr,te=train_test_split(t,test_size=.2,stratify=y,random_state=seed)
    past=np.flatnonzero(~future);later=np.flatnonzero(future)
    assert tr.max()>=later.min() and past.max()<later.min()
    def eval_(a,b):
        model=RandomForestClassifier(n_estimators=70,max_depth=5,min_samples_leaf=10,
                                     n_jobs=1,random_state=seed).fit(X[a],y[a])
        return auc(y[b],model,X[b])
    return Result("temporal_future_exposure",seed,eval_(tr,te),eval_(past,later),"L3.1")

def run(n_seeds=12):
    import argparse
    funcs=[proxy_case,full_selection_case,group_case,future_case]
    all_rows=[]
    for fn in funcs:
        all_rows.extend(fn(100+i) for i in range(n_seeds))
    summaries=[]
    for fn in funcs:
        rows=[r for r in all_rows if r.mechanism==fn(100).mechanism]
        summaries.append(dict(mechanism=rows[0].mechanism,category=rows[0].category,
            invalid_mean=mean(r.invalid_auc for r in rows),
            controlled_mean=mean(r.controlled_auc for r in rows)))
    output=dict(evidence_class="SYNTHETIC_ML_EXECUTION_NOT_CIVIL_WAR_REPLAY",
                source_doi="10.1016/j.patter.2023.100804",seed_start=100,
                trials=[asdict(r) for r in all_rows],summary=summaries)
    raw=(json.dumps(output,indent=2,sort_keys=True)+"\n").encode()
    Path("mqr489_experiment_results.json").write_bytes(raw)
    assert len(all_rows)==4*n_seeds
    print("MQR489_EXECUTED_SYNTHETIC_TRIALS="+str(len(all_rows)))
    for row in summaries:
        print(row["mechanism"],round(row["invalid_mean"],3),
              round(row["controlled_mean"],3))
    print("MQR489_RESULT_SHA256="+sha256(raw).hexdigest())
    print("MQR489_ORIGINAL_DATA_REPLICATION=NOT_PERFORMED")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--seeds",type=int,default=12)
    run(parser.parse_args().seeds)
