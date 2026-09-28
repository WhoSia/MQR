import Std

namespace MQR

structure StopEligibilityWitness where
  oqscEligible : Bool
  rawStopsNow : Bool
  externallyCalibrated : Bool
  futureSpaceClosed : Bool
  deriving DecidableEq, Repr

def stopEligibilityWitness : StopEligibilityWitness :=
  { oqscEligible := true, rawStopsNow := true,
    externallyCalibrated := false, futureSpaceClosed := false }

theorem immediateEligibilityDoesNotEntailExternalCalibration :
    stopEligibilityWitness.oqscEligible = true ∧
    stopEligibilityWitness.rawStopsNow = true ∧
    stopEligibilityWitness.externallyCalibrated = false ∧
    stopEligibilityWitness.futureSpaceClosed = false := by
  decide

structure StopLagWitness where
  firstEligible : Bool
  liveRiskAtFirstEligible : Bool
  lagOneStopsAtFirstEligible : Bool
  safeAfterOneMore : Bool
  deriving DecidableEq, Repr

def stopLagWitness : StopLagWitness :=
  { firstEligible := true, liveRiskAtFirstEligible := true,
    lagOneStopsAtFirstEligible := false, safeAfterOneMore := true }

theorem oneStepConfirmationCanBlockFirstEligiblePrematureStop :
    stopLagWitness.firstEligible = true ∧
    stopLagWitness.liveRiskAtFirstEligible = true ∧
    stopLagWitness.lagOneStopsAtFirstEligible = false ∧
    stopLagWitness.safeAfterOneMore = true := by
  decide

structure StopReopenWitness where
  priorLocalStopSafe : Bool
  novelPostStopBreak : Bool
  priorStopRetroactivelyPremature : Bool
  reopenRequired : Bool
  deriving DecidableEq, Repr

def stopReopenWitness : StopReopenWitness :=
  { priorLocalStopSafe := true, novelPostStopBreak := true,
    priorStopRetroactivelyPremature := false, reopenRequired := true }

theorem novelPostStopBreakRequiresReopenWithoutRetroactivePrematurity :
    stopReopenWitness.priorLocalStopSafe = true ∧
    stopReopenWitness.novelPostStopBreak = true ∧
    stopReopenWitness.priorStopRetroactivelyPremature = false ∧
    stopReopenWitness.reopenRequired = true := by
  decide

structure StopMetricCrossingWitness where
  policyAPremature : Nat
  policyAOverInquiry : Nat
  policyBPremature : Nat
  policyBOverInquiry : Nat
  aDominatesB : Bool
  bDominatesA : Bool
  deriving DecidableEq, Repr

def stopMetricCrossingWitness : StopMetricCrossingWitness :=
  { policyAPremature := 0, policyAOverInquiry := 5,
    policyBPremature := 1, policyBOverInquiry := 0,
    aDominatesB := false, bDominatesA := false }

theorem crossingStopMetricsNeedNotHaveParetoWinner :
    stopMetricCrossingWitness.policyAPremature <
      stopMetricCrossingWitness.policyBPremature ∧
    stopMetricCrossingWitness.policyAOverInquiry >
      stopMetricCrossingWitness.policyBOverInquiry ∧
    stopMetricCrossingWitness.aDominatesB = false ∧
    stopMetricCrossingWitness.bDominatesA = false := by
  decide

structure StopCalibrationWitness where
  calibrationSplitPassed : Bool
  untouchedHoldoutPassed : Bool
  internalBenchmarkCalibrated : Bool
  externalScientificCalibration : Bool
  universalOptimality : Bool
  deriving DecidableEq, Repr

def stopCalibrationWitness : StopCalibrationWitness :=
  { calibrationSplitPassed := true, untouchedHoldoutPassed := true,
    internalBenchmarkCalibrated := true,
    externalScientificCalibration := false,
    universalOptimality := false }

theorem internalHoldoutCalibrationDoesNotImplyExternalValidity :
    stopCalibrationWitness.calibrationSplitPassed = true ∧
    stopCalibrationWitness.untouchedHoldoutPassed = true ∧
    stopCalibrationWitness.internalBenchmarkCalibrated = true ∧
    stopCalibrationWitness.externalScientificCalibration = false ∧
    stopCalibrationWitness.universalOptimality = false := by
  decide

structure StopLeakageWitness where
  policySeesObservable : Bool
  policySeesHiddenGold : Bool
  scorerSeesHiddenGold : Bool
  outcomeSequestered : Bool
  deriving DecidableEq, Repr

def stopLeakageWitness : StopLeakageWitness :=
  { policySeesObservable := true, policySeesHiddenGold := false,
    scorerSeesHiddenGold := true, outcomeSequestered := true }

theorem scorerGoldCanBeSeparatedFromPolicyInput :
    stopLeakageWitness.policySeesObservable = true ∧
    stopLeakageWitness.policySeesHiddenGold = false ∧
    stopLeakageWitness.scorerSeesHiddenGold = true ∧
    stopLeakageWitness.outcomeSequestered = true := by
  decide

structure StopBudgetWitness where
  noLicensedStopBeforeBudget : Bool
  budgetExhausted : Bool
  prematureStopRequired : Bool
  failureOfInquiry : Bool
  deriving DecidableEq, Repr

def stopBudgetWitness : StopBudgetWitness :=
  { noLicensedStopBeforeBudget := true, budgetExhausted := true,
    prematureStopRequired := false, failureOfInquiry := false }

theorem justifiedBudgetExhaustionNeedNotLicensePrematureStop :
    stopBudgetWitness.noLicensedStopBeforeBudget = true ∧
    stopBudgetWitness.budgetExhausted = true ∧
    stopBudgetWitness.prematureStopRequired = false := by
  decide

#print axioms MQR.immediateEligibilityDoesNotEntailExternalCalibration
#print axioms MQR.oneStepConfirmationCanBlockFirstEligiblePrematureStop
#print axioms MQR.novelPostStopBreakRequiresReopenWithoutRetroactivePrematurity
#print axioms MQR.crossingStopMetricsNeedNotHaveParetoWinner
#print axioms MQR.internalHoldoutCalibrationDoesNotImplyExternalValidity
#print axioms MQR.scorerGoldCanBeSeparatedFromPolicyInput
#print axioms MQR.justifiedBudgetExhaustionNeedNotLicensePrematureStop

end MQR
