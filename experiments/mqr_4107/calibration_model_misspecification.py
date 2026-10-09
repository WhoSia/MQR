from fractions import Fraction as F

def q(t):
    t=F(t)
    return t*(t-100)/10000

def r(t):
    t=F(t)
    return t*(t-100)*(t-250)/1000000

def reading(t,d,h):
    return F(t)+F(d)*q(t)+F(h)*r(t)

def det(a,b):
    return q(a)*r(b)-q(b)*r(a)

def solve(a,b,ya,yb):
    z=det(a,b)
    if not z: raise ValueError("rank deficient")
    u,v=F(ya)-a,F(yb)-b
    return (u*r(b)-v*r(a))/z,(q(a)*v-q(b)*u)/z

assert all(reading(t,2,7)==t for t in (0,100))
assert r(250)==0 and q(250)==F(15,4)
assert det(250,300)==F(45,4)
assert reading(250,2,0)==reading(250,2,7)
assert reading(300,2,0)!=reading(300,2,7)
for d in range(-3,4):
    for h in range(-3,4):
        assert solve(250,300,reading(250,d,h),reading(300,d,h))==(F(d),F(h))
print("Exact fractional coefficient matrix at 250,300:",(q(250),r(250)),(q(300),r(300)))
print("Determinant:",det(250,300))
print("PASS: two-parameter identifiability with two independent off-endpoint anchors.")
print("Not a Regnault historical data fit. Model completeness still unproven.")
