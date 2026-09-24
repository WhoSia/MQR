# MQR-4.32 — Preseal Amendment A: Direct-Surface Independence

Status: PRE-REVEAL AMENDMENT / NO NATIVE DIRECT OUTCOME OPENED

Parent preseal:
a935fb38e50952cb6bf2ff7918ef52342ce5fb89

## Problem found by design attack

A nominal triangle can be circular if the B->C edge and the direct A->C adjudication are both computed from the same endpoint observation in a way that makes the direct verdict logically recoverable from the adjacent verdict.

In that case:
- the mediated prediction is not genuinely prospective relative to the direct test;
- direct validation can become a restatement of the data already used to establish B->C;
- PASS+PASS can appear compositional merely because C was consumed twice.

No MQR-4.32 native direct outcome has been opened at the time of this amendment.

## Additional confirmatory requirement

A confirmatory triangle must have a DIRECT-SURFACE-INDEPENDENCE receipt.

At least one of the following must hold:

1. HELDOUT_WORLD
   - B->C is established on one frozen world/fixture set;
   - A->C is adjudicated on an independently held-out world/fixture set under the same declared component law.

2. HELDOUT_COMPONENT
   - adjacent edges are established on a predeclared component subset;
   - direct A->C is adjudicated on a disjoint held-out component subset;
   - a presealed invariance rule licenses the family-level claim.

3. NONCOMMON_MEASUREMENT_ROUTE
   - adjacent and direct edges use materially noncommon measurement routes whose agreement/disagreement is itself testable.

4. SEALED_SELECTIVE_REVEAL
   - a trusted mechanical splitter reveals only the adjacent-edge receipt;
   - the direct A->C criterion remains cryptographically/structurally unrecoverable until the mediated prediction is sealed;
   - the adjacent receipt must not determine the direct verdict by logic alone.

## Forbidden pseudo-independence

The following do NOT suffice:
- hiding a JSON field while revealing another field that algebraically determines it;
- using the same C vector twice under two labels;
- aggregate B->C PASS when PASS definition uniquely determines every C component later called a direct test;
- renaming the same comparison as both adjacent and direct evidence.

## Additional machine field

Every confirmatory row/triangle must eventually carry:

direct_surface =
HELDOUT_WORLD |
HELDOUT_COMPONENT |
NONCOMMON_MEASUREMENT_ROUTE |
SEALED_SELECTIVE_REVEAL |
NOT_INDEPENDENT |
UNRESOLVED

Only the first four are confirmatory-admissible.

## Consequence for candidate search

Existing historical cases can still be diagnostic.

Fresh confirmation requires an actually independent direct surface. If no admissible corpus supplies this, MQR-4.32 closes with EXTERNAL_COMPOSITION_HOLD rather than weakening the rule.

## Verdict

DIRECT-SURFACE-INDEPENDENCE-REQUIRED /
SAME-ENDPOINT-DOUBLE-USE-FORBIDDEN /
NO-POST-REVEAL-REPAIR /
PARENT-PRESEAL-RETAINED.
