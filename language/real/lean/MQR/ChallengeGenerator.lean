import Std
namespace MQR

structure ChallengePair where
  sharedAuthorityAncestry : Bool
  sharedInfrastructure : Bool
  routeDiverse : Bool
  externalWorldContact : Bool
  deriving DecidableEq, Repr

def IndependentEnough (p : ChallengePair) : Bool :=
  (!p.sharedAuthorityAncestry) && p.routeDiverse &&
  (p.externalWorldContact || (!p.sharedInfrastructure))

def commonMode : ChallengePair :=
  { sharedAuthorityAncestry := true, sharedInfrastructure := false,
    routeDiverse := true, externalWorldContact := false }

def benignSharedInfra : ChallengePair :=
  { sharedAuthorityAncestry := false, sharedInfrastructure := true,
    routeDiverse := true, externalWorldContact := true }

theorem algorithmic_route_diversity_does_not_override_common_mode :
    commonMode.routeDiverse = true ∧ IndependentEnough commonMode = false := by
  exact ⟨rfl, rfl⟩

theorem shared_infrastructure_need_not_destroy_independence :
    benignSharedInfra.sharedInfrastructure = true ∧
    IndependentEnough benignSharedInfra = true := by
  exact ⟨rfl, rfl⟩

structure SearchState where
  bounded : Bool
  witnessFound : Bool
  deriving DecidableEq, Repr

def boundedNoWitness : SearchState := { bounded := true, witnessFound := false }

def CounterexampleAbsent (s : SearchState) : Bool :=
  (!s.bounded) && (!s.witnessFound)

theorem bounded_search_failure_does_not_establish_counterexample_absence :
    boundedNoWitness.bounded = true ∧
    boundedNoWitness.witnessFound = false ∧
    CounterexampleAbsent boundedNoWitness = false := by
  exact ⟨rfl, rfl, rfl⟩

structure GeneratorState where
  novel : Bool
  claimRelevant : Bool
  postOutcomeTuned : Bool
  deriving DecidableEq, Repr

def novelIrrelevant : GeneratorState :=
  { novel := true, claimRelevant := false, postOutcomeTuned := false }

def postOutcomeRelevant : GeneratorState :=
  { novel := true, claimRelevant := true, postOutcomeTuned := true }

def ProspectiveAuthority (g : GeneratorState) : Bool :=
  g.claimRelevant && (!g.postOutcomeTuned)

theorem novelty_does_not_imply_claim_relevance :
    novelIrrelevant.novel = true ∧ novelIrrelevant.claimRelevant = false := by
  exact ⟨rfl, rfl⟩

theorem post_outcome_tuning_does_not_earn_prospective_authority :
    postOutcomeRelevant.claimRelevant = true ∧
    ProspectiveAuthority postOutcomeRelevant = false := by
  exact ⟨rfl, rfl⟩

#print axioms MQR.algorithmic_route_diversity_does_not_override_common_mode
#print axioms MQR.shared_infrastructure_need_not_destroy_independence
#print axioms MQR.bounded_search_failure_does_not_establish_counterexample_absence
#print axioms MQR.novelty_does_not_imply_claim_relevance
#print axioms MQR.post_outcome_tuning_does_not_earn_prospective_authority
end MQR
