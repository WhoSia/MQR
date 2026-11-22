"""Same-specimen IDs are insufficient when sequential assays perturb latent targets.

Exact synthetic example; no real biomedical/quantum physical assertion.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

STATES = list(product((0, 1),repeat=2))
HALF=F(1,2)

def population(world):
    assert world in ('equal','opposite')
    return {(a,b):(HALF if b==(a if world=='equal' else 1-a) else F(0))
            for a,b in STATES}

def sequential(world, order):
    """First assay reads one bit then overwrites other with fair fresh noise."""
    assert order in ('AB','BA')
    answer=defaultdict(F)
    for (a,b),prob in population(world).items():
        for noise in (0,1):
            if order == 'AB':
                first,second=a,noise # A assay resets B before B assay
            else:
                first,second=b,noise # B assay resets A before A assay
            answer[(first,second)] += prob*HALF
    return dict(answer)

def simultaneous(world):
    """Ideal counterfactual read of both original bits without disturbing either."""
    return population(world)

def verify():
    for order in ('AB','BA'):
        p=sequential('equal',order)
        q=sequential('opposite',order)
        assert p==q=={pair:F(1,4) for pair in STATES}
    assert simultaneous('equal') != simultaneous('opposite')
    assert simultaneous('equal')[(0,0)] == HALF
    assert simultaneous('opposite')[(0,0)] == 0
    return 'PASS: perfect specimen IDs and sequential operations still cannot identify original association after disturbance'

if __name__ == '__main__':print(verify())
