"""MQR-4.109 P2: source-table arithmetic, same measurand rival court.

Regnault 1847, printed p241, table derived from graphical constructions.
Only published table entries used, not underlying raw readings or curves.
"""
from fractions import Fraction as F

T = F(250)
published = {
    "crystal_choisy": F(253),
    "ordinary_glass_5": F("250.05"),
    "green_glass_10": F("251.85"),
    "swedish_glass_11": F("251.44"),
}
offset = {k: v-T for k,v in published.items()}
assert offset == {
    "crystal_choisy": F(3),
    "ordinary_glass_5": F("0.05"),
    "green_glass_10": F("1.85"),
    "swedish_glass_11": F("1.44"),
}
assert max(published.values()) - min(published.values()) == F("2.95")
# Distinguish statement "values differ in reported table" from
# "one thermometer is correct"; latter requires uncertainty/model/
# reference legitimacy not supplied by this arithmetic.
# Same-target finite model: theta=250 by reported AIR scale convention,
# not a certified thermodynamic temperature or independent truth.
correctness = "UNDECIDABLE_FROM_TABLE_ONLY"
assert correctness == "UNDECIDABLE_FROM_TABLE_ONLY"
print("PASS published p241 at air-grid 250: offsets", offset)
print("PASS maximum table spread", F("2.95"), "deg C")
print("HOLD independent physical traceability, original-graph point status and novel warrant")
