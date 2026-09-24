# MQR-4.32 — Prospective Transport Composition Receipt

Status: ONE EXTERNAL SCOPED COMPOSITION PASS / FULL EXTERNAL PROMOTION HOLD

## Stage

MQR-4.32 — Prospective Transport Composition, Three-Regime Bridge Receipts, Component-Identity Drift, Nontransitivity Witnesses, Path-Dependent Edge Algebra & Whether Typed Transport Can Compose without Smuggling Equivalence

## Inherited constitution

MQR-4.31 replaced legacy scalar T with typed transport relations and froze:

A -> B TRANSPORT_PASS
AND
B -> C TRANSPORT_PASS

does not imply:

A -> C TRANSPORT_PASS.

MQR-4.32 tests when a composed claim can be earned.

## Primary preseal

Commit:
a935fb38e50952cb6bf2ff7918ef52342ce5fb89

Frozen distinction:
adjacent PASS edges produce at most COMPOSITION_CANDIDATE.

COMPOSITION_PASS requires an independently admitted direct A -> C surface after the mediated prediction is sealed.

## Direct-surface independence amendment

Commit:
03a2950cffce8a5d5cca94a4c75835ef8996fde2

A direct surface may not merely reuse or logically inherit the same endpoint evidence that established an adjacent edge.

Admissible direct surfaces are explicitly typed.

## Rust canonical algebra

Package:
experiments/mqr-4.32/rust/

Core implementation:
2df426bcc4a6b26eb1202a497e49c11387c338fb

Direct-surface admission:
eadeb00cbbf861fb8904e8eb55ccd3ae2de60ce0

Canonical workflow:
.github/workflows/mqr-4.32-transport-composition.yml

Quality gates:
- rustfmt;
- Clippy with warnings denied;
- unit tests;
- release build;
- deterministic synthetic edge-algebra regression;
- canonical external triangle adjudication.

Canonical external CI:
36036019743

Evidence head:
22d83845b41cd14deec2434ef572f61b21e895de

Result:
- formatting PASS;
- Clippy PASS;
- unit tests PASS;
- release build PASS;
- synthetic algebra PASS;
- external triangle adjudication PASS.

## Frozen external candidate manifest

Commit:
3dbbbd9c2b3b779f87d49fb8d7e84b10d088d8e6

### Confirmatory

TKN-001 — Hugging Face tokenizers version composition
Lineage:
ENGINEERING_DEVELOPMENT.

### Diagnostic only

EPI-P35 — RESEARCH_LAB.
Reason:
adjacent and proposed direct comparison reuse the same endpoint; direct surface is not independent under the 4.32 constitution.

HWPX-P316 — ENGINEERING_DEVELOPMENT.
Reason:
three repetition records exist, but pairwise comparison of the same repetition set does not provide a held-out/noncommon direct surface.

ChatGPT-Web-HWPX-MCP remains ENGINEERING_DEVELOPMENT, not a research Lab.

### Excluded

C3X-P19 — RESEARCH_LAB.
Reason:
outcome-bearing commit-message information was exposed during candidate discovery before an admissible mediated seal.

This exclusion remains even if the case would have helped promotion.

## Pre-reveal promotion ceiling

Before TKN-001 result reveal, the candidate manifest froze:

- admissible ENGINEERING_DEVELOPMENT confirmatory triangle: present;
- admissible RESEARCH_LAB confirmatory triangle: absent;
- confirmatory triangle count below six.

Therefore full MQR-4.32 external promotion could not PASS under the frozen minimum requirements.

No post-reveal sampling was used to repair this ceiling.

## TKN-001 constitution

Regimes:
- A = tokenizers 0.21.4
- B = tokenizers 0.22.2
- C = tokenizers 0.23.2

Observable component:
ordered token-ID sequence plus ordered token-string sequence under a fixed WordLevel vocabulary, [UNK] token, Whitespace pre-tokenizer and declared fixture.

Bridge fixtures:
B01..B06.

Direct held-out fixtures:
H01..H06.

Bridge and direct fixture sets are disjoint.

Claim ceiling:
only the declared encoding-output quotient.

No whole-library, API, implementation, serialization, performance or ontological equivalence is claimed.

## Pre-direct engineering repair lineage

The initial external probe required cross-version wrapper and formatting repairs before any bridge fixture successfully executed.

Evidence-custody amendment:
273ed316ad3ab077c18e1d012c3df7430df45ab8

The amendment froze that all pre-amendment bridge executions were noncanonical and that the next successful current-lineage bridge run would be the canonical adjacent-edge execution.

