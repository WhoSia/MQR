"""Point-source BEST geometry pilot. NOT original detector reproduction."""
import math
R_SPH=.6675
R_CYL=1.09
H_CYL=2.112
LINES=((.747,.8163),(.427,.0895),(.752,.0849),(.432,.0093))
AMP=.4
def average(dm2,nr=260,nz=480):
    dr=R_CYL/nr;dz=H_CYL/2/nz
    inner=sum(sum(w*(1-AMP*math.sin(1.267*dm2*(R_SPH*(i+.5)/nr)/E)**2) for E,w in LINES) for i in range(nr))/nr
    num=den=0.
    for j in range(nz):
        z=(j+.5)*dz
        for i in range(nr):
            rho=(i+.5)*dr;d2=rho*rho+z*z
            if d2<R_SPH**2:continue
            weight=rho*dr*dz/d2
            survival=sum(w*(1-AMP*math.sin(1.267*dm2*math.sqrt(d2)/E)**2) for E,w in LINES)
            den+=weight;num+=weight*survival
    return inner,num/den
if __name__=="__main__":
    print("MQR_4122_GEOMETRY=ACTUAL_PUBLISHED_DIMENSIONS_POINT_SOURCE_APPROX")
    print("MQR_4122_SOURCE_FINITE_SIZE=OMITTED")
    print("MQR_4122_LINE_DEPENDENT_CAPTURE_CROSS_SECTION=OMITTED")
    print("delta_m2,inner,outer,outer_over_inner")
    for dm in (.1,.5,1,3.3,5,10,30,100):
        a,b=average(dm)
        assert .6<=a<=1 and .6<=b<=1
        print(f"{dm:g},{a:.6f},{b:.6f},{b/a:.6f}")
    print("MQR_4122_POINT_GEOMETRY_CHECK=PASS_SYNTHETIC")
