# MQR-3.178 — Semantic-Mutant Implementation Preseal

Status: MUTANT-SET-NARROWED / PAPER2AGENT-T2-STRONGER-THAN-EXPECTED / MINIMAL-WORLD-CONTACT-AUTHORIZED

## Founding question

Can a real paper-to-agent pipeline be made to pass execution/reference validation while silently altering a challenge-relevant semantic or provenance route, and can a challenge-preserving validator distinguish that case?

## External calibration

The public Paper2Agent implementation is substantially stronger than a simple reference-replay validator.

Its fresh independent verifier explicitly requires:
- direct upstream execution and source binding inspection;
- full relevant reference values and figures;
- meaningful changed inputs and supported parameters;
- checks for ignored inputs, changed defaults, and label misalignment;
- relevant missing/invalid inputs and upstream failures;
- source reuse and wrapper-quality review;
- actual MCP calls;
- hashed verification reports.

Its runtime layer also:
- snapshots the resolved environment;
- pins tested runtime dependencies for delivery;
- validates a fresh runtime install;
- records repository/source identity and tested-file hashes.

Therefore the original M1/M2/M4 families are not assumed easy escapes. They become controls.

## Constitutional correction to MQR-3.177

T2 must not be defined as "checks that Paper2Agent does not already do."

Instead:
T2 = challenge-preserving fidelity at the strongest currently implemented validation surface.

If an existing system already implements a proposed CPC requirement, MQR receives no distinctness credit for that requirement.

## Minimal mutant set

Only three probes are authorized for the first real run.

### SM-B — Boundary-holdout semantic mutant

Target:
A small public repository with explicit documented domain/boundary behavior and no external API key.

Preferred target:
NCAR/pop-tools or another lightweight Paper2Agent-supported repository with a deterministic function whose boundary behavior is source-documented.

Mutation:
Alter exactly one load-bearing boundary behavior outside the tutorial/reference slice while preserving:
- import/runtime;
- tutorial/reference outputs;
- one ordinary changed-input case;
- tool signature.

Examples of admissible mutation forms:
- strict error -> clipping at one boundary;
- half-open interval -> closed interval;
- explicit unsupported region -> silent coercion.

Presealed prediction:
- T0: PASS.
- T1: PASS by construction.
- Paper2Agent verifier: EXPECTED FAIL if source review or independently chosen changed/error input reaches the boundary.
- CPC adversarial holdout: MUST FAIL.

Interpretation:
If Paper2Agent catches SM-B, this is evidence that its current verification already implements a real slice of CPC. MQR must not count that slice as novel.
If Paper2Agent passes SM-B while CPC holdout catches it, a residual CPC gap survives.

### SM-F — Failure-semantics laundering mutant

Target:
A deterministic tool with a source-backed invalid-input or upstream-failure contract.

Mutation:
Change one source-backed fail/abstain/error route into a successful coercion while keeping all valid-input outputs identical.

Presealed prediction:
- T0: PASS.
- T1 positive cases: PASS.
- Paper2Agent fresh verifier: EXPECTED FAIL because current verifier instructions explicitly require relevant missing/invalid inputs and upstream failures.
- CPC failure-contract test: MUST FAIL.

Interpretation:
SM-F is a positive control on whether the public verifier executes its own stated failure-semantics doctrine.
If it is caught, CPC receives no novelty credit for the generic rule FAILURE SEMANTICS MATTER.

### SM-P — Recorded-provenance authentication mutant

Target:
Paper2Agent workflow-state validation, independent of any scientific method.

Mutation:
After a structurally valid recorded workflow is assembled, replace repository.commit with another syntactically valid 40-character hash while leaving the local source bytes, selected source hashes, production files, and run reports unchanged.

Public implementation states that repository.commit is recorded source identity but the workflow helper does not query Git or authenticate that identity against a remote.

Presealed prediction:
- package/runtime and scientific reference checks: unchanged;
- workflow helper: EXPECTED PASS if no additional coordinator-side remote check is performed;
- CPC provenance validator with remote commit attestation: FAIL.

Interpretation:
This is not a truth-of-science failure. It is a provenance-custody failure.
If the documented behavior is reproduced, CPC retains a narrow operational residue:
RECORDED PROVENANCE != AUTHENTICATED PROVENANCE.

No claim follows that Paper2Agent is unsafe or scientifically unreliable. The public documentation already marks this helper boundary.

## Deferred mutants

