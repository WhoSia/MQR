# MQR — Measurement-Quotient Realism

This repository is the **living formal substrate** of MQR.

- `main` carries the current live doctrine and executable/auditable protocol surfaces.
- Historical notebooks, retired stages, and superseded drafts are archived outside this repository (canonical archival storage: Drive / Research OS).
- Do not create a branch for every research stage. Branches are reserved for genuinely live divergent work that cannot yet share one current state.
- Retired or superseded files should be deleted from the repository once their live successor is established; history remains recoverable from Git and external archives.
- Notion remains the live lab notebook. This repository contains only the parts that benefit from byte-level versioning, reuse, validation, or implementation.

## Current live surface

- `doctrine/CURRENT.md` — compressed current doctrine, including Generation-IV C/E/P/R_open authority semantics
- `language/r/README.md` — **R-Language / R-Packet**, the active event-to-realist-authority language
- `language/r/rpacket.py` — executable stdlib-only R-Packet compiler
- `language/r/examples/` — historical and current event packets
- `protocols/challenge-admission.md` — challenge-admission governance protocol
- `experiments/mqr-4.27/` — current live research stage

R-Language intentionally represents **truth-proximity as an auditable profile plus residue**, not as a primitive probability of truth.
The repository should stay small enough that a new contributor can tell what is *currently alive* without reconstructing the whole genealogy.