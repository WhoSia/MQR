import Std

namespace MQR

inductive SearchLane where
  | a
  | b
  deriving DecidableEq, Repr

inductive TwinWorld where
  | worldA
  | worldB
  deriving DecidableEq, Repr

def visibleHistorySignature : TwinWorld → Nat
  | .worldA => 43
  | .worldB => 43

def escapeCaptured : TwinWorld → SearchLane → Bool
  | .worldA, .a => true
  | .worldA, .b => false
  | .worldB, .a => false
  | .worldB, .b => true

theorem observationallyEquivalentWorldsCanRequireOppositeEscapeActions :
    visibleHistorySignature .worldA = visibleHistorySignature .worldB ∧
      escapeCaptured .worldA .a = true ∧
      escapeCaptured .worldB .a = false ∧
      escapeCaptured .worldA .b = false ∧
      escapeCaptured .worldB .b = true := by
  decide

theorem noSingleTwinWorldActionCapturesBothEscapes :
    ¬ (escapeCaptured .worldA .a = true ∧ escapeCaptured .worldB .a = true) ∧
      ¬ (escapeCaptured .worldA .b = true ∧ escapeCaptured .worldB .b = true) := by
  decide

theorem noSingleActionCanCaptureBothTwinWorldEscapes (action : SearchLane) :
    ¬ (escapeCaptured .worldA action = true ∧
       escapeCaptured .worldB action = true) := by
  cases action <;> decide

theorem noDeterministicPolicyOverVisibleSignatureCapturesBoth
    (policy : Nat → SearchLane) :
    ¬ (escapeCaptured .worldA (policy (visibleHistorySignature .worldA)) = true ∧
       escapeCaptured .worldB (policy (visibleHistorySignature .worldB)) = true) := by
  exact noSingleActionCanCaptureBothTwinWorldEscapes (policy 43)

structure ReserveWitness where
  reserveUnits : Nat
  activationCost : Nat
  deriving DecidableEq, Repr

def nominalOnlyReserve : ReserveWitness :=
  { reserveUnits := 1, activationCost := 2 }

def liveReserve : ReserveWitness :=
  { reserveUnits := 2, activationCost := 2 }

theorem nominalReserveDoesNotImplyActivationCapability :
    nominalOnlyReserve.reserveUnits > 0 ∧
      nominalOnlyReserve.reserveUnits < nominalOnlyReserve.activationCost := by
  decide

theorem activationThresholdCanCertifyNarrowReserveCompetence :
    liveReserve.reserveUnits > 0 ∧
      liveReserve.activationCost ≤ liveReserve.reserveUnits := by
  decide

inductive DebtClass where
  | query
  | representation
  deriving DecidableEq, Repr

structure DebtGeometry where
  count : Nat
  kind : DebtClass
  deriving DecidableEq, Repr

def queryDebt : DebtGeometry := { count := 1, kind := .query }
def representationDebt : DebtGeometry := { count := 1, kind := .representation }

theorem equalScalarDebtCountDoesNotIdentifyDebtGeometry :
    queryDebt.count = representationDebt.count ∧
      queryDebt.kind ≠ representationDebt.kind := by
  decide

structure AntiStarvationWitness where
  laneAActivatedByDue : Bool
  laneBActivatedByDue : Bool
  finiteDeclaredPortfolio : Bool
  worldFrontierComplete : Bool
  deriving DecidableEq, Repr

def antiStarvationWitness : AntiStarvationWitness :=
  { laneAActivatedByDue := true
    laneBActivatedByDue := true
    finiteDeclaredPortfolio := true
    worldFrontierComplete := false }

theorem finiteDeclaredAntiStarvationCanBeCertified :
    antiStarvationWitness.laneAActivatedByDue = true ∧
      antiStarvationWitness.laneBActivatedByDue = true ∧
      antiStarvationWitness.finiteDeclaredPortfolio = true := by
  decide

def firstCycleRoundRobinLane (step : Nat) : Nat :=
  step

theorem roundRobinVisitsEveryDeclaredLaneWithinOneCycle
    (laneCount lane : Nat)
    (hLane : lane < laneCount) :
    ∃ step, step < laneCount ∧ firstCycleRoundRobinLane step = lane := by
  exact ⟨lane, hLane, rfl⟩

theorem finiteRoundRobinPreventsUnitActivationStarvation
    (laneCount budget lane : Nat)
    (hBudget : budget = laneCount)
    (hLane : lane < laneCount) :
    ∃ step,
      step < laneCount ∧
      step < budget ∧
      firstCycleRoundRobinLane step = lane := by
  refine ⟨lane, hLane, ?_, rfl⟩
  rw [hBudget]
  exact hLane

