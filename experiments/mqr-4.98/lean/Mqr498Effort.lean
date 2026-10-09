import Lean

/-!
MQR-4.98. A zero-truncated field source records only those 3-window
encounter histories whose masks are nonzero. The observed list cannot
identify the true number of 000 birds, even if each of the three intervals
has a known duration (5 minutes). All claims are conditional elementary
math/logic, not an ecological occupancy theorem.
-/
namespace MQR498

def observed (fullHistories : List Nat) : List Nat :=
  fullHistories.filter (fun mask => mask != 0)

theorem unseen_zero_birds_are_observationally_erased :
  observed [1, 5] = observed [0, 1, 0, 5] := by decide

theorem different_latent_population_counts_same_capture_record :
  observed [1, 5] = observed [0, 1, 0, 5] ∧
    [1, 5].length ≠ [0, 1, 0, 5].length := by
  decide

def seenInThree (first second third : Bool) : Bool :=
  first || second || third

theorem all_three_not_detected_creates_missing_individual :
  seenInThree false false false = false := by rfl

theorem later_detection_is_not_early_detection :
  seenInThree false false true = true ∧
  (false || false) = false := by decide

/-!
For a rational conditional detection probability p=1/2 each FIVE-MINUTE
interval, independence would give missed probability (1/2)^2=1/4 in
TWO intervals and (1/2)^3=1/8 in THREE intervals.
The next Nat equalities encode exact numerator identities under this
stipulated same-p model. They do not show real field independence.
-/
def missedNumerator (perWindowMissN : Nat) (visits : Nat) : Nat :=
  perWindowMissN ^ visits

theorem independent_two_windows_miss_probability_quarters :
  missedNumerator 1 2 = 1 ∧
  (2:Nat)^2 = 4 := by decide

theorem independent_three_windows_miss_probability_eighths :
  missedNumerator 1 3 = 1 ∧
  (2:Nat)^3 = 8 := by decide

structure FieldProtocol where
  source : Nat
  effortMinutes : Nat
  geography : Option Nat
deriving DecidableEq

def dropProtocol (p : FieldProtocol) : Nat :=
  p.source

theorem measured_bird_calls_do_not_recover_unsupplied_effort_minutes :
  dropProtocol ⟨7, 5, none⟩ = dropProtocol ⟨7, 15, none⟩ ∧
  (⟨7, 5, none⟩ : FieldProtocol) ≠ ⟨7, 15, none⟩ := by decide

theorem source_identifier_does_not_fix_unobserved_spatial_footprint :
  dropProtocol ⟨8, 15, none⟩ = dropProtocol ⟨8, 15, some 125⟩ ∧
  (⟨8, 15, none⟩ : FieldProtocol) ≠ ⟨8, 15, some 125⟩ := by decide

end MQR498
