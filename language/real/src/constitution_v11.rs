use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

#[derive(Clone, Debug)]
struct AgendaSource {
    id: String,
    ancestry: String,
    kind: String,
}

#[derive(Clone, Debug)]
struct Burden {
    id: String,
    class: String,
}

#[derive(Clone, Debug)]
struct Obligation {
    id: String,
    source: String,
    mandatory: bool,
    burdens: BTreeSet<String>,
}

#[derive(Clone, Debug)]
struct Predecessor {
    id: String,
    burdens: BTreeSet<String>,
    debt: bool,
}

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    sources: BTreeMap<String, AgendaSource>,
    burdens: BTreeMap<String, Burden>,
    obligations: BTreeMap<String, Obligation>,
    predecessors: BTreeMap<String, Predecessor>,
    successors: BTreeMap<String, Vec<String>>,
    withdrawals: BTreeMap<String, bool>,
    debt_transfers: BTreeMap<String, Vec<String>>,
    challenge_route: String,
    escape_burden: String,
    witness_omitted_burden: String,
    expect_laundering: Option<String>,
    expect_successor_coverage: Option<String>,
    expect_common_mode: Option<String>,
    expect_reopen: Option<String>,
    expect_admissible: Option<String>,
}

fn toks(s: &str) -> Vec<String> {
    s.split_whitespace()
        .map(|x| x.trim_matches('"').to_string())
        .collect()
}

fn split_plus(s: &str) -> BTreeSet<String> {
    s.split('+')
        .filter(|x| !x.is_empty())
        .map(|x| x.to_string())
        .collect()
}

fn join_set(xs: &BTreeSet<String>) -> String {
    if xs.is_empty() {
        "NONE".into()
    } else {
        xs.iter().cloned().collect::<Vec<_>>().join("+")
    }
}

