# MQR-4.113 P1 — Exact Stochastic Experimental Comparison & REALCHANNEL 0.44 Candidate

**Status:** MQR-4.113 formally OPEN (user approved full title 2026-10-11), with MQR-4.112 simultaneously OPEN, not closed. Native implementation and formal finite stochastic experiment mathematical results **PASS_BOUNDED**. An empirical operational realist law, evidence that two real instruments measure the same quantity, and original whole FER source remain **HOLD**.

## Research question

Given two experiments on the **same declared latent physical-state index**, when does a stochastic map of one experiment's outputs exactly reproduce the other, and how much worst-state total-variation discrepancy remains if not? Is that statistical order sufficient to transfer any claim that the instruments physically measure the same quantity?

**No:** a stochastic experiment-order relation by itself is about statistical informativeness. Without independent operation–quantity and calibration warrants, even exact Blackwell equivalence can coexist with *declared* different measurands or calibration lineage. Conversely, distinct software coordinates can preserve the same physical source selection, as concretely witnessed earlier in 4.112 P1-J's original 2021 FER 49+49 grain dataset.

## Exact mathematical contract, limitations

Row-stochastic 2×2 rational matrices `A[theta,signal]`, `B[theta,signal]`. Source observation randomized by state-independent `K`, row-stochastic 2×2. The *directional*, not symmetric, deficiency:

`delta(A->B)=min_K max_theta TV((A K)[theta,:], B[theta,:])`.

For binary signals, write `K=[[x,1-x],[y,1-y]]` with `0<=x,y<=1` and auxiliary `t`. Minimize `t` subject to `|A[theta,0]*x+A[theta,1]*y-B[theta,0]|<=t` for both states. This is a bounded three-variable linear program; exact rational `Fraction` arithmetic and **all feasible intersections of three bounding planes** enumerate its vertices, and a linear objective has an optimal vertex. Both directional deficiencies and explicit optimal stochastic `K` matrices are recorded. The symmetric **Le Cam distance** is their maximum. This is **existing** statistical experiment comparison mathematics, not an original MQR theorem.

**Fixed limitations:** binary states, binary output, exact explicitly constructed rational probabilities; no empirical channel inference, no calibration model fitted, no independent real experiment, no n-sample asymptotic deficiency, no uncertainty over the true channel. All abstract fixtures and derived results are deterministic constructed experiments, NOT actual measured instruments.

## Actual native 4.113 P1 results

