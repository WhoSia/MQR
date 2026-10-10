# MQR — Measurement-Quotient Realism

This repository is the **living formal substrate** of MQR.

- `main` carries the current live doctrine and executable/auditable protocol surfaces.
- Historical notebooks, retired stages, and superseded drafts are archived outside this repository (canonical archival storage: Drive / Research OS).
- **Branch policy is MAIN_ONLY.** Temporary branch creation is forbidden unless the user explicitly authorizes an exception.
- Retired or superseded files should be deleted from the repository once their live successor is established; history remains recoverable from Git and external archives.
- Notion remains the live lab notebook. This repository contains only the parts that benefit from byte-level versioning, reuse, validation, or implementation.

## MQR-4.111 — Irreversible measurement and retrodiction (OPEN/HOLD)

**Current formal stage:** [Notion MQR-4.111](https://app.notion.com/p/3f5ef561cf92815c9263c9d8bcb535dc) · [research evidence, source limits and rival models](research/mqr_4111_irreversible_retrodiction.md).

- **P1**: eight-atom *synthetic* nonidentifiability/reset fixtures, [Rust source](experiments/mqr-4.111/src/main.rs), bounded PASS; no new theorem.
- **P2–P3**: five original OSL paper PDFs were recovered into Drive `10_PAPERS`. [Costas et al. (2012) Table 2 — 13 published sample summaries](experiments/mqr-4.111/costas_2012_table2.rs), independently re-computed in Rust; P4 descriptive additive-vs-proportional dose residual check, [read-only CI #38041208652 — SUCCESS](https://github.com/WhoSia/MQR/actions/runs/38041208652) on source commit `506165f` (**12 unit tests total**; P1 4 + real-paper P3–P5 8). The paper reports known-dose recovery means near 1 while young naturally dated specimens are over-aged against independent age controls; **do not infer new physical mechanisms or claim aliquot-level replication**.
- **P5 direct physical evidence:** GWD-245 independent aerial/GPR age estimate 2±1 years (expected 1±1 mGy), natural OSL EBG 23±5 mGy and separate light-cleared aliquots 8±1 mGy; source's 15mGy difference supports history-sensitive component mixture but does not identify original per-grain histories or a unique mechanism. Original Costas Fig S1 and raw aliquot streams remain unavailable locally. A separate [Guérin et al. (2021) source](https://gchron.copernicus.org/articles/3/229/2021/) has [public upstream BINX/CSV supplement](https://gchron.copernicus.org/articles/3/229/2021/gchron-3-229-2021-supplement.zip), with binary acquisition unverified here; its illustrative radiocarbon ages must be distinguished from observed dates.
- **Scientific verdict**: MQR-4.111 OPEN. Five original PDFs archived to canonical Drive `10_PAPERS` and published-summary reproduction PASS_BOUNDED; post-hoc dose residuals (young-seven mean 26.714 mGy; additive LOOCV RMSE 10.541 mGy vs proportional 19.759 mGy) **descriptive only**. Novel physical data, full per-aliquot observations and independent distinctness against SAR/causal-identification models HOLD. Earlier 4.110 OPEN/HOLD preserved.

## MQR-4.110 — Source-grounded calibration transport (OPEN/HOLD)

[Notion canonical](https://app.notion.com/p/3f5ef561cf9281f7a246d950d72f4a41) · [Source-byte and rival audit](research/mqr_4110_source_graph_calibration_transport.md). Original Regnault DjVu verified against public original by SHA-256; **824 pages and six native-rendered source images confirmed** in [Actions #38033207087](https://github.com/WhoSia/MQR/actions/runs/38033207087). **Erratum:** DjVu pp.274–275 = printed pp.238–239, not pp.240–241. [Drive page-render archive](https://drive.google.com/file/d/1wz3A8v6HtEna4TBYFB_aWH6bkinz7Ilj/view). [Rust experiment CI #38031726173](https://github.com/WhoSia/MQR/actions/runs/38031726173) and [Rust dependency audit #38032842985](https://github.com/WhoSia/MQR/actions/runs/38032842985) SUCCESS. Fisher–Neyman/Blackwell/VIM/GUM/Tal/Chang remain strong rivals; novelty HOLD.

## MQR-4.109 — Provenance-sensitive sufficiency (OPEN/HOLD)

[Notion canonical](https://app.notion.com/p/3f5ef561cf9281e88238f23450b60504) · [Research charter and rival court](research/mqr_4109_provenance_sensitive_sufficiency.md) · [Exact local binary test](experiments/mqr_4109/provenance_blackwell_court.py). Successor to 4.108: distinguish fixed-target Blackwell information, calibration-chain authority and historical source provenance. Synthetic mathematical fixture locally PASS; scientific originality and reference certification HOLD. No new CI Actions.

## MQR-4.108 — Cross-principle traceability (OPEN/HOLD)

[Notion 4.108](https://app.notion.com/p/3f4ef561cf92815d9c1ec11355427c92) · [Research source court](research/mqr_4108_calibration_model_underdetermination.md) · [Exact shared-reference test](experiments/mqr_4108/traceability_counterexample.py). Different measurement physics does not certify independent calibration ancestry. Against VIM, GUM, Tal (2017), and Chang (2004), original philosophical distinctness remains HOLD. MQR-4.107 original-image and interpolation limitations are inherited.

## Active historical-metrology court: MQR-4.107 (OPEN/HOLD)

[Notion canonical](https://app.notion.com/p/3f4ef561cf92810384a6c022ad64f20d) · [Research audit](research/mqr_4107_evidential_history_equivalence.md) · [Regnault comparator test](experiments/mqr_4107/regnault_comparability.py) · [Heeger/SNO comparison](research/mqr_4106_heeger_ch9_comparison.md).

Regnault 1847 data are distinguished from **synthetic shared-bias examples**. The current question is whether complete likelihood equivalence entails historically warranted measurement comparability. Lindsey 1997, standard selective inference and Chang 2004 are rivals, not MQR validations. **No new scientific novelty established; 4.106 and 4.107 remain OPEN/HOLD.** No Actions workflow is added for this court.

## Archive and research continuity

Old README sections (former 4.100–4.104 frontiers, prior test/operational notes and legacy live-surface detail) were migrated to the [Drive Markdown archive](https://drive.google.com/file/d/1kjnVmLScrf078-oy8xpYRZLFS6tkH8Ht/view), within [MQR historical archive folder](https://drive.google.com/drive/folders/1-m3vRlSf4UDjx-ilqXkTwGpm-bc2s-cO). **Original byte-accurate text** is recoverable from Git README blob `b5e58df5f86545933fed0f13575773a47d627818`; the Drive export reflows some Markdown whitespace.

**Previous stages:** The 4.108 and 4.109 studies and their source links above remain historically accessible; consult the exact current 4.111 Notion page and research ledger for ongoing work. Prior OPEN/HOLD statuses are not retroactively closed.

A passing finite test certifies **only its stated local contract**; it does not establish historical source truth, independent traceability or new scientific discovery.
