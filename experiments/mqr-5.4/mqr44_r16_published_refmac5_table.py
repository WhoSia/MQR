"""Reproduce a published five-system joint X-ray/NMR refinement table.

Source: Rinaldelli et al., Acta Cryst D 70 (2014) 958-967, DOI
10.1107/S1399004713034160, Table 1. Values are author-published summaries;
this script does NOT re-refine diffraction factors or individual NMR restraints.
"""
from dataclasses import dataclass
from decimal import Decimal as D

@dataclass(frozen=True)
class Case:
    protein: str
    pdb: str
    q_before: D
    q_after: D
    rfree_before: D
    rfree_after: D

CASES = (
    Case('MMP-1 catalytic', '3SHI', D('.414'), D('.160'), D('.264'), D('.267')),
    Case('ubiquitin', '3NHE', D('.360'), D('.121'), D('.158'), D('.160')),
    Case('GB3', '1IGD', D('.146'), D('.081'), D('.132'), D('.134')),
    Case('calmodulin', '1EXR', D('.398'), D('.308'), D('.142'), D('.147')),
    Case('calmodulin-DAPk', '1YR5', D('.540'), D('.201'), D('.304'), D('.307')),
)

def result(c):
    return {'protein':c.protein, 'pdb':c.pdb, 'q_reduction':c.q_before-c.q_after,
            'relative_q_reduction':(c.q_before-c.q_after)/c.q_before,
            'delta_rfree':c.rfree_after-c.rfree_before,
            'q_below_0_2':c.q_after<D('.2')}

def test():
    assert len(CASES)==5
    assert all(c.q_after < c.q_before for c in CASES)
    assert all(c.rfree_after >= c.rfree_before for c in CASES)
    assert sum(result(c)['q_below_0_2'] for c in CASES)==3
    assert result(CASES[3])['q_below_0_2'] is False
    assert result(CASES[4])['q_below_0_2'] is False
    assert all(result(c)['delta_rfree']<=D('.005') for c in CASES)
    assert all(c.pdb in ('3SHI','3NHE','1IGD','1EXR','1YR5') for c in CASES)
    return True

if __name__=='__main__':
    assert test()
    for c in CASES:
        print(result(c))
    print('PASS 8 exact assertions from 2014 Table 1 author summaries')
