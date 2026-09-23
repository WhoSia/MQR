# MQR-4.8 — Evaluator-Leakage Attack, Hidden-Identity Engineering Packets, Independent Rival Compilation, Post-Freeze Outcome Reveal & Whether Tool-Sequence Blindness Survives Model-Memory and Case-Recognition Confounds

## 0. Question
MQR-4.7 established freeze -> held-out reveal -> adjudicate, but the evaluator was a pretrained language model and the engineering case was public.

MQR-4.8 asks whether tool-sequence outcome blindness survives evaluator-side case recognition, latent training memory and benchmark contamination.

Answer: NOT AUTOMATICALLY.

## 1. Identity masking is insufficient
Removing title, source name, DOI, report number, institution, benchmark name or URL does not prove blindness.

A model may still recognize a case through:
- variable vocabulary;
- characteristic parameter ranges;
- benchmark-specific wording;
- distinctive mechanism combinations;
- canonical-example structure;
- public plots/tables encountered during training;
- paraphrased or synthetic derivatives of the source.

Therefore:
IDENTITY MASKING != TRAINING-MEMORY INDEPENDENCE.

## 2. Leakage channels
L1 DIRECT IDENTITY LEAKAGE — explicit identifiers.
L2 DOMAIN FINGERPRINT LEAKAGE — variable vocabulary/regime reveals the source family.
L3 MECHANISM FINGERPRINT LEAKAGE — distinctive causal structure identifies the canonical case.
L4 LATENT OUTCOME MEMORY — the evaluator may not consciously identify the case but memorized associations can bias direction, confidence, parameter range or expected failure mode.

L4 cannot be ruled out by evaluator self-report.

## 3. Hidden-identity packet levels
M0 IDENTITY-REVEALED — source identity and domain labels present.
M1 DOMAIN-CUED / IDENTITY-HIDDEN — names and source identifiers removed; physical semantics retained.
M2 MECHANISM-MASKED — source-specific names and salient variable labels replaced by neutral symbols while preserving causal topology, dimensional relations, baseline evidence and intervention structure.

M2 must not erase the scientific problem itself.

## 4. Pre-outcome recognition probe
Before any rival prediction, the evaluator must freeze:
1. whether the case/source family is recognized;
2. guessed domain;
3. guessed benchmark/report/canonical example;
4. recognition confidence;
5. whether a specific outcome direction already feels familiar.

If exact identity is recognized with high confidence or the outcome is reported as familiar, that packet cannot count as a clean blind test for that evaluator.

## 5. Prediction invariance test
For one scientific structure generate semantically equivalent variants:
- original wording;
- paraphrased wording;
- variable-renamed wording;
- evidence-order-shuffled wording.

Large changes in predicted winner, confidence, mechanism or threshold under meaning-preserving edits are a contamination/memorization warning.

This does not prove contamination by itself, but defeats a clean-blindness claim.

## 6. Independent rival compilation requirement
The same agent cannot strongly establish independence if it selects the source, knows its identity/outcome, writes the rivals and then merely hides names from itself.

Confirmatory roles:
COMPILER — sees source identity/outcome and produces masked packet + immutable receipt.
ADJUDICATOR — sees only pre-outcome packet; no identity/outcome.
SCORER — sees frozen prediction and revealed outcome only after adjudication.

At minimum, adjudicator context must be isolated from compiler context.

## 7. Post-freeze reveal
Reveal must disclose exact source identity, held-out outcome, masked-variable mapping and data-reduction caveats.
No packet may be modified after prediction freeze.

If masking removed a load-bearing variable: PACKET INVALID, not post-hoc repair.

## 8. Public-source contamination ceiling
For public historical sources, frontier-model training-memory risk cannot be eliminated by prompt masking alone because the evaluator generally cannot audit its complete training corpus.

Public-source tests may earn:
- SEQUENCE-HELD-OUT;
- IDENTITY-MASKED;
- MASKING-ROBUST if perturbation tests pass.

They cannot automatically earn TRAINING-INDEPENDENT status.

## 9. Source-strength ordering
Leakage risk generally decreases from:
1. famous public historical case;
2. obscure public historical case;
3. newly published post-cutoff case;
4. private/sealed preexisting case never publicly indexed;
5. newly generated measurement after prediction freeze.

Recent alone does not establish unseen if the provider could have accessed it before evaluation.

## 10. Reassessment of MQR-4.7
MQR-4.7 remains valid as TOOL-SEQUENCE PROCEDURAL HELD-OUT WORLD-CONTACT.

It demonstrated prediction freeze before source reveal, fixed win criteria, and post-reveal authority update from physical data.

