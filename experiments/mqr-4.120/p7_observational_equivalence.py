"""MQR 4.120 P7 exact rational observational-equivalence countermodels.
Synthetic classical causal nonidentification; not real institutional effects.
"""
from fractions import Fraction as Q

def law(model, intervene=None):
    out={}
    for u in (0,1):
        a=u if intervene is None else intervene
        y=u if model=="common_cause" else a
        out[(a,y)]=out.get((a,y),Q(0))+Q(1,2)
    return out

def mean_y(dist):
    return sum((Q(y)*p for (a,y),p in dist.items()),Q(0))

def effect(model):
    return mean_y(law(model,1))-mean_y(law(model,0))

def run():
    m0,m1="common_cause","direct_effect"
    expected={(0,0):Q(1,2),(1,1):Q(1,2)}
    assert law(m0)==law(m1)==expected
    assert effect(m0)==0
    assert effect(m1)==1
    assert law(m0,0)!=law(m1,0)
    assert law(m0,1)!=law(m1,1)
    # Under consistency, observed diagonal fair binary law imposes
    # E Y(1) in [1/2,1], E Y(0) in [0,1/2] => ATE in [0,1].
    # Both endpoints are attained by the two constructed SCMs.
    lower,upper=Q(0),Q(1)
    assert lower==effect(m0) and upper==effect(m1)
    print("Observed law", expected)
    print("ATE endpoints",lower,upper)
    print("PASS: exact rational synthetic nonidentification witness")
if __name__=="__main__":run()
