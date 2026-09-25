# MQR — Measurement-Quotient Realism

This repository is the **living formal substrate** of MQR.

- `main` carries the current live doctrine and executable/auditable protocol surfaces.
- Historical notebooks, retired stages, and superseded drafts are archived outside this repository (canonical archival storage: Drive / Research OS).
- **Branch policy is MAIN_ONLY.** Temporary branch creation is forbidden unless the user explicitly authorizes an exception.
- Retired or superseded files should be deleted from the repository once their live successor is established; history remains recoverable from Git and external archives.
- Notion remains the live lab notebook. This repository contains only the parts that benefit from byte-level versioning, reuse, validation, or implementation.

## Current live surface

- `doctrine/CURRENT.md` — compressed current doctrine, including Generation-IV C/E/P/R_open authority semantics
- `language/real/README.md` — Real-Language v0.3–v0.8, including proof, transfer, composition, substitution and frontier-relative contact-rank lanes
- `language/real/src/main.rs` — canonical Rust compiler; `language/real/reference.py` — independent Python reference
- `language/real/examples/` — historical and current Real-Packets
- `protocols/challenge-admission.md` — challenge-admission governance protocol
- `experiments/mqr-4.41/` — current live adversarial court; MQR-4.41 replaces primitive empirical-degree rank with frontier-relative external discrimination cover

Real-Language v0.3 remains the transport-compatible historical lane; v0.4 is the proof-boundary lane; v0.5 is the executable authority-transfer lane; v0.6 adds compositional transfer; v0.7 adds world-contact substitution; v0.8 adds frontier-relative contact-rank analysis. MQR-4.41 rejects analyst-declared empirical degrees as a primitive ontology for minimal contact, retains only a claim/rival/query/root-indexed minimum external discrimination cover, rejects generic basis-exchange/matroidality, and requires rank reopening under frontier or root-semantic drift. Formalization remains route-relative and optional. Scalar projection remains OFF and truth-distance semantics remain UNIDENTIFIED.

Lineage typing is explicit in v0.3. In particular, **ChatGPT-Web-HWPX-MCP is ENGINEERING_DEVELOPMENT, not a research Lab**. Engineering/development lineages may be used as valuable external cases without being redescribed as scientific programmes.

Newly touched executable surfaces should prefer **Rust as canonical implementation** when practical; Python is retained as an independent reference/audit implementation where useful. Existing Python is migrated only when the surface becomes live again or a concrete reliability/portability/performance reason exists.
The repository should stay small enough that a new contributor can tell what is *currently alive* without reconstructing the whole genealogy.