But:
MQR-4.7 != MEMORY-INDEPENDENT BLIND CONFIRMATION.

E387 is a public canonical low-Re airfoil case and plausibly exists in large-scale training corpora.

Therefore 4.7 authority is typed:
procedural held-out evidence + external physical world-contact - unresolved evaluator-memory independence.

No engineering result from 4.7 is revoked. Only blindness authority is narrowed.

## 11. Blindness falsifier
A future packet counts as evaluator-blind only if:
C1 DIRECT MASKING — no source identity.
C2 RECOGNITION PROBE — exact identity not recognized with high confidence.
C3 PERTURBATION INVARIANCE — prediction stable under paraphrase / variable rename / order change.
C4 CONTEXT ISOLATION — adjudicator does not share compiler context.
C5 OUTCOME SEALING — outcome inaccessible until prediction receipt exists.
C6 SOURCE FRESHNESS OR EXCLUSION EVIDENCE — post-cutoff/new measurement or credible evidence source was unavailable to training/development.

Failure of C6 does not invalidate engineering data. It limits the claim to procedural blindness.

## 12. Four non-substitutable blindness labels
SEQUENCE-HELD-OUT — outcome revealed after prediction freeze in the current execution.
IDENTITY-MASKED — explicit case identifiers removed.
CONTEXT-INDEPENDENT — adjudicator isolated from compiler/source-selection context.
TRAINING-INDEPENDENT — credible evidence source/outcome was unavailable to the evaluated model's training/development path.

SEQUENCE-HELD-OUT + IDENTITY-MASKED != TRAINING-INDEPENDENT.

## 13. Prior-art pressure
Modern LLM evaluation already distinguishes verbatim contamination, paraphrased overlap, derived/synthetic contamination, rephrasing tests, rotating/private evaluations and date-based splits.

MQR claims no novelty for contamination detection.

MQR-specific use is constitutional: contamination state limits the authority of an AI-mediated scientific adjudication.

## 14. World-contact vs evaluator blindness
Physical engineering evidence and evaluator cleanliness are separate dimensions.

A wind-tunnel measurement can be excellent world-contact even if the AI already knows its answer.

WORLD-CONTACT QUALITY != EVALUATOR-BLINDNESS QUALITY.

If the goal is historical theory assessment, known physical evidence remains valuable.
If the goal is prospective evaluator discrimination, memory leakage is decisive.

## 15. Generation-IV metadata consequence
AI-mediated authority objects should record inside evidence state Et:
- world-contact provenance;
- evaluation-separation status.

This is typed metadata, not a new constitutional field.

Example:
World contact = external physical wind tunnel.
Evaluation separation = SEQUENCE-HELD-OUT / NOT TRAINING-INDEPENDENT.

## 16. Current result
MQR-4.8 does NOT establish that masking defeats memory leakage.

It establishes the boundary:
PROMPT-LEVEL MASKING ALONE CANNOT CERTIFY EVALUATOR INDEPENDENCE.

Tool-sequence blindness remains useful but weaker.

Strong prospective realist promotion requires isolated adjudication plus anti-recognition checks, post-cutoff/sealed evidence, or genuinely new measurement after freeze.

## 17. Next executable discriminator
Preferred successor design:
1. select newly generated or post-cutoff engineering evidence;
2. compiler freezes a masked baseline packet before outcome access;
3. separate adjudicator generates rival predictions;
4. recognition probe and perturbation invariance are run;
5. outcome is revealed only after immutable receipt;
6. authority update reports world-contact and evaluator-separation status separately.

If this cannot be done, do not simulate full blindness.

## 18. Verdict
PASS-EVALUATOR-LEAKAGE-ATTACK / IDENTITY-MASKING-NOT-SUFFICIENT / DIRECT-DOMAIN-MECHANISM-LATENT-MEMORY-LEAKAGE-TYPED / PRE-OUTCOME-RECOGNITION-PROBE-CONSTITUTED / PARAPHRASE-VARIABLE-RENAME-INVARIANCE-GATE / COMPILER-ADJUDICATOR-SCORER-SEPARATION-REQUIRED / PUBLIC-SOURCE-TRAINING-INDEPENDENCE-CEILING / MQR-4.7-RETAINED-AS-SEQUENCE-HELD-OUT-NOT-MEMORY-INDEPENDENT / FOUR-BLINDNESS-LABELS-FROZEN / WORLD-CONTACT-QUALITY-SEPARATED-FROM-EVALUATOR-BLINDNESS / PROMPT-MASKING-ALONE-CANNOT-CERTIFY-INDEPENDENCE / GENERATION-IV-CONTINUES.