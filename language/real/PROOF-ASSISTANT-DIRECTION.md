# Real-Language — Proof-Assistant Direction after MQR-4.36

Status: DIRECTIONAL CONSTITUTION / V0.4 PROOF LANE

## 1. Direction

Real-Language is not becoming a theorem prover.

Its role is to become the **typed boundary language between world contact and theorem proving**.

Target architecture:

```text
WORLD
  -> instrument / intervention / provider
  -> native evidence
  -> typed empirical receipt
  -> Real-Language premise + authority state
  -> formal obligation
  -> Lean proof term
  -> kernel / independent checker
  -> scoped consequence
```

The proof assistant certifies derivability inside the formal region.

Real-Language preserves the authority/provenance boundary that tells us what the formal region is allowed to mean scientifically.

## 2. Why Lean cannot replace MQR

A theorem prover can certify:

```text
Gamma |- phi
```

It cannot, merely by checking the proof term, establish:

```text
World |= Gamma
```

when Gamma contains empirical or model premises.

Therefore the MQR origin remains load-bearing:

```text
Nature
 -> Physical Oracle
 -> Bits / Representation
 -> Logical Processor
```

Lean belongs principally to the logical-processor side.

It may verify the post-representation compiler and inference.

It does not become the physical oracle.

## 3. Real-Language v0.4 objects

### Premise

Every premise has:
- identity;
- kind: FORMAL / DEFINITION / MODEL / EMPIRICAL;
- authority state: PASS / HOLD / FAIL;
- provenance text.

### Obligation

Every obligation has:
- identity;
- boundary: FORMAL_ONLY / WORLD_DEPENDENT;
- explicit dependency set;
- proof status;
- proof receipt;
- requested empirical authority when world-dependent.

### Proof boundary

A WORLD_DEPENDENT obligation inherits an empirical ceiling equal to the weakest world-facing premise in its ancestry.

Kernel checking cannot raise the ceiling.

### Probe class

A finite probe class records:
- declared bound;
- declared scope;
- internal residue state;
- enumeration/receipt pointer.

It is forbidden to infer universal world closure from a zero-internal-residue certificate.

## 4. Theorem-prover integration levels

### L0 — syntax only

Real-Language stores a proof pointer without checking it.

Authority:
no formal promotion.

### L1 — kernel checked

A Lean proof term is accepted by the pinned kernel.

Authority:
formal validity for the stated formal proposition.

### L2 — independently rechecked

The compiled environment/proof object is checked by a materially independent checker such as nanoda when supported.

Authority:
stronger software/proof custody, not stronger empirical truth.

### L3 — explicit axiom ancestry

Every theorem's non-definitional assumptions are surfaced and mapped back to Real-Language premise identities.

Authority:
formal consequence can be audited against empirical/model ancestry.

### L4 — proof-carrying empirical receipt

Machine evidence, Real-Language packet and checked theorem are cryptographically/provenance-bound into one receipt.

Authority:
a durable audit object whose empirical scope remains exactly the scope of its world-facing premises.

No level licenses final metaphysical truth.

## 5. Proof-Carrying Realist Authority

PCRA is the working architecture:

```text
PCRA =
  WORLD_RECEIPT
  + TYPED_PREMISE_AUTHORITY
  + FORMAL_DEPENDENCY_GRAPH
  + KERNEL_CHECK
  + INDEPENDENT_RECHECK_WHEN_AVAILABLE
  + OPEN_WORLD_RESIDUE
```

The authority of the conclusion is not the maximum confidence of the parts.

For world-dependent claims it is bounded above by the weakest load-bearing empirical/model premise.

## 6. Negative constitutional rules

Real-Language must reject:

1. **Axiom laundering**
   - empirical HOLD premise;
   - checked theorem depends on it;
   - packet requests empirical PASS.

2. **Boundary laundering**
   - WORLD_DEPENDENT obligation declared FORMAL_ONLY while depending on empirical/model premise.

3. **Residue laundering**
   - internal zero residue presented as open-world zero residue.

4. **Proof-pointer laundering**
   - arbitrary text path or theorem name treated as CHECKED without a checker receipt in a promoted packet.

5. **Model laundering**
   - kernel correctness of the encoded model treated as evidence that the encoded model is adequate to the target world.

6. **Receipt reification**
   - immutable receipt interpreted as final ontology.

## 7. UV–Vis return

The earliest MQR question asked whether an instrument's scientific result could be compiled toward logical structure.

Real-Language + Lean now provide a sharper answer.

For a UV–Vis-style chain:

```text
sample
 -> photon interaction
 -> detector
 -> ADC bits
 -> baseline/calibration transform
 -> absorbance representation
 -> scientific constraint
```

a proof assistant can in principle verify:
- arithmetic transformations;
- declared calibration equations;
- bounded properties of an inference algorithm;
- logical consequences of explicit measurement assumptions.

It cannot verify by theoremhood alone:
- that the detector coupled to every relevant physical distinction;
- that the calibration model is adequate outside tested support;
- that two physically distinct realizers do not remain measurement-equivalent;
- that the chosen observation vocabulary exhausts future science.

That is the permanent MQR/Lean division of labor.

## 8. Development direction

Near-term:
- v0.3 remains the canonical transport-capable historical/compiler lane;
- v0.4 proof lane remains explicit and separately routed;
- Rust remains the canonical Real-Language compiler;
- Lean is the first formal backend;
- independent proof rechecking is preferred where practical;
- Python may remain an independent audit/reference surface rather than canonical authority.

Before v0.4 becomes the single default grammar, require:
- stable proof-boundary CI;
- negative laundering regression;
- explicit proof/axiom ancestry;
- at least one real MQR packet bound to a world-contact receipt;
- no regression of v0.3 typed transport.

## 9. Claim ceiling

Real-Language may become increasingly proof-carrying.

It must never silently become:
- a truth oracle;
- a metaphysical closure engine;
- a substitute for measurement;
- a substitute for model criticism;
- a mechanism for deleting open-world residue.

The desired endpoint is not:

```text
SCIENCE = THEOREMS
```

but:

```text
SCIENTIFIC AUTHORITY =
  WORLD CONTACT
  + EXPLICIT REPRESENTATION
  + CHECKED INFERENCE
  + REACHABLE DEFEAT
```.
