use std::{env, fs};

fn put(slot: &mut Option<String>, v: &str, name: &str) -> Result<(), String> {
    if slot.is_some() { return Err(format!("duplicate {name}")); }
    *slot = Some(v.to_string());
    Ok(())
}
fn yn(b: bool) -> &'static str { if b { "YES" } else { "NO" } }

fn main() {
    if let Err(e) = run() {
        eprintln!("REALREFLEX_ERROR {e}");
        std::process::exit(2);
    }
}

fn run() -> Result<(), String> {
    let path = env::args().nth(1).ok_or("usage: real-v25-reflex <file>")?;
    let src = fs::read_to_string(path).map_err(|e| e.to_string())?;

    let mut header = false;
    let mut ended = false;
    let mut id = None;
    let mut genealogy = None;
    let mut transition = None;
    let mut obligations = None;
    let mut role = None;
    let mut utility = None;
    let mut mechanism = None;
    let mut replay = None;
    let mut ontology = None;
    let mut self_subjection = None;
    let mut anti_inflation = None;
    let mut closure_ceiling = None;
    let mut scaffold = None;
    let mut world_claim = None;
    let mut drake = None;
    let mut toy = None;
    let mut retirement = None;
    let mut scalar = None;
    let mut fixed_point = None;

    for (ln, raw) in src.lines().enumerate() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with('#') { continue; }
        if ended { return Err(format!("content after END at line {}", ln + 1)); }

        let t: Vec<&str> = line.split_whitespace().collect();
        if !header {
            if t.as_slice() == ["REALREFLEX", "0.25"] {
                header = true;
                continue;
            }
            return Err(format!("expected REALREFLEX 0.25 at line {}", ln + 1));
        }

        match t[0] {
            "END" if t.len() == 1 => ended = true,
            "id" if t.len() == 2 => put(&mut id, t[1], "id")?,
            "actor_genealogy" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad actor_genealogy".into()); }
                put(&mut genealogy, t[1], "actor_genealogy")?;
            }
            "transition_provenance" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad transition_provenance".into()); }
                put(&mut transition, t[1], "transition_provenance")?;
            }
            "obligation_transport" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad obligation_transport".into()); }
                put(&mut obligations, t[1], "obligation_transport")?;
            }
            "role_reauthorization" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad role_reauthorization".into()); }
                put(&mut role, t[1], "role_reauthorization")?;
            }
            "utility_reconstitution" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad utility_reconstitution".into()); }
                put(&mut utility, t[1], "utility_reconstitution")?;
            }
            "mechanism_lineage" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad mechanism_lineage".into()); }
                put(&mut mechanism, t[1], "mechanism_lineage")?;
            }
            "mechanism_replay" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad mechanism_replay".into()); }
                put(&mut replay, t[1], "mechanism_replay")?;
            }
            "ontology_expansion" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad ontology_expansion".into()); }
                put(&mut ontology, t[1], "ontology_expansion")?;
            }
            "self_subjection" if t.len() == 2 => {
                if !matches!(t[1], "ACTIVE" | "ABSENT") { return Err("bad self_subjection".into()); }
                put(&mut self_subjection, t[1], "self_subjection")?;
            }
            "anti_inflation" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad anti_inflation".into()); }
                put(&mut anti_inflation, t[1], "anti_inflation")?;
            }
            "closure_ceiling" if t.len() == 2 => {
                if !matches!(t[1], "ENFORCED" | "ABSENT") { return Err("bad closure_ceiling".into()); }
                put(&mut closure_ceiling, t[1], "closure_ceiling")?;
            }
            "scaffold_profile" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad scaffold_profile".into()); }
                put(&mut scaffold, t[1], "scaffold_profile")?;
            }
            "world_claim_separation" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "FAIL") { return Err("bad world_claim_separation".into()); }
                put(&mut world_claim, t[1], "world_claim_separation")?;
            }
            "drake_role_admission" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad drake_role_admission".into()); }
                put(&mut drake, t[1], "drake_role_admission")?;
            }
            "toy_model_scope" if t.len() == 2 => {
                if !matches!(t[1], "PASS" | "HOLD" | "FAIL") { return Err("bad toy_model_scope".into()); }
                put(&mut toy, t[1], "toy_model_scope")?;
            }
            "scaffold_retirement" if t.len() == 2 => {
                if !matches!(t[1], "ACTIVE" | "ABSENT") { return Err("bad scaffold_retirement".into()); }
                put(&mut retirement, t[1], "scaffold_retirement")?;
            }
            "truth_distance_scalar" if t.len() == 2 => {
                if !matches!(t[1], "OFF" | "ON") { return Err("bad truth_distance_scalar".into()); }
                put(&mut scalar, t[1], "truth_distance_scalar")?;
            }
            "final_fixed_point" if t.len() == 2 => {
                if !matches!(t[1], "NO_CLAIM" | "CLAIMED") { return Err("bad final_fixed_point".into()); }
                put(&mut fixed_point, t[1], "final_fixed_point")?;
            }
            _ => return Err(format!("unknown or malformed line {}: {}", ln + 1, line)),
        }
    }

    if !header || !ended { return Err("missing header or END".into()); }
    let _id = id.ok_or("missing id")?;
    let genealogy = genealogy.ok_or("missing actor_genealogy")?;
    let transition = transition.ok_or("missing transition_provenance")?;
    let obligations = obligations.ok_or("missing obligation_transport")?;
    let role = role.ok_or("missing role_reauthorization")?;
    let utility = utility.ok_or("missing utility_reconstitution")?;
    let mechanism = mechanism.ok_or("missing mechanism_lineage")?;
    let replay = replay.ok_or("missing mechanism_replay")?;
    let ontology = ontology.ok_or("missing ontology_expansion")?;
    let self_subjection = self_subjection.ok_or("missing self_subjection")?;
    let anti_inflation = anti_inflation.ok_or("missing anti_inflation")?;
    let closure_ceiling = closure_ceiling.ok_or("missing closure_ceiling")?;
    let scaffold = scaffold.ok_or("missing scaffold_profile")?;
    let world_claim = world_claim.ok_or("missing world_claim_separation")?;
    let drake = drake.ok_or("missing drake_role_admission")?;
    let toy = toy.ok_or("missing toy_model_scope")?;
    let retirement = retirement.ok_or("missing scaffold_retirement")?;
    let scalar = scalar.ok_or("missing truth_distance_scalar")?;
    let fixed_point = fixed_point.ok_or("missing final_fixed_point")?;

    let local =
        genealogy == "PASS" &&
        transition == "PASS" &&
        obligations == "PASS" &&
        role == "PASS" &&
        utility == "PASS" &&
        mechanism == "PASS" &&
        replay == "PASS" &&
        ontology == "PASS" &&
        self_subjection == "ACTIVE" &&
        anti_inflation == "PASS" &&
        closure_ceiling == "ENFORCED" &&
        scaffold == "PASS" &&
        world_claim == "PASS" &&
        drake == "PASS" &&
        toy == "PASS" &&
        retirement == "ACTIVE" &&
        scalar == "OFF" &&
        fixed_point == "NO_CLAIM";

    let diagnosis =
        if genealogy != "PASS" { "GENEALOGY_GAP" }
        else if transition != "PASS" { "TRANSITION_PROVENANCE_GAP" }
        else if obligations != "PASS" { "OBLIGATION_TRANSPORT_GAP" }
        else if role != "PASS" { "ROLE_REAUTHORIZATION_GAP" }
        else if utility != "PASS" { "UTILITY_RECONSTITUTION_GAP" }
        else if mechanism != "PASS" { "MECHANISM_LINEAGE_GAP" }
        else if replay != "PASS" { "MECHANISM_REPLAY_GAP" }
        else if ontology != "PASS" { "ONTOLOGY_EXPANSION_GAP" }
        else if self_subjection != "ACTIVE" { "CONSTITUTION_SELF_EXEMPTION" }
        else if anti_inflation != "PASS" { "RAVEL_NOOP_INFLATION" }
        else if closure_ceiling != "ENFORCED" { "CLOSURE_FINALITY_OVERCLAIM" }
        else if scaffold != "PASS" { "SCAFFOLD_PROFILE_GAP" }
        else if world_claim != "PASS" { "SCAFFOLD_WORLD_AUTHORITY_CONFLATION" }
        else if drake != "PASS" { "DRAKE_ROLE_GAP" }
        else if toy != "PASS" { "TOY_MODEL_SCOPE_GAP" }
        else if retirement != "ACTIVE" { "SCAFFOLD_FOSSILIZATION" }
        else if scalar != "OFF" { "TRUTH_DISTANCE_SCALAR_RESURRECTION" }
        else if fixed_point == "CLAIMED" { "FINAL_REFLECTIVE_FIXED_POINT_OVERCLAIM" }
        else { "LOCAL_REFLEXIVE_ECOLOGY_ADMISSIBLE" };

    println!("reflex.actor_genealogy={genealogy}");
    println!("reflex.transition_provenance={transition}");
    println!("reflex.obligation_transport={obligations}");
    println!("reflex.role_reauthorization={role}");
    println!("reflex.utility_reconstitution={utility}");
    println!("reflex.mechanism_lineage={mechanism}");
    println!("reflex.mechanism_replay={replay}");
    println!("reflex.ontology_expansion={ontology}");
    println!("reflex.self_subjection={self_subjection}");
    println!("reflex.anti_inflation={anti_inflation}");
    println!("reflex.closure_ceiling={closure_ceiling}");
    println!("reflex.scaffold_profile={scaffold}");
    println!("reflex.world_claim_separation={world_claim}");
    println!("reflex.drake_role_admission={drake}");
    println!("reflex.toy_model_scope={toy}");
    println!("reflex.scaffold_retirement={retirement}");
    println!("reflex.truth_distance_scalar={scalar}");
    println!("reflex.final_fixed_point={fixed_point}");
    println!("reflex.local_reflexive_robustness={}", yn(local));
    println!("reflex.diagnosis={diagnosis}");
    println!("reflex.fixed_actor_ontology=REJECT");
    println!("reflex.fixed_utility_transport=REJECT");
    println!("reflex.fixed_mechanism_ontology=REJECT");
    println!("reflex.constitution_self_immunity=REJECT");
    println!("reflex.stage_closure_finality=REJECT");
    println!("reflex.scaffold_value_equals_world_authority=REJECT");
    println!("reflex.world_authority_equals_scaffold_value=REJECT");
    println!("reflex.truth_distance_scalar_authority=NOT_EARNED");
    println!("reflex.universal_self_reduction_fixed_point=NOT_EARNED");
    println!("reflex.wcaer={}", if local { "EARNED_LOCAL_CANDIDATE" } else { "HOLD" });
    println!("reflex.rcsr={}", if local { "EARNED_LOCAL_CANDIDATE" } else { "HOLD" });
    println!("reflex.isp={}", if local { "EARNED_LOCAL_CANDIDATE" } else { "HOLD" });

    Ok(())
}
