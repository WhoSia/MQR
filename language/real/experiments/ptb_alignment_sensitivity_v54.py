"""Lag sensitivity of three *published figure-export* PTB 2025 waveforms.

Equal x coordinates do not establish same-run/clock physical synchronization.
Only arithmetic differences among tabular samples are assessed.
"""
from __future__ import annotations
from math import sqrt
from statistics import fmean
from ptb_oa_graph_checks_v54 import load_time_voltage


def alignment_sensitivity(a,b,c,lags=(-2,-1,0,1,2)):
    if not (len(a)==len(b)==len(c)) or len(a)<4:
        raise ValueError('Same nonempty exported trace dimensions required')
    grids=tuple(x[0] for x in a)
    if any(tuple(x[0] for x in t)!=grids for t in (b,c)):
        raise ValueError('Published x grid differs')
    if any(grids[i]>=grids[i+1] for i in range(len(grids)-1)):
        raise ValueError('Unsorted output grid')
    values={k:tuple(x[1] for x in t) for k,t in [('a',a),('b',b),('c',c)]}
    output={}
    for lag in lags:
        if isinstance(lag,bool) or not isinstance(lag,int):
            raise ValueError('Lag must be an integer number of samples')
        if abs(lag)>=len(a)-2:
            raise ValueError('Lag exceeds usable training and holdout')
        low=max(0,-lag)
        high=min(len(a),len(a)-lag)
        residual=[values['a'][i+lag]+values['b'][i]-values['c'][i]
                  for i in range(low,high)]
        m=len(residual)//2
        offset=fmean(residual[:m])
        test=residual[m:]
        output[lag]={
            'lag_in_export_samples':lag,
            'holdout_count':len(test),
            'fitted_offset_mV':offset,
            'holdout_rmse_mV':sqrt(fmean([(x-offset)**2 for x in test])),
        }
    return output


def from_zip(path):
    a,b,c=(load_time_voltage(path,n) for n in ('fig3b.txt','fig3d.txt','fig3f.txt'))
    return alignment_sensitivity(a,b,c)
