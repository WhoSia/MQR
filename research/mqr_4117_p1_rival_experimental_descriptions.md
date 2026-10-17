# MQR-4.117 P1 — Rival Description of a UV–Vis Measurement

2026-10-17. 4.117 ACTIVE. This is a **constructed analysis of a real type of method**, not a report of a particular laboratory observation or historian-verified exclusion.

## Shared case
A researcher reports UV–Vis absorbance for a solution and estimates a concentration using a calibration curve. At the procedural level, blank choice, sample preparation, wavelength selection, and reference standards matter. These are generic features, not an inspected experiment record.

## Encoding L — operation dependency
Nodes include blank correction, wavelength selection, reference acquisition, absorbance readout, fitted calibration relation, concentration inference. Dependencies may be logically typed and checked. It can detect missing calibration inputs or inconsistent data transformations. It does **not** by itself express who controls the certification of standards or whether suppressed failed trials were eligible evidence.

## Encoding P — material and institutional practice
Records the physical preparation of standards, custody of reference stocks, instrument drift checks, who is allowed to challenge an SOP, how failed runs are classified and retained, and who has authority to declare an anomalous result inadmissible. It can disclose contestation about the source of standards or excluded observations. It does not, by itself, prove the numerical correctness of Beer–Lambert inference or restore missing raw data.

## Divergence test
Construct cases X and Y with the exact same final absorbance vector, calibration fit, and operation-dependency graph; in X, the standards have independently inspectable calibration provenance and all failed runs remain accessible; in Y, the standard provenance is controlled by the same body under challenge and failed runs are discarded without an independent audit. A purely final-output/logic encoding equates X and Y, whereas the practice encoding distinguishes them. These are stipulated possible cases; they are not claims that Y occurred in an actual laboratory. Normative validity still needs an independent argument—practice description does not confer it.

Counterpressure against Encoding P: add a case with complete custody records but incorrect unit conversion in the curve. Encoding P can be internally rich but still fail analytical correctness. Hence neither encoding subsumes the other. The choice of what to record is itself contestable and may change once participants describe an unencoded objection.

## A revision protocol, not another closed taxonomy
1. Preserve a challenge in the challenger's own terms before assigning a graph label.
2. State what each encoding can/cannot decide; pair counterexamples in both directions.
3. Separate a genuinely unexpressible question from one expressible but empirically unanswered.
4. Require question-level justification before claiming a single numeric notion of methodological progress.
5. Permit replacing the research question itself while retaining traceability to the earlier question.

## Continuity / provenance
The original experimental-method→logical-operations inquiry remains. 4.114 original calibration custody still HOLD; 4.115 citation-provenance and proof-congruence and 4.116 archival-selection limits remain inherited. Existing Harvest W05/K02/K04/C2 are lineage references, not independently harvested findings. This conceptual construction does not cure empirical holds.

## Future formal-name candidate; NOT activated
**MQR-4.118 — The Politics of Epistemic Legibility & the Plurality of Scientific Reasons: Incommensurable Problem Formulations, Material Practice, Institutional Contestability, Counterfactual Exclusion & the Limits of Methodological Self-Correction**

4.117 remains ACTIVE, its tests unfinished. Propose advancement when contrasting encodings have source-grounded cases and demonstrated rival judgments rather than moving version numbers automatically.
