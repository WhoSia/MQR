"""MQR-4.122 P1: synthetic radial averaging, NOT BEST detector reproduction."""
import math
AMP=0.4
E_MEV=0.75
# Illustrative radial intervals in m; NOT the actual BEST zones.
BINS=((0.10,0.65),(0.65,1.20))
def mean(dm2,bounds,n=10000):
    lo,hi=bounds
    return sum(1-AMP*math.sin(1.267*dm2*(lo+(j+.5)*(hi-lo)/n)/E_MEV)**2 for j in range(n))/n
if __name__=="__main__":
    print("MQR_4122_BEST_TOY_ONLY=TRUE")
    print("dm2_eV2,in_toy,out_toy,out_over_in")
    for dm2 in (.1,.5,1,5,10,30,100):
        a,b=[mean(dm2,z) for z in BINS]
        assert .6<=a<=1 and .6<=b<=1
        print(f"{dm2:g},{a:.6f},{b:.6f},{b/a:.6f}")
        if dm2>=10:assert abs(b/a-1)<.01
    print("MQR_4122_ZONE_AVERAGING=PASS_SYNTHETIC")
    print("MQR_4122_REAL_BEST_GEOMETRY_AND_SPECTRUM=HOLD")
