import Lean
namespace MQR4100Approx
theorem approximate_pair_upper
    (oldA oldB projA projB gap epsA epsB : Nat)
    (hA : oldA ≤ projA + epsA)
    (hGap : projA ≤ projB + gap)
    (hB : projB ≤ oldB + epsB) :
    oldA ≤ oldB + gap + epsA + epsB := by
  omega

theorem equal_new_observations_only_bound_old_discrepancy
    (oldA oldB projA projB epsA epsB : Nat)
    (hA1 : oldA ≤ projA + epsA)
    (hA2 : projA ≤ oldA + epsA)
    (hB1 : oldB ≤ projB + epsB)
    (hB2 : projB ≤ oldB + epsB)
    (heq : projA = projB) :
    oldA ≤ oldB + epsA + epsB ∧
    oldB ≤ oldA + epsA + epsB := by
  constructor <;> omega

theorem discrepancy_pair_extremal_example :
    (6:Nat) ≠ 4 ∧ (5:Nat) = 5 ∧
    (6:Nat) ≤ 5 + 1 ∧ (5:Nat) ≤ 4 + 1 := by
  decide

theorem overlap_count_upper_lower
    (n11 n10 n01 n00 : Nat) :
    n11 ≤ n11 + n10 ∧
    n11 ≤ n11 + n01 ∧
    (n11 + n10) + (n11 + n01) ≤
      (n11 + n10 + n01 + n00) + n11 := by
  constructor
  · omega
  constructor <;> omega

end MQR4100Approx
