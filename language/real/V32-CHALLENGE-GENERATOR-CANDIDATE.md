# REALCHALLENGE 0.32-CANDIDATE — Challenge-Generator Independence Receipt

Status: **DEVELOPMENT-ONLY / UNPROMOTED / MQR-4.75**

REALCHALLENGE records whether challenge generators are locally independent enough to support authority updates.

It does not generate critics, optimize critic portfolios, or certify open-world challenge completeness.

## Header

```text
REALCHALLENGE 0.32-CANDIDATE
id <token>
sealed PASS
claim_scope_hash <token>
challenge_family_hash <token>
portfolio_id <token>
admissibility_rule_hash <token>
dependency_rule_hash <token>
evidence_kind <OBSERVED|PROVED|ENUMERATED|SIMULATED|INFERRED|OPEN>
completeness_claim RELATIVE_ONLY
open_world_complete OFF
...
END
```

## Generator rows

```text
generator <id> <family> <ancestry_hash> <target_model_dependency> <world_contact> <postoutcome_tuned> <novel> <claim_relevant> <bounded_search>
```

Boolean fields use YES / NO.

## Pair rows

```text
pair <g1> <g2> <shared_authority_ancestry> <shared_infrastructure> <route_diverse> <relation>
```

Relations:
- COMMON_MODE_HOLD
- INDEPENDENT_CHALLENGE
- ROUTE_DIVERSE_LOCAL
- AUTHORITY_UPGRADED
- BENIGN_SHARED_INFRASTRUCTURE
- NO_CLOSURE_FROM_SEARCH_FAILURE

## Mechanical boundaries

The compiler rejects:
- open-world completeness;
- novelty promoted as independence;
- algorithm/family diversity promoted despite shared authority ancestry;
- shared infrastructure treated as automatic common-mode dependence;
- post-outcome tuned generators promoted as prospective authority;
- bounded search failure promoted as counterexample absence;
- claim-irrelevant novelty promoted as challenge authority;
- relation rows referring to undeclared generators.

## Authority semantics

```text
NOVELTY != INDEPENDENCE
ALGORITHM_DIVERSITY != ASSUMPTION_DIVERSITY
SHARED_INFRASTRUCTURE != AUTOMATIC_DEPENDENCE
BOUNDED_SEARCH_FAILURE != ABSENCE_OF_COUNTEREXAMPLE
PORTFOLIO_DIVERSITY != GENERATOR_COMPLETENESS
POSTOUTCOME_TUNING != PROSPECTIVE_AUTHORITY
```

## Promotion boundary

`REALACQUIRE 0.29` remains latest promoted syntax.

All 0.30–0.32 lanes remain unpromoted.
