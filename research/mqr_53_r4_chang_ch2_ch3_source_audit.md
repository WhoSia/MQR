# MQR-5.3 R4 — Chang chapters 2–3 source audit

Date: 2026-10-31. This is a source-specific research note, not a claim of a new theorem or a full audit of all 9,247 lines of MQR 36.md.

## Source-verified corrections

1. Chang (2004), *Inventing Temperature*, chapter **2** is **Spirit, Air, and Quicksilver** (pp. 57–102), not 'The Vexatious Nature of Temperature'. Chapter **3** is **To Go Beyond** (pp. 103–158).
2. Boerhaave's mercury and alcohol thermometers, graduated at the same fixed points, disagreed; chapter 2 calls attention to *nomic measurement* and the circularity of determining the thermometer law by unknown temperatures.
3. De Luc's mixing method assumes, inter alia, effectively constant water heat capacity; caloric theories contested that assumption. See pp. 60–69.
4. Regnault's comparability is a cross-instrument consistency criterion, not proof that air expands strictly linearly with thermodynamic temperature. Eleven mercury thermometers made from four glasses varied, in the worst cases by over 5 degrees C. See chapter 2, pp. 74–96.
5. Chapter 3's mercury-freezing episode shows that an instrument cannot simply certify a point beyond its dependable working range; early numerical reports differed profoundly (pp. 104–113).
6. Wedgwood's clay pyrometry and the competing platinum/air pyrometers reveal the underdetermination of extensions. Chang specifies **conformity** and **overlap** requirements for metrological extension (pp. 152–155) and discusses **mutual grounding** (from p. 155).
7. Tal (2017), *Calibration: Modelling the Measurement Process*: calibration is predictive measurement-process modeling and testing; standards useful for coherence but not strictly necessary for all calibration. Avoid falsely attributing the MQR equations to Tal or Chang.

## Constructed MQR hypothesis, not historical result

Let actual standard realization S = G(P,U), indication R = K(S,I), and reported observable Z = D(R,C). Claim-relative calibration adequacy should depend on reference realization, instrument response, nuisance contexts, and inferential target. Concordant readings do not rule out shared systematic error, and overlap agreement alone does not guarantee extrapolation validity.

## Audit boundaries / outstanding checks

- MQR 36.md original found in Drive; high-level mathematical lineage checked, not independently reproduced line-by-line.
- No direct edition comparison of each 18th/19th-century historical primary source; Chang is a secondary historical source.
- No new empirical predictive advantage established.
- No missing Chang/Tal source: both present in Google Drive; original historical studies by De Luc, Regnault, Braun, Wedgwood require item-level availability audit before claiming they are absent.
- Main research manuscript appended in Google Drive before this commit. Notion record requires a separate explicit verified write.

Source pointers: Chang Drive ID `1RwuRfY9Ifz6iEAUZZm57z4EzHX8CP0CV`; Tal Drive ID `1P5guGX-EJBfjr0fKigoSyTOghk5q8Ff2`; archive `15T62LwCSxzyioz8jIohE8FNHnfm2oi-B`; master `1rSArpBZ9GvYLkJrI5j3oEu6o-cdGobpi0xzmVj7SiH8`.

Operational rule: no GitHub Actions bot as author/committer, and development commits only after research review.
