#!/usr/bin/env python3
import csv, itertools, pathlib
from collections import defaultdict, Counter

ROOT = pathlib.Path(__file__).resolve().parent

def read_tsv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def load():
    rows=read_tsv(ROOT/"RESPONSE-MATRIX-FREEZE.tsv")
    histories=[r["history"] for r in rows]
    tests=[k for k in rows[0] if k!="history"]
    response={(r["history"],t):int(r[t]) for r in rows for t in tests}
    return histories,tests,response

def rank_gf2(columns):
    if not columns: return 0
    M=[list(col) for col in columns]
    r=0
    n=len(M[0])
    for j in range(n):
        pivot=next((i for i in range(r,len(M)) if M[i][j]),None)
        if pivot is None: continue
        M[r],M[pivot]=M[pivot],M[r]
        for i in range(len(M)):
            if i!=r and M[i][j]:
                M[i]=[a^b for a,b in zip(M[i],M[r])]
        r+=1
    return r

def main():
    H,T,R=load()

    # Column signatures over the eight frozen histories.
    sig={t:tuple(R[(h,t)] for h in H) for t in T}
    signature_classes=defaultdict(list)
    for t,s in sig.items(): signature_classes[s].append(t)

    loops=[t for t in T if len(set(sig[t]))==1]
    parallels=[]
    for ts in signature_classes.values():
        if len(ts)>1 and not all(t in loops for t in ts):
            parallels.append(tuple(sorted(ts)))

    # The frozen table is linear over the three coordinate probes A,B,C.
    coords=["A","B","C"]
    coord_rows=[]
    for t in T:
        # Solve by direct lookup of coefficients from responses on basis histories:
        # H100, H010, H001 encode A,B,C.
        v=(R[("H100",t)],R[("H010",t)],R[("H001",t)])
        # verify linear representation across all histories
        ok=True
        for h in H:
            bits=tuple(int(x) for x in h[1:])
            pred=(v[0]*bits[0] + v[1]*bits[1] + v[2]*bits[2])%2
            if pred!=R[(h,t)]:
                ok=False; break
        coord_rows.append((t,v,ok))

    linear_tests=[t for t,v,ok in coord_rows if ok]
    vectors={t:v for t,v,ok in coord_rows if ok}

    bases=[]
    for comb in itertools.combinations(linear_tests,3):
        if rank_gf2([vectors[t] for t in comb])==3:
            bases.append(comb)

    # Pairwise separator hypergraph.
    pair_sep={}
    for a,b in itertools.combinations(H,2):
        pair_sep[(a,b)]=tuple(t for t in T if R[(a,t)]!=R[(b,t)])

    # Obligations needed for full separation are all history pairs.
    # A family is fully separating iff it intersects every pair separator.
    def hits_all(fam):
        s=set(fam)
        return all(s.intersection(seps) for seps in pair_sep.values())

    hit_bases=[b for b in bases if hits_all(b)]

    # Distinct bases after quotienting exact duplicate response columns.
    rep={}
    for s,ts in signature_classes.items():
        canonical=sorted(ts)[0]
        for t in ts: rep[t]=canonical
    quotient_bases=sorted(set(tuple(sorted(rep[t] for t in b)) for b in bases))

    out=ROOT/"results"; out.mkdir(exist_ok=True)
    with open(out/"hypergraph_summary.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["metric","value"])
        w.writerow(["TESTS",len(T)])
        w.writerow(["UNIQUE_RESPONSE_SIGNATURES",len(signature_classes)])
        w.writerow(["LOOPS",",".join(sorted(loops)) or "-"])
        w.writerow(["PARALLEL_CLASSES",";".join(",".join(x) for x in sorted(parallels)) or "-"])
        w.writerow(["LINEAR_REPRESENTATION_TESTS",sum(ok for _,_,ok in coord_rows)])
        w.writerow(["GF2_RANK",rank_gf2([vectors[t] for t in linear_tests])])
        w.writerow(["RANK3_BASE_COUNT",len(bases)])
        w.writerow(["FULL_SEPARATING_BASE_COUNT",len(hit_bases)])
        w.writerow(["DUPLICATE_QUOTIENT_BASE_COUNT",len(quotient_bases)])
        w.writerow(["PAIR_SEPARATOR_OBLIGATIONS",len(pair_sep)])

    with open(out/"basis_census.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["rank","basis"])
        for i,b in enumerate(sorted(bases),1): w.writerow([i,",".join(b)])

    with open(out/"separator_hypergraph.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["history_a","history_b","separator_count","separators"])
        for (a,b),seps in sorted(pair_sep.items()):
            w.writerow([a,b,len(seps),",".join(seps)])

    with open(out/"linear_representation.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["test","coef_A","coef_B","coef_C","verified"])
        for t,v,ok in coord_rows: w.writerow([t,*v,str(ok).upper()])

    ok=(
        len(T)==8
        and rank_gf2([vectors[t] for t in linear_tests])==3
        and len(bases)==24
        and len(hit_bases)==24
        and "CONST" in loops
        and any(set(x)=={"A","R"} for x in parallels)
    )
    print("MQR470_HYPERGRAPH=" + ("PASS" if ok else "FAIL"))
    print("MQR470_GF2_RANK=" + str(rank_gf2([vectors[t] for t in linear_tests])))
    print("MQR470_RANK3_BASE_COUNT=" + str(len(bases)))
    print("MQR470_FULL_SEPARATING_BASE_COUNT=" + str(len(hit_bases)))
    print("MQR470_DUPLICATE_QUOTIENT_BASE_COUNT=" + str(len(quotient_bases)))
    print("MQR470_LOOP_TESTS=" + ",".join(sorted(loops)))
    print("MQR470_PARALLEL_CLASSES=" + ";".join(",".join(x) for x in sorted(parallels)))
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
