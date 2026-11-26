"""MQR 5.4: descriptive stratified mode association and exact selection countermodel.
No private observer/coordinate data emitted; no causal or occupancy estimate.
"""
import csv, hashlib, io, json, sys, zipfile
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

SHA = '5376aac7f12f981299bf0b4a964a4f6c453f501eb1b8ce29df1ce59f90b7b836'
SOURCE = 'acf9b46d-e71a-4ccb-91d2-a021ffda4dd4'
CELLS = ((1,1),(1,0),(0,1),(0,0))


def strata(groups):
    num = den = F(0)
    counts = Counter()
    for c in groups.values():
        a,b,c1,d = (c[k] for k in CELLS)
        n = a+b+c1+d
        num += F(a*d,n)
        den += F(b*c1,n)
        if not (a+b)*(c1+d)*(a+c1)*(b+d):
            counts['uninformative'] += 1
        else:
            counts['negative' if a*d < b*c1 else 'positive' if a*d > b*c1 else 'tie'] += 1
    return {'MH_OR_descriptive':str(num/den) if den else None,
            'MH_OR_float':float(num/den) if den else None,
            'strata':len(groups), **{k:counts[k] for k in ('negative','positive','tie','uninformative')}}


def audit(path):
    p = Path(path)
    if hashlib.sha256(p.read_bytes()).hexdigest() != SHA:
        raise ValueError('wrong historical ZIP')
    groups = defaultdict(list)
    with zipfile.ZipFile(p) as z:
        if z.namelist() != ['0031144-240626123714530.csv']:
            raise ValueError('wrong original member')
        with z.open(z.namelist()[0]) as raw:
            r = csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8-sig'),delimiter='\t')
            total = 0
            for row in r:
                total += 1
                if row['datasetKey'] != SOURCE: continue
                doc = row['catalogNumber']
                if not doc or row['occurrenceID'].split('#',1)[0] != doc:
                    raise ValueError('document ancestry mismatch')
                if row['occurrenceStatus'] not in ('PRESENT','ABSENT'):
                    raise ValueError('invalid status')
                groups[doc].append(row)
    assert (total,len(groups),sum(map(len,groups.values()))) == (29543,2272,14651)
    year,slots,both = (defaultdict(Counter) for _ in range(3))
    allcells = Counter()
    for rows in groups.values():
        years = {r['year'] for r in rows}
        if len(years) != 1: raise ValueError('mixed years')
        y = years.pop()
        f = int(any('/' not in r['eventDate'] and r['occurrenceStatus']=='PRESENT' for r in rows))
        w = int(any('/' in r['eventDate'] and r['occurrenceStatus']=='PRESENT' for r in rows))
        k = sum('/' in r['eventDate'] for r in rows)
        for c in (allcells,year[y],slots[k],both[(y,k)]): c[(f,w)] += 1
    a,b,c,d = (allcells[k] for k in CELLS)
    assert (a,b,c,d) == (695,1178,391,8)
    assert {y:v[(0,0)] for y,v in year.items() if v[(0,0)]} == {'2020':8}
    # Hypothetical population masses, not estimated real missing document counts.
    missing_cell = F(b*c,a)
    keep00 = F(d,1)/missing_cell
    assert F(a,1)*missing_cell == b*c
    assert missing_cell*keep00 == d
    assert 0 < keep00 <= 1
    # Exact observation equivalence: for arbitrary positive population q and
    # observed p, choose common k <= min(q_i/p_i), s_i = k*p_i/q_i.
    p = [F(v,a+b+c+d) for v in (a,b,c,d)]
    q = [F(1,4)]*4
    k = min(qi/pi for qi,pi in zip(q,p))
    s = [k*pi/qi for pi,qi in zip(p,q)]
    assert all(0 < x <= 1 for x in s)
    mass = [qi*si for qi,si in zip(q,s)]
    assert [x/sum(mass) for x in mass] == p
    # This demonstrates non-identification, not evidence selection occurred.
    return {'status':'PASS_PINNED_DESCRIPTIVE_AUDIT','documents':len(groups),
            'cell_order':['both','first_only','weekend_only','neither'],
            'cells':[a,b,c,d],'year_cells':{y:[v[k] for k in CELLS] for y,v in sorted(year.items())},
            'slot_cells':{str(y):[v[k] for k in CELLS] for y,v in sorted(slots.items())},
            'year':strata(year),'slots':strata(slots),'year_slots':strata(both),
            'observed_OR':float(F(a*d,b*c)),
            'independent_hypothetical_00_mass':str(missing_cell),
            'hypothetical_00_retention':str(keep00),
            'actual_selection_mechanism_identified':False,
            'causal_effect_identified':False,'new_field_data':False}


if __name__ == '__main__':
    print(json.dumps(audit(sys.argv[1]),sort_keys=True,indent=2))
