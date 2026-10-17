# MQR-4.120 P8 — Bidirectional Ordered Matching and the 15-Row Identity Fiber

2026-10-17. SOURCE-TEXT CHECK PASS_BOUNDED. Literal original bytes/checksums NOT verified.

## Observational question and methodology
MIT jtpa.raw (11,204 rows; 19 columns) and Zenodo 18836198 jtpa.csv (9,223 observations; 11 columns) were again fetched in entirety as rendered public text. Match keys were (earnings, randomized Z, training D, sex) = MIT columns (2,3,4,5) and Zenodo (earnings,Z2,D2,sex). Run a greedy earliest *forward* subsequence alignment, and an independent latest *backward* subsequence alignment. Both cover all Zenodo observations in order. If earliest index = latest index for a Zenodo row, its original source position is forced under ordered key-preserving embedding; otherwise row identity is ambiguous. This is a combinatorial property conditional on these two source renderings, their complete relative order and the key mapping, not primary documentary provenance.

## Finite result
- Entire subsequence match: **9,223 / 9,223** in BOTH forward and backward alignments.
- **9,208 Zenodo rows** have identical earliest/latest MIT row positions, hence unique *within the stated ordered-embedding model*.
- **15 Zenodo rows** have different earliest/latest source positions; all 15 have **earnings = 0**. Fourteen have earliest/latest index separation 1, one has separation 2. These are local identity fibers, not proof of individual absence from either dataset.
- The ambiguous Zenodo observation numbers (1-based, excluding header) are: **227, 490, 2155, 2219, 2371, 3829, 4801, 4921, 5811, 6689, 7835, 8325, 8424, 8428, 8726**.
- Earliest-vs-latest candidates carry distinct original MIT first-column IDs (e.g., Zenodo row 227 corresponds to MIT source ID 300489 or 300492; row 6689 to 314917 or 314919).
- Under either matching, there are 1,981 unassigned MIT source rows, but WHICH original IDs were excluded is unresolved for at least those ambiguity fibers. Do not claim a historical deletion list. Group descriptive differences by (earnings,Z,D,sex) remain unchanged by swapping identical-key matches, but distribution of unobserved extra MIT columns among matched/excluded people may change.

## Sharp, conditional interpretation
Within **ordered key-preserving embedding** and given the full rendered source lists, 9,208 positions are fixed by agreement between extremal alignments. Fifteen positions have at least two feasible assignments and cannot be uniquely attributed from these keys. This is a finite combinatorial identification result, not a probabilistic confidence claim. It is not the unconditional identification of original participants: even uniquely aligned observations could have undergone transformations or mismatched historical identifiers, and direct source-byte custody remains HOLD.

## Reconnection to MQR
- Original measurement quotient: many latent identities can be mapped to identical observed keys.
- 4.101: source selection changes target populations; missing observations cannot be declared random without evidence.
- 4.107–4.109: descriptive equivalence of outputs is not evidence-history equivalence, nor calibration/authority custody.
- 4.113: experiment information order is target-relative; distinct records do not themselves establish independent physical warrants.
- 4.119/4.120: a clean matching algorithm (J1-like conditional correctness) cannot certify authority/provenance of row construction (J2-like legitimacy).
- 4.89 Bernoulli causal nonidentification is prior art and is NOT recreated or presented as a novel discovery.

## Next discriminating source
Find Han's CSV generation/row selection code, external IDs or original source-field provenance. Additional candidate MIT covariates might distinguish the 15, but only if meaningfully cross-referenced to Zenodo; matching source-only covariates to nothing would be fake progress. Verify raw MIT and Zenodo file bytes/checksums independently before release-grade provenance statements. Assess whether source-selected sample contains education/density transformations and whether their creation explains the 1,981 missing rows. No design-adjusted ITT/LATE or original QTE replication is claimed.

## Verdict
BIDIRECTIONAL_9223_PASS_BOUNDED; ORDERED_IDENTITY_9208_FORCED_CONDITIONALLY; FIFTEEN_ZERO_EARNINGS_FIBERS_HOLD; EXCLUSION_IDS_HOLD; SELECTION_RULE_HOLD; FILE_BYTE_AND_MD5_HOLD; ORIGINAL_IV_REPLICATION_HOLD; REAL_REMEDY_SCOPE_HOLD. 4.120 ACTIVE / P8. All inherited Greenberg, CCQM, Harvest and 4.119 assessor HOLDs preserved.
