import Std

namespace MQR

inductive Severity where
  | none
  | bounded
  | material
  | fatal
  deriving DecidableEq, Repr

def Severity.rank : Severity → Nat
  | .none => 0
  | .bounded => 1
  | .material => 2
  | .fatal => 3

def Severity.le (a b : Severity) : Prop := a.rank ≤ b.rank

structure TypedLoss where
  sep : Severity
  reopen : Severity
  prov : Severity
  ext : Severity
  release : Severity
  deriving DecidableEq, Repr

def ComponentwiseLe (a b : TypedLoss) : Prop :=
  Severity.le a.sep b.sep ∧
  Severity.le a.reopen b.reopen ∧
  Severity.le a.prov b.prov ∧
  Severity.le a.ext b.ext ∧
  Severity.le a.release b.release

def HardForbid (l : TypedLoss) : Prop :=
  l.release = .fatal

def HardReexpand (l : TypedLoss) : Prop :=
  l.reopen = .fatal

def HardReopen (l : TypedLoss) : Prop :=
  l.prov = .fatal ∨ l.ext = .fatal

def ComponentwiseAdmissible (loss budget : TypedLoss) : Prop :=
  ComponentwiseLe loss budget ∧
  ¬ HardForbid loss ∧
  ¬ HardReexpand loss ∧
  ¬ HardReopen loss

/--
If a loss profile is componentwise admissible, any coordinatewise-weaker profile
remains within the same componentwise budget. This theorem says nothing about
whether the budget itself is scientifically justified.
-/
theorem weakening_preserves_budget
    {loss weaker budget : TypedLoss}
    (hweak : ComponentwiseLe weaker loss)
    (hadm : ComponentwiseAdmissible loss budget) :
    ComponentwiseLe weaker budget := by
  rcases hweak with ⟨hs, hr, hp, he, hx⟩
  rcases hadm.1 with ⟨bs, br, bp, be, bx⟩
  constructor
  · exact Nat.le_trans hs bs
  constructor
  · exact Nat.le_trans hr br
  constructor
  · exact Nat.le_trans hp bp
  constructor
  · exact Nat.le_trans he be
  · exact Nat.le_trans hx bx

/--
A fatal release-coordinate loss cannot be made componentwise admissible by
improving unrelated coordinates.
-/
theorem fatal_release_forbids
    (loss budget : TypedLoss)
    (hf : loss.release = .fatal) :
    ¬ ComponentwiseAdmissible loss budget := by
  intro h
  exact h.2.1 hf

/--
A fatal reopening-coordinate loss cannot be made admissible by unrelated
coordinate improvements.
-/
theorem fatal_reopen_reexpands
    (loss budget : TypedLoss)
    (hf : loss.reopen = .fatal) :
    ¬ ComponentwiseAdmissible loss budget := by
  intro h
  exact h.2.2.1 hf

/--
Fatal provenance or exterior-route loss blocks componentwise admissibility.
No cross-coordinate weighted compensation appears in the statement.
-/
theorem fatal_prov_or_ext_reopens
    (loss budget : TypedLoss)
    (hf : loss.prov = .fatal ∨ loss.ext = .fatal) :
    ¬ ComponentwiseAdmissible loss budget := by
  intro h
  exact h.2.2.2 hf

#print axioms MQR.weakening_preserves_budget
#print axioms MQR.fatal_release_forbids
#print axioms MQR.fatal_reopen_reexpands
#print axioms MQR.fatal_prov_or_ext_reopens

end MQR
