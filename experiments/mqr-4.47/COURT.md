# MQR-4.47 — Translation-Challenge Constitution Court

Status: **CLOSED / B+C+D+E+F+G / A REJECTED-AS-WORLD-FACING-SUFFICIENT / H REJECTED / I REJECTED / TCCR+SFR+DRCM+PAG+SSR+DCR+CER+CRL+SAE / CONSTITUTED-REOPENABLE / OPEN-CHALLENGE-SPACE / MAIN-ONLY**

## Formal stage name

**MQR-4.47 — Translation-Challenge Constitution Court, Separator-Selection Authority, Challenge-Family Gerrymandering, Defeat-Route Coverage, Probe-Ancestry Independence, Challenge-Expansion Instability, Discriminator Capture & Whether Mapping Authority Can Be Narrowed by World-Facing Tests When the Space of Tests That Count as Relevant Separators Is Itself Contestable**

## Verdict

MQR-4.47 rejects the inference:

~~~text
WORLD-FACING PROBE
-> AUTHORIZED SEPARATOR
~~~

A world-facing challenge may genuinely contact the world while still being selected retrospectively, drawn from a gerrymandered family, ancestry-collapsed, route-incomplete, relevance-captured, score-captured, or unstable under admissible challenge expansion.

The positive result is narrower:

~~~text
TCCR Translation-Challenge Constitution Receipt
+ SFR Separator Family Registry
+ DRCM Defeat-Route Coverage Matrix
+ PAG Probe-Ancestry Graph
+ SSR Separator-Selection Receipt
+ DCR Discriminator Capture Receipt
+ CER Challenge Expansion Receipt
+ CRL Challenge Residue Ledger
+ SAE Separator Admissibility Envelope
-----------------------------------------------
SCOPED AUTHORITY TO NARROW A MAPPING CAS
WITHOUT CLAIMING CHALLENGE-SPACE COMPLETENESS
~~~

## Frozen branch verdicts

- **A WORLD-FACING-SUFFICIENT — REJECTED.** World contact alone does not authorize test selection.
- **B CONSTITUTED-SELECTION — PASS.** Candidate family, selected packet and selection rule must be separately receipted.
- **C ROUTE-COVERAGE — PASS.** Defeat-route coverage, not raw probe count, is the live adequacy surface.
- **D ANCESTRY-AWARE — PASS.** Surface-distinct probes sharing one load-bearing ancestry remain common-mode.
- **E CAPTURE-SENSITIVE — PASS.** Candidate-derived relevance/scoring defeats independent discrimination.
- **F EXPANSION-REOPENABLE — PASS.** Admissible challenge expansion may reopen prior narrowing.
- **G LOCAL-STABILITY — PASS.** Repeated finite stability can earn family-relative robustness only.
- **H CHALLENGE-CLOSURE — REJECTED.** No finite successful family certifies complete separator space.
- **I SEPARATOR-FATAL — REJECTED.** Contestability of challenge selection does not make all world-facing narrowing illegitimate; scoped authority survives under explicit constitution.

## Internal novelty kill

MQR-3.136 already established challenge-generator exteriority and ancestry.
MQR-3.137 already established captured relevance/admission as a governance problem.
MQR-3.138 already established challenge-opportunity allocation and common-mode challenge ecology.
MQR-3.172 already established multiple admissible translations.
MQR-4.46 already established set-valued mapping authority and local world-facing CAS narrowing.

Therefore MQR-4.47 claims no novelty for generic challenge diversity, relevance-veto capture, test selection, evidential diversity, or finite test-suite adequacy.

The residual problem is specifically:

~~~text
WHEN A FINITE WORLD-FACING PACKET
DIRECTLY NARROWS A BURDEN-TRANSLATION CAS,
WHAT CONSTITUTES THE AUTHORITY OF THAT PACKET?
~~~

## Separator selection

The executable court distinguishes:
- the registered candidate family;
- the selected packet;
- the selection rule;
- selection timing.

A registered family can contain opposite world-facing separators.

Selecting only one can produce:

~~~text
Q = {q_exact, q_overlap}

select q_exact   -> CAS_after = {EXACT}
select q_overlap -> CAS_after = {OVERLAP}
~~~

If an unselected registered counterprobe remains compatible with CAS_before but conflicts with the selected narrowing, the receipt reopens as:

~~~text
REOPEN_OMITTED_COUNTERPROBE
~~~

Thus registration alone does not cure cherry-picking; packet-selection provenance is load-bearing.

## Defeat-route coverage

Probe cardinality is not coverage.

The court separately computes:
- registered probe count;
- selected probe count;
- selected world-facing probe count;
- declared route count;
- covered route count;
- uncovered route count.

A six-probe family can still cover only two defeat routes.

~~~text
PROBE COUNT != DEFEAT-ROUTE COVERAGE
~~~

The declared route ontology is itself provisional. Complete declared coverage never changes:

~~~text
challenge.current_family_complete=NO
~~~

## Probe ancestry

Nominally separate probes may share one load-bearing ancestry.

The court distinguishes selected-world-facing probe count from selected ancestry count.

~~~text
2 WORLD-FACING PROBES
1 ANCESTRY
-> COMMON_MODE
~~~

Common ancestry can therefore block provisional narrowing even under declared route coverage.

## Discriminator capture

v0.14 executable capture witnesses are deliberately narrow:
- incumbent-defined selection rule;
- candidate-derived relevance for a selected world-facing probe;
- candidate-derived score source for a selected world-facing probe.

Any such witness yields:

~~~text
HOLD_DISCRIMINATOR_CAPTURE
~~~

This is a sufficient capture witness, not a complete theory of experimental bias.

## Post-outcome selection

A prospective registry does not rescue retrospective packet choice.

