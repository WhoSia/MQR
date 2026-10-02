import MQR.ConsequenceFamily

namespace MQR

structure CheapChallengeWitness where
  cheapYieldHigh : Bool
  expensiveLoadBearing : Bool
  cheapMaterial : Bool
  deriving DecidableEq, Repr

def cheapChallengeWitness : CheapChallengeWitness :=
  { cheapYieldHigh := true, expensiveLoadBearing := true, cheapMaterial := false }

theorem cheapYieldPerCostNeedNotTrackScientificValue :
    cheapChallengeWitness.cheapYieldHigh = true ∧
    cheapChallengeWitness.expensiveLoadBearing = true ∧
    cheapChallengeWitness.cheapMaterial = false := by decide

structure InformationRelevanceWitness where
  informationRanksA : Bool
  relevanceRanksB : Bool
  deriving DecidableEq, Repr

def informationRelevanceWitness : InformationRelevanceWitness :=
  { informationRanksA := true, relevanceRanksB := true }

theorem informationGainNeedNotOrderTargetRelevance :
    informationRelevanceWitness.informationRanksA = true ∧
    informationRelevanceWitness.relevanceRanksB = true := by decide

structure NoveltyWitness where
  noveltyIncreases : Bool
  targetRelevanceDecreases : Bool
  deriving DecidableEq, Repr

def noveltyWitness : NoveltyWitness :=
  { noveltyIncreases := true, targetRelevanceDecreases := true }

theorem noveltyIncreaseNeedNotIncreaseTargetValue :
    noveltyWitness.noveltyIncreases = true ∧
    noveltyWitness.targetRelevanceDecreases = true := by decide

structure ProxyGoodhartWitness where
  proxyImproves : Bool
  targetValueFalls : Bool
  proxySharesTargetRepresentation : Bool
  deriving DecidableEq, Repr

def proxyGoodhartWitness : ProxyGoodhartWitness :=
  { proxyImproves := true, targetValueFalls := true, proxySharesTargetRepresentation := true }

theorem challengeProxyOptimizationCanGoodhart :
    proxyGoodhartWitness.proxyImproves = true ∧
    proxyGoodhartWitness.targetValueFalls = true ∧
    proxyGoodhartWitness.proxySharesTargetRepresentation = true := by decide

structure TargetDriftWitness where
  targetChanged : Bool
  oldRankingRetained : Bool
  oldRankingStillLicensed : Bool
  deriving DecidableEq, Repr

def targetDriftWitness : TargetDriftWitness :=
  { targetChanged := true, oldRankingRetained := true, oldRankingStillLicensed := false }

theorem targetDriftCanDefeatOldRelevanceOrder :
    targetDriftWitness.targetChanged = true ∧
    targetDriftWitness.oldRankingRetained = true ∧
    targetDriftWitness.oldRankingStillLicensed = false := by decide

structure DecoyFloodWitness where
  manyIndependent : Bool
  proxyHigh : Bool
  touchesLiveBoundary : Bool
  deriving DecidableEq, Repr

def decoyFloodWitness : DecoyFloodWitness :=
  { manyIndependent := true, proxyHigh := true, touchesLiveBoundary := false }

theorem independentHighProxyChallengesNeedNotBeMaterial :
    decoyFloodWitness.manyIndependent = true ∧
    decoyFloodWitness.proxyHigh = true ∧
    decoyFloodWitness.touchesLiveBoundary = false := by decide

structure CommonEvaluatorWitness where
  generatorDiverse : Bool
  valueModelSingle : Bool
  sharedBlindSpot : Bool
  deriving DecidableEq, Repr

def commonEvaluatorWitness : CommonEvaluatorWitness :=
  { generatorDiverse := true, valueModelSingle := true, sharedBlindSpot := true }

theorem generatorDiversityDoesNotImplyValuationDiversity :
    commonEvaluatorWitness.generatorDiverse = true ∧
    commonEvaluatorWitness.valueModelSingle = true ∧
    commonEvaluatorWitness.sharedBlindSpot = true := by decide

structure UnitRankWitness where
  orderBefore : Bool
  orderAfter : Bool
  scienceUnchanged : Bool
  deriving DecidableEq, Repr

