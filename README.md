# MQR — Measurement-Quotient Realism

This repository is the **living formal substrate** of MQR.

- `main` carries the current live doctrine and executable/auditable protocol surfaces.
- Historical notebooks, retired stages, and superseded drafts are archived outside this repository (canonical archival storage: Drive / Research OS).
- Do not create a branch for every research stage. Branches are reserved for genuinely live divergent work that cannot yet share one current state.
- Retired or superseded files should be deleted from the repository once their live successor is established; history remains recoverable from Git and external archives.
- Notion remains the live lab notebook. This repository contains only the parts that benefit from byte-level versioning, reuse, validation, or implementation.

## Current live surface

- `doctrine/CURRENT.md` — compressed current doctrine, including Generation-IV C/E/P/R_open authority semantics
- `language/real/README.md` — **Real-Language / Real-Packet v0.3**, the active profile-first event-to-realist-authority language
- `language/real/src/main.rs` — canonical Rust compiler; `language/real/reference.py` — independent Python reference
- `language/real/examples/` — historical and current Real-Packets
- `protocols/challenge-admission.md` — challenge-admission governance protocol
- `experiments/mqr-4.31/` — current live research stage

Real-Language v0.3 represents **world-constrained evidential profile + typed transport map + residue**. MQR-4.31 deprecates the legacy scalar/ordinal T coordinate and separates transport target, evaluability, and survival. W and I remain externally calibrated ordinal indices; N and D retain their previous HOLD ceilings. Scalar projection remains OFF and truth-distance semantics remain UNIDENTIFIED.

Lineage typing is explicit in v0.3. In particular, **ChatGPT-Web-HWPX-MCP is ENGINEERING_DEVELOPMENT, not a research Lab**. Engineering/development lineages may be used as valuable external cases without being redescribed as scientific programmes.

Newly touched executable surfaces should prefer **Rust as canonical implementation** when practical; Python is retained as an independent reference/audit implementation where useful. Existing Python is migrated only when the surface becomes live again or a concrete reliability/portability/performance reason exists.
The repository should stay small enough that a new contributor can tell what is *currently alive* without reconstructing the whole genealogy.