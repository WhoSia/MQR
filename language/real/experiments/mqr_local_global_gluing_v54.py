"""MQR 5.4 / chat44: exact local-compatibility versus global-gluing toy models.

Synthetic finite probability systems, NOT quantum experimental data.
Known parity/contextuality construction; no novelty or physicality claim.
"""
from fractions import Fraction
from itertools import product

HALF = Fraction(1, 2)
ZERO = Fraction(0)

def anti_pair():
    return {(0, 1): HALF, (1, 0): HALF}

def equal_pair():
    return {(0, 0): HALF, (1, 1): HALF}

def marginal(pair, index):
    return {bit: sum((prob for bits, prob in pair.items() if bits[index] == bit), ZERO)
            for bit in (0, 1)}

def contexts_compatible(edge_models):
    """All shared one-variable marginals coincide."""
    names = set(name for pair in edge_models for name in pair)
    for name in names:
        observed = []
        for edge, table in edge_models.items():
            if name in edge:
                observed.append(marginal(table, edge.index(name)))
        if any(p != observed[0] for p in observed[1:]):
            return False
    return True

def deterministic_global_assignments(edge_models):
    """Return all global assignments in the intersection of local supports."""
    names = sorted(set(name for edge in edge_models for name in edge))
    feasible = []
    for bits in product((0, 1), repeat=len(names)):
        assignment = dict(zip(names, bits))
        if all(table.get(tuple(assignment[n] for n in edge), ZERO) > ZERO
               for edge, table in edge_models.items()):
            feasible.append(assignment)
    return feasible

def verify():
    triangle = {("A", "B"): anti_pair(),
                ("B", "C"): anti_pair(),
                ("A", "C"): anti_pair()}
    assert contexts_compatible(triangle)
    assert deterministic_global_assignments(triangle) == []
    # Odd xor cycle: A!=B, B!=C, A!=C impossible over {0,1}.
    tree = {("A", "B"): anti_pair(), ("B", "C"): anti_pair()}
    assert contexts_compatible(tree)
    assert len(deterministic_global_assignments(tree)) == 2
    # Equal parity cycle is globally consistent; a uniform mix of solutions
    # reproduces each edge's 50/50 anticorrelation.
    square = {("A", "B"): anti_pair(), ("B", "C"): anti_pair(),
              ("C", "D"): anti_pair(), ("A", "D"): anti_pair()}
    assert contexts_compatible(square)
    solutions = deterministic_global_assignments(square)
    assert len(solutions) == 2
    for edge, table in square.items():
        induced = {outcome: sum(
            (Fraction(1, len(solutions)) for s in solutions
             if tuple(s[n] for n in edge) == outcome), ZERO)
                   for outcome in product((0, 1), repeat=2)}
        assert all(induced[z] == table.get(z, ZERO) for z in induced)
    # An obvious marginal mismatch should be detected before asking about gluing.
    incompatible = {("A", "B"): anti_pair(),
                    ("A", "C"): {(0, 0): Fraction(1)}}
    assert not contexts_compatible(incompatible)
    assert all(sum(t.values(), ZERO) == 1 for t in triangle.values())
    return "PASS triangle obstruction; tree and square controls; overlap mismatch"

if __name__ == "__main__":
    print(verify())