theorem proceduralCoverageDoesNotImplyWorldFrontierCompleteness :
    antiStarvationWitness.laneAActivatedByDue = true ∧
      antiStarvationWitness.laneBActivatedByDue = true ∧
      antiStarvationWitness.worldFrontierComplete = false := by
  decide

structure ExploitationTrapWitness where
  currentFrontierGain : Bool
  reopeningLaneStarved : Bool
  offFrontierEscapeExists : Bool
  explorationRetirementLicensed : Bool
  deriving DecidableEq, Repr

def exploitationTrapWitness : ExploitationTrapWitness :=
  { currentFrontierGain := true
    reopeningLaneStarved := true
    offFrontierEscapeExists := true
    explorationRetirementLicensed := false }

theorem localExploitationGainDoesNotLicenseExplorationRetirement :
    exploitationTrapWitness.currentFrontierGain = true ∧
      exploitationTrapWitness.reopeningLaneStarved = true ∧
      exploitationTrapWitness.offFrontierEscapeExists = true ∧
      exploitationTrapWitness.explorationRetirementLicensed = false := by
  decide

structure EnvelopeWitness where
  scheduleAAdmissible : Bool
  scheduleBAdmissible : Bool
  uniqueWorldOptimumIdentified : Bool
  deriving DecidableEq, Repr

def envelopeWitness : EnvelopeWitness :=
  { scheduleAAdmissible := true
    scheduleBAdmissible := true
    uniqueWorldOptimumIdentified := false }

theorem setValuedAdmissibilityDoesNotIdentifyUniqueWorldOptimum :
    envelopeWitness.scheduleAAdmissible = true ∧
      envelopeWitness.scheduleBAdmissible = true ∧
      envelopeWitness.uniqueWorldOptimumIdentified = false := by
  decide

structure EscapeReallocationWitness where
  escapeDetected : Bool
  allocationReceiptReopened : Bool
  deriving DecidableEq, Repr

def escapeReallocationWitness : EscapeReallocationWitness :=
  { escapeDetected := true
    allocationReceiptReopened := true }

theorem frontierEscapeCanMandateAllocationReopening :
    escapeReallocationWitness.escapeDetected = true ∧
      escapeReallocationWitness.allocationReceiptReopened = true := by
  decide

structure RandomizationBoundaryWitness where
  boundedGapCoverage : Bool
  calibratedDiscoveryProbability : Bool
  worldFrontierComplete : Bool
  deriving DecidableEq, Repr

def randomizationBoundaryWitness : RandomizationBoundaryWitness :=
  { boundedGapCoverage := true
    calibratedDiscoveryProbability := false
    worldFrontierComplete := false }

theorem randomizedCoverageIsNotAnEpistemicOracle :
    randomizationBoundaryWitness.boundedGapCoverage = true ∧
      randomizationBoundaryWitness.calibratedDiscoveryProbability = false ∧
      randomizationBoundaryWitness.worldFrontierComplete = false := by
  decide

#print axioms MQR.observationallyEquivalentWorldsCanRequireOppositeEscapeActions
#print axioms MQR.noSingleTwinWorldActionCapturesBothEscapes
#print axioms MQR.noSingleActionCanCaptureBothTwinWorldEscapes
#print axioms MQR.noDeterministicPolicyOverVisibleSignatureCapturesBoth
#print axioms MQR.nominalReserveDoesNotImplyActivationCapability
#print axioms MQR.activationThresholdCanCertifyNarrowReserveCompetence
#print axioms MQR.equalScalarDebtCountDoesNotIdentifyDebtGeometry
#print axioms MQR.finiteDeclaredAntiStarvationCanBeCertified
#print axioms MQR.roundRobinVisitsEveryDeclaredLaneWithinOneCycle
#print axioms MQR.finiteRoundRobinPreventsUnitActivationStarvation
#print axioms MQR.proceduralCoverageDoesNotImplyWorldFrontierCompleteness
#print axioms MQR.localExploitationGainDoesNotLicenseExplorationRetirement
#print axioms MQR.setValuedAdmissibilityDoesNotIdentifyUniqueWorldOptimum
#print axioms MQR.frontierEscapeCanMandateAllocationReopening
#print axioms MQR.randomizedCoverageIsNotAnEpistemicOracle

end MQR
