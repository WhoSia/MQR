# MQR 5.4 · MQR 44 · R23 — Newly located author-hosted primary supplementary archives for joint X-ray/NMR refinement

**Date:** 2026-11-21 KST. **Status:** source-discovery verified using original PMC/IUCr article; raw-file retrieval and inventory **HOLD**. MQR 5.4 OPEN.

## Newly discovered source-specific items

Rinaldelli, Ravera, Calderone, Parigi, Murshudov & Luchinat (2014), *Acta Crystallographica D* **70:958–967**, DOI [10.1107/S1399004713034160](https://doi.org/10.1107/S1399004713034160), original [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4306559/) and [IUCr journal original](https://journals.iucr.org/d/issues/2014/04/00/dz5299/index.html), explicitly cite **Supplementary Material**:

- [dz5299sup1.doc — Instructions for NMR plus X-ray refinement](https://doi.org/10.1107/S1399004713034160/dz5299sup1.doc), publisher/PMC identifies DOC ~27KB. PMC attachment location `https://pmc.ncbi.nlm.nih.gov/articles/instance/4306559/bin/d-70-00958-sup1.doc`.
- [dz5299sup2.zip — protocols, coordinate files with NMR/X-ray data and refined coordinates](https://doi.org/10.1107/S1399004713034160/dz5299sup2.zip), publisher/PMC labels ZIP ~10.8MB. PMC attachment location `https://pmc.ncbi.nlm.nih.gov/articles/instance/4306559/bin/d-70-00958-sup2.zip`. **This is an actual published candidate archive for reproducibility, not yet an inspected raw waveform/structure-factor cache.**

The original paper's wording is narrower than the statement that this ZIP necessarily contains everything required to replay every experimental condition: the archive claims coordinate files, protocols and NMR/X-ray-related materials. Do not assert it includes measured raw NMR RDC/PCS lists, original diffraction intensity data, R-free flags, complete metadata, every source family or a working REFMAC5 binary until after listing and inspection.

## Attempted acquisition and failed states

1. Web original-page inspection: DOI links and PMC attachment paths verified with primary article text.
2. Following the PMC ZIP/DOC attachments via web yielded **cache miss**, not attached bytes.
3. Container HTTPS download from both PMC attachment and IUCr supplement routes yielded **DNS resolution errors**. No successful HTTP 200 content or ZIP signature, no acquired binary, no SHA-256 hash, no member listing, no source-specific Drive file ID, no decomposition into manifest.
4. Connected Drive targeted title/filename search for Rinaldelli, dz5299sup2, 1IGD, 1EXR returned no exact match in checked results; this is **scope-limited search nonconfirmation, not global nonexistence**.

**Precise status:** `PUBLISHER_SUPPLEMENT_LOCATED`, `BINARIES_NOT_RETRIEVED`, `CONTENTS_NOT_INSPECTED`, `RAW_REFINEMENT_NOT_REPLAYED`. The finding is a genuine improvement to source location but not achieved custody.

## Exact next source test after bytes become accessible

Before calculating physical cross-world conclusions: acquire both files as immutable bytes from official DOI or PMC, record byte length/hash and archive member listing, refuse path traversal on ZIP extraction, classify CIF reflection structure factors vs modeled coordinates vs NMR RDC/PCS restraint lists vs free-R flags vs executable control scripts. Assign specimen/regime IDs separately for `1EXR` and `1IGD`. Then check actual REFMAC5 version and published restraints. Distinguish (a) original experiment data, (b) processed auxiliary data, (c) refined coordinate outputs, (d) documentation. A paper-cited archive is not an independent external replication.

**No incoming Drive source or official 17 missing-source groups closed.** The supplements are additional project-specific acquisition targets. No new Real-Lang authoritative release or global Harvest promotion.
