"""MQR 4.121 P1H: cross-validated optical-vs-pH contrast under synthetic independent calibration.

Toy spectra, known response matrices and bounded additive signals only. No physical
methyl-red data, actual chemical species identification or frequentist test validity.
"""
from math import log10

def mv(m,x): return tuple(sum(a*b for a,b in zip(row,x)) for row in m)
def plus(*xs): return tuple(sum(x[i] for x in xs) for i in range(len(xs[0])))

def inverse(m):
    n=len(m); a=[list(row)+[float(i==j) for j in range(n)] for i,row in enumerate(m)]
    for j in range(n):
        k=max(range(j,n),key=lambda i:abs(a[i][j]))
        if abs(a[k][j])<1e-12:raise ValueError('singular calibration')
        a[j],a[k]=a[k],a[j]
        d=a[j][j];a[j]=[x/d for x in a[j]]
        for i in range(n):
            if i!=j:
                d=a[i][j];a[i]=[v-d*w for v,w in zip(a[i],a[j])]
    return tuple(tuple(row[n:]) for row in a)

def absorption_bounds(sample,reference,M,q_sample,q_reference,err):
    """Rectangular error on sample+reference counts, fixed exact independently calibrated M."""
    im=inverse(M); n=len(im)
    xs=mv(im,tuple(x-q for x,q in zip(sample,q_sample)))
    xr=mv(im,tuple(x-q for x,q in zip(reference,q_reference)))
    margin=[sum(abs(a)*err for a in row) for row in im]
    if any(x<=m for x,m in zip(xs,margin)) or any(x<=m for x,m in zip(xr,margin)):
        raise ValueError('unresolved positivity')
    return tuple((-log10((xs[i]+margin[i])/(xr[i]-margin[i])),
                  -log10((xs[i]-margin[i])/(xr[i]+margin[i]))) for i in range(n))

def simulation(chemical=True,err=.001):
    M={'wide':((1.,.018,.008),(.012,1.,.006),(.008,.016,1.)),
       'narrow':((1.,.006,.003),(.005,1.,.004),(.002,.006,1.))}
    qs={'wide':(.007,.004,.003),'narrow':(.002,.002,.001)}
    qr={'wide':(.003,.002,.002),'narrow':(.001,.001,.001)}
    T0=(.72,.44,.60);T1=(.55,.51,.47) if chemical else T0
    records={}
    for level,T in [('low',T0),('high',T1)]:
        for optic in M:
            records[level,optic]=(plus(mv(M[optic],T),qs[optic]),
                                  plus(mv(M[optic],(1.,1.,1.)),qr[optic]))
    # No optical-only rival should be rejected unless the calibrated pH contrast
    # excludes zero after imposing the *same pH comparison in both optical settings*.
    bounds={}
    for optic in M:
        b0=absorption_bounds(*records['low',optic],M[optic],qs[optic],qr[optic],err)
        b1=absorption_bounds(*records['high',optic],M[optic],qs[optic],qr[optic],err)
        bounds[optic]=[(b1[i][0]-b0[i][1],b1[i][1]-b0[i][0]) for i in range(3)]
    intersection=[(max(bounds[o][i][0] for o in M), min(bounds[o][i][1] for o in M)) for i in range(3)]
    truth=[-log10(b/a) for a,b in zip(T0,T1)]
    assert all(lo<=v<=hi for (lo,hi),v in zip(intersection,truth))
    separated=all(lo>0 or hi<0 for lo,hi in intersection)
    assert separated==chemical
    # Confounded unbalanced protocol compares a different optical setting at each pH
    s0,r0=records['low','wide'];s1,r1=records['high','narrow']
    naive=[-log10(s1[i]/r1[i])+log10(s0[i]/r0[i]) for i in range(3)]
    return M,records,T0,T1,truth,intersection,naive

def test():
    M,records,T0,T1,delta,intersection,naive=simulation(True)
    _,_,_,_,zero,uncorrected,optical_naive=simulation(False)
    assert max(abs(v) for v in optical_naive)>.001
    assert all(abs(v)<1e-14 for v in zero)
    assert all(lo<0<hi for lo,hi in uncorrected)
    # If q can depend on pH arbitrarily, constant latent optics can mimic the
    # chemical fixture. Independent q upper bounds are indispensable.
    alt=tuple(min(a,b)-.01 for a,b in zip(T0,T1))
    for optic in M:
        for level in ('low','high'):
            s,_=records[level,optic]
            q_alt=tuple(a-b for a,b in zip(s,mv(M[optic],alt)))
            assert min(q_alt)>=0
            assert all(abs(a-b)<1e-12 for a,b in zip(plus(mv(M[optic],alt),q_alt),s))
    print('MQR_P1H_RIVAL_CROSS_INTERVENTION=PASS_SYNTHETIC')
    print('MQR_P1H_PREDICTED_CHEMICAL_DELTA_AU='+','.join(f'{v:.6f}' for v in delta))
    for i,(lo,hi) in enumerate(intersection):
        print(f'MQR_P1H_INTERSECTION_DELTA_{i}={lo:.6f},{hi:.6f}')
    print('MQR_P1H_OPTICAL_ONLY_PREDICTION_ZERO=IN_ALL_INTERVALS')
    print('MQR_P1H_CONFOUNDED_NAIVE_DELTA_AU='+','.join(f'{v:.6f}' for v in optical_naive))
    print('MQR_P1H_UNBOUNDED_PH_DEPENDENT_OOB=NONIDENTIFIABLE')
    print('MQR_P1H_REAL_CHEMICAL_SPECIES_COUNT=HOLD')

if __name__=='__main__':test()
