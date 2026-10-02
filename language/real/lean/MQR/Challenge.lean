import Std

namespace MQR

structure ProbePortfolio where
  namedProbes : Nat
  coveredRoutes : Nat
  ancestryClasses : Nat
  deriving DecidableEq, Repr

def routeSparsePortfolio : ProbePortfolio :=
  { namedProbes := 4, coveredRoutes := 1, ancestryClasses := 1 }

def routeBroadPortfolio : ProbePortfolio :=
  { namedProbes := 4, coveredRoutes := 4, ancestryClasses := 4 }

theorem equalProbeCountsDoNotDetermineDefeatRouteCoverage :
    routeSparsePortfolio.namedProbes = routeBroadPortfolio.namedProbes ∧
    routeSparsePortfolio.coveredRoutes ≠ routeBroadPortfolio.coveredRoutes := by
  decide

theorem equalProbeCountsDoNotDetermineAncestryIndependence :
    routeSparsePortfolio.namedProbes = routeBroadPortfolio.namedProbes ∧
    routeSparsePortfolio.ancestryClasses ≠ routeBroadPortfolio.ancestryClasses := by
  decide

inductive Relation where
  | exact
  | overlap
  deriving DecidableEq, Repr

structure CherryPickWitness where
  registeredExactProbe : Bool
  registeredOverlapProbe : Bool
  selectedExactOnly : Relation
  selectedOverlapOnly : Relation
  deriving DecidableEq, Repr

def cherryPickWitness : CherryPickWitness :=
  { registeredExactProbe := true
    registeredOverlapProbe := true
    selectedExactOnly := .exact
    selectedOverlapOnly := .overlap }

theorem oneRegisteredFamilyCanSupportOppositeCherryPickedNarrowings :
    cherryPickWitness.registeredExactProbe = true ∧
    cherryPickWitness.registeredOverlapProbe = true ∧
    cherryPickWitness.selectedExactOnly ≠ cherryPickWitness.selectedOverlapOnly := by
  decide

structure CoverageWitness where
  declaredRoutesCovered : Bool
  futureChallengeSpaceComplete : Bool
  deriving DecidableEq, Repr

def coverageWitness : CoverageWitness :=
  { declaredRoutesCovered := true
    futureChallengeSpaceComplete := false }

theorem completeDeclaredRouteCoverageDoesNotImplyFutureChallengeCompleteness :
    coverageWitness.declaredRoutesCovered = true ∧
    coverageWitness.futureChallengeSpaceComplete = false := by
  decide

structure CaptureWitness where
  worldFacing : Bool
  candidateDerivedScore : Bool
  independentDiscrimination : Bool
  deriving DecidableEq, Repr

def captureWitness : CaptureWitness :=
  { worldFacing := true
    candidateDerivedScore := true
    independentDiscrimination := false }

theorem worldFacingCandidateDerivedScoringDoesNotEstablishIndependentDiscrimination :
    captureWitness.worldFacing = true ∧
    captureWitness.candidateDerivedScore = true ∧
    captureWitness.independentDiscrimination = false := by
  decide

structure ExpansionWitness where
  beforeExpansionNarrowed : Bool
  expansionConflict : Bool
  reopenRequired : Bool
  deriving DecidableEq, Repr

def expansionWitness : ExpansionWitness :=
  { beforeExpansionNarrowed := true
    expansionConflict := true
    reopenRequired := true }

theorem challengeExpansionCanReopenPriorNarrowing :
    expansionWitness.beforeExpansionNarrowed = true ∧
    expansionWitness.expansionConflict = true ∧
    expansionWitness.reopenRequired = true := by
  decide

structure StabilityWitness where
  finiteStableExpansions : Nat
  futureChallengeSpaceClosed : Bool
  deriving DecidableEq, Repr

def stabilityWitness : StabilityWitness :=
  { finiteStableExpansions := 5
    futureChallengeSpaceClosed := false }

theorem repeatedFiniteChallengeStabilityDoesNotImplyFutureClosure :
    stabilityWitness.finiteStableExpansions = 5 ∧
    stabilityWitness.futureChallengeSpaceClosed = false := by
  decide

structure WorldFacingWitness where
  worldFacing : Bool
  selectionAuthority : Bool
  deriving DecidableEq, Repr

def worldFacingWitness : WorldFacingWitness :=
  { worldFacing := true
    selectionAuthority := false }

theorem worldFacingStatusAloneDoesNotCreateSelectionAuthority :
    worldFacingWitness.worldFacing = true ∧
    worldFacingWitness.selectionAuthority = false := by
  decide

#print axioms MQR.equalProbeCountsDoNotDetermineDefeatRouteCoverage
#print axioms MQR.equalProbeCountsDoNotDetermineAncestryIndependence
#print axioms MQR.oneRegisteredFamilyCanSupportOppositeCherryPickedNarrowings
#print axioms MQR.completeDeclaredRouteCoverageDoesNotImplyFutureChallengeCompleteness
#print axioms MQR.worldFacingCandidateDerivedScoringDoesNotEstablishIndependentDiscrimination
#print axioms MQR.challengeExpansionCanReopenPriorNarrowing
#print axioms MQR.repeatedFiniteChallengeStabilityDoesNotImplyFutureClosure
#print axioms MQR.worldFacingStatusAloneDoesNotCreateSelectionAuthority

end MQR
