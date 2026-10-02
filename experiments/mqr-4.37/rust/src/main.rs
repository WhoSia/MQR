use std::collections::BTreeSet;

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Status {
    Fail,
    Hold,
    Pass,
}

fn ceiling(xs: &[Status]) -> Status {
    xs.iter().copied().min().unwrap_or(Status::Hold)
}

fn residue(universe: &[&str], tested: &BTreeSet<&str>) -> usize {
    universe.iter().filter(|p| !tested.contains(**p)).count()
}

fn quantifier_scope_attack() {
    let p1 = ["a"];
    let p2 = ["a", "b"];
    let p3 = ["a", "b", "c"];
    let tested = BTreeSet::from(["a"]);

    let r1 = residue(&p1, &tested);
    let r2 = residue(&p2, &tested);
    let r3 = residue(&p3, &tested);

    assert_eq!(r1, 0);
    assert_eq!(r2, 1);
    assert_eq!(r3, 2);

    println!("QSA_P1_RESIDUE={r1}");
    println!("QSA_P2_RESIDUE={r2}");
    println!("QSA_P3_RESIDUE={r3}");
    println!("QUANTIFIER_SCOPE_LAUNDERING_COUNTERMODEL=PASS");
}

#[derive(Clone, Debug)]
struct Ancestry<'a> {
    surface_premise: &'a str,
    receipts: Vec<(&'a str, Status)>,
}

impl<'a> Ancestry<'a> {
    fn world_ceiling(&self) -> Status {
        let states: Vec<_> = self.receipts.iter().map(|(_, s)| *s).collect();
        ceiling(&states)
    }
}

fn premise_ancestry_attack() {
    let a = Ancestry {
        surface_premise: "P_EMPIRICAL_PASS",
        receipts: vec![("measurement", Status::Pass), ("calibration", Status::Pass)],
    };
    let b = Ancestry {
        surface_premise: "P_EMPIRICAL_PASS",
        receipts: vec![("measurement", Status::Pass), ("calibration", Status::Hold)],
    };

    assert_eq!(a.surface_premise, b.surface_premise);
    assert_eq!(a.world_ceiling(), Status::Pass);
    assert_eq!(b.world_ceiling(), Status::Hold);

    println!("RECEIPT_COMPRESSION_SAME_SURFACE=true");
    println!("RECEIPT_COMPRESSION_FINE_CEILINGS_DIFFER=true");
    println!("RECEIPT_COMPRESSION_PARADOX_COUNTERMODEL=PASS");
}

#[derive(Clone, Copy, Debug)]
struct FrontierState {
    formal_steps: usize,
    world_premise_ceiling: Status,
}

fn frontier_migration_attack() {
    let before = FrontierState {
        formal_steps: 1,
        world_premise_ceiling: Status::Hold,
    };
    let after = FrontierState {
        formal_steps: 4,
        world_premise_ceiling: Status::Hold,
    };

    assert!(after.formal_steps > before.formal_steps);
    assert_eq!(
        after.world_premise_ceiling,
        before.world_premise_ceiling
    );

    println!("FORMAL_REGION_EXPANDED=true");
    println!("WORLD_AUTHORITY_IMPROVED=false");
    println!("EPISTEMIC_DEBT_CONCENTRATION_COUNTERMODEL=PASS");
}

#[derive(Clone, Copy, Debug)]
struct Independence {
    statement: bool,
    compiler: bool,
    kernel_a: bool,
    kernel_b: bool,
    world: bool,
}

impl Independence {
    fn checker_plurality_pass(self) -> bool {
        self.kernel_a && self.kernel_b
    }

    fn authority_transfer_pass(self) -> bool {
        self.statement && self.compiler && self.kernel_a && self.world
    }
}

fn checker_independence_attack() {
    let shared_bad_encoding = Independence {
        statement: false,
        compiler: true,
        kernel_a: true,
        kernel_b: true,
        world: false,
    };

    assert!(shared_bad_encoding.checker_plurality_pass());
    assert!(!shared_bad_encoding.authority_transfer_pass());

    println!("CHECKER_PLURALITY_PASS=true");
    println!("STATEMENT_INDEPENDENCE_PASS=false");
    println!("WORLD_INDEPENDENCE_PASS=false");
    println!("CHECKER_INDEPENDENCE_VECTOR_ATTACK=PASS");
}

