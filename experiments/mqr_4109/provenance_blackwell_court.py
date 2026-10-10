"""MQR-4.109 P1 finite experiment vs documentary authorization.
Constructed example, not historical Regnault data; no new Blackwell theorem.
"""
from fractions import Fraction as F
from itertools import product

THETA=(0,1)
X=(0,1)
E={(t,x): F(3,4) if t==x else F(1,4) for t,x in product(THETA,X)}
K={(x,y): F(int(x==y)) for x,y in product(X,X)}
Y={(t,y): sum(E[t,x]*K[x,y] for x in X) for t,y in product(THETA,X)}
assert E==Y
assert all(sum(K[x,y] for y in X)==1 for x in X)
for t,y in product(THETA,X):
    assert E[t,y]==sum(Y[t,x]*K[x,y] for x in X)
for kernel in (E,Y):
    risk=sum(F(1,2)*sum(kernel[t,x] for x in X if x!=t) for t in THETA)
    assert risk==F(1,4)

def traceability_claim(authenticated_chain:bool,complete_uncertainties:bool)->bool:
    return authenticated_chain and complete_uncertainties
assert traceability_claim(True,True)
assert not traceability_claim(False,True)
assert not traceability_claim(True,False)
assert not traceability_claim(False,False)
A=(F(0),F(2)); B=(F(1),F(1))
mean=lambda z:sum(z,F(0))/len(z)
ss=lambda z:sum((v-mean(z))**2 for v in z)
assert mean(A)==mean(B)==1 and ss(A)==2 and ss(B)==0
print("PASS: 2x2 exactly Blackwell-equivalent kernels, prior risk=1/4")
print("PASS: same likelihood with different externally stipulated certificate status")
print("PASS: normal mean compression loses unknown-variance residual scatter")
print("STATUS: local synthetic contract only; novelty and historical transport HOLD")
