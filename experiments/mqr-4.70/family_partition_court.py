#!/usr/bin/env python3
import csv, itertools, math, pathlib
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent

def read_tsv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def load_matrix():
    rows = read_tsv(ROOT / "RESPONSE-MATRIX-FREEZE.tsv")
    tests = [k for k in rows[0] if k != "history"]
    histories = [r["history"] for r in rows]
    response = {(r["history"], t): r[t] for r in rows for t in tests}
    return histories, tests, response

def load_families():
    rows = read_tsv(ROOT / "PROBE-FAMILIES-FREEZE.tsv")
    out = {}
    for r in rows:
        out[r["family_id"]] = [] if r["members"] == "-" else r["members"].split(",")
    return out

def partition(histories, response, family):
    buckets = defaultdict(list)
    for h in histories:
        sig = tuple(response[(h,t)] for t in family)
        buckets[sig].append(h)
    classes = tuple(sorted(tuple(v) for v in buckets.values()))
    return classes

def refines(p_fine, p_coarse):
    coarse_of = {}
    for i,c in enumerate(p_coarse):
        for h in c:
            coarse_of[h] = i
    for c in p_fine:
        if len({coarse_of[h] for h in c}) > 1:
            return False
    return True

def entropy(xs):
    n=len(xs); c=Counter(xs)
    return -sum((v/n)*math.log2(v/n) for v in c.values())

def mutual_information(xs, ys):
    n=len(xs)
    hx,hy=entropy(xs),entropy(ys)
    pairs=list(zip(xs,ys))
    hxy=entropy(pairs)
    return hx+hy-hxy

def current_class_labels(histories, response, family):
    sigs={h:tuple(response[(h,t)] for t in family) for h in histories}
    uniq={s:i for i,s in enumerate(sorted(set(sigs.values())))}
    return [uniq[sigs[h]] for h in histories]

def choose_current_alignment(histories,response,base,candidates):
    labels=current_class_labels(histories,response,base)
    scored=[]
    for t in candidates:
        vals=[response[(h,t)] for h in histories]
        scored.append((mutual_information(vals,labels),t))
    best=max(x[0] for x in scored)
    return sorted(t for s,t in scored if abs(s-best)<1e-12)[0], scored

def within_class_split_score(histories,response,base,t):
    p=partition(histories,response,base)
    score=0
    for c in p:
        for a,b in itertools.combinations(c,2):
            if response[(a,t)] != response[(b,t)]:
                score += 1
    return score

def choose_within_class(histories,response,base,candidates):
    scored=[(within_class_split_score(histories,response,base,t),t) for t in candidates]
    best=max(x[0] for x in scored)
    return sorted(t for s,t in scored if s==best)[0], scored

def minimal_families_for_partition(histories,tests,response,target):
    winners=[]
    for k in range(len(tests)+1):
        for subset in itertools.combinations(tests,k):
            if partition(histories,response,subset)==target:
                winners.append(subset)
        if winners:
            return winners
    return []

def separators(histories, tests, response):
    sep={}
    for a,b in itertools.combinations(histories,2):
        sep[(a,b)] = tuple(t for t in tests if response[(a,t)] != response[(b,t)])
    return sep

def transport_preserves(histories,response,source_family,target_family):
    ps=partition(histories,response,source_family)
    pt=partition(histories,response,target_family)
    return refines(pt,ps)

