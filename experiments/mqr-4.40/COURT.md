# MQR-4.40 — Direct-vs-Composed Authority Substitution Court

Status: CLOSED / B+C / WORLD-CONTACT-BASIS SUBSTITUTION / INTERNAL COHERENCE NOT WORLD CONTACT / MAIN-ONLY

## Canonical question

Can compositional transfer ever replace fresh direct adjudication without creating a closed epistemic loop?

Answer:

```text
YES, for transport-only or basis-generated claims under an externally rooted WCSC.
NO, if substitution is asked to create, refresh, or replace world contact itself.
```

MQR-4.40 therefore rejects both extremes:

```text
FRESH DIRECT ENDPOINT CONTACT IS NOT UNIVERSALLY REQUIRED.
INTERNAL COHERENCE IS NEVER A SUBSTITUTE FOR EXTERNAL WORLD CONTACT.
```

## The decisive shift

MQR-4.39 attached a direct source-to-target receipt to every full composite PASS.

MQR-4.40 replaces that universal endpoint obligation with a conditional **World-Contact Substitution Certificate (WCSC)**.

The relevant burden is not the number of transformation endpoints.

It is the declared set of load-bearing empirical degrees that the endpoint claim depends on or newly introduces.

## World-Contact Basis

A **World-Contact Basis (WCB)** is a declared family of externally rooted measurement/intervention receipts covering the load-bearing empirical degrees required by an endpoint claim family.

The v0.7 checker can solve the finite set-cover problem induced by the declared degree/root relation.

Positive basis fixture:

```text
declared degrees = {D_TEMP, D_PRESSURE}
one live external root LAB covers both
minimum declared root cover = 1
direct endpoint receipt = ABSENT
substitution = PASS
```

This does **not** identify an ontically minimal experiment set.

It is only minimal relative to the declared empirical-degree and coverage graph.

The completeness, independence and correct granularity of those degrees remain world-facing burdens.

## External Root Cut

Every load-bearing justification node reachable from the endpoint must have a path to an EXTERNAL world-contact root.

This is the **External Root Cut (ERC)**.

An internally closed cycle can be perfectly coherent and still fail ERC.

Therefore:

```text
COHERENCE CLOSURE != WORLD-CONTACT CLOSURE
```

## Frozen attack adjudication

### 1. Direct-receipt fetishism

REJECTED.

The transport-only positive control has:
- live external root;
- definitional/formally exact transport;
- no new empirical degree;
- generated endpoint query;
- ancestry/defeat continuity;
- no direct endpoint receipt.

It receives substitution PASS in both Rust and Haskell.

Fresh endpoint measurement is therefore not a universal prerequisite.

### 2. Closed coherence loop

BLOCKED.

An unanchored internal justification loop fails external-root/exteriority requirements.

Lean independently shows that internal path agreement and commutation do not entail an external root.

### 3. Common-mode path independence

BLOCKED.

Multiple agreeing paths sharing a HOLD root remain bounded by that root.

```text
PATH AGREEMENT != INDEPENDENT WORLD CONTACT
```

### 4. Query-basis leakage

BLOCKED.

The endpoint query must be reachable from an externally rooted query basis through every declared generation map.

Lean supplies a countermodel in which two paths agree on the checked Boolean basis point and disagree outside it.

### 5. Non-congruent path equivalence

BLOCKED.

When multiple paths are invoked, equivalence must survive declared PRE and POST extension.

Endpoint-only agreement is insufficient.

The original proposition-level countermodel was deliberately localized to a Boolean witness after it exposed a `propext` dependency; the canonical theorem is axiom-empty.

### 6. Higher coherence

BOUNDED.

`CLOSED` may earn PASS only for the declared diagram/query class.

`FINITE_ONLY` and `OPEN` remain HOLD for a stronger substitution claim.

Checked faces do not establish universal higher coherence.

### 7. Stale anchor / freshness reset

BLOCKED.

Roots are LIVE / STALE / EXPIRED.

Derived receipts cannot improve root freshness.

Lean theorem:

```text
MQR.compositionCannotRefreshRootFreshness
```

### 8. Recursive substitution inflation

BLOCKED BY CONSTITUTION.

A substituted endpoint may be reused only while retaining original external-root identity, ancestry and freshness.

