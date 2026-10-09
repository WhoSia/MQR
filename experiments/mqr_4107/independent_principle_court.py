"""MQR-4.107 P4: independent physical principle vs shared calibration.
Synthetic only. Exhaustive exact rational model: raw shared readout y=t+d*q(t),
independent physical channel z=t with independently fixed semantics.
"""
from fractions import Fraction as F

def q(t):
    t=F(t)
    return t*(t-100)/10000

def raw(t,d):
    return F(t)+F(d)*q(t)

def independent(t):
    return F(t)

def recover_delta(y,z):
    if q(z)==0: raise ValueError("no curvature sensitivity")
    return (F(y)-F(z))/q(z)

for t in (F(150), F(200), F(250), F(300)):
    for d in range(-5,6):
        y=raw(t,d)
        z=independent(t)
        assert recover_delta(y,z)==d
for t in (0,100):
    try: recover_delta(raw(t,3),independent(t))
    except ValueError: pass
    else: raise AssertionError("must be unidentifiable at fixed point")
assert raw(250,2)==raw(250,2)  # replication shares the same calibration
print("PASS: 44 exact independent-reference recoveries and endpoint non-identifiability")
print("NECESSARY: independent channel z has warranted scale, distinct error ancestry")
print("HOLD: if z has unmodelled shared bias, this conditional identification is not a physical calibration certificate")
