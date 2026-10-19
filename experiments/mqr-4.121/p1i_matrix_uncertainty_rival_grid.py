"""MQR P1I finite matrix-uncertainty enclosure; calibrated toy world only.

All 3x3 entries vary within an *assumed* box around independent calibration.
This is a finite 2^9-corner sensitivity study, not a certified enclosure over
the continuous 9-dimensional calibration uncertainty box.
"""
from itertools import product
from math import log10
from p1h_cross_intervention_rivals import simulation, inverse, mv

def corners(M, radius):
    if radius<0 or radius>.01:raise ValueError("pilot bound outside admitted envelope")
    for signs in product((-1,1),repeat=9):
        yield tuple(tuple(M[i][j]+radius*signs[3*i+j] for j in range(3)) for i in range(3))

def corrected_ranges(y, q_nom, M, radius, bound=0.0015):
    ranges=[]
    for candidate in corners(M,radius):
        if any(candidate[i][i] <= sum(abs(candidate[i][j]) for j in range(3) if j!=i) for i in range(3)):
            raise ValueError("matrix invalid under perturbation")
        V=inverse(candidate)
        center=mv(V,tuple(a-b for a,b in zip(y,q_nom)))
        d=tuple(sum(abs(a)*bound for a in row) for row in V)
        ranges.append(tuple((a-e,a+e) for a,e in zip(center,d)))
    lo=[min(v[i][0] for v in ranges) for i in range(3)]
    hi=[max(v[i][1] for v in ranges) for i in range(3)]
    if min(lo)<=0:raise ValueError("positive intensity not certified")
    return list(zip(lo,hi))

def A_ranges(sample, ref, q_sample, q_ref, M, radius):
    s=corrected_ranges(sample,q_sample,M,radius)
    r=corrected_ranges(ref,q_ref,M,radius)
    return [(-log10(s[i][1]/r[i][0]),-log10(s[i][0]/r[i][1])) for i in range(3)]

def contrast_intersections(chemical, matrix_error):
    M,records,T0,T1,truth,*_=simulation(chemical)
    qs={'wide':(.007,.004,.003),'narrow':(.002,.002,.001)}
    qr={'wide':(.003,.002,.002),'narrow':(.001,.001,.001)}
    band={}
    for optic in M:
        low=A_ranges(*records['low',optic],qs[optic],qr[optic],M[optic],matrix_error)
        high=A_ranges(*records['high',optic],qs[optic],qr[optic],M[optic],matrix_error)
        band[optic]=[(hi[0]-lo[1],hi[1]-lo[0]) for lo,hi in zip(low,high)]
    # Cross-setting intersection is only warranted because chemical state is
    # stipulated constant across optical configurations in this toy experiment.
    inter=[(max(band[o][i][0] for o in M),min(band[o][i][1] for o in M)) for i in range(3)]
    assert all(a<=b for a,b in inter)
    assert all(a<=t<=b for (a,b),t in zip(inter,truth))
    return inter,truth

def test():
    base,t=contrast_intersections(True,0.)
    wider,t=contrast_intersections(True,.002)
    null,z=contrast_intersections(False,.002)
    assert all(hi<0 or lo>0 for lo,hi in wider), "chemical contrast should survive *chosen* bounded matrix error"
    assert all(lo<0<hi for lo,hi in null), "unchanged chemistry must not be rejected"
    assert all((b-a)>=(y-x)-1e-12 for (a,b),(x,y) in zip(wider,base))
    print("MQR_P1I_MATRIX_UNCERTAINTY=PASS_FINITE_GRID_SYNTHETIC")
    print("MQR_P1I_MATRIX_CORNER_CASES_PER_OPTIC=512")
    for i,((a,b),(x,y)) in enumerate(zip(base,wider)):
        print(f"MQR_P1I_DELTA_A_{i}_EXACT_MATRIX={a:.6f},{b:.6f}")
        print(f"MQR_P1I_DELTA_A_{i}_UNCERTAIN_MATRIX={x:.6f},{y:.6f}")
    print("MQR_P1I_UNBOUNDED_OUT_OF_RANGE_LIGHT=UNIDENTIFIABLE")
    print("MQR_P1I_CONTINUOUS_MATRIX_BOX_CERTIFICATE=HOLD")
    print("MQR_P1I_LABORATORY_CHEMICAL_ONTOLOGY=HOLD")

if __name__=="__main__":test()
