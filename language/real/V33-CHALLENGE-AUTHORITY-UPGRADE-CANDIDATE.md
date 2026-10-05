# REALUPGRADE 0.33-CANDIDATE — Challenge-Authority Upgrade Receipt

Status: **DEVELOPMENT-ONLY / UNPROMOTED / MQR-4.76**

REALUPGRADE records a scoped authority change for a challenge whose source history remains explicit.

It does not:
- convert later authority into original independence;
- assign a scalar independence score;
- infer that external replication is automatically independent;
- equate natural-science and mathematical evidence types;
- certify permanent independence.

## Header

```text
REALUPGRADE 0.33-CANDIDATE
id <token>
sealed PASS
origin <INTERNAL|EXTERNAL|MIXED|UNKNOWN>
source_challenge_hash <token>
claim_scope_hash <token>
source_dependency_graph_hash <token>
witness_route <token>
witness_provenance_hash <token>
correspondence <EXACT|REFINE|MERGE|OVERLAP|DISJOINT>
postoutcome_tuned <YES|NO>
contact_kind <MEASUREMENT|RAW_DATA|ANALYSIS|SEMANTIC|PROOF|MODEL|NONE>
split_merge <NONE|SPLIT|MERGE>
residual_common_mode <YES|NO>
authority_state <NO_UPGRADE|DIAGNOSTIC_REPLICATION_ONLY|LOCAL_AUTHORITY_UPGRADE|CROSS_ROUTE_INDEPENDENCE_UPGRADE|SPLIT_REQUIRED|MERGE_COLLAPSE|REOPEN>
certificate_version <token>
reopen_on_ancestry_revision YES
dependency <name> <BREAK|PRESERVE|REPLACE|UNRESOLVED|NEW> <provenance>
...
END
```

## Dependency semantics

A dependency is claim-relative and authority-relevant.

- `BREAK` — the witness route removes a source dependency from the authority-changing failure route.
- `PRESERVE` — the dependency remains active.
- `REPLACE` — the source dependency is replaced by a distinct dependency whose provenance must be visible.
- `UNRESOLVED` — whether the dependency remains common-mode is not established.
- `NEW` — the witness route introduces a new authority-relevant dependency.

No count of BREAK rows is a scalar measure of independence.

## Mechanical admissibility

Any authority upgrade requires:
- non-DISJOINT challenge correspondence;
- at least one explicit BREAK;
- explicit provenance for every BREAK/REPLACE/NEW row;
- `postoutcome_tuned NO`;
- `reopen_on_ancestry_revision YES`.

`CROSS_ROUTE_INDEPENDENCE_UPGRADE` additionally requires:
- `residual_common_mode NO`;
- a non-NONE contact kind.

`SPLIT_REQUIRED` requires `split_merge SPLIT` or non-EXACT partial correspondence.

`MERGE_COLLAPSE` requires `split_merge MERGE`.

A diagnostic or NO_UPGRADE state may still carry useful evidence.

## Immutable history invariant

```text
LATER_AUTHORITY_UPGRADE != ORIGINAL_INDEPENDENCE
```

The packet outputs the declared `origin` unchanged. No upgrade state rewrites it.

## Hard boundaries

```text
EXTERNAL_LOCATION != EXTERNAL_AUTHORITY
REPLICATION_COUNT != INDEPENDENCE
SEMANTIC_RECONSTRUCTION != AUTOMATIC_UPGRADE
COMMON_MODE_EDGE_BROKEN != ALL_COMMON_MODES_BROKEN
MORE_BROKEN_EDGES != SCALAR_MORE_INDEPENDENT
WITNESS_COUNT != INDEPENDENT_WITNESS_COUNT
CERTIFICATE_PASS != PERMANENT_INDEPENDENCE
CROSS_DOMAIN_ROLE_EQUIVALENCE != EVIDENCE_TYPE_IDENTITY
```

## Promotion boundary

`REALACQUIRE 0.29` remains latest promoted syntax.

All 0.30–0.33 lanes remain unpromoted unless a later promotion court independently authorizes them.
