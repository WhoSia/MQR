import Std
namespace MQR
def covers {R O : Type} (inc : R → O → Bool) (basis : List R) (obs : List O) : Bool := obs.all (fun o => basis.any (fun r => inc r o))
def singleCoverExists {R O : Type} (inc : R → O → Bool) (roots : List R) (obs : List O) : Bool := roots.any (fun r => obs.all (fun o => inc r o))

inductive Root4 | r1 | r2 | r3 | r4 deriving DecidableEq, Repr
inductive Obl4 | o1 | o2 | o3 | o4 deriving DecidableEq, Repr
def sep4 : Root4 → Obl4 → Bool
  | .r1,.o1 => true | .r1,.o2 => true | .r2,.o3 => true | .r2,.o4 => true
  | .r3,.o1 => true | .r3,.o3 => true | .r4,.o2 => true | .r4,.o4 => true | _,_ => false
def allObl4 : List Obl4 := [.o1,.o2,.o3,.o4]
theorem twoMinimumCoverWitnesses :
  covers sep4 [.r1,.r2] allObl4 = true ∧ covers sep4 [.r3,.r4] allObl4 = true ∧
  singleCoverExists sep4 [.r1,.r2,.r3,.r4] allObl4 = false := by decide
theorem minimumWorldContactBasesNeedNotSatisfyExchange :
  covers sep4 [.r2,.r3] allObl4 = false ∧ covers sep4 [.r2,.r4] allObl4 = false := by decide

inductive Root2 | a | b deriving DecidableEq, Repr
inductive Obl3 | x | y | z deriving DecidableEq, Repr
def sepFrontier : Root2 → Obl3 → Bool | .a,.x=>true | .a,.y=>true | .b,.z=>true | _,_=>false
theorem frontierExpansionCanIncreaseContactRank :
  singleCoverExists sepFrontier [.a,.b] [.x,.y] = true ∧
  singleCoverExists sepFrontier [.a,.b] [.x,.y,.z] = false ∧
  covers sepFrontier [.a,.b] [.x,.y,.z] = true := by decide

def sepBeforeDrift : Root2 → Obl3 → Bool | .a,.x=>true | .a,.y=>true | .b,.y=>true | _,_=>false
def sepAfterDrift : Root2 → Obl3 → Bool | .a,.x=>true | .b,.y=>true | _,_=>false
theorem rootDriftCanIncreaseContactRank :
  singleCoverExists sepBeforeDrift [.a,.b] [.x,.y] = true ∧
  singleCoverExists sepAfterDrift [.a,.b] [.x,.y] = false ∧
  covers sepAfterDrift [.a,.b] [.x,.y] = true := by decide

inductive Root3 | p | q | joint deriving DecidableEq, Repr
inductive Obl2 | u | v deriving DecidableEq, Repr
def sepInstrument : Root3 → Obl2 → Bool | .p,.u=>true | .q,.v=>true | .joint,_=>true | _,_=>false
theorem instrumentExpansionCanDecreaseContactRank :
  singleCoverExists sepInstrument [.p,.q] [.u,.v] = false ∧
  covers sepInstrument [.p,.q] [.u,.v] = true ∧
  singleCoverExists sepInstrument [.p,.q,.joint] [.u,.v] = true := by decide

inductive RenRootA | ar1 | ar2 deriving DecidableEq, Repr
inductive RenOblA | ao1 | ao2 deriving DecidableEq, Repr
inductive RenRootB | brX | brY deriving DecidableEq, Repr
inductive RenOblB | boP | boQ deriving DecidableEq, Repr
def sepA : RenRootA → RenOblA → Bool | .ar1,.ao1=>true | .ar2,.ao2=>true | _,_=>false
def sepB : RenRootB → RenOblB → Bool | .brX,.boP=>true | .brY,.boQ=>true | _,_=>false
theorem incidenceRenamingPreservesRankWitness :
  singleCoverExists sepA [.ar1,.ar2] [.ao1,.ao2] = false ∧ covers sepA [.ar1,.ar2] [.ao1,.ao2] = true ∧
  singleCoverExists sepB [.brX,.brY] [.boP,.boQ] = false ∧ covers sepB [.brX,.brY] [.boP,.boQ] = true := by decide

inductive OntRoot | only deriving DecidableEq, Repr
inductive OntObl | one | two | three deriving DecidableEq, Repr
def sepOntology : OntRoot → OntObl → Bool | .only,_=>true
theorem sameMinimumRankDoesNotIdentifyFrontierOntology :
  singleCoverExists sepOntology [.only] [.one,.two] = true ∧
  singleCoverExists sepOntology [.only] [.one,.two,.three] = true := by decide

def declaredDegreeCountA : Nat := 1
def declaredDegreeCountB : Nat := 2
theorem declaredDegreeCountCanChangeWithoutAWorldWitness : declaredDegreeCountA ≠ declaredDegreeCountB := by decide

#print axioms MQR.twoMinimumCoverWitnesses
#print axioms MQR.minimumWorldContactBasesNeedNotSatisfyExchange
#print axioms MQR.frontierExpansionCanIncreaseContactRank
#print axioms MQR.rootDriftCanIncreaseContactRank
#print axioms MQR.instrumentExpansionCanDecreaseContactRank
#print axioms MQR.incidenceRenamingPreservesRankWitness
#print axioms MQR.sameMinimumRankDoesNotIdentifyFrontierOntology
#print axioms MQR.declaredDegreeCountCanChangeWithoutAWorldWitness
end MQR
