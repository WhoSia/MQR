# Real-Language v0.4 — Proof-Boundary Preseal

Status: PRESEALED / FORMAL-EMPIRICAL SEPARATION

## Direction

Real-Language v0.4 explores proof-assistant integration.

The proof assistant is not a truth oracle.

Lean may certify:

```text
premises |- proposition
```

inside a formal system.

It does not by itself certify:

```text
the empirical premises are true of the world.
```

## New conceptual split

Every proof-bearing packet distinguishes:

- FORMAL_VALIDITY — derivability/type-checking status;
- EMPIRICAL_ENTITLEMENT — receipt-backed status of world-facing premises;
- PROOF_BOUNDARY — which claims are formal, empirical, mixed, or unresolved;
- AXIOM_ANCESTRY — explicit list of assumptions not discharged by the kernel.

No formal proof may raise an empirical gate from HOLD/FAIL to PASS.

## Planned v0.4 constructs

Provisional syntax:

```text
premise <id> <FORMAL|EMPIRICAL|MODEL|DEFINITION> <PASS|HOLD|FAIL> "text"
obligation <id> <FORMAL_ONLY|WORLD_DEPENDENT> "proposition"
depends <obligation-id> <premise-id>...
proof <obligation-id> <CHECKED|UNCHECKED|REFUTED|NOT_APPLICABLE> "checker/receipt"
probe_class <id> FINITE <bound> "scope"
residue <probe-class-id> <ZERO_INTERNAL|NONZERO|UNRESOLVED> "receipt"
```

Exact grammar may change only before first v0.4 behavioral fixture.

## Authority rule

A checked WORLD_DEPENDENT obligation receives no more authority than the weakest empirical/model premise on which it depends.

```text
FORMAL_CERTAINTY_CANNOT_LAUNDER_EMPIRICAL_UNCERTAINTY
```

## Lean bridge target

The first Lean bridge should prove only bounded structural statements such as:

- complete enumeration of a declared finite probe class implies zero untested residue inside that class;
- zero internal residue does not imply universal/open-world closure;
- authority propagation is monotone downward with respect to premise status.

No Lean theorem in v0.4 may assert an unmeasured world fact.

## Negative fixture

A packet that marks an EMPIRICAL HOLD premise, proves a dependent theorem in Lean, and then promotes empirical authority to PASS must be rejected mechanically.
