# MQR-4.71 — Three-Layer Contact Topology Constitution

Status: **PRESEALED / CANDIDATE-SCIENTIFIC-EXECUTION LAYERS SEPARATED / NONMONOTONE-REVISION-OPEN**

## Core objects

At time t define:

- C_t — generator-produced candidate contacts;
- S_t subseteq C_t — scientifically relevant/discriminating contacts under the declared scientific scope;
- X_t subseteq S_t — currently executable/permitted/resource-admissible contacts.

Canonical inclusion:

    X_t subseteq S_t subseteq C_t

## Distinct closure questions

1. Candidate-generator closure: is C_t complete relative to the declared generator scope?
2. Scientific-relevance closure: does S_t contain every scientifically relevant contact within the declared scientific scope?
3. Execution closure: does X_t contain every currently executable contact within the declared technology/permission/resource state?

No implication from a lower layer to a higher layer is automatic.

## Frozen transitions

### Generator expansion
Changes C_t directly. Example: rival/instrument/anomaly generator introduces a new candidate.

### Scientific reclassification
Changes S_t within C_t. A candidate may become scientifically relevant after a rival, anomaly or semantics update without becoming executable.

### Execution unlock
Changes X_t within S_t through technology, permission or resource change.

### Execution restriction
Can shrink X_t without changing S_t, for example due to safety, ethics, law or resource loss.

### Scientific retirement
Can shrink S_t without requiring an execution change if a candidate is shown irrelevant/redundant under an independently warranted scientific scope.

## Frozen nonimplications

    X-CLOSED does not imply S-CLOSED
    S-CLOSED does not imply C-CLOSED
    X-EXPANSION does not imply S-EXPANSION
    S-EXPANSION does not imply C-EXPANSION
    C-EXPANSION does not imply S-EXPANSION

## Nonmonotonicity

Execution envelopes need not expand monotonically:
- technology can add contacts;
- ethics/legal/safety revision can remove contacts;
- resources can expand or contract.

Scientific-relevance envelopes also need not be monotone:
- new rivals can add relevance;
- redundancy/semantic collapse can remove relevance.

## Frozen witness requirements

1. Candidate-only contact: q in C but not S.
2. Scientific-but-blocked contact: q in S but not X.
3. Executable scientific contact: q in X.
4. Technology unlock: S unchanged, X expands.
5. Ethics restriction: S unchanged, X contracts.
6. Rival arrival: C or S expands while X may remain unchanged.
7. Candidate expansion with scientific null: C expands while S and X remain unchanged.

## Claim ceiling

This topology is bookkeeping unless it yields distinct audit/closure consequences.

It is not a new lattice theory and receives no novelty credit merely for set inclusion.