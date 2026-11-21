# MQR 42 · 기록 02 — Nov 21 2026 accession / seven immutable Drive objects

Seven objects were identified by **reopening the actual Research OS `00_INTAKE` folder**, because a raw Drive parent search initially returned an incorrect zero count. The folder was rechecked after each set of moves. All seven retain their source Drive IDs and raw byte sizes; only names and parents were changed. At close, direct children of [00_INTAKE](https://drive.google.com/drive/folders/1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16) = 0, a time-scoped observation. **No file was moved to the MQR Chat Archive.** The Research OS [naming](https://docs.google.com/document/d/1OY2hQdUH0xYwiJr6HKTg5wixWLWcfymYM5U-XDeMoyM/edit) and [custody](https://docs.google.com/document/d/1GK7OrfZfr4nBEfpHEszzmp8LCPFYAxP_g46YVek-rlc/edit) standards were read.

| Original item | Primary identity and exact role | Canonical Drive location | Original size | Custody class |
|---|---|---|---:|---|
| `Opto-JAWS.zip` | Kraus, Kieler, Behr & Palafox (2025), [PTB-OAR dataset 10.7795/720.20250210](https://doi.org/10.7795/720.20250210); 12 figure-export tables + README | [1iE96PNpjXKVqROx1GXprQ7N7D42KOabF](https://drive.google.com/file/d/1iE96PNpjXKVqROx1GXprQ7N7D42KOabF/view) | 1,447,799 | 11_SUPPLEMENTARY_MATERIALS; byte-verified |
| `Malus_app_inventor.aia` | Rivera-Ortega et al. (2025), MIT App Inventor project of Malus/LEGO experiment; Blockly XML/source/screens/assets | [1dmiuP_h92Qv0PMvoZKLLrkJjk-rmhkgh](https://drive.google.com/file/d/1dmiuP_h92Qv0PMvoZKLLrkJjk-rmhkgh/view) | 1,033,634 | 11_SUPPLEMENTARY_MATERIALS; local SHA, provider equality unverified |
| `LEGO_MALUS.lxf` | Rivera-Ortega et al. (2025), LEGO Digital Designer 4.3 Mindstorms CAD XML/project | [1Bz6_KSRf5nzB4P34lmn134uIRoamOa2l](https://drive.google.com/file/d/1Bz6_KSRf5nzB4P34lmn134uIRoamOa2l/view) | 13,885 | 11_SUPPLEMENTARY_MATERIALS; local SHA, provider equality unverified |
| `Pli_article_def.pdf` | Friso Timmenga (2024), “Academic Philosophy: A Way of Life?”, *Pli* 35:47–72, Groningen publisher-pdf label; **mostly image scan** | [1hrd4TzGJmkYQlW8WQANAobSTB6JniAB8](https://drive.google.com/file/d/1hrd4TzGJmkYQlW8WQANAobSTB6JniAB8/view) | 15,085,910 | IMAGE_SCANS OCR backlog; do not claim full machine text |
| `Hadot, Pierre _ Internet Encyclopedia of Philosophy.pdf` | Matthew Sharpe, undated IEP **secondary encyclopedia** article “Pierre Hadot” | [1aS0L_RDEqGWEkM7e0kFMqQvZSNKlwnGe](https://drive.google.com/file/d/1aS0L_RDEqGWEkM7e0kFMqQvZSNKlwnGe/view) | 338,731 | 20_NON_PAPER_SOURCES; not an original Hadot work |
| `rorty1984.pdf` | Richard Rorty, “The Historiography of Philosophy: Four Genres”, in *Philosophy in History* (1984), pp.49–75; later Cambridge digital text DOI [10.1017/CBO9780511625534.006](https://doi.org/10.1017/CBO9780511625534.006) | [1jFjhCBBvTNVt1EoDXW8zNmJLQCvXyWT9](https://drive.google.com/file/d/1jFjhCBBvTNVt1EoDXW8zNmJLQCvXyWT9/view) | 1,842,017 | 11_SOURCES; scholarly book chapter primary |
| `Dataset for comparison of QuantumPower method to the differentiall PJVS method.7z` | Šíra (2023), original [Zenodo 10.5281/zenodo.10046413](https://doi.org/10.5281/zenodo.10046413), experimental archives and QPSW traces | [178ypBIq_G460hGi7oHoweTBfNfb5qmK_](https://drive.google.com/file/d/178ypBIq_G460hGi7oHoweTBfNfb5qmK_/view) | 71,607,511 | 20_NON_PAPER_SOURCES; byte-verified |

## Source hashes verified before Drive metadata-only move
PTB ZIP SHA256: `cdc5cfe15c2d5f81e59515113b78a5eff5abdcffda624849a154cd3ca5836a8c` — matches PTB official public checksum.
MIT App .aia SHA256: `7a3254198882403363c9f0236dc94180eb7669a73a4d1802ea317ec99b782494`.
LEGO .lxf SHA256: `433bcda1de6432204f7c4e2eac374539e599133fb4d77cf502167ffac354ba9c`.
Timmenga PDF SHA256: `ce41eb5ff74a69c72eced5463c6c76b032a418ff0be82e2bb0b4a16f3acf123b`.
Šíra .7z SHA256: `a4a68342b1e514d7611e6bd6a93d12a4afe5cc5531b92af5ae711a3eb233583e`, MD5 `e53319bb7d760122979e9b6c60395598` — matches published archive digest.

Original-size and destination readback verified for all seven. No new GitHub PDF binary copies: Drive owns original bytes. Full old-edition parity and empirical run-specific provenance are separate issues.
