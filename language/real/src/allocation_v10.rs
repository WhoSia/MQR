use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

#[derive(Clone, Debug)]
struct Lane {
    id: String,
    ancestry: String,
    activation_cost: u64,
    mandatory: bool,
    role: String,
    class: String,
}

#[derive(Clone, Debug)]
struct Obligation {
    id: String,
    lane: String,
    due_step: u64,
}

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    budget: Option<u64>,
    horizon: Option<u64>,
    lanes: BTreeMap<String, Lane>,
    obligations: BTreeMap<String, Obligation>,
    allocations: Vec<(u64, String, u64)>,
    outcomes: Vec<(u64, String, String)>,
    reserve: Option<u64>,
    normative_prior: String,
    normative_utility: String,
    history_signature: String,
    policy: String,
    witness_escape_lane: String,
    expect_acrr: Option<String>,
    expect_starvation: Option<String>,
    expect_debt: Option<String>,
    expect_escape_reallocation: Option<String>,
    expect_common_mode: Option<String>,
}

fn toks(s: &str) -> Vec<String> {
    s.split_whitespace().map(|x| x.trim_matches('"').to_string()).collect()
}

fn parse_u64(x: &str, what: &str) -> Result<u64, String> {
    x.parse::<u64>().map_err(|_| format!("invalid {what}: {x}"))
}