[Source code](../experiments/mqr-4.113/p1_exact_binary_experiments.py), [read-only native CI #38138948231 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38138948231), executed source `e523b14d25ee98d1993727a4a8ac4a2ece0e3cae`.

| Constructed 2×2 experiment comparison | δ(A→B) | δ(B→A) | mathematical verdict |
|---|---|---|---|
| Perfect binary witness vs symmetric 3/4 reliable noisy witness | 0 | 1/4 | A strictly Blackwell dominates |
| 4/5 vs 3/5 reliable symmetric channels | 0 | 1/5 | A strictly dominates |
| Complementing reported output labels | 0 | 0 | statistical equivalence |
| State-independent 1/2/1/2 signal vs perfect state witness | 1/2 | 0 | B strictly dominates |
| One-sided discrim. experiments `[[1,0],[1/2,1/2]]` vs `[[1/2,1/2],[0,1]]` | 1/6 | 1/6 | **Blackwell-incomparable** |
| Same statistical channel under synthetic declared TEMPERATURE vs DOSE instrument names | 0 | 0 | statistical equality but **declared physical quantity mismatch** |
| Same statistical channel with two differently named synthetic operations and shared unverified calibration ancestor | 0 | 0 | statistical equality, external calibration/operational identity **HOLD** |

Native Python **10 regression tests PASS**, all 7 exact rational LP cases with explicit optimal witness matrices inspected, actual existing v0.42 and v0.43 Real-Language Rust source tests re-run and PASS. [Artifact #11701607909](https://github.com/WhoSia/MQR/actions/runs/38138948231/artifacts/11701607909), SHA256 `dd94d46e03b8614c077a5d762699024a2bb9c914dc652fd722601c65ae497c8f`, downloaded ZIP and verified by `sha256sum`. The first CI succeeded; no empirical law promoted.

## Executable Real-Language channel front end

The new *independent, unpromoted* [`REALCHANNEL 0.44-CANDIDATE` parser](../language/real/real_channel_v44.py) accepts typed 2×2 channel probabilities, quantity and operation names, calibration ancestry declarations, and source reporting status. It uses exactly the P1 rational optimizer. [Three real executable synthetic fixtures](../language/real/fixtures/v44/) model strict dominance, incomparable statistical rivals, and statistically identical but physically different quantity names; the fourth fixture demands rejection of a source-reported claim without a hash pointer. A source hash still **cannot prove** actual empirical lineage. Always emits `measured_physical_equivalence=HOLD`, `empirical_source_warrant=UNVERIFIED_EVEN_WITH_HASH` and `real_language_promotion=UNPROMOTED_CANDIDATE`.

[Real-Language CI #38139129035 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38139129035), executable source `e11175de3c2a9dd475de64ee5ba1b575a22bf1fb`, old Real-Language binary build and v0.42/v0.43 Rust regression PASS, exact-engine tests 10/10 PASS, 3 correct packet verdicts, self-certification rejection PASS. [Artifact #11701674832](https://github.com/WhoSia/MQR/actions/runs/38139129035/artifacts/11701674832), SHA256 `515f05b06744dfad7716956fde52880af2cd5c361f431e012e61b90ec2367c15`, downloaded and byte hash checked.

## Connection to real 4.112 primary data and role of prior art

The source-indexed 2021 Guérin FER1/FER3 tutorial has 49+49 actual measured physical grains; P1-J's source→JAGS witness verified 98/98 source keys and modern row displacement FER1 21/49, FER3 49/49. 4.113 takes that source truth as a **constraint on representation comparisons**, not as an observation of the *whole* original 2015/2021 cohort or evidence of an actual 2×2 detector kernel. Original complete FER BIN/BINX, screening/rejection logs and full-versus-public age impact remain HOLD under both 4.112 and 4.113. Corresponding author request was sent once and only its SENT state was checked earlier; no additional email or inbox monitoring now.

Relevant original literature read in user's Drive: [Blackwell 1951](https://drive.google.com/file/d/1AabK3bac9aNuX5ASeEqkRDRucQSDZ7JB/view), [Torgersen 1991](https://drive.google.com/file/d/112DN9KJ-JdKpRhLIbIDeusmejZ99msAX/view), [Tal 2017](https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view), [Vessonen 2021](https://drive.google.com/file/d/1jkafhd23yHYGUZYzXZtd32Pmy76fcTLu/view), [van Fraassen 2012](https://drive.google.com/file/d/1hP92t9SNeHh-gI6IIDA_o0m8cK_69xGr/view). A current exposition of Le Cam directional TV-deficiency uses the same convention (<https://api.repository.cam.ac.uk/server/api/core/bitstreams/86a25f46-b1d8-495f-bbf7-4ea71b4c597d/content>); this corroborates definition, not priority of mathematical discovery. Neither statistical equality nor identical nominal measured quantity confirms the natural-world correspondence, as Tal and van Fraassen explain.

## P1 judgment and next attacks

**PASS:** exact rational binary-state/binary-signal Blackwell/Le Cam mathematical countermodels, two nonzero reverse deficiencies, bidirectional incomparability, symbolic label permutation equivalence, declared quantity-mismatch firewall, Real-Language typed channel front end, compatibility with v0.42/v0.43, continuity of 4.112. **HOLD:** measured stochastic channel from real physical repeated observations, common-root calibration ancestry independently adjudicated, cross-regime source-indexed operation identity, real full-FER chronology effect, original realist law.

**Next P2 discriminator:** acquire or use an ALREADY OWNED real calibration/measurement experiment that reports known physical units plus repeated observations and apparatus lineage. Compare actual source-data fitted channels and calibration model against a *matched physical quantity under two operational representations*, with nuisance uncertainty and an independent reference check. If no suitable source exists, sharpen counterexamples to the language's operational grounding but do not claim physical equivalence. Real-Language 0.44 remains explicitly a development candidate pending separate semantic, measurement, and prior-art reviews.

**Governance:** MQR-4.113 OPEN is approved; MQR-4.112 OPEN too. One canonical MQR Notion Lab row only, GitHub main-only WhoSia author/committer, no fabricated original author source, no language promotion from green CI.
