from fractions import Fraction as F
# Identical selected-record distribution; different underlying result prevalence.
models = {
 "I": {"p": F(1,2), "r1": F(1,2), "r0": F(1,2)}, # MCAR
 "II":{"p": F(1,4), "r1": F(1),   "r0": F(1,3)}  # MNAR
}
def observed(m):
 p,r1,r0=m["p"],m["r1"],m["r0"]
 return (p*r1,(1-p)*r0)
assert observed(models["I"])==observed(models["II"])==(F(1,4),F(1,4))
assert models["I"]["p"]!=models["II"]["p"]
# Audit of the unseen sampling frame (true p) separates worlds.
assert (models["I"]["p"],observed(models["I"]))!=(models["II"]["p"],observed(models["II"]))
print("PASS same observed retained counts, different underlying prevalences and mechanisms")
