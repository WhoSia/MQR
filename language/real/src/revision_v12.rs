use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

#[derive(Clone, Debug)]
struct SourceBurden {
    id: String,
    challenges: BTreeSet<String>,
    debt: bool,
}

#[derive(Clone, Debug)]
struct TargetBurden {
    id: String,
    challenges: BTreeSet<String>,
}

#[derive(Clone, Debug)]
struct MapEdge {
    sources: BTreeSet<String>,
    kind: String,
    targets: BTreeSet<String>,
    provenance: String,
}

#[derive(Clone, Debug)]
struct Conflict {
    id: String,
    source_obligation: String,
    target_obligation: String,
    kind: String,
}

#[derive(Clone, Debug)]
struct PathEdge {
    id: String,
    source: String,
    via: String,
    target: String,
    strength: String,
}

#[derive(Default, Debug)]
struct Packet {
    id: String,
    claim_scope: String,
    source_ontology: String,
    target_ontology: String,
    source_burdens: BTreeMap<String, SourceBurden>,
    target_burdens: BTreeMap<String, TargetBurden>,
    maps: Vec<MapEdge>,
    target_cover: BTreeSet<String>,
    withdrawals: BTreeMap<String, bool>,
    debt_traces: BTreeSet<(String, String)>,
    debt_count_mode: String,
    conflicts: Vec<Conflict>,
    paths: Vec<PathEdge>,
    witness_future_burden: String,
    expect_debt_complete: Option<String>,
    expect_merge_preserved: Option<String>,
    expect_path_conflict: Option<String>,
    expect_arbitration: Option<String>,
    expect_same_label_drift: Option<String>,
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

fn yes(x: bool) -> &'static str {
    if x { "YES" } else { "NO" }
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
        if t[0] == "REALREVISE" {
            if t.len() != 2 || t[1] != "0.12" {
                return Err("expected REALREVISE 0.12".into());
            }
            if started {
                return Err("duplicate REALREVISE header".into());
            }
            started = true;
            continue;
        }
        if !started {
            return Err("packet must begin REALREVISE 0.12".into());
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
            "source_ontology" if t.len() == 2 => p.source_ontology = t[1].clone(),
            "target_ontology" if t.len() == 2 => p.target_ontology = t[1].clone(),
            "source_burden" if t.len() == 4 => {
                let state = t[3].to_uppercase();
                if !["DEBT", "CLEAR"].contains(&state.as_str()) {
                    return Err(format!("invalid source burden state: {}", t[3]));
                }
                let challenges = split_plus(&t[2]);
                if challenges.is_empty() {
                    return Err(format!("source burden {} has empty challenge set", t[1]));
                }
                if p.source_burdens.contains_key(&t[1]) {
                    return Err(format!("duplicate source burden: {}", t[1]));
                }
                p.source_burdens.insert(t[1].clone(), SourceBurden {
                    id: t[1].clone(),
                    challenges,
                    debt: state == "DEBT",
                });
            }
            "target_burden" if t.len() == 3 => {
                let challenges = split_plus(&t[2]);
                if challenges.is_empty() {
                    return Err(format!("target burden {} has empty challenge set", t[1]));
                }
                if p.target_burdens.contains_key(&t[1]) {
                    return Err(format!("duplicate target burden: {}", t[1]));
                }
                p.target_burdens.insert(t[1].clone(), TargetBurden {
                    id: t[1].clone(),
                    challenges,
                });
            }
            "map" if t.len() == 5 => {
                let kind = t[2].to_uppercase();
                if !["EXACT", "REFINE", "MERGE", "OVERLAP", "DISJOINT", "UNMAPPED"]
                    .contains(&kind.as_str())
                {
                    return Err(format!("invalid map kind: {}", t[2]));
                }
                let provenance = t[4].to_uppercase();
                if !["INTERNAL", "EXTERNAL", "MIXED"].contains(&provenance.as_str()) {
                    return Err(format!("invalid map provenance: {}", t[4]));
                }
                let sources = split_plus(&t[1]);
                let targets = split_plus(&t[3]);
                if sources.is_empty() {
                    return Err("map has empty source set".into());
                }
                if kind != "UNMAPPED" && kind != "DISJOINT" && targets.is_empty() {
                    return Err("semantic map has empty target set".into());
                }
                p.maps.push(MapEdge { sources, kind, targets, provenance });
            }
            "target_cover" if t.len() == 2 => p.target_cover.extend(split_plus(&t[1])),
            "withdraw_source" if t.len() == 3 => {
                let state = t[2].to_uppercase();
                if !["DECLARED", "NONE"].contains(&state.as_str()) {
                    return Err(format!("invalid withdrawal state: {}", t[2]));
                }
                p.withdrawals.insert(t[1].clone(), state == "DECLARED");
            }
            "debt_trace" if t.len() == 3 => {
                p.debt_traces.insert((t[1].clone(), t[2].clone()));
            }
            "debt_count_mode" if t.len() == 2 => {
                let x = t[1].to_uppercase();
                if !["SOURCE_ANCESTRY", "TARGET_CARRIER"].contains(&x.as_str()) {
                    return Err(format!("invalid debt_count_mode: {}", t[1]));
                }
                p.debt_count_mode = x;
            }
            "conflict" if t.len() == 5 => {
                let kind = t[4].to_uppercase();
                if !["MANDATE", "WITHDRAWAL", "UNMAPPED", "MERGE_COLLISION"].contains(&kind.as_str()) {
                    return Err(format!("invalid conflict kind: {}", t[4]));
                }
                p.conflicts.push(Conflict {
                    id: t[1].clone(),
                    source_obligation: t[2].clone(),
                    target_obligation: t[3].clone(),
                    kind,
                });
            }
            "path" if t.len() == 6 => {
                let strength = t[5].to_uppercase();
                if !["FULL", "PARTIAL", "NONE"].contains(&strength.as_str()) {
                    return Err(format!("invalid path strength: {}", t[5]));
                }
                p.paths.push(PathEdge {
                    id: t[1].clone(),
                    source: t[2].clone(),
                    via: t[3].clone(),
                    target: t[4].clone(),
                    strength,
                });
            }
            "witness_future_burden" if t.len() == 2 => p.witness_future_burden = t[1].clone(),
            "authorize_debt_complete" if t.len() == 2 => p.expect_debt_complete = Some(t[1].to_uppercase()),
            "authorize_merge_preserved" if t.len() == 2 => p.expect_merge_preserved = Some(t[1].to_uppercase()),
            "authorize_path_conflict" if t.len() == 2 => p.expect_path_conflict = Some(t[1].to_uppercase()),
            "authorize_arbitration" if t.len() == 2 => p.expect_arbitration = Some(t[1].to_uppercase()),
            "authorize_same_label_drift" if t.len() == 2 => p.expect_same_label_drift = Some(t[1].to_uppercase()),
            _ => return Err(format!("{}:{} malformed command: {line}", path.display(), i + 1)),
        }
    }

    if !ended {
        return Err("missing END".into());
    }
    if p.id.is_empty()
        || p.claim_scope.is_empty()
        || p.source_ontology.is_empty()
        || p.target_ontology.is_empty()
        || p.source_burdens.is_empty()
        || p.target_burdens.is_empty()
        || p.debt_count_mode.is_empty()
        || p.witness_future_burden.is_empty()
    {
        return Err("missing required field".into());
    }

    for m in &p.maps {
        for s in &m.sources {
            if !p.source_burdens.contains_key(s) {
                return Err(format!("map references unknown source burden: {s}"));
            }
        }
        for t in &m.targets {
            if !p.target_burdens.contains_key(t) {
                return Err(format!("map references unknown target burden: {t}"));
            }
        }
    }
    for t in &p.target_cover {
        if !p.target_burdens.contains_key(t) {
            return Err(format!("target_cover references unknown target burden: {t}"));
        }
    }
    for s in p.withdrawals.keys() {
        if !p.source_burdens.contains_key(s) {
            return Err(format!("withdraw_source references unknown source burden: {s}"));
        }
    }
    for (s, t) in &p.debt_traces {
        if !p.source_burdens.contains_key(s) || !p.target_burdens.contains_key(t) {
            return Err(format!("invalid debt_trace: {s}->{t}"));
        }
    }
    Ok(p)
}