fn parse(path: &Path) -> Result<Packet, String> {
    let text = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut p = Packet::default();
    let mut started = false;
    let mut ended = false;

    for (i, raw) in text.lines().enumerate() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') {
            continue;
        }
        let t = toks(line);
        if t.is_empty() {
            continue;
        }

        if t[0] == "REALCONSTITUTE" {
            if t.len() != 2 || t[1] != "0.11" {
                return Err("expected REALCONSTITUTE 0.11".into());
            }
            if started {
                return Err("duplicate REALCONSTITUTE header".into());
            }
            started = true;
            continue;
        }

        if !started {
            return Err("packet must begin REALCONSTITUTE 0.11".into());
        }

        if t[0] == "END" {
            if t.len() != 1 {
                return Err("END takes no arguments".into());
            }
            ended = true;
            break;
        }

        match t[0].as_str() {
            "id" if t.len() == 2 => p.id = t[1].clone(),
            "claim_scope" if t.len() == 2 => p.claim_scope = t[1].clone(),
            "agenda_source" if t.len() == 4 => {
                let kind = t[3].to_uppercase();
                if !["ENDOGENOUS", "EXTERNAL", "MIXED"].contains(&kind.as_str()) {
                    return Err(format!("invalid agenda source kind: {}", t[3]));
                }
                if p.sources.contains_key(&t[1]) {
                    return Err(format!("duplicate agenda source: {}", t[1]));
                }
                p.sources.insert(
                    t[1].clone(),
                    AgendaSource {
                        id: t[1].clone(),
                        ancestry: t[2].clone(),
                        kind,
                    },
                );
            }
            "burden" if t.len() == 3 => {
                let class = t[2].to_uppercase();
                if ![
                    "GENERATOR",
                    "QUERY",
                    "REPRESENTATION",
                    "INSTRUMENT",
                    "RESIDUAL",
                    "EXTERNAL_CASE",
                ]
                .contains(&class.as_str())
                {
                    return Err(format!("invalid burden class: {}", t[2]));
                }
                if p.burdens.contains_key(&t[1]) {
                    return Err(format!("duplicate burden: {}", t[1]));
                }
                p.burdens.insert(
                    t[1].clone(),
                    Burden {
                        id: t[1].clone(),
                        class,
                    },
                );
            }
            "obligation" if t.len() == 5 => {
                let mode = t[3].to_uppercase();
                if !["MANDATORY", "OPTIONAL"].contains(&mode.as_str()) {
                    return Err(format!("invalid obligation mode: {}", t[3]));
                }
                if p.obligations.contains_key(&t[1]) {
                    return Err(format!("duplicate obligation: {}", t[1]));
                }
                let burdens = split_plus(&t[4]);
                if burdens.is_empty() {
                    return Err(format!("obligation {} has empty burden set", t[1]));
                }
                p.obligations.insert(
                    t[1].clone(),
                    Obligation {
                        id: t[1].clone(),
                        source: t[2].clone(),
                        mandatory: mode == "MANDATORY",
                        burdens,
                    },
                );
            }
            "predecessor" if t.len() == 4 => {
                let state = t[3].to_uppercase();
                if !["DEBT", "CLEAR"].contains(&state.as_str()) {
                    return Err(format!("invalid predecessor state: {}", t[3]));
                }
                if p.predecessors.contains_key(&t[1]) {
                    return Err(format!("duplicate predecessor: {}", t[1]));
                }
                let burdens = split_plus(&t[2]);
                if burdens.is_empty() {
                    return Err(format!("predecessor {} has empty burden set", t[1]));
                }
                p.predecessors.insert(
                    t[1].clone(),
                    Predecessor {
                        id: t[1].clone(),
                        burdens,
                        debt: state == "DEBT",
                    },
                );
            }
            "successor" if t.len() == 3 => {
                if p.successors.contains_key(&t[1]) {
                    return Err(format!("duplicate successor declaration: {}", t[1]));
                }
                let xs = split_plus(&t[2]).into_iter().collect::<Vec<_>>();
                if xs.is_empty() {
                    return Err(format!("successor {} has empty target set", t[1]));
                }
                p.successors.insert(t[1].clone(), xs);
            }
            "withdraw" if t.len() == 3 => {
                let state = t[2].to_uppercase();
                if !["DECLARED", "NONE"].contains(&state.as_str()) {
                    return Err(format!("invalid withdrawal state: {}", t[2]));
                }
                if p.withdrawals.contains_key(&t[1]) {
                    return Err(format!("duplicate withdrawal declaration: {}", t[1]));
                }
                p.withdrawals.insert(t[1].clone(), state == "DECLARED");
            }
            "debt_transfer" if t.len() == 3 => {
                if p.debt_transfers.contains_key(&t[1]) {
                    return Err(format!("duplicate debt transfer declaration: {}", t[1]));
                }
                let xs = split_plus(&t[2]).into_iter().collect::<Vec<_>>();
                if xs.is_empty() {
                    return Err(format!("debt transfer {} has empty target set", t[1]));
                }
                p.debt_transfers.insert(t[1].clone(), xs);
            }
            "challenge_route" if t.len() == 2 => {
                let x = t[1].to_uppercase();
                if !["LIVE", "ABSENT"].contains(&x.as_str()) {
                    return Err(format!("invalid challenge route: {}", t[1]));
                }
                p.challenge_route = x;
            }
            "escape_burden" if t.len() == 2 => p.escape_burden = t[1].clone(),
            "witness_omitted_burden" if t.len() == 2 => {
                p.witness_omitted_burden = t[1].clone()
            }
            "authorize_laundering" if t.len() == 2 => {
                p.expect_laundering = Some(t[1].to_uppercase())
            }
            "authorize_successor_coverage" if t.len() == 2 => {
                p.expect_successor_coverage = Some(t[1].to_uppercase())
            }
            "authorize_common_mode" if t.len() == 2 => {
                p.expect_common_mode = Some(t[1].to_uppercase())
            }
            "authorize_reopen" if t.len() == 2 => {
                p.expect_reopen = Some(t[1].to_uppercase())
            }
            "authorize_admissible" if t.len() == 2 => {
                p.expect_admissible = Some(t[1].to_uppercase())
            }
            _ => {
                return Err(format!(
                    "{}:{} malformed command: {line}",
                    path.display(),
                    i + 1
                ))
            }
        }
    }

    if !ended {
        return Err("missing END".into());
    }
    if p.id.is_empty()
        || p.claim_scope.is_empty()
        || p.sources.is_empty()
        || p.burdens.is_empty()
        || p.obligations.is_empty()
        || p.challenge_route.is_empty()
        || p.escape_burden.is_empty()
        || p.witness_omitted_burden.is_empty()
    {
        return Err("missing required field".into());
    }

    for o in p.obligations.values() {
        if !p.sources.contains_key(&o.source) {
            return Err(format!("unknown agenda source for obligation {}: {}", o.id, o.source));
        }
        for b in &o.burdens {
            if !p.burdens.contains_key(b) {
                return Err(format!("unknown burden for obligation {}: {b}", o.id));
            }
        }
    }

    for pred in p.predecessors.values() {
        for b in &pred.burdens {
            if !p.burdens.contains_key(b) {
                return Err(format!("unknown burden for predecessor {}: {b}", pred.id));
            }
        }
    }

    for (old, news) in &p.successors {
        if !p.predecessors.contains_key(old) {
            return Err(format!("successor references unknown predecessor: {old}"));
        }
        for n in news {
            if !p.obligations.contains_key(n) {
                return Err(format!("successor {old} references unknown obligation: {n}"));
            }
        }
    }

    for old in p.withdrawals.keys() {
        if !p.predecessors.contains_key(old) {
            return Err(format!("withdraw references unknown predecessor: {old}"));
        }
    }

    for (old, news) in &p.debt_transfers {
        if !p.predecessors.contains_key(old) {
            return Err(format!("debt_transfer references unknown predecessor: {old}"));
        }
        for n in news {
            if !p.obligations.contains_key(n) {
                return Err(format!("debt_transfer {old} references unknown obligation: {n}"));
            }
        }
    }

    if p.escape_burden != "NONE" && !p.burdens.contains_key(&p.escape_burden) {
        return Err(format!("unknown escape burden: {}", p.escape_burden));
    }

    Ok(p)
}