A derived/internal receipt cannot replace its stale external root and claim renewed freshness.

### 9. Unanchored SCC

BLOCKED.

Cycles in justification are not forbidden as such.

But every load-bearing node in the reachable justification region must reach an external root.

Lean countermodel shows a closed two-node cycle does not entail exteriority.

### 10. Direct-vs-composed conflict

REOPENING SURVIVES.

A later direct PASS is compatible with the composition.

A later direct HOLD or FAIL changes the substitution coordinate to HOLD and triggers re-adjudication.

MQR does not infer:

```text
DIRECT EVIDENCE = INFALLIBLE ORACLE
```

Direct evidence is a privileged new defeat route because it adds endpoint world contact, not because its conclusion is definitionally superior.

## Claim-type split

### TRANSPORT_ONLY

Substitution may PASS without fresh direct endpoint contact when:
- the endpoint introduces no new empirical degree;
- the source basis is live and external;
- query generation is explicit;
- semantic/naturality obligations are satisfied;
- ancestry, assumptions, defeatability and global non-amplification survive.

### BASIS_GENERATED

Substitution may PASS without fresh direct endpoint contact when every declared load-bearing empirical degree is covered by a live WCB and the endpoint query is generated within the certified class.

### NEW_EMPIRICAL

Substitution FAILS.

A genuinely new load-bearing empirical degree cannot be manufactured by transformation, path agreement or formal exactness.

It requires new world-facing support.

## Real-Language v0.7

Canonical Rust:

`language/real/src/substitute_v07.rs` / `real-v07-substitute`

Independent Haskell:

`language/real/haskell/SubstituteV07.hs`

Formal boundary:

`language/real/lean/MQR/Substitution.lean`

Constitution:

`language/real/V07-SUBSTITUTION.md`

Live coordinates:

```text
EXTERNAL_ROOT
WORLD_CONTACT_BASIS
QUERY_BASIS
NATURALITY
PATH_INDEPENDENCE
CONGRUENCE
HIGHER_COHERENCE
ANCESTRY
ASSUMPTION
NO_NEW_EMPIRICAL_DEGREE
DEFEAT_TO_WORLD
EXTERIORITY
BRIDGE_STATE
GLOBAL_NONAMPLIFICATION
DIRECT_CONFLICT
SUBSTITUTION
```

No scalar exists.

A PASS means only:

```text
WORLD_CONTACT_BASIS_PRESERVING_NONAMPLIFYING SUBSTITUTION ADMISSIBILITY
```

## Formal receipts

Canonical axiom-empty Lean boundary:

```text
run 36179201342 = SUCCESS
MQR440_SUBSTITUTION_AXIOM_ANCESTRY=EMPTY
```

Pinned independent nanoda replay:

```text
run 36179288342 = SUCCESS
MQR440_NANODA_INDEPENDENT_CHECKER=PASS
MQR440_SUBSTITUTION_COUNTERMODELS_REPLAY=PASS
INTERNAL_COHERENCE_IS_NOT_WORLD_CONTACT=TRUE
```

All ten MQR-4.40 target theorems have empty axiom ancestry.

## Executable receipts

Canonical Rust/Haskell stage court:

```text
run 36178894475 = SUCCESS
MQR440_RUST_COURT=PASS
MQR440_HASKELL_COURT=PASS
MQR440_FRESH_DIRECT_UNIVERSALLY_REQUIRED=REJECT
MQR440_TRANSPORT_ONLY_SUBSTITUTION=PASS
MQR440_WORLD_CONTACT_BASIS_SUBSTITUTION=PASS
MQR440_INTERNAL_COHERENCE_CREATES_WORLD_CONTACT=REJECT
MQR440_EXTERNAL_ROOT_CUT=PASS
MQR440_DIRECT_CONFLICT_REOPENS=PASS
```

Canonical Real-Language v0.7 CI:

```text
run 36178894481 = SUCCESS
REAL_LANGUAGE_V07_SUBSTITUTION_GUARDS=PASS
REAL_LANGUAGE_V07_RUST_HASKELL_CONCORDANCE=PASS
MQR440_DIRECT_ALWAYS_REQUIRED=REJECT
MQR440_WORLD_CONTACT_BASIS_SUBSTITUTION=PASS
INTERNAL_COHERENCE_IS_NOT_WORLD_CONTACT=TRUE
```

