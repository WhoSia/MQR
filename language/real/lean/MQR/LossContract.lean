import Std

namespace MQR

inductive LossSeverity where
  | none
  | bounded
  | material
  | fatal
  deriving DecidableEq, Repr

def LossSeverity.rank : LossSeverity → Nat
  | .none => 0
  | .bounded => 1
  | .material => 2
  | .fatal => 3

def LossSeverity.le (a b : LossSeverity) : Prop :=
  a.rank ≤ b.rank

structure ContractTypedLoss where
  sep : LossSeverity
  reopen : LossSeverity
  prov : LossSeverity
  ext : LossSeverity
  release : LossSeverity
  deriving DecidableEq, Repr

def ContractComponentwiseLe (a b : ContractTypedLoss) : Prop :=
  LossSeverity.le a.sep b.sep ∧
  LossSeverity.le a.reopen b.reopen ∧
  LossSeverity.le a.prov b.prov ∧
  LossSeverity.le a.ext b.ext ∧
  LossSeverity.le a.release b.release

inductive WarrantState where
  | open
  | complete
  deriving DecidableEq, Repr

inductive TransportState where
  | hold
  | valid
  deriving DecidableEq, Repr

inductive RevisionState where
  | none
  | requestedUnauthorized
  | requestedAuthorized
  deriving DecidableEq, Repr

structure LossContract where
  loss : ContractTypedLoss
  ceiling : ContractTypedLoss
  warrant : WarrantState
  transport : TransportState
  reopeningTrigger : Bool
  revision : RevisionState
  deriving DecidableEq, Repr

def WarrantComplete (c : LossContract) : Prop :=
  c.warrant = .complete

def TransportValid (c : LossContract) : Prop :=
  c.transport = .valid

def CeilingSatisfied (c : LossContract) : Prop :=
  ContractComponentwiseLe c.loss c.ceiling

def ReopeningDominates (c : LossContract) : Prop :=
  c.reopeningTrigger = true ∨ c.loss.reopen = .fatal

def ContractAdmissible (c : LossContract) : Prop :=
  WarrantComplete c ∧
  TransportValid c ∧
  CeilingSatisfied c ∧
  ¬ ReopeningDominates c ∧
  c.loss.release ≠ .fatal ∧
  c.revision ≠ .requestedUnauthorized

/--
An incomplete warrant blocks contract admissibility independently of loss
magnitudes. This proves only the frozen contract relation, not that its warrant
criteria are scientifically correct.
-/
theorem open_warrant_blocks
    (c : LossContract)
    (h : c.warrant = .open) :
    ¬ ContractAdmissible c := by
  intro hadm
  have hc : c.warrant = .complete := hadm.1
  rw [h] at hc
  contradiction

/--
A failed cross-domain transport certificate blocks admissibility even when the
same severity labels occur in both domains.
-/
theorem transport_hold_blocks
    (c : LossContract)
    (h : c.transport = .hold) :
    ¬ ContractAdmissible c := by
  intro hadm
  have hc : c.transport = .valid := hadm.2.1
  rw [h] at hc
  contradiction

/--
A reopening trigger dominates a locally satisfied ceiling in the frozen
contract relation. No universal lexical priority is inferred.
-/
theorem reopening_trigger_blocks
    (c : LossContract)
    (h : c.reopeningTrigger = true) :
    ¬ ContractAdmissible c := by
  intro hadm
  exact hadm.2.2.2.1 (Or.inl h)

/--
An unauthorized requested revision cannot make the frozen contract admissible
by changing thresholds after reveal.
-/
theorem unauthorized_revision_blocks
    (c : LossContract)
    (h : c.revision = .requestedUnauthorized) :
    ¬ ContractAdmissible c := by
  intro hadm
  exact hadm.2.2.2.2.2 h

/--
Ordinary componentwise feasibility is a necessary conjunct of the richer
frozen contract. This does not prove that the other conjuncts are irreducible
to standard constrained decision theory.
-/
theorem admissible_implies_componentwise
    (c : LossContract)
    (h : ContractAdmissible c) :
    ContractComponentwiseLe c.loss c.ceiling :=
  h.2.2.1

#print axioms MQR.open_warrant_blocks
#print axioms MQR.transport_hold_blocks
#print axioms MQR.reopening_trigger_blocks
#print axioms MQR.unauthorized_revision_blocks
#print axioms MQR.admissible_implies_componentwise

end MQR
