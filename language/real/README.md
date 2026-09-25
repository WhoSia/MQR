# Real-Language / Real-Packet v0.4 proof boundary + v0.3 transport compatibility

Real-Language is MQR's active event-to-realist-authority language.

It compiles a scientific, methodological, or engineering event into a scoped authority packet while preserving open-world residue and successor vulnerability.

## Version boundary

### v0.2
Historical profile grammar:

- C/E/P/R authority gates
- W/N/I/T/D profile
- scalar projection OFF by default

v0.2 remains readable for archival reproducibility.

### v0.3
Transport grammar retained for canonical/historical compatibility:

- C/E/P/R authority gates
- W/N/I/D profile
- **legacy axis T is forbidden**
- transport is represented by a typed relation map
- lineage kind is explicit

### v0.4 — live proof-boundary lane

v0.4 adds explicit formal/empirical ancestry without replacing world contact:

- typed FORMAL / DEFINITION / MODEL / EMPIRICAL premises;
- FORMAL_ONLY / WORLD_DEPENDENT obligations;
- explicit dependency ancestry;
- CHECKED / UNCHECKED / REFUTED / NOT_APPLICABLE proof states;
- empirical authority ceilings;
- finite probe-class / internal-residue receipts;
- mechanical rejection of axiom laundering.

Canonical proof receipt:

`language/real/V04-PROOF-RECEIPT.md`

Canonical v0.4 proof run:

`36146576232`

The target Lean theorems have empty axiom ancestry and were independently rechecked by a pinned nanoda stack.

The first world-contact-bound v0.4 packet is:

`language/real/examples/mqr-4.36-fresh-fiber-pcra.real`

It permits PASS for the narrowly receipt-backed internal-residue claim, keeps open-world adequacy at HOLD, and records fresh NU3 sufficiency as FAIL.

Therefore:

```text
KERNEL_VERIFIED != WORLD_VERIFIED
FORMAL_CERTAINTY_CANNOT_LAUNDER_EMPIRICAL_UNCERTAINTY
ZERO_INTERNAL_RESIDUE != ZERO_OPEN_WORLD_RESIDUE
```

MQR-4.31 found that one T coordinate conflated:
1. transport target/component,
2. evaluability,
3. survival conditional on evaluation.

Therefore:

```text
legacy.profile.T = DEPRECATED
transport.mode = TYPED_RELATION_MAP
```

## Lineage kinds

Every v0.3 packet must declare exactly one:

- `RESEARCH_LAB`
- `ENGINEERING_DEVELOPMENT`
- `METHODOLOGY_DEVELOPMENT`
- `OTHER`

This prevents development lineages from being silently reconstructed as scientific Labs.

Example:
ChatGPT-Web-HWPX-MCP is `ENGINEERING_DEVELOPMENT`.

The lineage kind changes interpretation/context, not the mechanical transport semantics.

## Authority gates

- C: constitutional/adjudication legitimacy
- E: admissible world-contact
- P: provenance/time/auditability
- R: open-world rival invariance

If any gate is not PASS:
authority = HOLD.

## Current profile

v0.3 retains:

- W: world resistance
- N: noncommon evidence-route strength
- I: inferential identification
- D: defeat exposure / corrigibility

Calibration status after MQR-4.30:

```text
W = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL
I = LEVEL-3 EXTERNALLY CALIBRATED ORDINAL
N = LEVEL-3 HOLD
D = external polarity PASS / Level-3 discriminant HOLD
```

The old scalar TPX remains retired.

```text
PROFILE_ORDER = PARETO_PARTIAL
SCALAR_PROJECTION_DEFAULT = OFF
FINAL_TRUTH_DISTANCE = UNIDENTIFIED
```

## Typed transport

v0.3 transport syntax:

```text
transport "<component>" "<source-regime>" "<target-regime>" <DIMENSION> <EVALUABILITY> <SURVIVAL> "<note>"
```

### Evaluability

Exactly one:

- `TESTED`
- `UNTESTED_AVAILABLE`
- `TARGET_UNAVAILABLE`
- `OUT_OF_SCOPE`

### Survival

When evaluability is `TESTED`:

- `SURVIVED`
- `FAILED`
- `MIXED_OR_NONATOMIC`

Otherwise:

- `NA`

### Derived transport authority

```text
TESTED + SURVIVED            -> TRANSPORT_PASS
TESTED + FAILED              -> TRANSPORT_FAIL
TESTED + MIXED_OR_NONATOMIC -> SPLIT_REQUIRED
UNTESTED_AVAILABLE           -> HOLD_UNTESTED
TARGET_UNAVAILABLE           -> HOLD_TARGET_UNAVAILABLE
OUT_OF_SCOPE                 -> OUT_OF_SCOPE
```

No averaging is permitted.

Claim-level transport is compiled to one of:

- `ALL_REQUIRED_CELLS_PASS`
- `SOME_REQUIRED_CELLS_FAIL`
- `PARTIAL_WITH_HOLDS`
- `SPLIT_REQUIRED`
- `NO_EVALUABLE_TARGET`

## MQR-4.31 validation

Fresh transport confirmation was sealed before native-label reveal.

Confirmatory corpus:
- RESEARCH_LAB: C3X and EPISTEME
- ENGINEERING_DEVELOPMENT: ChatGPT-Web-HWPX-MCP

