"""Pinned-original FinBIF reporting-panel audit; not biological occupancy.
No personal, coordinate or document identifiers are emitted.
"""
import csv, hashlib, io, json, sys, zipfile
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

SHA = '5376aac7f12f981299bf0b4a964a4f6c453f501eb1b8ce29df1ce59f90b7b836'
SPRING = 'acf9b46d-e71a-4ccb-91d2-a021ffda4dd4'


def bounds(positive, observed, cohort):
    if not 0 <= positive <= observed <= cohort or not cohort:
        raise ValueError('invalid counts')
    return Fraction(positive, cohort), Fraction(positive + cohort - observed, cohort)


def audit(path):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != SHA:
        raise ValueError('not pinned historical archive')
    docs = defaultdict(list)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        assert z.namelist() == ['0031144-240626123714530.csv']
        with z.open(z.namelist()[0]) as stream:
            rows = csv.DictReader(io.TextIOWrapper(stream, encoding='utf-8-sig'), delimiter='\t')
            n = 0
            for row in rows:
                n += 1
                if row['datasetKey'] == SPRING:
                    assert row['occurrenceID'].split('#', 1)[0] == row['catalogNumber']
                    assert row['occurrenceStatus'] in ('ABSENT', 'PRESENT')
                    docs[row['catalogNumber']].append(row)
    assert n == 29543 and len(docs) == 2272 and sum(map(len, docs.values())) == 14651
    years = defaultdict(list)
    for records in docs.values():
        assert len({r['year'] for r in records}) == 1
        years[records[0]['year']].append(records)
    totals = Counter(); annual = {}; table = []
    for year, records in sorted(years.items()):
        slots = sorted({r['eventDate'] for d in records for r in d if '/' in r['eventDate']})
        patterns = Counter(); blocks = Counter(); counts = [Counter() for _ in slots]
        for d in records:
            interval = [r for r in d if '/' in r['eventDate']]
            lookup = {r['eventDate']: r['occurrenceStatus'] for r in interval}
            if len(lookup) != len(interval):
                raise ValueError('duplicate document-slot record')
            mask = ''.join('1' if s in lookup else '0' for s in slots)
            patterns[mask] += 1
            totals['prefix'] += '01' not in mask
            observed = [lookup[s] for s in slots if s in lookup]
            p = ''.join('1' if y == 'PRESENT' else '0' for y in observed)
            k = sum(v == '1' and (i == 0 or p[i-1] == '0') for i,v in enumerate(p))
            blocks[k] += 1; totals[f'positive_blocks_{k}'] += 1
            for i,s in enumerate(slots):
                if s in lookup:
                    counts[i][lookup[s]] += 1
        annual[year] = {'documents': len(records), 'observed_slot_union': len(slots),
                        'availability_patterns': dict(sorted(patterns.items())),
                        'positive_block_counts': dict(sorted(blocks.items()))}
        if year == '2024':
            for s,c in zip(slots,counts):
                p, a = c['PRESENT'], c['ABSENT']; lo,hi = bounds(p,p+a,len(records))
                table.append({'slot':s,'present':p,'absent':a,'missing':len(records)-p-a,
                              'lower':str(lo),'upper':str(hi)})
    assert totals['prefix'] == 2272
    assert (totals['positive_blocks_0'], totals['positive_blocks_1'], totals['positive_blocks_2']) == (1186,1075,11)
    assert sum(x['present'] for x in table) == 70 and sum(x['absent'] for x in table) == 796
    for row in table:
        assert row['present'] + row['absent'] + row['missing'] == 131
    # Sharp completion bounds, no restrictions between missing binary cells.
    def diff(i,j):
        a,b = table[i],table[j]
        return [str(Fraction(b['lower'])-Fraction(a['upper'])),
                str(Fraction(b['upper'])-Fraction(a['lower']))]
    return {'source_sha256':SHA, 'rows':n, 'spring_rows':14651, 'documents':len(docs),
            'totals':dict(totals), 'annual':annual,'slots_2024':table,
            'may04_minus_apr20':diff(4,5), 'may18_minus_may04':diff(5,6),
            'jun01_minus_may18':diff(6,7), 'certified_physical_revisits':None,
            'estimand':'hypothetical binary completion of exported document slots, not ecological flowering or true occupancy'}


if __name__ == '__main__':
    assert bounds(2,128,131) == (Fraction(2,131),Fraction(5,131))
    try:
        bounds(3,2,4)
    except ValueError:
        pass
    else:
        raise AssertionError('invalid counts accepted')
    print(json.dumps(audit(sys.argv[1]), ensure_ascii=False, sort_keys=True, indent=2))