The scientific variables were unchanged:
- versions;
- vocabulary;
- bridge fixtures;
- held-out fixtures;
- observable;
- equality criterion;
- mediated prediction rule.

## Canonical adjacent bridge

Run:
36035350447

Trigger SHA:
81800ebcd46e7f8a4ea6eb5482de8401909b9cdd

Persisted bridge receipt commit:
1fcc5477c251a6cbdcada348581e2d9d3fce1507

Receipt:
receipts/mqr-4.32/tokenizers-bridge.tsv

Observed:
- A -> B = TRANSPORT_PASS
- B -> C = TRANSPORT_PASS
- DIRECT_A_TO_C = NOT_EXECUTED

Bridge classes:
- A -> B = QUOTIENT_COMPATIBLE
- B -> C = QUOTIENT_COMPATIBLE

## Mediated seal before direct reveal

Commit:
b03c31531d8eca42f5b567d6ffbe94164fad5371

Frozen before direct execution:

COMPOSITION_CANDIDATE = YES

Predicted direct A -> C:
TRANSPORT_PASS

Expected path:
COMMUTES_AT_CLAIM_QUOTIENT

At seal time:
DIRECT_A_TO_C = NOT_EXECUTED.

## Canonical held-out direct execution

Workflow run:
36035751815

Trigger SHA:
56d8ba62471fbd1d62c541183ef91c90c2fa0462

Preflight verified the mediated seal before H01..H06 execution.

Both A and C version jobs:
PASS.

Direct adjudication:
PASS.

Prospective prediction:
TRANSPORT_PASS.

Observed direct A -> C:
TRANSPORT_PASS.

Path class:
COMMUTES_AT_CLAIM_QUOTIENT.

Composition state:
COMPOSITION_PASS.

## Direct evidence artifacts

Canonical adjudication artifact:
- artifact id 10825046164
- digest sha256:cad4723d76d527de033bc648ee26790d19bedb8e678bfd307d80512b8225de5b

A artifact:
- id 10825071154
- digest sha256:f6e54f1424f78e64943e2887424eeb7eeac086d98a9257e9847dc4c47acf3ff9

C artifact:
- id 10824681316
- digest sha256:82502cdb69de578e62b3179bd6bf73e450ea7718a3dadb9577671eb408c35ff0

## Custody push-race failure

The direct scientific adjudication succeeded, but workflow run 36035751815 is red at the workflow level.

Reason:
after adjudication, the workflow created local receipt commit 843d89c, but a concurrent documentation commit advanced main and the final push was rejected as non-fast-forward.

This is typed as:

CUSTODY_FAILURE_AFTER_SUCCESSFUL_ADJUDICATION

not:

SCIENTIFIC_TRANSPORT_FAILURE.

The exact machine-emitted adjudication fields were recovered unchanged and persisted at:

receipts/mqr-4.32/tokenizers-direct.tsv

Recovery commit:
8f48f9030126a88a397680788874da9455ea97b3

Custody repair narrative:
9bd6d723f41b5d133ce1acaf53c0de99ef78cd4c

No scientific field was changed during recovery.

A post-direct duplicate bridge run triggered by the custody-note path also failed only at receipt persistence after successful replay. It is noncanonical and does not replace canonical bridge run 36035350447.

World-contact workflows were subsequently frozen as manual read-only replay surfaces:
- bridge replay freeze: 3ef3af855d4d4683f03bd52293b5dd9f429ab5ba
- direct replay freeze: 18fbb438d5de1ae40a764021d5fa1a09980860ab

Canonical receipts are now mutation-disabled by those replay workflows.

## Canonical Rust external adjudication

External data:
experiments/mqr-4.32/external-triangles.tsv

Materialization:
a7b4962ecb304b8fd4a32d61c57788b1c30d1550

CI binding:
22d83845b41cd14deec2434ef572f61b21e895de

Machine result:

TRIANGLE=TKN-001
lineage=ENGINEERING_DEVELOPMENT
candidate=true
direct=Pass
path=CommutesAtClaimQuotient
direct_surface=HeldoutWorld
admitted=true
composition=COMPOSITION_PASS

TRIANGLES=1
COMPOSITION_CANDIDATES=1
COMPOSITION_PASS_COUNT=1
CONFIRMATORY_TRIANGLES=1
REJECTED_CONFIRMATORY_TRIANGLES=0
CROSS_LINEAGE_CONFIRMATORY=HOLD
MQR432_EXTERNAL_PROMOTION=HOLD
GLOBAL_TRANSITIVITY=REJECTED_AS_DEFAULT

## What TKN-001 earns

TKN-001 establishes one prospective external example in which:

