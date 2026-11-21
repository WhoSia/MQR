"""Multi-criterion audit of author-published REFMAC5 summary table.
Exact Decimals, no raw diffraction/NMR re-refinement.
"""
from decimal import Decimal as D
from mqr44_r16_published_refmac5_table import CASES

def strict_pareto_improvement(a, b):
    """Does (Q, Rfree) after improve or tie both, strictly improve one?"""
    return a[0]<=b[0] and a[1]<=b[1] and (a[0]<b[0] or a[1]<b[1])

def pass_by_heuristic(threshold):
    return {c.pdb: c.q_after < threshold for c in CASES}

def tests():
    assert len(CASES)==5
    for c in CASES:
        before=(c.q_before,c.rfree_before)
        after=(c.q_after,c.rfree_after)
        assert not strict_pareto_improvement(after,before)
        assert not strict_pareto_improvement(before,after)
        assert c.q_after<c.q_before
        assert c.rfree_after>c.rfree_before
    assert sum(pass_by_heuristic(D('.200')).values())==3
    assert sum(pass_by_heuristic(D('.202')).values())==4
    assert pass_by_heuristic(D('.200'))['1YR5'] is False
    assert pass_by_heuristic(D('.202'))['1YR5'] is True
    assert pass_by_heuristic(D('.200'))['1EXR'] is False
    return True

if __name__=='__main__':
    assert tests()
    print('PASS exact Pareto/tradeoff and heuristic sensitivity assertions')
    for c in CASES:
        print(c.pdb, 'Q_RDC',c.q_before,'->',c.q_after,
              'Rfree',c.rfree_before,'->',c.rfree_after)
