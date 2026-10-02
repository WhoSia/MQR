# MQR-4.66 — Quotient Grammar Freeze

Status: **FROZEN / POST-LITERATURE / PRE-EXECUTABLE-REVEAL**

PRESEAL:
`54b24be19c7bd9b4e36bd07dfa178066830c6bfc`

LITERATURE boundary:
`00b11ac36827ce7e36b446ee7ebcc5090bca8996`

No state bit, event, output label, quotient definition, refinement rule, history horizon, witness criterion, or verdict threshold may change after first executable reveal.

## 1. Finite source state

The source state is a 9-bit tuple:

`(R0,R1,R2,S0,S1,S2,C,P,X)`

where:

- `Ri`: rival `i` is currently live;
- `Si`: a currently retained separator for rival `i` is available;
- `C`: current evidence ancestry is treated as independent for authority;
- `P`: provenance-root state that an `AUDIT` event will expose into `C`;
- `X`: an exterior route capable of producing a novelty event is live.

There are exactly:

`2^9 = 512`

source states.

This is a finite synthetic authority machine. It is **not** asserted to be a complete model of science.

## 2. Derived current authority label

Define:

`U = popcount(R & ~S)`

for the number of currently live rivals lacking a retained separator.

Current action alphabet:

- `HOLD` — always feasible;
- `COMMIT` — feasible iff `U=0 ∧ C=1`;
- `REOPEN` — feasible iff `U>0 ∨ C=0`;
- `PROBE` — always feasible.

Current release state:

`RELEASE = (U=0 ∧ C=1)`.

Frozen current label:

`LABEL(s) = (U, feasible_action_mask, RELEASE)`.

Important:
- `P` and `X` do **not** appear directly in the current label;
- they can matter under future events.

This is deliberate and frozen before reveal.

## 3. Frozen event alphabet

Exactly 18 deterministic events:

### Rival admission/removal
- `R0+`, `R1+`, `R2+`
- `R0-`, `R1-`, `R2-`

These set/clear the corresponding rival-live bit.

### Separator acquisition/loss
- `S0+`, `S1+`, `S2+`
- `S0-`, `S1-`, `S2-`

These set/clear the corresponding separator bit.

### Provenance-root mutation
- `P+` — set `P=1`
- `P-` — set `P=0`

### Provenance audit
- `AUDIT` — set `C := P`

### Exterior-route mutation
- `X+` — set `X=1`
- `X-` — set `X=0`

### Novelty admission
- `NOVELTY`:
  - if `X=1`, set `R2=1` and `S2=0`;
  - if `X=0`, leave the state unchanged.

No event is added or removed after reveal.

## 4. History surface

Initial state:

`000000000`.

Enumerate every event history of length 0 through 4.

History count:

`Σ_{k=0..4} 18^k = 111,151`.

For each history:
- replay from the initial state;
- record the reached 9-bit source state;
- record Q0/Q1/Q2/Q3/Q4 quotient block IDs.

The history surface is used for:
- bounded compression ratio;
- duplicate-history collapse;
- minimal concrete aliasing witnesses.

It is **not** used to infer unrestricted open-world coverage.

## 5. Candidate quotients

### Q0 — UNRESOLVED-COUNT
Merge source states by `U` only.

### Q1 — CURRENT-AUTHORITY
Merge by exact frozen `LABEL(s)`.

### Q2 — ONE-STEP AUTHORITY
Start from Q1 and refine each state by:
- its Q1 block;
- the Q1 block reached under each of the 18 events.

### Q3 — THREE-STEP AUTHORITY
Starting from Q1, apply exactly three rounds of transition-signature refinement.

The label “THREE-STEP” refers to three refinement rounds on this deterministic machine; it is not an unrestricted future-equivalence theorem.

### Q4 — STABLE AUTHORITY PARTITION
Starting from Q1, repeatedly refine by current block + ordered vector of successor block IDs under all 18 events until the partition stops changing.

Q4 is the finite coinductive/stable target.

## 6. Frozen naive quotient attacks

### N1 — VISIBLE-ONLY
Signature:
`(R0,R1,R2,S0,S1,S2,C)`.

It intentionally drops:
- `P`;
- `X`.

Attack goals:
- find a pair merged by N1 but separated by `AUDIT`;
- find a pair merged by N1 but separated by `NOVELTY`.

### N2 — CURRENT-AUTHORITY
Same as Q1.

Attack goal:
find the shortest event continuation that distinguishes any merged pair if such a pair exists.

### N3 — THREE-ROUND
Same as Q3.

