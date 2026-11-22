"""Two causal models with the SAME paired-test data but different interventions.

Synthetic exact-rational counterexample, not data about actual memory systems.
S: one shared memory bit H, reported with independent 3/4-accurate noise.
M: independent memory bits M_A,M_B; each task chooses, at random, to report
its own memory bit or a shared method/context bit C (each 1/2).
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

HALF, P = F(1,2), F(3,4)

def shared_memory(do_h=None):
    out=defaultdict(F)
    for h,ea,eb in product((0,1), repeat=3):
        if do_h is not None and h!=do_h: continue
        ph=HALF if do_h is None else F(1)
        # Error bits with P(no error)=3/4
        p=ph*(1-P if ea else P)*(1-P if eb else P)
        out[(h^ea,h^eb)]+=p
    return dict(out)

def independent_memories_shared_method(do_ma=None):
    out=defaultdict(F)
    # C and independent memories are all fair; S=1 samples memory, S=0 method
    for c,ma,mb,sa,sb in product((0,1),repeat=5):
        if do_ma is not None and ma!=do_ma: continue
        pm=F(1) if do_ma is not None else HALF
        weight=HALF*pm*HALF*HALF*HALF
        a=ma if sa else c
        b=mb if sb else c
        out[(a,b)]+=weight
    return dict(out)

def marginals(joint):
    return tuple(sum(p for (a,b),p in joint.items() if (a,b)[i]==1) for i in (0,1))

def correlation(joint):
    ea,eb=marginals(joint)
    covariance=joint[(1,1)]-ea*eb
    return covariance/(ea*(1-ea))

def verify():
    s=shared_memory(); m=independent_memories_shared_method()
    assert s==m=={(0,0):F(5,16),(0,1):F(3,16),
                    (1,0):F(3,16),(1,1):F(5,16)}
    assert sum(s.values())==1 and correlation(s)==F(1,4)
    assert marginals(s)==(HALF,HALF)
    # do(H=1) acts on *both* tasks in S.
    assert marginals(shared_memory(do_h=1))==(P,P)
    # do(M_A=1) acts on only its own task in M.
    assert marginals(independent_memories_shared_method(do_ma=1))==(P,HALF)
    assert shared_memory(do_h=1)!=independent_memories_shared_method(do_ma=1)
    return 'PASS: matched 4-cell observational distribution; intervention changes both vs only A'

if __name__=='__main__':
    print(verify())
