use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

#[derive(Clone, Debug)]
struct Query { id: String, kind: String }

#[derive(Clone, Debug)]
struct Generator { id: String, class: String, ancestry: String }

#[derive(Clone, Debug)]
struct Rival { id: String, phase: String, generator: String }

#[derive(Clone, Debug)]
struct Root { id: String, kind: String, fresh: String }

#[derive(Clone, Debug)]
struct Obligation { id: String, phase: String }

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    queries: BTreeMap<String, Query>,
    generators: BTreeMap<String, Generator>,
    rivals: BTreeMap<String, Rival>,
    admits: BTreeMap<String, String>,
    distinguishes: BTreeSet<(String, String, String)>,
    aliases: BTreeSet<(String, String, String)>,
    roots: BTreeMap<String, Root>,
    obligations: BTreeMap<String, Obligation>,
    separates: BTreeSet<(String, String)>,
    searches: Vec<(String, u64, String)>,
    grammar_closed: bool,
    expect_escape: Option<String>,
    expect_off_query: Option<String>,
    expect_common_mode: Option<String>,
    expect_saturation_mirage: Option<String>,
    expect_rank_before: Option<String>,
    expect_rank_after: Option<String>,
}

fn toks(s: &str) -> Vec<String> {
    s.split_whitespace().map(|x| x.trim_matches('"').to_string()).collect()
}

fn pair(a: &str, b: &str) -> (String, String) {
    if a <= b { (a.to_string(), b.to_string()) } else { (b.to_string(), a.to_string()) }
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

        if t[0] == "REALFRONTIER" {
            if t.len() != 2 || t[1] != "0.9" { return Err("expected REALFRONTIER 0.9".into()); }
            started = true;
            continue;
        }
        if !started { return Err("packet must begin REALFRONTIER 0.9".into()); }
        if t[0] == "END" { ended = true; break; }

        match t[0].as_str() {
            "id" if t.len() == 2 => p.id = t[1].clone(),
            "claim_scope" if t.len() == 2 => p.claim_scope = t[1].clone(),
            "query" if t.len() == 3 => {
                let kind = t[2].to_uppercase();
                if !["BASE", "EXTENSION"].contains(&kind.as_str()) { return Err(format!("invalid query kind {kind}")); }
                p.queries.insert(t[1].clone(), Query { id: t[1].clone(), kind });
            }
            "generator" if t.len() == 4 => {
                p.generators.insert(t[1].clone(), Generator { id: t[1].clone(), class: t[2].clone(), ancestry: t[3].clone() });
            }
            "rival" if t.len() == 4 => {
                let phase = t[2].to_uppercase();
                if !["BASELINE", "DISCOVERED"].contains(&phase.as_str()) { return Err(format!("invalid rival phase {phase}")); }
                p.rivals.insert(t[1].clone(), Rival { id: t[1].clone(), phase, generator: t[3].clone() });
            }
            "admit" if t.len() == 3 => {
                let s = t[2].to_uppercase();
                if !["PASS", "HOLD", "FAIL"].contains(&s.as_str()) { return Err(format!("invalid admit state {s}")); }
                p.admits.insert(t[1].clone(), s);
            }
            "distinguish" if t.len() == 4 => {
                let (a, b) = pair(&t[2], &t[3]);
                p.distinguishes.insert((t[1].clone(), a, b));
            }
            "alias" if t.len() == 4 => {
                let (a, b) = pair(&t[2], &t[3]);
                p.aliases.insert((t[1].clone(), a, b));
            }
            "root" if t.len() == 4 => {
                let kind = t[2].to_uppercase();
                let fresh = t[3].to_uppercase();
                if !["EXTERNAL", "INTERNAL"].contains(&kind.as_str()) { return Err(format!("invalid root kind {kind}")); }
                if !["LIVE", "STALE", "EXPIRED"].contains(&fresh.as_str()) { return Err(format!("invalid root freshness {fresh}")); }
                p.roots.insert(t[1].clone(), Root { id: t[1].clone(), kind, fresh });
            }
            "obligation" if t.len() == 3 => {
                let phase = t[2].to_uppercase();
                if !["BASELINE", "DISCOVERED"].contains(&phase.as_str()) { return Err(format!("invalid obligation phase {phase}")); }
                p.obligations.insert(t[1].clone(), Obligation { id: t[1].clone(), phase });
            }
            "separates" if t.len() == 3 => { p.separates.insert((t[1].clone(), t[2].clone())); }
            "search" if t.len() == 4 => {
                let attempts = t[2].parse::<u64>().map_err(|_| format!("invalid search count {}", t[2]))?;
                let outcome = t[3].to_uppercase();
                if !["NEW", "NO_NEW"].contains(&outcome.as_str()) { return Err(format!("invalid search outcome {outcome}")); }
                p.searches.push((t[1].clone(), attempts, outcome));
            }
            "grammar" if t.len() == 2 => {
                let x = t[1].to_uppercase();
                if !["CLOSED", "OPEN"].contains(&x.as_str()) { return Err(format!("invalid grammar state {x}")); }
                p.grammar_closed = x == "CLOSED";
            }
            "authorize_escape" if t.len() == 2 => p.expect_escape = Some(t[1].to_uppercase()),
            "authorize_off_query_escape" if t.len() == 2 => p.expect_off_query = Some(t[1].to_uppercase()),
            "authorize_common_mode" if t.len() == 2 => p.expect_common_mode = Some(t[1].to_uppercase()),
            "authorize_saturation_mirage" if t.len() == 2 => p.expect_saturation_mirage = Some(t[1].to_uppercase()),
            "authorize_rank_before" if t.len() == 2 => p.expect_rank_before = Some(t[1].to_uppercase()),
            "authorize_rank_after" if t.len() == 2 => p.expect_rank_after = Some(t[1].to_uppercase()),
            _ => return Err(format!("{}:{} malformed command: {line}", path.display(), i + 1)),
        }
    }

    if !ended { return Err("missing END".into()); }
    if p.id.is_empty() || p.claim_scope.is_empty() || p.queries.is_empty() || p.generators.is_empty() || p.rivals.is_empty() {
        return Err("missing required field".into());
    }

    for r in p.rivals.values() {
        if !p.generators.contains_key(&r.generator) { return Err(format!("unknown generator for rival {}: {}", r.id, r.generator)); }
    }
    for r in p.admits.keys() {
        if !p.rivals.contains_key(r) { return Err(format!("unknown rival in admit: {r}")); }
    }
    for (q, a, b) in p.distinguishes.iter().chain(p.aliases.iter()) {
        if !p.queries.contains_key(q) { return Err(format!("unknown query: {q}")); }
        if !p.rivals.contains_key(a) || !p.rivals.contains_key(b) { return Err(format!("unknown rival in query relation: {a},{b}")); }
        if p.distinguishes.contains(&(q.clone(), a.clone(), b.clone())) && p.aliases.contains(&(q.clone(), a.clone(), b.clone())) {
            return Err(format!("query pair both alias and distinguish: {q} {a} {b}"));
        }
    }
    for (r, o) in &p.separates {
        if !p.roots.contains_key(r) { return Err(format!("unknown root in separates: {r}")); }
        if !p.obligations.contains_key(o) { return Err(format!("unknown obligation in separates: {o}")); }
    }
    for (g, _, _) in &p.searches {
        if !p.generators.contains_key(g) { return Err(format!("unknown generator in search: {g}")); }
    }
    Ok(p)
}

