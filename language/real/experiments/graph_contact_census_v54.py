"""Census of four-preparation practice-graph ambiguity and certified anchors.

Enumerates all 2**6 labeled simple undirected graphs on four vertices.
Counts are *combinatorial*, not estimates of how real scientific practices
are distributed. Uniformly weighting labeled graphs is not a physical prior.
"""
from collections import Counter
from itertools import combinations
from contact_stabilizer_v54 import EncounterProblem, PhysicalHandoff, undirected_practice


def census_four() -> dict:
    labels = ('a', 'b', 'c', 'd')
    allowed = tuple(combinations(labels, 2))
    orders = Counter()
    contacts_required = Counter()
    for mask in range(1 << len(allowed)):
        graph = undirected_practice(labels,
            tuple(e for i, e in enumerate(allowed) if mask & (1 << i)))
        candidate_count = len(EncounterProblem(graph, graph,
                                              structural_invariance_established=True).candidates())
        orders[candidate_count] += 1
        for k in range(len(labels)):
            possible = any(
                len(EncounterProblem(graph, graph, contacts=tuple(
                        PhysicalHandoff(x, x, True, True) for x in chosen),
                        structural_invariance_established=True).candidates()) == 1
                for chosen in combinations(labels, k)
            )
            if possible:
                contacts_required[k] += 1
                break
        else:
            raise AssertionError('All four anchors should be sufficient')
    if sum(orders.values()) != 64 or sum(contacts_required.values()) != 64:
        raise AssertionError('Enumeration count inconsistent')
    return {
        'graph_count':64,
        'automorphism_orders':dict(sorted(orders.items())),
        'minimum_certified_anchors':dict(sorted(contacts_required.items())),
        'mean_minimum_anchors_uniform_labeled_graphs':sum(k*v for k,v in contacts_required.items())/64,
        'interpretation':'Combinatorial census conditional on graph preservation, not real laboratory prevalence or a cross-language translator.'
    }


if __name__=='__main__':
    import json
    print(json.dumps(census_four(),indent=2))
