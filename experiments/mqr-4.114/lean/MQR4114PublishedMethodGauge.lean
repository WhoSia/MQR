/-
MQR-4.114 P2-C (Carstensen 2010 printed pair model): an external-origin gauge.
Formal domain: exact integers, deterministic affine model only.
This is an old algebraic identity, NOT a proof of external calibration history.
-/
import Lean

namespace MQR4114P2C

def reported (methodIntercept methodSlope latentQuantity residual : Int) : Int :=
  methodIntercept + methodSlope * latentQuantity + residual

theorem affine_reference_shift_invariant
    (α β θ ε c : Int) :
    reported (α - β * c) β (θ + c) ε = reported α β θ ε := by
  unfold reported
  calc
    (α - β*c) + β*(θ+c) + ε
       = (α - β*c) + (β*θ + β*c) + ε := by rw [mul_add]
    _ = ((α - β*c) + β*c) + β*θ + ε := by ac_rfl
    _ = α + β*θ + ε := by simp

theorem both_methods_same_printed_pair_under_shift
    (α₁ β₁ ε₁ α₂ β₂ ε₂ θ c : Int) :
    (reported (α₁ - β₁*c) β₁ (θ+c) ε₁,
     reported (α₂ - β₂*c) β₂ (θ+c) ε₂) =
    (reported α₁ β₁ θ ε₁, reported α₂ β₂ θ ε₂) := by
  simp [affine_reference_shift_invariant]

-- A mathematical invariance does not make the two representations
-- physically exchangeable without an externally verified reference.
theorem unknown_origin_even_with_multiple_methods
    (α₁ β₁ ε₁ α₂ β₂ ε₂ α₃ β₃ ε₃ θ c : Int) :
    (reported (α₁ - β₁*c) β₁ (θ+c) ε₁,
      reported (α₂ - β₂*c) β₂ (θ+c) ε₂,
      reported (α₃ - β₃*c) β₃ (θ+c) ε₃) =
    (reported α₁ β₁ θ ε₁, reported α₂ β₂ θ ε₂,
      reported α₃ β₃ θ ε₃) := by
  simp [affine_reference_shift_invariant]

end MQR4114P2C
