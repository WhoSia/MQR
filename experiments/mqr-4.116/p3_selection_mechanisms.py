# Finite selection mechanism diagnostic. Constructed examples, not observed populations.
from itertools import product
from fractions import Fraction
records=list(product((0,1),repeat=2)) # A=authority observed; Y=claim-relevant hidden result
def prop(sel, a,y): return Fraction(sel(a,y),4)
def compare(sel):
    rows=[(a,y,prop(sel,a,y)) for a,y in records]
    # conditional differences exactly inspectable in deliberately specified mechanisms
    return rows
mcar=lambda a,y: Fraction(1,2)
mar=lambda a,y: Fraction(3,4) if a else Fraction(1,4)
mnar=lambda a,y: Fraction(3,4) if y else Fraction(1,4)
assert all(mcar(a,y)==Fraction(1,2) for a,y in records)
assert all(mar(a,0)==mar(a,1) for a in (0,1))
assert all(mnar(0,y)==mnar(1,y) for y in (0,1))
assert mnar(0,0)!=mnar(0,1)
# Marginal published fraction with equal priors on Y:
def observed_y_rate(sel):
    top=sum((Fraction(1,4)*sel(a,y) for a,y in records if y==1),Fraction(0))
    den=sum((Fraction(1,4)*sel(a,y) for a,y in records),Fraction(0))
    return top/den
assert observed_y_rate(mcar)==Fraction(1,2)
assert observed_y_rate(mar)==Fraction(1,2)
assert observed_y_rate(mnar)==Fraction(3,4)
print('PASS 3 mechanisms; selection observed Y rates',[(s, str(observed_y_rate(f))) for s,f in [('MCAR',mcar),('MAR',mar),('MNAR',mnar)]])
