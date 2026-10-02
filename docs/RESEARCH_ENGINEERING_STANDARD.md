# MQR Research-Engineering Standard

Status: LIVE GUIDANCE / NON-EPISTEMIC INFRASTRUCTURE

This document governs how MQR research code and evidence are packaged.
It does not add scientific authority by itself.

## Why this exists

A serious research repository should make it difficult to confuse:
- code that happened to run once;
- code that is regression-tested;
- evidence that is reproducible;
- evidence that is scientifically admissible;
- artifacts that are too large or too mutable to live in Git.

MQR therefore separates research constitution from engineering quality while requiring both.

## External engineering harvest

The following patterns are adopted as engineering lessons, not as philosophical authority.

### SWE-bench experiments
Useful pattern:
- small repository entries contain metadata and result summaries;
- large logs/trajectories can live in external artifact stores;
- validation logs remain public and inspectable;
- benchmark versions and reruns are explicit.

MQR adoption:
- Git stores preseals, manifests, hashes, small receipts and adjudicators;
- large raw artifacts may remain external when immutable location/hash custody exists;
- validation/replay receipts are first-class artifacts.

### Hugging Face tokenizers
Useful pattern:
- Rust is the reference implementation;
- language bindings are explicit adapters rather than competing canonical cores;
- runnable examples are part of the product contract;
- CI checks formatting/style and generated interface consistency.

MQR adoption:
- newly touched canonical executable surfaces prefer Rust;
- Python may remain an independent reference/audit lane;
- examples and negative fixtures are executable;
- adapter agreement is tested, not assumed.

### ai-memory
Useful pattern:
- typed crate boundaries;
- pinned/self-contained development expectations;
- fmt, clippy with warnings denied, full tests and dependency policy as merge gates;
- every behavior change should carry a regression test;
- slow/stress tests are tiered rather than silently omitted.

MQR adoption:
- every new Rust evaluator must have unit/regression tests;
- clippy warnings are CI failures;
- expensive world-contact tests may be a separate tier, but the cheap algebra/fixture tier must always run;
- new failure modes receive frozen regression fixtures.

### Cloudflare quiche
Useful pattern:
- fuzz targets are explicit repository surfaces;
- seed corpora and coverage procedures are documented;
- parser/protocol robustness is tested beyond hand-written examples.

MQR adoption:
- parsers, packet compilers and receipt decoders should gain fuzz/property-test surfaces when they become load-bearing;
- malformed evidence packets must fail closed;
- corpus seeds should include historical bugs and forbidden inference examples.

### agentgateway
Useful pattern:
- exact development toolchain/dependency behavior is documented;
- lockfile-consistent installs are used across local, CI and release paths;
- UI/e2e checks are separated from core Rust checks.

MQR adoption:
- CI commands should match documented local commands;
- dependency pinning is preferred for load-bearing executable surfaces;
- research-world-contact jobs remain separate from cheap core quality gates.

## Repository layers

### 1. Constitution
Contains:
- doctrine;
- stage preseal;
- admission/exclusion rules;
- promotion ceilings.

May not be rewritten after outcome reveal except through a successor receipt.

### 2. Executable adjudication
Contains:
- canonical evaluator;
- typed schemas;
- unit tests;
- negative fixtures;
- deterministic synthetic regression lane.

Must be buildable independently of external research outcomes.

### 3. Evidence metadata
Contains:
- immutable source identifiers;
- blob/commit hashes;
- run IDs;
- artifact hashes;
- masked profile seals;
- reveal receipts.

Keep this small and clone-friendly.

### 4. Large/raw artifacts
May live outside Git when:
- immutable or content-addressed custody exists;
- retrieval location is recorded;
- hash/size/schema are recorded;
- loss of the external object is treated as evidence loss, not silently reconstructed.

### 5. Human-readable receipt
Explains:
- what was frozen;
- what was run;
- what failed;
- what was excluded;
- what authority changed;
- what remains HOLD.

The prose receipt is never a substitute for machine evidence.

