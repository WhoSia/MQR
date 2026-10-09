# MQR-4.99-P3 — Published Behavioral Availability, Sharp Conditional Bounds & Cross-Protocol Nontransport

**Date:** 2026-10-09. **Stage judgment:** P3 CLOSED BOUNDED — reported aggregate transcription and elementary conditional-set arithmetic verified in Rust/Python; original per-bird behavior events and scientific target calibration HOLD. This court is not a new field or method discovery. This note is **not** an original ecological calibration study, not a proof of a new theorem, and not a test of transfer to Oregon or Alder Flycatcher.

## A. Correct the significance of P2

P2 independently downloaded the **same previously published** 2024 Kéry et al. Oregon/eBird ZIP, checked provider byte identity, compared published/raw counts and mismatched identifiers, and automated this as Python/Rust regression with a Drive backup. These are useful reproducibility and custody checks. No new birds were observed; no original model was fully refit and replicated; no independent availability sensor or new external ecological risk outcome was acquired. GitHub CI success certifies arithmetic and data operations **only**. Avoid phrases suggesting P2 constitutes an ecological discovery or methodological advance.

## B. Prior art and behavioral observations

Diefenbach, Marshall, Mattice & Brauning (2007), *Incorporating availability for detection in estimates of bird abundance*, **The Auk** 124(1), 96–106, DOI: https://doi.org/10.1093/auk/124.1.96 (USGS bibliographic older-form DOI https://doi.org/10.1642/0004-8038(2007)124%5B96:IAFDIE%5D2.0.CO;2). Their **actual field design** banded Henslow's and Grasshopper Sparrows in Pennsylvania, observed specific individuals' singing and visibility during 2002–2003, and recorded timed events in an ACCESS database. They then estimated availability from these behavioral observations, including randomly positioned 5- and 10-minute windows. This is a different observation instrument from detecting unseen birds during an ordinary point count.

**Source limitation:** the paper's Table 1 reports averages, standard errors and nominal 95% confidence intervals. We have the article PDF and its published aggregate table, but **have not obtained or reanalyzed the original bird-by-bird timed ACCESS event records**. All CSV rows under `experiments/mqr-4.99/sources/` are explicitly labeled **hand-transcribed published table values**, never raw ecological samples. An unsuccessful search of publisher/USGS page for downloadable source rows does not prove that the records no longer exist.

Table 1 (published point estimates and reported intervals):

| Bird | Condition | 5 min | 10 min | Monitoring periods |
| --- | --- | --- | --- | ---: |
| Henslow's Sparrow | song only | 0.435 [0.38, 0.53] | 0.501 [0.45, 0.61] | 54 |
| Henslow's Sparrow | song AND visible | 0.391 [0.34, 0.49] | 0.439 [0.38, 0.54] | 54 |
| Grasshopper Sparrow | song only | 0.115 [0.09, 0.14] | 0.211 [0.17, 0.27] | 80 |
| Grasshopper Sparrow | song AND visible | 0.103 [0.08, 0.13] | 0.192 [0.15, 0.25] | 80 |

Line-transect availability reported separately: Henslow 0.442 [0.39,0.54], Grasshopper 0.206 [0.16,0.26], with method-specific approximately 8.8-minute exposure. The interval exposure and detection criterion are part of the type of each number. The paper's Table 1 `n=54` and `n=80` are **monitoring periods**, not 54 and 80 independent birds, and a reported 95% confidence interval is not a known deterministic parameter range.

Derived checks: at the published point values, 10-minute singing-or-visibility event availability is not less than its nested 5-minute event availability; singing AND visible is not more frequent than singing alone. Under an *additional hypothetical constant-rate Poisson singing model*, `a10 = 1-(1-a5)^2`: Henslow song-only 0.435 predicts 0.680775, versus reported 0.501; Grasshopper song-only 0.115 predicts 0.216775, versus reported 0.211. These are descriptive point-value contrasts **without interval covariance or a statistical rejection test**. The paper itself discusses individual singing behavior heterogeneity. Do not apply homogeneous Poisson assumptions to compound song+visible conditions without an additional model.