fn yes(b: bool) -> &'static str {
    if b { "YES" } else { "NO" }
}

fn obligation_union<'a, I>(p: &Packet, ids: I) -> BTreeSet<String>
where
    I: IntoIterator<Item = &'a String>,
{
    let mut out = BTreeSet::new();
    for id in ids {
        if let Some(o) = p.obligations.get(id) {
            out.extend(o.burdens.iter().cloned());
        }
    }
    out
}

fn successor_full(p: &Packet, old: &str) -> bool {
    let Some(pred) = p.predecessors.get(old) else {
        return false;
    };
    let Some(news) = p.successors.get(old) else {
        return false;
    };
    let union = obligation_union(p, news.iter());
    pred.burdens.is_subset(&union)
}

fn debt_transfer_full(p: &Packet, old: &str) -> bool {
    let Some(pred) = p.predecessors.get(old) else {
        return false;
    };
    let Some(targets) = p.debt_transfers.get(old) else {
        return false;
    };
    let Some(successors) = p.successors.get(old) else {
        return false;
    };
    let successor_set: BTreeSet<_> = successors.iter().cloned().collect();
    if targets.iter().any(|t| !successor_set.contains(t)) {
        return false;
    }
    let union = obligation_union(p, targets.iter());
    pred.burdens.is_subset(&union)
}

