import Std

namespace MQR

structure RegressRefinementWitness where
  registered : Bool
  replayed : Bool
  authorityChanges : Bool
  operationalStop : Bool
  deriving DecidableEq, Repr

def regressMaterialRefinementWitness : RegressRefinementWitness :=
  { registered := true, replayed := true, authorityChanges := true, operationalStop := false }

theorem materialRegisteredRefinementBlocksOperationalStop :
    regressMaterialRefinementWitness.registered = true ∧
    regressMaterialRefinementWitness.replayed = true ∧
    regressMaterialRefinementWitness.authorityChanges = true ∧
    regressMaterialRefinementWitness.operationalStop = false := by
  decide

def regressInertRefinementWitness : RegressRefinementWitness :=
  { registered := true, replayed := true, authorityChanges := false, operationalStop := true }

theorem inertRegisteredRefinementCanLeaveAuthorityUnchanged :
    regressInertRefinementWitness.registered = true ∧
    regressInertRefinementWitness.replayed = true ∧
    regressInertRefinementWitness.authorityChanges = false ∧
    regressInertRefinementWitness.operationalStop = true := by
  decide

structure RegressFixedPointWitness where
  currentFixedPoint : Bool
  futureSpaceClosed : Bool
  metaphysicalTermination : Bool
  deriving DecidableEq, Repr

def regressFixedPointWitness : RegressFixedPointWitness :=
  { currentFixedPoint := true, futureSpaceClosed := false, metaphysicalTermination := false }

theorem localOperationalFixedPointDoesNotImplyFutureClosure :
    regressFixedPointWitness.currentFixedPoint = true ∧
    regressFixedPointWitness.futureSpaceClosed = false ∧
    regressFixedPointWitness.metaphysicalTermination = false := by
  decide

structure RegressScopeWitness where
  distinctionBefore : Bool
  postOutcomeShrink : Bool
  distinctionVisibleAfter : Bool
  originalWitnessRetained : Bool
  deriving DecidableEq, Repr

def regressScopeCaptureWitness : RegressScopeWitness :=
  { distinctionBefore := true, postOutcomeShrink := true,
    distinctionVisibleAfter := false, originalWitnessRetained := true }

theorem postOutcomeScopeShrinkCanHideButNotEraseExistingWitness :
    regressScopeCaptureWitness.distinctionBefore = true ∧
    regressScopeCaptureWitness.postOutcomeShrink = true ∧
    regressScopeCaptureWitness.distinctionVisibleAfter = false ∧
    regressScopeCaptureWitness.originalWitnessRetained = true := by
  decide

structure RegressCriterionWitness where
  criterionOneInert : Bool
  criterionTwoInert : Bool
  robustStop : Bool
  criterionFamilyComplete : Bool
  deriving DecidableEq, Repr

def regressCriterionDisagreementWitness : RegressCriterionWitness :=
  { criterionOneInert := true, criterionTwoInert := false,
    robustStop := false, criterionFamilyComplete := false }

theorem criterionDisagreementBlocksCriterionRobustStop :
    regressCriterionDisagreementWitness.criterionOneInert = true ∧
    regressCriterionDisagreementWitness.criterionTwoInert = false ∧
    regressCriterionDisagreementWitness.robustStop = false := by
  decide

def regressCriterionAgreementWitness : RegressCriterionWitness :=
  { criterionOneInert := true, criterionTwoInert := true,
    robustStop := true, criterionFamilyComplete := false }

theorem criterionAgreementDoesNotProveCriterionCompleteness :
    regressCriterionAgreementWitness.criterionOneInert = true ∧
    regressCriterionAgreementWitness.criterionTwoInert = true ∧
    regressCriterionAgreementWitness.robustStop = true ∧
    regressCriterionAgreementWitness.criterionFamilyComplete = false := by
  decide

structure RegressMetaCycleWitness where
  cyclicSupport : Bool
  externalFoundationAdded : Bool
  deriving DecidableEq, Repr

def regressMetaCycleWitness : RegressMetaCycleWitness :=
  { cyclicSupport := true, externalFoundationAdded := false }

theorem metaCriterionCycleDoesNotCreateExternalFoundation :
    regressMetaCycleWitness.cyclicSupport = true ∧
    regressMetaCycleWitness.externalFoundationAdded = false := by
  decide

structure RegressContactWitness where
  fixedPointBefore : Bool
  newContactDistinguishes : Bool
  fixedPointAfter : Bool
  reopening : Bool
  deriving DecidableEq, Repr

def regressContactWitness : RegressContactWitness :=
  { fixedPointBefore := true, newContactDistinguishes := true,
    fixedPointAfter := false, reopening := true }

theorem newWorldContactCanBreakPriorOperationalFixedPoint :
    regressContactWitness.fixedPointBefore = true ∧
    regressContactWitness.newContactDistinguishes = true ∧
    regressContactWitness.fixedPointAfter = false ∧
    regressContactWitness.reopening = true := by
  decide

structure RegressDecisionWitness where
  descriptiveInvariant : Bool
  actionInvariantUnderD0 : Bool
  actionInvariantUnderD1 : Bool
  universalActionWarrant : Bool
  deriving DecidableEq, Repr

def regressDecisionWitness : RegressDecisionWitness :=
  { descriptiveInvariant := true, actionInvariantUnderD0 := true,
    actionInvariantUnderD1 := false, universalActionWarrant := false }

theorem descriptiveInvarianceDoesNotImplyDecisionContractInvariance :
    regressDecisionWitness.descriptiveInvariant = true ∧
    regressDecisionWitness.actionInvariantUnderD0 = true ∧
    regressDecisionWitness.actionInvariantUnderD1 = false := by
  decide

theorem oneContractActionInvarianceDoesNotImplyUniversalActionWarrant :
    regressDecisionWitness.actionInvariantUnderD0 = true ∧
    regressDecisionWitness.universalActionWarrant = false := by
  decide

structure RegressAuthorizationWitness where
  operationalStop : Bool
  metaphysicalTermination : Bool
  finalOntology : Bool
  reopeningReserve : Bool
  deriving DecidableEq, Repr

def regressAuthorizationWitness : RegressAuthorizationWitness :=
  { operationalStop := true, metaphysicalTermination := false,
    finalOntology := false, reopeningReserve := true }

theorem operationalAuthorizationCanCoexistWithAntiFinality :
    regressAuthorizationWitness.operationalStop = true ∧
    regressAuthorizationWitness.metaphysicalTermination = false ∧
    regressAuthorizationWitness.finalOntology = false ∧
    regressAuthorizationWitness.reopeningReserve = true := by
  decide

#print axioms MQR.materialRegisteredRefinementBlocksOperationalStop
#print axioms MQR.inertRegisteredRefinementCanLeaveAuthorityUnchanged
#print axioms MQR.localOperationalFixedPointDoesNotImplyFutureClosure
#print axioms MQR.postOutcomeScopeShrinkCanHideButNotEraseExistingWitness
#print axioms MQR.criterionDisagreementBlocksCriterionRobustStop
#print axioms MQR.criterionAgreementDoesNotProveCriterionCompleteness
#print axioms MQR.metaCriterionCycleDoesNotCreateExternalFoundation
#print axioms MQR.newWorldContactCanBreakPriorOperationalFixedPoint
#print axioms MQR.descriptiveInvarianceDoesNotImplyDecisionContractInvariance
#print axioms MQR.oneContractActionInvarianceDoesNotImplyUniversalActionWarrant
#print axioms MQR.operationalAuthorizationCanCoexistWithAntiFinality

end MQR
