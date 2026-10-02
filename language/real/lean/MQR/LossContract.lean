import Std
import MQR.Approximation

namespace MQR

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
  loss : TypedLoss
  ceiling : TypedLoss
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
  ComponentwiseLe c.loss c.ceiling

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
An incomplete warrant blocks contract admissibility independently of the loss
magnitudes. This is a theorem about the frozen contract syntax, not a theorem
that the chosen warrant criteria are scientifically correct.
-/
theorem open_warrant_blocks
    (c : LossContract)
    (h : c.warrant = .open) :
    ¬ ContractAdmissible c := by
  intro hadm
  exact (show c.warrant ≠ .complete by simp [h]) hadm.1

/--
A failed cross-domain transport certificate blocks admissibility even when the
same severity labels appear on both sides.
-/
theorem transport_hold_blocks
    (c : LossContract)
    (h : c.transport = .hold) :
    ¬ ContractAdmissible c := by
  intro hadm
  exact (show c.transport ≠ .valid by simp [h]) hadm.2.1

/--
A reopening trigger dominates a locally satisfied ceiling in the frozen
contract relation. This encodes the constitution; it does not establish that
scientific reopening should universally have lexical priority.
-/
theorem reopening_trigger_blocks
    (c : LossContract)
    (h : c.reopeningTrigger = true) :
    ¬ ContractAdmissible c := by
  intro hadm
  exact hadm.2.2.2.1 (Or.inl h)

/--
An unauthorized requested revision cannot turn a contract admissible merely by
changing thresholds after reveal.
-/
theorem unauthorized_revision_blocks
    (c : LossContract)
    (h : c.revision = .requestedUnauthorized) :
    ¬ ContractAdmissible c := by
  intro hadm
  exact hadm.2.2.2.2.2 h

/--
This theorem intentionally exposes that ordinary componentwise feasibility is
only one conjunct of the richer frozen contract. It does not prove that the
extra conjuncts are scientifically irreducible to standard constraints.
-/
theorem admissible_implies_componentwise
    (c : LossContract)
    (h : ContractAdmissible c) :
    ComponentwiseLe c.loss c.ceiling :=
  h.2.2.1

#print axioms MQR.open_warrant_blocks
#print axioms MQR.transport_hold_blocks
#print axioms MQR.reopening_trigger_blocks
#print axioms MQR.unauthorized_revision_blocks
#print axioms MQR.admissible_implies_componentwise

end MQR
