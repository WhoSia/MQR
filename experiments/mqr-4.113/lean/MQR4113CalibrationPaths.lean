/-!
MQR-4.113 P2-A — Lean 4 finite calibration order and inverse-history firewall.
Scope: constructed integer kernels only; no physical measurement assertion.
Rust holds the executable rational stochastic validation; these statements
independently check arithmetic witnesses and the general noninjectivity rule.
-/

namespace MQR4113P2

def cd00 : Nat := 3 * 2 + 1 * 1
def cd01 : Nat := 3 * 0 + 1 * 1
def cd10 : Nat := 1 * 2 + 3 * 1
def cd11 : Nat := 1 * 0 + 3 * 1

def dc00 : Nat := 2 * 3 + 0 * 1
def dc01 : Nat := 2 * 1 + 0 * 3
def dc10 : Nat := 1 * 3 + 1 * 1
def dc11 : Nat := 1 * 1 + 1 * 3

theorem cd_exact : cd00 = 7 ∧ cd01 = 1 ∧ cd10 = 5 ∧ cd11 = 3 := by
  decide

theorem dc_exact : dc00 = 6 ∧ dc01 = 2 ∧ dc10 = 4 ∧ dc11 = 4 := by
  decide

theorem composition_order_matters : cd00 ≠ dc00 := by
  decide

-- Two error-one-quarter kernels in sequence:
-- numerator [[10,6],[6,10]] over denominator 16,
-- equivalent to a one-stage [[5,3],[3,5]] over denominator 8.
theorem distinct_factorizations_same_endpoint :
    (10 : Nat) * 8 = 5 * 16 ∧
    (6 : Nat) * 8 = 3 * 16 := by
  decide

theorem observational_equivalence_blocks_path_identification
    {Path Observation : Type}
    (observe : Path → Observation)
    (history₁ history₂ : Path)
    (distinct : history₁ ≠ history₂)
    (same : observe history₁ = observe history₂) :
    ¬ Function.Injective observe := by
  intro injective
  exact distinct (injective same)

end MQR4113P2