def unitRankWitness : UnitRankWitness :=
  { orderBefore := true, orderAfter := false, scienceUnchanged := true }

theorem arbitraryCostRescalingCanReverseBadScalarRanking :
    unitRankWitness.orderBefore = true ∧
    unitRankWitness.orderAfter = false ∧
    unitRankWitness.scienceUnchanged = true := by decide

structure HorizonWitness where
  shortPrefersA : Bool
  longPrefersB : Bool
  bOpensFutureFamily : Bool
  deriving DecidableEq, Repr

def horizonWitness : HorizonWitness :=
  { shortPrefersA := true, longPrefersB := true, bOpensFutureFamily := true }

theorem challengePreferenceCanDependOnDeclaredHorizon :
    horizonWitness.shortPrefersA = true ∧
    horizonWitness.longPrefersB = true ∧
    horizonWitness.bOpensFutureFamily = true := by decide

structure ActionabilityWitness where
  separationRanksA : Bool
  actionRanksB : Bool
  deriving DecidableEq, Repr

def actionabilityWitness : ActionabilityWitness :=
  { separationRanksA := true, actionRanksB := true }

theorem separationPowerNeedNotOrderActionValue :
    actionabilityWitness.separationRanksA = true ∧
    actionabilityWitness.actionRanksB = true := by decide

structure SurpriseWitness where
  surpriseHigh : Bool
  importanceLow : Bool
  deriving DecidableEq, Repr

def surpriseWitness : SurpriseWitness :=
  { surpriseHigh := true, importanceLow := true }

theorem surpriseNeedNotImplyScientificImportance :
    surpriseWitness.surpriseHigh = true ∧
    surpriseWitness.importanceLow = true := by decide

structure SunkYieldWitness where
  pastYieldHigh : Bool
  freshEscapeElsewhere : Bool
  policyStaysIncumbent : Bool
  deriving DecidableEq, Repr

def sunkYieldWitness : SunkYieldWitness :=
  { pastYieldHigh := true, freshEscapeElsewhere := true, policyStaysIncumbent := true }

theorem historicalYieldNeedNotLicenseFutureLockIn :
    sunkYieldWitness.pastYieldHigh = true ∧
    sunkYieldWitness.freshEscapeElsewhere = true ∧
    sunkYieldWitness.policyStaysIncumbent = true := by decide

structure SelfInsulationWitness where
  challengeTargetsValueModel : Bool
  valueModelRejectsAsIrrelevant : Bool
  deriving DecidableEq, Repr

def selfInsulationWitness : SelfInsulationWitness :=
  { challengeTargetsValueModel := true, valueModelRejectsAsIrrelevant := true }

theorem valueModelCanSelfInsulateAgainstCriticism :
    selfInsulationWitness.challengeTargetsValueModel = true ∧
    selfInsulationWitness.valueModelRejectsAsIrrelevant = true := by decide

structure OptionStructureWitness where
  currentValueEqual : Bool
  onlyBOpensNewFamily : Bool
  deriving DecidableEq, Repr

def optionStructureWitness : OptionStructureWitness :=
  { currentValueEqual := true, onlyBOpensNewFamily := true }

theorem equalCurrentValueNeedNotImplyEqualOptionStructure :
    optionStructureWitness.currentValueEqual = true ∧
    optionStructureWitness.onlyBOpensNewFamily = true := by decide

structure LocalOptimizerWitness where
  priorDeclared : Bool
  utilityDeclared : Bool
  costDeclared : Bool
  uniqueLocalOptimum : Bool
  worldOptimum : Bool
  deriving DecidableEq, Repr

def localOptimizerWitness : LocalOptimizerWitness :=
  { priorDeclared := true, utilityDeclared := true, costDeclared := true,
    uniqueLocalOptimum := true, worldOptimum := false }

theorem declaredModelCanHaveUniqueLocalOptimumWithoutWorldOptimum :
    localOptimizerWitness.priorDeclared = true ∧
    localOptimizerWitness.utilityDeclared = true ∧
    localOptimizerWitness.costDeclared = true ∧
    localOptimizerWitness.uniqueLocalOptimum = true ∧
    localOptimizerWitness.worldOptimum = false := by decide

