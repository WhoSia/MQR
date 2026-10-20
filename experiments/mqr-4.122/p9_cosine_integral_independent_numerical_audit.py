#!/usr/bin/env python3
"""P9 independent non-Taylor oscillation kernel:
integrate source/target angle analytically using cosine integrals
of cos(2kd)/d; then independently evaluate via mpmath high precision
Gauss-Legendre quadrature. This is an independent numeric cross-check,
not a rigorous certified enclosure (P7 remains the certified route)."""
import mpmath as mp
mp.mp.dps=45
a=mp.mpf('0.05')
shells=[('0.20','0.34'),('0.34','0.49'),('0.49','0.65')]
def K0(r):
    if abs(r)<a: raise ValueError
    return (3*r/(2*a**3))*(r*a+(a*a-r*r)/2*mp.log((r+a)/(r-a)))
def Kosc(r,k):
    # integral over s via radial Gauss Legendre; angular cosine term exact:
    # mean_{u} [r² cos(2kd)/d²] = r/(2s) [Ci(2k(r+s))-Ci(2k(r-s))]
    # for k>0, d>0, Ci derivative = cos(z)/z
    def s_term(s):
        if s==0: return (3*s*s/a**3)*mp.cos(2*k*r)
        t=(r/(2*s))*(mp.ci(2*k*(r+s))-mp.ci(2*k*(r-s)))
        return (3*s*s/a**3)*t
    cospart=mp.quadgl(s_term,[0,a],degree=60)
    return (1-mp.mpf('0.55')/2)*K0(r)+(mp.mpf('0.55')/2)*cospart
def main():
    v=[];b=[];c=[]
    for slo,shi in shells:
        lo,hi=mp.mpf(slo),mp.mpf(shi)
        v.append((hi**3-lo**3)/3)
        b.append(mp.quadgl(K0,[lo,hi],degree=50))
        c.append(mp.quadgl(lambda r:Kosc(r,mp.mpf(8)),[lo,hi],degree=45))
    d=mp.det(mp.matrix([v,b,c]))
    print("P9_DET_CI_QUADRATURE =",mp.nstr(d,30))
    assert mp.mpf('0.0002683063923697') < d < mp.mpf('0.0002683063923699')
    print("MQR_4122_P9_INDEPENDENT_ANGLE_CI_QUADRATURE=PASS")
    print("MQR_4122_P9_INDEPENDENT_RIGOROUS_ERROR_BOUND=HOLD")
    print("MQR_4122_P9_BEST_GEOMETRY=HOLD")
if __name__=="__main__":main()
