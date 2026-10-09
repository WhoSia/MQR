# MQR-4.97 P1B — Secondary Visit-Order Detection Heterogeneity Diagnostic

**Frozen after inspecting P1 actual original NAAMP heldout numbers; not blind confirmatory evidence.** The NAAMP 2001 real field original two species and original Rust audit are already safely archived in Drive `1bU2woFMjvPIsJs-I2V7BRmNRRa2HNKbb`; Lean original proof receipt `1_vAOSl-aj9CXgOl26jt4J4NmjctvVypL`.

P1 actual source SHA check success, Rust 130 field sites, 337 visits per species, 20/13/97 sites with one/two/three within-year visits, Julian days 72–179. Site-visit record metadata is not direct true occupancy, includes 0–3 ordinal call strength and environmental covariates. `P. crucifer` 96/130 ever heard; 95 first visit heard; transitions (0→1)=4, (1→0)=76 across 207 adjacent visit pairs; homogeneous occupancy fit `ψ=0.9506,p=0.43796`. `P. feriarum` 43/130 ever heard; 39 first heard; transitions (0→1)=4, (1→0)=40; homogeneous model ψ at numerical boundary 1 and p≈0.128. Holdout 30 entire sites: homogeneous occupancy and full-training visit-marginal iid model almost tied; no established occupancy predictive superiority. These already-seen results are now explicitly marked **post-discovery diagnostic triggers**.

**P1B new discriminant:** Does **occasion-specific observation probability** capture the strong directional changes across survey occasions without requiring a stable, source-free or truly geographically independent occupancy process?

With exactly the same original 130 physical site keys, site-level fixed train/test partition and real observation rows, predeclare three observation-prediction contracts:
1. `iid_all`: single marginal detection rate estimated from **all training survey observations**, independent Bernoulli across visits, one scalar `q`.
2. `iid_occasion`: 3 empirical training first/second/third occasion detection rates `q_j` across actual observed sites, independent across occasions **unconditionally** (no latent occupancy).
3. `occu_homogeneous`: P1 independently recorded site occupancy latent ψ and one detection p.
4. `occu_occasion`: site latent ψ with 3 observation probabilities p1,p2,p3 fitted via conventional EM for single-season occupancy, given no false positives, fixed site occupancy during the survey season, independent secondary visits conditional occupancy, and common p_j across sites. If stationary occupancy fails across Julian 72–179, this is a phenomenological conditional fit, not truth.

Score all four on **heldout entire site histories**, exactly one fixed partition, negative log likelihood lower is better. Fit p_j only from training; no outcome-tuned hyperparameters. Record each visit-order empirical observed positive/total per species, fitted parameter p_j and occupancy ψ, boundary solutions, and results from the first published P1 contract. A strong fall in p_j cannot by itself be attributed causally to phenology, because which sites have the 2nd/3rd visit varies by site and dates/effort. This is a diagnostic of observation-process nonstationarity and missing closure justification, not a confirmatory p-value or generalizable predictive superiority.

**Math/formal:** Retain previous Lean example: one visit ψp alone insufficient; two-visits can separate model worlds IF repeated conditional detections share stationary p and closure. Under varying p_j and unknown site frame, no automatic identification; toy Lean theorem is not a theorem that true occupancy/heterogeneous p parameters are identified by actual data.

**Stop:** P1B official CI success + Drive derived receipt + GitHub scientific court + Notion original single Lab -> 4.97 bounded CLOSE, propose next distinct title (do not automatically open).
