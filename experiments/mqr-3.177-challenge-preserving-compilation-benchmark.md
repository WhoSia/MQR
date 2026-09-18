# MQR-3.177 — Challenge-Preserving Compilation Benchmark Preseal

Status: BENCHMARK-CONSTITUTED / EMPIRICAL-EXECUTION-HOLD

## Founding question

Can an active paper/document interface preserve the live defeat geometry of its source artifact, rather than merely reproduce nominal outputs or remain operationally valid?

## Core distinction

EXECUTABILITY != CHALLENGE PRESERVATION.

Let a compilation K map a static epistemic artifact A into an active interface I:

K: A -> I.

Ordinary validation V_exec asks whether I runs and reproduces declared reference behavior.

Challenge-preserving validation V_cpc additionally asks whether I preserves the source's challenge-relevant semantics:

V_cpc = {
  domain/exclusion semantics,
  defaults/parameter semantics,
  units/preprocessing,
  boundary/initial conditions,
  failure/abstention behavior,
  stochasticity/seeds,
  output semantics,
  provenance/identity,
  dependency/environment assumptions,
  authority-type transitions
}.

A compiler earns CHALLENGE-PRESERVING status only if semantically load-bearing changes that preserve reference outputs are detectable or explicitly surfaced.

## Fatal criterion

CPC has no distinct operational value if an ordinary reference-output/integration validator already rejects nearly all challenge-relevant mutants.

CPC survives only if there exist mutants m such that:

1. m passes ordinary package/runtime/reference-output validation;
2. m changes at least one load-bearing defeat route;
3. CPC-aware validation rejects or localizes m;
4. the difference changes a scientifically relevant authority/reopenability judgment.

## Semantic-mutant families

### M1 — Boundary-condition mutant
Keep reference examples inside the original regime unchanged, but alter a boundary condition outside that reference slice.

Paper-agent example:
- source method excludes x < 0 or t > T;
- mutant silently extends/clips/wraps the domain.

HWPX analogue:
- document remains valid and text-equal on inspected paragraphs;
- locator stability semantics are changed so a revision-bound locator is presented as intrinsically stable.

Expected:
- V_exec: likely PASS on reference slice.
- V_cpc: FAIL.

### M2 — Default-parameter mutant
Preserve explicitly parameterized examples, but change an implicit default used in ordinary calls.

Paper-agent example:
- normalization, threshold, regularization, reference genome, solver tolerance.

HWPX analogue:
- edit API keeps explicit revision-guard examples correct but silently changes fallback locator resolution/default conflict policy.

Expected:
- V_exec: PASS when examples specify arguments.
- V_cpc: FAIL.

### M3 — Preprocessing/units mutant
Preserve post-preprocessed tutorial inputs while changing the raw-input preprocessing transform or units.

Expected:
- reference figure replay can PASS;
- transported execution on new data changes;
- V_cpc must detect preprocessing/units divergence.

### M4 — Failure-semantics mutant
Successful inputs behave identically, but an invalid/out-of-domain case that originally abstained/errors now coerces, clips, imputes or returns a value.

HWPX analogue:
- stale expected_revision or unknown locator is silently coerced instead of rejecting atomically.

Expected:
- success-path tests PASS;
- challenge geometry changes because a route that should expose incompatibility is erased.

### M5 — Stochasticity mutant
Reported seed/reference run remains identical, but seed handling, RNG source or nondeterministic dependency behavior changes.

Expected:
- single reference replay PASS;
- reproducibility/reopenability surface differs.

### M6 — Provenance/identity mutant
Outputs are byte/number-identical, but source version, dependency version, revision identity or provenance receipt is collapsed.

HWPX analogue:
- semantic_sha256 preserved but revision/structure provenance is not advanced or distinguishable.

Expected:
- ordinary output validation PASS;
- authority transport becomes ambiguous.

### M7 — Composition-authority mutant
Two source-bounded tools are composed. The resulting workflow reports parent source authority as though it transferred transitively to the novel composition.

