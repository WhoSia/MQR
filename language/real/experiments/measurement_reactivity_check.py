"""Finite cohort selection + bounded individual measurement reactivity."""
from itertools import product
from fractions import Fraction


def cost(pos, missing, total):
    return max(0, pos-total, total-pos-missing)


def feasible(g0, g1, k):
    # Group triples: observed negatives, observed positives, unobserved.
    return {(a,b) for a in range(sum(g0)+1) for b in range(sum(g1)+1)
            if cost(g0[1],g0[2],a)+cost(g1[1],g1[2],b)<=k}


def extrema(g0,g1,k):
    n0,n1=sum(g0),sum(g1)
    if min(n0,n1)<=0: raise ValueError('empty baseline group')
    # D=n0*c1-n1*c0, sign of unmeasured baseline-group contrast.
    def allocate(a,wa,b,wb):
        if wa<wb: a,b,wa,wb=b,a,wb,wa
        x=min(a,k)
        return wa*x+wb*min(b,k-x)
    lo=n0*g1[1]-n1*(g0[1]+g0[2])-allocate(g1[1],n0,g0[0],n1)
    hi=n0*(g1[1]+g1[2])-n1*g0[1]+allocate(g1[0],n0,g0[1],n1)
    return lo,hi


def exact_group(g):
    obs=(0,)*g[0]+(1,)*g[1]
    result={}
    for y in product((0,1),repeat=sum(g)):
        c=sum(y); d=sum(a!=b for a,b in zip(y,obs))
        result[c]=min(result.get(c,d),d)
    return result


def verify():
    groups=[g for g in product(range(5),repeat=3) if 1<=sum(g)<=4]
    actual={g:exact_group(g) for g in groups}
    cases=robust=0
    for g0,g1 in product(groups,repeat=2):
        for k in range(g0[0]+g0[1]+g1[0]+g1[1]+1):
            truth={(a,b) for a,c in actual[g0].items() for b,d in actual[g1].items() if c+d<=k}
            assert truth==feasible(g0,g1,k)
            ds=[sum(g0)*b-sum(g1)*a for a,b in truth]
            assert extrema(g0,g1,k)==(min(ds),max(ds))
            lo,hi=min(ds),max(ds)
            robust+=lo>0 or hi<0;cases+=1
    assert [extrema((4,0,1),(0,4,1),k) for k in range(5)]==[(15,25),(10,25),(5,25),(0,25),(-5,25)]
    # Mean equality across observation regimes is compatible with opposite association.
    x=(0,1); measured=(0,1); untouched=(1,0)
    cov=lambda y: Fraction(sum(a*b for a,b in zip(x,y)),2)-Fraction(sum(x)*sum(y),4)
    assert sum(measured)==sum(untouched) and cov(measured)==-cov(untouched)==Fraction(1,4)
    print(f'{len(groups)} group patterns; {cases} exact cases; {robust} strict sign cases')
    print('balanced example:',[extrema((4,0,1),(0,4,1),k) for k in range(5)])

if __name__=='__main__': verify()
