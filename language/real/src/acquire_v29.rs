use std::{collections::HashMap, env, fs};

fn yn(v: &str) -> bool { matches!(v, "YES" | "ACTIVE" | "PASS") }
fn get<'a>(m: &'a HashMap<String,String>, k: &str, d: &'a str) -> &'a str {
    m.get(k).map(String::as_str).unwrap_or(d)
}

fn main() {
    let p = env::args().nth(1).expect("packet");
    let s = fs::read_to_string(p).expect("read");
    let mut m = HashMap::new();
    let mut header_ok = false;

    for raw in s.lines() {
        let line = raw.trim();
        if line.is_empty() { continue; }
        if line == "REALACQUIRE 0.29" { header_ok = true; continue; }
        if line == "END" { break; }
        let mut it = line.split_whitespace();
        if let (Some(k), Some(v), None) = (it.next(), it.next(), it.next()) {
            m.insert(k.to_string(), v.to_string());
        }
    }
    if !header_ok { panic!("expected REALACQUIRE 0.29"); }

    let sealed = get(&m,"sealed","PASS") == "PASS";
    let lineage = get(&m,"lineage","PASS") == "PASS";
    let audit = get(&m,"audit","PASS") == "PASS";
    if !(sealed && lineage && audit) { panic!("governance gate"); }

    let myopic = yn(get(&m,"myopic_best","NO"));
    let option_loss = yn(get(&m,"option_loss","NO"));
    let separator = yn(get(&m,"unique_future_separator","NO"));
    let id_gain = yn(get(&m,"identifiability_gain","NO"));
    let live = yn(get(&m,"live_claim_relevance","NO"));
    let prior = yn(get(&m,"prior_sensitive","NO"));
    let model = yn(get(&m,"model_sensitive","NO"));
    let repr = yn(get(&m,"representation_sensitive","NO"));
    let blind = yn(get(&m,"sampling_blind_spot","NO")) || yn(get(&m,"confirmation_loop","NO")) || yn(get(&m,"generator_closed","NO"));
    let common = yn(get(&m,"common_mode","NO"));
    let reserve = yn(get(&m,"reopening_reserve","YES"));
    let order = yn(get(&m,"order_sensitive","NO"));
    let debt = yn(get(&m,"exploration_debt","NO"));
    let causal = yn(get(&m,"causal_decisive","NO"));
    let random = yn(get(&m,"randomization","NO"));
    let hidden = yn(get(&m,"hidden_rival","NO"));
    let generator_closed = yn(get(&m,"generator_closed","NO"));
    let drift = yn(get(&m,"intervention_drift","NO"));
    let contamination = yn(get(&m,"contamination","NO"));
    let pareto = yn(get(&m,"pareto_multiple","NO"));
    let destructive = yn(get(&m,"destructive","NO"));
    let outcome_loss = yn(get(&m,"outcome_contingent_loss","NO"));

    let opt_req = option_loss && separator;
    let selection =
        if destructive && opt_req { "FORBIDDEN_BY_DESTRUCTIVE_CONTRACT" }
        else if opt_req { "OPTION_PRESERVE" }
        else if hidden || generator_closed { "REOPEN_REQUIRED" }
        else if debt { "DEBT_CARRY" }
        else if prior || model || repr || pareto { "HOLD_INCOMPARABLE" }
        else if random { "BOUNDED_EXTERIOR_PROBE" }
        else { "LOCAL_ADMISSIBLE" };

    let anticipation = separator || causal || hidden || (id_gain && live);

    println!("acquisition.selection_state={selection}");
    println!("acquisition.option_preservation_required={}", if opt_req {"YES"} else {"NO"});
    println!("acquisition.myopic_sequence_optimal={}", if myopic && opt_req {"NO"} else {"NOT_DEFEATED"});
    println!("acquisition.identifiability_local_value={}", if id_gain && live {"YES"} else {"NO"});
    println!("acquisition.identifiability_universal_value=NO");
    println!("acquisition.query_order_commutative={}", if order {"NO"} else {"YES"});
    println!("acquisition.policy_blind_spot={}", if blind {"YES"} else {"NO"});
    println!("acquisition.evidence_independence={}", if common {"NO"} else {"NOT_DEFEATED"});
    println!("acquisition.reopening_reserve_active={}", if reserve {"YES"} else {"NO"});
    println!("acquisition.reopening_required={}", if hidden || generator_closed || blind {"YES"} else {"NO"});
    println!("acquisition.exploration_debt={}", if debt {"ACTIVE"} else {"INACTIVE"});
    println!("acquisition.outcome_contingent_option_loss={}", if outcome_loss {"YES"} else {"NO"});
    println!("acquisition.randomization_oracle=NO");
    println!("acquisition.fixed_exploration_universal=NO");
    println!("acquisition.pareto_unique_selector={}", if pareto {"NO"} else {"NOT_APPLICABLE"});
    println!("acquisition.cost_ratio_universal=NO");
    println!("acquisition.relation_anticipation_material={}", if anticipation {"YES"} else {"NO"});
    println!("acquisition.intervention_semantics_stable={}", if drift {"NO"} else {"NOT_DEFEATED"});
    println!("acquisition.baseline_preserved={}", if contamination {"NO"} else {"NOT_DEFEATED"});
    println!("acquisition.history_scalarization=OFF");
    println!("acquisition.universal_expected_epistemic_utility_optimizer=NOT_EARNED");
    println!("acquisition.easr=CANDIDATE");
    println!("acquisition.raer=CANDIDATE");
    println!("acquisition.opr=CANDIDATE");
    println!("acquisition.idr=CANDIDATE");
    println!("acquisition.arr=CANDIDATE");
    println!("acquisition.nedl=CANDIDATE");
}
