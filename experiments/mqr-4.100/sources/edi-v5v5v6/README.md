# Original EDI v5/v5/v6 reproducibility fixtures

These are exact untouched ZIP bytes downloaded on 2026-10-09 from the EDI Data Portal's **Full Data Package (Zip)** by the user via the normal authenticated sign-in. The underlying EDI datasets are openly licensed under **CC0 1.0** per their package metadata; attribution is retained for scientific provenance even where not legally required.

- `knb-lter-pal.219.5.zip` / Adélie — DOI https://doi.org/10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f, SHA-256 `29771c188cb1274b30f3d356716a3eadfed0954c55bbe5675cb49b10d26c79bd`.
- `knb-lter-pal.220.5.zip` / Gentoo — DOI https://doi.org/10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689, SHA-256 `7d141b10500a849c9de7f36c175f424ff929aa951100c0e5c62d50313186ddb9`.
- `knb-lter-pal.221.6.zip` / Chinstrap — DOI https://doi.org/10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e, SHA-256 `c83097abfda2489386eedae03e8f3dd8835f655463bd6caf173c2ae271b50b0e`.

Each ZIP contains its EDI data CSV, EML package metadata XML, EDI text metadata, quality report XML and original download manifest, without any user session tokens or login credentials. This is a **snapshot/mirror** for public reproducibility, not an officially issued EDI signature or a new collection.

Compare with the pinned 2024 `palmerpenguins` combined CSV at `https://raw.githubusercontent.com/allisonhorst/palmerpenguins/8957207b78d6ccd1b4654a9dd9c9041b657478ab/inst/extdata/penguins_raw.csv` (SHA-256 `144f623143c9360fd77322a4f86acb06dc198814dbd2669724c63e6457b907bd`), using `experiments/mqr-4.100/p6_edi_reconcile.py`.

Not a new biological measurement, independent data collection or source-to-target ecological identification result. Full unmodified original ZIPs and forensic receipts are preserved in Google Drive MQR `01_SOURCE_ACCRUAL_RAW`.
