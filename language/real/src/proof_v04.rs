use std::{
    collections::BTreeMap,
    env, fs,
    path::Path,
};

const GATES: [&str; 4] = ["C", "E", "P", "R"];
const AXES: [&str; 4] = ["W", "N", "I", "D"];

#[derive(Clone, Debug)]
struct Premise {
    id: String,
    kind: String,
    status: String,
    text: String,
}
#[derive(Clone, Debug)]
struct Obligation {
    id: String,
    kind: String,
    text: String,
    deps: Vec<String>,
    proof: String,
    proof_receipt: String,
    requested: String,
}
#[derive(Clone, Debug)]
struct ProbeClass {
    id: String,
    bound: usize,
    scope: String,
}
#[derive(Clone, Debug)]
struct ProbeResidue {
    id: String,
    state: String,
    receipt: String,
}
#[derive(Clone, Debug)]
struct Transport {
    component: String,
    source: String,
    target: String,
    dimension: String,
    evaluability: String,
    survival: String,
    note: String,
}

#[derive(Default)]
struct Packet {
    id: String,
    epoch: String,
    claim_type: String,
    claim_text: String,
    scope: String,
    lineage: String,
    gates: BTreeMap<String, String>,
    axes: BTreeMap<String, (f64, String)>,
    premises: BTreeMap<String, Premise>,
    obligations: BTreeMap<String, Obligation>,
    probe_classes: BTreeMap<String, ProbeClass>,
    probe_residue: Vec<ProbeResidue>,
    transports: Vec<Transport>,
    sources: Vec<String>,
}

fn tokens(s: &str) -> Result<Vec<String>, String> {
    let mut out = Vec::new();
    let mut cur = String::new();
    let mut q = false;
    let mut esc = false;
    for ch in s.chars() {
        if esc {
            cur.push(ch);
            esc = false;
            continue;
        }
        if ch == '\\' {
            esc = true;
            continue;
        }
        if ch == '"' {
            q = !q;
            continue;
        }
        if ch.is_whitespace() && !q {
            if !cur.is_empty() {
                out.push(std::mem::take(&mut cur));
            }
        } else {
            cur.push(ch);
        }
    }
    if esc || q {
        return Err("unterminated quote/escape".into());
    }
    if !cur.is_empty() {
        out.push(cur)
    }
    Ok(out)
}