fn parse(path: &Path) -> Result<Packet, String> {
    let text = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut p = Packet::default();
    let mut started = false;
    let mut ended = false;

    for (i, raw) in text.lines().enumerate() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        let t = toks(line);
        if t.is_empty() { continue; }
        if t[0] == "REALALLOCATE" {
            if t.len() != 2 || t[1] != "0.10" { return Err("expected REALALLOCATE 0.10".into()); }
            started = true;
            continue;
        }
        if !started { return Err("packet must begin REALALLOCATE 0.10".into()); }
        if t[0] == "END" { ended = true; break; }

        match t[0].as_str() {
            "id" if t.len() == 2 => p.id = t[1].clone(),
            "claim_scope" if t.len() == 2 => p.claim_scope = t[1].clone(),
            "budget" if t.len() == 2 => p.budget = Some(parse_u64(&t[1], "budget")?),
            "horizon" if t.len() == 2 => p.horizon = Some(parse_u64(&t[1], "horizon")?),
            "lane" if t.len() == 7 => {
                let activation_cost = parse_u64(&t[3], "activation cost")?;
                if activation_cost == 0 { return Err("activation cost must be positive".into()); }
                let obligation = t[4].to_uppercase();
                if !["MANDATORY", "OPTIONAL"].contains(&obligation.as_str()) {
                    return Err(format!("invalid lane obligation: {}", t[4]));
                }
                let role = t[5].to_uppercase();
                if !["REOPENING", "EXPLOITATION"].contains(&role.as_str()) {
                    return Err(format!("invalid lane role: {}", t[5]));
                }
                let class = t[6].to_uppercase();
                if !["GENERATOR", "QUERY", "REPRESENTATION", "INSTRUMENT", "RESIDUAL", "EXTERNAL_CASE"].contains(&class.as_str()) {
                    return Err(format!("invalid lane class: {}", t[6]));
                }
                if p.lanes.contains_key(&t[1]) { return Err(format!("duplicate lane: {}", t[1])); }
                p.lanes.insert(t[1].clone(), Lane {
                    id: t[1].clone(),
                    ancestry: t[2].clone(),
                    activation_cost,
                    mandatory: obligation == "MANDATORY",
                    role,
                    class,
                });
            }
            "obligation" if t.len() == 4 => {
                let due_step = parse_u64(&t[3], "obligation due step")?;
                if p.obligations.contains_key(&t[1]) { return Err(format!("duplicate obligation: {}", t[1])); }
                p.obligations.insert(t[1].clone(), Obligation {
                    id: t[1].clone(),
                    lane: t[2].clone(),
                    due_step,
                });
            }
            "allocate" if t.len() == 4 => p.allocations.push((
                parse_u64(&t[1], "allocation step")?,
                t[2].clone(),
                parse_u64(&t[3], "allocation units")?,
            )),
            "outcome" if t.len() == 4 => {
                let state = t[3].to_uppercase();
                if !["NEW", "NO_NEW", "ESCAPE", "NA"].contains(&state.as_str()) {
                    return Err(format!("invalid outcome state: {}", t[3]));
                }
                p.outcomes.push((parse_u64(&t[1], "outcome step")?, t[2].clone(), state));
            }
            "reserve" if t.len() == 2 => p.reserve = Some(parse_u64(&t[1], "reserve")?),
            "normative_prior" if t.len() == 2 => {
                let x = t[1].to_uppercase();
                if !["NONE", "DECLARED"].contains(&x.as_str()) { return Err(format!("invalid normative_prior: {}", t[1])); }
                p.normative_prior = x;
            }
            "normative_utility" if t.len() == 2 => {
                let x = t[1].to_uppercase();
                if !["NONE", "DECLARED"].contains(&x.as_str()) { return Err(format!("invalid normative_utility: {}", t[1])); }
                p.normative_utility = x;
            }
            "history_signature" if t.len() == 2 => p.history_signature = t[1].clone(),
            "policy" if t.len() == 2 => p.policy = t[1].to_uppercase(),
            "witness_escape_lane" if t.len() == 2 => p.witness_escape_lane = t[1].clone(),
            "authorize_acrr" if t.len() == 2 => p.expect_acrr = Some(t[1].to_uppercase()),
            "authorize_starvation" if t.len() == 2 => p.expect_starvation = Some(t[1].to_uppercase()),
            "authorize_debt" if t.len() == 2 => p.expect_debt = Some(t[1].clone()),
            "authorize_escape_reallocation" if t.len() == 2 => p.expect_escape_reallocation = Some(t[1].to_uppercase()),
            "authorize_common_mode" if t.len() == 2 => p.expect_common_mode = Some(t[1].to_uppercase()),
            _ => return Err(format!("{}:{} malformed command: {line}", path.display(), i + 1)),
        }
    }

    if !ended { return Err("missing END".into()); }
    if p.id.is_empty() || p.claim_scope.is_empty() || p.budget.is_none() || p.horizon.is_none()
        || p.reserve.is_none() || p.lanes.is_empty() || p.normative_prior.is_empty()
        || p.normative_utility.is_empty() || p.history_signature.is_empty()
        || p.policy.is_empty() || p.witness_escape_lane.is_empty()
    {
        return Err("missing required field".into());
    }

    let horizon = p.horizon.unwrap();
    for o in p.obligations.values() {
        let Some(lane) = p.lanes.get(&o.lane) else {
            return Err(format!("unknown lane for obligation {}: {}", o.id, o.lane));
        };
        if !lane.mandatory { return Err(format!("obligation {} targets non-mandatory lane {}", o.id, o.lane)); }
        if o.due_step == 0 { return Err(format!("obligation {} has zero due step", o.id)); }
    }
    for (step, lane, _) in &p.allocations {
        if *step == 0 || *step > horizon { return Err(format!("allocation step out of horizon: {step}")); }
        if !p.lanes.contains_key(lane) { return Err(format!("unknown lane in allocation: {lane}")); }
    }
    for (step, lane, _) in &p.outcomes {
        if *step == 0 || *step > horizon { return Err(format!("outcome step out of horizon: {step}")); }
        if !p.lanes.contains_key(lane) { return Err(format!("unknown lane in outcome: {lane}")); }
    }
    if p.witness_escape_lane != "NONE" && !p.lanes.contains_key(&p.witness_escape_lane) {
        return Err(format!("unknown witness escape lane: {}", p.witness_escape_lane));
    }
    Ok(p)
}

fn yes(b: bool) -> &'static str { if b { "YES" } else { "NO" } }

fn spend_until(p: &Packet, lane: &str, due: u64) -> u64 {
    p.allocations.iter()
        .filter(|(step, l, _)| *step <= due && l == lane)
        .fold(0u64, |acc, (_, _, u)| acc.saturating_add(*u))
}

fn spend_role(p: &Packet, role: &str) -> u64 {
    p.allocations.iter()
        .filter(|(_, lane, _)| p.lanes.get(lane).map(|x| x.role.as_str()) == Some(role))
        .fold(0u64, |acc, (_, _, u)| acc.saturating_add(*u))
}

