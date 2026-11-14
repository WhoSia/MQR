# Real Language · MQR 5.4 Open-Horizon Bridge Audit (experimental, unpromoted)

**Status:** NON-PROMOTING RESEARCH UTILITY / NOT A NEW REAL LANG GRAMMAR OR RELEASE.
**Research session:** MQR 41, 2026-11-13.

This directory already contains canonical Rust Real-Packet/transfer lanes and multi-language independent checks. The small Python module `open_horizon_bridge_v54.py` **does not replace, import authority from, or override** those implementations. It is an independent, intentionally low-authority study of the MQR 5.4 question: how can two partially mutually unintelligible scientific practices learn a bounded observational correspondence **without laundering that correspondence into shared ontology or automatic theory translation**?

## Why this exists

The MQR 5.0 archive explicitly criticized requiring complete theory translation where Galison-style *trading zones* achieve practical cooperation using partial correspondence. MQR 5.2 proposed learning the world–concept bridge rather than positing it in advance; 5.3 investigated calibration and evidence ancestry. MQR 5.4 restores the broader philosophical question rather than treating each calibration receipt as the end of inquiry.

The Real Lang v0.5/v0.6 direction already separates formal custody and world authority, retains missing ancestry and prevents local success from laundering global authority. This experimental helper **does not rediscover or supersede those principles**. It implements one reusable bounded, testable guard without changing canonical syntax.

## Input contract

`PairedReceipt(case_id, left_output, right_output, comparable, common_operation_witness, independent_calibration_witness, ancestry_divergence_witness)`

All witness flags are **supplied declarations**, not externally validated world facts. They should be set only from verifiable source-linked receipts in real research. `left_output`/`right_output` are assumed already normalized by an independently tested conversion; the program does not discover that conversion.

One receipt means a **scoped, paired experimental preparation**, not a theoretical sentence, ontological equivalence, or a general logic-mapping theorem.

## Output semantics

- `HOLD_NO_COMMON_OPERATION`: no grounded paired experiment or incomparable outcomes.
- `HOLD_UNVERIFIED_ANCHOR`: conversion/calibration anchor not independently checked.
- `HOLD_SHARED_ANCESTRY`: failure-lineage separation not witnessed, so independent corroboration cannot be inferred.
- `HOLD_NO_CASES`: no experiment.
- `FAIL_SCOPED_MISMATCH`: a **declared comparable** paired observation contradicts the candidate conversion on its tested scope (not a blanket denial that any translator exists).
- `BOUNDED_OPERATIONAL_MATCH`: the **declared** finite receipts agree; not a universal PASS for translation, science, ontology or paradigm change.

Mismatches outrank matches, and unresolved tests cannot be promoted to a success by adding many ordinary matches. Duplicate IDs fail explicitly. Scope is the finite set of paired experiment identifiers, not a post hoc claim of universal equivalence.

**Critical limitation:** This is a conditional checker with trusted-flag inputs, not a physical experiment or externally calibrated metrological evaluator. A false or circular witness declaration can make its positive outcome spurious. `ancestry_divergence_witness=True` cannot be set merely because two files or team names differ. No full Real Lang release should import `BOUNDED_OPERATIONAL_MATCH` as `WORLD_AUTHORITY_PASS`.

## Reproduction

From `language/real/experiments`:

```bash
python -m unittest -v test_open_horizon_bridge_v54.py
```

Nine tests:
1. identical outputs without grounded common operation held;
2. uncalibrated conversion held;
3. shared calibration ancestry held;
4. scoped mismatch detected;
5. finite positive explicitly bounded;
6. 100 matches cannot hide one mismatch;
7. mixed unresolved/positive remains held;
8. duplicate and empty IDs rejected;
9. empty dataset held.

The nine assertions passed on Python stdlib locally **before GitHub submission**. This is not a Rust/Haskell/Prolog cross-language concordance result or complete Real-Language CI success claim. The existing Real-Language CI is triggered by changes under `language/real/**`; any ensuing check runs separately and should not be asserted successful without an inspected workflow receipt.

## Philosophical interface and next challenge

**Scientific cooperation ≠ complete theoretical translation ≠ shared ontology.**

A future Real Language design could model partial translation as a *typed, witness-indexed, revisable empirical bridge*, while its formation as a scientific and historical achievement remains out of reach of a Boolean validator. A meaningful external test requires ground-truth pre-registered apparatus, matched physical preparation, calibration provenance and a conflicting rival, not just a toy string comparison.

Research history and evidence map:
[2026-11-13 MQR 41 macro-genealogy](../../research/mqr_54_mqr41_macro_genealogy_science_studies_real_language_reflection.md) (subject to its own independent evidential scope).


## Follow-up: admissible experiment sequences

[Protocol frontier experiment](protocol_frontier_v54.py) searches declared finite
models and a protocol automaton for the minimum-cost separating observation.
A reset requirement can make two models equivalent on every allowed trace
even while both expose the same elementary actions. A separate budget result
retains the minimum witness when it cannot currently be afforded.

```bash
python -m unittest discover -s language/real/experiments -p 'test_protocol_frontier_v54.py' -v
```

The comparison starts from known initial states and assumes deterministic
transitions, commonly interpreted labels and an observation at each prefix.
The existing paired-receipt audit still handles declarations about calibration
and evidence ancestry. See the [research note](../../../research/mqr_54_protocol_frontier_and_waveguide_design.md)
for the finite-model result and the historical comparison.
