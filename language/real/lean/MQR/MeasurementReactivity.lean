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
    let t := max 0 (max (p-k) (c-m))
    have h0 : 0 ≤ t := le_max_left _ _
    have h1 : p-k ≤ t := le_trans (le_max_left _ _) (le_max_right _ _)
    have h2 : c-m ≤ t := le_trans (le_max_right _ _) (le_max_right _ _)
    have hn' : t ≤ n := max_le hn (max_le (by omega) (by omega))
    have hu : t ≤ p+k := max_le (by omega) (max_le (by omega) (by omega))
    have hc : t ≤ c := max_le hc0 (max_le hcl (by omega))
    exact ⟨t,h0,hn',h1,hu,hc,by omega⟩

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

#print axioms sharp_group_bounds
#print axioms budget_characterization
#print axioms average_invariance_does_not_preserve_association
#print axioms greater_budget_preserves_feasibility

end MQR.MeasurementReactivity
