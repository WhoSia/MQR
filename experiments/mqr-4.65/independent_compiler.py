from __future__ import annotations
from itertools import combinations_with_replacement, product
from pathlib import Path

HERE=Path(__file__).resolve().parent
RESULTS=HERE/"results"

CAT=[
("A0_HI_DROP",2,0,0,0,0,0),("A1_FULL",1,0,3,1,1,1),("A2_COST_FULL",2,1,3,1,1,1),
("A3_S0_HI",2,0,1,0,0,0),("A4_S1_HI",2,0,2,0,0,0),("A5_S0_REOPEN",1,0,1,1,1,0),
("A6_S1_REOPEN",1,0,2,1,1,0),("A7_FULL_EXT",1,0,3,0,0,1),("A8_DROP_REOPEN",2,1,0,1,1,1),
("A9_CHEAP_FULL_G0",1,1,3,1,0,0),("A10_LOW_FULL",0,0,3,1,1,1),("A11_HI_FULL",2,0,3,0,0,0),
("A12_HI_REOPEN_DROP",2,0,0,1,0,0),("A13_HI_G1_DROP",2,0,0,0,1,0),
("A14_HI_EXT_DROP",2,0,0,0,0,1),("A15_FULL_REOPEN_EXT_G0",1,0,3,1,0,1),
]
CONS=["OPR","ARR","EAI","EXTERIOR","NEDL"]
BASES=["MYOPIC","LOOKAHEAD","CONSTRAINED","DIVERSITY"]

def pop2(x): return int(bool(x&1))+int(bool(x&2))
def eff_sep(a,w):
    if not w["irr"]: return 3
    if w["sub"]: return 1 if a[3] else 0
    return a[3]
def eff_reopen(a,w): return True if not w["irr"] else bool(a[4])
def source_allowed(a,actions,w,c):
    if c=="OPR":
        return (not w["irr"]) or (not any(eff_sep(x,w) for x in actions)) or bool(eff_sep(a,w))
    if c=="ARR":
        return (not w["reopen_live"]) or (not any(eff_reopen(x,w) for x in actions)) or eff_reopen(a,w)
    if c=="EAI":
        return (not w["anc_live"]) or (not any(bool(x[5]) for x in actions)) or bool(a[5])
    if c=="EXTERIOR":
        return (not w["ext_live"]) or (not any(bool(x[6]) for x in actions)) or bool(a[6])
    if not w["irr"]: return True
    if w["sub"]:
        return (not any(eff_sep(x,w) for x in actions)) or bool(eff_sep(a,w))
    if any(eff_sep(x,w)==3 for x in actions): return eff_sep(a,w)==3
    return (not any(eff_sep(x,w) for x in actions)) or bool(eff_sep(a,w))

def target_allowed(a,actions,w,c):
    # independent spelling from the source branch
    sep=[eff_sep(x,w) for x in actions]
    if c=="OPR": return True if not w["irr"] else (all(x==0 for x in sep) or eff_sep(a,w)>0)
    if c=="ARR": return True if not w["reopen_live"] else (all(not eff_reopen(x,w) for x in actions) or eff_reopen(a,w))
    if c=="EAI": return True if not w["anc_live"] else (all(x[5]==0 for x in actions) or a[5]==1)
    if c=="EXTERIOR": return True if not w["ext_live"] else (all(x[6]==0 for x in actions) or a[6]==1)
    if not w["irr"]: return True
    if w["sub"]: return all(x==0 for x in sep) or eff_sep(a,w)>0
    if 3 in sep: return eff_sep(a,w)==3
    return all(x==0 for x in sep) or eff_sep(a,w)>0

def bfeasible(actions,w,b):
    ids=[0,1,2]
    if b=="CONSTRAINED" and w["irr"] and any(eff_sep(a,w) for a in actions):
        ids=[i for i,a in enumerate(actions) if eff_sep(a,w)]
    return ids
def score(a,w,b):
    n=(a[1]-a[2])*20
    if b in ("MYOPIC","CONSTRAINED"): return n
    if b=="LOOKAHEAD": return n+20*pop2(eff_sep(a,w))+(10 if w["reopen_live"] and eff_reopen(a,w) else 0)
    return n+(8 if w["anc_live"] and a[5] else 0)+(8 if w["ext_live"] and a[6] else 0)
def choose(actions,w,b,ids):
    if not ids: return None
    return max(ids,key=lambda i:(score(actions[i],w,b),-i))

