"""MQR 4.121 P1F: bounded signal-model counterexamples (synthetic, not observations)."""
from itertools import product
from math import isclose, log10

def mixing(a: float, b: float):
    return ((1.0 - a, a), (b, 1.0 - b))

def forward(m, x):
    return (m[0][0]*x[0]+m[0][1]*x[1], m[1][0]*x[0]+m[1][1]*x[1])

def invert2(m, y):
    a,b=m[0]; c,d=m[1]; det=a*d-b*c
    if abs(det) < 1.e-12:
        raise ValueError('singular response')
    return ((d*y[0]-b*y[1])/det, (-c*y[0]+a*y[1])/det)

def inf_norm(m):
    return max(sum(abs(v) for v in row) for row in m)

def condition_inf(m):
    inverse_columns=(invert2(m,(1.,0.)),invert2(m,(0.,1.)))
    inverse=((inverse_columns[0][0],inverse_columns[1][0]),(inverse_columns[0][1],inverse_columns[1][1]))
    return inf_norm(m)*inf_norm(inverse)

def main():
    m=mixing(.02,.01)
    physical=(.01,.5)
    oob=(.003,0.)
    ideal=forward(m,physical)
    measured=(ideal[0]+oob[0],ideal[1]+oob[1])
    naive=invert2(m,measured)
    assert all(v>0 for v in naive)
    assert all(isclose(v, w, abs_tol=1e-12) for v,w in zip(forward(m,naive),measured))
    assert all(isclose(v, w, abs_tol=1e-12) for v,w in zip(invert2(m,(measured[0]-oob[0],measured[1])),physical))
    a_true=-log10(physical[0]); a_naive=-log10(naive[0])
    # Finite uncertainty grid only; NOT a sharp bound or a statistical confidence interval.
    absorbances=[]
    for a,b,d1,d2,e1,e2 in product((.018,.020,.022),(.009,.010,.011),(0.,.0015,.003),(0.,.00025),(-.0001,.0001),(-.0001,.0001)):
        mm=mixing(a,b)
        x=invert2(mm,(measured[0]+e1-d1,measured[1]+e2-d2))
        if x[0]>0 and x[1]>0:
            absorbances.append(-log10(x[0]))
    assert min(absorbances) <= a_true <= max(absorbances)
    assert min(absorbances) <= a_naive <= max(absorbances)
    assert abs(a_true-a_naive)>.1
    assert condition_inf(m)<1.1
    print('MQR-P1F: SYNTHETIC PASS')
    for k,v in {'measured_1':measured[0],'measured_2':measured[1],'first_absorbance_true':a_true,'first_absorbance_naive':a_naive,'bias_naive':a_naive-a_true,'matrix_condition_inf':condition_inf(m),'finite_grid_count':len(absorbances),'finite_grid_A1_min':min(absorbances),'finite_grid_A1_max':max(absorbances)}.items():
        print(f'{k}={v:.9f}' if isinstance(v,float) else f'{k}={v}')

if __name__=='__main__': main()
