use std::{collections::HashMap, env, fs, process};

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Sev { None, Bounded, Material, Fatal }

impl Sev {
    fn parse(s: &str) -> Option<Self> {
        match s {
            "NONE" => Some(Self::None),
            "BOUNDED" => Some(Self::Bounded),
            "MATERIAL" => Some(Self::Material),
            "FATAL" => Some(Self::Fatal),
            _ => None,
        }
    }
    fn as_str(self) -> &'static str {
        match self {
            Self::None => "NONE",
            Self::Bounded => "BOUNDED",
            Self::Material => "MATERIAL",
            Self::Fatal => "FATAL",
        }
    }
    fn nonzero(self) -> bool { self != Self::None }
}

fn get<'a>(m: &'a HashMap<String,String>, k: &str) -> &'a str {
    m.get(k).map(String::as_str).unwrap_or_else(|| {
        eprintln!("missing required field: {k}");
        process::exit(2)
    })
}
fn parse_u(m: &HashMap<String,String>, k: &str) -> u64 {
    get(m,k).parse::<u64>().unwrap_or_else(|_| {
        eprintln!("invalid nonnegative integer: {k}");
        process::exit(2)
    })
}
fn sev(m: &HashMap<String,String>, k: &str) -> Sev {
    Sev::parse(get(m,k)).unwrap_or_else(|| {
        eprintln!("invalid severity: {k}");
        process::exit(2)
    })
}
fn yes(b: bool) -> &'static str { if b {"YES"} else {"NO"} }

fn main() {
    let p = env::args().nth(1).unwrap_or_else(|| {
        eprintln!("usage: real-v30-approx <packet>");
        process::exit(2)
    });
    let s = fs::read_to_string(p).unwrap_or_else(|e| {
        eprintln!("read failed: {e}");
        process::exit(2)
    });

    let mut header_ok = false;
    let mut m = HashMap::<String,String>::new();
    for raw in s.lines() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        if line == "REALAPPROX 0.30-CANDIDATE" { header_ok = true; continue; }
        if line == "END" { break; }
        let mut it = line.split_whitespace();
        match (it.next(), it.next(), it.next()) {
            (Some(k), Some(v), None) => { m.insert(k.to_string(),v.to_string()); }
            _ => {
                eprintln!("invalid packet line: {line}");
                process::exit(2)
            }
        }
    }
    if !header_ok {
        eprintln!("expected REALAPPROX 0.30-CANDIDATE");
        process::exit(2);
    }

    for k in ["sealed","lineage","audit"] {
        if get(&m,k) != "PASS" {
            eprintln!("governance gate failed: {k}");
            process::exit(2);
        }
    }
    if get(&m,"scalar_mode") != "OFF" {
        eprintln!("scalar_mode must be OFF");
        process::exit(2);
    }

    let evidence = get(&m,"evidence_kind");
    if !matches!(evidence,"OBSERVED"|"PROVED"|"ENUMERATED"|"SIMULATED"|"INFERRED"|"OPEN") {
        eprintln!("invalid evidence_kind");
        process::exit(2);
    }

    let losses = [
        ("sep", sev(&m,"loss_sep"), sev(&m,"budget_sep")),
        ("reopen", sev(&m,"loss_reopen"), sev(&m,"budget_reopen")),
        ("prov", sev(&m,"loss_prov"), sev(&m,"budget_prov")),
        ("ext", sev(&m,"loss_ext"), sev(&m,"budget_ext")),
        ("release", sev(&m,"loss_release"), sev(&m,"budget_release")),
    ];

    let debt_sep = parse_u(&m,"debt_sep");
    let debt_reopen = parse_u(&m,"debt_reopen");
    let debt_prov = parse_u(&m,"debt_prov");
    let debt_ext = parse_u(&m,"debt_ext");
    let debt_release = parse_u(&m,"debt_release");

    let debt_reexpand =
        debt_sep >= 4 ||
        debt_reopen >= 3 ||
        debt_prov >= 2 ||
        debt_ext >= 3 ||
        debt_release >= 2;

    let loss_sep = losses[0].1;
    let loss_reopen = losses[1].1;
    let loss_prov = losses[2].1;
    let loss_ext = losses[3].1;
    let loss_release = losses[4].1;

    let hard_forbid = loss_release == Sev::Fatal;
    let hard_reexpand = loss_reopen == Sev::Fatal || debt_reexpand;
    let hard_reopen = loss_prov == Sev::Fatal || loss_ext == Sev::Fatal;
    let budget_exceeded = losses.iter().any(|(_,l,b)| *l > *b);
    let any_loss = losses.iter().any(|(_,l,_)| l.nonzero());

    let decision =
        if hard_forbid { "FORBID_MERGE" }
        else if hard_reexpand { "REEXPAND_REQUIRED" }
        else if hard_reopen { "REOPEN_REQUIRED" }
        else if budget_exceeded { "HOLD_INCOMPARABLE" }
        else if any_loss { "ACCEPT_WITH_AUDIT" }
        else { "ACCEPT_LOCAL" };

    println!("approximation.decision={decision}");
    for (name,l,b) in losses {
        println!("approximation.loss.{name}={}",l.as_str());
        println!("approximation.budget.{name}={}",b.as_str());
        println!("approximation.budget_exceeded.{name}={}",yes(l>b));
    }
    println!("approximation.hard_forbid={}",yes(hard_forbid));
    println!("approximation.reopen_required={}",yes(hard_reopen));
    println!("approximation.reexpand_required={}",yes(hard_reexpand));
    println!("approximation.debt_reexpand={}",yes(debt_reexpand));
    println!("approximation.merge_ancestry={}",get(&m,"merge_ancestry"));
    println!("approximation.scalar_authority=OFF");
    println!("approximation.global_loss_score=FORBIDDEN");
    println!("approximation.evidence_kind={evidence}");
    println!("approximation.world_validity={}",
        if evidence=="SIMULATED" {"NOT_ESTABLISHED"}
        else if evidence=="OPEN" {"OPEN"}
        else {"LIMITED_BY_EVIDENCE_KIND"});
    println!("approximation.universal_epistemic_utility=NOT_EARNED");
    println!("approximation.realapprox_status=CANDIDATE_UNPROMOTED");
}
