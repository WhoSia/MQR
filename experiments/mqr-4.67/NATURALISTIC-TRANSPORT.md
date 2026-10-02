# MQR-4.67 — Naturalistic Transport Audit

Status: **PARTIAL / PROVENANCE-AXIS SUPPORTED / FULL TYPED-LOSS TRANSPORT OPEN / NOT PROSPECTIVE / NO PROMOTION AUTHORITY**

## Purpose

The synthetic 4.67 machine may not validate itself.

This audit asks only whether any frozen loss coordinate corresponds to a distinction that external scientific practice has independently treated as materially relevant.

It does **not** attempt to fit external cases to the simulator after the fact and then call the simulator validated.

## Evidence discipline

- **OBSERVED** — directly supported by the cited external source.
- **INFERRED** — MQR mapping from the external source to a frozen 4.67 coordinate.
- **OPEN** — not established.

The naturalistic cases were selected after the 4.67 coordinate system was frozen. They are therefore **retrospective transport probes**, not prospective validation.

## Case A — Omics provenance / reproducibility

### Goodman, Fanelli & Ioannidis (2016)

Drive source:
`1bq3QOu9szFksordyxAVRxCo0xOCIqxY0`

**OBSERVED.**
The paper distinguishes methods reproducibility, results reproducibility, and inferential reproducibility and warns against treating reproducibility itself as a surrogate for truth.

**OBSERVED.**
For laboratory and biomedical work, reproducibility can require fine-grained metadata about materials, measurements, analysis code and processing. The paper specifically notes that detecting batch effects may require knowing which samples were tested on which machine, in what order, on what day, together with calibration information; such details are often not reported or retained.

**INFERRED transport.**
This is strong external support for the general proposition that provenance variables may be currently absent from the final result representation yet materially affect later audit/reanalysis authority.

This supports the **PROV** coordinate family qualitatively.

It does not validate:
- the 4.67 P bit;
- the frozen FATAL/MATERIAL/BOUNDED thresholds;
- the AUDIT event semantics;
- the full five-coordinate loss vector.

## Case B — Duke omics / forensic bioinformatics

External source family:
- Baggerly, Coombes & Neeley (2008), *Run batch effects potentially compromise the usefulness of genomic signatures for ovarian cancer*, DOI `10.1200/JCO.2007.15.1951`.
- Baggerly & Coombes (2011), *What information should be required to support clinical "omics" publications?*, DOI `10.1373/clinchem.2010.158618`.
- National Academies, *Evolution of Translational Omics: Lessons Learned and the Path Forward*.

**OBSERVED.**
Independent investigators were unable to reproduce important genomic-test results from the available information, and later reviews documented data/analysis errors and concerns about batch effects in signatures that had entered clinical-trial contexts.

**OBSERVED.**
The National Academies discussion of the case reports Baggerly and Coombes's recommendation that omics publications provide raw data, code, **evidence of the provenance of raw data so labels can be checked**, descriptions of nonscriptable steps, and prespecified analysis plans.

**OBSERVED.**
The same National Academies case history reports that insufficient access to data/code and unclear information about data/statistical methods limited independent evaluation; multiple questioned genomic predictors were later associated with suspended/terminated trials and retractions.

**INFERRED transport.**
This is a naturalistic example where deleting provenance/process ancestry from a compact scientific representation can obstruct later checking and can matter to downstream scientific/clinical authority.

It therefore supports:
`PROVENANCE INFORMATION CAN BE FUTURE-AUTHORITY MATERIAL`.

It does **not** establish that the exact 4.67 componentwise veto rule is correct.

## Case C — Same data, many defensible analyses

### Silberzahn et al. (2018)
*Many Analysts, One Data Set*

Drive source:
`1x6zbA1sV2Jd4Tn65NYdY6QMfSAEA3T2z`

**OBSERVED.**
Twenty-nine teams analyzed the same dataset for the same research question using substantially different defensible analysis strategies. Reported effect estimates varied materially and significance conclusions differed across teams.

**OBSERVED.**
The authors interpret the exercise as making transparent how subjective but defensible analytic choices affect results.

**INFERRED transport.**
This supports the broader warning that an apparently compact “current result” can erase analysis-path distinctions that remain relevant to later inference/audit.

The mapping is closer to **provenance / analysis ancestry** than to the frozen EXT or REOPEN coordinates.

## Case D — Weight-of-evidence practice

### EFSA Scientific Committee (2017)
*Guidance on the Use of the Weight of Evidence Approach in Scientific Assessments*

Drive source:
`1IytbCZ4mlHF2qfwKWjNb3iYKZ3zgq9vP`

**OBSERVED.**
The guidance distinguishes reliability, relevance and consistency and states that criteria need not have equal importance; their relative importance may be case-specific.

**OBSERVED.**
It requires uncertainties, methodological choices, evidence inclusion/exclusion and expert judgment to be made transparent.

**INFERRED transport.**
This is compatible with typed, non-uniform evidence/loss bookkeeping.

But it does not establish non-scalarizability, nor does it validate MQR's five coordinates.

## Transport verdict

### Supported locally

**OBSERVED + INFERRED**
There are real scientific settings in which provenance, processing ancestry, analysis choices and uncertainty metadata are not dispensable merely because a current output can be represented compactly.

Thus the 4.67 **PROV** family is not purely a simulator-internal invention.

### Not supported yet

**OPEN**
No naturalistic case in this pass prospectively validates the complete frozen tuple:

`(SEP, REOPEN, PROV, EXT, RELEASE)`.

In particular:
- exact EXT semantics remains synthetic;
- exact REOPEN thresholding remains synthetic;
- exact RELEASE loss severity remains synthetic;
- coordinatewise debt thresholds are synthetic;
- hard-veto priority is synthetic;
- B0/B1/B2 budgets are synthetic.

## Formal naturalistic status

`NATURALISTIC_TRANSPORT_PARTIAL_PROV_ONLY`

and

`FULL_TYPED_VECTOR_TRANSPORT_HOLD`.

This status is insufficient for Real-Language v0.30 semantic promotion.

## Anti-self-confirmation conclusion

The naturalistic lane does **not** say:

> the simulator predicted reality.

It says:

> one frozen coordinate family, provenance/ancestry, has independently documented analogues in scientific practice where omitted provenance obstructed later checking or changed the authority of downstream use.

That is a transport clue, not validation of the simulator.
