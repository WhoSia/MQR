# MQR-5.3 R2 — Claim-relative calibration

Date 2026-10-31. Literature: Tal (2017), Calibration: Modelling the Measurement Process; Chang (2004), Inventing Temperature. Tal argues calibration uses model construction and predictive tests, with standards useful but not necessary.

For R=a*x+b+noise, reparameterize x'=c*x+d, a'=a/c, b'=b-a*d/c (c>0). Observed R is unchanged. Absolute latent quantities remain unidentified. A target estimand invariant on observational equivalence classes can escape this particular ambiguity, but not necessarily all other ambiguities.

Three instruments R_i=x+2+noise_i may agree while sharing unverified +2 bias. Agreement is not proof of accuracy.

Historical interpretation: Galison's 1974 detector record selection and beam scans, and Rheinberger's biochemical fraction reconstruction and hydroxylamine assays, require distinct validation. Binary calibration examples from earlier MQR-5.3 are synthetic and not historical parameter estimates.

Next: formalize claim-indexed identification, test shared-source bias, distinguish referent stabilization from statistical calibration.
