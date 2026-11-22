# MQR 5.4 · MQR 44 · R37 — An important correction: Blackwell monotonicity blocks the slogan 'better information can make science worse'

**2026-11-22 KST.** Source priority: existing held literature. **Blackwell (1951) ORIGINAL full text HELD** Drive `1AabK3bac9aNuX5ASeEqkRDRucQSDZ7JB`, directly fetched and read (27,520-character extraction), and **Blackwell (1953) copy HELD but text-extraction unreadable** Drive `1P79HRYkphw4QwomJBfC8tkhLegFyMlHR` (166 characters, JSTOR boilerplate only; no claim to full-text read), with fully verified bibliographic DOI [10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032). Further held Kosenko (2021) `1emJF2yLYRq8bSBuhWobLiDiLctX23LsL` abstract read. Source online corroboration Blackwell (1951) [Berkeley symposium text](https://projecteuclid.org/euclid.bsmsp/1200500222), published 1953 result bibliographically indexed at [Celebratio](https://celebratio.org/Blackwell_DH/article/255/). 5.4 OPEN.

## 1. A serious objection to R35's unqualified anti-monotonicity
R34–R35 properly documented that a laboratory method may improve a chosen technological metric while a useful observation disappears. It would be mathematically incorrect to infer the unconditional proposition 'a signal *more informative in the Blackwell sense* can make the best expected outcome strictly worse for the same decision task'.

Let an experiment `E_new` emit X conditional on state θ, an older experiment `E_old` emit Y. If there exists a *state-independent* random postprocessing kernel K such that `P_old(Y|θ)=sum_X P_new(X|θ) K(Y|X)`, the old experiment is a **garbling** of the new. For every fixed prior p(θ), common action set A, bounded state-dependent reward u(a,θ), no prohibitive resource costs, and decision rules allowed to ignore or garble observations:
  V*(E_new) ≥ V*(E_old).
Proof: given any old policy π(a|Y), simulate old signal Y by K from new X and apply π; the new experiment can attain every value available under old, hence its optimum is no lower.

**The conditional thesis is classical and NOT MQR-original.** General nonmonotonic epistemic access can therefore arise from **noncomparable experiments**, changed underlying state/measurand, changed action/goal, inaccessible raw information, flawed use policy, selection or cost restrictions—not pure Blackwell dominance in an unchanged, freely optimised decision task.

## 2. Two crucial ways to misread the RNA 'improvement'
- The historian's report is about RNA extraction **yield** and radioactivity **signal**. These are different measurements/technical objectives. More isolated RNA mass does *not* establish that the new method's observation channel Blackwell-dominates the old method for the question 'is amino acid radioactivity associated with this RNA?'. A modification can improve yield while destroying a sensitive signal; Blackwell's theorem is not violated.
- A replacement protocol is not equivalent to supplementing an old protocol with a new channel while retaining the option to use either. With the joint new observation (old signal, new auxiliary yield), the old signal remains recoverable by projection; under no costs and same goal, the optimum cannot be worse. **If substitution removes the original observation**, the information structures can be incomparable or reversed.

## 3. Strong prior art and methodological significance
Blackwell's 1951 paper explicitly defined comparison of experiments by attainable risk vectors and provided the sufficient-statistic comparison (while leaving full converse unresolved in that paper); the 1953 paper established equivalent comparisons in broader generality. Avoid anachronistically saying the full 1953 theorem was *already proven in the 1951 paper*.
Kosenko's held 2021 arXiv on algebraic Blackwell order is later prior art; MQR's problem of experimental interface comparison is no fresh invention of garbling orders.

## 4. Precisely bounded research thesis
**Claim (source-relative):** better performance *on one laboratory metric* need not imply a more informative experiment *for another target scientific question*. This is consistent with Blackwell dominance, and its meaningful scientific challenge is specifying target state, feasible operations, observation readout, costs, and which old signals were lost or preserved.

This corrects R35. Statements that 'more informative evidence harms an optimal Bayesian investigator with the same goal and unrestricted actions' are REJECTED; historical anti-monotonicity is a different mechanism.
