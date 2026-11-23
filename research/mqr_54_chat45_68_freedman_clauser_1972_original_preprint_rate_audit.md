# MQR 5.4 · Chat45 R68 — Original January 1972 Freedman–Clauser preprint, exact rate contrasts and measurement bridge

**2026-11-23 KST | 5.4 OPEN | PRIMARY ORIGINAL PREPRINT FULL TEXT READ.** University of California eScholarship [LBL-392](https://escholarship.org/content/qt5qs9830k/qt5qs9830k_noSplash_f76b31bfeb77e6b12c55f3cbd8f6de86.pdf), titled *Experimental Test of Local Hidden-Variable Theories*, by Stuart J. Freedman & John F. Clauser, **January 1972**. This is the institutional author manuscript/preprint; it is NOT asserted to be a word-for-word certified published PRL issue facsimile. Later published PRL 28:938 on **3 April 1972**, DOI [10.1103/PhysRevLett.28.938](https://doi.org/10.1103/PhysRevLett.28.938). The preprint is openly retrievable and was inspected directly through available text; web PDF screenshot attempted but source cache refused the image request. No standalone PDF custody or Drive import verified.

## Primary evidence / engineering chain (not mere hindsight)

1. 1969 [CHSH original proposal](mqr_54_chat45_67_chsh1969_primary_math_measurement_feasible_design_bridge.md) explicitly establishes a testable inequality for realistic polarization measurements and criticizes the preceding Kocher–Commins settings 0° and 90°.
2. 1972 LBL-392 pp. 2–3 specifies rotatable **and removable** polarizers on two optical arms and names the observable rates R(φ), R1 (one polarizer removed), R2 (the other removed), and R0 (both removed).
3. On preprint p. 4, authors state separate assumptions: (i) photons as separate localized particles, (ii) each local polarizer selects transmission without reference to distant polarizer orientation, plus (iii) an additional **detection-probability assumption**, independent of whether photon passed through a polarizer. Do **not** identify this with full detector-loophole closure.
4. On p. 5, they describe **ten inclined glass plates** near Brewster's angle in each pile-of-plates polarizer, a rotation mechanism at **22.5° increments**, polarization transmission efficiencies close to 0.97 and 0.96 (parallel) vs 0.038 and 0.037 (perpendicular), and explicitly removable assemblies. This is an apparatus redesign, independently useful evidence of theory-directed new settings.
5. On pp. 5–6, **100-second acquisition periods**, alternation with both polarizers absent, neighboring R0 normalization, deliberate orientation sequence, accidental coincidence time-offset measurements. These choices defend against source drift and instrument asymmetry. **They are not randomized locality-closing setting switches** and should not be described as such.
6. Endnote 4 (preprint p. 8): the authors explicitly **do not assume** single-polarizer rates R1 and R2 independent of orientation in their data analysis; observed data are consistent with constancy and abbreviated notation is used. Avoid overclaiming that they imposed this constancy as an independent unverified premise in the final analysis.
7. Endnote 11 records the *rounded* ratios: R1/R0=0.497±0.009, R2/R0=0.499±0.009, R(22.5°)/R0=0.400±0.007, R(67.5°)/R0=0.100±0.003.

## Recomputed exact contrasts and limits

Using the four **rounded** source values and Fractions, define D(φ)=[3R(φ)−R(3φ)−R1−R2]/R0 subject to experimental `-1≤D(φ)≤0` under specified premises; assume R(202.5°)=R(22.5°) from periodicity.

- D(22.5°)=3(0.400)−0.100−0.497−0.499=**+0.104**. The article's endnote gives 0.104±0.026.
- D(67.5°)=3(0.100)−0.400−0.497−0.499=**−1.096** using rounded inputs, whereas author preprint reports **−1.097±0.018**, consistent with *original unrounded data* being unavailable in the rounded source excerpt. **Do not silently replace the published original author's figure with recomputed rounded figure or characterize their difference as a scientific disagreement.**
- The reduced diagnostic δ=|0.400−0.100|−0.250=**0.050**. Preprint result δ=**0.050±0.008**.
- If each displayed 0.001-precision rate is rounded to nearest 0.001, δ is constrained to [0.049,0.051] from these two rounded quantities; does not include measurement uncertainty, which is larger.
- The **6.25** value is simply 0.050/0.008 using *authors' reported standard deviation estimate*. It is **not a separately reproduced sampling distribution, p-value, or assumption-free evidence**. Original rate count sequences and covariance with shared R0 are not present in this text.

[Reproduction script](../language/real/experiments/mqr45_r68_freedman_clauser_1972_rounded_rates.py) was *executed locally with Python exact Fraction arithmetic and syntax compilation*, with output: D22=13/125, D67=−137/125, delta=1/20, rounding interval [49/1000,51/1000]; exact local **git hash-object equals remote fetched blob SHA 12e20e8257c26181afa8e29ee32b2ee42b9d4345**. Earlier R61 and R63 exact-script equivalents also compiled and executed with matching remote git-blob SHAs ac553a9ef37ce4a1d2705fef7b82eca3e7a8f295 and 8b5c304ea3c709fb9b7d7b35346cd01a6b470a5a. Thus this time Python execution on code verified **byte-identical** to published Git blob was completed, unlike prior Chat45.

## Strongest explanation, rivals, and honest limit

Historical evidence is much stronger for theory guiding design than simply following a chronological discovery: **the source explicitly cites CHSH and implements an arrangement of the angles and removal/normalization channels proposed in 1969**. This supports practical question generation from mathematics, alongside nontrivial optical engineering and pre-existing lab equipment; it does NOT prove that mathematics alone designed the experiment. A conventional history of Bell/CHSH explains the same sequence, so no claim of special MQR originality is established.

The observed inequality rejection is **conditional** on authors' localization and measurement bridge assumptions. It does not retrospectively close the detection, locality or freedom-of-choice loopholes. R61's globally selected PR-like sample cannot be read back as an implementation of this historical experiment.

**Verdict:** original institutional preprint and specific design changes read; rounded published-summary arithmetic reproduced *exactly*, no raw-count reanalysis. MQR 5.4 OPEN, AUTHORITY TRANSFERRED NONE.
