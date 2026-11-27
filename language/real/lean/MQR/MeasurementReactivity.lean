import Std

namespace MQR.MeasurementReactivity

/-- Exact count feasibility for one baseline group, with at most k observed
    individuals changed by measurement. Missing target outcomes are unrestricted. -/
def Feasible (n m p k c : Int) : Prop :=
  ∃ t : Int, 0 ≤ t ∧ t ≤ n ∧ p-k ≤ t ∧ t ≤ p+k ∧ t ≤ c ∧ c ≤ t+m

theorem sharp_group_bounds (n m p k c : Int)
    (hn : 0 ≤ n) (hm : 0 ≤ m) (hp : 0 ≤ p)
    (hpn : p ≤ n) (hk : 0 ≤ k) :
    Feasible n m p k c ↔
      0 ≤ c ∧ p-k ≤ c ∧ c ≤ n+m ∧ c ≤ p+k+m := by
  constructor
  · rintro ⟨t, ht0, htn, htl, htu, htc, hct⟩
    exact ⟨by omega, by omega, by omega, by omega⟩
  · rintro ⟨hc0,hcl,hcn,hcu⟩
    by_cases h0 : p-k ≤ 0 ∧ c-m ≤ 0
    · exact ⟨0, by omega, by omega, by omega, by omega, by omega, by omega⟩
    · by_cases h1 : c-m ≤ p-k
      · exact ⟨p-k, by omega, by omega, by omega, by omega, by omega, by omega⟩
      · exact ⟨c-m, by omega, by omega, by omega, by omega, by omega, by omega⟩

/-- The least number of observed mismatches compatible with c is
    max(0,p-c,c-p-m). Expressed as linear constraints to avoid a hidden
    nonnegative subtraction convention. -/
theorem budget_characterization (n m p k c : Int)
    (hn : 0 ≤ n) (hm : 0 ≤ m) (hp : 0 ≤ p)
    (hpn : p ≤ n) (hk : 0 ≤ k) (hc : 0 ≤ c) (hcn : c ≤ n+m) :
    Feasible n m p k c ↔ p-c ≤ k ∧ c-p-m ≤ k := by
  rw [sharp_group_bounds n m p k c hn hm hp hpn hk]
  constructor
  · intro h
    exact ⟨by omega, by omega⟩
  · intro h
    exact ⟨hc,by omega,hcn,by omega⟩

/-- Equal sums of binary responses do not preserve association with baseline
    group. Signed contrast is group-one positives minus group-zero positives. -/
theorem average_invariance_does_not_preserve_association :
    (∃ u0 u1 v0 v1 : Int,
      0 ≤ u0 ∧ u0 ≤ 1 ∧ 0 ≤ u1 ∧ u1 ≤ 1 ∧
      0 ≤ v0 ∧ v0 ≤ 1 ∧ 0 ≤ v1 ∧ v1 ≤ 1 ∧
      u0+u1 = v0+v1 ∧ u1-u0 < 0 ∧ 0 < v1-v0) := by
  exact ⟨1,0,0,1,by decide⟩

theorem greater_budget_preserves_feasibility (n m p k l c : Int)
    (h : k ≤ l) (hf : Feasible n m p k c) : Feasible n m p l c := by
  obtain ⟨t,h0,h1,h2,h3,h4,h5⟩ := hf
  exact ⟨t,h0,h1,by omega,by omega,h4,h5⟩

/-- One common budget for distances from two admissible count intervals.
    The nine constraints are the pairwise sums of three lower bounds each. -/
def JointBudget (l u a b z k : Int) : Prop :=
  ∃ x y : Int, 0 ≤ x ∧ l-z ≤ x ∧ z-u ≤ x ∧
    0 ≤ y ∧ a-z ≤ y ∧ z-b ≤ y ∧ x+y ≤ k

theorem joint_budget_elimination (l u a b z k : Int) :
    JointBudget l u a b z k ↔
      0 ≤ k ∧ l-z ≤ k ∧ z-u ≤ k ∧ a-z ≤ k ∧ z-b ≤ k ∧
      l+a-2*z ≤ k ∧ 2*z-u-b ≤ k ∧ l-b ≤ k ∧ a-u ≤ k := by
  constructor
  · rintro ⟨x,y,hx0,hxl,hxu,hy0,hyl,hyu,hk⟩
    exact ⟨by omega,by omega,by omega,by omega,by omega,
      by omega,by omega,by omega,by omega⟩
  · rintro ⟨hk,h1,h2,h3,h4,h5,h6,h7,h8⟩
    by_cases hx : l-z ≤ 0 ∧ z-u ≤ 0
    · exact ⟨0,k,by omega,by omega,by omega,by omega,by omega,by omega,by omega⟩
    · by_cases hy : z-u ≤ l-z
      · exact ⟨l-z,k-(l-z),by omega,by omega,by omega,by omega,by omega,by omega,by omega⟩
      · exact ⟨z-u,k-(z-u),by omega,by omega,by omega,by omega,by omega,by omega,by omega⟩

/-- If measurement can only increase a binary count, equality of margins
    rules out any 0-to-1 changes. Without monotonicity it does not. -/
theorem one_sided_equal_margin_no_change (up down : Int)
    (hdown : down = 0) (hequal : up-down = 0) : up = 0 := by omega

theorem equal_margin_can_hide_changes :
    ∀ n : Nat, ∃ up down : Nat, up = down ∧ up+down = 2*n := by
  intro n
  exact ⟨n,n,rfl,by omega⟩

/-- Nested observations with the same absolute budget preserve restrictions:
    new positives cannot decrease and new positives + missing cannot increase. -/
theorem nested_observation_preserves_restrictions
    (n m p n' m' p' k c : Int)
    (hn : 0 ≤ n) (hm : 0 ≤ m) (hp : 0 ≤ p) (hpn : p ≤ n)
    (hn' : 0 ≤ n') (hm' : 0 ≤ m') (hp' : 0 ≤ p') (hpn' : p' ≤ n')
    (hk : 0 ≤ k) (hsize : n+m = n'+m')
    (hpos : p ≤ p') (hupper : p'+m' ≤ p+m)
    (h : Feasible n' m' p' k c) : Feasible n m p k c := by
  have hnew := (sharp_group_bounds n' m' p' k c hn' hm' hp' hpn' hk).mp h
  apply (sharp_group_bounds n m p k c hn hm hp hpn hk).mpr
  exact ⟨by omega,by omega,by omega,by omega⟩

/-- One admissible latent count is excluded by the old absolute budget
    yet admitted after the protocol increases the budget. -/
theorem coverage_with_larger_budget_can_lose_restriction :
    ¬ Feasible 3 1 0 1 3 ∧ Feasible 4 0 1 2 3 := by
  constructor
  · rintro ⟨t,h0,h1,h2,h3,h4,h5⟩
    omega
  · exact ⟨3,by decide,by decide,by decide,by decide,by decide,by decide⟩

#print axioms nested_observation_preserves_restrictions
#print axioms coverage_with_larger_budget_can_lose_restriction
#print axioms joint_budget_elimination
#print axioms one_sided_equal_margin_no_change
#print axioms equal_margin_can_hide_changes
#print axioms sharp_group_bounds
#print axioms budget_characterization
#print axioms average_invariance_does_not_preserve_association
#print axioms greater_budget_preserves_feasibility

end MQR.MeasurementReactivity
