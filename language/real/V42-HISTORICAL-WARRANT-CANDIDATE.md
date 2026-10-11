# Real-Language 0.42-CANDIDATE — Historical Warrant & Observational-Quotient Semantics

**Status:** executable Rust **DEVELOPMENT CANDIDATE**, **NOT PROMOTED**. Does not edit `REALPACKET 0.2/0.3`, `REALACQUIRE 0.29`, or `REALREFERENCE 0.41-CANDIDATE`. Trigger: MQR-4.107 (historical sufficiency), MQR-4.108–4.110 (calibration/reference genealogy), 4.111 (nonrecoverable pre-intervention state), and 4.112 (original FER grain selection versus published reduced example). Historical argument and exact API are version-local; this is **not** a new MQR formal research version.

## What question does Real-Language now answer?

**Not** "does a claim match the world?" The compiler is not a world witness. A narrower, model-relative question is:

> For a **declared finite set of possible experimental histories**, does a target historical claim take the same value in every history producing the same currently accessible observation? If not, which additional **declared AVAILABLE** trace fields, separately or jointly, would distinguish those histories? What remains blocked by UNKNOWN or DESTROYED traces?

This separates *what the current experiment observes*, *what the modeled history was*, *what additional measurement could separate modeled rivals*, and *whether any actual world evidence warrants the assumed history universe*. No universal truth metric, scalar progress, complete rival atlas, real-world model selection, root independence guarantee, or scientific stopping rule is inferred.

## Elementary semantic contract, not novel theorem

Let (H) be a finite **declared** history set, (O:H\to\mathcal O) the projection to presently available observation coordinates, and (Q:H\to\mathcal Q) the declared historical target. There exists a function (f:O(H)\to\mathcal Q) satisfying (Q=f\circ O) **if and only if** (Q) is constant on every fiber (O^{-1}(o)). Necessity is immediate; sufficiency defines (f(o)) as the unique target value on that fiber. This is standard quotient/factorization logic, **not a new MQR mathematical discovery**.

The executable returns a *constructive twin-history witness* whenever there exist (h_1,h_2\in H) with (O(h_1)=O(h_2)) and (Q(h_1)\ne Q(h_2)). It counts unordered such pairs. A new available probe (P) refines (O) to ((O,P)); the count of indistinguishable opposite-target pairs **cannot increase**, but nothing ensures the probes are factually achievable or exhaust all rival histories. The implementation enumerates finite minimal **cardinality** sets among at most 8 declared AVAILABLE probes that eliminate these pairs; a DESTROYED or UNKNOWN probe is never treated as acquired. Minimal cardinality is not minimal cost, causal relevance or unique epistemic strategy.

**Crucial counterexample to over-inference:** Even when finite factorization PASSes, expanding (H) to include a previously unconceived history can invalidate it. Therefore finite proof does not certify the ontology of histories or empirical completeness. A code-reported zero conflicting pairs is internal only.

## Isolated typed surface and grammar

Independent CLI: `cargo run --manifest-path language/real/Cargo.toml --bin real-v42-history -- language/real/fixtures/v42/joint-ancestry-required.real`.

```text
REALHISTORY 0.42-CANDIDATE
id MQR4112_joint_ancestry_discriminator
basis FINITE_COUNTERMODEL
target claimed_mechanism
observe tutorial_digest
observe printed_interval
probe original_roster AVAILABLE
probe analysis_revision AVAILABLE
probe measured_d0 UNKNOWN
world h_selection tutorial_digest=PUB printed_interval=REPORTED original_roster=R1 analysis_revision=V1 measured_d0=UNSEEN claimed_mechanism=SELECTION
world h_version tutorial_digest=PUB printed_interval=REPORTED original_roster=R1 analysis_revision=V2 measured_d0=UNSEEN claimed_mechanism=WRAPPER
world h_quality tutorial_digest=PUB printed_interval=REPORTED original_roster=R2 analysis_revision=V1 measured_d0=UNSEEN claimed_mechanism=QUALITY
END
```

Typed fields are nonempty identifier-like atoms and not arbitrary natural language. All modeled worlds require identical schemas; duplicate world names, fields, probes, extra commands and trailing content fail closed. A `SOURCE_REPORTED` basis requires a hexadecimal 64-byte-represented SHA256 identifier (receipt pointer), but still **does not** authenticate source, external custodian, experimental adequacy, science truth or independence. A `FINITE_COUNTERMODEL` **cannot** claim a real source hash: simulated histories remain simulated.