### M2 implicit-default mutant
DEFER as first-line discriminator.
Reason: current verifier explicitly checks changed defaults and meaningful parameter variation.

### M3 preprocessing/units mutant
RESERVE.
Potentially valuable, but requires selecting a repository whose preprocessing contract is explicit enough to avoid inventing semantics.

### M5 stochasticity mutant
RESERVE.
Requires a method with source-backed seed/RNG semantics.

### M7 composition-authority mutant
HOLD-NONEXECUTABLE.
Current pipeline has no machine-readable epistemic-authority type that can be mutated without first inventing a new schema.

### M8 maintenance semantic drift
HIGH-VALUE RESERVE.
Requires two real dependency/API states where reference cases remain invariant while a load-bearing semantic changes. More expensive than the first probe.

## Target selection rule

The first scientific target must satisfy:
1. public repository;
2. no restricted credentials/API keys;
3. deterministic or tightly controlled execution;
4. small enough for cheap agentification;
5. explicit source-backed boundary or invalid-input semantics;
6. at least one tutorial/example that does not itself exercise the chosen mutant boundary;
7. existing Paper2Agent compatibility or close alignment.

Current preferred first target:
NCAR/pop-tools, because Paper2Agent already used POP-TOOLS in published adversarial evaluation and tutorial-removal ablation, and the repository is public and installable.

Fallback:
MLearner, already present in Paper2Agent's adversarial benchmark set.

Final target is not frozen until the exact function and source-backed contract are identified before mutation.

## T0–T1–T2 matrix

| Probe | T0 runtime | T1 reference | Existing Paper2Agent verifier | CPC adversarial validator |
|---|---|---|---|---|
| SM-B boundary holdout | PASS expected | PASS required | FAIL expected | FAIL required |
| SM-F failure laundering | PASS expected | PASS on valid cases | FAIL expected | FAIL required |
| SM-P provenance auth | PASS/NA | PASS/NA | workflow helper PASS expected | FAIL required |

## Fatal criteria

### CPC reduction
If Paper2Agent catches SM-B and SM-F, and a small remote-attestation addition closes SM-P, then most of CPC's operational content is engineering provenance/test discipline already instantiated in the system. MQR must reduce its claim accordingly.

### CPC residual survival
A distinct operational residue survives only if:
- T0/T1 pass;
- existing Paper2Agent verification passes;
- CPC adversarial validation fails the mutant;
- the mutant changes a load-bearing challenge route or provenance route.

### Philosophical firewall
Even a surviving CPC residual does not by itself establish new realist philosophy.
It only operationalizes a portion of live Defeat Geometry.

## Minimal world-contact authorization

AUTHORIZED, but bounded.

Authorized execution packet:
1. freeze one source repository commit;
2. identify one exact source-backed boundary/failure contract;
3. generate baseline Paper2Agent MCP;
4. verify baseline through its native verifier;
5. inject one mutant only;
6. rerun the same Paper2Agent pipeline/verifier without revealing mutant location;
7. independently run the presealed CPC holdout;
8. log T0/T1/P2A-T2/CPC-T2 outcomes;
9. do not repair the mutant before verdict;
10. stop after one boundary/failure mutant plus the provenance-helper probe.

Not authorized in this stage:
- broad benchmark expansion;
- changing validator criteria after seeing failures;
- selecting a different mutant because the first was caught;
- claiming Paper2Agent weakness from a known documented helper limitation;
- philosophical promotion from one software result.

## Current verdict

MQR-3.178 = PASS-PRESEAL / NEGATIVE-CORRECTION.

The public implementation defeated the easy version of MQR-3.177:
Paper2Agent is already more challenge-aware than a T1 reference validator.

Surviving first-run probes:
- boundary holdout;
- failure-semantics laundering;
- recorded-vs-authenticated provenance.

The strongest immediate falsifier is not "Paper2Agent fails semantics."
It is:
PAPER2AGENT CATCHES THE SEMANTIC MUTANTS IT CLAIMS TO CHECK.

If that happens, MQR must credit the rival and narrow CPC.

## Reauthorization trigger

Actual command execution of the frozen baseline + one semantic mutant + provenance helper probe.

## Suggested successor

MQR-3.179 — First Executable Semantic-Mutant World Contact, POP-TOOLS Boundary/Failure Contract Freeze, Blind Baseline-vs-Mutant Agentification & Whether Challenge-Preserving Compilation Survives a Rival That Already Implements Independent Changed-Input Verification
