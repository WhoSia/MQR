#!/usr/bin/env python3
"""MQR-4.122 P7: exact rational enclosures of a continuous finite-ball emitter.
Uses standard-library integer/Fraction arithmetic, NOT ordinary floating-point
interval endpoints. No BEST target geometry, nuclear cross sections or fit.
"""
from fractions import Fraction as Q
from math import comb, factorial

SOURCE_RADIUS = Q(1, 20)  # 0.05 metre uniform source ball
KAPPA = Q(8)               # 8 radians/metre synthetic oscillation
AMPLITUDE = Q(11, 20)      # 0.55
SHELLS = ((Q(1,5), Q(17,50)),
          (Q(17,50), Q(49,100)),
          (Q(49,100), Q(13,20)))
N_BASELINE = 11
N_COSINE = 33

def baseline_interval(lo, hi):
    """Enclose ∫dr E_source[r²/d²] on lo≤r≤hi, source radius a<lo.

    Angular average at fixed r,s: (r/(2s))log((r+s)/(r-s))
    = Σ_{n≥0} (s/r)^(2n)/(2n+1).
    Uniform-ball E[s^(2n)] = 3 a^(2n)/(2n+3).
    All coefficients positive. Tail bound uses r≥lo and a/lo≤1/4.
    """
    assert SOURCE_RADIUS < lo < hi
    total = Q(0)
    a = SOURCE_RADIUS
    for n in range(N_BASELINE + 1):
        coefficient = Q(3, (2*n+1)*(2*n+3))*a**(2*n)
        integral = (hi-lo if n==0 else
                    (lo**(1-2*n)-hi**(1-2*n))/Q(2*n-1))
        total += coefficient*integral
    n = N_BASELINE + 1
    ratio = (a/lo)**2
    first_coefficient = Q(3, (2*n+1)*(2*n+3))
    # Integral of each omitted term ≤ (hi-lo)*ratio^n,
    # coefficient decreases with n; geometric tail bounds remainder.
    tail = (hi-lo)*first_coefficient*ratio**n/(1-ratio)
    return total, total+tail

def moment(n, lo, hi):
    """Exact integral ∫dr r² E_{s,u}[(r²+s²-2rsu)^(n-1)].
    u uniformly distributed on [-1,1]; source radial density 3s²/a³.
    Angular mean computed by binomial integration, no quadrature.
    """
    assert n >= 1
    a = SOURCE_RADIUS
    total = Q(0)
    for j in range(1,2*n+1,2):
        power = 2*n-j+1
        factor = Q(3*comb(2*n,j),2*n*(j+2))*a**(j-1)
        total += factor*(hi**(power+1)-lo**(power+1))/Q(power+1)
    return total

def oscillation_interval(lo, hi):
    """C= B + A/2 ∫r² E[(cos(2κd)-1)/d²] dr.
    Taylor remainder on cos: |R|≤(2κd)^(2N+2)/(2N+2)!;
    integrating positive r²d^(2N) produces certified moment remainder.
    """
    b_lower,b_upper = baseline_interval(lo,hi)
    terms = Q(0)
    for n in range(1,N_COSINE+1):
        terms += Q((-1)**n*(2*KAPPA)**(2*n),factorial(2*n))*moment(n,lo,hi)
    remainder = Q((2*KAPPA)**(2*N_COSINE+2),
                  factorial(2*N_COSINE+2))*moment(N_COSINE+1,lo,hi)
    return (b_lower+AMPLITUDE*Q(1,2)*(terms-remainder),
            b_upper+AMPLITUDE*Q(1,2)*(terms+remainder))

def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[1],-x[0]
def mul(x,y):
    outcomes=[a*b for a in x for b in y]
    return min(outcomes),max(outcomes)
def determinant_interval(v,b,c):
    result=(Q(0),Q(0))
    for i,j,k,sign in ((0,1,2,1),(1,2,0,1),(2,0,1,1),
                        (2,1,0,-1),(1,0,2,-1),(0,2,1,-1)):
        term=mul(mul(v[i],b[j]),c[k])
        result=add(result,term if sign==1 else neg(term))
    return result

def main():
    # V/(4π) = ∫_shell r²dr; sign of determinant is unchanged.
    volumes=[((hi**3-lo**3)/3,)*2 for lo,hi in SHELLS]
    baseline=[baseline_interval(lo,hi) for lo,hi in SHELLS]
    oscillation=[oscillation_interval(lo,hi) for lo,hi in SHELLS]
    d_lower,d_upper=determinant_interval(volumes,baseline,oscillation)
    print("P7_SOURCE_RADIUS_M=1/20; KAPPA_RAD_PER_M=8; AMP=11/20")
    print("P7_B_SERIES_ORDER",N_BASELINE,"P7_C_TAYLOR_ORDER",N_COSINE)
    for label,intervals in (("B",baseline),("C",oscillation)):
        for i,(lo,hi) in enumerate(intervals):
            print(f"P7_{label}{i+1}_LOWER={float(lo):.17g} UPPER={float(hi):.17g} WIDTH={float(hi-lo):.3g}")
    print(f"P7_DET_SCALED_LOWER={float(d_lower):.17g} UPPER={float(d_upper):.17g}")
    print("P7_DET_SIGN_STRICT_POSITIVE=",d_lower>0)
    assert d_lower>0, "failed to certify nonzero continuum determinant"
    assert d_upper-d_lower < Q(1,10**15), "enclosure too wide"
    assert all(x[0]>0 and x[1]>0 for x in baseline+oscillation)
    print("MQR_4122_P7_CONTINUUM_RATIONAL_ENCLOSURE=PASS")
    print("MQR_4122_P7_BEST_FIG8_REPRODUCTION=HOLD")
    print("MQR_4122_P7_LEAN_CONTINUUM_INTEGRAL_PROOF=HOLD")

if __name__=="__main__":main()
