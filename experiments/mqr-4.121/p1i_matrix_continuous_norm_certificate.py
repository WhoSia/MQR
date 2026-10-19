"""MQR-4.121 P1I continuous matrix-uncertainty enclosure via inverse norm.

Unlike 2^9 corner sampling, the bound applies to EVERY matrix perturbation with
||Delta M||_infinity <= eps, if the stated nuisance bounds and a common fixed
calibration setup are actually true. All data here remain synthetic.
"""
from math import log10
from p1h_cross_intervention_rivals import simulation,inverse,mv

def norm_inf(M):
    return max(sum(abs(v) for v in row) for row in M)

def continuous_intensity_box(y,M,q_nom,eps,signal_error):
    if eps<0 or signal_error<0:raise ValueError("negative bound")
    V=inverse(M)
    K=norm_inf(V)
    if K*eps>=1:raise ValueError("inverse norm stability not established")
    xhat=mv(V,tuple(a-b for a,b in zip(y,q_nom)))
    # x - xhat = -Mhat^-1 DeltaM*x - Mhat^-1 delta.
    # x <= xhat + (x-xhat) => Neumann-type uniform enclosure.
    radius=K*(eps*max(abs(v) for v in xhat)+signal_error)/(1-K*eps)
    lo=tuple(v-radius for v in xhat)
    hi=tuple(v+radius for v in xhat)
    if min(lo)<=0:raise ValueError("positive signal cannot be certified")
    return list(zip(lo,hi)),radius

def absorbance_box(sample,reference,M,q_sample,q_ref,eps,signal_error):
    s,_=continuous_intensity_box(sample,M,q_sample,eps,signal_error)
    r,_=continuous_intensity_box(reference,M,q_ref,eps,signal_error)
    return [(-log10(s[i][1]/r[i][0]), -log10(s[i][0]/r[i][1])) for i in range(3)]

def contrast(chemical,matrix_each_entry_limit=.002):
    M,records,T0,T1,truth,*_=simulation(chemical)
    qS={'wide':(.007,.004,.003),'narrow':(.002,.002,.001)}
    qR={'wide':(.003,.002,.002),'narrow':(.001,.001,.001)}
    # eps=3*entrywise_limit encloses every 3x3 DeltaM with |Delta M_ij|<=limit.
    eps=3*matrix_each_entry_limit
    inter=[]
    for optic in M:
        lo=absorbance_box(*records['low',optic],M[optic],qS[optic],qR[optic],eps,.0015)
        hi=absorbance_box(*records['high',optic],M[optic],qS[optic],qR[optic],eps,.0015)
        inter.append([(a[0]-b[1],a[1]-b[0]) for b,a in zip(lo,hi)])
    out=[(max(inter[0][i][0],inter[1][i][0]),min(inter[0][i][1],inter[1][i][1])) for i in range(3)]
    assert all(a<=t<=b for (a,b),t in zip(out,truth))
    return out,truth

def test():
    chemical,truth=contrast(True)
    null,zero=contrast(False)
    assert all(a>0 or b<0 for a,b in chemical),"chosen synthetic chemical shifts indistinguishable under norm certificate"
    assert all(a<=0<=b for a,b in null)
    # The direct finite-corner survey must be contained within the proven norm envelope.
    from p1i_matrix_uncertainty_rival_grid import contrast_intersections
    corner,_=contrast_intersections(True,.002)
    assert all(a<=c[0]+1e-10 and b>=c[1]-1e-10 for (a,b),c in zip(chemical,corner))
    try:continuous_intensity_box((.1,.2,.3),((1.,0.,0.),(0.,1.,0.),(0.,0.,1.)),(0.,0.,0.),1.,0.)
    except ValueError:pass
    else:raise AssertionError("unbounded-inverse case admitted")
    print("MQR_P1I_CONTINUOUS_MATRIX_ENCLOSURE=PASS_SYNTHETIC_THEOREM_PREMISES")
    for i,(a,b) in enumerate(chemical):
        print(f"MQR_P1I_CONTINUOUS_DELTA_A_{i}={a:.6f},{b:.6f}")
    print("MQR_P1I_CHEMICAL_SPECIES_UNIQUENESS=HOLD")
    print("MQR_P1I_REAL_INSTRUMENT_MATRIX_RADIUS=UNMEASURED")

if __name__=="__main__":test()
