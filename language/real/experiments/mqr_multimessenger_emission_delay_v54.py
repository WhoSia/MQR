"""Two-messenger time-delay identification with an unknown source lag.

Toy normalized distances; NOT real GW170817 measurements.
"""
from fractions import Fraction as F

def observed(delay_at_emission, slope, distance):
    return F(delay_at_emission)+F(slope)*F(distance)

def fit_common_intrinsic_lag(two_events):
    (d1,t1),(d2,t2)=two_events
    d1,d2,t1,t2=map(F,(d1,d2,t1,t2))
    assert d1 != d2
    k=(t2-t1)/(d2-d1)
    e=t1-k*d1
    return e,k

def verify():
    one=(F(1),F(2))
    assert observed(1,1,one[0])==2
    assert observed(2,0,one[0])==2
    a=(F(1),F(2));b=(F(3),F(4))
    assert fit_common_intrinsic_lag((a,b))==(F(1),F(1))
    for slope in (F(-3),F(0),F(1),F(6)):
        # Separate source delays allow the same observations with any propagation slope.
        e1=a[1]-slope*a[0]
        e2=b[1]-slope*b[0]
        assert observed(e1,slope,a[0])==a[1]
        assert observed(e2,slope,b[0])==b[1]
    return 'PASS: 1-event emission/propagation confounding; 2 distances identify slope ONLY with shared source-lag assumption'

if __name__=='__main__':print(verify())
