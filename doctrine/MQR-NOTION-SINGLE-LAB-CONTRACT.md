# MQR Notion Single-Lab Contract — Mandatory Entry Invariant

**Canonical Notion Lab:** `MQR — Measurement-Quotient Realism`, page `3c8ef561-cf92-8156-93b6-fcf6de9955f7`. This is the **only** valid `MQR*` row in the Research OS Notion `Labs` database (`collection://ad73e9ba-0ed8-4af6-b724-a95e849648dc`).

**User mandate:** MQR has no independent Notion version folders/pages. All research stages (`MQR-4.84` … `MQR-4.91` …), all checkpoints (`P0`, `P1.3`, `P1.4`), and incremental/multi-part outputs are headings or targeted patches **inside the same existing canonical MQR page**. They are not separate Labs, Notion pages, child pages, folders, or data-source rows. A version title is a section name, not a Lab entity.

## Prewrite barrier

1. Read the existing canonical MQR root page and its Lab identity. Read the Notion `Labs` schema when applicable.
2. Before any new MQR stage, retrieve `Labs` rows satisfying `Lab LIKE 'MQR%'`. The only admissible set is exactly the single canonical MQR root page ID above. If there are additional MQR-version rows, stop and repair the registry without deleting substantive content before verified source preservation.
3. **Prohibit** `notion_create_pages` into `Labs` for MQR stage, and **prohibit** `notion_create_pages` under MQR root for P-stage material. Invoke `notion_update_page` on the existing canonical page only, using `insert_content` / narrow `update_content`. No new Notion folders or phase pages.
4. MQR formal source code, executable court, receipts and papers may live in GitHub and Drive in version-specific paths: this is a **file-artifact organization rule**, not authority to create Notion pages.
5. If a tool's output would create another row or a child stage page, **FAIL CLOSED** with `MQR_NOTION_DUPLICATE_LAB_BLOCKED`, select the existing root, and retry as a section update.
6. Never assert success solely from a write tool: independently query the `Labs` collection and verify `MQR` row count is one, root exact ID. If this postwrite check fails, report structural breach and repair it.

## Repair incident 2026-10-08

Eight rows (`MQR-4.84` … `MQR-4.91`) had been created under `Labs`, including creation of `MQR-4.91` by agent while `MQR` main page already existed. These were not independent Labs and violated the author's established narrative model. Original row contents were preserved and the eight version pages moved **out of `Labs` to private workspace level** (not permanently deleted and not made MQR children); authorized canonical MQR root was amended in place. Readback SQL showed exactly one MQR row. If later requested, reconcile the parked history against canonical sections before any irreversible deletion. No user-facing claim of permanent deletion.

## Scientific pointer, not new Lab

As of incident remediation: `MQR-4.90` bounded source court closed; `MQR-4.91` remains OPEN as a **version section**, pinned Java Maxent original Oceania raster reprojected exactly 2,931 valid cells (max abs error 0.0), 4 original fold target rasters generated, reproducibility CI `37777179020` SUCCESS, fold-target AUC not yet computed. See `docs/MQR-4.91-P1-SOURCE-IDENTITY-CORRECTION.md`. All future source/Harvest and Pn outputs go to the same MQR canonical Notion page.
