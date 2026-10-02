# MQR-4.64 — FINAL SEAL

Status: **FINAL-SEAL / EXACT-HEAD-VERIFICATION-REQUIRED**

## Frozen ancestry

- MQR-4.63 canonical parent: `1dc3fcd183631c48d9cabc03b573bfbb8eb1cb9f`
- PRESEAL: `517da250c97c84770be3fae543ba2b6b9a3c0407`
- BINDING-MANIFEST: `3365c6ce4b87c7a9e7281246b3aac1de73c6209a`
- LITERATURE boundary: `4eff4a51fd7cfa58fbf32494760bfe1c4ea4e703`
- finite enumeration freeze: `df14dda7b42d4746d7b6c3100d8d23c1463a3a2e`
- missing-literature audit initial: `535e74b539df4ea4259e4c46f0804de3671c97b4`
- first executable reveal: `3090717f84b5d7d26aaecceebd5f4871fa2e0ac2`
- first reveal run: `36965537337`
- plumbing-only guard repair: `4d28431985a551df3a5f97b35031e0b3086b0c7c`
- minimality audit: `8e69c4d71046fbc282179abc6a8d790889de5cb1`
- full qualification workflow: `c139fd32b1265e4c5f2497428442cdeae4a20575`
- first full 5-job qualification run: `36965974819`

No action catalog, world grammar, baseline score, typed constraint, release condition, classification criterion or scientific threshold changed after first executable reveal.

The only first-reveal failure was a literal workflow grep mismatch against already-frozen text. That repair changed no scientific semantics.

## Executable surface

Frozen finite study:
- 16 action types
- 816 unordered triples with replacement
- 32 world-flag configurations
- 26,112 worlds
- 4 baselines
- 5 typed constraints
- 522,240 classifications

Canonical Rust and independent Python complete count matrix: concordant.
Deterministic exact replay: PASS.
Minimality / baseline-absorption audit: PASS.

## Sealed scientific result

~~~text
DIAGNOSTIC VARIATION
!= ACTIVATION

ACTIVATION
!= BINDING

BINDING
!= NONREDUNDANCY

NONREDUNDANCY
!= MQR-SPECIFIC CONTROL SEMANTICS
~~~

Binding is indexed to:
`world × baseline × constraint × horizon × scientific contract`.

### OPR
Against the matched minimum-separator CONSTRAINED baseline:
- DIAGNOSTIC_ONLY: 18,192
- BASELINE_ABSORBED: 7,920
- BINDING_LOCAL: 0

Therefore minimum-separator OPR is completely absorbed by the matched ordinary constrained baseline in the frozen grammar.

### NEDL
Against CONSTRAINED:
- DIAGNOSTIC_ONLY: 16,736
- REDUNDANT: 600
- BASELINE_ABSORBED: 6,800
- BINDING_LOCAL: 1,976
- OVERCONSTRAINING: 0

Strong local witness:
- irreversible action
- non-substitutable future separators
- baseline preserves one separator
- typed constraint preserves both

Substitutability releases the stronger constraint.

This establishes local nonabsorption from a **minimum-one-separator** baseline, not semantic irreducibility from constrained sequential planning generally.

### ARR / EAI / EXTERIOR
All have local binding regions.
ARR/EAI/EXTERIOR also expose explicit overconstraint regions under the matched constrained baseline.

These constraints remain expressible as ordinary state/action feasibility predicates in the finite grammar.

## Promotion boundary

A typed diagnostic earns local action-authority candidacy only when:
1. it activates;
2. it changes the feasible action set;
3. that change alters a materially declared future scientific reachability set;
4. the strong matched baseline does not already impose equivalent reachability;
5. activation uses contemporaneously available information;
6. own-ablation changes behavior/reachability;
7. the authority releases under reversibility, substitutability, or disappearance of the live scientific need.

## Semantic-version decision

**NO REALACQUIRE v0.30 PROMOTION.**

MQR-4.64 earns:
- binding-condition taxonomy;
- baseline-absorption discipline;
- release discipline;
- minimal binding witnesses;
- overconstraint visibility;
- a local NEDL nonabsorption witness.

It does not earn:
- BINDING_STRUCTURAL across heterogeneous natural scientific families;
- semantic irreducibility beyond constrained Bayesian design / CMDP / sequential planning;
- a new MQR acquisition controller formalism;
- a universal scientific feasible set;
- a scalar acquisition objective.

REALACQUIRE 0.29 remains current.

## Literature custody sidecar

`experiments/mqr-4.64/MISSING-LITERATURE.md` is the current best-effort load-bearing paper debt after exact-title/author Drive re-search.

Items newly verified in Drive were removed from the missing list rather than preserved as stale debt.

## Exact-head closure gate

The commit containing this file is canonical only if that exact SHA has all of:

1. `MQR-4.64/Rust-Characterization` SUCCESS
2. `MQR-4.64/Independent-Concordance` SUCCESS
3. `MQR-4.64/Deterministic-Replay` SUCCESS
4. `MQR-4.64/Structural-Guards` SUCCESS
5. `MQR-4.64/Minimality-Audit` SUCCESS

No cumulative Real-Language qualification is required because MQR-4.64 promotes no new Real-Language surface.

Repository policy remains **MAIN_ONLY**.

No repository mutation is permitted after verified closure.
