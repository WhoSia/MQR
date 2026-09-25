use std::{collections::BTreeMap, env, fs};

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Signature {
    component_identity: bool,
    direct_independent: bool,
    domain_covered: bool,
    information_preserved: bool,
    state_reset: bool,
    adapter_commutative: bool,
}

fn b(s: &str) -> Result<bool, String> {
    match s {
        "1" => Ok(true),
        "0" => Ok(false),
        _ => Err(format!("invalid boolean: {s}")),
    }
}

fn main() {
    let path = env::args()
        .nth(1)
        .unwrap_or_else(|| "experiments/mqr-4.33/collision/support-profile-collision.tsv".into());

    let input = fs::read_to_string(&path).unwrap_or_else(|e| {
        eprintln!("{e}");
        std::process::exit(2)
    });

    let mut lines = input.lines();
    let expected = "id\tcomponent_identity\tdirect_independent\tdomain_covered\tinformation_preserved\tstate_reset\tadapter_commutative\toutcome\tevidence_role";
    let header = lines.next().unwrap_or("");
    if header != expected {
        eprintln!("unexpected header: {header}");
        std::process::exit(2);
    }

    let mut profiles: BTreeMap<Signature, BTreeMap<String, Vec<String>>> = BTreeMap::new();

    for (idx, line) in lines.enumerate() {
        if line.trim().is_empty() {
            continue;
        }
        let p: Vec<&str> = line.split('\t').collect();
        if p.len() != 9 {
            eprintln!("line {} has {} columns", idx + 2, p.len());
            std::process::exit(2);
        }
        let sig = Signature {
            component_identity: b(p[1]).unwrap(),
            direct_independent: b(p[2]).unwrap(),
            domain_covered: b(p[3]).unwrap(),
            information_preserved: b(p[4]).unwrap(),
            state_reset: b(p[5]).unwrap(),
            adapter_commutative: b(p[6]).unwrap(),
        };
        profiles
            .entry(sig)
            .or_default()
            .entry(p[7].to_owned())
            .or_default()
            .push(p[0].to_owned());
    }

    let mut collisions = 0usize;
    for (sig, outcomes) in &profiles {
        if outcomes.len() > 1 {
            collisions += 1;
            let labels = outcomes.keys().cloned().collect::<Vec<_>>().join(",");
            let ids = outcomes
                .values()
                .flatten()
                .cloned()
                .collect::<Vec<_>>()
                .join(",");
            println!(
                "PROFILE_COLLISION={} signature={:?} outcomes={} ids={}",
                collisions, sig, labels, ids
            );
        }
    }

    println!("PROFILE_COUNT={}", profiles.len());
    println!("PROFILE_COLLISION_COUNT={collisions}");
    let identifiable = collisions == 0;
    println!(
        "SUPPORT_PROFILE_IDENTIFIABILITY={}",
        if identifiable { "PASS" } else { "FAIL" }
    );
    println!(
        "OUTCOME_FACTORIZATION_THROUGH_FROZEN_PROFILE={}",
        if identifiable { "NOT_DEFEATED" } else { "FAIL" }
    );
    println!(
        "FROZEN_SUPPORT_QUOTIENT_SUFFICIENCY={}",
        if identifiable { "NOT_DEFEATED" } else { "FAIL" }
    );
}
