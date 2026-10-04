import Std

namespace MQR

inductive PerturbationStatus where
  | admissibleFailure
  | scientificDebt
  | rejectedIncoherent
  | rejectedIrrelevant
  | postOutcomeHold
  | scopeTransportHold
  deriving DecidableEq, Repr

structure EnvelopeEntry where
  coherent : Bool
  claimRelevant : Bool
  independentMotivation : Bool
  executable : Bool
  scopePreserved : Bool
  deriving DecidableEq, Repr

def admissibleFailure (e : EnvelopeEntry) : Bool :=
  e.coherent && e.claimRelevant && e.independentMotivation && e.scopePreserved

def scientificDebt (e : EnvelopeEntry) : Bool :=
  e.coherent && e.claimRelevant && e.independentMotivation && (!e.executable) && e.scopePreserved

def defeatsSameScope (e : EnvelopeEntry) : Bool :=
  admissibleFailure e

def blockedButRelevant : EnvelopeEntry :=
  { coherent := true
    claimRelevant := true
    independentMotivation := true
    executable := false
    scopePreserved := true }

def incoherentExtreme : EnvelopeEntry :=
  { coherent := false
    claimRelevant := true
    independentMotivation := true
    executable := true
    scopePreserved := true }

def scopeDrift : EnvelopeEntry :=
  { coherent := true
    claimRelevant := true
    independentMotivation := true
    executable := true
    scopePreserved := false }

theorem execution_block_does_not_imply_scientific_irrelevance :
    blockedButRelevant.executable = false ∧
    blockedButRelevant.claimRelevant = true ∧
    scientificDebt blockedButRelevant = true := by
  exact ⟨rfl, rfl, rfl⟩

theorem incoherent_extremity_does_not_defeat_same_scope :
    incoherentExtreme.claimRelevant = true ∧
    defeatsSameScope incoherentExtreme = false := by
  exact ⟨rfl, rfl⟩

theorem scope_changing_perturbation_requires_transport :
    scopeDrift.coherent = true ∧
    scopeDrift.claimRelevant = true ∧
    defeatsSameScope scopeDrift = false := by
  exact ⟨rfl, rfl, rfl⟩

structure CertificateState where
  validAtOldEnvelope : Bool
  successorAuthorityOpen : Bool
  deriving DecidableEq, Repr

def afterAdmissibleExpansion : CertificateState :=
  { validAtOldEnvelope := true
    successorAuthorityOpen := true }

theorem later_expansion_can_reopen_without_retroactive_falsehood :
    afterAdmissibleExpansion.validAtOldEnvelope = true ∧
    afterAdmissibleExpansion.successorAuthorityOpen = true := by
  exact ⟨rfl, rfl⟩

structure EnvelopeClosure where
  finiteEnumerated : Bool
  independentlyScopedComplete : Bool
  deriving DecidableEq, Repr

def finiteOnly : EnvelopeClosure :=
  { finiteEnumerated := true
    independentlyScopedComplete := false }

def OpenWorldComplete (e : EnvelopeClosure) : Bool :=
  e.finiteEnumerated && e.independentlyScopedComplete

theorem finite_stress_saturation_does_not_force_open_world_completeness :
    finiteOnly.finiteEnumerated = true ∧
    OpenWorldComplete finiteOnly = false := by
  exact ⟨rfl, rfl⟩

structure EnvelopeComparison where
  moreTests : Bool
  oldLiveDistinctionsPreserved : Bool
  addedTestsClaimRelevant : Bool
  deriving DecidableEq, Repr

def biggerButWorse : EnvelopeComparison :=
  { moreTests := true
    oldLiveDistinctionsPreserved := false
    addedTestsClaimRelevant := false }

def StrongerEnvelope (e : EnvelopeComparison) : Bool :=
  e.oldLiveDistinctionsPreserved && e.addedTestsClaimRelevant

theorem more_stress_tests_do_not_force_stronger_envelope :
    biggerButWorse.moreTests = true ∧
    StrongerEnvelope biggerButWorse = false := by
  exact ⟨rfl, rfl⟩

#print axioms MQR.execution_block_does_not_imply_scientific_irrelevance
#print axioms MQR.incoherent_extremity_does_not_defeat_same_scope
#print axioms MQR.scope_changing_perturbation_requires_transport
#print axioms MQR.later_expansion_can_reopen_without_retroactive_falsehood
#print axioms MQR.finite_stress_saturation_does_not_force_open_world_completeness
#print axioms MQR.more_stress_tests_do_not_force_stronger_envelope

end MQR