fn target_challenge_union(p: &Packet, targets: &BTreeSet<String>) -> BTreeSet<String> {
    let mut out = BTreeSet::new();
    for t in targets {
        if let Some(tb) = p.target_burdens.get(t) {
            out.extend(tb.challenges.iter().cloned());
        }
    }
    out
}

fn targets_covered(p: &Packet, targets: &BTreeSet<String>) -> bool {
    targets.iter().all(|t| p.target_cover.contains(t))
}

fn traces_complete(p: &Packet, source: &str, targets: &BTreeSet<String>) -> bool {
    targets.iter().all(|t| p.debt_traces.contains(&(source.to_string(), t.clone())))
}

fn debt_transport_ok(p: &Packet, s: &SourceBurden) -> bool {
    if p.withdrawals.get(&s.id).copied().unwrap_or(false) {
        return true;
    }
    p.maps.iter().any(|m| {
        if !m.sources.contains(&s.id) {
            return false;
        }
        match m.kind.as_str() {
            "EXACT" | "REFINE" => {
                m.sources.len() == 1
                    && targets_covered(p, &m.targets)
                    && target_challenge_union(p, &m.targets) == s.challenges
                    && traces_complete(p, &s.id, &m.targets)
            }
            "MERGE" => {
                targets_covered(p, &m.targets)
                    && s.challenges.is_subset(&target_challenge_union(p, &m.targets))
                    && traces_complete(p, &s.id, &m.targets)
            }
            _ => false,
        }
    })
}