fn analyze(p: &Packet) -> BTreeMap<String, String> {
    let mut a = BTreeMap::new();
    let budget = p.budget.unwrap();
    let horizon = p.horizon.unwrap();
    let reserve = p.reserve.unwrap();
    let total_allocated = p.allocations.iter().fold(0u64, |acc, (_, _, u)| acc.saturating_add(*u));
    let budget_valid = total_allocated.saturating_add(reserve) <= budget;

    let lane_count = p.lanes.len();
    let mandatory_count = p.lanes.values().filter(|l| l.mandatory).count();
    let ancestries: BTreeSet<_> = p.lanes.values().map(|l| l.ancestry.clone()).collect();
    let common_mode = lane_count > 1 && ancestries.len() < lane_count;

    let reopening_lanes: Vec<_> = p.lanes.values().filter(|l| l.role == "REOPENING").collect();
    let nominal_reserve = reserve > 0;
    let acrr = nominal_reserve && reopening_lanes.iter().any(|l| l.activation_cost <= reserve);
    let reserve_state = if acrr { "LIVE" } else if nominal_reserve { "NOMINAL_ONLY" } else { "ABSENT" };

    let mut debts = Vec::new();
    let mut debt_classes = BTreeSet::new();
    for o in p.obligations.values() {
        if o.due_step > horizon { continue; }
        let lane = &p.lanes[&o.lane];
        if spend_until(p, &o.lane, o.due_step) < lane.activation_cost {
            debts.push(format!("{}@{}", o.id, lane.class));
            debt_classes.insert(lane.class.clone());
        }
    }
    debts.sort();
    let debt_count = debts.len();
    let starvation = debt_count > 0;

    let escape = p.outcomes.iter().any(|(_, _, s)| s == "ESCAPE");
    let new_count = p.outcomes.iter().filter(|(_, _, s)| s == "NEW").count();
    let exploitation_spend = spend_role(p, "EXPLOITATION");
    let reopening_spend = spend_role(p, "REOPENING");
    let exploration_starved = starvation && exploitation_spend > 0 && reopening_spend == 0;
    let greedy_yield_starvation = p.policy == "GREEDY_YIELD" && new_count > 0 && exploration_starved;
    let admissible = budget_valid && !starvation && acrr;

    a.insert("allocation.budget".into(), budget.to_string());
    a.insert("allocation.horizon".into(), horizon.to_string());
    a.insert("allocation.total_allocated".into(), total_allocated.to_string());
    a.insert("allocation.reserve_units".into(), reserve.to_string());
    a.insert("allocation.budget_valid".into(), yes(budget_valid).into());
    a.insert("allocation.lane_count".into(), lane_count.to_string());
    a.insert("allocation.mandatory_lane_count".into(), mandatory_count.to_string());
    a.insert("allocation.ancestry_count".into(), ancestries.len().to_string());
    a.insert("allocation.common_mode_detected".into(), yes(common_mode).into());
    a.insert("allocation.nominal_reserve".into(), yes(nominal_reserve).into());
    a.insert("allocation.activation_capable_reserve".into(), yes(acrr).into());
    a.insert("allocation.reserve_state".into(), reserve_state.into());
    a.insert("allocation.starvation_detected".into(), yes(starvation).into());
    a.insert("allocation.exploration_debt_count".into(), debt_count.to_string());
    a.insert("allocation.exploration_debt_items".into(), if debts.is_empty() { "NONE".into() } else { debts.join("+") });
    a.insert("allocation.exploration_debt_classes".into(), if debt_classes.is_empty() { "NONE".into() } else { debt_classes.into_iter().collect::<Vec<_>>().join("+") });
    a.insert("allocation.debt_scalar_default".into(), "OFF".into());
    a.insert("allocation.opportunity_cost_mode".into(), "VECTOR".into());
    a.insert("allocation.exploitation_spend".into(), exploitation_spend.to_string());
    a.insert("allocation.reopening_spend".into(), reopening_spend.to_string());
    a.insert("allocation.exploration_starved".into(), yes(exploration_starved).into());
    a.insert("allocation.greedy_yield_starvation_witness".into(), yes(greedy_yield_starvation).into());
    a.insert("allocation.escape_detected".into(), yes(escape).into());
    a.insert("allocation.escape_reallocation_required".into(), yes(escape).into());
    a.insert("allocation.reopen_on_escape".into(), "YES".into());
    a.insert("allocation.normative_prior".into(), p.normative_prior.clone());
    a.insert("allocation.normative_utility".into(), p.normative_utility.clone());
    a.insert("allocation.hidden_prior_inferred".into(), "NO".into());
    a.insert("allocation.hidden_utility_inferred".into(), "NO".into());
    a.insert("allocation.expected_discovery_value_inferred".into(), "NO".into());
    a.insert("allocation.unique_optimum_authorized".into(), "NO".into());
    a.insert("allocation.universal_next_action".into(), "UNIDENTIFIED".into());
    a.insert("allocation.local_optimizer_scope".into(),
        if p.normative_prior == "DECLARED" && p.normative_utility == "DECLARED" { "DECLARED_MODEL_ONLY".into() } else { "NOT_AUTHORIZED".into() });
    a.insert("allocation.guidance_mode".into(), "SET_VALUED_CONTRACT_RELATIVE".into());
    a.insert("allocation.admissible_envelope".into(), yes(admissible).into());
    a.insert("allocation.randomization_epistemic_oracle".into(), "NO".into());
    a.insert("allocation.policy_path_provenance".into(), "REQUIRED".into());
    a.insert("allocation.world_optimum_identified".into(), "NO".into());
    a.insert("allocation.world_frontier_complete".into(), "NO".into());
    a.insert("allocation.stopping_rule".into(), "FORBIDDEN".into());
    a
}

