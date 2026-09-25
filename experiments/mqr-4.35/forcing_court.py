#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class World:
    case_id: str
    mu: str
    map_algebra: str
    intervention_alignment: str
    sensitivity_scope: str
    core_probes: tuple[int, ...]
    refinement_probes: tuple[int, ...]
    mediated: Callable[[int], object]
    direct: Callable[[int], object]
    coarse: Callable[[object], object] = lambda x: x


def linear(x: int) -> int:
    return 2 * (x + 1)


def linear_boundary_shift(x: int) -> int:
    return linear(x) if x < 4 else linear(x) + 1


def pair_mediated(x: int) -> tuple[int, int]:
    return (x % 2, x)


def pair_direct_same(x: int) -> tuple[int, int]:
    return pair_mediated(x)


def pair_direct_refined_shift(x: int) -> tuple[int, int]:
    # The coarse parity channel is preserved; the successor-only coordinate changes.
    return (x % 2, x + 2)


def partial_mediated(x: int) -> int:
    return x * x + 1


def partial_direct_same(x: int) -> int:
    return partial_mediated(x)


def partial_direct_boundary(x: int) -> int:
    # A simple domain boundary changes the direct law; there is no case-id lookup.
    return partial_mediated(x) if x <= 2 else partial_mediated(x) + x


WORLDS: tuple[World, ...] = (
    World(
        "F-R0-HOMO",
        "R0|IDENTITY|SAME_COMPONENT|EQUAL_QUOTIENT|STABLE|SAME_ENDPOINT",
        "HOMOMORPHIC",
        "COMMUTES_BY_CONSTRUCTION",
        "GLOBAL",
        (0, 1, 2),
        (4, 5),
        linear,
        linear,
    ),
    World(
        "F-R0-CONTEXT",
        "R0|IDENTITY|SAME_COMPONENT|EQUAL_QUOTIENT|STABLE|SAME_ENDPOINT",
        "CONTEXTUAL",
        "EMPIRICAL_ONLY",
        "BOUNDARY",
        (0, 1, 2),
        (4, 5),
        linear,
        linear_boundary_shift,
    ),
    World(
        "F-R2-EXACT",
        "R2|SURJECTIVE|SAME_COMPONENT|COARSE_QUOTIENT|SUCCESSOR|SAME_ENDPOINT",
        "QUOTIENT_HOMOMORPHIC",
        "COMMUTES_BY_CONSTRUCTION",
        "GLOBAL",
        (0, 1, 2, 3),
        (4, 5),
        pair_mediated,
        pair_direct_same,
        coarse=lambda y: y[0],
    ),
    World(
        "F-R2-REFINED",
        "R2|SURJECTIVE|SAME_COMPONENT|COARSE_QUOTIENT|SUCCESSOR|SAME_ENDPOINT",
        "QUOTIENT_HOMOMORPHIC",
        "EMPIRICAL_ONLY",
        "BOUNDARY",
        (0, 1, 2, 3),
        (4, 5),
        pair_mediated,
        pair_direct_refined_shift,
        coarse=lambda y: y[0],
    ),
    World(
        "F-R1-LOCAL",
        "R1|INCLUSION|SAME_COMPONENT|EQUAL_QUOTIENT|STABLE|SAME_ENDPOINT",
        "PARTIAL",
        "EMPIRICAL_ONLY",
        "LOCAL",
        (0, 1, 2, 3),
        (4, 5),
        partial_mediated,
        partial_direct_same,
    ),
    World(
        "F-R1-BOUNDARY",
        "R1|INCLUSION|SAME_COMPONENT|EQUAL_QUOTIENT|STABLE|SAME_ENDPOINT",
        "PARTIAL",
        "EMPIRICAL_ONLY",
        "BOUNDARY",
        (0, 1, 2, 3),
        (4, 5),
        partial_mediated,
        partial_direct_boundary,
    ),
)


def empirical_reach(w: World) -> str:
    core_equal = all(w.coarse(w.mediated(p)) == w.coarse(w.direct(p)) for p in w.core_probes)
    if not core_equal:
        return "E2_NONE"
    all_probes: Iterable[int] = w.core_probes + w.refinement_probes
    full_equal = all(w.mediated(p) == w.direct(p) for p in all_probes)
    if full_equal:
        return "E0_FULL"
    return "E1_QUOTIENT_ONLY"


def key(w: World, level: int) -> tuple[str, ...]:
    parts = [w.mu]
    if level >= 1:
        parts.append(w.map_algebra)
    if level >= 2:
        parts.append(w.intervention_alignment)
    if level >= 3:
        parts.append(w.sensitivity_scope)
    return tuple(parts)


def collisions(level: int) -> dict[tuple[str, ...], set[str]]:
    grouped: dict[tuple[str, ...], set[str]] = defaultdict(set)
    for w in WORLDS:
        grouped[key(w, level)].add(empirical_reach(w))
    return {k: v for k, v in grouped.items() if len(v) > 1}


def main() -> int:
    for w in WORLDS:
        print(
            "CASE=" + w.case_id,
            "MU=" + w.mu,
            "MAP_ALGEBRA=" + w.map_algebra,
            "ALIGNMENT=" + w.intervention_alignment,
            "SENSITIVITY=" + w.sensitivity_scope,
            "EMPIRICAL_REACH=" + empirical_reach(w),
            sep="\t",
        )

    counts = []
    for level in range(4):
        c = collisions(level)
        counts.append(len(c))
        print(f"NU{level}_COLLISIONS={len(c)}")
        for k, reaches in sorted(c.items()):
            print(f"NU{level}_COLLISION_KEY={'||'.join(k)}\tREACHES={','.join(sorted(reaches))}")

    expected = [3, 2, 1, 0]
    print("EXPECTED_COLLISION_VECTOR=" + ",".join(map(str, expected)))
    print("OBSERVED_COLLISION_VECTOR=" + ",".join(map(str, counts)))
    if counts != expected:
        print("FORCING_CONSTITUTION=HOLD")
        return 1

    print("FORCING_CONSTITUTION=PASS")
    print("MU_UNIVERSAL_SUFFICIENCY=FAIL")
    print("COARSEST_FORCING_SEPARATING_REFINEMENT=NU3")
    print("NU3_AUTHORITY=FORCING_ONLY_NOT_UNIVERSAL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