fn admitted<'a>(p: &'a Packet, phase: &str) -> Vec<&'a Rival> {
    let mut v: Vec<_> = p.rivals.values()
        .filter(|r| r.phase == phase && p.admits.get(&r.id).map(String::as_str) == Some("PASS"))
        .collect();
    v.sort_by(|a, b| a.id.cmp(&b.id));
    v
}

fn admitted_all<'a>(p: &'a Packet) -> Vec<&'a Rival> {
    let mut v: Vec<_> = p.rivals.values()
        .filter(|r| p.admits.get(&r.id).map(String::as_str) == Some("PASS"))
        .collect();
    v.sort_by(|a, b| a.id.cmp(&b.id));
    v
}

fn base_queries<'a>(p: &'a Packet) -> Vec<&'a Query> {
    let mut v: Vec<_> = p.queries.values().filter(|q| q.kind == "BASE").collect();
    v.sort_by(|a, b| a.id.cmp(&b.id));
    v
}

fn extension_queries<'a>(p: &'a Packet) -> Vec<&'a Query> {
    let mut v: Vec<_> = p.queries.values().filter(|q| q.kind == "EXTENSION").collect();
    v.sort_by(|a, b| a.id.cmp(&b.id));
    v
}

fn rel_has(rel: &BTreeSet<(String, String, String)>, q: &str, a: &str, b: &str) -> bool {
    let (x, y) = pair(a, b);
    rel.contains(&(q.to_string(), x, y))
}

fn current_query_separation(p: &Packet) -> bool {
    let rs = admitted(p, "BASELINE");
    if rs.len() < 2 { return true; }
    let qs = base_queries(p);
    for i in 0..rs.len() {
        for j in i + 1..rs.len() {
            if !qs.iter().any(|q| rel_has(&p.distinguishes, &q.id, &rs[i].id, &rs[j].id)) { return false; }
        }
    }
    true
}

