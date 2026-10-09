# MQR-4.104 — Independent Adjudication Witnesses, Fallible-Reference Calibration & Verification-Protocol Transport

**FORMAL VERSION OPEN — 2026-10-10. Author-confirmed title.** Flowing Versioning moves the primitive question from known sequential selection probabilities and hypothetical reference error bounds to the **evidence required to certify reference errors and transport that certification under changed protocols**. This is not a declaration that MQR-4.103 or preceding versions have closed.

## Primitive scientific question

When clinical or other measurement labels are fallible, multiple adjudicators may share an unobserved failure lineage. What independent evidence, sampling protocol, and transport assumptions are sufficient to narrow a finite truth-risk identified set, and which claims remain observationally nonidentified despite apparent adjudicator agreement?

The program separates **witness count**, **noncommon error ancestry**, **actual truth access**, **calibration**, and **transport**. A new witness is not independent merely because it has a new name, codebase, institution, or report.

## Inherited source and exact boundary

- MQR-4.101: QTDB 487 selected beat opportunities, 402 complete dual-reader pairs, 76 disagreements, 85 incomplete; **zero independent third-party truth labels**, no externally certified error budgets.
- MQR-4.102: allocation arithmetic for 10 hypothetical adjudications; not actual follow-up reviews or real capacity.
- MQR-4.103: P1 and P2 CLOSED BOUNDED for exact synthetic finite models. P2 3/4 vs 1/4 randomization restores oracle-law identification and design HT unbiasedness but not single-history truth recovery or fallible-reference truth certification. [P2 final court](MQR-4.103-P2-SEQUENTIAL-DESIGN-SUPPORT-AND-FALLIBLE-REFERENCE-COURT.md); [CI #37948743557 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/37948743557), full source and results [archived and verified in Drive](https://drive.google.com/file/d/1cRwlurkKp1u3RDOfJY7gbv6hEBEO5Ej2/view). **4.103 itself remains OPEN** pending original-world validation and sequential transport.
- This 4.104 opening does not claim actual patient risk, novel verification bias theorems, or gold-standard clinical truth.

## P1: first adversarial model — agreement without independent truth

Let one latent bit T be the target. Observe two apparent binary witness labels A,B, but not T. The complete joint observable distribution can equal P(A=B=0)=P(A=B=1)=1/2, P(A != B)=0 under at least these two distinct worlds:

- W0: T is a fair bit and A=B=T (both labels truthful).
- W1: T is a fair bit and A=B=1-T (both labels perfectly wrong through a shared inversion mechanism).

Both yield the **same entire distribution of A,B**, including 100% agreement and marginal 50/50 labels. Yet each adjudicator's error risk P(A != T) is 0 in W0 and 1 in W1. Even arbitrarily many *copies sharing this exact mechanism* preserve the ambiguity. This illustrates nonidentification from common-error ancestry, not universal impossibility of learning from additional independently validated information.

**Important limitation:** these are two synthetic observationally equivalent parameterizations, not observed real QTDB adjudicators. For clinical labels, pathological inversion is an adversarial *logical* stress test, not an evidence-based prevalence claim. A third fully independent, certified-truth observation would change the observation model; a third unverified correlated label need not.

## P1 exact execution plan

1. Enumerate all T in {0,1} and both worlds; compare joint label histograms and truth-reference error numerators.
2. Extend to 1..4 agreement witnesses sharing the same latent failure mechanism. Verify that adding identical copies never changes the observational equivalence class.
3. Construct an actually independent third oracle C=T and show its recorded outcomes distinguish worlds when the assumed certification is legitimate.
4. Attack the oracle assumption by replacing C with a third correlated proxy. Prove via a concrete world pair that the alleged "independent adjudicator" cannot be promoted to certified truth merely by labeling it independent.
5. Separate finite simulated counterexamples, QTDB empirical reader disagreement, and any independently acquired certified reference dataset.
6. Keep protocol transport open: derive counterexamples showing that a certificate warranted under source calibration mechanism need not carry into a target where error dependence changes.

## Scientific success conditions and falsification

- A concrete world pair with equal observed joint witness distributions and different true error risk, plus a transparent invariance argument for added correlated witnesses.
- A *conditional*, assumption-explicit case where an external trusted observation breaks equivalence, and a failure case where a presumed new observer merely repeats a failure lineage.
- Published prior art on latent class diagnostic testing with imperfect references, dependent tests, nonidentifiability, verification bias, and protocol/domain shift. No originality claim based solely on classic counterexamples.
- Actual external original-source acquisition or a recorded **SOURCE CONTACT HOLD**; a GitHub Actions success does not substitute.
- A protocol transport contract defining precisely whose reference error certificate is transferred, from which source population, with what measurement and selection invariance.

## Status ledger

- Formal version: **OPEN**.
- P1: **OPEN** until executable complete enumeration and actual CI.
- SOURCE-CUSTODY / MATHEMATICAL / CI: NOT YET ADJUDICATED for 4.104 at opening.
- REFERENCE-TRUTH / EXTERNAL CALIBRATION / TRANSPORT / NOVELTY: **HOLD** until direct evidence.
- Parent 4.103: **OPEN**; P1/P2 CLOSED BOUNDED in local synthetic scope.
- Notion placement: existing single MQR Labs root, new child formal-version page. No duplicate Labs row.
