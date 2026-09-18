# MQR-3.176 — Historical Challenge-Reconstruction Fatal Test

Status: HISTORICAL-STRESS / RETROSPECTIVE-PRESEAL / P2A-REVERSE-IMPORT

## Epistemic warning

This is not a truly blinded natural experiment: the historical outcomes are already known. The anti-hindsight control is therefore weaker: freeze the explanatory variables and rival predictions before using outcome timing/mechanism as validation, and treat the result as a historical stress test rather than causal proof.

## Presealed variables

For claim C at time t, define the live challenge-route set:

L_t(C) = { r_j = (trigger, witness, reconstruction path, semantic fidelity, independence, cost, authority role) }.

A route can be:
- LIVE: reconstructible with bounded cost and known semantics;
- DEGRADED: reconstructible only through substantial forensic repair or uncertain semantic equivalence;
- DEAD: the load-bearing witness is unavailable and no licensed substitute route exists.

Do not classify the entire claim by archive status alone. A dead route may be replaced by another noncommon route.

Historical prediction:
1. lower-cost, semantically faithful live routes should enable faster/localized correction when a claim is wrong;
2. dead primary routes should increase reliance on indirect substitutes and weaken localization;
3. preservation of positive credit across succession should preserve relevant adverse burdens unless fresh noncommon contact supersedes them;
4. genuinely fresh severe contact can retire obsolete lineage debt.

## Episodes

### H1 — Antarctic ozone / TOMS (1979–1986)
The satellite system had recorded extreme low-ozone observations, but the retrieval/QC regime flagged values far outside the standard-profile range. After the British Antarctic Survey result, NASA re-examined TOMS/SBUV and reconstructed the regional hole. The underlying measurement stream and processing system remained available enough for reprocessing.

Preseal classification: PRIMARY ROUTE DEGRADED-BUT-LIVE.
Prediction: rapid correction/reinterpretation after external trigger.

### H2 — Helicobacter pylori culture (1982)
Routine lab handling discarded plates after ~48 h. The organism required roughly five days to become visible. An Easter-weekend interruption kept the culture alive long enough for colonies to appear.

Preseal classification: ROUTE SEMANTICALLY MIS-SPECIFIED; WITNESS PHYSICALLY DESTROYED BY STANDARD PROTOCOL UNTIL ACCIDENTAL WINDOW EXTENSION.
Prediction: correction requires reopening a boundary condition (incubation duration), not merely gathering more of the same 48 h data.

### H3 — OPERA superluminal-neutrino anomaly (2011–2012)
The collaboration exposed the anomaly, rechecked timing, scheduled short-pulse runs, and competing Gran Sasso experiments tested the same time-of-flight question. A faulty element in the fibre-optic timing system was identified; four experiments reported speeds consistent with light.

Preseal classification: MULTIPLE LIVE NONCOMMON ROUTES / HIGH RECONSTRUCTION CAPACITY.
Prediction: fast localization and authority reversal.

### H4 — Schön misconduct (2002)
Primary electronic data were deleted; systematic laboratory records were absent; devices/samples were unavailable or unusable. Yet independent replication failures and internal duplication/noise-pattern evidence supplied alternative defeat routes and supported misconduct findings/retractions.

Preseal classification: PRIMARY ROUTE DEAD / SUBSTITUTE ROUTES LIVE.
Prediction: original phenomena cannot be directly reconstructed; correction remains possible but through forensic/indirect routes, with weaker direct localization of the claimed physical effect.

### H5 — Potti/Nevins genomic signatures (2007–2011)
Independent forensic bioinformatics reconstructed supplied data/code and found serious irregularities. The effort was extremely costly (>1,500 person-hours). Later access to data/code enabled NCI re-evaluation to expose unstable models and non-reproducible validation.

Preseal classification: DEGRADED ROUTE / HIGH RECONSTRUCTION COST / PARTIAL ARTIFACT ACCESS.
Prediction: correction possible but delayed and labor-intensive; availability/provenance of raw data/code materially changes challenge capacity.

## Historical result

The binary hypothesis ARCHIVE-ALIVE > ARCHIVE-DEAD is rejected as too coarse.