~~~text
REGISTER Q BEFORE OUTCOME
SELECT S AFTER OUTCOME
!=
PROSPECTIVE SEPARATOR AUTHORITY
~~~

The executable state is:

~~~text
HOLD_POST_OUTCOME_SELECTION
~~~

## Challenge expansion

After a selected family narrows CAS, an admissible expansion may:
- remain stable;
- narrow further;
- alter the live set;
- make the current relation set empty.

A disjoint expansion yields:

~~~text
REOPEN_EXPANSION_CONFLICT
~~~

Repeated finite stable expansions remain:

~~~text
LOCAL ROBUSTNESS
NOT
FUTURE CHALLENGE-SPACE CLOSURE
~~~

## Positive control

A clean packet requires:
- PRESEALED selection timing;
- independent selection rule under the declared capture checks;
- selected world-facing probes;
- complete declared defeat-route coverage;
- ancestry-separated selected probes;
- no omitted registered counterprobe;
- no declared capture witness;
- no reopening expansion.

Such a packet can earn:

~~~text
AUTHORIZED_PROVISIONAL_NARROWING
~~~

This is family-relative and challenge-relative authority only.

## Real-Language v0.14

Canonical surface:
- Rust: `language/real/src/challenge_v14.rs` / `real-v14-challenge`
- independent relational evaluator: `language/real/prolog/challenge_v14.pl`
- Lean: `language/real/lean/MQR/Challenge.lean`
- constitution: `language/real/V14-CHALLENGE-CONSTITUTION.md`

Hard guards:

~~~text
challenge.current_family_complete=NO
challenge.future_challenge_space_closed=NO
challenge.probe_count_truth_oracle=NO
challenge.externality_truth_oracle=NO
challenge.cost_truth_oracle=NO
challenge.selection_rule_truth_oracle=NO
challenge.guidance_mode=CONSTITUTED_REOPENABLE_SEPARATOR_AUTHORITY
~~~

## Independent evaluator incident and repair

During implementation, Rust accepted clean/cherry fixtures while the Prolog evaluator rejected them before scientific adjudication.

The failure was localized to the Prolog reference-integrity contract. Parser and required-field checks passed; the four cross-reference guards failed together.

The reference guards were rewritten as explicit `forall/2` predicates without changing the scientific semantics:

~~~text
valid_cover_probe_refs
valid_cover_route_refs
valid_score_refs
valid_relevance_refs
~~~

After the repair:
- dedicated MQR-4.47 Court: SUCCESS;
- Rust-Prolog concordance: PASS;
- full Real-Language regression through v0.14: SUCCESS.

The failed diagnostic workflows were temporary and removed before closure.

## Formal boundary

Lean proves with empty axiom ancestry:
- equal probe counts do not determine defeat-route coverage;
- equal probe counts do not determine ancestry independence;
- one registered family can support opposite cherry-picked narrowings;
- complete declared route coverage does not imply future challenge completeness;
- candidate-derived scoring does not establish independent discrimination;
- challenge expansion can reopen prior narrowing;
- repeated finite stability does not imply future closure;
- world-facing status alone does not create selection authority.

The theorem family is independently replayed with pinned lean4export + nanoda.

## Literature pressure

Post-preseal literature pressure included:
- Mayo & Spanos on severity;
- Stegenga & Menon on independent evidence;
- Kuorikoski & Marchionni on evidential diversity/triangulation;
- Simmons, Nelson & Simonsohn on analytic flexibility;
- Steegen et al. on multiverse analysis;
- Dwork et al. on reusable holdouts;
- Weyuker and Fraser & Walkinshaw on test adequacy.

All load-bearing sources used for this court were already present in Drive.

No new DOI intake is required.

## Pre-closure executable checkpoint

After the Prolog contract repair:

~~~text
aa2ad739a68190bd7c8c6fca2873438c702d535e

36222603706  MQR-4.47/Court      SUCCESS
36222603699  Real-Language/CI    SUCCESS
~~~

Dedicated and integrated Lean v0.14 proof surfaces had already passed before the parser repair; the final same-head seal reruns all four surfaces together.

## Stop-rule audit

- opposite cherry-pick narrowing executable: PASS
- post-outcome packet selection executable: PASS
- probe-count/route-count gerrymandering executable: PASS
- common-ancestry probe plurality executable: PASS
- declared route-coverage hole executable: PASS
- candidate-derived scoring/relevance capture executable: PASS
- clean ancestry-separated positive control executable: PASS
- held-out/world-facing provisional narrowing executable: PASS
- challenge expansion reopening executable: PASS
- repeated finite stability remains non-closure: PASS
- Rust-Prolog concordance: PASS
- Lean theorem boundary: PASS
- literature contacted after preseal: PASS
- current family completeness disabled: PASS
- future challenge-space closure disabled: PASS
- main-only policy: REQUIRED FOR FINAL SEAL

## Closure thesis

~~~text
THE WORLD CAN ANSWER
ONLY THE QUESTIONS WE ACTUALLY ASK.

THEREFORE WORLD CONTACT
DOES NOT BY ITSELF
AUTHORIZE THE QUESTION SET.

A SEPARATOR FAMILY EARNS
ONLY SCOPED NARROWING AUTHORITY
WHEN ITS SELECTION,
ROUTE COVERAGE,
ANCESTRY,
CAPTURE RISK,
AND EXPANSION SENSITIVITY
ARE EXPLICITLY AUDITABLE.

MANY PROBES DO NOT MAKE
A COMPLETE TEST SPACE.

STABLE FINITE EXPANSION
DOES NOT CLOSE THE FUTURE.

WHEN NEW COUNTERPROBES ARRIVE,
REOPEN.
~~~
