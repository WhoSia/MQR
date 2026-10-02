# MQR-4.70 — Naturalistic Acquisition Manifest

Status: **PRE-OUTCOME / BOUNDED-ACQUISITION-AUTHORIZED / K562-PRIMARY-LANE / NO-SINGLE-CELL-BULK-DOWNLOAD-YET**

## Primary corpus

Replogle et al. (2022), *Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq*.

Canonical identifiers:
- DOI: 10.1016/j.cell.2022.05.013
- SRA BioProject: PRJNA831566
- processed-data Figshare+: 10.25452/figshare.plus.20029387
- raw/GEO manifest Figshare+: 10.25452/figshare.plus.20022944.v2

Available experimental families include:
- K562 genome-scale, day 8;
- K562 essential-scale, day 6;
- RPE1 essential-scale, day 7.

## Bounded primary lane

Use **K562 essential-scale** first.

Reason:
- smaller than genome-wide;
- same cell line as the genome-wide validation family;
- later causal-network work uses this screen because it has more guides per gene and a lower noise floor;
- allows an independent genome-wide family to remain available for transport/replication pressure.

## Acquisition order

1. metadata/file manifest only;
2. bounded processed pseudobulk object;
3. only if needed, selected processed single-cell metadata;
4. no raw FASTQ/BAM acquisition unless the scientific question cannot be answered from processed data.

The full processed release is approximately 160 GB and is not authorized as a default download.

## Outcome-blind family construction

The current and held-out perturbation families must be chosen without inspecting transcriptional response values.

Permitted pre-response variables:
- target-gene identifier;
- cell line;
- screen identity;
- collection day;
- manifest/library identity;
- guide-count / cell-count metadata only if available independently of expression-response effect estimates;
- deterministic lexical or hash-based ordering.

Not permitted for family selection:
- differential-expression magnitude;
- learned causal effect;
- graph centrality;
- response embedding;
- target knockdown effect estimated from expression;
- significance / FDR;
- any outcome-driven cluster.

## Canonical first split

After metadata normalization, define a deterministic target-gene ordering.

Primary rule:
- restrict to target genes with an adequate metadata record;
- sort by stable canonical target identifier;
- assign alternating blocks to CURRENT and HELD_OUT using a predeclared deterministic rule;
- preserve a third metadata-only REPLICATION block when sample size permits.

The exact block size must be frozen after metadata census and before response values are loaded.

## Primary scientific test

Construct a response-derived equivalence or neighborhood relation using CURRENT perturbations only.

Then reveal HELD_OUT responses and ask:

1. do some CURRENT-equivalent model/history candidates separate under HELD_OUT perturbations?
2. do some remain equivalent, providing null controls?
3. does a second metadata-only split rule reproduce the qualitative refinement result?
4. does the result survive simple noise/coverage matching?

## Comparator-only lane

Brown et al. (2025), *Large-scale causal discovery using interventional data sheds light on gene network structure in K562 cells*.

The paper analyzed 788 genes from the K562 essential-scale Perturb-seq after requiring:
- target-expression reduction of at least 0.75 SD;
- at least 50 cells receiving the targeting guide.

These criteria are **not** used to choose MQR-4.70 CURRENT/HELD_OUT families before response reveal because the first criterion is outcome-derived.

They may be used later as:
- a robustness comparator;
- a literature replication lane;
- a post-freeze quality filter sensitivity analysis.

## Secondary transport lane

Use K562 genome-wide as a distinct source-family/validation-family surface after the K562 essential primary analysis.

Do not call this cross-domain transport in the strong sense; it is same-cell-line cross-screen transport.

A stronger later transport can use RPE1 essential-scale.

## Naturalistic promotion burden

A useful 4.70 world-contact result requires:
- pre-response family freeze;
- held-out family refinement of at least one current equivalence;
- null held-out probes;
- robustness under an independent metadata-only split;
- explicit baseline comparison to ordinary experimental-design/identifiability language;
- no claim that the available perturbation universe is complete.

## Data-minimization boundary

Do not acquire multi-gigabyte single-cell matrices merely to demonstrate a structure that can be tested in pseudobulk.

Escalate data volume only when the lower-cost representation fails to preserve the required intervention-response distinctions.
