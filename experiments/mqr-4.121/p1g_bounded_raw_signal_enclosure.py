"""MQR 4.121 P1G: analytic interval enclosure for a *2-channel synthetic* optical pilot.

No instrument data, independent spectral calibration or chemical state assay is supplied.
Assumes fixed, known invertible intensity-domain response M; independently bounded
additive OOB illumination 0 <= q <= Q and additive detector noise -E <= e <= E.
"""
from math import isclose, log10

def inverse_2(m):
    a,b=m[0]; c,d=m[1]
    z=a*d-b*c
    if abs(z) < 1e-12: raise ValueError("singular detector response")
    return ((d/z,-b/z),(-c/z,a/z))

def matvec(m, v):
    return tuple(sum(a*b for a,b in zip(row,v)) for row in m)

def intensity_interval(y, m, qmax, noise):
    if qmax is None: raise ValueError("out-of-range spectral contribution has no independent bound")
    if len(y)!=2 or len(qmax)!=2 or len(noise)!=2: raise ValueError("2-channel fixture only")
    if any(z<0 for z in (*qmax,*noise)): raise ValueError("nonnegative limits required")
    inv=inverse_2(m)
    baseline=matvec(inv,y)
    lower=[];upper=[]
    for i in range(2):
        low=baseline[i]; high=baseline[i]
        for j in range(2):
            v=inv[i][j]
            wlow=-noise[j]; whigh=qmax[j]+noise[j]
            low-=max(v*wlow,v*whigh)
            high-=min(v*wlow,v*whigh)
        lower.append(low);upper.append(high)
    return tuple(lower),tuple(upper)

def absorbance_interval(sample, reference, m, sample_qmax, ref_qmax, noise):
    s0,s1=intensity_interval(sample,m,sample_qmax,noise)
    r0,r1=intensity_interval(reference,m,ref_qmax,noise)
    if min(*s0,*r0)<=0 or min(*s1,*r1)<=0:
        raise ValueError("positivity not certified for signal-domain logarithm")
    return tuple((-log10(s1[i]/r0[i]),-log10(s0[i]/r1[i])) for i in range(2))

def test():
    m=((.98,.02),(.01,.99))
    dark=(.0002,.0002)
    raw_ref=tuple(a+b+c for a,b,c in zip(matvec(m,(1.,.8)),(.001,0.),dark))
    raw_sample=tuple(a+b+c for a,b,c in zip(matvec(m,(.01,.5)),(.003,0.),dark))
    sample=tuple(a-d for a,d in zip(raw_sample,dark))
    ref=tuple(a-d for a,d in zip(raw_ref,dark))
    bounds=absorbance_interval(sample,ref,m,(.003,.001),(.001,.001),(.0001,.0001))
    targets=(2.,-log10(.5/.8))
    assert all(lo<=t<=hi for (lo,hi),t in zip(bounds,targets))
    assert all(lo<hi for lo,hi in bounds)
    exact=absorbance_interval(matvec(m,(.01,.5)),matvec(m,(1.,.8)),m,(0.,0.),(0.,0.),(0.,0.))[0]
    assert all(isclose(v,2.,abs_tol=1e-12) for v in exact)
    try: absorbance_interval(sample,ref,m,None,(.001,.001),(.0001,.0001))
    except ValueError as e: assert "no independent bound" in str(e)
    else: raise AssertionError("missing OOB bound must not silently pass")
    # The inverse of a well-conditioned response is not an assay of sample chemistry.
    print("MQR_P1G_INTERVAL_FIXTURE=PASS_SYNTHETIC")
    print("MQR_P1G_FIRST_CHANNEL_A_INTERVAL=%.9f,%.9f" % bounds[0])
    print("MQR_P1G_SECOND_CHANNEL_A_INTERVAL=%.9f,%.9f" % bounds[1])
    print("MQR_P1G_REAL_SOURCE_ADMISSION=HOLD")

if __name__=="__main__": test()
