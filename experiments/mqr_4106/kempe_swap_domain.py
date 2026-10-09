"""Minimal frozen-domain Kempe swap counterexample; NOT Heawood 1890."""
E=[(0,1),(1,2),(0,2)]
C={0:"B",1:"R",2:"G"}
def valid(c): return all(c[a]!=c[b] for a,b in E)
def swap_fixed(c,vertices,x,y):
 d=c.copy()
 for v in vertices:
  if d[v]==x: d[v]=y
  elif d[v]==y: d[v]=x
 return d
assert valid(C)
A={0,1}; B={1,2}
assert valid(swap_fixed(C,A,"B","R"))
assert valid(swap_fixed(C,B,"R","G"))
first=swap_fixed(C,A,"B","R")
frozen_second=swap_fixed(first,B,"R","G")
assert not valid(frozen_second)
print("Original:",C)
print("Individually valid:",swap_fixed(C,A,"B","R"),swap_fixed(C,B,"R","G"))
print("Frozen sequential application invalid:",frozen_second)
print("This does NOT establish the actual historical 25-vertex Heawood witness.")
