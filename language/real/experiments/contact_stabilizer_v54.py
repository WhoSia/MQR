"""Authenticated contact and structural symmetries in possible-science bootstrapping.

Finite, conditional model. The *experimenter* supplies each lab's entire
accessibility graph. Structural parity is separately assumed; a verified
physical handoff is separately asserted. Neither is inferred from matching
labels, numerical data, or the Boolean fields in this model.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from itertools import permutations
from math import log2


@dataclass(frozen=True)
class LocalPractice:
    preparations: tuple[str, ...]
    accessible_pairs: frozenset[tuple[str, str]]

    def __post_init__(self):
        n = len(self.preparations)
        if not 1 <= n <= 8 or len(set(self.preparations)) != n:
            raise ValueError("Expected 1..8 distinct preparation labels")
        domain = set(self.preparations)
        if any(len(pair) != 2 or pair[0] == pair[1]
               or pair[0] not in domain or pair[1] not in domain
               for pair in self.accessible_pairs):
            raise ValueError("Invalid local accessible pair")
        if any((v, u) in self.accessible_pairs for u, v in self.accessible_pairs):
            raise ValueError("Undirected graph must use one edge per pair")

    def adjacency(self) -> frozenset[frozenset[str]]:
        return frozenset(frozenset((a, b)) for a, b in self.accessible_pairs)


@dataclass(frozen=True)
class PhysicalHandoff:
    a_preparation: str
    b_preparation: str
    authenticated_identity: bool
    preparation_stability_checked: bool

    @property
    def usable(self) -> bool:
        return self.authenticated_identity and self.preparation_stability_checked


@dataclass(frozen=True)
class EncounterProblem:
    a: LocalPractice
    b: LocalPractice
    contacts: tuple[PhysicalHandoff, ...] = ()
    # Strong, explicit and defeasible hypothesis: experimental accessibility
    # has identical graph-theoretic meaning in both laboratories.
    structural_invariance_established: bool = False

    def __post_init__(self):
        if len(self.a.preparations) != len(self.b.preparations):
            raise ValueError("This finite model requires equal inventory sizes")
        for contact in self.contacts:
            if (contact.a_preparation not in self.a.preparations or
                    contact.b_preparation not in self.b.preparations):
                raise ValueError("Contact refers to an absent local preparation")

    def candidates(self) -> tuple[tuple[str, ...], ...]:
        """Return ALL permitted bijections, never inventing a forced match."""
        observed = tuple(c for c in self.contacts if c.usable)
        a = self.a.preparations
        b = self.b.preparations
        ea = self.a.adjacency()
        eb = self.b.adjacency()
        possibilities = []
        for perm in permutations(b):
            phi = dict(zip(a, perm))
            if any(phi[c.a_preparation] != c.b_preparation for c in observed):
                continue
            if self.structural_invariance_established:
                transported = frozenset(frozenset((phi[u], phi[v])) for u, v in self.a.accessible_pairs)
                if transported != eb:
                    continue
            possibilities.append(perm)
        return tuple(possibilities)

    def next_contact_value(self) -> tuple[dict[str, object], ...]:
        """Idealized query-design scores for one further *certified* handoff.

        Bayesian-sounding 'expected' posterior uses UNIFORM prior across the
        already surviving bijections. This is not a physical probability.
        Query cost, sample drift, false verification and non-bijective
        translations are outside the model.
        """
        cands = self.candidates()
        if not cands:
            return ()
        results = []
        n = len(cands)
        for i, a_name in enumerate(self.a.preparations):
            partition = Counter(p[i] for p in cands)
            sizes = tuple(sorted(partition.values(), reverse=True))
            if len(sizes) <= 1:
                continue
            expected_size = sum(k*k for k in sizes) / n
            expected_entropy = sum((k / n) * log2(k) for k in sizes)
            results.append({
                "a_preparation": a_name,
                "possible_b_targets": len(sizes),
                "worst_case_remaining": max(sizes),
                "expected_remaining_uniform": expected_size,
                "expected_information_bits_uniform": log2(n) - expected_entropy,
                "class_sizes": sizes,
            })
        return tuple(sorted(results, key=lambda r: (
            r["worst_case_remaining"], r["expected_remaining_uniform"],
            -r["expected_information_bits_uniform"], r["a_preparation"])))


def undirected_practice(labels: tuple[str, ...], edges: tuple[tuple[str, str], ...]) -> LocalPractice:
    return LocalPractice(labels, frozenset(edges))
