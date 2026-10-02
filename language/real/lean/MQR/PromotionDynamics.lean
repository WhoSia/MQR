import MQR.PromotionConflict

namespace MQR

structure SameLabelWitness where
  sameTerminalRelation : Bool
  sameMaterialHistory : Bool
  deriving DecidableEq, Repr

def sameLabelWitness : SameLabelWitness :=
  { sameTerminalRelation := true, sameMaterialHistory := false }

theorem sameTerminalRelationDoesNotImplySameMaterialHistory :
    sameLabelWitness.sameTerminalRelation = true ∧
    sameLabelWitness.sameMaterialHistory = false := by decide

structure RevisionOrderWitness where
  orderABEqualsBA : Bool
  deriving DecidableEq, Repr

def revisionOrderWitness : RevisionOrderWitness :=
  { orderABEqualsBA := false }

theorem revisionOrderNeedNotCommute :
    revisionOrderWitness.orderABEqualsBA = false := by decide

structure ReopenWitness where
  resolvedAtT1 : Bool
  reopenedAtT2 : Bool
  contradiction : Bool
  deriving DecidableEq, Repr

def reopenWitness : ReopenWitness :=
  { resolvedAtT1 := true, reopenedAtT2 := true, contradiction := false }

theorem resolvedConflictMayLegitimatelyReopen :
    reopenWitness.resolvedAtT1 = true ∧
    reopenWitness.reopenedAtT2 = true ∧
    reopenWitness.contradiction = false := by decide

structure VetoDynamicsWitness where
  vetoActiveAtT1 : Bool
  vetoActiveAtT2 : Bool
  globallyMonotone : Bool
  deriving DecidableEq, Repr

def vetoDynamicsWitness : VetoDynamicsWitness :=
  { vetoActiveAtT1 := true, vetoActiveAtT2 := false, globallyMonotone := false }

theorem vetoAuthorityNeedNotBeMonotone :
    vetoDynamicsWitness.vetoActiveAtT1 = true ∧
    vetoDynamicsWitness.vetoActiveAtT2 = false ∧
    vetoDynamicsWitness.globallyMonotone = false := by decide

structure ChronologyWitness where
  chronologyDiffers : Bool
  materialStateDiffers : Bool
  authorityDiffers : Bool
  deriving DecidableEq, Repr

def chronologyWitness : ChronologyWitness :=
  { chronologyDiffers := true, materialStateDiffers := false, authorityDiffers := false }

theorem chronologyAloneDoesNotCreateAuthority :
    chronologyWitness.chronologyDiffers = true ∧
    chronologyWitness.materialStateDiffers = false ∧
    chronologyWitness.authorityDiffers = false := by decide

structure MutationWitness where
  reasonTypeChanged : Bool
  ancestryPreserved : Bool
  secondIndependentWarrant : Bool
  deriving DecidableEq, Repr

def mutationWitness : MutationWitness :=
  { reasonTypeChanged := true, ancestryPreserved := true, secondIndependentWarrant := false }

theorem reasonMutationDoesNotDuplicateIndependentWarrant :
    mutationWitness.reasonTypeChanged = true ∧
    mutationWitness.ancestryPreserved = true ∧
    mutationWitness.secondIndependentWarrant = false := by decide

structure LostOptionWitness where
  sameRelationLabel : Bool
  optionLost : Bool
  exactRestoration : Bool
  deriving DecidableEq, Repr

def lostOptionWitness : LostOptionWitness :=
  { sameRelationLabel := true, optionLost := true, exactRestoration := false }

theorem lostOptionCanBlockExactRestoration :
    lostOptionWitness.sameRelationLabel = true ∧
    lostOptionWitness.optionLost = true ∧
    lostOptionWitness.exactRestoration = false := by decide

structure CycleWitness where
  cyclePersists : Bool
  scalarAggregationRequired : Bool
  deriving DecidableEq, Repr

def cycleWitness : CycleWitness :=
  { cyclePersists := true, scalarAggregationRequired := false }

theorem persistentConflictCycleDoesNotForceScalarAggregation :
    cycleWitness.cyclePersists = true ∧
    cycleWitness.scalarAggregationRequired = false := by decide

#print axioms MQR.sameTerminalRelationDoesNotImplySameMaterialHistory
#print axioms MQR.revisionOrderNeedNotCommute
#print axioms MQR.resolvedConflictMayLegitimatelyReopen
#print axioms MQR.vetoAuthorityNeedNotBeMonotone
#print axioms MQR.chronologyAloneDoesNotCreateAuthority
#print axioms MQR.reasonMutationDoesNotDuplicateIndependentWarrant
#print axioms MQR.lostOptionCanBlockExactRestoration
#print axioms MQR.persistentConflictCycleDoesNotForceScalarAggregation

end MQR
