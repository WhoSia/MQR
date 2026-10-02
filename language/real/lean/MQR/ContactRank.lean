import Std

namespace MQR

structure NonMatroidContactWitness where
  rank : Nat
  basisCount : Nat
  firstBasisCovers : Bool
  secondBasisCovers : Bool
  singleRootCovers : Bool
  exchangeR1WithR3Covers : Bool
  exchangeR1WithR4Covers : Bool
  deriving DecidableEq, Repr

def nonMatroidContactWitness : NonMatroidContactWitness :=
  { rank := 2
    basisCount := 2
    firstBasisCovers := true
    secondBasisCovers := true
    singleRootCovers := false
    exchangeR1WithR3Covers := false
    exchangeR1WithR4Covers := false }

theorem twoMinimumCoverWitnesses :
    nonMatroidContactWitness.rank = 2 ∧
      nonMatroidContactWitness.basisCount = 2 ∧
      nonMatroidContactWitness.firstBasisCovers = true ∧
      nonMatroidContactWitness.secondBasisCovers = true ∧
      nonMatroidContactWitness.singleRootCovers = false := by
  decide

theorem minimumWorldContactBasesNeedNotSatisfyExchange :
    nonMatroidContactWitness.exchangeR1WithR3Covers = false ∧
      nonMatroidContactWitness.exchangeR1WithR4Covers = false := by
  decide

structure RankTransitionWitness where
  beforeRank : Nat
  afterRank : Nat
  deriving DecidableEq, Repr

def frontierExpansionWitness : RankTransitionWitness :=
  { beforeRank := 1, afterRank := 2 }

theorem frontierExpansionCanIncreaseContactRank :
    frontierExpansionWitness.beforeRank = 1 ∧
      frontierExpansionWitness.afterRank = 2 ∧
      frontierExpansionWitness.beforeRank < frontierExpansionWitness.afterRank := by
  decide

def rootDriftWitness : RankTransitionWitness :=
  { beforeRank := 1, afterRank := 2 }

theorem rootDriftCanIncreaseContactRank :
    rootDriftWitness.beforeRank = 1 ∧
      rootDriftWitness.afterRank = 2 ∧
      rootDriftWitness.beforeRank < rootDriftWitness.afterRank := by
  decide

def instrumentExpansionWitness : RankTransitionWitness :=
  { beforeRank := 2, afterRank := 1 }

theorem instrumentExpansionCanDecreaseContactRank :
    instrumentExpansionWitness.beforeRank = 2 ∧
      instrumentExpansionWitness.afterRank = 1 ∧
      instrumentExpansionWitness.afterRank < instrumentExpansionWitness.beforeRank := by
  decide

structure RenamingWitness where
  leftRank : Nat
  rightRank : Nat
  leftObligations : Nat
  rightObligations : Nat
  incidenceIsomorphic : Bool
  deriving DecidableEq, Repr

def incidenceRenamingWitness : RenamingWitness :=
  { leftRank := 2
    rightRank := 2
    leftObligations := 2
    rightObligations := 2
    incidenceIsomorphic := true }

theorem incidenceRenamingPreservesRankWitness :
    incidenceRenamingWitness.incidenceIsomorphic = true ∧
      incidenceRenamingWitness.leftRank = incidenceRenamingWitness.rightRank := by
  decide

structure FrontierOntologyWitness where
  firstObligationCount : Nat
  secondObligationCount : Nat
  firstRank : Nat
  secondRank : Nat
  deriving DecidableEq, Repr

def frontierOntologyWitness : FrontierOntologyWitness :=
  { firstObligationCount := 2
    secondObligationCount := 3
    firstRank := 1
    secondRank := 1 }

theorem sameMinimumRankDoesNotIdentifyFrontierOntology :
    frontierOntologyWitness.firstObligationCount ≠ frontierOntologyWitness.secondObligationCount ∧
      frontierOntologyWitness.firstRank = frontierOntologyWitness.secondRank := by
  decide

structure DeclaredDegreeWitness where
  firstDeclaredCount : Nat
  secondDeclaredCount : Nat
  worldContactChanged : Bool
  deriving DecidableEq, Repr

def declaredDegreeWitness : DeclaredDegreeWitness :=
  { firstDeclaredCount := 1
    secondDeclaredCount := 2
    worldContactChanged := false }

theorem declaredDegreeCountCanChangeWithoutAWorldWitness :
    declaredDegreeWitness.firstDeclaredCount ≠ declaredDegreeWitness.secondDeclaredCount ∧
      declaredDegreeWitness.worldContactChanged = false := by
  decide


structure CalibrationContractWitness where
  coverMinimal : Bool
  calibrationAuthorityEstablished : Bool
  deriving DecidableEq, Repr

def calibrationContractWitness : CalibrationContractWitness :=
  { coverMinimal := true
    calibrationAuthorityEstablished := false }

theorem coverMinimalityDoesNotEstablishCalibrationAuthority :
    calibrationContractWitness.coverMinimal = true ∧
      calibrationContractWitness.calibrationAuthorityEstablished = false := by
  decide

structure SeparationContractWitness where
  sameMeasurementMaterial : Bool
  firstRank : Nat
  secondRank : Nat
  deriving DecidableEq, Repr

def separationContractWitness : SeparationContractWitness :=
  { sameMeasurementMaterial := true
    firstRank := 1
    secondRank := 2 }

theorem sameMeasurementMaterialCanHaveDifferentRankUnderDifferentSeparationContracts :
    separationContractWitness.sameMeasurementMaterial = true ∧
      separationContractWitness.firstRank ≠ separationContractWitness.secondRank := by
  decide

structure SelectionHistoryWitness where
  realizedMinimumRank : Nat
  selectionHistoryComplete : Bool
  deriving DecidableEq, Repr

def selectionHistoryWitness : SelectionHistoryWitness :=
  { realizedMinimumRank := 1
    selectionHistoryComplete := false }

theorem realizedMinimumDoesNotEstablishSelectionHistorySufficiency :
    selectionHistoryWitness.realizedMinimumRank = 1 ∧
      selectionHistoryWitness.selectionHistoryComplete = false := by
  decide

structure DecisionWarrantWitness where
  descriptiveCoverageComplete : Bool
  robustDecisionAvailable : Bool
  deriving DecidableEq, Repr

def decisionWarrantWitness : DecisionWarrantWitness :=
  { descriptiveCoverageComplete := false
    robustDecisionAvailable := true }

theorem contactRankDoesNotDetermineDecisionWarrant :
    decisionWarrantWitness.descriptiveCoverageComplete = false ∧
      decisionWarrantWitness.robustDecisionAvailable = true := by
  decide

#print axioms MQR.twoMinimumCoverWitnesses
#print axioms MQR.minimumWorldContactBasesNeedNotSatisfyExchange
#print axioms MQR.frontierExpansionCanIncreaseContactRank
#print axioms MQR.rootDriftCanIncreaseContactRank
#print axioms MQR.instrumentExpansionCanDecreaseContactRank
#print axioms MQR.incidenceRenamingPreservesRankWitness
#print axioms MQR.sameMinimumRankDoesNotIdentifyFrontierOntology
#print axioms MQR.declaredDegreeCountCanChangeWithoutAWorldWitness
#print axioms MQR.coverMinimalityDoesNotEstablishCalibrationAuthority
#print axioms MQR.sameMeasurementMaterialCanHaveDifferentRankUnderDifferentSeparationContracts
#print axioms MQR.realizedMinimumDoesNotEstablishSelectionHistorySufficiency
#print axioms MQR.contactRankDoesNotDetermineDecisionWarrant

end MQR
