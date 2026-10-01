import MQR.ReflexiveEcology

namespace MQR

structure AdditiveNotNecessaryWitness where
  additiveChange : Bool
  materialSimplification : Bool
  localPromotion : Bool
  deriving DecidableEq, Repr

def additiveNotNecessaryWitness : AdditiveNotNecessaryWitness :=
  { additiveChange := false, materialSimplification := true, localPromotion := true }

theorem additiveChangeNotNecessaryForLocalPromotion :
    additiveNotNecessaryWitness.additiveChange = false ∧
    additiveNotNecessaryWitness.materialSimplification = true ∧
    additiveNotNecessaryWitness.localPromotion = true := by decide

structure AdditiveNotSufficientWitness where
  additiveChange : Bool
  materialConsequence : Bool
  localPromotion : Bool
  deriving DecidableEq, Repr

def additiveNotSufficientWitness : AdditiveNotSufficientWitness :=
  { additiveChange := true, materialConsequence := false, localPromotion := false }

theorem additiveChangeNotSufficientForLocalPromotion :
    additiveNotSufficientWitness.additiveChange = true ∧
    additiveNotSufficientWitness.materialConsequence = false ∧
    additiveNotSufficientWitness.localPromotion = false := by decide

structure LocalCriterionCeiling where
  locallyUseful : Bool
  universalRuleEarned : Bool
  scalarScoreEarned : Bool
  deriving DecidableEq, Repr

def localCriterionCeiling : LocalCriterionCeiling :=
  { locallyUseful := true, universalRuleEarned := false, scalarScoreEarned := false }

theorem localCriterionDoesNotImplyUniversalRule :
    localCriterionCeiling.locallyUseful = true ∧
    localCriterionCeiling.universalRuleEarned = false := by decide

theorem localCriterionDoesNotImplyScalarScore :
    localCriterionCeiling.locallyUseful = true ∧
    localCriterionCeiling.scalarScoreEarned = false := by decide


structure OptionValueWitness where
  additiveChange : Bool
  optionValue : Bool
  localPromotion : Bool
  deriving DecidableEq, Repr

def optionValueWitness : OptionValueWitness :=
  { additiveChange := false, optionValue := true, localPromotion := true }

theorem optionValueCanSupportLocalPromotion :
    optionValueWitness.additiveChange = false ∧
    optionValueWitness.optionValue = true ∧
    optionValueWitness.localPromotion = true := by decide

structure CriterionAuditWitness where
  auditPresent : Bool
  localPromotion : Bool
  deriving DecidableEq, Repr

def criterionAuditWitness : CriterionAuditWitness :=
  { auditPresent := false, localPromotion := false }

theorem missingCriterionAuditBlocksLocalPromotion :
    criterionAuditWitness.auditPresent = false ∧
    criterionAuditWitness.localPromotion = false := by decide

#print axioms MQR.additiveChangeNotNecessaryForLocalPromotion
#print axioms MQR.additiveChangeNotSufficientForLocalPromotion
#print axioms MQR.localCriterionDoesNotImplyUniversalRule
#print axioms MQR.localCriterionDoesNotImplyScalarScore
#print axioms MQR.optionValueCanSupportLocalPromotion
#print axioms MQR.missingCriterionAuditBlocksLocalPromotion

end MQR