The literature already describes availability/perception separation. Stanislav et al. (2010), DOI https://doi.org/10.5751/ACE-00372-050103, combines multiple observers and time intervals under robust design. Thus P1's single-time two-observer cancellation does not rule out separately estimating parameters under multi-interval model assumptions; claim domains differ. Amundson et al. (2014), DOI https://doi.org/10.1642/AUK-14-11.1, fits distance/time models with restrictive assumptions. Kéry et al. (2024), DOI https://doi.org/10.1002/ecy.4292, uses common latent abundance/availability, variable durations and two data schemes; none is a license to transport Diefenbach's sparrow availability to American Robin or Alder Flycatcher.

## C. Classical *sharp* conditional set, not a new theory

Define, for **the same individuals, target, event and protocol**, `a=P(A=1)`, `p=P(D=1 | A=1)`, and `q=P(A=1,D=1)=a*p`. Assumptions: no detections when `A=0`, a known **unconditional at-risk denominator** making q a well-defined measured rate, and an externally justifiable true-availability bound `L <= a <= U`.

For `q>0, 0<=L<=U<=1`, feasible parameters exist exactly if `q <= U`. Then `a in [max(L,q),U]`, and the **sharp** set is

`p in [q/U, q/max(L,q)]`.

Attainability is immediate: each p inside this interval admits a=q/p within the permitted availability set; lower endpoint a=U, upper endpoint a=max(L,q). For q=0 and L>0, p=0; if L=0, a=0 allows any p in [0,1]. This uses existing probability algebra; novelty **not claimed**.

**Numerical test, deliberately hypothetical:** `q=0.20` is invented for an ideal same-target known-denominator survey, and **not** measured in Diefenbach, Kéry or the MQR datasets. If one had valid source-target invariance **and** treated the reported Henslow 5-minute singing+visible 95% interval [0.34,0.49] as a true bound, the conditional p range would be [20/49, 10/17] approximately [0.408163,0.588235]. Both endpoints are realized by `(a,p)=(0.49,20/49)` and `(0.34,10/17)`. This is a **scenario**, not an empirical confidence interval for p: nominal 95% intervals, source-target transport, and observed q each require separate justification. No joint coverage claim is implied.

**Without justified source-to-target bridge**, the same hypothetical `q=0.20` only implies `p in [0.20,1]`, with a in [0.20,1]. The Diefenbach interval cannot be imported to robins, 2005 flycatchers, or frogs. Conversely, the count ratio 819/1059 in P2 is **not** q: 819 sums counts of birds rather than a binary detected / known-present individual denominator; 1059 is eBird checklist count, not a known number of individual birds present.

**Mixture caution:** marginalizing heterogeneous birds gives E[a_i*p_i] rather than E[a_i]E[p_i]. A constructed two-group example a=(0.2,0.8), p=(0.8,0.2) gives mean product 0.16 versus product of means 0.25. External *average* behavioral availability alone cannot universally calibrate pooled detection probabilities under unknown covariance.

## D. Admissibility and no-overclaim ruling

- **VERIFIED LOCAL PROGRAM TEST PASS (GitHub Actions #37897402876):** accurate transcription of published Table 1 to a small source-labelled fixture; algebraic set bounds and constructive endpoints; Python/Rust deterministic agreement; 5/10-minute descriptive point checks.
- **HOLD:** bird-level primary behavior sequence (ACCESS database), any measured same-population unconditional q, empirical p separation for American Robins, cross-protocol source-target bridge, any confidence guarantee for p, ecological abundance/risk identification and method novelty.
- **P2 revised:** mechanical byte/source auditing, no scientifically independent replication of availability; refrain from treating multiple languages or CI PASS as more independent ecological evidence.
- **Next empirical exit gate:** matching the marked-bird availability logs to independent contemporaneous perception records or an explicitly documented same-target external calibration with known numerator/denominator and uncertainty. Otherwise retain P3 as a *bounded conceptual/aggregate sensitivity exercise*. Do not automatically advance or close MQR-4.99 scientifically.

## E. Executable receipt (no ecological promotion)

[GitHub Actions P3 arithmetic #37897402876](https://github.com/WhoSia/MQR/actions/runs/37897402876) completed successfully on commit 82eca89a3b006ae8751c33376e1b4f874e5514a7. Rust source check, P1 regression, published fixture inclusion, endpoint constructive witnesses and independent Python arithmetic check all passed. Both implementations read the same **manually transcribed published table**, so they do not constitute independent event-level field replicates. No behavior-event data, target-population known-denominator q, or uncertainty transport was acquired. Reader should not infer model rejection from descriptive Poisson discrepancies.