fn direct_composed_conflict(p: &Packet) -> bool {
    for d in p.paths.iter().filter(|x| x.via == "DIRECT") {
        for c in p.paths.iter().filter(|x| x.via != "DIRECT") {
            if d.source == c.source && d.target == c.target && d.strength != c.strength {
                return true;
            }
        }
    }
    false
}

fn analyze(p: &Packet) -> BTreeMap<String, String> {
    let mut a = BTreeMap::new();

    let source_count = p.source_burdens.len();
    let target_count = p.target_burdens.len();
    let debt_sources: Vec<_> = p.source_burdens.values().filter(|x| x.debt).collect();
    let debt_source_count = debt_sources.len();

    let count_kind = |k: &str| p.maps.iter().filter(|m| m.kind == k).count();
    let exact_count = count_kind("EXACT");
    let refine_count = count_kind("REFINE");
    let merge_count = count_kind("MERGE");
    let overlap_count = count_kind("OVERLAP");

    let semantic_kind = |k: &str| ["EXACT", "REFINE", "MERGE", "OVERLAP"].contains(&k);
    let mut mapped_sources = BTreeSet::new();
    let mut mapped_targets = BTreeSet::new();
    for m in &p.maps {
        if semantic_kind(&m.kind) {
            mapped_sources.extend(m.sources.iter().cloned());
            mapped_targets.extend(m.targets.iter().cloned());
        }
    }

    let all_sources: BTreeSet<_> = p.source_burdens.keys().cloned().collect();
    let all_targets: BTreeSet<_> = p.target_burdens.keys().cloned().collect();
    let unmapped_sources: BTreeSet<_> = all_sources.difference(&mapped_sources).cloned().collect();
    let novel_targets: BTreeSet<_> = all_targets.difference(&mapped_targets).cloned().collect();

    let same_label_drift = p.source_burdens.values().any(|s| {
        p.target_burdens
            .get(&s.id)
            .map(|t| t.challenges != s.challenges)
            .unwrap_or(false)
    });

    let different_label_exact_alias = p.maps.iter().any(|m| {
        if m.kind != "EXACT" || m.sources.len() != 1 || m.targets.len() != 1 {
            return false;
        }
        let s = m.sources.iter().next().unwrap();
        let t = m.targets.iter().next().unwrap();
        s != t && p.source_burdens[s].challenges == p.target_burdens[t].challenges
    });

    let debt_transport_complete = debt_sources.iter().all(|s| debt_transport_ok(p, s));

    let refinement_multiplicity = p.maps.iter().any(|m| {
        m.kind == "REFINE"
            && m.targets.len() > 1
            && m.sources.iter().any(|s| p.source_burdens[s].debt)
    });
    let debt_double_count = p.debt_count_mode == "TARGET_CARRIER" && refinement_multiplicity;

    let mut merge_collapse = false;
    let mut merge_preserved = true;
    for m in p.maps.iter().filter(|m| m.kind == "MERGE") {
        for s in m.sources.iter().filter(|s| p.source_burdens[*s].debt) {
            if !traces_complete(p, s, &m.targets) {
                merge_collapse = true;
                merge_preserved = false;
            }
        }
    }

    let path_conflict = direct_composed_conflict(p);
    let conflict_count = p.conflicts.len();
    let arbitration_required = conflict_count > 0;

    let reopen = !debt_transport_complete || debt_double_count || merge_collapse || path_conflict || arbitration_required;
    let state = if reopen {
        "REOPEN_REQUIRED"
    } else if !mapped_sources.is_empty() {
        "ADMISSIBLE_MAPPED_SUBSPACE"
    } else {
        "HOLD"
    };

    a.insert("revision.source_burden_count".into(), source_count.to_string());
    a.insert("revision.target_burden_count".into(), target_count.to_string());
    a.insert("revision.map_count".into(), p.maps.len().to_string());
    a.insert("revision.exact_count".into(), exact_count.to_string());
    a.insert("revision.refine_count".into(), refine_count.to_string());
    a.insert("revision.merge_count".into(), merge_count.to_string());
    a.insert("revision.overlap_count".into(), overlap_count.to_string());
    a.insert("revision.unmapped_source_count".into(), unmapped_sources.len().to_string());
    a.insert("revision.unmapped_sources".into(), join_set(&unmapped_sources));
    a.insert("revision.target_novel_burden_count".into(), novel_targets.len().to_string());
    a.insert("revision.target_novel_burdens".into(), join_set(&novel_targets));
    a.insert("revision.same_label_drift".into(), yes(same_label_drift).into());
    a.insert("revision.different_label_exact_alias".into(), yes(different_label_exact_alias).into());
    a.insert("revision.debt_source_count".into(), debt_source_count.to_string());
    a.insert("revision.debt_transport_complete".into(), yes(debt_transport_complete).into());
    a.insert("revision.debt_accounting_mode".into(), p.debt_count_mode.clone());
    a.insert("revision.refinement_multiplicity".into(), yes(refinement_multiplicity).into());
    a.insert("revision.debt_double_count_detected".into(), yes(debt_double_count).into());
    a.insert("revision.debt_collapse_detected".into(), yes(merge_collapse).into());
    a.insert("revision.merge_provenance_preserved".into(), yes(merge_preserved).into());
    a.insert("revision.comparable_source_burden_count".into(), mapped_sources.len().to_string());
    a.insert("revision.comparability_mode".into(), "MAPPED_SUBSPACE_ONLY".into());
    a.insert("revision.conflict_count".into(), conflict_count.to_string());
    a.insert("revision.arbitration_required".into(), yes(arbitration_required).into());
    a.insert("revision.conflict_scalar_default".into(), "OFF".into());
    a.insert("revision.direct_composed_conflict".into(), yes(path_conflict).into());
    a.insert("revision.reopen_required".into(), yes(reopen).into());
    a.insert("revision.reopen_on_path_conflict".into(), "YES".into());
    a.insert("revision.world_burden_identity_inferred".into(), "NO".into());
    a.insert("revision.future_revision_closed".into(), "NO".into());
    a.insert("revision.newer_ontology_truth_oracle".into(), "NO".into());
    a.insert("revision.provenance_truth_oracle".into(), "NO".into());
    a.insert("revision.guidance_mode".into(), "VERSIONED_LOSS_AWARE_TRANSPORT".into());
    a.insert("revision.state".into(), state.into());
    a
}

