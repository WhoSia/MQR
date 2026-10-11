# MQR-4.112 P1-L — Measurement-Representation Science & 4.113 Title Proposal

**Status 2026-10-11:** MQR-4.112 OPEN. **MQR-4.113 TITLE PROPOSED, NOT OPENED OR APPROVED**. Real Lang 0.43 is an unpromoted executable candidate.

## Scientific return

MQR-4.112 asks whether a source-indexed physical measurement history licenses retroactive claims about chronology. While the complete author FER1/FER3 data remain unavailable, a new scientific uncertainty is testable: **which claims about a physical measurement survive changes in numerical representation, processing, calibration ancestry and experimental operations?** Merely counting code commits or formal theorems does not answer that.

## Executed evidence (all bounded)

[Real Lang 0.43 specification](../language/real/V43-REPRESENTATION-BOUNDARY-CANDIDATE.md); [native CI #38137710993 SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38137710993), tested source HEAD `b9ab5fd2574a78653072db518571ffa648b70a2b`. **22 Rust tests**, all legacy Real-Language binaries built, seven physical/methodological finite countermodels, Python exhaustive **19,683** three-history deterministic source/garbling/target triples. Among 4,860 source-identifiable cases with strict finite information loss, 1,512 retained the chosen target and 3,348 lost it. These are enumeration counts, not empirical frequencies. [Native artifact #11701762003](https://github.com/WhoSia/MQR/actions/runs/38137710993/artifacts/11701762003) SHA256 `df4f0616a378d848d00057cee1d0ebc083ae3e05665351f2137821afefbc55bd`.

**Direct actual source:** Re-used original 2021 Guérin public FER1+FER3 98 physical-grain-key ↔ old-source/JAGS ↔ modern-BayLum row correspondence, SHA-pinned to prior [P1-J source CI](https://github.com/WhoSia/MQR/actions/runs/38132359197): FER1 modern row displacement 21/49, FER3 49/49, full public grain key bijection PASS independently in Rust/Python. This confirms representation permutation, **not** recovery of missing source grains or their age impact. The prior P1-J witness, not the reduced CSV alone, attests response-value matching. All `world_authority` and exact whole-cohort causal-age claims remain HOLD.

## The structural distinction

For a finite declared history set `H`, source observable `O`, deterministic processing `g`, and historical target `Q`, `Q` factoring through `g∘O` implies it factors through `O`; a target can survive noninjective loss even though some other targets do not. This classical statement is not a new theorem, and **does not establish stochastic Blackwell/Le Cam comparison or empirical operation equivalence**. The compiler tests typed Gy/mGy conversions, numeric noncommutativity, target-relative lossy translations and nominal operation ancestry; it never infers the reality of an operation from its name.

**Primary-source collision:** [Blackwell 1951 original](https://drive.google.com/file/d/1AabK3bac9aNuX5ASeEqkRDRucQSDZ7JB/view), [Blackwell 1953 DOI](https://doi.org/10.1214/aoms/1177729032), [Torgersen 1991 original book](https://drive.google.com/file/d/112DN9KJ-JdKpRhLIbIDeusmejZ99msAX/view), [Vessonen 2021](https://drive.google.com/file/d/1jkafhd23yHYGUZYzXZtd32Pmy76fcTLu/view), [Tal 2017](https://drive.google.com/file/d/1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2/view) and [van Fraassen 2012](https://drive.google.com/file/d/1hP92t9SNeHh-gI6IIDA_o0m8cK_69xGr/view). Therefore neither deterministic information monotonicity nor representation minimalism is MQR-original. Blackwell 1953 Drive PDF has an unhelpful extracted text layer; 1951 original and Torgersen book were substantively accessible. [Mayne 2026](https://drive.google.com/file/d/1IaYIYMToo6uxxhzr3WMFEd5p8U4Zb7-J/view) additionally preempts claiming domain-local realism as MQR's new idea.

## Proposed next exact formal name

**MQR-4.113 — Representation-Invariant Realist Warrant & the Limits of Measurement Equivalence: Operational Grounding, Blackwell–Le Cam Information Orders, Calibration-Path Noncommutativity & Source-Indexed Rival Falsification**

Interpretation if user approves opening later: move from specific original historical source retrodiction to the **physical-world boundary of measurement representation and evidential warrant**. The Blackwell–Le Cam stochastic experiment lane is **future research**, not implemented by the 0.43 finite checker. Calibration-path commutativity in the real physical world is also **untested**. Require a genuine physically witnessed operation/quantity pair and rivals capable of overturning a structural certificate before asserting original philosophical or empirical discovery. **MQR-4.113 NOT OPENED.**