Surviving law:
CURRENT AUTHORITY depends on the frontier of materially relevant challenge routes, not on the mere persistence of a static archive.

A useful internal representation is:
DG_t(C) contains route vectors r_j and a challenge-reconstruction frontier CRF_t(C).

CRF dimensions:
- semantic fidelity to the original method/claim;
- physical/data witness availability;
- noncommonness / independence;
- reconstruction competence;
- expected cost/time;
- localization power;
- authority role;
- replaceability by other routes.

No fifth runtime field is required; CRF is a view of live Defeat Geometry.

## Successor credit/burden symmetry

Historical test does not establish a universal causal law, but it sharpens the normative rule:

If a successor claims authority by transporting an ancestor's successful structure/result, relevant unresolved adverse routes travel with that transported constraint unless:
1. fresh noncommon contact defeats the adverse concern;
2. a licensed translation shows the old challenge no longer targets the transported content; or
3. a stronger substitute route resolves it.

Positive lineage without negative lineage is authority laundering.

## Paper2Agent reverse import

Paper2Agent suggests a concrete operational probe for CRF.

### Import P1 — challenge-preserving compilation
Static paper + code + data + supplements can be compiled into an executable interface. The scientific question is not merely "does it run?" but whether the compilation preserves the challenge-relevant semantics: domain, defaults, units, preprocessing, boundary/initial conditions, failure/abstention behaviour, stochasticity, output meaning, provenance and dependency versions.

### Import P2 — agentification failure as route witness
Failure to agentify may indicate missing code/data, environment breakage, tacit steps, or non-generalizable scripts. It is evidence about reconstruction capacity, but is NOT a pure reproducibility score because compiler limitations and paper type confound it.

### Import P3 — execution restoration != scientific-state restoration
Dependency repair can make a workflow run while changing scientific semantics. Reopenability requires semantic regression, not only runtime regression.

### Import P4 — authority-typed execution
SOURCE-BOUND -> SOURCE-EXECUTED -> TRANSPORTED-EXECUTION -> MODEL-INTERPRETED -> CROSS-SOURCE-SYNTHESIS -> NOVEL-HYPOTHESIS are different authority states. Cross-paper composition creates a new branch; parent authority is not inherited transitively.

### Import P5 — semantic-mutant challenge
Create mutants that preserve tutorials/reference figures but change one load-bearing boundary/default/failure semantic. A challenge compiler that cannot detect these mutants is executable but epistemically weak.

## HWPX relation

The HWPX MCP and Paper2Agent share a structural pattern:

STATIC ARTIFACT -> ACTIVE INTERFACE -> IDENTITY/PROVENANCE-PRESERVING OPERATIONS -> VALIDATION -> REUSABLE EXECUTABLE SURFACE.

But their authority targets differ:
- HWPX MCP primarily protects document/artifact identity, revision custody, rendering and transaction integrity.
- Paper2Agent targets executable scientific-method reconstruction.
- MQR asks whether the resulting active surface preserves live defeat opportunities.

Thus the common abstraction is not "documents should become agents." It is:

CHALLENGE-PRESERVING COMPILATION — converting a static epistemic artifact into an active interface without laundering identity, boundary conditions, failure semantics, provenance or authority.

## Verdict

HISTORICAL-FATAL-TEST = PASS-WITH-CONSTITUTIONAL-REVISION.

Rejected:
- binary archive-alive/archive-dead;
- static artifact availability as a sufficient reopenability measure;
- permanent lineage penalty.

Retained:
- route-set challenge capacity;
- graded reconstruction cost;
- substitute-route topology;
- successor credit/burden symmetry;
- fresh-contact debt retirement.

P2A reverse import = ADOPT AS OPERATIONALIZATION CANDIDATE, NOT PHILOSOPHICAL PRIORITY CLAIM.

Next:
MQR-3.177 — Challenge-Preserving Compilation, Executable Epistemic Custody, Semantic-Mutant Reopenability Benchmark & Whether Active Paper/Document Interfaces Can Operationalize Live Defeat Geometry without Confusing Executability with Scientific Authority.