fn status_rank(s: &str) -> Result<u8, String> {
    match s {
        "FAIL" => Ok(0),
        "HOLD" => Ok(1),
        "PASS" => Ok(2),
        _ => Err(format!("invalid status {s}")),
    }
}
fn transport_authority(e: &str, s: &str) -> Result<&'static str, String> {
    match (e, s) {
        ("TESTED", "SURVIVED") => Ok("TRANSPORT_PASS"),
        ("TESTED", "FAILED") => Ok("TRANSPORT_FAIL"),
        ("TESTED", "MIXED_OR_NONATOMIC") => Ok("SPLIT_REQUIRED"),
        ("UNTESTED_AVAILABLE", "NA") => Ok("HOLD_UNTESTED"),
        ("TARGET_UNAVAILABLE", "NA") => Ok("HOLD_TARGET_UNAVAILABLE"),
        ("OUT_OF_SCOPE", "NA") => Ok("OUT_OF_SCOPE"),
        _ => Err(format!("invalid transport pair {e}/{s}")),
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
        let t = tokens(line).map_err(|e| format!("{}:{}: {e}", path.display(), i + 1))?;
        if t.is_empty() {
            continue;
        }
        if t[0] == "REALPACKET" {
            if t.len() != 2 || t[1] != "0.4" {
                return Err(format!(
                    "{}:{}: expected REALPACKET 0.4",
                    path.display(),
                    i + 1
                ));
            }
            started = true;
            continue;
        }
        if !started {
            return Err(format!(
                "{}:{}: packet must begin REALPACKET 0.4",
                path.display(),
                i + 1
            ));
        }
        if t[0] == "END" {
            ended = true;
            break;
        }
        match t[0].as_str() {
            "id" if t.len() == 2 => p.id = t[1].clone(),
            "epoch" if t.len() == 2 => p.epoch = t[1].clone(),
            "claim" if t.len() >= 3 => {
                p.claim_type = t[1].to_uppercase();
                p.claim_text = t[2..].join(" ");
            }
            "scope" if t.len() >= 2 => p.scope = t[1..].join(" "),
            "lineage" if t.len() == 2 => {
                let k = t[1].to_uppercase();
                if ![
                    "RESEARCH_LAB",
                    "ENGINEERING_DEVELOPMENT",
                    "METHODOLOGY_DEVELOPMENT",
                    "OTHER",
                ]
                .contains(&k.as_str())
                {
                    return Err("invalid lineage".into());
                }
                p.lineage = k;
            }
            "gate" if t.len() == 3 => {
                let g = t[1].to_uppercase();
                let s = t[2].to_uppercase();
                if !GATES.contains(&g.as_str()) {
                    return Err(format!("invalid gate {g}"));
                }
                status_rank(&s)?;
                p.gates.insert(g, s);
            }
            "axis" if t.len() >= 3 => {
                let a = t[1].to_uppercase();
                if !AXES.contains(&a.as_str()) {
                    return Err(format!("v0.4 invalid axis {a}"));
                }
                let v: f64 = t[2].parse().map_err(|_| "axis must be numeric")?;
                if !(0.0..=1.0).contains(&v) {
                    return Err("axis outside [0,1]".into());
                }
                p.axes.insert(a, (v, t[3..].join(" ")));
            }
            "transport" if t.len() >= 8 => {
                let e = t[5].to_uppercase();
                let s = t[6].to_uppercase();
                transport_authority(&e, &s)?;
                p.transports.push(Transport {
                    component: t[1].clone(),
                    source: t[2].clone(),
                    target: t[3].clone(),
                    dimension: t[4].to_uppercase(),
                    evaluability: e,
                    survival: s,
                    note: t[7..].join(" "),
                });
            }
            "premise" if t.len() >= 5 => {
                let id = t[1].clone();
                let kind = t[2].to_uppercase();
                let status = t[3].to_uppercase();
                status_rank(&status)?;
                if !["FORMAL", "EMPIRICAL", "MODEL", "DEFINITION"].contains(&kind.as_str()) {
                    return Err(format!("invalid premise kind {kind}"));
                }
                if p.premises.contains_key(&id) {
                    return Err(format!("duplicate premise {id}"));
                }
                p.premises.insert(
                    id.clone(),
                    Premise {
                        id,
                        kind,
                        status,
                        text: t[4..].join(" "),
                    },
                );
            }
            "obligation" if t.len() >= 4 => {
                let id = t[1].clone();
                let kind = t[2].to_uppercase();
                if !["FORMAL_ONLY", "WORLD_DEPENDENT"].contains(&kind.as_str()) {
                    return Err(format!("invalid obligation kind {kind}"));
                }
                if p.obligations.contains_key(&id) {
                    return Err(format!("duplicate obligation {id}"));
                }
                p.obligations.insert(
                    id.clone(),
                    Obligation {
                        id,
                        kind,
                        text: t[3..].join(" "),
                        deps: Vec::new(),
                        proof: "UNCHECKED".into(),
                        proof_receipt: String::new(),
                        requested: String::new(),
                    },
                );
            }
            "depends" if t.len() >= 3 => {
                let o = p
                    .obligations
                    .get_mut(&t[1])
                    .ok_or_else(|| format!("depends before unknown obligation {}", t[1]))?;
                o.deps = t[2..].to_vec();
            }
            "proof" if t.len() >= 4 => {
                let o = p
                    .obligations
                    .get_mut(&t[1])
                    .ok_or_else(|| format!("proof for unknown obligation {}", t[1]))?;
                let s = t[2].to_uppercase();
                if !["CHECKED", "UNCHECKED", "REFUTED", "NOT_APPLICABLE"].contains(&s.as_str()) {
                    return Err(format!("invalid proof status {s}"));
                }
                o.proof = s;
                o.proof_receipt = t[3..].join(" ");
            }
            "authorize" if t.len() == 3 => {
                let o = p
                    .obligations
                    .get_mut(&t[1])
                    .ok_or_else(|| format!("authorize unknown obligation {}", t[1]))?;
                let s = t[2].to_uppercase();
                status_rank(&s)?;
                o.requested = s;
            }
            "probe_class" if t.len() >= 5 => {
                if t[2].to_uppercase() != "FINITE" {
                    return Err("v0.4 supports only FINITE probe_class".into());
                }
                let n: usize = t[3]
                    .parse()
                    .map_err(|_| "probe_class bound must be integer")?;
                if n == 0 {
                    return Err("probe_class bound must be positive".into());
                }
                let id = t[1].clone();
                p.probe_classes.insert(
                    id.clone(),
                    ProbeClass {
                        id,
                        bound: n,
                        scope: t[4..].join(" "),
                    },
                );
            }
            "probe_residue" if t.len() >= 4 => {
                let state = t[2].to_uppercase();
                if !["ZERO_INTERNAL", "NONZERO", "UNRESOLVED"].contains(&state.as_str()) {
                    return Err(format!("invalid probe residue {state}"));
                }
                p.probe_residue.push(ProbeResidue {
                    id: t[1].clone(),
                    state,
                    receipt: t[3..].join(" "),
                });
            }
            "source" if t.len() >= 2 => p.sources.push(t[1..].join(" ")),
            _ => {
                return Err(format!(
                    "{}:{}: malformed v0.4 command {}",
                    path.display(),
                    i + 1,
                    line
                ));
            }
        }
    }
    if !ended {
        return Err("missing END".into());
    }
    if p.id.is_empty()
        || p.epoch.is_empty()
        || p.claim_type.is_empty()
        || p.claim_text.is_empty()
        || p.scope.is_empty()
        || p.lineage.is_empty()
    {
        return Err("missing required packet field".into());
    }
    for g in GATES {
        if !p.gates.contains_key(g) {
            return Err(format!("missing gate {g}"));
        }
    }
    for a in AXES {
        if !p.axes.contains_key(a) {
            return Err(format!("missing axis {a}"));
        }
    }
    validate(&p)?;
    Ok(p)
}

