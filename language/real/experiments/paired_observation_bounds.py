"""Sharp finite-cohort binary joint-count bounds under partial linkage.
Not a reanalysis of Live-seq or any biological dataset.
"""
from itertools import product
from collections import defaultdict


def bounds(n, a, b, paired):
    """paired=(n00,n01,n10,n11); a,b are total cohort marginal counts."""
    if not all(isinstance(x,int) and x>=0 for x in (n,a,b,*paired)) or len(paired)!=4:
        raise ValueError('nonnegative integer counts required')
    q00,q01,q10,q11=paired
    m=n-sum(paired); ar=a-q10-q11; br=b-q01-q11
    if not (0<=ar<=m and 0<=br<=m):
        raise ValueError('marginals inconsistent with paired observations')
    return q11+max(0,ar+br-m),q11+min(ar,br)


def verify():
    cases=0; sign_resolved=0; genuinely_new=0
    for n in range(1,8):
        # 4 cell counts for paired subcohort, 4 for unpaired.
        possible=defaultdict(set)
        for p in product(range(n+1),repeat=4):
            k=sum(p)
            if k>n: continue
            m=n-k
            for u00 in range(m+1):
                for u01 in range(m-u00+1):
                    for u10 in range(m-u00-u01+1):
                        u11=m-u00-u01-u10
                        a=p[2]+p[3]+u10+u11
                        b=p[1]+p[3]+u01+u11
                        possible[a,b,p].add(p[3]+u11)
        for (a,b,p),cs in possible.items():
            lo,hi=bounds(n,a,b,p)
            assert cs==set(range(lo,hi+1))
            raw_lo,raw_hi=bounds(n,a,b,(0,0,0,0))
            assert raw_lo<=lo<=hi<=raw_hi
            cases+=1
            if n*lo>a*b or n*hi<a*b:
                sign_resolved+=1
                if not (n*raw_lo>a*b or n*raw_hi<a*b): genuinely_new+=1
    # Same marginal observations and same number of linked cells, unlike paired data.
    assert bounds(8,4,4,(2,0,0,2))==(2,4)
    assert bounds(8,4,4,(0,2,2,0))==(0,2)
    # With five linked observations, positive or negative covariance is certified.
    assert bounds(8,4,4,(2,0,0,3))==(3,4)
    assert bounds(8,4,4,(0,2,3,0))==(0,1)
    for args in ((2,0,0,(0,0,0,1)),(1,1,1,(0,0,0,2))):
        try: bounds(*args)
        except ValueError: pass
        else: raise AssertionError(args)
    print(f'Exact linked-margin cases: {cases}; strictly signed: {sign_resolved}; sign newly resolved: {genuinely_new}')


if __name__=='__main__':
    verify()