fn validate(p: &Packet, a: &BTreeMap<String, String>) -> Result<(), String> {
    let checks = [
        (&p.expect_debt_complete, "revision.debt_transport_complete"),
        (&p.expect_merge_preserved, "revision.merge_provenance_preserved"),
        (&p.expect_path_conflict, "revision.direct_composed_conflict"),
        (&p.expect_arbitration, "revision.arbitration_required"),
        (&p.expect_same_label_drift, "revision.same_label_drift"),
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
        "REAL-REVISION=0.12\nid={}\nclaim_scope={}\nsource_ontology={}\ntarget_ontology={}\n",
        p.id, p.claim_scope, p.source_ontology, p.target_ontology
    );
    for key in [
        "revision.source_burden_count",
        "revision.target_burden_count",
        "revision.map_count",
        "revision.exact_count",
        "revision.refine_count",
        "revision.merge_count",
        "revision.overlap_count",
        "revision.unmapped_source_count",
        "revision.unmapped_sources",
        "revision.target_novel_burden_count",
        "revision.target_novel_burdens",
        "revision.same_label_drift",
        "revision.different_label_exact_alias",
        "revision.debt_source_count",
        "revision.debt_transport_complete",
        "revision.debt_accounting_mode",
        "revision.refinement_multiplicity",
        "revision.debt_double_count_detected",
        "revision.debt_collapse_detected",
        "revision.merge_provenance_preserved",
        "revision.comparable_source_burden_count",
        "revision.comparability_mode",
        "revision.conflict_count",
        "revision.arbitration_required",
        "revision.conflict_scalar_default",
        "revision.direct_composed_conflict",
        "revision.reopen_required",
        "revision.reopen_on_path_conflict",
        "revision.world_burden_identity_inferred",
        "revision.future_revision_closed",
        "revision.newer_ontology_truth_oracle",
        "revision.provenance_truth_oracle",
        "revision.guidance_mode",
        "revision.state",
    ] {
        s.push_str(&format!("{key}={}\n", a[key]));
    }
    s.push_str(&format!("witness.future_burden={}\n", p.witness_future_burden));
    s.push_str("revision.meaning=VERSIONED_PARTIAL_BURDEN_TRANSPORT\n");
    s.push_str("same_label_does_not_mean_same_burden=true\n");
    s.push_str("mapping_does_not_mean_world_identity=true\n");
    s.push_str("arbitration_does_not_mean_truth=true\n");
    s.push_str("final_truth_distance=UNIDENTIFIED\n");
    s
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("usage: real-v12-revise <packet.real> [...]");
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
