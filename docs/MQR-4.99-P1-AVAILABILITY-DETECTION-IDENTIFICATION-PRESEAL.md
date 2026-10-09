# MQR-4.99 — P1 Source-Gated Availability–Detection Identification Contract

**Official PI-approved title (2026-10-09):** MQR-4.99 — Availability–Detection Separation, Zero-Truncated Observation Processes & Cross-Protocol Risk Identifiability.

**Status:** P1 OPEN / MATHEMATICAL SCOPE REPLAY ONLY / NEW INDEPENDENT FIELD DATA PENDING. MQR-4.98 remains CLOSED BOUNDED. Do not publish P1 as a new ecological estimator, biological observation, or novel identifiability theorem.

## Explanandum and scientific decision

MQR-4.98 preserved 98 positive encounter-history rows and 50 original stations in a distinct 2005 Alder Flycatcher protocol, and established a zero-truncated homogeneous interval estimate under restrictive assumptions. It did not expose the number of unrecorded individuals, independently measure song availability, or identify cross-protocol ecological risk.

P1 asks exactly what added measurements *separate* availability A from conditional observer detection D, and when two observations that sound independent still share a latent availability selection gate. New field data must be independently sourced relative to MQR-4.98, with individual matching and denominator provenance explicitly typed.

## A. One-channel indistinguishability

Let A~Bernoulli(a), D|A=1~Bernoulli(p), and Y=A·D with no false positives. With a known at-risk denominator, Pr(Y=1)=q=ap. Thus (a,p)=(0.8,0.5) and (0.5,0.8) give identical Bernoulli observed q=0.4. This is a classical nonidentifiability witness, not an original theorem. An unknown denominator or positive-only collection is strictly weaker.

If an *independent* defensible measurement implies a in [L,U] subset (0,1] and observed unconditional q>0 is established against the identical target denominator, admissible a is [max(q,L),U] (requires U>=max(q,L)), giving **sharp** algebraic p bounds [q/U, q/max(q,L)]. Without compatible joint target/protocol mapping, neither bound is transported. If q=0 and a=0 remains admissible, p can range freely: do not silently divide by zero.

Illustrative constructed values only: q=7/20 and a in [1/2,4/5] yield p in [7/16,7/10]. These are not field estimates.

## B. Shared availability + paired independent observers

Let Y1=A·D1 and Y2=A·D2 for a *single shared availability gate* A with probability a>0. Assume observer-specific Bernoulli detection probabilities p1,p2 are conditionally independent given A=1, observer matching is correct, and no false positives or double counting. Probability of patterns 10,01,11 respectively:
- a p1(1-p2), a (1-p1)p2, a p1 p2.

If only positive patterns survive (00 dropped), their **normalized proportions do not depend on a**. With positive overlap and idealized population probabilities, p1=Pr(11|Y2=1) and p2=Pr(11|Y1=1), while a remains completely unconstrained by the zero-truncated distribution. Do not treat the two observers as two independent *availability* measurements.

Exact constructed witness: p1=3/5, p2=2/5; a=1/2 and a=9/10 both yield the conditional positive pattern distribution (10,01,11) = (9/19,4/19,6/19). This does not establish field independence, matching, or identifiability in finite-sample boundary cases.

If the **true denominator N** is independently observed, and the unconditional share q_any=N_any/N is known against that same denominator, then a=q_any/(p1+p2-p1 p2) is identifiable within this model, provided the expression is valid in [0,1]. Incorrect matching, dependent detections, individual heterogeneity or changing availability break the result.

## C. Cross-protocol ecological risk remains a separate claim

Even if a and p are point-identifiable in each survey, a cross-protocol risk R_s=E_{P_s}[loss] is not warranted absent target-population correspondence, sampling/frame overlap (positivity), measured selection mechanisms, loss-label semantics, and transport assumptions. Do not equate matching a and p with equal populations, occupancies, or predictive losses.

## Independent scholarly ancestors / DOI

1. Nichols et al. (2000), *A double-observer approach for estimating detection probability and abundance from point counts*. https://doi.org/10.1093/auk/117.2.393
2. Diefenbach et al. (2007), *Incorporating availability for detection in estimates of bird abundance*. https://doi.org/10.1093/auk/124.1.96 (USGS also lists historical identifier 10.1642/0004-8038(2007)124[96:IAFDIE]2.0.CO;2). Field behavior was directly monitored in 2002–2003, unlike 4.98's 2005 source.
3. Stanislav et al. (2010), *Separation of Availability and Perception Processes for Aural Detection in Avian Point Counts*. https://doi.org/10.5751/ACE-00372-050103
4. Amundson et al. (2014), *A hierarchical model combining distance sampling and time removal to estimate detection probability during avian point counts*. https://doi.org/10.1642/AUK-14-11.1
5. Kéry et al. (2024), *Integrated distance sampling models for simple point counts*. https://doi.org/10.1002/ecy.4292 . Published data/code Zenodo DOI: https://doi.org/10.5281/zenodo.10666980 . As of P1, raw files **not yet acquired or independently replayed**.

DOI lookup and existing Drive title search were performed; search absence is *not* proof of global nonduplication. A separate intake and source-byte receipt are needed before any canonical paper promotion.

## P1 gates and stop conditions

- **P1 mathematics**: exact rational scope witness + independent Rust unit tests; no ecological inference.
- **P2 empirical entry**: independent original data, DOI/permissions, exact data bytes, data schema, native protocol (observer overlap / behavior / duration / denominators) and source-level checks.
- **P3 estimation**: predeclared identifiable quantities and residual identified sets, train/heldout by actual independent field unit, no source leakage, explicit calibration and baseline comparisons.
- **P4 promotion**: results only when field measurements warrant the numerical biological claim. No automatic continuation to 5.00.
- **Governance**: GitHub MAIN_ONLY; no github-actions[bot] authored commits; Rust primary when creating active compiled tools, other languages used for genuinely independent checks, not cosmetic multiplicity. Retired operations first archived to Drive with matching raw Git blobs before tree deletion.

**Verdict: P1 MATHEMATICAL CONTRACT PASS-IN-PRINCIPLE; empirical and transport authority HOLD pending independent real data and CI.**