fn off_query_escape(p: &Packet) -> bool {
    let base = admitted(p, "BASELINE");
    let disc = admitted(p, "DISCOVERED");
    let bq = base_queries(p);
    let eq = extension_queries(p);
    disc.iter().any(|d| {
        !base.is_empty() && !bq.is_empty()
            && base.iter().all(|b| bq.iter().all(|q| rel_has(&p.aliases, &q.id, &d.id, &b.id)))
            && base.iter().any(|b| eq.iter().any(|q| rel_has(&p.distinguishes, &q.id, &d.id, &b.id)))
    })
}

fn generator_stats(p: &Packet) -> (usize, usize, bool) {
    let ids: BTreeSet<_> = admitted_all(p).iter().map(|r| r.generator.clone()).collect();
    let ancestries: BTreeSet<_> = ids.iter().filter_map(|g| p.generators.get(g)).map(|g| g.ancestry.clone()).collect();
    let common_mode = ids.len() > 1 && ancestries.len() < ids.len();
    (ids.len(), ancestries.len(), common_mode)
}

fn saturation_mirage(p: &Packet) -> bool {
    for (g1, attempts1, out1) in &p.searches {
        if *attempts1 == 0 || out1 != "NO_NEW" { continue; }
        let Some(a1) = p.generators.get(g1).map(|g| g.ancestry.as_str()) else { continue; };
        for (g2, attempts2, out2) in &p.searches {
            if *attempts2 == 0 || out2 != "NEW" { continue; }
            let Some(a2) = p.generators.get(g2).map(|g| g.ancestry.as_str()) else { continue; };
            if a1 != a2 { return true; }
        }
    }
    false
}

fn generator_relative_saturation(p: &Packet) -> bool {
    !p.searches.is_empty() && p.searches.iter().all(|(_, n, o)| *n > 0 && o == "NO_NEW")
}

fn eligible_roots(p: &Packet) -> Vec<String> {
    let mut v: Vec<_> = p.roots.values().filter(|r| r.kind == "EXTERNAL" && r.fresh == "LIVE").map(|r| r.id.clone()).collect();
    v.sort();
    v
}

fn obligations(p: &Packet, include_discovered: bool) -> Vec<String> {
    let mut v: Vec<_> = p.obligations.values().filter(|o| include_discovered || o.phase == "BASELINE").map(|o| o.id.clone()).collect();
    v.sort();
    v
}

fn combinations(items: &[String], k: usize) -> Vec<Vec<String>> {
    fn rec(items: &[String], k: usize, start: usize, cur: &mut Vec<String>, out: &mut Vec<Vec<String>>) {
        if cur.len() == k { out.push(cur.clone()); return; }
        let need = k - cur.len();
        if items.len().saturating_sub(start) < need { return; }
        for i in start..items.len() {
            cur.push(items[i].clone());
            rec(items, k, i + 1, cur, out);
            cur.pop();
        }
    }
    let mut out = Vec::new();
    rec(items, k, 0, &mut Vec::new(), &mut out);
    out
}

fn covers(p: &Packet, roots: &[String], obs: &[String]) -> bool {
    obs.iter().all(|o| roots.iter().any(|r| p.separates.contains(&(r.clone(), o.clone()))))
}

fn minimum_rank(p: &Packet, include_discovered: bool) -> String {
    let obs = obligations(p, include_discovered);
    if obs.is_empty() { return "0".into(); }
    let roots = eligible_roots(p);
    if roots.len() > 24 { return "TOO_LARGE".into(); }
    for k in 0..=roots.len() {
        if combinations(&roots, k).into_iter().any(|b| covers(p, &b, &obs)) { return k.to_string(); }
    }
    "UNCOVERED".into()
}

fn yes(b: bool) -> &'static str { if b { "YES" } else { "NO" } }

