#!/usr/bin/env python3
"""MQR-4.100 P7 — source-native, retrospective event detection vs VIDEO-DERIVED annotations.

Distinct physical sensor sites ≠ independent errors; publisher-supplied video annotations
≠ independently reannotated truth. This is heldout classifier/event loss, NOT a
parameter-identification or cross-population transport theorem.

Uses only numpy and Python standard library. Byte-pinned original Clemson Data.zip.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, io, itertools, json, pathlib, zipfile
import numpy as np

EXPECTED_SHA='ce37832d5e234f6f014193a3a2af2f3162ab90905f303d473849512d690885da'
CONDS=('Regular','SemiRegular','Irregular')
SITES=('wrist','hip','ankle')
GRID=[(float(t),int(d)) for t in (1.5,2.5,3.5,5.0) for d in (4,6,8)]


def match(pred: np.ndarray, gold: np.ndarray, tau:int):
    i=j=0;matches=[]
    while i<len(pred) and j<len(gold):
        if int(pred[i])<int(gold[j])-tau:i+=1
        elif int(gold[j])<int(pred[i])-tau:j+=1
        else:
            matches.append((i,j));i+=1;j+=1
    return matches


def build_peaks(sig, med, mad, t, d):
    candidates=np.flatnonzero((sig[1:-1]>sig[:-2]) & (sig[1:-1]>=sig[2:]) & (sig[1:-1]>med+t*mad))+1
    order=candidates[np.argsort(-sig[candidates],kind='stable')]
    marks=np.zeros(len(sig),dtype=bool);chosen=[]
    for idx in order:
        if not marks[max(0,idx-d+1):min(len(sig),idx+d)].any():
            chosen.append(int(idx));marks[idx]=True
    return np.array(sorted(chosen),dtype=np.int32)


def trace(data):
    arr=np.loadtxt(io.BytesIO(data),dtype=np.float64)
    assert arr.ndim==2 and arr.shape[1]==9 and len(arr)>15
    output=[]
    for i in range(3):
        v=arr[:,3*i:3*i+3]
        mag=np.sqrt(np.sum(v*v,axis=1))
        smooth=np.convolve(mag,np.ones(13)/13,mode='same')
        sig=np.abs(mag-smooth)
        sig[:7]=0;sig[-7:]=0
        signal=sig[7:-7]
        med=float(np.median(signal));mad=float(np.median(np.abs(signal-med)))
        output.append((sig,med,max(mad,1e-6)))
    return output,len(arr)


def load(z):
    out=[];anom=[];total_counter=collections.Counter()
    assert len(z.namelist())==180
    assert z.testzip() is None
    for pid in range(1,31):
        for cond in CONDS:
            prefix=f'P{pid:03d}/{cond}/'
            sensor=[n for n in z.namelist() if n.startswith(prefix) and n.endswith('.txt') and not n.endswith('steps.txt')]
            assert len(sensor)==1,(prefix,sensor)
            signal,nrows=trace(z.read(sensor[0]))
            parsed=[line.split() for line in z.read(prefix+'steps.txt').decode('utf8').splitlines() if line.strip()]
            assert all(len(x)==2 and x[1] in ('left','right','leftshift','rightshift') for x in parsed)
            gold=[];shifts=[]
            for raw_idx,kind in parsed:
                idx=int(raw_idx);total_counter[kind]+=1
                if not (0<=idx<nrows):anom.append({'id':pid,'condition':cond,'event':kind,'time_index':idx,'samples':nrows});continue
                (gold if kind in ('left','right') else shifts).append(idx)
            assert all(a<b for a,b in zip(gold,gold[1:])),'Events must be in source order'
            out.append({'id':pid,'cond':cond,'n':nrows,'signals':signal,'steps':np.array(gold,dtype=np.int32),'shifts':np.array(shifts,dtype=np.int32)})
    assert len(out)==90
    assert total_counter=={'left':28319,'right':28349,'leftshift':2104,'rightshift':2029}
    assert anom==[{'id':10,'condition':'Regular','event':'leftshift','time_index':9233,'samples':9192}, {'id':19,'condition':'Irregular','event':'leftshift','time_index':10092,'samples':9968}]
    return out,anom,total_counter


def compute_court(input_path, output_dir):
    source=pathlib.Path(input_path).read_bytes()
    assert hashlib.sha256(source).hexdigest()==EXPECTED_SHA
    out=pathlib.Path(output_dir);out.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(source)) as z: trials, anomalies,counts=load(z)
    # Participant-split deterministic: all tuning on P001–P015, all test on P016–P030.
    tr=[a for a in trials if a['id']<=15];te=[a for a in trials if a['id']>=16]
    def candidate(a,site,param):
        if param not in a.setdefault('cache',[{} for _ in SITES])[site]:
            a['cache'][site][param]=build_peaks(*a['signals'][site],*param)
        return a['cache'][site][param]
    def counts_for(subset,site,param,tau=3,accept_shift=False):
        m=n_pred=n_true=0
        for trial in subset:
            event=trial['steps']
            if accept_shift:event=np.sort(np.concatenate([trial['steps'],trial['shifts']]))
            predicted=candidate(trial,site,param)
            m+=len(match(predicted,event,tau));n_pred+=len(predicted);n_true+=len(event)
        return {'tp':m,'fn':n_true-m,'fp':n_pred-m,'gt':n_true,'det':n_pred}
    chosen=[];training=[]
    for site in range(3):
        candidates=[]
        for param in GRID:
            c=counts_for(tr,site,param)
            loss=c['fp']+c['fn']
            candidates.append((loss,c['fn'],c['fp'],param))
        # pre-specified objective FN+FP, tie break lower FN, lower FP, then (t,d)
        candidates.sort(key=lambda x:(x[0],x[1],x[2],x[3]))
        chosen.append(candidates[0][-1]);training.append({'site':SITES[site],'t':chosen[-1][0],'d':chosen[-1][1],'train_best_loss':candidates[0][0]})
    def evaluate_predictions(pred, gold, tau=3):
        m=match(pred,gold,tau);TP=len(m)
        return {'tp':TP,'fn':len(gold)-TP,'fp':len(pred)-TP,'gt':len(gold),'det':len(pred)}
    # Union fusion: time-ordered union of peaks from selected sensors,
    # merge candidate peaks less than or equal to 3 frames apart by picking earliest
    # raw candidate position. No use of labels in fusion.
    def union(preds, merge=3):
        arr=np.sort(np.concatenate(preds))
        if len(arr)==0:return arr
        result=[int(arr[0])];last=int(arr[0]);prev=int(arr[0]);grp=[]
        clusters=[[int(arr[0])]]
        for val in arr[1:]:
            val=int(val)
            if val-clusters[-1][0]<=merge:clusters[-1].append(val)
            else:clusters.append([val])
        return np.array([int(np.median(g)) for g in clusters],dtype=np.int32)
    def intersect(a,b,tau=3):
        m=match(a,b,tau)
        return np.array([int(round((int(a[i])+int(b[j]))/2)) for i,j in m],dtype=np.int32)
    policies={
        'wrist':(0,), 'hip':(1,), 'ankle':(2,),
        'wrist_or_hip':(0,1),'wrist_or_ankle':(0,2),'hip_or_ankle':(1,2),
        'any_three':(0,1,2),'wrist_and_hip':(0,1)
    }
    per_rows=[]; detail=collections.defaultdict(lambda:collections.Counter())
    pairs_overlap=[]
    for a in te:
        preds=[candidate(a,i,chosen[i]) for i in range(3)]
        fused={SITES[i]:preds[i] for i in range(3)}
        for name,ix in policies.items():
            if name in fused:continue
            fused[name]=intersect(preds[0],preds[1]) if name=='wrist_and_hip' else union([preds[i] for i in ix])
        for name,pred in fused.items():
            for tau in (2,3,4):
                for shifts in ([False,True] if tau==3 else [False]):
                    gold=np.sort(np.concatenate([a['steps'],a['shifts']])) if shifts else a['steps']
                    c=evaluate_predictions(pred,gold,tau)
                    row={'person':a['id'],'condition':a['cond'],'policy':name,'tolerance_samples':tau,
                        'label_definition':'steps_plus_shifts' if shifts else 'left_right_steps_only',**c}
                    per_rows.append(row)
        # Error overlap among distinct sensors, CONDITIONAL ON VIDEO-LABELLED EVENTS,
        # not independent of gait, participant or shared annotation errors.
        matches=[]
        for pred in preds:
            matched={j for i,j in match(pred,a['steps'],3)}
            matches.append(matched)
        for x,y in ((0,1),(0,2),(1,2)):
            joint=len(matches[x]&matches[y]);nx=len(matches[x]);ny=len(matches[y]);n=len(a['steps'])
            pairs_overlap.append({'participant':a['id'],'condition':a['cond'], 'sensor_pair':SITES[x]+'_'+SITES[y],
                'steps':n,'detected_x':nx,'detected_y':ny,'detected_by_both':joint,
                'frechet_lower':max(0,nx+ny-n),'frechet_upper':min(nx,ny),
                'empirical_overlap_under_independence':nx*ny/n if n else 0})
    def summary(rows):
        c=collections.Counter()
        for row in rows:
            for k in ('tp','fp','fn','gt','det'):c[k]+=row[k]
        c=dict(c);c['loss_fp_plus_fn_per_video_step']=(c['fn']+c['fp'])/c['gt'] if c['gt'] else 0
        c['recall']=c['tp']/c['gt'] if c['gt'] else 0
        c['precision']=c['tp']/c['det'] if c['det'] else 0
        return c
    totals={}
    for policy in policies:
        subset=[r for r in per_rows if r['policy']==policy and r['tolerance_samples']==3 and r['label_definition']=='left_right_steps_only']
        totals[policy]=summary(subset)
    by_cond={}
    for condition in CONDS:
        by_cond[condition]={p:summary([r for r in per_rows if r['condition']==condition and r['policy']==p and r['tolerance_samples']==3 and r['label_definition']=='left_right_steps_only']) for p in policies}
    by_participant={}
    for pid in range(16,31):
        by_participant[str(pid)]={p:summary([r for r in per_rows if r['person']==pid and r['policy']==p and r['tolerance_samples']==3 and r['label_definition']=='left_right_steps_only']) for p in policies}
    sensitivity={}
    for tau in (2,3,4):
        sensitivity[str(tau)]={p:summary([r for r in per_rows if r['policy']==p and r['tolerance_samples']==tau and r['label_definition']=='left_right_steps_only']) for p in policies}
    shift_definition={p:summary([r for r in per_rows if r['policy']==p and r['tolerance_samples']==3 and r['label_definition']=='steps_plus_shifts']) for p in policies}
    overlap_totals={}
    for pair in ('wrist_hip','wrist_ankle','hip_ankle'):
        rows=[r for r in pairs_overlap if r['sensor_pair']==pair]
        c={k:sum(r[k] for r in rows) for k in ('steps','detected_x','detected_y','detected_by_both','frechet_lower','frechet_upper','empirical_overlap_under_independence')}
        c['det_x_rate']=c['detected_x']/c['steps'];c['det_y_rate']=c['detected_y']/c['steps'];c['both_rate']=c['detected_by_both']/c['steps']
        c['independent_pooled_expected_overlap']=c['det_x_rate']*c['det_y_rate']*c['steps']
        overlap_totals[pair]=c
    # Descriptive subject bootstrap, no claim to new-population CI, explicitly clustered by participant
    rng=np.random.default_rng(4100)
    bootstrap={}
    for competitor in ('wrist','hip','ankle','any_three','wrist_or_ankle','wrist_and_hip'):
        if competitor=='hip':continue
        vals=[]
        for _ in range(2000):
            sample=rng.choice(np.arange(16,31),size=15,replace=True)
            aa=collections.Counter();bb=collections.Counter()
            for ident in sample:
                u=by_participant[str(ident)]['hip'];v=by_participant[str(ident)][competitor]
                for k in ('fp','fn','gt'):aa[k]+=u[k];bb[k]+=v[k]
            vals.append((bb['fn']+bb['fp'])/bb['gt']-(aa['fn']+aa['fp'])/aa['gt'])
        bootstrap[competitor]={'delta_vs_hip_loss_per_video_step':totals[competitor]['loss_fp_plus_fn_per_video_step']-totals['hip']['loss_fp_plus_fn_per_video_step'],
            'subject_bootstrap_descriptive_percentile_95':[float(np.quantile(vals,.025)),float(np.quantile(vals,.975))]}
    result={'source_sha256':EXPECTED_SHA,'publisher':'Clemson Pedometer Evaluation Project',
        'source_url':'https://cecas.clemson.edu/tracking/Pedometer/Data.zip',
        'comparison_kind':'predeclared-within-this-exploratory-analysis, not preregistered before dataset inspection',
        'sampling_hz':15,'participant_train':'P001-P015','participant_test':'P016-P030',
        'train_trials':len(tr),'test_trials':len(te),'tuning_objective':'min(FP+FN), matched to video left/right step times within ±3 samples; pooled training trials; 12 threshold/refractory candidates per sensor; no test labels for tuning',
        'site_order':list(SITES),'threshold_grid':GRID,'parameters':training,
        'anomalous_source_annotations':anomalies,'source_counts':dict(counts),
        'test_reference_count':sum(len(a['steps']) for a in te),
        'primary_label_definition':'left_right_steps_only; shift annotations excluded from positives (could become FP), source-reported ambiguous step semantics',
        'primary_tolerance_frames':3,'primary_tolerance_seconds':.2,
        'primary_target':'observed video annotation events in heldout participants; NOT latent true gait events or Bayes risk',
        'primary_cost':'(FN+FP)/annotated-video-steps. not a bounded 0-1 Bayes risk, may exceed 1',
        'total_metrics':totals,'by_condition':by_cond,'per_test_participant':by_participant,
        'tolerance_sensitivity':sensitivity,'shifts_as_events_sensitivity':shift_definition,
        'conditional_error_overlap':overlap_totals,'paired_event_overlap_table':pairs_overlap,
        'subject_cluster_descriptive_bootstrap':bootstrap,
        'limitations':['3 separate physical sensors but within SAME study/clinical video labeling workflow; no independently reannotated video','sensor signals resampled / synchronized by publishers: no raw clock validation', 'labelled step events constitute partial annotations; unlabeled frames treated as negative by one-to-one matching, no proof of no non-annotated gait events','self-selected P001-P015 vs P016-P030 participant identifiers, not randomized; retrospective after prior publication','no causal intervention and no counterfactual observation process','time-window / per-event errors correlated, descriptive block bootstrap is not valid population confidence assertion','Fréchet overlap conditional on video event definition is not ecological latent availability or identification of parameter-indexed experiment','original two shift timestamps lie outside sensor time-series; reported and not silently corrected']}
    with (out/'p7_result.json').open('w') as f:json.dump(result,f,indent=2,ensure_ascii=False,sort_keys=True);f.write('\n')
    for name,rows in [('p7_test_per_trial.csv',per_rows),('p7_pair_overlap_by_trial.csv',pairs_overlap)]:
        with (out/name).open('w',newline='') as f:
            wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
    print(json.dumps({'parameters':training,'heldout_video_steps':result['test_reference_count'],'primary':totals,'by_condition':by_cond,'overlap':overlap_totals,'bootstrap':bootstrap,'test_trials':len(te)},indent=2))
    print('P7_CLEMSON_VIDEO_REFERENCE_SOURCE_BOUNDED_REPLAY_PASS; TRUE_INDEPENDENT_ERROR_AND_PARAMETER_TRANSPORT_HOLD')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('original_zip');p.add_argument('output_dir');args=p.parse_args()
    compute_court(args.original_zip,args.output_dir)
