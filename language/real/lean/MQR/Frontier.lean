import Std

namespace MQR

structure QueryClosureWitness where
  currentRivalsSeparated : Bool
  offQueryRivalExists : Bool
  worldQueryClosed : Bool
  deriving DecidableEq, Repr

def queryClosureWitness : QueryClosureWitness :=
  { currentRivalsSeparated := true
    offQueryRivalExists := true
    worldQueryClosed := false }

theorem currentRivalSeparationDoesNotImplyQueryLanguageClosure :
    queryClosureWitness.currentRivalsSeparated = true ∧
      queryClosureWitness.offQueryRivalExists = true ∧
      queryClosureWitness.worldQueryClosed = false := by
  decide

structure SaturationWitness where
  noDiscoveryRuns : Nat
  distinctGeneratorFindsRival : Bool
  worldFrontierComplete : Bool
  deriving DecidableEq, Repr

def saturationWitness : SaturationWitness :=
  { noDiscoveryRuns := 100
    distinctGeneratorFindsRival := true
    worldFrontierComplete := false }

theorem repeatedNoDiscoveryDoesNotImplyFrontierCompleteness :
    saturationWitness.noDiscoveryRuns = 100 ∧
      saturationWitness.distinctGeneratorFindsRival = true ∧
      saturationWitness.worldFrontierComplete = false := by
  decide

structure StableRankDiscoveryWitness where
  beforeRank : Nat
  afterRank : Nat
  newRivalAdmitted : Bool
  newObligationAdmitted : Bool
  deriving DecidableEq, Repr

def stableRankDiscoveryWitness : StableRankDiscoveryWitness :=
  { beforeRank := 1
    afterRank := 1
    newRivalAdmitted := true
    newObligationAdmitted := true }

theorem stableFcrCanAccompanyFrontierDiscovery :
    stableRankDiscoveryWitness.beforeRank = stableRankDiscoveryWitness.afterRank ∧
      stableRankDiscoveryWitness.newRivalAdmitted = true ∧
      stableRankDiscoveryWitness.newObligationAdmitted = true := by
  decide

structure RankIncreaseValueWitness where
  beforeRank : Nat
  afterRank : Nat
  claimRelevant : Bool
  deriving DecidableEq, Repr

def rankIncreaseValueWitness : RankIncreaseValueWitness :=
  { beforeRank := 1
    afterRank := 2
    claimRelevant := false }

theorem rankIncreaseAloneDoesNotEstablishDiscoveryValue :
    rankIncreaseValueWitness.beforeRank < rankIncreaseValueWitness.afterRank ∧
      rankIncreaseValueWitness.claimRelevant = false := by
  decide

structure GeneratorAncestryWitness where
  generatorCount : Nat
  ancestryCount : Nat
  independent : Bool
  deriving DecidableEq, Repr

def generatorAncestryWitness : GeneratorAncestryWitness :=
  { generatorCount := 2
    ancestryCount := 1
    independent := false }

theorem multipleGeneratorsDoNotImplyIndependentRivalSearch :
    generatorAncestryWitness.generatorCount = 2 ∧
      generatorAncestryWitness.ancestryCount = 1 ∧
      generatorAncestryWitness.independent = false := by
  decide

structure GrammarClosureWitness where
  finiteGrammarExhausted : Bool
  scientificFrontierComplete : Bool
  deriving DecidableEq, Repr

def grammarClosureWitness : GrammarClosureWitness :=
  { finiteGrammarExhausted := true
    scientificFrontierComplete := false }

theorem finiteGrammarClosureDoesNotImplyScientificFrontierClosure :
    grammarClosureWitness.finiteGrammarExhausted = true ∧
      grammarClosureWitness.scientificFrontierComplete = false := by
  decide

structure PortfolioWitness where
  firstHasA : Bool
  firstHasB : Bool
  secondHasA : Bool
  secondHasB : Bool
  deriving DecidableEq, Repr

def portfolioWitness : PortfolioWitness :=
  { firstHasA := true
    firstHasB := false
    secondHasA := false
    secondHasB := true }

theorem plausibleGeneratorPortfoliosCanYieldNonnestedFrontiers :
    portfolioWitness.firstHasA = true ∧
      portfolioWitness.firstHasB = false ∧
      portfolioWitness.secondHasA = false ∧
      portfolioWitness.secondHasB = true := by
  decide

structure QueryExtensionWitness where
  baseAliases : Bool
  extensionSeparates : Bool
  deriving DecidableEq, Repr

def queryExtensionWitness : QueryExtensionWitness :=
  { baseAliases := true
    extensionSeparates := true }

theorem queryExtensionCanRevealPreviouslyHiddenRival :
    queryExtensionWitness.baseAliases = true ∧
      queryExtensionWitness.extensionSeparates = true := by
  decide


structure ConditionalGuidanceWitness where
  currentFrontierExplicit : Bool
  localGuidanceAdmissible : Bool
  worldComplete : Bool
  reopenOnEscape : Bool
  deriving DecidableEq, Repr

def conditionalGuidanceWitness : ConditionalGuidanceWitness :=
  { currentFrontierExplicit := true
    localGuidanceAdmissible := true
    worldComplete := false
    reopenOnEscape := true }

theorem conditionalFrontierGuidanceDoesNotRequireWorldCompleteness :
    conditionalGuidanceWitness.currentFrontierExplicit = true ∧
      conditionalGuidanceWitness.localGuidanceAdmissible = true ∧
      conditionalGuidanceWitness.worldComplete = false ∧
      conditionalGuidanceWitness.reopenOnEscape = true := by
  decide

structure ReopeningReserveWitness where
  reserveLive : Bool
  generatorRelativeSaturation : Bool
  worldComplete : Bool
  deriving DecidableEq, Repr

def reopeningReserveWitness : ReopeningReserveWitness :=
  { reserveLive := true
    generatorRelativeSaturation := true
    worldComplete := false }

theorem reopeningReserveDoesNotEstablishFrontierCompleteness :
    reopeningReserveWitness.reserveLive = true ∧
      reopeningReserveWitness.generatorRelativeSaturation = true ∧
      reopeningReserveWitness.worldComplete = false := by
  decide

#print axioms MQR.currentRivalSeparationDoesNotImplyQueryLanguageClosure
#print axioms MQR.repeatedNoDiscoveryDoesNotImplyFrontierCompleteness
#print axioms MQR.stableFcrCanAccompanyFrontierDiscovery
#print axioms MQR.rankIncreaseAloneDoesNotEstablishDiscoveryValue
#print axioms MQR.multipleGeneratorsDoNotImplyIndependentRivalSearch
#print axioms MQR.finiteGrammarClosureDoesNotImplyScientificFrontierClosure
#print axioms MQR.plausibleGeneratorPortfoliosCanYieldNonnestedFrontiers
#print axioms MQR.queryExtensionCanRevealPreviouslyHiddenRival
#print axioms MQR.conditionalFrontierGuidanceDoesNotRequireWorldCompleteness
#print axioms MQR.reopeningReserveDoesNotEstablishFrontierCompleteness

end MQR
