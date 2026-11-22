# MQR 5.4 · Chat45 R61 — Continuous postselection strength: a counterfeit CHSH violation

**2026-11-23 KST. Mathematical toy model only. MQR 5.4 OPEN. No experimental quantum evidence.**

## Exact construction

Take all 16 global deterministic local assignments (a0,a1,b0,b1) in {−1,+1}^4 equally often. Four measurement contexts (x,y) are chosen. The *unfiltered* correlations are all zero, giving CHSH S=0.

Introduce a **joint postselection rule** based on BOTH stations' setting/outcome data. It accepts a record with relative weight 1 if the chosen outcomes obey ab=(−1)^(xy), and with relative weight rho ∈[0,1] otherwise. The conditioned joint distribution is

P_rho(a,b | x,y,selected) = [w_rho(a,b,x,y)] / [2(1+rho)],

where w_rho is 1 for target-parity and rho otherwise. Because the four unfiltered outcome pairs were each 1/4, this is an exact conditional distribution. The marginal at either station remains 1/2 at both settings. The contextwise selection rate is (1+rho)/2.

The four correlations are E_xy=(-1)^(xy)*(1−rho)/(1+rho), hence

S(rho)=4(1−rho)/(1+rho).

A **spurious Bell violation S>2** occurs iff rho<1/3. At rho=1/3 S=2; with rho=0 S=4, and rho=1 restores the unfiltered S=0. This construction is not a local independent loss rule and is not claimed to be a physical detection-loophole model. Its point is solely the inference danger of retrospective outcomes-and-settings-dependent inclusion.

| rho | fraction accepted per setting | S |
|---|---|---|
| 0 | 1/2 | 4 |
| 1/10 | 11/20 | 36/11 |
| 1/4 | 5/8 | 12/5 |
| 1/3 | 2/3 | 2 |
| 1/2 | 3/4 | 4/3 |
| 1 | 1 | 0 |

**Independent checks performed this turn:** exact-rational Python calculation of six case scores and acceptance probabilities; independent JS full enumeration of 65,535 nonempty subsets of the 16 deterministic assignment models and verification of the local |S|≤2 bound in every case; an independent six-case threshold consistency calculation. A new Python source file is committed at [R61 exact-code](../language/real/experiments/mqr45_r61_postselection_threshold.py); full execution of that exact committed Python file is **NOT VERIFIED** in this session (public GitHub raw file unavailable to the container), so do not misstate code CI/PASS. The independent mathematical calculations DID pass.

## What this falsifies—and what it does not

- Falsifies naive statement: "All four measurement-context tables are individually valid and non-signalling, so the physical system must be nonlocal." Each accepted context can agree on its marginals while selected data are not an admissible unbiased sample of one prespecified Bell model.
- Does not falsify Bell's theorem. The conventional Bell premises constrain probabilities **before** outcome-dependent global postselection or demand justified inclusion assumptions.
- Does not reproduce an actual local-detector exploit. No physical implementation, independence of remote choices, photon detection efficiency model, raw timestamp model, experimental data, or sample calibration is provided. Don't extrapolate the 1/3 mathematical threshold to detector-efficiency requirements in actual experiments.
- The strongest existing alternative explanations are well-studied Bell detection/coincidence loopholes and fair-sampling methodology. Sources: [Stanford Encyclopedia Bell's theorem](https://plato.stanford.edu/entries/bell-theorem/); [Larsson 2014 loophole review](https://doi.org/10.1088/1751-8113/47/42/424003). MQR does not have priority for these ideas.

## New MQR question raised

A mathematical inequality provides a testable cross-context discriminator only relative to a **specified admissible empirical protocol**. Changing which outputs count as data can transform an apparently contradictory observation pattern without changing underlying local assignments. This deepens the MQR Q5 (mathematical expressibility) versus Q7 (actual experimental question generation) distinction, but remains derivative of existing work.

**R61: SYNTHETIC EXACT / NO ORIGINAL PHYSICS / AUTHORITY TRANSFERRED NONE.**