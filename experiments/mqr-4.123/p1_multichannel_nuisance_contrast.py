#!/usr/bin/env python3
"""MQR-4.123 P1: exact rational 3-channel nuisance annihilation and failure."""
from fractions import Fraction as Q
from itertools import product

one=(Q(1),Q(1),Q(1))
drift=(Q(0),Q(1),Q(2))
w=(Q(1),Q(-2),Q(1))
signal=(Q(3,10),Q(0),Q(3,10))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def raw(h,b,c):return add(add(scale(b,one),scale(c,drift)),scale(h,signal))
def interval(center,radius):return(center-radius,center+radius)
def overlap(x,y):return max(x[0],y[0])<=min(x[1],y[1])
assert dot(w,one)==dot(w,drift)==0
assert dot(w,signal)==Q(3,5)
for b,c in product((Q(-4),Q(0),Q(3,2)),(Q(-2),Q(1,4))):
    assert dot(w,raw(Q(0),b,c))==0
    assert dot(w,raw(Q(1),b,c))==Q(3,5)
# All three channel errors bounded independently by eps => contrast error radius ||w||_1 eps=4 eps.
eps=Q(1,20)
radius=sum(map(abs,w))*eps
a,b=interval(Q(0),radius),interval(Q(3,5),radius)
assert not overlap(a,b)
assert b[0]-a[1]==Q(1,5)
# If a *new* nuisance enters in the exact signal direction, any real coefficient
# range containing both 0 and -1 can erase the distinction.
assert raw(Q(0),Q(0),Q(0))==add(raw(Q(1),Q(0),Q(0)),scale(Q(-1),signal))
# With eps = 1/10, even the ideal 3-channel bounded-error contrast overlaps.
large=Q(1,10)
assert overlap(interval(Q(0),4*large),interval(Q(3,5),4*large))
# A separate independent calibration channel for the signal-aligned nuisance t
# can recover separation if it bounds t tightly enough.
# New nuisance shift in contrast: t*(3/5). If |t|<=1/10,
# full contrast error radius = 4eps+3/50, gap = 3/5-2*(4eps+3/50)=2/25.
eta=Q(1,10)
r=radius+eta*dot(w,signal)
assert Q(3,5)-2*r==Q(2,25)
assert not overlap(interval(Q(0),r),interval(Q(3,5),r))
print("MQR_4123_P1_NULLSPACE_IDENTITY=PASS")
print("MQR_4123_P1_MULTICHANNEL_BOUNDED_ERROR_MARGIN=1/5")
print("MQR_4123_P1_ALIGNED_NUISANCE_ERASES_SIGNAL=PASS")
print("MQR_4123_P1_INDEPENDENT_CALIBRATION_MARGIN=2/25")
print("MQR_4123_P1_EMPIRICAL_IDENTIFICATION=HOLD")
