import MQR.PromotionCriterion

namespace MQR

structure ParetoMultiplicityWitness where
  aNondominated : Bool
  bNondominated : Bool
  uniqueDecision : Bool
  deriving DecidableEq, Repr

def paretoMultiplicityWitness : ParetoMultiplicityWitness :=
  { aNondominated := true, bNondominated := true, uniqueDecision := false }

theorem paretoNondominationDoesNotImplyUniquePromotion :
    paretoMultiplicityWitness.aNondominated = true ∧
    paretoMultiplicityWitness.bNondominated = true ∧
    paretoMultiplicityWitness.uniqueDecision = false := by decide

structure LocalVetoWitness where
  localVeto : Bool
  universalPriority : Bool
  deriving DecidableEq, Repr

def localVetoWitness : LocalVetoWitness :=
  { localVeto := true, universalPriority := false }

theorem localVetoDoesNotImplyUniversalPriority :
    localVetoWitness.localVeto = true ∧
    localVetoWitness.universalPriority = false := by decide

structure DominanceWitness where
  pairwiseDominance : Bool
  totalOrder : Bool
  deriving DecidableEq, Repr

def dominanceWitness : DominanceWitness :=
  { pairwiseDominance := true, totalOrder := false }

theorem pairwiseDominanceDoesNotImplyTotalOrder :
    dominanceWitness.pairwiseDominance = true ∧
    dominanceWitness.totalOrder = false := by decide

structure HorizonReversalWitness where
  shortPromote : Bool
  mediumPromote : Bool
  contradiction : Bool
  deriving DecidableEq, Repr

def horizonReversalWitness : HorizonReversalWitness :=
  { shortPromote := true, mediumPromote := false, contradiction := false }

theorem changingHorizonCanReverseLocalAdmissibility :
    horizonReversalWitness.shortPromote = true ∧
    horizonReversalWitness.mediumPromote = false ∧
    horizonReversalWitness.contradiction = false := by decide

structure DuplicateReasonWitness where
  nominalCount : Nat
  independentAncestryCount : Nat
  strongerByDuplication : Bool
  deriving DecidableEq, Repr

def duplicateReasonWitness : DuplicateReasonWitness :=
  { nominalCount := 3, independentAncestryCount := 1, strongerByDuplication := false }

theorem duplicateReasonsDoNotCreateIndependentWarrant :
    duplicateReasonWitness.nominalCount = 3 ∧
    duplicateReasonWitness.independentAncestryCount = 1 ∧
    duplicateReasonWitness.strongerByDuplication = false := by decide

#print axioms MQR.paretoNondominationDoesNotImplyUniquePromotion
#print axioms MQR.localVetoDoesNotImplyUniversalPriority
#print axioms MQR.pairwiseDominanceDoesNotImplyTotalOrder
#print axioms MQR.changingHorizonCanReverseLocalAdmissibility
#print axioms MQR.duplicateReasonsDoNotCreateIndependentWarrant

end MQR
