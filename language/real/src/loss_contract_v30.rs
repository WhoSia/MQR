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
    fn rank(self) -> u8 { self as u8 }
    fn as_str(self) -> &'static str {
        match self {
            Self::None => "NONE",
            Self::Bounded => "BOUNDED",
            Self::Material => "MATERIAL",
            Self::Fatal => "FATAL",
        }
    }
}

fn get<'a>(m: &'a HashMap<String,String>, k: &str) -> &'a str {
    m.get(k).map(String::as_str).unwrap_or_else(|| {
        eprintln!("missing required field: {k}");
        process::exit(2)
    })
}
fn yes(v: bool) -> &'static str { if v {"YES"} else {"NO"} }

fn parse_sev(m: &HashMap<String,String>, k: &str) -> Sev {
    Sev::parse(get(m,k)).unwrap_or_else(|| {
        eprintln!("invalid severity: {k}");
        process::exit(2)
    })
}

fn evidence_ok(s: &str) -> bool {
    matches!(s,"OBSERVED"|"PROVED"|"ENUMERATED"|"SIMULATED"|"INFERRED"|"OPEN")
}

fn main() {
    let path = env::args().nth(1).unwrap_or_else(|| {
        eprintln!("usage: real-v30-loss-contract <packet>");
        process::exit(2)
    });
    let src = fs::read_to_string(path).unwrap_or_else(|e| {
        eprintln!("read failed: {e}");
        process::exit(2)
    });

    let mut header = false;
    let mut m = HashMap::<String,String>::new();
    for raw in src.lines() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        if line == "REALLOSS 0.30-CANDIDATE" { header = true; continue; }
        if line == "END" { break; }
        let mut it = line.split_whitespace();
        match (it.next(), it.next(), it.next()) {
            (Some(k),Some(v),None) => { m.insert(k.to_string(),v.to_string()); }
            _ => { eprintln!("invalid packet line: {line}"); process::exit(2); }
        }
    }
    if !header {
        eprintln!("expected REALLOSS 0.30-CANDIDATE");
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
    let warrant_kind = get(&m,"warrant_kind");
    if !evidence_ok(evidence) || !evidence_ok(warrant_kind) {
        eprintln!("invalid evidence kind");
        process::exit(2);
    }

    let context = get(&m,"context");
    if !matches!(context,"EXPLORATORY"|"AUDIT"|"PUBLIC_RELEASE"|"CROSS_DOMAIN") {
        eprintln!("invalid context");
        process::exit(2);
    }

    let loss = [
        parse_sev(&m,"loss_sep"),
        parse_sev(&m,"loss_reopen"),
        parse_sev(&m,"loss_prov"),
        parse_sev(&m,"loss_ext"),
        parse_sev(&m,"loss_release"),
    ];
    let ceiling = [
        parse_sev(&m,"ceiling_sep"),
        parse_sev(&m,"ceiling_reopen"),
        parse_sev(&m,"ceiling_prov"),
        parse_sev(&m,"ceiling_ext"),
        parse_sev(&m,"ceiling_release"),
    ];

    let warrant_complete =
        warrant_kind != "OPEN"
        && get(&m,"warrant_source") != "OPEN"
        && get(&m,"warrant_defeaters") != "OPEN"
        && get(&m,"horizon") != "OPEN"
        && get(&m,"expiry") != "OPEN";

    let transport_valid = get(&m,"transport_valid") == "PASS";
    let reopening_trigger = get(&m,"reopening_trigger") == "YES";
    let revision_requested = get(&m,"revision_requested") == "YES";
    let revision_authorized = get(&m,"revision_authorized") == "YES";

    if revision_requested && !matches!(get(&m,"revision_trigger"),"OBSERVED_SCOPE_CHANGE"|"OBSERVED_REOPENING_EVENT"|"PREDECLARED_EXPIRY") {
        if revision_authorized {
            eprintln!("revision authorization lacks admitted trigger");
            process::exit(2);
        }
    }

    let budget_exceeded = loss.iter().zip(ceiling.iter()).any(|(l,b)| l.rank() > b.rank());
    let any_loss = loss.iter().any(|x| *x != Sev::None);

    let decision =
        if !warrant_complete { "HOLD_WARRANT_OPEN" }
        else if context == "CROSS_DOMAIN" && !transport_valid { "HOLD_TRANSPORT" }
        else if revision_requested {
            if revision_authorized { "REVISION_AUTHORIZED" } else { "REVISION_FORBIDDEN" }
        }
        else if loss[4] == Sev::Fatal { "FORBID_MERGE" }
        else if reopening_trigger || loss[1] == Sev::Fatal { "REEXPAND_REQUIRED" }
        else if loss[2] == Sev::Fatal || loss[3] == Sev::Fatal { "REOPEN_REQUIRED" }
        else if budget_exceeded { "HOLD_CONTEXT_CEILING" }
        else if any_loss { "ACCEPT_WITH_AUDIT" }
        else { "ACCEPT_LOCAL" };

    println!("loss_contract.decision={decision}");
    println!("loss_contract.context={context}");
    println!("loss_contract.horizon={}", get(&m,"horizon"));
    println!("loss_contract.warrant.kind={warrant_kind}");
    println!("loss_contract.warrant.source={}",get(&m,"warrant_source"));
    println!("loss_contract.warrant.defeaters={}",get(&m,"warrant_defeaters"));
    println!("loss_contract.warrant.complete={}",yes(warrant_complete));
    for (name,l,b) in [
        ("sep",loss[0],ceiling[0]),("reopen",loss[1],ceiling[1]),
        ("prov",loss[2],ceiling[2]),("ext",loss[3],ceiling[3]),
        ("release",loss[4],ceiling[4])
    ] {
        println!("loss_contract.loss.{name}={}",l.as_str());
        println!("loss_contract.ceiling.{name}={}",b.as_str());
        println!("loss_contract.ceiling_exceeded.{name}={}",yes(l.rank()>b.rank()));
    }
    println!("loss_contract.reopening_trigger={}",yes(reopening_trigger));
    println!("loss_contract.transport_valid={}",yes(transport_valid));
    println!("loss_contract.revision_requested={}",yes(revision_requested));
    println!("loss_contract.revision_authorized={}",yes(revision_authorized));
    println!("loss_contract.revision_trigger={}",get(&m,"revision_trigger"));
    println!("loss_contract.expiry={}",get(&m,"expiry"));
    println!("loss_contract.merge_ancestry={}",get(&m,"merge_ancestry"));
    println!("loss_contract.scalar_authority=OFF");
    println!("loss_contract.global_loss_score=FORBIDDEN");
    println!("loss_contract.cross_domain_severity_equality=NOT_ASSUMED");
    println!("loss_contract.evidence_kind={evidence}");
    println!("loss_contract.world_validity={}",
        if evidence=="SIMULATED" {"NOT_ESTABLISHED"}
        else if evidence=="OPEN" {"OPEN"}
        else {"LIMITED_BY_EVIDENCE_KIND"});
    println!("loss_contract.authority_reducibility=NOT_ESTABLISHED_BY_REPRESENTATION");
    println!("loss_contract.status=CANDIDATE_UNPROMOTED");
}