fn analyze(p: &Packet) -> BTreeMap<String, String> {
    let mut a = BTreeMap::new();

    let source_count = p.sources.len();
    let ancestries: BTreeSet<_> = p.sources.values().map(|s| s.ancestry.clone()).collect();
    let ancestry_count = ancestries.len();
    let common_mode = source_count > 1 && ancestry_count < source_count;

    let obligation_count = p.obligations.len();
    let mandatory_count = p.obligations.values().filter(|o| o.mandatory).count();

    let mut covered = BTreeSet::new();
    for o in p.obligations.values() {
        covered.extend(o.burdens.iter().cloned());
    }
    let burden_count = p.burdens.len();
    let covered_count = covered.len();
    let all_burdens: BTreeSet<_> = p.burdens.keys().cloned().collect();
    let uncovered: BTreeSet<_> = all_burdens.difference(&covered).cloned().collect();

    let mandatory_sources = p
        .obligations
        .values()
        .filter(|o| o.mandatory)
        .map(|o| &p.sources[&o.source])
        .collect::<Vec<_>>();
    let endogenous_only = !mandatory_sources.is_empty()
        && mandatory_sources.iter().all(|s| s.kind == "ENDOGENOUS");
    let external_present = p.sources.values().any(|s| s.kind == "EXTERNAL" || s.kind == "MIXED");

    let invalid_successor_count = p
        .successors
        .keys()
        .filter(|old| !successor_full(p, old))
        .count();
    let successor_coverage_complete = invalid_successor_count == 0;

    let explicit_withdrawal_count = p.withdrawals.values().filter(|x| **x).count();
    let mut debt_transfer_required_count = 0usize;
    let mut debt_transfer_missing_count = 0usize;
    let mut debt_transfer_items = Vec::new();

    for pred in p.predecessors.values().filter(|x| x.debt) {
        let withdrawn = p.withdrawals.get(&pred.id).copied().unwrap_or(false);
        if withdrawn {
            continue;
        }
        debt_transfer_required_count += 1;
        if successor_full(p, &pred.id) && debt_transfer_full(p, &pred.id) {
            debt_transfer_items.push(pred.id.clone());
        } else {
            debt_transfer_missing_count += 1;
        }
    }

    debt_transfer_items.sort();
    let burden_laundering = debt_transfer_missing_count > 0;

    let escape = p.escape_burden != "NONE";
    let challenge_live = p.challenge_route == "LIVE";
    let admissible = challenge_live
        && successor_coverage_complete
        && !burden_laundering
        && uncovered.is_empty()
        && !escape;

    let state = if escape {
        "REOPEN_REQUIRED"
    } else if admissible {
        "ADMISSIBLE"
    } else {
        "HOLD"
    };

    a.insert("constitution.obligation_count".into(), obligation_count.to_string());
    a.insert("constitution.mandatory_obligation_count".into(), mandatory_count.to_string());
    a.insert("constitution.burden_count".into(), burden_count.to_string());
    a.insert("constitution.covered_burden_count".into(), covered_count.to_string());
    a.insert("constitution.burden_union".into(), join_set(&covered));
    a.insert("constitution.uncovered_declared_burdens".into(), join_set(&uncovered));
    a.insert("constitution.agenda_source_count".into(), source_count.to_string());
    a.insert("constitution.agenda_ancestry_count".into(), ancestry_count.to_string());
    a.insert("constitution.agenda_common_mode".into(), yes(common_mode).into());
    a.insert("constitution.endogenous_only".into(), yes(endogenous_only).into());
    a.insert("constitution.external_source_present".into(), yes(external_present).into());
    a.insert("constitution.challenge_route".into(), p.challenge_route.clone());
    a.insert(
        "constitution.successor_claim_count".into(),
        p.successors.len().to_string(),
    );
    a.insert(
        "constitution.invalid_successor_claim_count".into(),
        invalid_successor_count.to_string(),
    );
    a.insert(
        "constitution.successor_coverage_complete".into(),
        yes(successor_coverage_complete).into(),
    );
    a.insert(
        "constitution.explicit_withdrawal_count".into(),
        explicit_withdrawal_count.to_string(),
    );
    a.insert(
        "constitution.debt_transfer_required_count".into(),
        debt_transfer_required_count.to_string(),
    );
    a.insert(
        "constitution.debt_transfer_missing_count".into(),
        debt_transfer_missing_count.to_string(),
    );
    a.insert(
        "constitution.debt_transfer_items".into(),
        if debt_transfer_items.is_empty() {
            "NONE".into()
        } else {
            debt_transfer_items.join("+")
        },
    );
    a.insert(
        "constitution.burden_laundering_detected".into(),
        yes(burden_laundering).into(),
    );
    a.insert(
        "constitution.partition_count_authority".into(),
        "REJECT".into(),
    );
    a.insert(
        "constitution.partition_audit_surface".into(),
        "DECLARED_BURDEN_UNION".into(),
    );
    a.insert(
        "constitution.external_source_truth_oracle".into(),
        "NO".into(),
    );
    a.insert(
        "constitution.endogenous_source_truth_oracle".into(),
        "NO".into(),
    );
    a.insert("constitution.escape_detected".into(), yes(escape).into());
    a.insert(
        "constitution.escape_reconstitution_required".into(),
        yes(escape).into(),
    );
    a.insert("constitution.reopen_on_escape".into(), "YES".into());
    a.insert(
        "constitution.world_obligation_complete".into(),
        "NO".into(),
    );
    a.insert(
        "constitution.burden_atom_ontology_complete".into(),
        "NO".into(),
    );
    a.insert(
        "constitution.omitted_burden_inferred".into(),
        "NO".into(),
    );
    a.insert(
        "constitution.open_world_receipt".into(),
        "REQUIRED".into(),
    );
    a.insert(
        "constitution.guidance_mode".into(),
        "CONTRACT_RELATIVE_CONSTITUTIONAL".into(),
    );
    a.insert(
        "constitution.admissible_envelope".into(),
        yes(admissible).into(),
    );
    a.insert("constitution.state".into(), state.into());
    a
}

