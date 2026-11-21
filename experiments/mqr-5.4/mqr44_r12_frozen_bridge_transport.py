"""MQR 5.4 R12: cross-field bridge frozen before shift, exact zero/one-loss controls."""
from fractions import Fraction as Q
from itertools import product
S=tuple(product((0,1),repeat=2))

def p(kind,s):
    if kind=='aligned':return Q(1,2) if s[0]==s[1] else Q(0)
    if kind=='anti':return Q(1,2) if s[0]!=s[1] else Q(0)
    if kind=='independent':return Q(1,4)
    raise ValueError(kind)

def accuracy(kind,predictor,target=1):
    return sum((p(kind,s) for s in S if predictor(s)==s[target]),Q(0))

def tests():
    frozen_identity=lambda s:s[0]
    frozen_inverted=lambda s:1-s[0]
    direct_y=lambda s:s[1]
    assert accuracy('aligned',frozen_identity)==1
    assert accuracy('anti',frozen_identity)==0
    assert accuracy('independent',frozen_identity)==Q(1,2)
    assert accuracy('aligned',frozen_inverted)==0
    assert accuracy('anti',frozen_inverted)==1
    assert all(accuracy(d,direct_y)==1 for d in ('aligned','anti','independent'))
    assert all(accuracy(d,lambda s:s[0],target=0)==1 for d in ('aligned','anti','independent'))
    assert all(sum((p(d,s) for s in S),Q(0))==1 for d in ('aligned','anti','independent'))
    return True
if __name__=='__main__':
    assert tests()
    print('PASS 8 exact assertions; all source distributions hypothetical')
    print([(d,str(accuracy(d,lambda s:s[0]))) for d in ('aligned','anti','independent')])
