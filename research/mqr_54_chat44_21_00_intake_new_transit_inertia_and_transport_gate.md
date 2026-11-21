# MQR 5.4 / MQR44 R21 — Actual 00_INTAKE delta and transit-route behavior as a transport stress case

**2026-11-21 KST** | Real Research OS connected Drive inspection, not a user-requested move of someone else's source and not a new MQR experiment. Official 17 missing-source groups **unchanged**.

## 00_INTAKE actually changed since prior read

Authenticated Google Drive folder [canonical 00_INTAKE](https://drive.google.com/drive/folders/1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16) returned exactly **one visible direct-child PDF** on this inspection:
- Drive file id `18_dp4wTC7zCTkUfUnDwNuzH3Ui4yF_YD`, title `1-s2.0-S0965856425000953-main.pdf`, PDF size **2,646,521 bytes**, file timestamp 2026-11-21T13:59:46Z. The same file was directly fetched via Google Drive text extraction; no hash was newly computed and original bytes not independently downloaded.
- The file is Jacqueline Arriagada, Carlo Prato and Marcela Munizaga (2025), **'Incorporating the inertia effect into a route choice model using fare transaction data from a large-scale public transport network'**, *Transportation Research Part A* **196**, article **104467**, DOI [10.1016/j.tra.2025.104467](https://doi.org/10.1016/j.tra.2025.104467). [Public university source](https://eprints.whiterose.ac.uk/id/eprint/235367/) is consistent with the metadata; author-hosted PDF found [here](https://eprints.whiterose.ac.uk/id/eprint/235367/2/1-s2.0-S0965856425000953-main.pdf).

## Direct source-scoped reading and relevance to MQR

Authors analyse smart-card and vehicle-location data from Santiago's public transit around the launch of **Metro Line 6 on 3 November 2017**. Route-choice inertia/stickiness and frequency-based preferences differ between stable versus changed travel networks, and the effect of change evolves differently for users who adopted the new line vs nonadopters. The authors use an integrated discrete-choice/latent-class approach. This demonstrates a **real empirical design studying regime shifts**, which is useful to contrast with synthetic MQR44 R12, where a fixed source prediction Y_hat=X fails under an analyst-specified shifted distribution. It **does not** imply the Chilean paper's empirical causal inference shares the binary toy mechanism or that its estimated coefficient reversals exactly match R12.

Data availability statement (direct PDF text): **'The authors do not have permission to share data.'** Thus the paper can be directly read and parameters transcribed/checked, but its underlying individual smart-card transaction microdata **cannot be freely obtained or replayed** from this publication. The PDF **is not itself a public individual passenger dataset**. No user/account-level inference or unauthorized data access should be attempted.

**Immediate custody recommendation:** this is a valuable original cross-project transit-behavior paper, but it does not close Behr 2015 raw voltage, Burroughs 2013 transitions, the 2025 Feest complete volume, 1927 Fraenkel edition, or any current MQR 17 exact gaps. Preserve in 00_INTAKE pending Research OS subject/ownership/folder decision; do not silently move to MQR 10_PAPERS. Any possible reuse for the user's ALGO/public-transport project is an intellectual connection, not a transfer of project scope or personal data.

## Precise transfer question

Given one source period before a material transit network modification and a target period after it, separate:
- **stable explanatory feature definition** (route repetition, path choice size, last-chosen route);
- **changed feasible choice set** (new route/line);
- **new population selection** (adopters/nonadopters, repeated cards);
- **changed parameter interpretation** (frequency vs short-term stickiness);
- **different empirical estimand and admissible raw evidence**.

A scientific result may be a previously unaskable route-choice question due to a changed *real* transport system, not just a re-labelled input. Real-Lang should report `SOURCE_RAW_ORIGINAL_MICRODATA = UNAVAILABLE_FROM_PUBLICATION` and `PUBLISHED_MODEL_SUMMARY = DIRECTLY_READ`, never `INDEPENDENT_RAW_REPLAY = PASS`.

## Source and claim boundaries

This note uses original PDF text, verified citation and the publicly linked publication record. It does not verify the complete underlying transaction extraction, latent-class inference, instrumental stability or causal inference. New PDF acquisition=0 (file already in intake). File moves=0; deletion=0; MQR source gap closure=0. No harvest global promotion, version remains 5.4 OPEN.
