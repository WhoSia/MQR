#!/usr/bin/env python3
"""MQR 4.122 P8: independently derived exact rational radial moments.

Unlike P7's angular-endpoint binomial difference formula, directly expand
(r²+s²-2rsu)^(n-1). Odd u powers vanish and even u^(2k)
average to 1/(2k+1). Then independently integrate s and r monomials.
No numerical quadrature, no import of P7 derivation, no physical BEST mask.
"""
from fractions import Fraction as F
from math import comb

RADIUS=F(1,20)
SHELLS=((F(1,5),F(17,50)),(F(17,50),F(49,100)),(F(49,100),F(13,20)))

def independent_moment(n,lo,hi):
    assert n>=1 and 0<lo<hi
    m=n-1
    acc=F(0)
    for k in range(0,m+1,2):
        for t in range(m-k+1):
            # (r²+s²-2rsu)^m: even angular power k
            # monomial exponents: r^(2m-k-2t) s^(k+2t)
            sp=k+2*t
            rp=2*m-k-2*t+2 # r² measure
            coeff=(F(comb(m,k)*comb(m-k,t)*2**k,k+1)
                   *F(3,sp+3)*RADIUS**sp)
            acc+=coeff*(hi**(rp+1)-lo**(rp+1))/F(rp+1)
    return acc

def endpoint_moment(n,lo,hi):
    """Independent implementation of the P7 expression solely for cross-check."""
    acc=F(0)
    for j in range(1,2*n+1,2):
        rp=2*n-j+1
        acc+=F(3*comb(2*n,j),2*n*(j+2))*RADIUS**(j-1) * (
            hi**(rp+1)-lo**(rp+1))/F(rp+1)
    return acc

def main():
    for n in range(1,35):
        for lo,hi in SHELLS:
            assert independent_moment(n,lo,hi)==endpoint_moment(n,lo,hi), (
                f"mismatch at order {n}, shell {lo}:{hi}")
    print("MQR_4122_P8_INDEPENDENT_MOMENTS_102_OVER_102=PASS")
    print("MQR_4122_P8_KERNEL_FORMALIZATION_IN_LEAN=HOLD")
    print("MQR_4122_P8_ACTUAL_BEST_GEOMETRY=HOLD")

if __name__=="__main__":
    main()
