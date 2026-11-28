"""Dimensionless conservative oscillators: shared period, distinct spatial moments."""
import math

def sample(lam, a, n=4096):
    if a <= 0 or 2*abs(lam)*a >= 1 or n <= 0:
        raise ValueError("non-monotone shear or invalid orbit/grid")
    dt=2*math.pi/n
    t=moment=0.0
    for i in range(n):
        y=a*math.cos((i+0.5)*dt)
        w=1+2*lam*y
        x=y+lam*y*y
        t+=w*dt
        moment+=x*w*dt
    return t,moment/t

def verify():
    cases=0
    for lam in (-0.4,-0.2,0,0.2,0.4):
        for a in (0.1,0.25,0.5,0.75,1.0):
            t,m=sample(lam,a)
            assert abs(t-2*math.pi)<1e-11
            assert abs(m-1.5*lam*a*a)<1e-11
            assert abs(((a+lam*a*a)-(-a+lam*a*a))-2*a)<1e-12
            cases+=1
    try: sample(0.5,1)
    except ValueError: pass
    else: raise AssertionError("singular shear accepted")
    print(f"{cases} orbit cases, period and mean match; singular shear rejected")
    for lam in (0,0.2,-0.2):
        print(lam,sample(lam,1))

if __name__=="__main__":
    verify()
