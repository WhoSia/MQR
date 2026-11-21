import unittest
from collections import Counter
from itertools import permutations, combinations
from graph_contact_census_v54 import census_four


class CensusTests(unittest.TestCase):
    def test_distributions_and_mean(self):
        r = census_four()
        self.assertEqual(r['graph_count'],64)
        self.assertEqual(r['automorphism_orders'],{2:36,4:12,6:8,8:6,24:2})
        self.assertEqual(r['minimum_certified_anchors'],{1:36,2:26,3:2})
        self.assertEqual(r['mean_minimum_anchors_uniform_labeled_graphs'],1.46875)

    def test_independent_edge_set_automorphism_oracle(self):
        edges = tuple(combinations(range(4),2))
        hist=Counter()
        for mask in range(64):
            relation=frozenset(e for i,e in enumerate(edges) if mask&(1<<i))
            count=0
            for p in permutations(range(4)):
                image=frozenset(tuple(sorted((p[i],p[j]))) for i,j in relation)
                count += image==relation
            hist[count]+=1
        self.assertEqual(dict(sorted(hist.items())),census_four()['automorphism_orders'])

    def test_independent_anchor_oracle(self):
        edges=tuple(combinations(range(4),2))
        hist=Counter()
        for mask in range(64):
            relation=frozenset(e for i,e in enumerate(edges) if mask&(1<<i))
            aut=[p for p in permutations(range(4)) if frozenset(
                tuple(sorted((p[i],p[j]))) for i,j in relation)==relation]
            minimal=next(k for k in range(4) if any(
                sum(all(p[i]==i for i in subset) for p in aut)==1
                for subset in combinations(range(4),k)))
            hist[minimal]+=1
        self.assertEqual(dict(sorted(hist.items())),census_four()['minimum_certified_anchors'])


if __name__=='__main__':
    unittest.main()
