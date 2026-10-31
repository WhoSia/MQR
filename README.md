# MQR — Methods of Quantitative Realism

**Current phase: 5.3 — Evidence-Lineage Transport, Calibration and Causal Abstraction**

MQR investigates how scientific and mathematical knowledge becomes possible, what limits its authority, and how inquiry can generate new concepts, observables, explanations, and questions. Its ambition is not a narrow history of particular discoveries or an ever-growing taxonomy of audit gates. It asks how fallible contact with a world can support scientific understanding and how inquiry can advance when its original problem representation is inadequate.

The historical trajectory runs from measurement and observational equivalence (0.X), through scientific individuality and cross-domain lawhood (1.X), evidence transport and prospective validation (3.X), fallible reference standards and physical identifiability (4.X), to sustained philosophical and historical inquiry (5.0–5.1). This is a *selective thematic reconstruction*, not a certification that every intervening version or result has been revalidated.


## MQR-5.3 — Evidence-Lineage Transport (2026-10-31)

**Formal active research version:** [MQR-5.3 Notion master](https://app.notion.com/p/40aef561cf928165977af8e05ffc1b4f) and [Google Drive research manuscript](https://docs.google.com/document/d/1rSArpBZ9GvYLkJrI5j3oEu6o-cdGobpi0xzmVj7SiH8/edit). Follows [MQR-5.2](https://app.notion.com/p/409ef561cf9281e99712d11eeaf5e98b). Historical analysis compares Galison's 1974 detector records and Rheinberger's 1952–55 fraction/assay studies without treating historical numbers as synthetic-model parameters.

**Real Lang development, not promoted syntax:** [calibration experiment and tests](language/real/experiments/MQR53-CALIBRATION-README.md). The binary calibration boundary q=f+(1-f-n)b exposes nonidentification if false-positive and false-negative rates are unknown. Separate independent error intervals [0.08,0.12] imply b in [0.375,0.425] when q=0.42; the symmetric-error restriction f=n yields narrower bounds. Finite-sample Hoeffding bounds require iid testing and known calibration rates.

**Method and limitations:** Reuses prior causal transport/abstraction results (Pearl–Bareinboim; Rubenstein et al.; Rischel–Weichwald), does not assert novelty of established algebra. Real Lang analysis is a Python prototype, not a Rust compiler release. Historical figure digitization, calibration covariance, original run files, external prediction tests and CI receipt remain unverified. GitHub Actions must remain read-only; commits are made through the author-controlled repository interface.

---

## Working questions

1. **World and representation.** When do different scientific representations describe the same physical constraints, and when does observational equivalence conceal distinct causal implementations? Translation may exist without being discoverable.
2. **Discovery beyond a given hypothesis space.** How can an investigator identify that a fixed collection of variables, observables, or mechanisms is inadequate, and rationally propose a new problem representation?
3. **Pursuit versus acceptance.** How should one distinguish a novel hypothesis or useful experiment worth pursuing from a claim already supported by independent evidence? A proposal's originality is not its confirmation.
4. **Measurement and intervention.** When does a change of observable reveal physical distinctions inaccessible to the previous measurement interface, and what new calibration or disturbance assumptions does that change introduce?
5. **Mathematics, scientific traditions, and conceptual change.** Compare mathematical practice, theory choice, conceptual invention, historical transmission, and scientific progress without assuming a single inevitable trajectory.

## Current case study — observables are not a fixed gift

**Constructed mathematical example (not physical data):** Two idealized intensity profiles,

- `H1: I1(t) = 2 exp(-2t)`
- `H2: I2(t) = 0.5 exp(-t/2)`

have the same integrated intensity `N = integral_0^infinity I(t) dt = 1`. A measurement interface reporting only `N` cannot discriminate them, regardless of precision. If time-resolved measurements are permitted, the observable `F(tau) = integral_0^tau I(t) dt / N` yields `F1(1) = 1 - exp(-2) ≈ 0.864665` and `F2(1) = 1 - exp(-0.5) ≈ 0.393469`. The difference is approximately `0.471196`.

**What follows:** This proves observational equivalence *relative to an explicitly restricted measurement interface* and its removal after expanding that interface. It does **not** prove that MQR invented a novel discovery method, that time-resolved measurement is unavailable to established methods, or that proposing a new observable automatically constitutes a conceptual revolution.

**Open research question:** When the scientist does not already entertain the new observable, how can a change in what is measured become a reasoned, testable research proposal? Which aspects of the proposal's generation, choice of experiment, calibration, and eventual empirical confirmation are independently supported?

## Adversarial comparison

Compare at least four genuine competitors rather than inventing new MQR terminology in advance:

- Fixed-hypothesis Bayesian or optimal experimental design, including model-checking controls.
- Robust/misspecified-model experimental design.
- Causal discovery, latent-variable and system-identification methods, including interventions.
- Computational scientific discovery and model-based concept formation (including Nersessian), allowing structural and observational-language change.

Evaluate **separately** (i) whether a useful new problem/observable is proposed, (ii) discriminatory power of a prospective intervention, (iii) evidential support independent of proposal construction, and (iv) transport to new regimes. Do not turn these endpoints into an unjustified universal scalar score. Preserve negative cases in which existing methods suffice or MQR's proposed distinction collapses.

**Historical test bed:** Mendel (1866), de Vries, Correns, and Tschermak (1900) are retained as an adversarial historical case, not the final subject of MQR. Claims about priority, sources, author-corrected copies and original tables remain conditional on actual source collation. Narrative similarity is not independent scientific confirmation.

## Research practice and epistemic status

- **Original sources before interpretation.** Separate exact document claims, later translations, competing historiography, and present-day analytical reconstruction.
- **Conjecture is not a theorem.** Distinguish formal consequences of stated models, synthetic experiments, historical interpretation, and reproduced physical evidence.
- **Hypothesis-space enlargement is not automatically conceptual invention.** A new polynomial term, a newly measured variable, and a change in the scientific question can have different implications; test the difference rather than stipulate it.
- **Strong prior art is an asset and an adversary.** Read Kuhn, Fleck, Nickles, Nersessian and modern causal/experimental-design literature against concrete claims. Do not claim novelty by relabeling known concepts.
- **Failures should teach.** Separate data used to generate or repair a hypothesis from genuinely independent evidence of its successor. Keep earlier MQR results as historical records unless their mathematical and empirical claims are specifically reverified.
- **Research OS custody.** Notion stores canonical research meaning; Drive stores preserved source bytes and historical exports. Review provenance, versions, duplicate status and access restrictions before filing. No raw source deletion or unsafe authentication bypass.
- **No progress theater.** More courts, checklists or documents are not evidence of greater scientific understanding. Publication remains an optional output, not a prerequisite.

## Canonical workspace

- [MQR 5.0 research notebook](https://app.notion.com/p/400ef561cf9281f9bba6cfc7cfbe7686)
- [MQR 5.0 retrospective inquiry](https://app.notion.com/p/401ef561cf9281f883a5fd1861ab348d)
- [Research OS chat archive protocol](https://docs.google.com/document/d/1gqzYreWnyFvel5dxBDYZAGa2zSDCwj5Pjzsvh8b-kG0/edit)
- [MQR Drive — retired-code and branch archive](https://drive.google.com/drive/folders/1t38uCfyYGH2qKo9HPqA-ufA0qKnf3oqg)
- [Verbatim earlier README — HEAD 73991906](https://docs.google.com/document/d/1Pcd0uKBncfxCJW84n5l8bRTbKz1ReI_KExmFem1Q1mg/edit)
- [Historical Git tree/path/SHA inventory — HEAD 73991906](https://docs.google.com/document/d/1GY2iX-213sKZlAtqYVjMhxa_LvFq7QzGHG5qUGPDzro/edit)

## Repository and authorship boundary

The README describes current research; legacy code, workflows and historical artifacts are not automatically active 5.1 projects. Retirement requires a byte-complete Drive archive and restoration check before human-authored deletion. GitHub Actions must remain read-only and never commit as `github-actions[bot]`.

**Status:** Active research question and constructed counterexample; independent conceptual-generation advantage and physical validation **not yet established**. No new universal theorem or finalized manuscript asserted.
