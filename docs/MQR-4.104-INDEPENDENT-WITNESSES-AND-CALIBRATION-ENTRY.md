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

## P1: inherited regression fixture — agreement without independent truth (NOT NOVEL)

Let one latent bit T be the target. Observe two apparent binary witness labels A,B, but not T. The complete joint observable distribution can equal P(A=B=0)=P(A=B=1)=1/2, P(A != B)=0 under at least these two distinct worlds:

- W0: T is a fair bit and A=B=T (both labels truthful).
- W1: T is a fair bit and A=B=1-T (both labels perfectly wrong through a shared inversion mechanism).

Both yield the **same entire distribution of A,B**, including 100% agreement and marginal 50/50 labels. Yet each adjudicator's error risk P(A != T) is 0 in W0 and 1 in W1. Even arbitrarily many *copies sharing this exact mechanism* preserve the ambiguity. This illustrates nonidentification from common-error ancestry, not universal impossibility of learning from additional independently validated information.

**Important limitation:** these are two synthetic observationally equivalent parameterizations, not observed real QTDB adjudicators. For clinical labels, pathological inversion is an adversarial *logical* stress test, not an evidence-based prevalence claim. A third fully independent, certified-truth observation would change the observation model; a third unverified correlated label need not.

## Research genealogy and duplicate-result correction

**This example was incorrectly introduced as a new P1 scientific result.** Prior MQR-3.133 established that marginally admitted witnesses may share calibration drift, preprocessing artifacts or latent common causes. MQR-3.134 distinguished unidentified latent cause from an identified absence of such cause; MQR-3.135 limited dependence robustness to the admitted dependence family. MQR-4.103-P2 already gave exhaustive same-observation/different-truth witnesses under unrestricted reader errors (`T=000,E=000` versus `T=111,E=111` with `A=000`). The W0/W1 correlated-flip construction below is therefore **a minimal regression fixture**, not a discovery, new theorem, or independent scientific advance. It must not be scored as the P1 scientific closure criterion.

**Corrected new intervention target:** given realistically fallible readers and a proposed external calibration protocol, determine which *observable audits or randomized adjudication interventions*, beyond correlated agreement, can partially identify an explicitly chosen error-risk estimand, what bounds they warrant, and which assumptions invalidate transport. A perfectly certified oracle is only a conditional benchmark, not an acquisition strategy. A genuine new claim needs a nontrivial, falsifiable intervention or real independent reference data not inherited from these common-error examples.

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
- P1: **OPEN** for genuinely new calibration/verification intervention and source contact; the correlated-witness code, even if all tests pass, is **REGRESSION ONLY**, not P1 scientific completion.
- SOURCE-CUSTODY / MATHEMATICAL / CI: NOT YET ADJUDICATED for 4.104 at opening.
- REFERENCE-TRUTH / EXTERNAL CALIBRATION / TRANSPORT / NOVELTY: **HOLD** until direct evidence.
- Parent 4.103: **OPEN**; P1/P2 CLOSED BOUNDED in local synthetic scope.
- Notion placement: existing single MQR Labs root, new child formal-version page. No duplicate Labs row.

## Harvest-backed P1 refinement — certificate scope, not renewed independence discovery

**Genealogy collision confirmed:** [MQR-4.76](https://app.notion.com/p/3f1ef561cf92810b9b6bf5a0993e7f25) already handled historically dependent challenge origin, relevant dependency cuts, defeasible upgrade certificates, ancestry-aware split/merge, and cross-domain role-level transport. None are original to 4.104. [Global Harvest FMT](https://app.notion.com/p/3dfef561cf9281deaa23c2c71efa492c) also kills novelty claims about ordinary witness preservation, diagnosability, robust preservation and assurance-case update; its CRF residue remains novelty-unverified. [MQR Harvest backflow contract](https://app.notion.com/p/3d5ef561cf928132a2ecc02734f1b885) denies automatic authority transfer from these fragments. Therefore **P1 conceptual target narrows to operational calibration of fallible adjudicators over named populations, selection policies and times**, not rediscovering generic independence.

A minimal *conditional* calibration bound is worth using as a baseline, not as a theorem of MQR. For loss `L=1{A != T}`, let `R_s=E_s[L]`, `R_t=E_t[L]`. If an independently justified source confidence bound establishes `R_s <= e` and a *separately justified target discrepancy certificate* establishes `|R_t-R_s| <= d` for this **same loss and observation protocol**, then `R_t <= min(1,e+d)`. Without `d`, the target bound is `[0,1]` even if source reference error is exactly zero. A target mechanism can reverse all source labels while preserving all unvalidated apparent label agreement. The inequality is elementary and conditional; neither e nor d is presently certified for the QTDB task. The **research obligation** is to make the discrepancy certificate testable, with protected probability selection, witness provenance, and transport checks, rather than asserting an arbitrary value of d.

In particular, split the future empirical contract into (i) named target loss and denominator, (ii) source truth-reference provenance, (iii) verification inclusion probabilities and selective missingness, (iv) explicit protocol-version identifiers, (v) observable drift sentinels versus truth-linked drift, and (vi) falsifying counterexamples. An observable-label drift sentinel alone can miss coordinated hidden truth drift and **must not** be called a reference-error certificate.

**4.104 remains OPEN / substantive increment = bounded research target and ancestry correction, not empirical calibration achievement.** The next Flowing question changes from *what constitutes an admissible calibration certificate* to *when an existing certificate must be reopened or reacquired under evidence/protocol drift and a finite audit budget*. Proposed 4.105 title is not opened here.
