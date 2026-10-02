use std::{env, fs};

fn put(slot: &mut Option<String>, v: &str, name: &str) -> Result<(), String> {
    if slot.is_some() { return Err(format!("duplicate {name}")); }
    *slot = Some(v.to_string());
    Ok(())
}
fn yn(b: bool) -> &'static str { if b { "YES" } else { "NO" } }

fn main() {
    if let Err(e) = run() {
        eprintln!("REALSTRATEGY_ERROR {e}");
        std::process::exit(2);
    }
}

fn run() -> Result<(), String> {
    let path = env::args().nth(1).ok_or("usage: real-v24-strategy <file>")?;
    let src = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut header = false;
    let mut ended = false;
    let mut id = None;
    let mut agent = None;
    let mut private_info = None;
    let mut incentive = None;
    let mut supply = None;
    let mut cost = None;
    let mut target = None;
    let mut proxy = None;
    let mut performative = None;
    let mut ancestry = None;
    let mut sybil = None;
    let mut mechanism_cf = None;
    let mut exterior = None;
    let mut equilibrium = None;
    let mut capture = None;
    let mut reopening = None;
    let mut scope = None;
    let mut wcepr = None;
    let mut universal = None;

    for (ln, raw) in src.lines().enumerate() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        if ended { return Err(format!("content after END at line {}", ln + 1)); }
        let t: Vec<&str> = line.split_whitespace().collect();
        if !header {
            if t.as_slice() == ["REALSTRATEGY", "0.24"] {
                header = true;
                continue;
            }
            return Err(format!("expected REALSTRATEGY 0.24 at line {}", ln + 1));
        }

        match t[0] {
            "END" if t.len() == 1 => ended = true,
            "id" if t.len() == 2 => put(&mut id, t[1], "id")?,
            "agent_map" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad agent_map".into()); }
                put(&mut agent, t[1], "agent_map")?;
            }
            "private_information" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad private_information".into()); }
                put(&mut private_info, t[1], "private_information")?;
            }
            "incentive_map" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad incentive_map".into()); }
                put(&mut incentive, t[1], "incentive_map")?;
            }
            "supply_provenance" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad supply_provenance".into()); }
                put(&mut supply, t[1], "supply_provenance")?;
            }
            "cost_reconciliation" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad cost_reconciliation".into()); }
                put(&mut cost, t[1], "cost_reconciliation")?;
            }
            "target_provenance" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad target_provenance".into()); }
                put(&mut target, t[1], "target_provenance")?;
            }
            "proxy_choice_provenance" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad proxy_choice_provenance".into()); }
                put(&mut proxy, t[1], "proxy_choice_provenance")?;
            }
            "performative_feedback" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad performative_feedback".into()); }
                put(&mut performative, t[1], "performative_feedback")?;
            }
            "strategic_ancestry" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad strategic_ancestry".into()); }
                put(&mut ancestry, t[1], "strategic_ancestry")?;
            }
            "anti_sybil" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad anti_sybil".into()); }
                put(&mut sybil, t[1], "anti_sybil")?;
            }
            "mechanism_counterfactual" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad mechanism_counterfactual".into()); }
                put(&mut mechanism_cf, t[1], "mechanism_counterfactual")?;
            }
            "exterior_reserve" if t.len() == 2 => {
                if !matches!(t[1], "ACTIVE" | "ABSENT") { return Err("bad exterior_reserve".into()); }
                put(&mut exterior, t[1], "exterior_reserve")?;
            }
            "equilibrium_ceiling" if t.len() == 2 => {
                if !matches!(t[1], "ENFORCED" | "ABSENT") { return Err("bad equilibrium_ceiling".into()); }
                put(&mut equilibrium, t[1], "equilibrium_ceiling")?;
            }
            "capture_attribution" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad capture_attribution".into()); }
                put(&mut capture, t[1], "capture_attribution")?;
            }
            "reopening" if t.len() == 2 => {
                if !matches!(t[1], "ACTIVE" | "INACTIVE") { return Err("bad reopening".into()); }
                put(&mut reopening, t[1], "reopening")?;
            }
            "mechanism_scope" if t.len() == 2 => {
                if !matches!(t[1], "DECLARED_LOCAL" | "WORLD") { return Err("bad mechanism_scope".into()); }
                put(&mut scope, t[1], "mechanism_scope")?;
            }
            "wcepr_dependency" if t.len() == 2 => {
                if !matches!(t[1], "DECLARED" | "HIDDEN") { return Err("bad wcepr_dependency".into()); }
                put(&mut wcepr, t[1], "wcepr_dependency")?;
            }
            "universal_mechanism" if t.len() == 2 => {
                if !matches!(t[1], "NO_CLAIM" | "CLAIMED") { return Err("bad universal_mechanism".into()); }
                put(&mut universal, t[1], "universal_mechanism")?;
            }
            _ => return Err(format!("unknown or malformed line {}: {}", ln + 1, line)),
        }
    }

    if !header || !ended { return Err("missing header or END".into()); }
    let _id = id.ok_or("missing id")?;
    let agent = agent.ok_or("missing agent_map")?;
    let private_info = private_info.ok_or("missing private_information")?;
    let incentive = incentive.ok_or("missing incentive_map")?;
    let supply = supply.ok_or("missing supply_provenance")?;
    let cost = cost.ok_or("missing cost_reconciliation")?;
    let target = target.ok_or("missing target_provenance")?;
    let proxy = proxy.ok_or("missing proxy_choice_provenance")?;
    let performative = performative.ok_or("missing performative_feedback")?;
    let ancestry = ancestry.ok_or("missing strategic_ancestry")?;
    let sybil = sybil.ok_or("missing anti_sybil")?;
    let mechanism_cf = mechanism_cf.ok_or("missing mechanism_counterfactual")?;
    let exterior = exterior.ok_or("missing exterior_reserve")?;
    let equilibrium = equilibrium.ok_or("missing equilibrium_ceiling")?;
    let capture = capture.ok_or("missing capture_attribution")?;
    let reopening = reopening.ok_or("missing reopening")?;
    let scope = scope.ok_or("missing mechanism_scope")?;
    let wcepr = wcepr.ok_or("missing wcepr_dependency")?;
    let universal = universal.ok_or("missing universal_mechanism")?;

    let robust =
        agent == "PASS" &&
        private_info == "PASS" &&
        incentive == "PASS" &&
        supply == "PASS" &&
        cost == "PASS" &&
        target == "PASS" &&
        proxy == "PASS" &&
        performative == "PASS" &&
        ancestry == "PASS" &&
        sybil == "PASS" &&
        mechanism_cf == "PASS" &&
        exterior == "ACTIVE" &&
        equilibrium == "ENFORCED" &&
        capture == "PASS" &&
        reopening == "ACTIVE" &&
        scope == "DECLARED_LOCAL" &&
        wcepr == "DECLARED" &&
        universal == "NO_CLAIM";

    let diagnosis =
        if agent != "PASS" { "AGENT_MAP_GAP" }
        else if private_info != "PASS" { "PRIVATE_INFORMATION_BLIND" }
        else if incentive != "PASS" { "INCENTIVE_MAP_GAP" }
        else if supply != "PASS" { "SUPPLY_ENDOGENEITY_BLIND" }
        else if cost != "PASS" { "COST_REPORT_ORACLE" }
        else if target != "PASS" { "TARGET_FRAMING_GAP" }
        else if proxy != "PASS" { "PROXY_ARBITRAGE_GAP" }
        else if performative != "PASS" { "PERFORMATIVE_FEEDBACK_BLIND" }
        else if ancestry != "PASS" { "STRATEGIC_ANCESTRY_GAP" }
        else if sybil != "PASS" { "SYBIL_MULTIPLICITY" }
        else if mechanism_cf != "PASS" { "MECHANISM_COUNTERFACTUAL_GAP" }
        else if exterior != "ACTIVE" { "EXTERIOR_RESERVE_ABSENT" }
        else if equilibrium != "ENFORCED" { "EQUILIBRIUM_OVERCLAIM" }
        else if capture != "PASS" { "CAPTURE_ATTRIBUTION_GAP" }
        else if reopening != "ACTIVE" { "STRATEGIC_REOPENING_FAILURE" }
        else if scope == "WORLD" { "WORLD_MECHANISM_OVERCLAIM" }
        else if wcepr != "DECLARED" { "HIDDEN_WCEPR_DEPENDENCY" }
        else if universal == "CLAIMED" { "UNIVERSAL_MECHANISM_OVERCLAIM" }
        else { "LOCAL_STRATEGIC_ECOLOGY_ADMISSIBLE" };

    println!("strategy.agent_map={agent}");
    println!("strategy.private_information={private_info}");
    println!("strategy.incentive_map={incentive}");
    println!("strategy.supply_provenance={supply}");
    println!("strategy.cost_reconciliation={cost}");
    println!("strategy.target_provenance={target}");
    println!("strategy.proxy_choice_provenance={proxy}");
    println!("strategy.performative_feedback={performative}");
    println!("strategy.strategic_ancestry={ancestry}");
    println!("strategy.anti_sybil={sybil}");
    println!("strategy.mechanism_counterfactual={mechanism_cf}");
    println!("strategy.exterior_reserve={exterior}");
    println!("strategy.equilibrium_ceiling={equilibrium}");
    println!("strategy.capture_attribution={capture}");
    println!("strategy.reopening={reopening}");
    println!("strategy.mechanism_scope={scope}");
    println!("strategy.wcepr_dependency={wcepr}");
    println!("strategy.universal_mechanism={universal}");
    println!("strategy.local_strategic_robustness={}", yn(robust));
    println!("strategy.diagnosis={diagnosis}");
    println!("strategy.wcepr_incentive_robust_by_default=REJECT");
    println!("strategy.equilibrium_implies_epistemic_adequacy=REJECT");
    println!("strategy.nominal_agent_count_implies_independence=REJECT");
    println!("strategy.universal_scientific_mechanism=NOT_EARNED");
    println!("strategy.wcser={}", if robust { "EARNED_LOCAL_CANDIDATE" } else { "HOLD" });

    Ok(())
}
