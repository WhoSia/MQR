# MQR-4.100 — P5 Internal Source-Authentication and Independent Video-Reference Audit

**Official MQR-4.100 title unchanged.** This is an internal P stage, not an independently named research project.

## EDI authenticated access status

EDI's official notices state that sign-in was required for data-package summaries from 2026-04-24, and that authentication is required for its REST API from 2026-07-30. Supported sign-in providers include Google, Microsoft, GitHub and ORCID. This policy explains the present login-screen/HTTP-403 retrieval results, but does not prove these specific data objects are otherwise restricted.

Sources:
- https://www.edirepository.org/news/news-20260727.00
- https://web-x.edirepository.org/news/news-20260424.00
- https://web-x.edirepository.org/resources/accessing-data
- https://auth.edirepository.org/auth/ui/signin

Exact version targets for a human to download through the ordinary authenticated EDI portal, from The R Journal 2022:
1. Adelie, knb-lter-pal.219.5: https://portal.edirepository.org/nis/mapbrowse?packageid=knb-lter-pal.219.5
2. Gentoo, knb-lter-pal.220.5: https://portal.edirepository.org/nis/mapbrowse?packageid=knb-lter-pal.220.5
3. Chinstrap, knb-lter-pal.221.6: https://portal.edirepository.org/nis/mapbrowse?packageid=knb-lter-pal.221.6

The EDI help instructs Data Portal landing page → Resources → Download Data, or Download Zip Archive for the whole versioned package. Human task: sign in on the official site and download exact three versioned files/archives; upload files to Research OS 00_INTAKE or the conversation. **Do not send passwords, EDI access keys, token strings or session cookies.** A stored research PDF, third-party mirror or older 219.3/220.3/221.2 file is NOT proof of original versioned source-byte identity. The first-party row-level 344-row EDI-to-palmerpenguins comparison is still HOLD; existing p4_edi_reconcile.py is a provisional comparison gate, not an executed receipt.

## Stronger independent reference modality: Clemson pedometer recordings

Clemson Pedometer Evaluation Project: https://cecas.clemson.edu/~ahoover/pedometer/
Publisher source: https://cecas.clemson.edu/tracking/Pedometer/Data.zip
Different publisher source files:
- Data.zip ~31 MB: 30 anonymized participants × three locomotion regimes × two paired files (sensor and video-based steps.txt), 90 source pairs, synchronized 15 Hz from wrist, hip, ankle accelerometers (9 columns).
- RawData.zip ~277 MB: initially slightly asynchronous raw multi-IMU accelerometer/gyroscope/magnetometer files.
- Videos.zip ~11 GB: original videos; not obtained or independently relabelled.

Preliminary downloaded Data.zip (31,661,301 bytes; SHA-256 ce37832d5e234f6f014193a3a2af2f3162ab90905f303d473849512d690885da) was extracted in an external exploratory environment that lacked a trusted TLS certificate chain; that instance did not authenticate publisher delivery. The current GitHub Actions workflow attempts the SAME HTTPS URL using **normal TLS verification** and an exact source SHA-256 pin. If that fails, do NOT silently use an insecure option or claim authenticated download success.

Exploratory 180-file content check:
- 90 nine-axis inertial data text files; 90 manually video-annotated event-index text files.
- 60,801 event entries. Exactly 28,349 right and 28,319 left steps; 2,029 rightshift and 2,104 leftshift. The 4,133 shift events cannot silently be called ordinary steps.
- By condition (event records, sensor sample rows): Regular (31,528, 266,802), SemiRegular (22,215, 260,015), Irregular (7,058, 424,608).
- Two event indices outside the 0-based sensor-sample row interval: P010/Regular, leftshift at 9,233 vs 9,192 rows; P019/Irregular, leftshift at 10,092 vs 9,968 rows. No duplicate event indices within a file in the preliminary scan.
- Thesis describes 60,853 manually marked steps; cause of divergence from this present archive's 60,801 marked left/right/shift entries remains UNKNOWN. Different source editions/annotation semantics plausible, but not established.

**Important epistemic boundary:** three sensors and video annotations are different physical modalities, but the supplied video annotations still share the same original investigators, video-synchronization tools and possible labeling error. The full video source has not been reannotated. No independent gold-standard truth, sensor error distribution, identifiable latent-state experiment or target risk was established.

## Computational and audit gates

Source checksum plus 90-file linkage and event bounds: experiments/mqr-4.100/p5_clemson_audit.py.
Publisher-original TLS and source hash validation: .github/workflows/mqr-4.100-p5-video-annotations.yml.
The current P5 computation should only pass the source/schema receipt when CI succeeds. Regardless of CI result, EDI remains AUTHENTICATION_GATED_ORIGINAL_BYTES_HOLD and scientific identification remains HOLD. No new official title or automatic MQR-4.101.

**User-access handoff:** when normal EDI sign-in works, supply the three version-specific original files, NOT account secrets. If the portal still fails after sign-in, retain the failure page or HTTP status and use the EDI official contact option. No forced bypass.