1. A -> B and B -> C both survived at a declared component quotient;
2. a mediated A -> C prediction was sealed before direct execution;
3. a disjoint held-out direct A -> C surface was then executed;
4. the prospective direct prediction survived;
5. mediated and direct paths commuted at the declared claim quotient.

Therefore a typed transport system can earn:

SCOPED RECEIPT-CONDITIONED COMPOSITION

in at least one external engineering case.

## What it does not earn

MQR-4.32 does not establish:
- universal transport transitivity;
- regime equivalence;
- component identity outside the declared quotient;
- whole-library compatibility;
- path independence in general;
- a category or functor law;
- cross-lineage composition validity;
- a generic composition rule for research claims.

No external NONTRANSITIVITY_WITNESS was obtained in the admitted confirmatory corpus.

No external PATH_DIVERGENT_PASS was obtained in the admitted confirmatory corpus.

Those are missing pressures, not negative evidence that such cases do not exist.

## Full 4.32 adjudication

Presealed minimum external promotion requirements included:
- >= 6 confirmatory triangles;
- >= 2 lineage kinds;
- >= 1 RESEARCH_LAB triangle;
- >= 1 ENGINEERING_DEVELOPMENT triangle;
- >= 1 COMPOSITION_PASS;
- >= 1 canonical NONTRANSITIVITY_WITNESS;
- >= 1 path-congruence failure/refinement divergence.

Observed admitted confirmatory corpus:
- triangles = 1;
- lineage kinds = 1;
- engineering = present;
- research = absent;
- COMPOSITION_PASS = 1;
- NONTRANSITIVITY_WITNESS = 0;
- path divergence = 0.

Therefore:

MQR432_EXTERNAL_PROMOTION = HOLD.

This HOLD was fixed structurally before direct reveal and was not repaired after the favorable TKN-001 outcome.

## Research-engineering harvest

MQR-4.32 also raised repository engineering standards.

Live guidance:
docs/RESEARCH_ENGINEERING_STANDARD.md

Current direction:
- Rust canonical for newly touched authority-bearing executable surfaces when practical;
- Python reference/audit or exploratory analysis rather than default canonical adjudication;
- independent gate families for deterministic core, generated-contract drift, compatibility geometry, integration/conformance, security/supply-chain provenance and scientific world-contact;
- world-contact evidence and software quality remain non-substitutable.

Repository sophistication does not add scientific authority.

Scientific value does not excuse weak engineering custody.

## Philosophical result

MQR-4.32 rejects both extremes:

1. transport edges never compose;
2. transport PASS is automatically transitive.

The supported position is narrower:

Transport composition is a separately earned relation over a declared component quotient.

Adjacent survival establishes a candidate path.
Independent direct target contact adjudicates that candidate.

Thus:

A -> B PASS + B -> C PASS

can support a prospective A -> C prediction,

but only an independently admissible direct A -> C receipt can promote that prediction to COMPOSITION_PASS.

A single earned composition does not erase the default nontransitivity discipline.

## Verdict

RUST-TYPED-EDGE-ALGEBRA=PASS /
DIRECT-SURFACE-INDEPENDENCE=PASS /
NO-SMUGGLED-EQUIVALENCE=PASS /
TKN-001-ADJACENT-A-B=TRANSPORT_PASS /
TKN-001-ADJACENT-B-C=TRANSPORT_PASS /
TKN-001-MEDIATED-PREDICTION=PRESEALED /
TKN-001-DIRECT-A-C=TRANSPORT_PASS /
TKN-001-PATH=COMMUTES_AT_CLAIM_QUOTIENT /
TKN-001-COMPOSITION=COMPOSITION_PASS /
SCOPED-RECEIPT-CONDITIONED-COMPOSITION=EXTERNALLY-WITNESSED /
NONTRANSITIVITY-WITNESS=NOT-OBSERVED-IN-ADMITTED-EXTERNAL-CORPUS /
RESEARCH-LAB-CONFIRMATORY-TRIANGLE=ABSENT /
CROSS-LINEAGE-CONFIRMATION=HOLD /
MQR432-EXTERNAL-PROMOTION=HOLD /
GLOBAL-TRANSITIVITY=REJECTED-AS-DEFAULT /
CUSTODY-FAILURE-TYPING=INSTALLED /
WORLD-CONTACT-WORKFLOWS=FROZEN-READ-ONLY-REPLAY /
RUST-FIRST-RESEARCH-ENGINEERING-STANDARD=RAISED /
NO-REGIME-EQUIVALENCE /
NO-TRUTH-SCALAR-RESURRECTION /
GENERATION-IV-CONTINUES.
