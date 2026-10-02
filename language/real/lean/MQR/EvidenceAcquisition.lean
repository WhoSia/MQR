import MQR.PromotionDynamics

namespace MQR

structure InformationTrapWitness where
  maximalImmediateInformation : Bool
  uniqueFutureSeparatorDestroyed : Bool
  sequenceOptimal : Bool
  deriving DecidableEq, Repr

def informationTrapWitness : InformationTrapWitness :=
  { maximalImmediateInformation := true
    uniqueFutureSeparatorDestroyed := true
    sequenceOptimal := false }

theorem maximalImmediateInformationNeedNotBeSequenceOptimal :
    informationTrapWitness.maximalImmediateInformation = true ∧
    informationTrapWitness.uniqueFutureSeparatorDestroyed = true ∧
    informationTrapWitness.sequenceOptimal = false := by decide

structure IdentifiabilityWitness where
  identifiabilityGain : Bool
  liveClaimRelevance : Bool
  universalScientificValue : Bool
  deriving DecidableEq, Repr

def identifiabilityWitness : IdentifiabilityWitness :=
  { identifiabilityGain := true
    liveClaimRelevance := false
    universalScientificValue := false }

theorem identifiabilityGainDoesNotImplyUniversalScientificValue :
    identifiabilityWitness.identifiabilityGain = true ∧
    identifiabilityWitness.liveClaimRelevance = false ∧
    identifiabilityWitness.universalScientificValue = false := by decide

structure SequenceWitness where
  orderABPreservesSeparator : Bool
  orderBAPreservesSeparator : Bool
  commutes : Bool
  deriving DecidableEq, Repr

def sequenceWitness : SequenceWitness :=
  { orderABPreservesSeparator := true
    orderBAPreservesSeparator := false
    commutes := false }

theorem evidenceAcquisitionOrderNeedNotCommute :
    sequenceWitness.orderABPreservesSeparator = true ∧
    sequenceWitness.orderBAPreservesSeparator = false ∧
    sequenceWitness.commutes = false := by decide

structure BlindSpotWitness where
  policyUsesOwnModel : Bool
  exteriorRegionSampled : Bool
  policyAdequate : Bool
  deriving DecidableEq, Repr

def blindSpotWitness : BlindSpotWitness :=
  { policyUsesOwnModel := true
    exteriorRegionSampled := false
    policyAdequate := false }

theorem acquisitionPolicyCanCreateItsOwnBlindSpot :
    blindSpotWitness.policyUsesOwnModel = true ∧
    blindSpotWitness.exteriorRegionSampled = false ∧
    blindSpotWitness.policyAdequate = false := by decide

structure RandomizationWitness where
  randomExteriorProbe : Bool
  blindSpotBroken : Bool
  adequacyCertified : Bool
  deriving DecidableEq, Repr

def randomizationWitness : RandomizationWitness :=
  { randomExteriorProbe := true
    blindSpotBroken := true
    adequacyCertified := false }

theorem randomizationCanBreakBlindSpotWithoutCertifyingAdequacy :
    randomizationWitness.randomExteriorProbe = true ∧
    randomizationWitness.blindSpotBroken = true ∧
    randomizationWitness.adequacyCertified = false := by decide

structure OptionWitness where
  immediateGainLower : Bool
  futureSeparatorPreserved : Bool
  constitutionallyAdmissible : Bool
  deriving DecidableEq, Repr

def optionWitness : OptionWitness :=
  { immediateGainLower := true
    futureSeparatorPreserved := true
    constitutionallyAdmissible := true }

theorem lowerImmediateGainCanBeAdmissibleByOptionPreservation :
    optionWitness.immediateGainLower = true ∧
    optionWitness.futureSeparatorPreserved = true ∧
    optionWitness.constitutionallyAdmissible = true := by decide

structure ParetoExperimentWitness where
  nondominatedActionCount : Nat
  uniqueSelector : Bool
  deriving DecidableEq, Repr

def paretoExperimentWitness : ParetoExperimentWitness :=
  { nondominatedActionCount := 2
    uniqueSelector := false }

theorem paretoNondominationDoesNotSelectUniqueExperiment :
    paretoExperimentWitness.nondominatedActionCount = 2 ∧
    paretoExperimentWitness.uniqueSelector = false := by decide

structure ExplorationDebtWitness where
  locallyRationalChoice : Bool
  uniqueSeparatorSkipped : Bool
  debtCreated : Bool
  deriving DecidableEq, Repr

def explorationDebtWitness : ExplorationDebtWitness :=
  { locallyRationalChoice := true
    uniqueSeparatorSkipped := true
    debtCreated := true }

theorem localRationalityCanCreateNonmyopicExplorationDebt :
    explorationDebtWitness.locallyRationalChoice = true ∧
    explorationDebtWitness.uniqueSeparatorSkipped = true ∧
    explorationDebtWitness.debtCreated = true := by decide

#print axioms MQR.maximalImmediateInformationNeedNotBeSequenceOptimal
#print axioms MQR.identifiabilityGainDoesNotImplyUniversalScientificValue
#print axioms MQR.evidenceAcquisitionOrderNeedNotCommute
#print axioms MQR.acquisitionPolicyCanCreateItsOwnBlindSpot
#print axioms MQR.randomizationCanBreakBlindSpotWithoutCertifyingAdequacy
#print axioms MQR.lowerImmediateGainCanBeAdmissibleByOptionPreservation
#print axioms MQR.paretoNondominationDoesNotSelectUniqueExperiment
#print axioms MQR.localRationalityCanCreateNonmyopicExplorationDebt

end MQR