Expected:
- computational execution PASS;
- authority typing FAIL.

### M8 — Maintenance-repair mutant
Dependency/API repair restores execution and reference figures while changing one scientifically load-bearing semantic dimension.

Expected:
- regression-on-output PASS;
- semantic regression FAIL.

## Three validator tiers

T0 PACKAGE/RUNTIME VALIDITY
- parses, imports, executes.

T1 REFERENCE-SURFACE FIDELITY
- tutorial/example outputs, reported figures, known cases.

T2 CHALLENGE-PRESERVING FIDELITY
- semantic mutant suite;
- boundary/failure tests;
- provenance and authority-transition checks;
- alternate/adverse-route reconstruction.

Constitutional rule:
T0/T1 success cannot be promoted to T2 by rhetoric.

## HWPX calibration result

The current HWPX MCP already implements several T2-like custody protections:
- explicit locator-stability classes;
- exact expected_revision;
- resolve-all-before-edit;
- candidate-package validation;
- atomic replace;
- semantic_sha256 + structure_sha256;
- stale/unknown/duplicate operation rejection without mutation.

Therefore M4/M6-like artifact-custody mutants are not merely hypothetical there: the project has explicitly designed them as failure conditions.

But HWPX visual/semantic equivalence is still bounded:
- no claim yet to native Hancom visual fidelity;
- structural/formatting operations remain out of current scope;
- renderer oracle is deferred.

This supports a general principle:
A validator can be challenge-preserving for one authority layer and incomplete for another.

## P2A status

Paper2Agent harvest supports the benchmark motivation:
- execution restoration != scientific-state restoration;
- validation on a declared reference surface need not exhaust boundary/failure semantics;
- cross-paper composition creates a new authority branch;
- semantic-mutant testing is the highest-value successor experiment.

However this Court does NOT claim that current Paper2Agent fails M1–M8 empirically.
No live Paper2Agent compiler/validator execution was performed here.

Therefore:
P2A SEMANTIC-MUTANT VERDICT = EMPIRICAL EXECUTION HOLD.

## MQR consequence

Challenge-Reconstruction Frontier (CRF) gains an operational representation:

CRF route r_j is not "preserved" merely because the executable interface can reproduce the source's successful outputs.

Preservation requires:
- source-side adverse condition can still be expressed;
- interface does not silently quotient away the failure distinction;
- relevant provenance/identity survives;
- failure semantics remain observable;
- substitute routes are recorded;
- composition creates new defeat obligations.

Thus CPC operationalizes only a slice of live Defeat Geometry:
artifact/method custody + executable challenge preservation.

It does not itself establish:
- truth of the claim;
- empirical adequacy outside tested domains;
- causal validity;
- realism;
- independent world contact.

## Authority firewall

SOURCE EXECUTABILITY != SOURCE AUTHORITY.
SOURCE AUTHORITY != COMPOSITION AUTHORITY.
CPC PASS != REALIST PROMOTION.

CPC can raise the ceiling on what can be responsibly re-tested.
It cannot supply the world-contact outcome.

## Verdict

BENCHMARK-CONSTITUTED / CPC OPERATIONAL OBJECT DEFINED / HWPX PROVIDES POSITIVE CUSTODY CALIBRATION / P2A SEMANTIC-MUTANT EXECUTION HOLD / NO CLAIM OF PAPER2AGENT FAILURE / CRF-TO-COMPILER BRIDGE ESTABLISHED / AUTHORITY FIREWALL PRESERVED / HISTORICAL NOVELTY HOLD / NO FIFTH FIELD.

## Reauthorization trigger

Execute the M1–M8 semantic-mutant suite against a real Paper2Agent-generated agent or equivalent paper-to-agent compiler, with T0/T1/T2 outcomes logged prospectively.

## Suggested next stage

MQR-3.178 — Semantic-Mutant Implementation Preseal, Boundary/Failure/Provenance Mutation Compiler, T0–T1–T2 Detection Matrix & Minimal Real Paper-Agent World-Contact Authorization — Executable Reopenability Probe
