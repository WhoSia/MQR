# MQR-4.70 — Naturalistic Source Receipt

Status: **SOURCE-LOCATORS-FROZEN / PRIMARY-AUTHORITY-SEPARATED-FROM-SECONDARY-LOCATOR / RESPONSE-NOT-ACQUIRED**

## Primary scientific source

Replogle et al. (2022), *Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq*.

Primary identifiers:
- DOI: 10.1016/j.cell.2022.05.013
- SRA BioProject: PRJNA831566
- processed-data Figshare+ article: 20029387
- SRA/GEO manifest Figshare+ article: 20022944

The primary paper states that processed downloadable single-cell and pseudobulk populations are available and that raw sequencing is deposited under PRJNA831566.

## Primary K562 essential lane

Dataset:
- K562 essential-scale Perturb-seq
- collection: day 6 post-transduction

Authorized first acquisition:
1. KD6 manifest metadata;
2. K562 essential pseudobulk object.

Single-cell object is deferred.

## Secondary reproducibility locator

A public independent reanalysis repository pins the following Figshare file locators:

### manifest
- name: `KD6_raw_files.csv`
- file id: `35773886`
- size: `75,702` bytes
- md5: `908ee4d31af665842240c8341ff03452`

### bounded pseudobulk
- name: `K562_essential_raw_bulk_01.h5ad`
- file id: `35773070`
- size: `79,766,954` bytes
- md5: `8321d5d3ffc99db2a5c71edca4189735`

### deferred single-cell
- name: `K562_essential_raw_singlecell_01.h5ad`
- file id: `35773219`
- size: `10,661,879,995` bytes
- md5: `4f1122ce1c7f13299a68df6459a266d3`

These locators are **secondary** and must be verified against the source deposit at acquisition time.

They are not used as scientific outcome evidence.

## Data-minimization ruling

Authorized default volume:
- metadata manifest: yes;
- ~80 MB pseudobulk: yes;
- ~10.7 GB single-cell: no, unless pseudobulk is insufficient.

## Outcome boundary

No expression-response values have been acquired or used to choose CURRENT/HELD_OUT families in MQR-4.70.

The next authorized mutation after source verification is a metadata census and deterministic family assignment receipt.
