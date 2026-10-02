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
        if line == "REALPROMOTE 0.28" { header_ok = true; continue; }
        if line == "END" { break; }
        let mut it = line.split_whitespace();
        if let (Some(k), Some(v), None) = (it.next(), it.next(), it.next()) {
            m.insert(k.to_string(), v.to_string());
        }
    }
    if !header_ok { panic!("expected REALPROMOTE 0.28"); }

    let sealed = get(&m,"sealed","PASS") == "PASS";
    let lineage = get(&m,"lineage","PASS") == "PASS";
    let audit = get(&m,"audit","PASS") == "PASS";
    if !(sealed && lineage && audit) { panic!("governance gate"); }

    let old = get(&m,"prior_relation","INCOMPARABLE");
    let new = get(&m,"new_relation","INCOMPARABLE");
    let sb = get(&m,"scope_before","LOCAL");
    let sa = get(&m,"scope_after","LOCAL");
    let hb = get(&m,"horizon_before","MEDIUM");
    let ha = get(&m,"horizon_after","MEDIUM");
    let rb = get(&m,"reason_before","INDEPENDENT_WORLD_CONTACT");
    let ra = get(&m,"reason_after","INDEPENDENT_WORLD_CONTACT");
    let vb = yn(get(&m,"veto_before","OFF"));
    let va = yn(get(&m,"veto_after","OFF"));
    let cb = yn(get(&m,"cycle_before","OFF"));
    let ca = yn(get(&m,"cycle_after","OFF"));
    let reopen = yn(get(&m,"reopen","NO"));
    let lost = yn(get(&m,"lost_option","NO"));
    let debt = yn(get(&m,"irreversible_debt","NO"));
    let provenance = yn(get(&m,"provenance_changed","NO"));
    let material_flag = yn(get(&m,"material_history","NO"));
    let chronology = yn(get(&m,"chronology_only","NO"));
    let order_sensitive = yn(get(&m,"event_order_sensitive","NO"));
    let same_ancestry = yn(get(&m,"same_ancestry","YES"));

    let material = material_flag || lost || debt || provenance;
    let transition =
        if chronology && !material { "HISTORY_IRRELEVANT" }
        else if rb != ra { "REASON_MUTATED" }
        else if !vb && va { "VETO_ACTIVATED" }
        else if vb && !va { "VETO_RETIRED" }
        else if reopen { "REOPENED" }
        else if sb != sa { "SCOPE_REVERSED" }
        else if hb != ha { "HORIZON_REVERSED" }
        else if !cb && ca { "CYCLE_ENTERED" }
        else if cb && !ca { "CYCLE_EXITED" }
        else if old == "INCOMPARABLE" && new == "DOMINATES" { "INCOMPARABLE_TO_DOMINATES" }
        else if old == "DOMINATES" && new == "INCOMPARABLE" { "DOMINATES_TO_INCOMPARABLE" }
        else if old != new { "RELATION_REVISED" }
        else { "STABLE" };

    let exact = old == new && sb == sa && hb == ha && rb == ra && vb == va && cb == ca
        && !lost && !debt && !provenance;
    let mutation = if rb != ra { format!("{rb}_TO_{ra}") } else { "NONE".into() };
    let independent = if rb != ra && same_ancestry { "NO" } else { "NOT_INFERRED" };
    let veto_transition = if !vb && va { "ACTIVATED" } else if vb && !va { "RETIRED" } else { "STABLE" };

    println!("promotion.transition={transition}");
    println!("promotion.old_relation={old}");
    println!("promotion.new_relation={new}");
    println!("promotion.history_material={}", if material {"YES"} else {"NO"});
    println!("promotion.path_sensitive={}", if material || order_sensitive {"YES"} else {"NO"});
    println!("promotion.revision_commutative={}", if order_sensitive {"NO"} else {"YES"});
    println!("promotion.hysteresis={}", if lost || debt || provenance {"ACTIVE"} else {"INACTIVE"});
    println!("promotion.lost_option_debt={}", if lost || debt {"ACTIVE"} else {"INACTIVE"});
    println!("promotion.reason_mutation={mutation}");
    println!("promotion.veto_transition={veto_transition}");
    println!("promotion.reopen={}", if reopen {"YES"} else {"NO"});
    println!("promotion.exact_restoration={}", if exact {"YES"} else {"NO"});
    println!("promotion.independent_warrant_created={independent}");
    println!("promotion.history_scalarization=OFF");
    println!("promotion.universal_historical_meta_utility=NOT_EARNED");
    println!("promotion.prtr=CANDIDATE");
    println!("promotion.phl=CANDIDATE");
    println!("promotion.odr=CANDIDATE");
    println!("promotion.rmr=CANDIDATE");
}
