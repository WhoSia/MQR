import Std

namespace MQR

structure AuthorityMode where
  claimFrozen : Bool
  probeActive : Bool
  provisionalUse : Bool
  deriving DecidableEq, Repr

def claimFreezeProbeActive : AuthorityMode :=
  { claimFrozen := true, probeActive := true, provisionalUse := false }

theorem claimFreezeCanCoexistWithActiveInquiry :
    claimFreezeProbeActive.claimFrozen = true ∧
    claimFreezeProbeActive.probeActive = true := by
  decide

structure BinaryProjectionWitness where
  first : AuthorityMode
  second : AuthorityMode
  firstBinaryStop : Bool
  secondBinaryStop : Bool
  deriving DecidableEq, Repr

def binaryProjectionWitness : BinaryProjectionWitness :=
  { first := { claimFrozen := true, probeActive := true, provisionalUse := false },
    second := { claimFrozen := true, probeActive := false, provisionalUse := false },
    firstBinaryStop := true,
    secondBinaryStop := true }

theorem binaryStopProjectionCanEraseProbeState :
    binaryProjectionWitness.first ≠ binaryProjectionWitness.second ∧
    binaryProjectionWitness.firstBinaryStop =
      binaryProjectionWitness.secondBinaryStop := by
  decide

structure LagGranularityWitness where
  sameWorldState : Bool
  originalLagOneStops : Bool
  duplicatedInertCheckpointLagOneStops : Bool
  deriving DecidableEq, Repr

def lagGranularityWitness : LagGranularityWitness :=
  { sameWorldState := true,
    originalLagOneStops := false,
    duplicatedInertCheckpointLagOneStops := true }

theorem inertCheckpointRefinementCanChangeLagOneWithoutWorldChange :
    lagGranularityWitness.sameWorldState = true ∧
    lagGranularityWitness.originalLagOneStops = false ∧
    lagGranularityWitness.duplicatedInertCheckpointLagOneStops = true := by
  decide

structure PartialWindowWitness where
  earliest : Nat
  latest : Nat
  uniqueStopIdentified : Bool
  deriving DecidableEq, Repr

def partialWindowWitness : PartialWindowWitness :=
  { earliest := 3, latest := 5, uniqueStopIdentified := false }

theorem nondegenerateStopWindowDoesNotIdentifyUniqueStopTime :
    partialWindowWitness.earliest < partialWindowWitness.latest ∧
    partialWindowWitness.uniqueStopIdentified = false := by
  decide

structure HistoricalActionWitness where
  historicalFreeze : Bool
  scorerGoldByHistory : Bool
  independentWorldAdjudicationRequired : Bool
  deriving DecidableEq, Repr

def historicalActionWitness : HistoricalActionWitness :=
  { historicalFreeze := true,
    scorerGoldByHistory := false,
    independentWorldAdjudicationRequired := true }

theorem historicalActionDoesNotConstituteGold :
    historicalActionWitness.historicalFreeze = true ∧
    historicalActionWitness.scorerGoldByHistory = false ∧
    historicalActionWitness.independentWorldAdjudicationRequired = true := by
  decide

structure ContractWitness where
  sameEvidence : Bool
  treatmentUseAuthorized : Bool
  universalMechanismClosed : Bool
  deriving DecidableEq, Repr

def contractWitness : ContractWitness :=
  { sameEvidence := true,
    treatmentUseAuthorized := true,
    universalMechanismClosed := false }

theorem actionAuthorityCanPrecedeUniversalMechanisticClosure :
    contractWitness.sameEvidence = true ∧
    contractWitness.treatmentUseAuthorized = true ∧
    contractWitness.universalMechanismClosed = false := by
  decide

structure PositiveConvergenceWitness where
  independentConvergence : Bool
  falsifierPresent : Bool
  localClaimFreeze : Bool
  deriving DecidableEq, Repr

def positiveConvergenceWitness : PositiveConvergenceWitness :=
  { independentConvergence := true,
    falsifierPresent := false,
    localClaimFreeze := true }

theorem positiveConvergenceCanSupportClosureWithoutFalsifier :
    positiveConvergenceWitness.independentConvergence = true ∧
    positiveConvergenceWitness.falsifierPresent = false ∧
    positiveConvergenceWitness.localClaimFreeze = true := by
  decide

structure NaturalisticTransportWitness where
  sourceTemporalReconstruction : Bool
  fiveClaimWindowsCompatible : Bool
  binaryOntologyTransported : Bool
  eventCountLagInvariant : Bool
  prospectiveExternalValidation : Bool
  deriving DecidableEq, Repr

def naturalisticTransportWitness : NaturalisticTransportWitness :=
  { sourceTemporalReconstruction := true,
    fiveClaimWindowsCompatible := true,
    binaryOntologyTransported := false,
    eventCountLagInvariant := false,
    prospectiveExternalValidation := false }

theorem partialHistoricalCompatibilityDoesNotEstablishExternalCalibration :
    naturalisticTransportWitness.sourceTemporalReconstruction = true ∧
    naturalisticTransportWitness.fiveClaimWindowsCompatible = true ∧
    naturalisticTransportWitness.binaryOntologyTransported = false ∧
    naturalisticTransportWitness.eventCountLagInvariant = false ∧
    naturalisticTransportWitness.prospectiveExternalValidation = false := by
  decide

#print axioms MQR.claimFreezeCanCoexistWithActiveInquiry
#print axioms MQR.binaryStopProjectionCanEraseProbeState
#print axioms MQR.inertCheckpointRefinementCanChangeLagOneWithoutWorldChange
#print axioms MQR.nondegenerateStopWindowDoesNotIdentifyUniqueStopTime
#print axioms MQR.historicalActionDoesNotConstituteGold
#print axioms MQR.actionAuthorityCanPrecedeUniversalMechanisticClosure
#print axioms MQR.positiveConvergenceCanSupportClosureWithoutFalsifier
#print axioms MQR.partialHistoricalCompatibilityDoesNotEstablishExternalCalibration

end MQR