## Mandatory cheap CI for newly touched Rust research surfaces

1. cargo fmt --check
2. cargo clippy --all-targets -- -D warnings
3. cargo test
4. release build
5. deterministic synthetic/negative-fixture execution

World-contact/provider/native-application jobs may be slower and separately triggered.

## Failure discipline

A failed CI run is retained as a failure lineage when it changes the experiment.

Do not:
- delete an inconvenient failure and rerun under an unrecorded repair;
- edit a sealed prediction after reveal;
- reinterpret missing execution as negative evidence;
- promote a repaired pipeline as if the original pipeline had passed.

## Change discipline

For user-visible/executable semantic changes, record at least one of:
- successor-stage receipt;
- changelog entry;
- regression fixture;
- migration note.

Pure refactors need tests but not a scientific receipt unless they change evidence semantics.

## Fuzz/property-test promotion rule

Add a fuzz/property-test surface when a parser/compiler:
- accepts external evidence;
- maps evidence into authority-bearing states;
- performs schema migration;
- composes transport/bridge relations;
- has produced at least one historical parsing or boundary bug.

MQR-4.32 composition parsing is a candidate for this next.

## Anti-theater rule

Repository sophistication is not scientific authority.

A beautiful Rust crate with perfect CI can still encode a bad scientific constitution.

Conversely, a scientifically valuable result should not be excused from:
- reproducibility;
- clear artifact custody;
- regression protection;
- executable validation.

The target is:

SCIENTIFIC DISCIPLINE
AND
ENGINEERING DISCIPLINE

without allowing either to launder the other.


## 2026-09-25 engineering harvest — separate failure surfaces

Mature repositories do not treat one green `cargo test` job as a proxy for engineering quality. They separate failure families so that a success in one lane cannot hide failure in another.

The following patterns are now adopted as the target direction for newly touched MQR executable surfaces.

### Hugging Face tokenizers — canonical core plus independent compatibility surfaces

Observed engineering pattern:
- Rust build/test across Linux, Windows and macOS;
- Clippy across the platform matrix;
- formatting as an independent job;
- generated README consistency checks;
- dependency vulnerability audit;
- semantic-version compatibility checks;
- feature-combination testing rather than only `--all-features`;
- an independent released-crate oracle for a compatibility-sensitive component;
- Python/Node/documentation/release workflows separated from the Rust core.

MQR consequence:
- a canonical Rust core does not excuse untested adapters;
- when feature flags alter evidence semantics, test the relevant feature powerset or an explicitly justified covering array;
- generated doctrine/schema/interface artifacts must have drift checks;
- a successor executable surface should gain a version-compatibility oracle when backward compatibility is load-bearing.

### Astral uv — generated-state, lock-state and release-state as independent gates

Observed engineering pattern:
- formatting, lint, generated-file drift, lockfile consistency, publish checks and release checks are separate workflow families;
- snapshot tests make command behavior reviewable as an explicit artifact;
- benchmark and profiling workloads are versioned development surfaces;
- release artifacts carry provenance/attestation machinery.

MQR consequence:
- generated files and checked-in schemas may not silently drift from their generators;
- dependency lock consistency is a testable repository invariant;
- output-rich command-line adjudicators should prefer snapshot/golden testing where byte-level receipts are part of the contract;
- release/provenance checks are distinct from scientific world-contact.

### tokio-rs/topcoat — target and feature geometry are first-class

Observed engineering pattern:
- test, Clippy, format and documentation warnings are independent;
- feature-by-feature checks supplement all-feature builds;
- non-default compilation targets such as wasm are explicit gates;
- unused dependency checks and release gating are first-class.

MQR consequence:
- portability claims require explicit target matrices;
- `cargo check` on one host does not establish target transport;
- documentation compilation with warnings denied is appropriate when docs define executable or user-facing contracts;
- unused or accidental dependencies should be periodically audited on canonical crates.

### agentgateway — integration failures get their own evidence