fn validate(p: &Packet) -> Result<(), String> {
    for o in p.obligations.values() {
        let mut world_deps = Vec::new();
        for d in &o.deps {
            let pr = p
                .premises
                .get(d)
                .ok_or_else(|| format!("obligation {} depends on unknown premise {d}", o.id))?;
            if pr.kind == "EMPIRICAL" || pr.kind == "MODEL" {
                world_deps.push(pr);
            }
        }
        if o.kind == "FORMAL_ONLY" && !world_deps.is_empty() {
            return Err(format!(
                "FORMAL_ONLY obligation {} depends on world-facing premise",
                o.id
            ));
        }
        if o.kind == "WORLD_DEPENDENT" {
            if world_deps.is_empty() {
                return Err(format!(
                    "WORLD_DEPENDENT obligation {} lacks EMPIRICAL/MODEL ancestry",
                    o.id
                ));
            }
            let ceiling = world_deps
                .iter()
                .map(|x| status_rank(&x.status).unwrap())
                .min()
                .unwrap();
            if !o.requested.is_empty() && status_rank(&o.requested)? > ceiling {
                return Err(format!(
                    "FORMAL_CERTAINTY_CANNOT_LAUNDER_EMPIRICAL_UNCERTAINTY: obligation {} requests {} above empirical ceiling",
                    o.id, o.requested
                ));
            }
        } else if !o.requested.is_empty() {
            return Err(format!(
                "FORMAL_ONLY obligation {} may not request empirical authority",
                o.id
            ));
        }
    }
    for r in &p.probe_residue {
        let pc = p
            .probe_classes
            .get(&r.id)
            .ok_or_else(|| format!("probe_residue references unknown class {}", r.id))?;
        if r.state == "ZERO_INTERNAL" && pc.bound == 0 {
            return Err("zero internal residue requires positive finite bound".into());
        }
    }
    Ok(())
}

fn esc(s: &str) -> String {
    s.replace('\\', "\\\\")
        .replace('\n', "\\n")
        .replace('=', "\\=")
}

