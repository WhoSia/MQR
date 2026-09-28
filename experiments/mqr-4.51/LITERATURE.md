# MQR-4.51 — Literature Pressure, Machinery Donors & Novelty Kill

Status: POST-PRESEAL / CANONICAL-PAPERS-READ / CROSS-LAB-HARVEST / CLAIM-CEILING ACTIVE

Preseal commit: `c61c9516a4e38ee1241a30ca3d09186bc58b53e8`.

## Intake normalization

Four newly supplied papers were resolved after the preseal and moved from `00_INTAKE — Literature Radar` to the canonical `10_PAPERS — Canonical Literature Commons` with Drive IDs/raw bytes preserved:

- Hubacher Haerle (2026), *Rational Uncertainty and the Success Norm for Inquiry* — DOI 10.1093/mind/fzaf057.
- González de Prado (2026), *Higher-Order Uncertainty at the End of Inquiry* — DOI 10.1017/epi.2025.10096.
- Douven & Wagner (2025), *Acceptance in the Context of Inquiry* — DOI 10.1007/s13194-025-00688-8.
- Carolan (2026), *Saturation or Sufficiency? Epistemic Closure and the Problem of “Enough” in Qualitative Research* — DOI 10.1111/soin.70061.

No second bibliographic copy of these four was found in the Commons during exact-title/DOI resolution.

## Cross-lab canonical papers reused without duplication

The following relevant papers were already canonical in `10_PAPERS`; no new physical copy was made:

- Lehrer & Wang (2024), *The Value of Information in Stopping Problems*.
- Russell & Wefald (1991), *Principles of Metareasoning*.
- Horvitz (1987), *Reasoning About Beliefs and Actions Under Computational Resource Constraints*.
- Callaway et al. (2022), *Rational Use of Cognitive Resources in Human Planning*.
- Agrawal, McHale & Oettl (2023), *Artificial Intelligence and Scientific Discovery: A Model of Prioritized Search*.
- Veiga & Renoux (2023), *From Reactive to Active Sensing: A Survey on Information Gathering in Decision-theoretic Planning*.
- Stanton & Roelich (2021), *Decision Making under Deep Uncertainties: A Review of the Applicability of Methods in Practice*.
- MacKay (1992), *Information-Based Objective Functions for Active Data Selection*.

This is cross-lab semantic reuse over one Commons custody object, not paper duplication.

## Novelty kill

### Inquiry may rationally stop without certainty

Hubacher Haerle argues that rational inquiry itself can have epistemic limits and that uncertainty may remain when continued inquiry is not rationally supportable.

González de Prado argues that higher-order uncertainty can persist at the end of inquiry, including when additional checking is ineffective, inadvisable, or optional.

**Novelty killed:** MQR-4.51 cannot claim the generic idea that unresolved uncertainty is compatible with rational stopping.

### No context-free stopping winner

Douven & Wagner compare stopping/acceptance rules by simulation and show different speed–accuracy trade-offs. Which trade-off is appropriate depends on the inquiry context.

**Novelty killed:** MQR-4.51 cannot claim that stopping policies should be evaluated on both error and delay/cost, or that there is one context-free optimal rule.

This directly supports the presealed anti-scalarization decision: the primary result should remain a vector/Pareto comparison, not an arbitrary universal weighted score.

### Sufficiency is not discovered completeness

Carolan reframes qualitative saturation as socially justified epistemic closure/sufficiency despite further possible data and interpretations, distinguishing multiple grammars of closure.

**Novelty killed:** the generic distinction between exhaustiveness and enoughness, and the claim that stopping requires a defensible sufficiency practice rather than literal data exhaustion.

**Counter-pressure:** a machine-generated MQR receipt must not confuse procedural/audit credibility with independently calibrated scientific usefulness. This is exactly why 4.51 tests 4.50 instead of merely restating it.

### Value of information / metareasoning

Lehrer & Wang formalize stopping when further information has value but carries delay/acquisition cost.

Russell & Wefald and Horvitz make computation/reasoning itself a resource-allocation problem whose value depends on effects on external action.

Callaway et al. connect planning effort to rational allocation of cognitive resources.

**Novelty killed:** inquiry-budget allocation, computational effort as a cost, value-of-further-reasoning, and stopping by resource-sensitive metareasoning are prior art.

**Machinery donor:** distinguish value of another inquiry step from the value of the final external action; benchmark over-inquiry cost separately from action error.

### Active information gathering

MacKay derives different active-data-selection criteria from different information objectives and explicitly notes dependence on the correctness of the assumed hypothesis space.

Veiga & Renoux survey active sensing where information gathering can itself be the goal of decision-theoretic planning.

**Novelty killed:** active choice of what information to gather next and expected informativeness are not MQR inventions.

**Countermodel donor:** high expected information gain inside a misspecified/too-small hypothesis space does not certify open-world adequacy; MQR must preserve upstream-admissibility and reopening.

### Scientific search allocation

Agrawal, McHale & Oettl model scientific discovery as prioritized sequential search over a vast combinatorial hypothesis space.

**Novelty killed:** finite scientific search budgets and prioritization of hypothesis exploration are not novel.

**Machinery donor:** a stop rule should be assessed against allocation opportunity cost and late discoveries, not only current confidence.

### Deep uncertainty

Stanton & Roelich synthesize robust/adaptive decision methods under deep uncertainty and stress dependence on institutional, organizational and individual context.

**Novelty killed:** robust action under unresolved model/future uncertainty and context-sensitive decision framing are prior art.

## Scoring correction induced by literature-independent audit

Before implementation, the preseal was found to contain a scorer tension: a full-future suffix oracle would label a legitimate local stop as premature merely because genuinely new post-stop evidence later arrives.

This is repaired in `AMENDMENT-A-LOCAL-STOP-VS-REOPEN.md` by separating:
- missed obligations already live/reachable before stopping -> premature-stop error;
- genuinely novel post-stop contact -> reopening-latency test.

The correction does not come from literature and changes no policy threshold.

## Surviving candidate contribution

The literature leaves a narrower conjunction-level candidate:

~~~text
UPSTREAM-ADMITTED SCIENTIFIC-AUTHORITY TRACE
+ OUTCOME-SEQUESTERED POLICY EXECUTION
+ LIVE-OBLIGATION PREMATURE-STOP SCORING
+ OVER-INQUIRY COST
+ ACTION ERROR
+ POST-STOP REOPENING LATENCY
+ COUNTERFACTUAL STOP/CONTINUE REPLAY
+ CALIBRATION-ONLY BASELINE TUNING
+ UNTOUCHED HOLDOUT
+ SAME-KERNEL CROSS-DOMAIN TRANSPORT
+ NON-SCALAR PRIMARY VERDICT
------------------------------------------------
PROSPECTIVE INTERNAL CALIBRATION
OF A REOPENABLE SCIENTIFIC-AUTHORITY STOP RULE
~~~

If this survives, the contribution is not a new stopping theory. It is an executable calibration constitution for whether MQR's own operational stop receipt improves finite inquiry behavior under predeclared adversarial trace families.

## External-validity ceiling

Even a perfect generated holdout result would remain:

~~~text
INTERNAL BENCHMARK CALIBRATION = POSSIBLE
EXTERNAL SCIENTIFIC CALIBRATION = HOLD
UNIVERSAL STOPPING OPTIMALITY = FORBIDDEN
~~~

Naturalistic or experimental external calibration would require a later prospective stage with independently arising inquiry traces.
