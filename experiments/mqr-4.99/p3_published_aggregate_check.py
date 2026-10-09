#!/usr/bin/env python3
"""Independent arithmetic check of *published* aggregate table, NOT original behavior events."""
import csv,io,math,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
source=ROOT/"sources"/"p3_diefenbach_published_table1.csv"
rows=list(csv.DictReader(io.StringIO(source.read_text(encoding="utf8"))))
assert len(rows)==10
def cell(species,kind,minutes):
 x=[r for r in rows if r["species"]==species and r["protocol"]==kind and float(r["minutes"])==minutes]
 assert len(x)==1
 return float(x[0]["availability"])
def sharp(q,lower,upper):
 assert 0<=q<=1 and 0<=lower<=upper<=1
 if q>upper:return None
 if q==0:return (0,1) if lower==0 else (0,0)
 return q/upper,q/max(q,lower)
for species,expected in [("HenslowSparrow",(0.435,0.501)),("GrasshopperSparrow",(0.115,0.211))]:
 p5,p10=expected
 assert cell(species,"song_only",5)==p5 and cell(species,"song_only",10)==p10
 for period in (5,10):
  assert cell(species,"song_and_visible",period)<=cell(species,"song_only",period)
 assert p10>=p5
 print(f"{species} observed_5={p5:.3f} observed_10={p10:.3f} model_reference_10={1-(1-p5)**2:.6f} NOT_A_HYPOTHESIS_TEST")
q=0.2 # constructed number, not measured detection frequency
lo,hi=sharp(q,0.34,0.49)
assert math.isclose(lo,20/49) and math.isclose(hi,10/17)
assert math.isclose(lo*0.49,q) and math.isclose(hi*0.34,q)
assert sharp(q,0,1)==(0.2,1.0)
assert sharp(0.6,0.34,0.49) is None
assert not math.isclose((.2*.8+.8*.2)/2,((.2+.8)/2)*((.8+.2)/2))
print(f"P3_PYTHON_CONDITIONAL_PASS hypothetical_q={q} transported_bound=({lo:.9f},{hi:.9f}) no_transport=(0.2,1.0)")
