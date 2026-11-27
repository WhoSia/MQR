"""Independent finite calibration bounds for the measurement-reactivity model."""
from itertools import product
from measurement_reactivity_check import exact_group, extrema, feasible, cost


def linked_total_bounds(g0,g1,k,b):
    n0,n1=sum(g0),sum(g1)
    l1,u1=g1[1],g1[1]+g1[2]
    l2,u2=b-g0[1]-g0[2],b-g0[1]
    if max(l1-u2,l2-u1,0)>k: return None
    lo=max(0,b-n0,l1-k,l2-k,-(-(l1+l2-k)//2))
    hi=min(n1,b,u1+k,u2+k,(u1+u2+k)//2)
    if lo>hi: return None
    return lo,hi


def mismatch_bounds(n,a,b):
    return abs(a-b),min(a+b,2*n-a-b)


def verify():
    groups=[g for g in product(range(5),repeat=3) if 1<=sum(g)<=4]
    tables={g:exact_group(g) for g in groups}
    cases=inconsistent=tightened=new_sign=0
    for g0,g1 in product(groups,repeat=2):
        n0,n1=sum(g0),sum(g1)
        for k in range(g0[0]+g0[1]+g1[0]+g1[1]+1):
            c_lo,c_hi=extrema(g0,g1,k)
            for b in range(n0+n1+1):
                actual={x1 for x0,d0 in tables[g0].items() for x1,d1 in tables[g1].items() if x0+x1==b and d0+d1<=k}
                interval=linked_total_bounds(g0,g1,k,b)
                cases+=1
                if interval is None:
                    assert not actual; inconsistent+=1;continue
                lo,hi=interval
                assert actual==set(range(lo,hi+1))
                a_lo,a_hi=(n0+n1)*lo-n1*b,(n0+n1)*hi-n1*b
                assert c_lo<=a_lo<=a_hi<=c_hi
                tightened+=a_lo>c_lo or a_hi<c_hi
                new_sign+=(a_lo>0 or a_hi<0) and not(c_lo>0 or c_hi<0)
    count=0
    for n in range(1,8):
        possible={}
        for x in product((0,1),repeat=n):
            for y in product((0,1),repeat=n):
                possible.setdefault((sum(x),sum(y)),set()).add(sum(a!=b for a,b in zip(x,y)))
        for (a,b),ds in possible.items():
            lo,hi=mismatch_bounds(n,a,b)
            assert ds==set(range(lo,hi+1,2));count+=1
        assert mismatch_bounds(n,n//2,n//2)==(0,2*(n//2))
    print(f'total calibration: {cases} cases, {inconsistent} inconsistent, {tightened} strictly tightened, {new_sign} newly signed')
    print(f'mismatch calibration: {count} margin patterns; exact endpoints and parity verified')
    # Example: same total mean plus a tight mismatch budget can certify contrast.
    for k in range(5):
        print(k,linked_total_bounds((4,0,1),(0,4,1),k,5))

def verify_nested():
    comparisons=0
    for g in product(range(6),repeat=3):
        n=sum(g)
        if not 1<=n<=5: continue
        for a in range(g[2]+1):
            for b in range(g[2]-a+1):
                h=(g[0]+a,g[1]+b,g[2]-a-b)
                for c in range(n+1):
                    assert cost(g[1],g[2],c)<=cost(h[1],h[2],c)
                    comparisons+=1
    old=((3,0,1),(0,3,1)); new=((3,1,0),(1,3,0))
    assert extrema(*old,1)==(4,16)
    assert extrema(*new,1)==(4,12)
    assert extrema(*new,2)==(0,16)
    assert (2,2) not in feasible(*old,1) and (2,2) in feasible(*new,2)
    assert (1,3) in feasible(*old,1)&feasible(*new,2)
    print(f'nested comparisons: {comparisons}; fixed budget (4,12); replacement (0,16)')

if __name__=='__main__':
    verify()
    verify_nested()
