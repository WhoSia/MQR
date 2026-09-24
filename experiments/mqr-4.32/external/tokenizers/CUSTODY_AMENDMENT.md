# MQR-4.32 TKN-001 — Canonical Evidence-Custody Amendment

Status: PRE-DIRECT-REVEAL / SEMANTICS UNCHANGED / CUSTODY-ONLY AMENDMENT

## Reason

The TKN-001 scientific preseal remains unchanged:

- regimes A/B/C = tokenizers 0.21.4 / 0.22.2 / 0.23.2;
- bridge fixtures = B01..B06;
- held-out direct fixtures = H01..H06;
- adjacent PASS criterion = byte-identical canonical output on all bridge fixtures;
- mediated prediction rule remains conditional on adjacent A->B and B->C states;
- direct A->C execution remains forbidden until a mediated seal is committed.

After the candidate manifest was frozen, the probe required cross-version API compatibility repairs before a canonical execution could be relied on. Those repairs change only the wrapper used to instantiate the already frozen WordLevel + Whitespace behavior; they do not change versions, vocabulary, fixtures, observable output, edge criterion, or prediction rule.

## Canonicalization rule

Any TKN-001 bridge execution before this amendment is NONCANONICAL for MQR-4.32, regardless of whether it failed, succeeded, or produced an artifact.

The next successful bridge execution from the current main lineage is the only canonical adjacent-edge execution.

Its adjudication must be written back to:

receipts/mqr-4.32/tokenizers-bridge.tsv

with the triggering Git SHA recorded alongside the two adjacent states.

This persistence change is evidence custody only. It does not alter any scientific admission or promotion rule.

## Direct-reveal lock

The held-out H01..H06 direct surface remains unopened.

No direct A->C workflow may be added until:

1. the canonical bridge receipt exists in Git;
2. A->B and B->C states are read from that receipt;
3. COMPOSITION_CANDIDATE yes/no and the mediated A->C prediction are committed.

## Verdict

PRE-DIRECT-REVEAL /
CUSTODY-AMENDMENT-ONLY /
PRESEAL-SEMANTICS-UNCHANGED /
EARLIER-BRIDGE-RUNS-NONCANONICAL /
NEXT-SUCCESSFUL-BRIDGE-WRITEBACK-CANONICAL.
