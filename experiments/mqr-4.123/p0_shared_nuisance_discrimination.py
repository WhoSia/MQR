#!/usr/bin/env python3
"""MQR 4.123 P0: exact rational nuisance-relative discrimination fixture."""
from fractions import Fraction as Q

delta=Q(3,10)
def interval(center,radius):
    return center-radius,center+radius
def overlap(x,y):
    return max(x[0],y[0]) <= min(x[1],y[1])
def gap(x,y):
    return max(Q(0),max(y[0]-x[1],x[0]-y[1]))
def contrast(eta,eps):
    radius=eta+2*eps
    return interval(Q(0),radius),interval(delta,radius)

assert overlap(interval(Q(0),Q(1)),interval(delta,Q(1)))
assert not overlap(interval(Q(0),Q(0)),interval(delta,Q(0)))
a,b=contrast(Q(1,20),Q(1,100))
assert not overlap(a,b)
assert gap(a,b)==Q(4,25)
c,d=contrast(Q(1,5),Q(1,100))
assert overlap(c,d)
assert delta > 2*Q(1,20)+4*Q(1,100)
assert delta <= 2*Q(1,5)+4*Q(1,100)
print("MQR_4123_P0_SHARED_BIAS_PAIRED_CONTRAST=PASS")
print("MQR_4123_P0_BOUNDED_DRIFT_MARGIN=4/25")
print("MQR_4123_P0_LARGE_DRIFT_OVERLAP=PASS")
print("MQR_4123_P0_ORIGINAL_DATA_EXPERIMENTAL_DISCRIMINATION=HOLD")