Attack goal:
test whether Q3 has stabilized; if not, produce a pair merged by Q3 but separated by further continuation.

No stronger/weaker naive quotient may be substituted after reveal.

## 7. Exact soundness criterion on this finite machine

A quotient is **finite-authority-sound** iff:

1. states in one block have identical current labels;
2. for every event, successor states of states in one block land in the same quotient block.

On a deterministic labeled transition system, these two conditions imply preservation of the entire future label trace language under arbitrary finite event continuations.

This implication will be the Lean theorem boundary.

It does **not** establish that the label contract is scientifically complete.

## 8. Minimal aliasing witness

For a candidate quotient `Q`, a witness is:

`(s,t,w)`

where:
- `s≠t`;
- `Q(s)=Q(t)`;
- `w` is a finite event word;
- the label reached from `s` after `w` differs from the label reached from `t` after `w`.

A witness is **length-minimal** if no shorter continuation separates that pair.

The Prolog lane searches relationally for witnesses of N1/N2/N3.

The Haskell/C++ lanes independently verify reported witness validity.

## 9. Dynamic schema-reopening interpretation

The `X` bit is not current authority; it is a frozen proxy for whether a novelty route exists.

Two states that differ only in `X` can look identical under current authority but react differently to `NOVELTY`.

If a quotient merges them and therefore fails to preserve the future label trace, this is classified:

**OPEN_FRONTIER_SCHEMA_ALIASING**.

This is a finite synthetic witness only.

## 10. Provenance interpretation

The `P` bit is not current authority; it is a frozen provenance-root condition revealed by `AUDIT`.

If a quotient drops `P`, states may be currently identical but diverge after `AUDIT`.

Such failure is classified:

**PROVENANCE_ALIASING**.

Again, this is a finite synthetic witness, not a claim about all scientific provenance systems.

## 11. Frozen measurements

Record:

- number of Q0 blocks;
- number of Q1 blocks;
- number of Q2 blocks;
- number of Q3 blocks;
- number of Q4 blocks;
- refinement rounds to stability;
- Q4 compression ratio from 512 source states;
- Q4 compression ratio from 111,151 bounded histories;
- number of N1 merged pairs;
- shortest N1 provenance witness length;
- shortest N1 novelty witness length;
- whether Q3=Q4;
- runtime for Haskell canonical and C++ independent implementation.

No target block count is predeclared.

## 12. Multi-language qualification

### Haskell canonical
Must:
- implement the exact 512-state machine;
- implement Q0–Q4;
- enumerate the 111,151 histories;
- emit canonical sorted state→Q4 block mapping and summary.

### Prolog adversary
Must:
- independently encode the frozen event relation and label relation;
- produce an N1 provenance alias witness;
- produce an N1 novelty alias witness;
- search N2/N3 for shortest separating continuations up to a frozen safety bound of length 8;
- report no witness only as bounded-no-witness unless soundness follows from Q4 mapping supplied separately.

### C++ independent census
Must independently implement:
- state transitions;
- labels;
- Q0–Q4 refinement;
- history enumeration;
- summary counts;
- Q4 canonical partition signature.

It may not parse Haskell output to compute its own result.

### Lean 4 proof boundary
Must prove, for an abstract deterministic labeled transition system:
- label equality inside an equivalence class;
- transition congruence under each event;
imply equality of labels after every finite event word.

Lean does not prove that 4.66's scientific labels are world-complete.

## 13. Frozen verdict logic

### NONTRIVIAL_SOUND_QUOTIENT
Q4 has fewer than 512 blocks and passes Haskell/C++ concordance + Lean preservation boundary.

### COARSEST_SOUND_FINITE_QUOTIENT
Additionally, the stable refinement construction is independently concordant and every pair of distinct Q4 blocks differs in label or successor-block signature.

This verdict is only for the frozen 512-state machine.

### TRIVIAL_FULL_STATE_ONLY
Q4 has exactly 512 blocks.

### DYNAMIC_REFINEMENT_RECOVERS
A weaker quotient aliases states but Q4 separates the witness.

### MINIMALITY_UNPROVED
Used if implementation concordance or distinguishing-block audit fails.

## 14. Anti-inflation guard

Even if Q4 is dramatically smaller than 512 or 111,151 histories, 4.66 may not call that a new general theory of sufficient scientific state.

Even if N1/Q1/Q3 fail, 4.66 may not infer that ordinary state-abstraction theory fails.

The only eligible MQR-specific interpretation concerns the chosen scientific-authority preservation contract and its reopening/provenance obligations.
