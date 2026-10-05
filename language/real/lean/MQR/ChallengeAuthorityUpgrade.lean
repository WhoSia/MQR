import Std
namespace MQR

structure UpgradeReceipt where
  sourceInternal : Bool
  challengeCorresponds : Bool
  relevantDependencyBroken : Bool
  postOutcomeTuned : Bool
  residualCommonMode : Bool
  deriving DecidableEq, Repr

def LocalUpgrade (r : UpgradeReceipt) : Bool :=
  r.sourceInternal &&
  r.challengeCorresponds &&
  r.relevantDependencyBroken &&
  (!r.postOutcomeTuned)

def CrossRouteUpgrade (r : UpgradeReceipt) : Bool :=
  LocalUpgrade r && (!r.residualCommonMode)

def internalThenExternal : UpgradeReceipt :=
  { sourceInternal := true
    challengeCorresponds := true
    relevantDependencyBroken := true
    postOutcomeTuned := false
    residualCommonMode := true }

def mereExternalHosting : UpgradeReceipt :=
  { sourceInternal := true
    challengeCorresponds := true
    relevantDependencyBroken := false
    postOutcomeTuned := false
    residualCommonMode := true }

def crossRouteWitness : UpgradeReceipt :=
  { sourceInternal := true
    challengeCorresponds := true
    relevantDependencyBroken := true
    postOutcomeTuned := false
    residualCommonMode := false }

theorem later_upgrade_does_not_rewrite_internal_origin :
    internalThenExternal.sourceInternal = true ∧
    LocalUpgrade internalThenExternal = true := by
  exact ⟨rfl, rfl⟩

theorem externality_without_relevant_cut_does_not_upgrade :
    mereExternalHosting.challengeCorresponds = true ∧
    LocalUpgrade mereExternalHosting = false := by
  exact ⟨rfl, rfl⟩

theorem residual_common_mode_blocks_cross_route_upgrade :
    LocalUpgrade internalThenExternal = true ∧
    CrossRouteUpgrade internalThenExternal = false := by
  exact ⟨rfl, rfl⟩

theorem independent_route_cut_can_upgrade_without_origin_laundering :
    crossRouteWitness.sourceInternal = true ∧
    CrossRouteUpgrade crossRouteWitness = true := by
  exact ⟨rfl, rfl⟩

structure WitnessBundle where
  witnessCount : Nat
  sharedAuthorityAncestry : Bool
  deriving DecidableEq, Repr

def EffectiveWitnessMultiplicity (w : WitnessBundle) : Nat :=
  if w.sharedAuthorityAncestry then
    if w.witnessCount = 0 then 0 else 1
  else
    w.witnessCount

def collapsedThree : WitnessBundle :=
  { witnessCount := 3, sharedAuthorityAncestry := true }

theorem ancestry_merge_can_collapse_witness_multiplicity :
    collapsedThree.witnessCount = 3 ∧
    EffectiveWitnessMultiplicity collapsedThree = 1 := by
  exact ⟨rfl, rfl⟩

structure UpgradeCertificate where
  currentPass : Bool
  ancestryRevisionDefeats : Bool
  deriving DecidableEq, Repr

def CertificateStillLive (c : UpgradeCertificate) : Bool :=
  c.currentPass && (!c.ancestryRevisionDefeats)

def defeatedCertificate : UpgradeCertificate :=
  { currentPass := true, ancestryRevisionDefeats := true }

theorem independence_certificate_is_defeasible :
    defeatedCertificate.currentPass = true ∧
    CertificateStillLive defeatedCertificate = false := by
  exact ⟨rfl, rfl⟩

#print axioms MQR.later_upgrade_does_not_rewrite_internal_origin
#print axioms MQR.externality_without_relevant_cut_does_not_upgrade
#print axioms MQR.residual_common_mode_blocks_cross_route_upgrade
#print axioms MQR.independent_route_cut_can_upgrade_without_origin_laundering
#print axioms MQR.ancestry_merge_can_collapse_witness_multiplicity
#print axioms MQR.independence_certificate_is_defeasible
end MQR
