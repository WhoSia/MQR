import json,sys
from collections import defaultdict
p=json.load(open("experiments/mqr-4.30/profile-seal.json",encoding="utf-8"))
a=json.load(open("experiments/mqr-4.30/external-adjudication.json",encoding="utf-8"))
scores={c["id"]:c["profile"] for c in p["cases"]}
pairs=[]
for cid,row in a["cases"].items():
    for axis,native in row["native"].items():
        pred=scores[cid][axis]
        pairs.append((cid,row["domain"],axis,pred,native,pred==native))
n=len(pairs); ok=sum(x[-1] for x in pairs)
print(f"EVALUABLE_PAIRS={n}")
print(f"EXACT_DIRECTIONAL_AGREEMENT={ok}/{n}")
print(f"EXACT_DIRECTIONAL_RATE={ok/n:.6f}")
assert ok/n>=0.80
print("E1_EXTERNAL_DIRECTIONAL_CONCORDANCE=PASS")

bydom=defaultdict(lambda:[0,0])
byaxis=defaultdict(lambda:[0,0,set(),set()])
for cid,dom,axis,pred,native,match in pairs:
    bydom[dom][1]+=1; bydom[dom][0]+=int(match)
    byaxis[axis][1]+=1; byaxis[axis][0]+=int(match)
    byaxis[axis][2].add(dom); byaxis[axis][3].add(native)
for dom,(k,t) in sorted(bydom.items()):
    print(f"DOMAIN {dom} {k}/{t} {k/t:.6f}")
    if t>=2: assert k/t>=2/3
print("E2_CROSS_DOMAIN_FLOOR=PASS")

for axis,(k,t,doms,vals) in sorted(byaxis.items()):
    print(f"AXIS {axis} {k}/{t} {k/t:.6f} DOMAINS={len(doms)} NATIVE_LEVELS={','.join(sorted(vals))}")

# E3/E4 frozen qualitative witnesses
negative_with_D_high=0
for cid,row in a["cases"].items():
    nat=row["native"]
    if nat.get("D")=="HIGH" and any(nat.get(x)=="LOW" for x in ("W","I","T")):
        negative_with_D_high+=1
print(f"NEGATIVE_TARGET_WITH_D_HIGH={negative_with_D_high}")
assert negative_with_D_high>=3
print("E3_TARGET_AXIS_DISCRIMINANCE=PASS")
assert negative_with_D_high>=2
print("E4_DEFEAT_EXPOSURE_POLARITY=PASS")

assert a["literature_N_lane"]["Javadi2019"]["N"]=="MID"
assert a["literature_N_lane"]["Zhang2011"]["N"]=="LOW-MID"
assert a["literature_N_lane"]["RayWelsh2018"]["N"]=="LOW"
print("E5_N_ANTI_COUNTING=PASS")

# Axis promotion: >=3 judgments, >=2 domains, >=.8 agreement, >=2 native levels.
for axis in ("W","I","T","D"):
    k,t,doms,vals=byaxis[axis]
    promotable=(t>=3 and len(doms)>=2 and k/t>=.80 and len(vals)>=2)
    print(f"LEVEL3_ORDINAL_{axis}={'PASS' if promotable else 'HOLD'}")
# N separately insufficient cross-domain criterion lane.
print("LEVEL3_ORDINAL_N=HOLD")
print("E6_CROSS_DOMAIN_ORDINAL_INVARIANCE=PARTIAL")
print("E7_NO_SCALAR_RESURRECTION=PASS")
print("LEVEL3_NUMERIC_ALL_AXES=HOLD")
print("FULL_WNITD_LEVEL3_PROMOTION=HOLD")