structure PartialOrderWitness where
  dominanceExists : Bool
  incomparabilityExists : Bool
  deriving DecidableEq, Repr

def partialOrderWitness : PartialOrderWitness :=
  { dominanceExists := true, incomparabilityExists := true }

theorem partialOrderCanGuideWithoutTotalRanking :
    partialOrderWitness.dominanceExists = true ∧
    partialOrderWitness.incomparabilityExists = true := by decide

structure DriftReopeningWitness where
  contractChanged : Bool
  sentinelFires : Bool
  oldOrderReused : Bool
  reconstituted : Bool
  deriving DecidableEq, Repr

def driftReopeningWitness : DriftReopeningWitness :=
  { contractChanged := true, sentinelFires := true, oldOrderReused := false, reconstituted := true }

theorem targetDriftCanMandateValueReconstitution :
    driftReopeningWitness.contractChanged = true ∧
    driftReopeningWitness.sentinelFires = true ∧
    driftReopeningWitness.oldOrderReused = false ∧
    driftReopeningWitness.reconstituted = true := by decide

structure ValueRevisionWitness where
  predictedSuperiority : Bool
  prospectiveFailure : Bool
  valueModelRevised : Bool
  deriving DecidableEq, Repr

def valueRevisionWitness : ValueRevisionWitness :=
  { predictedSuperiority := true, prospectiveFailure := true, valueModelRevised := true }

theorem worldContactCanReviseChallengeValueModel :
    valueRevisionWitness.predictedSuperiority = true ∧
    valueRevisionWitness.prospectiveFailure = true ∧
    valueRevisionWitness.valueModelRevised = true := by decide

structure UniversalUtilityWitness where
  localGuidancePossible : Bool
  universalUtilityEarned : Bool
  worldOptimalPolicyEarned : Bool
  deriving DecidableEq, Repr

def universalUtilityWitness : UniversalUtilityWitness :=
  { localGuidancePossible := true, universalUtilityEarned := false, worldOptimalPolicyEarned := false }

theorem localGuidanceDoesNotImplyUniversalScientificUtility :
    universalUtilityWitness.localGuidancePossible = true ∧
    universalUtilityWitness.universalUtilityEarned = false := by decide

theorem localGuidanceDoesNotImplyWorldOptimalExpansionPolicy :
    universalUtilityWitness.localGuidancePossible = true ∧
    universalUtilityWitness.worldOptimalPolicyEarned = false := by decide

#print axioms MQR.cheapYieldPerCostNeedNotTrackScientificValue
#print axioms MQR.informationGainNeedNotOrderTargetRelevance
#print axioms MQR.noveltyIncreaseNeedNotIncreaseTargetValue
#print axioms MQR.challengeProxyOptimizationCanGoodhart
#print axioms MQR.targetDriftCanDefeatOldRelevanceOrder
#print axioms MQR.independentHighProxyChallengesNeedNotBeMaterial
#print axioms MQR.generatorDiversityDoesNotImplyValuationDiversity
#print axioms MQR.arbitraryCostRescalingCanReverseBadScalarRanking
#print axioms MQR.challengePreferenceCanDependOnDeclaredHorizon
#print axioms MQR.separationPowerNeedNotOrderActionValue
#print axioms MQR.surpriseNeedNotImplyScientificImportance
#print axioms MQR.historicalYieldNeedNotLicenseFutureLockIn
#print axioms MQR.valueModelCanSelfInsulateAgainstCriticism
#print axioms MQR.equalCurrentValueNeedNotImplyEqualOptionStructure
#print axioms MQR.declaredModelCanHaveUniqueLocalOptimumWithoutWorldOptimum
#print axioms MQR.partialOrderCanGuideWithoutTotalRanking
#print axioms MQR.targetDriftCanMandateValueReconstitution
#print axioms MQR.worldContactCanReviseChallengeValueModel
#print axioms MQR.localGuidanceDoesNotImplyUniversalScientificUtility
#print axioms MQR.localGuidanceDoesNotImplyWorldOptimalExpansionPolicy

end MQR
