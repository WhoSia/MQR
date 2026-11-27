import Std

namespace MQR.ReusableInquiry

/-- Equal-quality answers in both routes; the reusable route pays an
    upfront premium and avoids a fixed additional cost on each later task. -/
def directCost (initial base saving tasks : Nat) : Nat :=
  initial + tasks * base + tasks * saving

def reusableCost (initial base premium tasks : Nat) : Nat :=
  initial + tasks * base + premium

theorem reusable_wins_iff (a b p s n : Nat) :
    reusableCost a b p n < directCost a b s n ↔ p < n*s := by
  unfold reusableCost directCost
  omega

theorem costs_tie_iff (a b p s n : Nat) :
    reusableCost a b p n = directCost a b s n ↔ p = n*s := by
  unfold reusableCost directCost
  omega

theorem immediate_cost_prefers_direct (a b p s : Nat) (hp : 0 < p) :
    directCost a b s 0 < reusableCost a b p 0 := by
  simp [directCost, reusableCost]
  omega

/-- No finite universal additive regret bound for the immediate-cost choice
    even with unit premium and unit reuse saving. -/
theorem immediate_choice_unbounded_regret (r : Nat) :
    ∃ n : Nat, reusableCost 1 1 1 n + r < directCost 1 1 1 n := by
  refine ⟨r+2, ?_⟩
  simp [reusableCost, directCost]
  omega

theorem direct_weakly_optimal_at_smaller_horizon (a b p s n h : Nat)
    (hn : n ≤ h) (hp : h*s ≤ p) :
    directCost a b s n ≤ reusableCost a b p n := by
  have hs : n*s ≤ h*s := Nat.mul_le_mul_right s hn
  unfold directCost reusableCost
  omega

theorem reuse_weakly_optimal_at_larger_horizon (a b p s n l : Nat)
    (hl : l ≤ n) (hp : p ≤ l*s) :
    reusableCost a b p n ≤ directCost a b s n := by
  have hs : l*s ≤ n*s := Nat.mul_le_mul_right s hl
  unfold directCost reusableCost
  omega

#print axioms reusable_wins_iff
#print axioms costs_tie_iff
#print axioms immediate_cost_prefers_direct
#print axioms immediate_choice_unbounded_regret
#print axioms direct_weakly_optimal_at_smaller_horizon
#print axioms reuse_weakly_optimal_at_larger_horizon

end MQR.ReusableInquiry