A later full Real-Language replay after the axiom-free localization also succeeded:

```text
run 36179201332 = SUCCESS
```

## Failed precursor receipts

Failed runs are preserved.

Initial MQR-4.40 formalization compressed Lean structure declarations too aggressively, producing syntax errors.

The first Haskell independent evaluator also used an over-compressed layout that failed parsing, while Rust had already passed the stage court.

After repair, one proposition-level extension-congruence witness depended on `propext`. It was localized to the actual finite Boolean countermodel being claimed.

None of these failures were waived. The canonical proof has empty axiom ancestry and independent nanoda replay.

## Literature constraints

Existing Drive literature constrained the result.

Rubenstein et al.'s exact transformations provide a strong formal example in which an explicitly specified intervention-preserving transformation can compose transitively.

Rischel & Weichwald show why composition requires explicit observation/intervention relations and why model-to-world adequacy remains tied to physical measurement and intervention implementations.

Lorenz & Tull make query/semantic mappings part of the abstraction object through natural transformations.

MQR therefore accepts formal compositional substitution only when the scientific world-contact roots and query class are carried explicitly.

These sources do not themselves promote any MQR claim to world truth.

## Minimal end-to-end world-contact burden

The strongest surviving principle is:

```text
FRESH WORLD CONTACT IS NOT OWED PER ENDPOINT.

WORLD CONTACT IS OWED FOR EVERY LOAD-BEARING EMPIRICAL DEGREE
NOT ALREADY COVERED BY A LIVE, EXTERNALLY ROOTED BASIS
UNDER THE CERTIFIED QUERY / INTERVENTION CLASS.
```

Equivalently, direct adjudication is triggered by **empirical novelty or root invalidation**, not by representation change alone.

But the phrase "empirical degree" is itself not yet primitive or mechanically identified.

The WCB minimum is therefore conditional on the declared degree ontology.

## Outcome branches

```text
A. DIRECT-ALWAYS = REJECTED.

B. TRANSPORT-SUBSTITUTABLE = SUPPORTED.
   Exact/definitional transport with no new empirical burden need not receive fresh endpoint contact.

C. BASIS-SUBSTITUTABLE = SUPPORTED WITH DECLARED-BASIS SCOPE.
   A live WCB can support a family of generated endpoint claims without per-endpoint direct contact.

D. COHERENCE-SUFFICIENT = REJECTED.
   Naturality, path independence and higher coherence cannot create an external world root.

E. NO FINITE SUBSTITUTION LAW = REJECTED INSIDE AN EXPLICITLY CLOSED DECLARED CLASS.
   Universal open-world sufficiency is NOT established; undeclared empirical degrees and future drift remain open residue.

CANONICAL SYNTHESIS = B + C
```

## Strongest result

MQR-4.40 relocates the direct-contact requirement.

```text
OLD:
every composite endpoint -> fresh direct receipt

NEW:
every uncovered load-bearing empirical degree
or invalidated/stale world root
-> fresh world contact
```

Thus compositional transfer can replace **redundant endpoint adjudication**.

It cannot replace **the external world anchor that makes adjudication scientific**.

## Verdict

```text
DIRECT-ALWAYS=REJECT
TRANSPORT-ONLY-SUBSTITUTION=PASS
WORLD-CONTACT-BASIS-SUBSTITUTION=PASS
NEW-EMPIRICAL-WITHOUT-NEW-CONTACT=REJECT
INTERNAL-COHERENCE-AS-WORLD-CONTACT=REJECT
PATH-AGREEMENT-AS-INDEPENDENT-EVIDENCE=REJECT
QUERY-BASIS-LEAKAGE-GUARD=PASS
CONGRUENCE-UNDER-EXTENSION=PASS
FINITE-FACES-IMPLY-HIGHER-COHERENCE=REJECT
FRESHNESS-RESET-BY-DERIVATION=REJECT
UNANCHORED-CYCLIC-JUSTIFICATION=REJECT
DIRECT-CONFLICT-REOPENING=PASS
WCB-MINIMALITY=RELATIVE-TO-DECLARED-DEGREES
FINAL-TRUTH-DISTANCE=UNIDENTIFIED
OUTCOME=B+C
GENERATION-IV-CONTINUES
```