Outputs include `history.base_ambiguous_pairs`, explicit conflicting named histories, `history.base_finite_factorization`, `history.all_available_probe_ambiguous_pairs`, `history.probe_minimal_resolving_sets`, `history.nonavailable_probe_fields`. **Always** outputs `world_authority=HOLD`, `extrapolation_to_unmodeled_histories=FORBIDDEN`, `source_truth_from_sha256=NOT_INFERRED`, `real_language_promotion=UNPROMOTED_CANDIDATE`.

## Five explicit philosophy-of-nature countermodels

1. **FER data ancestry** [`fer-selection-twin.real`](fixtures/v42/fer-selection-twin.real): same tutorial observation and printed interval, different modeled age mechanisms; FULL ROSTER may separate this **restricted two-world** toy model. This DOES NOT mean a roster alone suffices for the real FER reconstruction. The actual full original author source is NOT AVAILABLE.
2. **Joint ancestry correction** [`joint-ancestry-required.real`](fixtures/v42/joint-ancestry-required.real): three invented histories have identical observed data. **Three** discordant pairs. Neither full selection roster nor analysis software revision alone identifies the mechanism; their **joint** proposed availability resolves these declared three. The true FER world could require additional instrumentation, historical quality logs, calibration model or other causes; `measured_d0 UNKNOWN`.
3. **Irreversible experiment** [`destructive-measurement-history.real`](fixtures/v42/destructive-measurement-history.real): two distinct prior states yield same post-test signal; lost pre-state observation is `DESTROYED`, so no available witness eliminates ambiguity in this small model. This does not prove universal retrodictive impossibility if other independent external evidence later appears.
4. **Common calibration ancestor** [`calibration-common-root.real`](fixtures/v42/calibration-common-root.real): two calibrated descendants agree in observed readings despite divergent absolute offsets. A **declared potentially accessible** independent reference separates this finite rival pair, but independent causal ancestry must be externally checked; its name cannot certify independence.
5. **Finite adequacy mirage** [`local-factorization-nonworld.real`](fixtures/v42/local-factorization-nonworld.real): three modeled histories locally factor the target through observed reading; this does **not** demonstrate world completeness.

These are synthetic models with no newly recovered OSL grain bytes, no genuinely independent physical calibration witness, and no empirical causal attribution.

## Real execution and regression evidence

- [Read-only original CI #38133414430 — SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38133414430), source head `d543eab0`: 11 Rust tests PASS, all legacy Real-Language binaries build, four finite model fixtures and deliberate rejection of `SOURCE_REPORTED` self-assertion.
- [Expanded native CI #38133519768 — SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38133519768), source head `c83aa0545b3ffdb6ba73bb61def2d6406aa7aa53`: **12 Rust tests PASS**, full legacy binary regression build SUCCESS, five executable fixture receipts and expected rejection PASS. [Artifact #11699559295](https://github.com/WhoSia/MQR/actions/runs/38133519768/artifacts/11699559295), SHA256 `6cca35a6677c7ee759baf10e8b162976f62e57834093f656b04dfe373079b231`; downloaded ZIP byte-hash independently checked.
- Pre-repair CI [#38133348217](https://github.com/WhoSia/MQR/actions/runs/38133348217) FAILURE: Rust E0282 untyped minimal-set vector; fixed with explicit `Vec<Vec<String>>`. Not a scientific failed prediction. The cited passes are source-head bound: later documentation updates are not automatically CI-certified.
- Scope: **COMPILER_STRUCTURE_PASS / FINITE_COUNTEREXAMPLE_PASS / HISTORICAL_EMPIRICAL_WARRANT_HOLD / LANGUAGE_PROMOTION_HOLD**. Proof-assistant theorem and independent Haskell implementation are NOT supplied and are NOT claimed.

## Why this is philosophical science, not an audit-as-ontology

The experiment enforces a three-way separation:

`OBSERVABLE COINCIDENCE != HISTORICAL IDENTITY != WORLD-WARRANTED CLAIM`.

Unlike an ordinary evidence ledger, REALHISTORY can *falsify* a proposition that a declared observation is sufficient for a target, by supplying two explicit histories. Unlike the world itself, the language **cannot** know which possible histories were never proposed. It thus preserves the strongest lessons of realist humility without treating all evidential judgments as equal or impossible. Real progress requires a subsequent world-facing probe separating scientifically relevant competing mechanisms and showing why its physical instrumentation/custody is warranted.

**Next scientific discriminator:** Genuine source-selected FER dataset or independently witnessed calibration history; otherwise use newly represented countermodel classes to test philosophical hypotheses (e.g., criterion of empirical grounding, analog causal models) without posing constructed histories as measured facts.
