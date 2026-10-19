"""MQR 4.121 P1H raw optical intake: structural checks ONLY; no provenance authentication."""
import json, argparse
from math import isfinite
from pathlib import Path

def require(ok,msg):
    if not ok: raise ValueError(msg)

def vector(v,n,label):
    require(isinstance(v,list) and len(v)==n and all(isinstance(x,(int,float)) and not isinstance(x,bool) and isfinite(x) and x>=0 for x in v),label)

def validate(d):
    require(d.get('schema_version')=='MQR-4.121-P1H/1','schema_version')
    kind=d.get('provenance',{}).get('kind')
    require(kind in ('synthetic','physical'),'provenance')
    inst=d['instrument']; n=len(inst['wavelength_nm'])
    require(n>=2 and inst['response_architecture'] in ('array','scanning'),'architecture')
    require(inst['units']=='raw_linear_detector_counts','absorbance cannot substitute for raw')
    vector(inst['wavelength_nm'],n,'wavelengths')
    require(all(x<y for x,y in zip(inst['wavelength_nm'],inst['wavelength_nm'][1:])),'wavelength ordering')
    maxcount=inst['max_linear_count']
    require(isinstance(maxcount,(int,float)) and maxcount>0,'detector ceiling')
    cals={}
    for c in d['calibrations']:
        require(c['id'] not in cals and c['instrument_serial']==inst['serial'],'calibration identity')
        require(c['independent_of_test_samples'] is True and c['method']=='monochromatic_line_spread','independent laser SLSF')
        require(bool(c.get('evidence_uri')),'calibration provenance')
        M=c['response_matrix']
        require(isinstance(M,list) and len(M)==n,'matrix size')
        for row in M:vector(row,n,'matrix row')
        require(all(M[i][i]>sum(M[i][j] for j in range(n) if j!=i) for i in range(n)),'diagonal dominance pilot gate')
        for key in ('sample_oob_upper_counts','reference_oob_upper_counts','noise_abs_upper_counts'):
            vector(c.get(key),n,key)
        cals[c['id']]=c
    require(bool(cals),'no calibration')
    ids=set()
    for r in d['records']:
        require(r['id'] not in ids,'duplicate ID')
        ids.add(r['id'])
        require(r['calibration_id'] in cals,'no matching calibration')
        require(r['optical_config_id']==cals[r['calibration_id']]['optical_config_id'],'mismatched optical setup')
        for key in ('sample_raw','reference_raw','sample_dark','reference_dark'):
            vector(r.get(key),n,key)
        for typ in ('sample','reference'):
            require(all(lo<hi<maxcount for hi,lo in zip(r[typ+'_raw'],r[typ+'_dark'])),'dark/saturation gate')
        for key in ('sample_id','sample_history_id','block_id','run_order','pH','temperature_K','concentration_mol_L','integration_ms'):
            require(r.get(key) is not None and r.get(key)!='','missing '+key)
        for key in ('pH','temperature_K','concentration_mol_L','integration_ms'):
            require(isinstance(r[key],(int,float)) and isfinite(r[key]),'invalid '+key)
        require(0<=r['pH']<=14 and r['temperature_K']>0 and r['concentration_mol_L']>0 and r['integration_ms']>0,'physical metadata')
        if inst['response_architecture']=='scanning':
            for key in ('sample_channel_times_iso','reference_channel_times_iso'):
                require(isinstance(r.get(key),list) and len(r[key])==n and all(isinstance(x,str) and x for x in r[key]),'per-channel acquisition time required')
        if kind=='physical':
            h=r.get('raw_file_sha256','')
            require(len(h)==64 and all(x in '0123456789abcdef' for x in h.lower()),'raw bytes SHA256 required')
            require(r.get('raw_file_uri','').startswith(('https://','s3://','file://')),'raw file locator required')
    require(bool(ids),'no records')
    return {'result':'STRUCTURAL_PASS_PROVENANCE_UNVERIFIED','kind':kind,'channels':n,'records':len(ids),'calibrations':len(cals),'chemical_species_inference':'HOLD'}

def fixture():
    return {'schema_version':'MQR-4.121-P1H/1','provenance':{'kind':'synthetic'},
      'instrument':{'model':'SYNTH','serial':'SIM-001','response_architecture':'array','units':'raw_linear_detector_counts','wavelength_nm':[450.,550.,650.],'max_linear_count':10000},
      'calibrations':[{'id':'cal0','instrument_serial':'SIM-001','optical_config_id':'wide','method':'monochromatic_line_spread','independent_of_test_samples':True,'evidence_uri':'synthetic://independent-toy-calibration','response_matrix':[[1,.01,.01],[.01,1,.01],[.01,.01,1]],'sample_oob_upper_counts':[5,5,5],'reference_oob_upper_counts':[5,5,5],'noise_abs_upper_counts':[2,2,2]}],
      'records':[{'id':'SIM001','calibration_id':'cal0','optical_config_id':'wide','sample_id':'S','sample_history_id':'H','block_id':'B','run_order':1,'pH':6,'temperature_K':298.15,'concentration_mol_L':.0001,'integration_ms':100,'sample_raw':[1000,2000,3000],'sample_dark':[2,2,2],'reference_raw':[5000,5000,5000],'reference_dark':[2,2,2]}]}

def selftest():
    from copy import deepcopy
    s=fixture()
    assert validate(s)['result']=='STRUCTURAL_PASS_PROVENANCE_UNVERIFIED'
    def reject(variant):
        try:validate(variant)
        except ValueError:return
        raise AssertionError('unsafe record admitted')
    a=deepcopy(s);a['instrument']['units']='absorbance';reject(a)
    a=deepcopy(s);a['calibrations'][0].pop('sample_oob_upper_counts');reject(a)
    a=deepcopy(s);a['calibrations'][0]['independent_of_test_samples']=False;reject(a)
    a=deepcopy(s);a['records'][0]['sample_raw'][0]=2;reject(a)
    a=deepcopy(s);a['instrument']['response_architecture']='scanning';reject(a)
    a=deepcopy(s);a['provenance']['kind']='physical';reject(a)
    print('MQR_P1H_INTAKE_SCHEMA=PASS_SYNTHETIC')
    print('MQR_P1H_EXTERNAL_FILE_AUTHENTICATION=HOLD')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--validate',type=Path);p.add_argument('--example',action='store_true')
    a=p.parse_args();selftest()
    if a.example:print(json.dumps(fixture(),indent=2))
    if a.validate:print(json.dumps(validate(json.loads(a.validate.read_text())),indent=2))
