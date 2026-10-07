# MQR-4.86 — Noninvertible Obligation Transport
Status: EXECUTABLE ATTACK / NO SCIENTIFIC CLOSURE

## Origin
Scientific authority must not increase merely because an annotation is erased. Prior 4.86 signature equality is a deliberately weak prototype, not authority semantics.

## State
For a single obligation, state is (live, discharged, receipts, lost). Each coordinate is a set of obligation IDs. A legitimate transition conserves ownership: initial = live disjoint-union discharged; every discharge must carry a verified independent receipt. No operation may silently erase an obligation. Reopening moves one ID from discharged to live and invalidates its prior discharge authorization, while retaining history in the trace.

## Operations
KEEP retains the state. DISCHARGE(id, valid_receipt) moves id from live to discharged if a valid receipt exists. ERASE(id) deletes live id without a receipt. REOPEN(id) restores id to live from discharged (with history). SELECT picks one path, but without independent selection authority cannot turn a bad path into a good one.

## Two-path diamond
Initial live={a}. Left KEEP then DISCHARGE(a, verified receipt) -> live={} and discharged={a}. Right ERASE(a) then KEEP -> live={} and discharged={}. They have identical visible 'live obligations' projection yet differing authority. The right path violates conservation. A legitimate no-erasure path and an illegal erasure path may have the same final relation and same visible debt projection.

## Proposition 4.86-D (conservation soundness)
For any finite sequence built from KEEP, DISCHARGE with a valid receipt, and REOPEN retaining history, initial obligations partition into currently live and historically accounted-for discharged obligations, with every discharged ID supported by its receipt. Proof by induction on trace length. An ERASE step with an unaccounted live ID falsifies conservation. This is a standard state-invariant theorem; novelty is not claimed for induction or accounting.

## Falsifier
If a scientific implementation judges the two paths identically from their final projected relation and visible live set, it cannot enforce the stated debt authority constitution.

## Caveats
This toy uses stipulated receipt validity and assumes distinct obligation identities. It does not establish a nontrivial theorem for actual science. The next challenge is whether different independently evidenced discharge mechanisms and competing scope authorities admit a nontrivial, compositional criterion stronger than ordinary audit ledgers. Comparison with provenance semirings and event-sourced ledgers remains required.
