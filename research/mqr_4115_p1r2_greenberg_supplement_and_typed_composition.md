# MQR-4.115 P1-R2 — Greenberg Supplement Intake and Typed Proof Obligations

Date 2026-10-14. MQR-4.115 OPEN. The previously unavailable **BMJ supplementary source** for Greenberg (2009), *How Citation Distortions Create Unfounded Authority*, has now been found in user Drive.

Canonical original Drive ID: `1N7iO3C15_dCjANtX0FLxPAWqTKE5NzJN`, renamed `Greenberg (2009) — How Citation Distortions Create Unfounded Authority — BMJ SUPPLEMENTARY NOTES AND TABLES 1–4.pdf`, moved from 00_INTAKE Literature Radar `1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16` to 10_PAPERS Commons `1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP`, Drive update successful. Separate ~5KB `.fdmdownload` incomplete file not promoted, untouched.

Directly inspected extracted source text: supplementary notes 1–17; Table 1 p.47, Table 2 p.73, Table 3 p.79 onward (original statements, mapped citations, 302 numbered entries per table introduction), Table 4 p.116 onward, author-assigned per-paper claim-specific supportive/critical/neutral citations and PMID. Page 116 table explains paper #1 supportive links to 11,83,88,93,94,96 and neutral link to 4. Paper #2 supportive links to 4,21,74,93,94,96,129 and neutral to 121. These are **author-coded observational/citation data**, not independently reproduced truth judgments. Prior paper-level aggregate 242 papers and 675 citations should not be blindly equated to Table 3's 302 indexed records; verify inclusion, claim subset, edge filtering and denominator first. No full table extraction or graph CI claimed in this phase.

## Proof-relevant arrow signatures
Typed objects `Method`, `Operation`, `Observation`, `Document`, `Claim`, `Institution`, `Authority`. Labelled arrows `requires: Method -> Operation`, `reports: Document -> Observation`, `cites: Document -> Document`, `supports: Evidence -> Claim`, `promotes: Authority -> ClaimUptake`, `changes: ClaimUptake -> FutureSampling`.

The **free category** on the typed directed multigraph always admits formal paths (composition), but a path is not a semantic warrant. A separate partial interpretation `J` into an evidence-judgment category must be defined and only available when domain-specific proof obligations hold: `source_authenticity`, `claim_alignment`, `reference_validity`, `defeater_check`, `dependency_provenance`, `scope_preservation`. No functor from *all* free paths to admissible evidential inferences is presumed. A `cite` then `promotes` path may exist but lacks an admissible witness of `supports`.

## Formal challenge
Let `G` be a finite typed directed multigraph, `Free(G)` its path category, and `E` a judgment structure with claim-scoped proof obligations. The relation `Reach_G(x,y)` only checks a path in `Free(G)`. `Warrant_G(x,c)` requires a valid derivation object with admissible evidence constructors; authority and citation edges alone are not constructors. Adding authority edges monotonically expands `Reach` but leaves `Warrant` unchanged **only if** admissibility, evidence source nodes, all defeater state, and knowledge-producing interventions are explicitly held fixed. This is a model-relative invariance, not a claim that authority never causes real evidence.

The first nontrivial target is not reproving this definitional invariance: identify minimal assumptions for an independently checkable **representation-invariant quotient** under operation-node refinement, preserving source roots and valid proof obligations while permitting degree concentration to vary. Test countermodels where a refinement creates hidden shared ancestry or changes claim-level defeater scope.

## Source and provenance guards
Greenberg Table 4 edges carry `SOURCE_REPORTED` citation stance; not independently certified evidence. Distinct citation edges `!=` independent experimental roots. Label `supportive` describes the paper author's coding of how citations were used, not logical entailment or truth. Existing MQR-4.114 SRM 917c source genealogy and same-serum calibration independence remain HOLD. No 4.115 new empirical validation claim.

Next: reproduce and audit a small selected Table 4 row subset from the actual source; then expand with tracked row extraction, duplicate-sensitive and document-version-aware graph counts. Read-only CI; human-only GitHub commits.
