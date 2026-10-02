from __future__ import annotations
from dataclasses import dataclass, field, replace
from typing import Dict, FrozenSet, Tuple

@dataclass(frozen=True)
class Actor:
    actor_id: str
    lineage: FrozenSet[str]
    roles: FrozenSet[str]
    utility_version: str
    obligations: FrozenSet[str] = frozenset()

@dataclass(frozen=True)
class Mechanism:
    mechanism_id: str
    version: int
    domain: str
    parent: str | None = None

@dataclass(frozen=True)
class Ecology:
    actors: Dict[str, Actor]
    mechanism: Mechanism
    genealogy_events: Tuple[str, ...] = ()
    ontology: FrozenSet[str] = frozenset({"actor", "mechanism", "role", "utility"})
    receipt_version: int = 1

def born(ecology: Ecology, actor: Actor) -> Ecology:
    actors = dict(ecology.actors)
    actors[actor.actor_id] = actor
    return replace(
        ecology,
        actors=actors,
        genealogy_events=ecology.genealogy_events + (f"birth:{actor.actor_id}",),
    )

def retire(ecology: Ecology, actor_id: str) -> tuple[Ecology, FrozenSet[str]]:
    actor = ecology.actors[actor_id]
    actors = dict(ecology.actors)
    del actors[actor_id]
    return (
        replace(
            ecology,
            actors=actors,
            genealogy_events=ecology.genealogy_events + (f"death:{actor_id}",),
        ),
        actor.obligations,
    )

def merge(ecology: Ecology, left: str, right: str, merged_id: str) -> Ecology:
    a = ecology.actors[left]
    b = ecology.actors[right]
    merged = Actor(
        actor_id=merged_id,
        lineage=a.lineage | b.lineage | frozenset({left, right}),
        roles=a.roles | b.roles,
        utility_version=f"merge({a.utility_version},{b.utility_version})",
        obligations=a.obligations | b.obligations,
    )
    actors = dict(ecology.actors)
    del actors[left]
    del actors[right]
    actors[merged_id] = merged
    return replace(
        ecology,
        actors=actors,
        genealogy_events=ecology.genealogy_events + (f"merge:{left}+{right}->{merged_id}",),
    )

def fission(ecology: Ecology, source: str, children: tuple[str, str]) -> Ecology:
    a = ecology.actors[source]
    actors = dict(ecology.actors)
    del actors[source]
    for child in children:
        actors[child] = Actor(
            actor_id=child,
            lineage=a.lineage | frozenset({source}),
            roles=a.roles,
            utility_version=a.utility_version,
            obligations=a.obligations,
        )
    return replace(
        ecology,
        actors=actors,
        genealogy_events=ecology.genealogy_events + (f"fission:{source}->{children[0]}+{children[1]}",),
    )

def mutate_role(ecology: Ecology, actor_id: str, new_role: str) -> Ecology:
    actors = dict(ecology.actors)
    a = actors[actor_id]
    actors[actor_id] = replace(a, roles=frozenset({new_role}))
    return replace(
        ecology,
        actors=actors,
        genealogy_events=ecology.genealogy_events + (f"role:{actor_id}->{new_role}",),
    )

def mutate_utility(ecology: Ecology, actor_id: str, version: str) -> Ecology:
    actors = dict(ecology.actors)
    a = actors[actor_id]
    actors[actor_id] = replace(a, utility_version=version)
    return replace(
        ecology,
        actors=actors,
        genealogy_events=ecology.genealogy_events + (f"utility:{actor_id}->{version}",),
    )

def amend_mechanism(ecology: Ecology, new_id: str | None = None, domain: str | None = None) -> Ecology:
    old = ecology.mechanism
    new = Mechanism(
        mechanism_id=new_id or old.mechanism_id,
        version=old.version + 1,
        domain=domain or old.domain,
        parent=f"{old.mechanism_id}@{old.version}",
    )
    return replace(
        ecology,
        mechanism=new,
        genealogy_events=ecology.genealogy_events + (f"mechanism:{old.mechanism_id}@{old.version}->{new.mechanism_id}@{new.version}",),
    )

def expand_ontology(ecology: Ecology, primitive: str) -> Ecology:
    return replace(
        ecology,
        ontology=ecology.ontology | frozenset({primitive}),
        genealogy_events=ecology.genealogy_events + (f"ontology:+{primitive}",),
    )

def ancestry_classes(ecology: Ecology) -> set[FrozenSet[str]]:
    return {a.lineage for a in ecology.actors.values()}

@dataclass(frozen=True)
class ScaffoldProfile:
    name: str
    decomposition: str
    question_generation: str
    measurement_agenda: str
    modal_exploration: str
    coordination: str
    error_localization: str
    revision_leverage: str
    world_claim_authority: str
    scalar_score: None = None

DRAKE = ScaffoldProfile(
    name="Drake",
    decomposition="HIGH",
    question_generation="HIGH",
    measurement_agenda="HIGH",
    modal_exploration="MID",
    coordination="HIGH",
    error_localization="HIGH",
    revision_leverage="HIGH",
    world_claim_authority="HETEROGENEOUS",
)

SCHELLING = ScaffoldProfile(
    name="Schelling",
    decomposition="MID",
    question_generation="HIGH",
    measurement_agenda="MID",
    modal_exploration="HIGH",
    coordination="MID",
    error_localization="MID",
    revision_leverage="HIGH",
    world_claim_authority="SCOPED_HOLD",
)

HARDY_WEINBERG = ScaffoldProfile(
    name="Hardy-Weinberg",
    decomposition="HIGH",
    question_generation="HIGH",
    measurement_agenda="HIGH",
    modal_exploration="MID",
    coordination="HIGH",
    error_localization="HIGH",
    revision_leverage="HIGH",
    world_claim_authority="REGULATIVE_NOT_LITERAL",
)

NEWTON = ScaffoldProfile(
    name="Newton",
    decomposition="HIGH",
    question_generation="HIGH",
    measurement_agenda="HIGH",
    modal_exploration="HIGH",
    coordination="HIGH",
    error_localization="HIGH",
    revision_leverage="HIGH",
    world_claim_authority="STRONG_WITHIN_REGIME",
)

@dataclass(frozen=True)
class Constitution:
    name: str
    executable_distinctions: FrozenSet[str]
    world_contact_routes: FrozenSet[str]
    predecessor: str | None = None

def ravel_transition(previous: Constitution, candidate: Constitution) -> str:
    new_distinctions = candidate.executable_distinctions - previous.executable_distinctions
    new_routes = candidate.world_contact_routes - previous.world_contact_routes
    if not new_distinctions and not new_routes:
        return "COMPRESS_NO_PROMOTION"
    return "PROMOTION_CANDIDATE"

def base_ecology() -> Ecology:
    actors = {
        "lab": Actor("lab", frozenset({"lab-origin"}), frozenset({"producer"}), "u1", frozenset({"replicate"})),
        "reviewer": Actor("reviewer", frozenset({"review-origin"}), frozenset({"evaluator"}), "u1"),
    }
    return Ecology(actors=actors, mechanism=Mechanism("grant-rule", 1, "domain-A"))
