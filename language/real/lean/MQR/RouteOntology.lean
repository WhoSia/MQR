import Std

namespace MQR

structure RouteCountWitness where
  routeCountA : Nat
  routeCountB : Nat
  defeatContentA : Nat
  defeatContentB : Nat
  deriving DecidableEq, Repr

def equalCountDifferentContent : RouteCountWitness :=
  { routeCountA := 2, routeCountB := 2, defeatContentA := 2, defeatContentB := 3 }

theorem equalRouteCountsDoNotImplyEqualDefeatContent :
    equalCountDifferentContent.routeCountA = equalCountDifferentContent.routeCountB ∧
    equalCountDifferentContent.defeatContentA ≠ equalCountDifferentContent.defeatContentB := by
  decide

structure CoverageFractionWitness where
  coveredA : Nat
  totalA : Nat
  coveredB : Nat
  totalB : Nat
  equivalent : Bool
  deriving DecidableEq, Repr

def equalFractionDifferentCoverage : CoverageFractionWitness :=
  { coveredA := 1, totalA := 2, coveredB := 1, totalB := 2, equivalent := false }

theorem equalCoverageFractionsDoNotImplyCoverageEquivalence :
    equalFractionDifferentCoverage.coveredA = equalFractionDifferentCoverage.coveredB ∧
    equalFractionDifferentCoverage.totalA = equalFractionDifferentCoverage.totalB ∧
    equalFractionDifferentCoverage.equivalent = false := by
  decide

structure SplitWitness where
  sourceRoutes : Nat
  targetRoutes : Nat
  sourceContents : Nat
  targetContents : Nat
  deriving DecidableEq, Repr

def splitWitness : SplitWitness :=
  { sourceRoutes := 1, targetRoutes := 5, sourceContents := 1, targetContents := 1 }

theorem splittingOneRouteDoesNotCreateNewDefeatContent :
    splitWitness.sourceRoutes = 1 ∧
    splitWitness.targetRoutes = 5 ∧
    splitWitness.sourceContents = splitWitness.targetContents := by
  decide

structure MergeWitness where
  sourceContents : Nat
  coveredSourceContents : Nat
  mergedTargetContents : Nat
  fullCoverageDischarged : Bool
  deriving DecidableEq, Repr

def mergeWitness : MergeWitness :=
  { sourceContents := 2, coveredSourceContents := 1, mergedTargetContents := 2, fullCoverageDischarged := false }

theorem mergingRoutesDoesNotDischargeUncoveredPredecessorContent :
    mergeWitness.sourceContents = 2 ∧
    mergeWitness.coveredSourceContents = 1 ∧
    mergeWitness.mergedTargetContents = 2 ∧
    mergeWitness.fullCoverageDischarged = false := by
  decide

structure LabelDriftWitness where
  sameLabel : Bool
  sameDefeatContent : Bool
  deriving DecidableEq, Repr

def labelDriftWitness : LabelDriftWitness :=
  { sameLabel := true, sameDefeatContent := false }

theorem sameRouteLabelDoesNotGuaranteeRouteIdentity :
    labelDriftWitness.sameLabel = true ∧
    labelDriftWitness.sameDefeatContent = false := by
  decide

structure AliasWitness where
  sameLabel : Bool
  sameDefeatContent : Bool
  deriving DecidableEq, Repr

def aliasWitness : AliasWitness :=
  { sameLabel := false, sameDefeatContent := true }

theorem differentRouteLabelsCanPreserveDeclaredDefeatContent :
    aliasWitness.sameLabel = false ∧
    aliasWitness.sameDefeatContent = true := by
  decide

structure RefinementWitness where
  sourceContentCount : Nat
  targetContentCount : Nat
  transportedContentCount : Nat
  coveragePreserved : Bool
  deriving DecidableEq, Repr

def refinementWitness : RefinementWitness :=
  { sourceContentCount := 2, targetContentCount := 2, transportedContentCount := 2, coveragePreserved := true }

theorem contentPreservingRefinementCanPreserveLocalCoverage :
    refinementWitness.sourceContentCount = refinementWitness.targetContentCount ∧
    refinementWitness.transportedContentCount = refinementWitness.sourceContentCount ∧
    refinementWitness.coveragePreserved = true := by
  decide

structure HiddenRouteWitness where
  priorScopedResultRetained : Bool
  affectedCoverageReopened : Bool
  finalDefeatSpaceClosed : Bool
  deriving DecidableEq, Repr

def hiddenRouteWitness : HiddenRouteWitness :=
  { priorScopedResultRetained := true, affectedCoverageReopened := true, finalDefeatSpaceClosed := false }

theorem hiddenRouteDiscoveryCanReopenLocallyWithoutGlobalNegation :
    hiddenRouteWitness.priorScopedResultRetained = true ∧
    hiddenRouteWitness.affectedCoverageReopened = true ∧
    hiddenRouteWitness.finalDefeatSpaceClosed = false := by
  decide

structure RouteStabilityWitness where
  finiteStableRevisions : Nat
  futureDefeatSpaceClosed : Bool
  deriving DecidableEq, Repr

def routeStabilityWitness : RouteStabilityWitness :=
  { finiteStableRevisions := 6, futureDefeatSpaceClosed := false }

theorem repeatedFiniteRouteStabilityDoesNotImplyFutureDefeatClosure :
    routeStabilityWitness.finiteStableRevisions = 6 ∧
    routeStabilityWitness.futureDefeatSpaceClosed = false := by
  decide

#print axioms MQR.equalRouteCountsDoNotImplyEqualDefeatContent
#print axioms MQR.equalCoverageFractionsDoNotImplyCoverageEquivalence
#print axioms MQR.splittingOneRouteDoesNotCreateNewDefeatContent
#print axioms MQR.mergingRoutesDoesNotDischargeUncoveredPredecessorContent
#print axioms MQR.sameRouteLabelDoesNotGuaranteeRouteIdentity
#print axioms MQR.differentRouteLabelsCanPreserveDeclaredDefeatContent
#print axioms MQR.contentPreservingRefinementCanPreserveLocalCoverage
#print axioms MQR.hiddenRouteDiscoveryCanReopenLocallyWithoutGlobalNegation
#print axioms MQR.repeatedFiniteRouteStabilityDoesNotImplyFutureDefeatClosure

end MQR
