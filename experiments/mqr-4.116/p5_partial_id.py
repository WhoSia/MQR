from fractions import Fraction as F
q1=q0=F(1,4)
def bounds(G):
 return max(q1,q1/(q1+G*q0)),min(1-q0,G*q1/(q0+G*q1))
assert bounds(1)==(F(1,2),F(1,2))
assert bounds(2)==(F(1,3),F(2,3))
assert bounds(3)==(F(1,4),F(3,4))
print('PASS',*[str(bounds(g)) for g in (1,2,3)])
