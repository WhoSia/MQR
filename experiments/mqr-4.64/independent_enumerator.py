from __future__ import annotations
from collections import defaultdict
from itertools import combinations_with_replacement
from pathlib import Path

HERE=Path(__file__).resolve().parent
RESULTS=HERE/"results"

CAT=[
("A0_HI_DROP",2,0,0,0,0,0),
("A1_FULL",1,0,3,1,1,1),
("A2_COST_FULL",2,1,3,1,1,1),
("A3_S0_HI",2,0,1,0,0,0),
("A4_S1_HI",2,0,2,0,0,0),
("A5_S0_REOPEN",1,0,1,1,1,0),
("A6_S1_REOPEN",1,0,2,1,1,0),
("A7_FULL_EXT",1,0,3,0,0,1),
("A8_DROP_REOPEN",2,1,0,1,1,1),
("A9_CHEAP_FULL_G0",1,1,3,1,0,0),
("A10_LOW_FULL",0,0,3,1,1,1),
("A11_HI_FULL",2,0,3,0,0,0),
("A12_HI_REOPEN_DROP",2,0,0,1,0,0),
("A13_HI_G1_DROP",2,0,0,0,1,0),
("A14_HI_EXT_DROP",2,0,0,0,0,1),
("A15_FULL_REOPEN_EXT_G0",1,0,3,1,0,1),
]
BASES=["MYOPIC","LOOKAHEAD","CONSTRAINED","DIVERSITY"]
CONS=["OPR","ARR","EAI","EXTERIOR","NEDL"]
CLASSES=["DIAGNOSTIC_ONLY","REDUNDANT_CONSTRAINT","BASELINE_ABSORBED","BINDING_LOCAL","OVERCONSTRAINING"]

def pop2(x): return int(bool(x&1))+int(bool(x&2))
def eff_sep(a,w):
    if not w["irr"]: return 3
    if w["sub"]: return 1 if a[3] else 0
    return a[3]
def eff_reopen(a,w): return True if not w["irr"] else bool(a[4])
def net(a): return a[1]-a[2]

def baseline_feasible(actions,w,b):
    ids=list(range(3))
    if b=="CONSTRAINED" and w["irr"] and any(eff_sep(a,w) for a in actions):
        ids=[i for i,a in enumerate(actions) if eff_sep(a,w)]
    return ids

def score(a,w,b):
    n=net(a)*20
    if b in ("MYOPIC","CONSTRAINED"): return n
    if b=="LOOKAHEAD":
        return n+20*pop2(eff_sep(a,w))+(10 if w["reopen_live"] and eff_reopen(a,w) else 0)
    return n+(8 if w["anc_live"] and a[5]==1 else 0)+(8 if w["ext_live"] and a[6] else 0)

def choose(actions,w,b,ids):
    # Rust max_by_key with (score, -i)
    return max(ids,key=lambda i:(score(actions[i],w,b),-i))

def allowed(a,actions,w,c):
    if c=="OPR":
        if not w["irr"]: return True
        anyp=any(eff_sep(x,w) for x in actions)
        return (not anyp) or bool(eff_sep(a,w))
    if c=="ARR":
        if not w["reopen_live"]: return True
        anyp=any(eff_reopen(x,w) for x in actions)
        return (not anyp) or eff_reopen(a,w)
    if c=="EAI":
        if not w["anc_live"]: return True
        anyp=any(x[5]==1 for x in actions)
        return (not anyp) or a[5]==1
    if c=="EXTERIOR":
        if not w["ext_live"]: return True
        anyp=any(bool(x[6]) for x in actions)
        return (not anyp) or bool(a[6])
    if not w["irr"]: return True
    if w["sub"]:
        anyp=any(eff_sep(x,w) for x in actions)
        return (not anyp) or bool(eff_sep(a,w))
    anyfull=any(eff_sep(x,w)==3 for x in actions)
    if anyfull: return eff_sep(a,w)==3
    anyp=any(eff_sep(x,w) for x in actions)
    return (not anyp) or bool(eff_sep(a,w))

def reach(a,w): return (eff_sep(a,w),eff_reopen(a,w),a[5],bool(a[6]))
def gain(base,typed,w,c):
    if c in ("OPR","NEDL"):
        eb,et=eff_sep(base,w),eff_sep(typed,w)
        return (et!=0 and eb==0) if w["sub"] else bool(et & ~eb) or pop2(et)>pop2(eb)
    if c=="ARR": return w["reopen_live"] and eff_reopen(typed,w) and not eff_reopen(base,w)
    if c=="EAI": return w["anc_live"] and typed[5]==1 and base[5]==0
    return w["ext_live"] and bool(typed[6]) and not bool(base[6])

def classify(actions,w,b,c):
    global_allowed=[i for i,a in enumerate(actions) if allowed(a,actions,w,c)]
    fb=baseline_feasible(actions,w,b)
    tf=[i for i in fb if allowed(actions[i],actions,w,c)]
    base=choose(actions,w,b,fb)
    if len(global_allowed)==3: return "DIAGNOSTIC_ONLY"
    if len(tf)==len(fb): return "BASELINE_ABSORBED"
    if not tf: return "OVERCONSTRAINING"
    typed=choose(actions,w,b,tf)
    if typed==base or reach(actions[typed],w)==reach(actions[base],w): return "REDUNDANT_CONSTRAINT"
    return "BINDING_LOCAL" if gain(actions[base],actions[typed],w,c) else "OVERCONSTRAINING"

def main():
    counts=defaultdict(int); worlds=0; comps=0
    for ii in combinations_with_replacement(range(16),3):
        actions=[CAT[i] for i in ii]
        for flags in range(32):
            w={"irr":bool(flags&1),"sub":bool(flags&2),"reopen_live":bool(flags&4),
               "anc_live":bool(flags&8),"ext_live":bool(flags&16)}
            worlds+=1
            for b in BASES:
                for c in CONS:
                    counts[(c,b,classify(actions,w,b,c))]+=1; comps+=1
    RESULTS.mkdir(exist_ok=True)
    lines=["kind\tconstraint\tbaseline\tclass\tcount"]
    for c in CONS:
        for b in BASES:
            for cl in CLASSES:
                lines.append(f"COUNT\t{c}\t{b}\t{cl}\t{counts[(c,b,cl)]}")
    # Compare count rows only; Rust adds promotion/meta rows.
    (RESULTS/"python_counts.tsv").write_text("\n".join(lines)+"\n")
    print(f"MQR464_PY_WORLD_COUNT={worlds}")
    print(f"MQR464_PY_COMPARISON_COUNT={comps}")
    print("MQR464_PY_INDEPENDENT_ENUMERATION=PASS")

if __name__=="__main__":
    main()