fn canonical(p: &Packet) -> String {
    let mut o = Vec::new();
    o.push("REAL-LANGUAGE=0.4".into());
    o.push(format!("id={}", esc(&p.id)));
    o.push(format!("epoch={}", esc(&p.epoch)));
    o.push(format!("claim.type={}", esc(&p.claim_type)));
    o.push(format!("claim.text={}", esc(&p.claim_text)));
    o.push(format!("scope={}", esc(&p.scope)));
    o.push(format!("lineage.kind={}", p.lineage));
    for g in GATES {
        o.push(format!("gate.{g}={}", p.gates[g]));
    }
    for a in AXES {
        let (v, n) = &p.axes[a];
        o.push(format!("profile.{a}={v:.6}"));
        o.push(format!("profile.{a}.note={}", esc(n)));
    }
    let packet_auth = if GATES.iter().all(|g| p.gates[*g] == "PASS") {
        "SCOPED_REALIST_AUTHORITY"
    } else {
        "HOLD"
    };
    o.push(format!("authority={packet_auth}"));
    o.push("profile.order=PARETO_PARTIAL".into());
    o.push("profile.scalar.default=OFF".into());
    o.push("legacy.profile.T=DEPRECATED".into());
    o.push(format!("transport.count={}", p.transports.len()));
    for (i, t) in p.transports.iter().enumerate() {
        o.push(format!("transport.{i}.component={}", esc(&t.component)));
        o.push(format!("transport.{i}.source={}", esc(&t.source)));
        o.push(format!("transport.{i}.target={}", esc(&t.target)));
        o.push(format!("transport.{i}.dimension={}", t.dimension));
        o.push(format!("transport.{i}.evaluability={}", t.evaluability));
        o.push(format!("transport.{i}.survival={}", t.survival));
        o.push(format!(
            "transport.{i}.authority={}",
            transport_authority(&t.evaluability, &t.survival).unwrap()
        ));
        o.push(format!("transport.{i}.note={}", esc(&t.note)));
    }
    o.push(format!("premise.count={}", p.premises.len()));
    for (i, pr) in p.premises.values().enumerate() {
        o.push(format!("premise.{i}.id={}", esc(&pr.id)));
        o.push(format!("premise.{i}.kind={}", pr.kind));
        o.push(format!("premise.{i}.status={}", pr.status));
        o.push(format!("premise.{i}.text={}", esc(&pr.text)));
    }
    o.push(format!("obligation.count={}", p.obligations.len()));
    for (i, ob) in p.obligations.values().enumerate() {
        o.push(format!("obligation.{i}.id={}", esc(&ob.id)));
        o.push(format!("obligation.{i}.boundary={}", ob.kind));
        o.push(format!("obligation.{i}.text={}", esc(&ob.text)));
        o.push(format!("obligation.{i}.formal_validity={}", ob.proof));
        o.push(format!(
            "obligation.{i}.proof_receipt={}",
            esc(&ob.proof_receipt)
        ));
        o.push(format!(
            "obligation.{i}.axiom_ancestry={}",
            esc(&ob.deps.join(","))
        ));
        if ob.kind == "WORLD_DEPENDENT" {
            let deps: Vec<_> = ob
                .deps
                .iter()
                .filter_map(|d| p.premises.get(d))
                .filter(|x| x.kind == "EMPIRICAL" || x.kind == "MODEL")
                .collect();
            let rank = deps
                .iter()
                .map(|x| status_rank(&x.status).unwrap())
                .min()
                .unwrap();
            let ceiling = match rank {
                0 => "FAIL",
                1 => "HOLD",
                _ => "PASS",
            };
            o.push(format!(
                "obligation.{i}.empirical_entitlement_ceiling={ceiling}"
            ));
            o.push(format!(
                "obligation.{i}.authorized={}",
                if ob.requested.is_empty() {
                    ceiling
                } else {
                    &ob.requested
                }
            ));
        } else {
            o.push(format!(
                "obligation.{i}.empirical_entitlement_ceiling=NOT_APPLICABLE"
            ));
            o.push(format!("obligation.{i}.authorized=FORMAL_ONLY"));
        }
    }
    o.push(format!("probe_class.count={}", p.probe_classes.len()));
    for (i, pc) in p.probe_classes.values().enumerate() {
        o.push(format!("probe_class.{i}.id={}", esc(&pc.id)));
        o.push(format!("probe_class.{i}.kind=FINITE"));
        o.push(format!("probe_class.{i}.bound={}", pc.bound));
        o.push(format!("probe_class.{i}.scope={}", esc(&pc.scope)));
        if let Some(r) = p.probe_residue.iter().find(|r| r.id == pc.id) {
            o.push(format!("probe_class.{i}.internal_residue={}", r.state));
            o.push(format!(
                "probe_class.{i}.residue_receipt={}",
                esc(&r.receipt)
            ));
        } else {
            o.push(format!("probe_class.{i}.internal_residue=UNRESOLVED"));
        }
    }
    o.push("proof.world_laundering_guard=PASS".into());
    o.push("formal_validity_is_not_empirical_truth=true".into());
    o.push("open_world_residue=true".into());
    o.push("final_truth_distance=UNIDENTIFIED".into());
    for (i, s) in p.sources.iter().enumerate() {
        o.push(format!("source.{i}={}", esc(s)));
    }
    o.join("\n") + "\n"
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("usage: real-v04 PACKET...");
        std::process::exit(2)
    }
    let mut first = true;
    for a in args {
        match parse(Path::new(&a)) {
            Ok(p) => {
                if !first {
                    println!("---")
                }
                print!("{}", canonical(&p));
                first = false;
            }
            Err(e) => {
                eprintln!("{e}");
                std::process::exit(1)
            }
        }
    }
}
