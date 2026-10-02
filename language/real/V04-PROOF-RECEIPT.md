# Real-Language v0.4 — Canonical Proof-Boundary Receipt

Status: KERNEL PASS / TARGET-CLOSURE INDEPENDENT RECHECK PASS / WORLD-TRUTH LAUNDERING FORBIDDEN

## Canonical run

GitHub Actions run:
`36146576232`

Evidence head:
`65e1932ea48c013d59384c8b2f7e1d778865c061`

Conclusion:
SUCCESS.

## Pinned formal environment

Lean toolchain:
`leanprover/lean4:v4.34.0`

lean-action:
`38fbc41a8c28c4cbaec22d7f7de508ec2e7c0dd9`

lean4export:
`076e8e57707e813375e8f9da8bf989799ace9680`

nanoda_lib:
`68d5ca9db226849b41a6fff59d796ff19d0a8840`

The proof receipt is version-indexed. A later Lean/checker release does not silently replace this receipt.

## Target theorems

Only the transitive closure of these MQR theorems was exported to the independent checker:

- `MQR.zeroInternalResidueOfComplete`
- `MQR.extensionContainsUncoveredProbe`
- `MQR.checkedProofCannotRaiseHoldToPass`

The independent nanoda configuration used:

```text
permitted_axioms = []
unpermitted_axiom_hard_error = true
```

## Kernel result

Lean reported for all three targets:

```text
does not depend on any axioms
```

and:

```text
REAL_LANGUAGE_V04_LEAN_KERNEL=PASS
REAL_LANGUAGE_V04_AXIOM_ANCESTRY=EMPTY
```

## Independent checker result

The pinned lean4export emitted only the target theorem closure.

Pinned nanoda independently accepted the resulting environment.

Machine receipt:

```text
REAL_LANGUAGE_V04_NANODA_INDEPENDENT_CHECKER=PASS
LEAN_PROOF_IS_NOT_WORLD_VERIFICATION=TRUE
```

## Failed precursor receipts

Several earlier proof-CI attempts are retained in GitHub Actions history.

They are noncanonical infrastructure diagnostics, not failed theorems.

Two especially informative failures were:

1. mutable/latest checker stack against Lean 4.34.1:
   export parser failure (`invalid digit found in string`);

2. whole-module independent export:
   unrelated environment primitive `Lean.ofReduceNat` entered the export and was correctly rejected by the empty/strict axiom policy.

The canonical repair did not add an axiom exception.

It narrowed the independent replay to the preregistered theorem closure.

## Scientific meaning

The receipt establishes:

```text
FORMAL_DERIVABILITY_OF_TARGET_THEOREMS = CHECKED
TARGET_THEOREM_AXIOM_ANCESTRY = EMPTY
INDEPENDENT_FORMAL_RECHECK = PASS
```

It does not establish:

```text
WORLD |= empirical premises
WORLD |= declared probe class is complete
OPEN_WORLD_RESIDUE = ZERO
```

Therefore:

```text
KERNEL_VERIFIED != WORLD_VERIFIED
FORMAL_CERTAINTY_CANNOT_LAUNDER_EMPIRICAL_UNCERTAINTY
```

## Real-Language consequence

v0.4 now has an executable proof-boundary lane with:

- Rust premise/authority compiler;
- negative axiom-laundering regression;
- Lean kernel receipt;
- explicit theorem axiom ancestry;
- materially separate nanoda recheck;
- finite-probe residue theorem;
- explicit open-world claim ceiling.

This is sufficient to make the v0.4 proof lane **LIVE**, while v0.3 typed transport remains readable and regression-tested for historical/canonical compatibility.

It does not make Real-Language a theorem prover or truth oracle.