def main():
    histories,tests,response=load_matrix()
    families=load_families()

    parts={fid:partition(histories,response,members) for fid,members in families.items()}

    # inclusion monotonicity over all frozen named families
    inclusion_checks=0
    inclusion_failures=0
    impossible_merges=0
    ids=sorted(families)
    for a in ids:
        for b in ids:
            if set(families[a]).issubset(set(families[b])):
                inclusion_checks += 1
                if not refines(parts[b],parts[a]):
                    inclusion_failures += 1
                    impossible_merges += 1

    same_partition_alts = [
        fid for fid in ["F_AB","F_AX","F_BX"]
        if parts[fid] == parts["F_AB"]
    ]

    target=parts["F_ABC"]
    mins=minimal_families_for_partition(histories,tests,response,target)

    sep=separators(histories,tests,response)
    collapsed_pairs=[
        (a,b) for a,b in itertools.combinations(histories,2)
        if all(response[(a,t)]==response[(b,t)] for t in families["F_AB"])
    ]
    exterior_c_separates=sum(response[(a,"C")]!=response[(b,"C")] for a,b in collapsed_pairs)

    s1,s1_scores=choose_current_alignment(histories,response,families["F_AB"],["C","R","CONST"])
    s2,s2_scores=choose_within_class(histories,response,families["F_AB"],["C","R","CONST"])

    good_transport=transport_preserves(histories,response,["A","B","C"],["A","B","C"])
    lossy_transport=transport_preserves(histories,response,["A","B","C"],["A","B","CONST"])

    out=ROOT/"results"; out.mkdir(exist_ok=True)
    with open(out/"court_summary.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["metric","value"])
        for k,v in [
            ("HISTORY_COUNT",len(histories)),
            ("TEST_COUNT",len(tests)),
            ("NAMED_FAMILY_COUNT",len(families)),
            ("INCLUSION_CHECKS",inclusion_checks),
            ("INCLUSION_FAILURES",inclusion_failures),
            ("IMPOSSIBLE_MERGES",impossible_merges),
            ("F_AB_CLASS_COUNT",len(parts["F_AB"])),
            ("F_ABC_CLASS_COUNT",len(parts["F_ABC"])),
            ("SAME_PARTITION_ALTERNATIVES",len(same_partition_alts)),
            ("MINIMAL_FAMILY_SIZE_FOR_F_ABC",len(mins[0]) if mins else -1),
            ("MINIMAL_FAMILY_COUNT_FOR_F_ABC",len(mins)),
            ("F_AB_COLLAPSED_PAIR_COUNT",len(collapsed_pairs)),
            ("EXTERIOR_C_SEPARATED_COLLAPSED_PAIRS",exterior_c_separates),
            ("CURRENT_ALIGNMENT_CHOICE",s1),
            ("WITHIN_CLASS_CHOICE",s2),
            ("GOOD_TRANSPORT_PRESERVES",str(good_transport).upper()),
            ("LOSSY_TRANSPORT_PRESERVES",str(lossy_transport).upper()),
        ]: w.writerow([k,v])

    with open(out/"partitions.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["family_id","members","class_count","partition"])
        for fid in sorted(families):
            w.writerow([fid,",".join(families[fid]) or "-",len(parts[fid]),";".join(",".join(c) for c in parts[fid])])

    with open(out/"minimal_families.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["rank","size","members"])
        for i,m in enumerate(mins,1):
            w.writerow([i,len(m),",".join(m)])

    with open(out/"selector_scores.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["criterion","test","score"])
        for score,t in sorted(s1_scores,key=lambda x:x[1]): w.writerow(["CURRENT_CLASS_INFORMATION",t,f"{score:.12f}"])
        for score,t in sorted(s2_scores,key=lambda x:x[1]): w.writerow(["WITHIN_CLASS_DISTINCTION",t,score])

    ok = (
        inclusion_failures==0
        and parts["F_AB"]==parts["F_AX"]==parts["F_BX"]
        and len(parts["F_ABC"])>len(parts["F_AB"])
        and len(mins)>=3
        and exterior_c_separates>0
        and s1=="R"
        and s2=="C"
        and good_transport
        and not lossy_transport
    )
    print("MQR470_COURT=" + ("PASS" if ok else "FAIL"))
    print(f"MQR470_CLASSES_F_AB={len(parts['F_AB'])}")
    print(f"MQR470_CLASSES_F_ABC={len(parts['F_ABC'])}")
    print(f"MQR470_MINIMAL_FAMILY_COUNT={len(mins)}")
    print(f"MQR470_CURRENT_ALIGNMENT_CHOICE={s1}")
    print(f"MQR470_WITHIN_CLASS_CHOICE={s2}")
    print(f"MQR470_GOOD_TRANSPORT={'PASS' if good_transport else 'FAIL'}")
    print(f"MQR470_LOSSY_TRANSPORT={'PRESERVE' if lossy_transport else 'BREAK'}")
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
