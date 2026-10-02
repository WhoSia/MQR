import Std

namespace MQR

def testedSmall (_ : Fin 1) : Bool := true

def testedLarge (p : Fin 2) : Bool := p.val == 0

theorem smallClosedLargeOpen :
    (∀ p : Fin 1, testedSmall p = true) ∧
      (∃ p : Fin 2, testedLarge p = false) := by
  constructor
  · intro p
    rfl
  · exact ⟨⟨1, by decide⟩, by decide⟩

structure ReceiptAncestry where
  surfacePremise : String
  measurementPass : Bool
  calibrationPass : Bool
  deriving DecidableEq, Repr

def ancestryA : ReceiptAncestry :=
  { surfacePremise := "P_EMPIRICAL_PASS"
    measurementPass := true
    calibrationPass := true }

def ancestryB : ReceiptAncestry :=
  { surfacePremise := "P_EMPIRICAL_PASS"
    measurementPass := true
    calibrationPass := false }

def ancestryWorldPass (a : ReceiptAncestry) : Bool :=
  a.measurementPass && a.calibrationPass

theorem receiptCompressionLosesLoadBearingDistinction :
    ancestryA.surfacePremise = ancestryB.surfacePremise ∧
      ancestryWorldPass ancestryA = true ∧
      ancestryWorldPass ancestryB = false := by
  decide

structure FrontierState where
  formalSteps : Nat
  worldAdequacySupported : Bool
  deriving DecidableEq, Repr

def frontierBefore : FrontierState :=
  { formalSteps := 1, worldAdequacySupported := false }

def frontierAfter : FrontierState :=
  { formalSteps := 4, worldAdequacySupported := false }

theorem formalExpansionDoesNotEstablishWorldAdequacy :
    frontierAfter.formalSteps > frontierBefore.formalSteps ∧
      frontierAfter.worldAdequacySupported =
        frontierBefore.worldAdequacySupported := by
  decide

structure IndependenceVector where
  statement : Bool
  compiler : Bool
  kernelA : Bool
  kernelB : Bool
  world : Bool
  deriving DecidableEq, Repr

def sharedBadEncoding : IndependenceVector :=
  { statement := false
    compiler := true
    kernelA := true
    kernelB := true
    world := false }

def checkerPluralityPass (i : IndependenceVector) : Bool :=
  i.kernelA && i.kernelB

def authorityTransferPass (i : IndependenceVector) : Bool :=
  i.statement && i.compiler && i.kernelA && i.world

theorem checkerPluralityDoesNotEntailAuthorityTransfer :
    checkerPluralityPass sharedBadEncoding = true ∧
      authorityTransferPass sharedBadEncoding = false := by
  decide

structure TruthCandidate where
  formalCustody : Nat
  worldAlignmentSupported : Bool
  deriving DecidableEq, Repr

def formallyStronger : TruthCandidate :=
  { formalCustody := 4, worldAlignmentSupported := false }

def formallyWeaker : TruthCandidate :=
  { formalCustody := 1, worldAlignmentSupported := true }

theorem formalCustodyDoesNotIdentifyTruthOrder :
    formallyStronger.formalCustody > formallyWeaker.formalCustody ∧
      formallyStronger.worldAlignmentSupported = false ∧
      formallyWeaker.worldAlignmentSupported = true := by
  decide

#print axioms MQR.smallClosedLargeOpen
#print axioms MQR.receiptCompressionLosesLoadBearingDistinction
#print axioms MQR.formalExpansionDoesNotEstablishWorldAdequacy
#print axioms MQR.checkerPluralityDoesNotEntailAuthorityTransfer
#print axioms MQR.formalCustodyDoesNotIdentifyTruthOrder

end MQR