fn validate(p: &Packet, a: &BTreeMap<String, String>) -> Result<(), String> {
    let checks = [
        (&p.expect_laundering, "constitution.burden_laundering_detected"),
        (
            &p.expect_successor_coverage,
            "constitution.successor_coverage_complete",
        ),
        (&p.expect_common_mode, "constitution.agenda_common_mode"),
        (
            &p.expect_reopen,
            "constitution.escape_reconstitution_required",
        ),
        (&p.expect_admissible, "constitution.admissible_envelope"),
    ];
    for (expected, key) in checks {
        if let Some(x) = expected {
            if a[key] != *x {
                return Err(format!("{key} mismatch expected {x} got {}", a[key]));
            }
        }
    }
    Ok(())
}

fn emit(p: &Packet, a: &BTreeMap<String, String>) -> String {
    let mut s = format!(
        "REAL-CONSTITUTION=0.11\nid={}\nclaim_scope={}\n",
        p.id, p.claim_scope
    );

    for key in [
        "constitution.obligation_count",
        "constitution.mandatory_obligation_count",
        "constitution.burden_count",
        "constitution.covered_burden_count",
        "constitution.burden_union",
        "constitution.uncovered_declared_burdens",
        "constitution.agenda_source_count",
        "constitution.agenda_ancestry_count",
        "constitution.agenda_common_mode",
        "constitution.endogenous_only",
        "constitution.external_source_present",
        "constitution.challenge_route",
        "constitution.successor_claim_count",
        "constitution.invalid_successor_claim_count",
        "constitution.successor_coverage_complete",
        "constitution.explicit_withdrawal_count",
        "constitution.debt_transfer_required_count",
        "constitution.debt_transfer_missing_count",
        "constitution.debt_transfer_items",
        "constitution.burden_laundering_detected",
        "constitution.partition_count_authority",
        "constitution.partition_audit_surface",
        "constitution.external_source_truth_oracle",
        "constitution.endogenous_source_truth_oracle",
        "constitution.escape_detected",
        "constitution.escape_reconstitution_required",
        "constitution.reopen_on_escape",
        "constitution.world_obligation_complete",
        "constitution.omitted_burden_inferred",
        "constitution.open_world_receipt",
        "constitution.guidance_mode",
        "constitution.admissible_envelope",
        "constitution.state",
    ] {
        s.push_str(&format!("{key}={}\n", a[key]));
    }

    s.push_str(&format!(
        "witness.omitted_burden={}\n",
        p.witness_omitted_burden
    ));
    s.push_str("constitution.meaning=PROVISIONAL_OPEN_WORLD_OBLIGATION_GOVERNANCE\n");
    s.push_str("explicit_does_not_mean_adequate=true\n");
    s.push_str("external_does_not_mean_true=true\n");
    s.push_str("partition_count_does_not_mean_burden=true\n");
    s.push_str("final_truth_distance=UNIDENTIFIED\n");
    s
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("usage: real-v11-constitute <packet.real> [...]");
        std::process::exit(2);
    }

    for f in args {
        match parse(Path::new(&f)) {
            Ok(p) => {
                let a = analyze(&p);
                if let Err(e) = validate(&p, &a) {
                    eprintln!("{e}");
                    std::process::exit(1);
                }
                print!("{}", emit(&p, &a));
            }
            Err(e) => {
                eprintln!("{e}");
                std::process::exit(1);
            }
        }
    }
}
