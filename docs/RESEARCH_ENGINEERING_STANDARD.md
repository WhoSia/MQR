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
