"""MQR 5.4 / chat MQR 41 — two-channel spectrometer identifiability audit.

Illustrative synthetic numbers only, not measurements from Zong et al.
Instrument y=M x, matrix calibrated with monochromatic unit probes e1,e2.
Provenance comparator: Zong et al. 2006, Applied Optics 45:1111-1119.
"""
from math import isclose

def apply(M, x):
    return tuple(sum(M[i][j]*x[j] for j in (0,1)) for i in (0,1))

def det(M):
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]

def invert(M, y):
    d=det(M)
    if abs(d)<1e-12:
        raise ValueError("rank deficient: calibration cannot recover spectrum")
    return ((M[1][1]*y[0]-M[0][1]*y[1])/d,
            (-M[1][0]*y[0]+M[0][0]*y[1])/d)

def calibration_from_basis(M):
    c0=apply(M,(1.0,0.0))
    c1=apply(M,(0.0,1.0))
    return ((c0[0],c1[0]),(c0[1],c1[1]))

def run():
    true=(1.,.1)
    M=((1.,.12),(.05,1.))
    observed=apply(M,true)
    naive=observed
    assert observed==(1.012,.15000000000000002) or all(
        isclose(v,w,rel_tol=0,abs_tol=1e-12)
        for v,w in zip(observed,(1.012,.15)))
    assert isclose((naive[1]-true[1])/true[1],.5,abs_tol=1e-12)
    # One reading is consistent with two different (spectrum, instrument) pairs:
    assert apply(((1.,0.),(0.,1.)), observed)==observed
    # New calibration interventions identify instrument mixing in this model:
    estimated=calibration_from_basis(M)
    assert estimated==M
    recovered=invert(estimated,observed)
    assert all(isclose(a,b,abs_tol=1e-12) for a,b in zip(recovered,true))
    singular=((1.,1.),(.5,.5))
    assert det(singular)==0
    try:
        invert(calibration_from_basis(singular),(2.,1.))
    except ValueError:
        pass
    else:
        raise AssertionError("expected non-identifiability")
    print("observed channels",tuple(round(v,6) for v in observed))
    print("naive weak-band relative error: +50%")
    print("with calibrated matrix: recovered",tuple(round(v,6) for v in recovered))
    print("singular detector response: inversion correctly rejected")
    print("PASS: instrument-state ambiguity, calibration remedy, rank-deficiency limit")

if __name__=="__main__":run()