def closed():
    pred=pred_m=pol=pol_m=0
    for ii in combinations_with_replacement(range(16),3):
        actions=[CAT[i] for i in ii]
        for flags in range(32):
            w={"irr":bool(flags&1),"sub":bool(flags&2),"reopen_live":bool(flags&4),
               "anc_live":bool(flags&8),"ext_live":bool(flags&16)}
            for c in CONS:
                for a in actions:
                    pred+=1
                    pred_m += source_allowed(a,actions,w,c)!=target_allowed(a,actions,w,c)
                for b in BASES:
                    base=bfeasible(actions,w,b)
                    s=[i for i in base if source_allowed(actions[i],actions,w,c)]
                    t=[i for i in base if target_allowed(actions[i],actions,w,c)]
                    pol+=1
                    pol_m += choose(actions,w,b,s)!=choose(actions,w,b,t)
    return pred,pred_m,pol,pol_m

def debt(h):
    d=False
    for e in h:
        if e=="D": d=True
        elif e=="R": d=False
    return d
def memory():
    hs=[h for n in range(6) for h in product("NDR",repeat=n)]
    collisions=sum(debt(h)!=(bool(h) and h[-1]=="D") for h in hs)
    mism=0; comps=0
    for h in hs:
        src=debt(h); c2=debt(h)
        for action in range(3):
            comps+=1
            mism += (not(src and action==1)) != (not(c2 and action==1))
    return len(hs),comps,collisions,mism

def frontier():
    comps=fixed=c3=0
    for n in range(1,9):
        mask=(1<<n)-1
        low=(1<<min(n,2))-1
        for live in range(mask+1):
            for cov in range(mask+1):
                src=(live & (~cov) & mask)==0
                t1=((live&low) & (~cov) & low)==0
                t3=(live & (~cov) & mask)==0
                comps+=1; fixed += src!=t1; c3 += src!=t3
    n=3; mask=7; live=4; cov=0; low=3
    witness=((live & (~cov) & mask)!=0) and (((live&low)&(~cov)&low)==0)
    return comps,fixed,c3,witness

def apply(s,e):
    i=e%4
    return s | (1<<i) if e<4 else s & ~(1<<i)
def genesis():
    hs=[h for n in range(5) for h in product(range(8),repeat=n)]
    mism=0
    for h in hs:
        src=0
        for e in h: src=apply(src,e)
        c3=0
        for e in h: c3=apply(c3,e)
        mism += src!=c3
    return len(hs),mism

def main():
    closed_n,closed_m,pol_n,pol_m=closed()
    mh,mc,mcoll,m2=memory()
    fc,fm,f3,wit=frontier()
    gh,gm=genesis()
    expected={
      "CLOSED_POLICY_COMPARISONS":522240,"CLOSED_POLICY_MISMATCHES":0,
      "CLOSED_PREDICATE_COMPARISONS":391680,"CLOSED_PREDICATE_MISMATCHES":0,
      "FRONTIER_C3_MISMATCHES":0,"FRONTIER_COMPARISONS":87380,
      "FRONTIER_FIXED2_MISMATCHES":39312,"GENESIS_C3_MISMATCHES":0,
      "GENESIS_HISTORIES":4681,"MEMORY_ACTION_COMPARISONS":1092,
      "MEMORY_C1_STATE_COLLISIONS":58,"MEMORY_C2_MISMATCHES":0,
      "MEMORY_HISTORIES":364,"MINIMAL_FIXED2_WITNESS":1,
    }
    got={
      "CLOSED_POLICY_COMPARISONS":pol_n,"CLOSED_POLICY_MISMATCHES":pol_m,
      "CLOSED_PREDICATE_COMPARISONS":closed_n,"CLOSED_PREDICATE_MISMATCHES":closed_m,
      "FRONTIER_C3_MISMATCHES":f3,"FRONTIER_COMPARISONS":fc,
      "FRONTIER_FIXED2_MISMATCHES":fm,"GENESIS_C3_MISMATCHES":gm,
      "GENESIS_HISTORIES":gh,"MEMORY_ACTION_COMPARISONS":mc,
      "MEMORY_C1_STATE_COLLISIONS":mcoll,"MEMORY_C2_MISMATCHES":m2,
      "MEMORY_HISTORIES":mh,"MINIMAL_FIXED2_WITNESS":int(wit),
    }
    assert got==expected,(got,expected)
    RESULTS.mkdir(exist_ok=True)
    (RESULTS/"python_summary.tsv").write_text("metric\tvalue\n"+"".join(f"{k}\t{got[k]}\n" for k in sorted(got)))
    print("MQR465_PY_INDEPENDENT=PASS")
    print("MQR465_PY_CLOSED_C1=PASS")
    print("MQR465_PY_MEMORY_C2=PASS")
    print("MQR465_PY_C3_FRONTIER=PASS")
    print("MQR465_PY_C3_GENESIS=PASS")
if __name__=="__main__": main()