Result:

```text
16 confirmatory cells
15/16 exact typed-state agreement = 0.9375
C1 untested-vs-failed = PASS
C2 componentwise transport = PASS
C3 cross-lineage concordance = PASS
C4 HWPX engineering/non-Lab typing = PASS
C5 success-collapse attack = PASS
```

The one mismatch was informative:
an operation-level `reject_all` promotion was incorrectly generalized to an uninstantiated component-specific `insert-reject` round-trip specimen.

Therefore:
**component-specific evaluability cannot be inherited from broader operation success.**

## Packet grammar

```text
REALPACKET 0.3
id "packet-id"
epoch "epoch"
claim CONSTRAINT "claim text"
scope "licensed scope"
lineage ENGINEERING_DEVELOPMENT

gate C PASS
gate E PASS
gate P PASS
gate R PASS

axis W 0.75 "why"
axis N 0.50 "why"
axis I 0.75 "why"
axis D 0.75 "why"

transport "component-a" "source" "target" VERSION TESTED SURVIVED "why"
transport "component-b" "source" "target" VERSION UNTESTED_AVAILABLE NA "why"

generator STRUCTURAL "description"
rival SURVIVING "description"
residue MODERATE "description"
mystery OPEN "description"
ontic HOLD "description"
successor VULNERABLE
source "source pointer"
END
```

## Canonical implementation policy

- Rust is the canonical compiler and the default for newly touched executable MQR surfaces.
- Python is retained as an independent reference/audit implementation where useful.
- Existing Python is not mechanically rewritten merely to change repository language statistics.
- Migration occurs when a surface becomes live again or when Rust/static implementation has a concrete reliability, portability, or performance advantage.

CI requires:
- v0.2 archival packet compatibility;
- v0.3 Rust/Python canonical-receipt concordance;
- rejection of v0.3 legacy `axis T`;
- Rust-first build success.

Implementation language is not an epistemic primitive.

## Proof-assistant division of labor

Real-Language is the typed boundary between world contact and proof systems.

Target architecture:

```text
WORLD CONTACT
 -> native evidence
 -> typed empirical receipt
 -> Real-Language premise authority
 -> formal obligation
 -> Lean proof
 -> independent formal recheck
 -> scoped consequence
```

Lean or another prover may certify derivability inside the formal region.
It does not certify the truth of empirical premises merely because they are formalized.

MQR-4.37 retires **PCRA as one monolithic scientific-authority construct** while preserving it as historical workflow architecture. The live decomposition is: **formal custody + world-facing authority + explicit transfer contract**. See `V05-AUTHORITY-TRANSFER.md`.

## Ceiling

Real-Language is allowed to represent earned authority, transport relations, premise ancestry and proof receipts.

It is not allowed to infer `TRANSFER=PASS` merely from formal-custody PASS.

It is not allowed to manufacture:
- a truth percentage,
- final ontology,
- universal cross-domain numeric units,
- transport authority for an untested component.


## v0.5 — executable world–statement transfer lane

MQR-4.38 makes the MQR-4.37 transfer boundary executable without turning it into a truth oracle.

Canonical implementation:
- Rust: `src/transfer_v05.rs` / binary `real-v05-transfer`;
- independent evaluator: `haskell/TransferV05.hs`;
- formal countermodels: `lean/MQR/Transfer.lean`.

The live transfer coordinates are:
- semantic correspondence;
- scope admissibility;
- authority-relevant ancestry preservation;
- defeat reachability;
- noncircular warrant;
- formal custody when applicable.

Each coordinate uses `PASS / HOLD / FAIL / NOT_APPLICABLE`. No numeric transfer score exists. HOLD is not collapsed into FAIL.

For a formally mediated route, `TRANSFER=PASS` means only:

```text
STRUCTURAL_ADMISSIBILITY_NONAMPLIFYING
```

The transfer contract cannot raise the source world-authority ceiling. A semantic-correspondence receipt remains a defeasible world-facing warrant rather than something the compiler can certify into existence.

A nonformal route is a first-class positive control:

```text
WORLD_AUTHORITY=PASS
FORMAL_CUSTODY=NOT_APPLICABLE
TRANSFER=NOT_APPLICABLE
```

Therefore formalization is optional and route-relative, not a universal condition for scientific authority.

Rust/Haskell concordance is implementation-diversity evidence only. It does not establish semantic or world independence.


## v0.6 — compositional transfer boundary

MQR-4.39 adds `REALCOMPOSE 0.6` and separates algebraic composition from scientific composition.

Canonical Rust: `src/compose_v06.rs` / `real-v06-compose`.
Independent Haskell: `haskell/ComposeV06.hs`.
Lean boundary: `lean/MQR/Composition.lean`.

The authority meet is associative and NoLaunder is transitive, but local transfer PASS does not imply composite PASS. The composition lane tracks endpoint compatibility, semantic composition, pathwise scope mapping, original-source ancestry, end-to-end defeat segments, assumption closure, global non-amplification and a direct source-to-target receipt.

A full PASS therefore means **conditional pathwise non-amplification**, not categorical closure of scientific authority. The live structural classification is **partial / witness-indexed composition**. See `V06-COMPOSITION.md`.