#[derive(Clone, Copy, Debug)]
struct Architecture {
    world_receipt: bool,
    typed_premise: bool,
    dependency_graph: bool,
    kernel_check: bool,
    independent_recheck: bool,
    open_residue: bool,
}

impl Architecture {
    fn formal_custody(self) -> bool {
        self.dependency_graph && self.kernel_check
    }

    fn scoped_world_authority_eligible(self) -> bool {
        self.world_receipt
            && self.typed_premise
            && self.open_residue
            && self.formal_custody()
    }

    fn robustness(self) -> bool {
        self.formal_custody() && self.independent_recheck
    }
}

fn ablate(base: Architecture, component: &str) -> Architecture {
    match component {
        "WORLD_RECEIPT" => Architecture {
            world_receipt: false,
            ..base
        },
        "TYPED_PREMISE" => Architecture {
            typed_premise: false,
            ..base
        },
        "FORMAL_DAG" => Architecture {
            dependency_graph: false,
            ..base
        },
        "KERNEL" => Architecture {
            kernel_check: false,
            ..base
        },
        "RECHECK" => Architecture {
            independent_recheck: false,
            ..base
        },
        "OPEN_RESIDUE" => Architecture {
            open_residue: false,
            ..base
        },
        _ => base,
    }
}

fn pcra_minimality_attack() {
    let base = Architecture {
        world_receipt: true,
        typed_premise: true,
        dependency_graph: true,
        kernel_check: true,
        independent_recheck: true,
        open_residue: true,
    };

    assert!(base.scoped_world_authority_eligible());
    assert!(base.robustness());

    for component in [
        "WORLD_RECEIPT",
        "TYPED_PREMISE",
        "FORMAL_DAG",
        "KERNEL",
        "RECHECK",
        "OPEN_RESIDUE",
    ] {
        let x = ablate(base, component);
        println!(
            "ABLATE_{component}=WORLD_ELIGIBLE:{};FORMAL_CUSTODY:{};ROBUSTNESS:{}",
            x.scoped_world_authority_eligible(),
            x.formal_custody(),
            x.robustness()
        );
    }

    let no_recheck = ablate(base, "RECHECK");
    assert!(no_recheck.scoped_world_authority_eligible());
    assert!(no_recheck.formal_custody());
    assert!(!no_recheck.robustness());

    println!("INDEPENDENT_RECHECK_CONSTITUTIVE_WORLD_PRIMITIVE=false");
    println!("INDEPENDENT_RECHECK_ROLE=FORMAL_CUSTODY_ROBUSTNESS");
    println!("PCRA_MINIMALITY_ATTACK=PASS");
}

#[derive(Clone, Copy, Debug)]
struct Candidate {
    formal_custody_level: u8,
    world_alignment_supported: bool,
}

fn truth_oracle_trap() {
    let formally_stronger = Candidate {
        formal_custody_level: 4,
        world_alignment_supported: false,
    };
    let formally_weaker = Candidate {
        formal_custody_level: 1,
        world_alignment_supported: true,
    };

    assert!(formally_stronger.formal_custody_level > formally_weaker.formal_custody_level);
    assert!(!formally_stronger.world_alignment_supported);
    assert!(formally_weaker.world_alignment_supported);

    println!("FORMAL_CUSTODY_MONOTONE_TRUTH_ORDER=REJECT");
    println!("FINAL_TRUTH_DISTANCE=UNIDENTIFIED");
    println!("TRUTH_ORACLE_TRAP=PASS");
}

fn main() {
    quantifier_scope_attack();
    premise_ancestry_attack();
    frontier_migration_attack();
    checker_independence_attack();
    pcra_minimality_attack();
    truth_oracle_trap();

    println!("FINITE_CLOSURE_INTERNAL_VALIDITY=SURVIVES");
    println!("FINITE_CLOSURE_AUTHORITY_TRANSFER=NOT_ENTAILED");
    println!("PCRA_UNIFIED_SCIENTIFIC_AUTHORITY_PRIMITIVE=REJECT");
    println!("FORMAL_CUSTODY_SCIENTIFIC_AUTHORITY_SPLIT=SUPPORTED");
    println!("OUTCOME_BRANCH_C=SUPPORTED");
    println!("OUTCOME_BRANCH_E=SUPPORTED");
    println!("MQR437_ADVERSARIAL_COURT=PASS");
}
