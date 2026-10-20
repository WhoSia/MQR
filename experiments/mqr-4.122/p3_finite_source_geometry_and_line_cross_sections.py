"""BEST geometry audit: physically finite *mathematical* emission volume, not source operation.

Uses published external dimensions and line weights, with expressly idealized
inner sphere/spherical central cavity and outer cylinder-minus-sphere.
No re-entrant tube, complete shell wall, full detailed vessel, or BEST likelihood.
Only independent computations; never fit geometric parameters to 52.03/54.41 cm.
"""
import argparse, math
PI=math.pi
SPHERE=.6675; CYL=1.09; HALF_H=1.056
SOURCE_R=.043; SOURCE_HALF_H=.054
# Emission fractions: BEST PRC 105 (2022), §I.
# Cross sections: separate 2021 secondary compilation, Universe 7, 246,
# Table 4 (model-dependent); NOT the BEST collaboration's Bahcall line list.
LINES=((.747,.8163,62.58),(.427,.0895,26.72),
       (.752,.0849,63.22),(.432,.0093,27.14))
TOTAL_SIGMA=sum(branch*xs for _,branch,xs in LINES)
WEIGHTS=tuple((energy,branch*xs/TOTAL_SIGMA) for energy,branch,xs in LINES)

def vdc(index,base):
    result=0.;power=1./base
    while index:
        index,rem=divmod(index,base)
        result+=rem*power
        power/=base
    return result

def point_source_outer_path(steps=200000):
    # For a point at the center, integrate ray length over |cos(theta)| in [0,1].
    s=0.
    for j in range(steps):
        mu=(j+.5)/steps
        lcyl=min(CYL/math.sqrt(1-mu*mu),HALF_H/mu)
        s+=lcyl-SPHERE
    return s/steps

def finite_source(zone,n=120000,seed=0,inner_cavity=.073,dm2=0,amplitude=.4):
    assert zone in ("inner","outer")
    assert 0<=inner_cavity<SPHERE and 0<=amplitude<=1
    bases=(2,3,5,7,11,13)
    if zone=="inner":
        volume=4*PI/3*(SPHERE**3-inner_cavity**3)
    else:
        volume=PI*CYL**2*(2*HALF_H)
    geom=survival=kept=0.
    for k in range(seed+1,seed+n+1):
        u=[vdc(k,b) for b in bases]
        if zone=="inner":
            rr=(inner_cavity**3+u[0]*(SPHERE**3-inner_cavity**3))**(1/3)
            mu=2*u[1]-1
            phi=2*PI*u[2]
            xx=rr*math.sqrt(1-mu*mu)*math.cos(phi)
            yy=rr*math.sqrt(1-mu*mu)*math.sin(phi)
            zz=rr*mu
        else:
            rr=CYL*math.sqrt(u[0]);phi=2*PI*u[1]
            xx=rr*math.cos(phi);yy=rr*math.sin(phi)
            zz=(2*u[2]-1)*HALF_H
            if xx*xx+yy*yy+zz*zz<SPHERE**2: continue
        rs=SOURCE_R*math.sqrt(u[3]);phs=2*PI*u[4]
        xs=rs*math.cos(phs);ys=rs*math.sin(phs)
        zs=(2*u[5]-1)*SOURCE_HALF_H
        d2=(xx-xs)**2+(yy-ys)**2+(zz-zs)**2
        if d2<1e-16:raise ValueError("unresolved near-source divergence")
        base=1/d2
        geom+=base
        if dm2:
            dist=math.sqrt(d2)
            avg=sum(w*(1-amplitude*math.sin(1.267*dm2*dist/E)**2)
                    for E,w in WEIGHTS)
            survival+=base*avg
        kept+=1
    path=volume*geom/(4*PI*n) # sample over enclosing volume
    return {"path_cm":100*path,"acceptance":kept/n,
            "survival":survival/geom if dm2 else 1.,
            "sigma_weighted_1e46_cm2":TOTAL_SIGMA}

def test():
    assert abs(sum(w for _,w in WEIGHTS)-1)<1e-13
    assert abs(sum(b for _,b,_ in LINES)-1)<1e-13
    assert math.isclose(point_source_outer_path(20000),.5542949487,abs_tol=.00002)
    assert math.isclose((SPHERE-.073)*100,59.45,abs_tol=1e-10)
    print("MQR_4122_FINITE_SOURCE_INTEGRAND_TEST=PASS")
    print("MQR_4122_REAL_TARGET_RESPONSE=HOLD")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--samples",type=int,default=120000)
    p.add_argument("--dm2",type=float,default=10.)
    args=p.parse_args()
    assert 100<=args.samples<=1000000
    test()
    print("SOURCE_MODEL=FINITE_UNIFORM_MATHEMATICAL_CYLINDER")
    print("TARGET=IDEAL_SPHERE_WITH_FIXED_7.3CM_CAVITY_AND_CYLINDER_MINUS_SPHERE")
    print("CAPTURE_LINE_SOURCE=2021_SECONDARY_COMPILATION_NOT_BEST_ORIGINAL")
    print("SIGMA_WEIGHTED_1E46_CM2",round(TOTAL_SIGMA,6))
    print("POINT_IDEAL_INNER_CM",66.75)
    print("POINT_IDEAL_OUTER_CM",round(point_source_outer_path()*100,6))
    print("zone,path_cm,survival,acceptance")
    for zone in ("inner","outer"):
        v=finite_source(zone,args.samples,dm2=args.dm2)
        print(zone,round(v["path_cm"],6),round(v["survival"],6),
              round(v["acceptance"],6),sep=",")
    print("BEST_PUBLISHED_TARGET_IN_CM=52.03")
    print("BEST_PUBLISHED_TARGET_OUT_CM=54.41")
    print("MQR_4122_INDEPENDENT_FULL_GEOMETRY_REPRODUCTION=HOLD")

if __name__=="__main__":main()