Observed engineering pattern:
- platform-specific Rust tests;
- generated-code and lint lanes;
- UI end-to-end tests with traces retained on failure;
- controller tests, race checks, conformance tests and environment-level E2E;
- debug bundles and timing artifacts preserved for failed integration runs.

MQR consequence:
- native/provider/world-contact failures should preserve debug evidence rather than collapse to a red status;
- integration and conformance lanes are not substitutes for unit tests, and unit tests are not substitutes for integration;
- costly native-contact tests may be separately scheduled, but their failure artifacts must be retained long enough for adjudication.

## Gate families

A newly touched load-bearing MQR executable surface should use the smallest justified subset of the following independent families.

### G0 — deterministic core
Mandatory by default:
- formatter;
- linter with warnings denied;
- unit tests;
- release build;
- deterministic negative/regression fixtures.

### G1 — generated-contract integrity
Required when generated artifacts exist:
- schema regeneration dry-run;
- generated README/docs/API stub drift check;
- checked-in fixture or golden-output drift check;
- lockfile consistency check where lock state is part of reproducibility.

### G2 — compatibility geometry
Required when portability/transport is claimed:
- supported OS/target matrix;
- feature/configuration matrix;
- backward/forward version compatibility tests;
- adapter/binding concordance;
- independent released-version oracle where practical.

### G3 — integration and conformance
Required when behavior crosses process/provider/native boundaries:
- end-to-end or conformance tests;
- native application/provider smoke;
- retained traces/debug bundles on failure;
- explicit timeout/missingness semantics.

### G4 — security and supply-chain provenance
Required for release-bearing or externally consumed tooling:
- dependency advisory audit;
- pinned or policy-governed CI dependencies;
- artifact hashes and, when practical, attestations/signatures;
- release provenance distinct from scientific result provenance.

### G5 — scientific world contact
Research-only authority surface:
- preseal/admission contract;
- frozen prediction or criterion;
- world-facing execution;
- immutable result receipt;
- explicit failure/HOLD semantics.

G0–G4 can establish engineering quality.
They cannot manufacture G5 scientific authority.

G5 can produce valuable scientific evidence.
It does not excuse weak G0–G4 engineering.

## Tiering rule

Not every experimental helper needs every gate.

Classify newly touched executable surfaces:

- **Tier A — disposable diagnostic:** deterministic execution plus a recorded hash/commit is sufficient; no authority-bearing output.
- **Tier B — research adjudicator:** G0 mandatory; G1/G2 as applicable; malformed input fails closed.
- **Tier C — reusable research infrastructure:** G0–G3 mandatory as applicable; fuzz/property tests strongly preferred for parsers and state compilers.
- **Tier D — release-facing tooling:** G0–G4 mandatory as applicable; reproducible release/provenance policy required.

This prevents process theater while still raising the floor where failures are consequential.

## Snapshot/golden-output rule

Use snapshot or golden-output tests when:
- canonical text/JSON/TSV receipts are part of the public contract;
- a compiler/adjudicator emits human-reviewable state;
- a historical bug involved output ordering, omission or schema drift.

A snapshot update is a semantic change unless demonstrated otherwise.
It must be reviewed rather than blindly accepted.

## Failure-artifact rule

For expensive integration/native/provider jobs, a failure should preserve enough evidence to distinguish:
- build/setup failure;
- environment failure;
- target unavailable;
- execution timeout;
- semantic mismatch;
- parser/adjudicator failure.

A single red check is operationally useful but epistemically under-typed.

## Current language direction

Rust remains the default canonical language for newly touched MQR executable adjudication because typed enums, exhaustive matching, single-binary deployment and strong tooling fit the present failure model.

Other compiled/static languages are preferred over Python when they provide a concrete advantage for:
- target portability;
- type-level state constraints;
- native integration;
- performance;
- formal verification or stronger static analysis.

Python remains appropriate for:
- independent reference implementations;
- exploratory statistics;
- notebook-scale analysis;
- glue that is not authority-bearing.

Language choice never changes the scientific promotion rule.
