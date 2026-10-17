from itertools import product
W=list(product((0,1),repeat=2))
def J(w):return w==(1,0)
def O(w,keep_i,keep_d):return (w[0] if keep_i else None,w[1] if keep_d else None)
def ambiguous(a,b):
 obs={O(w,a,b) for w in W}
 return sum(len({J(w) for w in W if O(w,a,b)==o})>1 for o in obs)
assert [ambiguous(a,b) for a,b in [(1,1),(0,1),(1,0),(0,0)]]==[0,1,1,1]
print('PASS four missingness regimes')
