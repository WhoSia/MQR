"""MQR44 R11: synthetic data-transfer and preserved-purpose gates; stdlib only.

Not an experimental dataset. Each world distribution is stipulated, not learned.
"""
from fractions import Fraction as Q
from itertools import product

STATES = tuple(product((0, 1), repeat=2))

def joint(kind):
    if kind == 'aligned':
        return {s: Q(1,2) if s[0] == s[1] else Q(0) for s in STATES}
    if kind == 'anti':
        return {s: Q(1,2) if s[0] != s[1] else Q(0) for s in STATES}
    if kind == 'independent':
        return {s: Q(1,4) for s in STATES}
    raise ValueError(kind)

def acc(law, code, target):
    # Bayes-optimal target-specific readout. An absent code value contributes zero.
    return sum((max(sum(p for s,p in law.items() if code(s)==z and s[target]==k)
                    for k in (0,1)) for z in (0,1)), Q(0))

def cond_prob(law, event):
    return sum((p for s,p in law.items() if event(s)), Q(0))

def label(law, code, target, floor=Q(9,10)):
    return 'PASS' if acc(law, code, target) >= floor else 'FAIL'

def profile(law, code):
    return (label(law,code,0), label(law,code,1))

def tests():
    code_x = lambda s:s[0]
    code_y = lambda s:s[1]
    assert all(sum(joint(d).values(), Q(0))==1 for d in ('aligned','anti','independent'))
    assert all(cond_prob(joint(d),lambda s:s[0]==0)==Q(1,2)
               for d in ('aligned','anti','independent'))
    assert all(cond_prob(joint(d),lambda s:s[1]==0)==Q(1,2)
               for d in ('aligned','anti','independent'))
    assert acc(joint('aligned'),code_x,1)==1
    assert acc(joint('anti'),code_x,1)==1  # decoder refit: inversion allowed
    assert acc(joint('independent'),code_x,1)==Q(1,2)
    assert profile(joint('aligned'),code_x)==('PASS','PASS')
    assert profile(joint('independent'),code_x)==('PASS','FAIL')
    assert profile(joint('independent'),code_y)==('FAIL','PASS')
    assert cond_prob(joint('aligned'),lambda s:s[0]==s[1])==1
    assert cond_prob(joint('anti'),lambda s:s[0]==s[1])==0
    assert cond_prob(joint('independent'),lambda s:s[0]==s[1])==Q(1,2)
    return True

if __name__=='__main__':
    assert tests()
    print('PASS 12 exact tests (synthetic data only)')
    for d in ('aligned','anti','independent'):
        print(d, 'P(X=Y)', cond_prob(joint(d),lambda s:s[0]==s[1]),
              'X-only target accuracies',acc(joint(d),lambda s:s[0],0),acc(joint(d),lambda s:s[0],1))
