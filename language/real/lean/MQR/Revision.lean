import Std

namespace MQR

structure BurdenView where
  label : String
  q1 : Bool
  q2 : Bool
  deriving DecidableEq, Repr

def oldSameLabel : BurdenView :=
  { label := "A", q1 := true, q2 := false }

def newSameLabel : BurdenView :=
  { label := "A", q1 := true, q2 := true }

theorem sameLabelDoesNotGuaranteeSameDeclaredBurden :
    oldSameLabel.label = newSameLabel.label ∧
    oldSameLabel.q1 = newSameLabel.q1 ∧
    oldSameLabel.q2 ≠ newSameLabel.q2 := by
  decide

def oldAlias : BurdenView :=
  { label := "A", q1 := true, q2 := true }

def newAlias : BurdenView :=
  { label := "Z", q1 := true, q2 := true }

theorem differentLabelsCanPreserveDeclaredChallengeProfile :
    oldAlias.label ≠ newAlias.label ∧
    oldAlias.q1 = newAlias.q1 ∧
    oldAlias.q2 = newAlias.q2 := by
  decide

def refinementPreservesDebt
    (oldQ1 oldQ2 targetQ1 targetQ2 : Bool) : Bool :=
  (!oldQ1 || targetQ1) && (!oldQ2 || targetQ2)

theorem partialRefinementCannotDischargeFullDeclaredDebt :
    refinementPreservesDebt true true true false = false := by
  decide

theorem fullRefinementCanPreserveDeclaredDebt :
    refinementPreservesDebt true true true true = true := by
  decide

structure MergeDebtWitness where
  sourceDebtAncestryCount : Nat
  targetCarrierCount : Nat
  preservedSourceAncestryCount : Nat
  deriving DecidableEq, Repr

def mergeDebtWitness : MergeDebtWitness :=
  { sourceDebtAncestryCount := 2
    targetCarrierCount := 1
    preservedSourceAncestryCount := 2 }

theorem mergeCarrierCardinalityDoesNotCollapseSourceDebtAncestry :
    mergeDebtWitness.sourceDebtAncestryCount = 2 ∧
    mergeDebtWitness.targetCarrierCount = 1 ∧
    mergeDebtWitness.preservedSourceAncestryCount =
      mergeDebtWitness.sourceDebtAncestryCount := by
  decide

inductive RevisionKind where
  | exact
  | overlap
  deriving DecidableEq, Repr

structure EqualCountRevisionWitness where
  sourceBurdenCount : Nat
  targetBurdenCount : Nat
  relation : RevisionKind
  deriving DecidableEq, Repr

def exactEqualCount : EqualCountRevisionWitness :=
  { sourceBurdenCount := 1, targetBurdenCount := 1, relation := .exact }

def overlapEqualCount : EqualCountRevisionWitness :=
  { sourceBurdenCount := 1, targetBurdenCount := 1, relation := .overlap }

theorem equalBurdenCountsDoNotIdentifyCrossVersionRelation :
    exactEqualCount.sourceBurdenCount = overlapEqualCount.sourceBurdenCount ∧
    exactEqualCount.targetBurdenCount = overlapEqualCount.targetBurdenCount ∧
    exactEqualCount.relation ≠ overlapEqualCount.relation := by
  decide

inductive PathStrength where
  | complete
  | limited
  | absent
  deriving DecidableEq, Repr

def directRevisionStrength : PathStrength := .limited
def composedRevisionStrength : PathStrength := .complete

theorem directAndComposedRevisionPathsCanDisagree :
    directRevisionStrength ≠ composedRevisionStrength := by
  decide

structure ComparabilityWitness where
  mappedSourceBurdenCount : Nat
  totalSourceBurdenCount : Nat
  wholeOntologyIdentity : Bool
  deriving DecidableEq, Repr

def partialComparabilityWitness : ComparabilityWitness :=
  { mappedSourceBurdenCount := 1
    totalSourceBurdenCount := 2
    wholeOntologyIdentity := false }

theorem mappedSubspaceComparabilityDoesNotImplyWholeOntologyIdentity :
    partialComparabilityWitness.mappedSourceBurdenCount <
      partialComparabilityWitness.totalSourceBurdenCount ∧
    partialComparabilityWitness.wholeOntologyIdentity = false := by
  decide

structure RevisionClosureWitness where
  currentTransportPass : Bool
  futureRevisionClosed : Bool
  deriving DecidableEq, Repr

def revisionClosureWitness : RevisionClosureWitness :=
  { currentTransportPass := true, futureRevisionClosed := false }

theorem finiteRevisionTransportDoesNotImplyFutureRevisionClosure :
    revisionClosureWitness.currentTransportPass = true ∧
    revisionClosureWitness.futureRevisionClosed = false := by
  decide

structure ConflictBoundaryWitness where
  conflictLocalized : Bool
  trueWinnerIdentified : Bool
  deriving DecidableEq, Repr

def conflictBoundaryWitness : ConflictBoundaryWitness :=
  { conflictLocalized := true, trueWinnerIdentified := false }

theorem conflictLocalizationDoesNotIdentifyTrueWinner :
    conflictBoundaryWitness.conflictLocalized = true ∧
    conflictBoundaryWitness.trueWinnerIdentified = false := by
  decide

#print axioms MQR.sameLabelDoesNotGuaranteeSameDeclaredBurden
#print axioms MQR.differentLabelsCanPreserveDeclaredChallengeProfile
#print axioms MQR.partialRefinementCannotDischargeFullDeclaredDebt
#print axioms MQR.fullRefinementCanPreserveDeclaredDebt
#print axioms MQR.mergeCarrierCardinalityDoesNotCollapseSourceDebtAncestry
#print axioms MQR.equalBurdenCountsDoNotIdentifyCrossVersionRelation
#print axioms MQR.directAndComposedRevisionPathsCanDisagree
#print axioms MQR.mappedSubspaceComparabilityDoesNotImplyWholeOntologyIdentity
#print axioms MQR.finiteRevisionTransportDoesNotImplyFutureRevisionClosure
#print axioms MQR.conflictLocalizationDoesNotIdentifyTrueWinner

end MQR