fn analyze(p: &Packet) -> BTreeMap<String, String> {
    let mut a = BTreeMap::new();
    let baseline = admitted(p, "BASELINE");
    let discovered = admitted(p, "DISCOVERED");
    let all = admitted_all(p);
    let (gcount, acount, common_mode) = generator_stats(p);
    let qcur = current_query_separation(p);
    let offq = off_query_escape(p);
    let sat_mirage = saturation_mirage(p);
    let sat = generator_relative_saturation(p);
    let before = minimum_rank(p, false);
    let after = minimum_rank(p, true);
    let stable = !discovered.is_empty() && before == after;
    let inc = match (before.parse::<i64>(), after.parse::<i64>()) { (Ok(b), Ok(c)) => c > b, _ => false };

    a.insert("frontier.baseline_rival_count".into(), baseline.len().to_string());
    a.insert("frontier.discovered_rival_count".into(), discovered.len().to_string());
    a.insert("frontier.admitted_rival_count".into(), all.len().to_string());
    a.insert("frontier.admitted_rivals".into(), all.iter().map(|r| r.id.clone()).collect::<Vec<_>>().join("+"));
    a.insert("frontier.generator_count".into(), gcount.to_string());
    a.insert("frontier.generator_ancestry_count".into(), acount.to_string());
    a.insert("frontier.generator_common_mode_detected".into(), yes(common_mode).into());
    a.insert("frontier.query_separates_current".into(), yes(qcur).into());
    a.insert("frontier.escape_detected".into(), yes(!discovered.is_empty()).into());
    a.insert("frontier.off_query_escape".into(), yes(offq).into());
    a.insert("frontier.saturation_mirage".into(), yes(sat_mirage).into());
    a.insert("frontier.generator_relative_saturation".into(), yes(sat).into());
    a.insert("frontier.grammar_closed".into(), yes(p.grammar_closed).into());
    a.insert("frontier.fcr_before".into(), before);
    a.insert("frontier.fcr_after".into(), after);
    a.insert("frontier.stable_rank_escape".into(), yes(stable).into());
    a.insert("frontier.rank_increasing_escape".into(), yes(inc).into());
    a.insert("frontier.world_complete".into(), "NO".into());
    a.insert("frontier.discovery_value_scalar".into(), "OFF".into());
    a.insert("frontier.fcr_guidance_scope".into(), "CONDITIONAL".into());
    a.insert("frontier.generator_independence_inferred".into(), "NO".into());
    a.insert("frontier.query_language_complete_inferred".into(), "NO".into());
    a.insert("frontier.admission_rule_complete_inferred".into(), "NO".into());
    a.insert("frontier.search_count_implies_completeness".into(), "NO".into());
    a
}

fn validate(p: &Packet, a: &BTreeMap<String, String>) -> Result<(), String> {
    let checks = [
        (&p.expect_escape, "frontier.escape_detected"),
        (&p.expect_off_query, "frontier.off_query_escape"),
        (&p.expect_common_mode, "frontier.generator_common_mode_detected"),
        (&p.expect_saturation_mirage, "frontier.saturation_mirage"),
        (&p.expect_rank_before, "frontier.fcr_before"),
        (&p.expect_rank_after, "frontier.fcr_after"),
    ];
    for (expected, key) in checks {
        if let Some(x) = expected {
            if a[key] != *x { return Err(format!("{key} mismatch expected {x} got {}", a[key])); }
        }
    }
    Ok(())
}

fn emit(p: &Packet, a: &BTreeMap<String, String>) -> String {
    let mut s = format!("REAL-FRONTIER=0.9\nid={}\nclaim_scope={}\n", p.id, p.claim_scope);
    for k in [
        "frontier.baseline_rival_count",
        "frontier.discovered_rival_count",
        "frontier.admitted_rival_count",
        "frontier.admitted_rivals",
        "frontier.generator_count",
        "frontier.generator_ancestry_count",
        "frontier.generator_common_mode_detected",
        "frontier.query_separates_current",
        "frontier.escape_detected",
        "frontier.off_query_escape",
        "frontier.saturation_mirage",
        "frontier.generator_relative_saturation",
        "frontier.grammar_closed",
        "frontier.fcr_before",
        "frontier.fcr_after",
        "frontier.stable_rank_escape",
        "frontier.rank_increasing_escape",
        "frontier.world_complete",
        "frontier.discovery_value_scalar",
        "frontier.fcr_guidance_scope",
        "frontier.generator_independence_inferred",
        "frontier.query_language_complete_inferred",
        "frontier.admission_rule_complete_inferred",
        "frontier.search_count_implies_completeness",
    ] {
        s.push_str(&format!("{k}={}\n", a[k]));
    }
    s.push_str("frontier.meaning=GENERATOR_QUERY_ADMISSION_RELATIVE_OPEN_FRONTIER_RECEIPT\n");
    s.push_str("no_new_rival_does_not_mean_no_possible_rival=true\n");
    s.push_str("delta_fcr_does_not_equal_discovery_value=true\n");
    s.push_str("grammar_closure_does_not_equal_scientific_closure=true\n");
    s.push_str("final_truth_distance=UNIDENTIFIED\n");
    s
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("usage: real-v09-frontier <packet.real> [...]");
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