fn validate(p: &Packet, a: &BTreeMap<String, String>) -> Result<(), String> {
    let checks = [
        (&p.expect_acrr, "allocation.activation_capable_reserve"),
        (&p.expect_starvation, "allocation.starvation_detected"),
        (&p.expect_debt, "allocation.exploration_debt_count"),
        (&p.expect_escape_reallocation, "allocation.escape_reallocation_required"),
        (&p.expect_common_mode, "allocation.common_mode_detected"),
    ];
    for (expected, key) in checks {
        if let Some(x) = expected {
            if a[key] != *x { return Err(format!("{key} mismatch expected {x} got {}", a[key])); }
        }
    }
    Ok(())
}

fn emit(p: &Packet, a: &BTreeMap<String, String>) -> String {
    let mut s = format!(
        "REAL-ALLOCATION=0.10\nid={}\nclaim_scope={}\nhistory_signature={}\npolicy={}\n",
        p.id, p.claim_scope, p.history_signature, p.policy
    );
    for key in [
        "allocation.budget","allocation.horizon","allocation.total_allocated","allocation.reserve_units",
        "allocation.budget_valid","allocation.lane_count","allocation.mandatory_lane_count","allocation.ancestry_count",
        "allocation.common_mode_detected","allocation.nominal_reserve","allocation.activation_capable_reserve",
        "allocation.reserve_state","allocation.starvation_detected","allocation.exploration_debt_count",
        "allocation.exploration_debt_items","allocation.exploration_debt_classes","allocation.debt_scalar_default",
        "allocation.opportunity_cost_mode","allocation.exploitation_spend","allocation.reopening_spend",
        "allocation.exploration_starved","allocation.greedy_yield_starvation_witness","allocation.escape_detected",
        "allocation.escape_reallocation_required","allocation.reopen_on_escape","allocation.normative_prior",
        "allocation.normative_utility","allocation.hidden_prior_inferred","allocation.hidden_utility_inferred",
        "allocation.expected_discovery_value_inferred","allocation.unique_optimum_authorized",
        "allocation.universal_next_action","allocation.local_optimizer_scope","allocation.guidance_mode",
        "allocation.admissible_envelope","allocation.randomization_epistemic_oracle",
        "allocation.policy_path_provenance","allocation.world_optimum_identified",
        "allocation.world_frontier_complete","allocation.stopping_rule",
    ] {
        s.push_str(&format!("{key}={}\n", a[key]));
    }
    s.push_str(&format!("witness.escape_lane={}\n", p.witness_escape_lane));
    s.push_str("allocation.meaning=CONTRACT_RELATIVE_OPEN_FRONTIER_ATTENTION_GOVERNANCE\n");
    s.push_str("admissible_does_not_mean_optimal=true\n");
    s.push_str("procedural_coverage_does_not_mean_frontier_completeness=true\n");
    s.push_str("finite_budget_does_not_price_unknown_rivals=true\n");
    s.push_str("final_truth_distance=UNIDENTIFIED\n");
    s
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("usage: real-v10-allocate <packet.real> [...]");
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
