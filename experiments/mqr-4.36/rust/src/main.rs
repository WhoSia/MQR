use std::{
    collections::{BTreeMap, BTreeSet},
    env, fs,
    path::Path,
};

#[derive(Clone, Debug)]
struct Row {
    case_id: String,
    fiber: String,
    version: String,
    probe_class: String,
    probe_id: String,
    exact: String,
    coarse: String,
    status: String,
}

#[derive(Default)]
struct CaseRows {
    fiber: String,
    rows: Vec<Row>,
}

fn parse(path: &Path) -> Result<Vec<Row>, String> {
    let s = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut out = Vec::new();
    for (i, line) in s.lines().enumerate() {
        if i == 0 || line.trim().is_empty() {
            continue;
        }
        let p: Vec<&str> = line.split('\t').collect();
        if p.len() != 8 {
            return Err(format!(
                "{}:{}: expected 8 columns, got {}",
                path.display(),
                i + 1,
                p.len()
            ));
        }
        out.push(Row {
            case_id: p[0].into(),
            fiber: p[1].into(),
            version: p[2].into(),
            probe_class: p[3].into(),
            probe_id: p[4].into(),
            exact: p[5].into(),
            coarse: p[6].into(),
            status: p[7].into(),
        });
    }
    Ok(out)
}

fn expected_versions(case: &str) -> Option<[&'static str; 3]> {
    match case {
        "JSCHEMA-001" => Some(["3.2.0", "4.17.3", "4.25.1"]),
        "OASV-001" => Some(["0.5.6", "0.6.0", "0.7.2"]),
        "UCD2-001" => Some(["14.0.0", "15.1.0", "16.0.0"]),
        "WCWIDTH-001" => Some(["0.2.5", "0.2.10", "0.2.14"]),
        _ => None,
    }
}

fn case_reach(c: &CaseRows, case: &str) -> Result<(String, bool, String, String), String> {
    let [a, b, cc] = expected_versions(case).ok_or_else(|| format!("unknown case {case}"))?;
    let mut versions: BTreeSet<String> = BTreeSet::new();
    for r in &c.rows {
        versions.insert(r.version.clone());
    }
    for v in [a, b, cc] {
        if !versions.contains(v) {
            return Ok(("E3_UNRESOLVED".into(), false, "HOLD".into(), "HOLD".into()));
        }
    }

    let mut by: BTreeMap<(String, String, String), &Row> = BTreeMap::new();
    for r in &c.rows {
        by.insert(
            (r.version.clone(), r.probe_class.clone(), r.probe_id.clone()),
            r,
        );
    }

    let mut core_ids = BTreeSet::new();
    let mut refinement_ids = BTreeSet::new();
    for r in &c.rows {
        if r.probe_class == "CORE" {
            core_ids.insert(r.probe_id.clone());
        }
        if r.probe_class == "REFINEMENT" {
            refinement_ids.insert(r.probe_id.clone());
        }
    }

    let any_error = c.rows.iter().any(|r| r.status != "OK");
    if any_error {
        return Ok(("E3_UNRESOLVED".into(), false, "HOLD".into(), "HOLD".into()));
    }

    let lookup = |v: &str, k: &str, id: &str| -> Result<&Row, String> {
        by.get(&(v.to_string(), k.to_string(), id.to_string()))
            .copied()
            .ok_or_else(|| format!("missing {case}/{v}/{k}/{id}"))
    };

    let mut bridge_ok = true;
    for id in &core_ids {
        let ra = lookup(a, "CORE", id)?;
        let rb = lookup(b, "CORE", id)?;
        let rc = lookup(cc, "CORE", id)?;
        if ra.coarse != rb.coarse || rb.coarse != rc.coarse {
            bridge_ok = false;
        }
    }
    if !bridge_ok {
        return Ok((
            "E2_NONE".into(),
            false,
            "ACTION_REJECT_REUSE".into(),
            "REJECT_CORE_REUSE".into(),
        ));
    }

    let mut ac_core_coarse = true;
    let mut ac_all_exact = true;
    for id in &core_ids {
        let ra = lookup(a, "CORE", id)?;
        let rc = lookup(cc, "CORE", id)?;
        if ra.coarse != rc.coarse {
            ac_core_coarse = false;
        }
        if ra.exact != rc.exact {
            ac_all_exact = false;
        }
    }
    for id in &refinement_ids {
        let ra = lookup(a, "REFINEMENT", id)?;
        let rc = lookup(cc, "REFINEMENT", id)?;
        if ra.exact != rc.exact {
            ac_all_exact = false;
        }
    }

    let reach = if !ac_core_coarse {
        "E2_NONE"
    } else if ac_all_exact {
        "E0_FULL"
    } else {
        "E1_QUOTIENT_ONLY"
    };
    let d36 = match reach {
        "E0_FULL" => "ACTION_FULL_REUSE",
        "E1_QUOTIENT_ONLY" => "ACTION_CORE_ONLY",
        "E2_NONE" => "ACTION_REJECT_REUSE",
        _ => "ACTION_HOLD",
    };
    let dcore = match reach {
        "E0_FULL" | "E1_QUOTIENT_ONLY" => "ALLOW_CORE_REUSE",
        "E2_NONE" => "REJECT_CORE_REUSE",
        _ => "HOLD",
    };
    Ok((reach.into(), true, d36.into(), dcore.into()))
}

fn main() -> Result<(), String> {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        return Err("usage: mqr436-adjudicate TSV...".into());
    }
    let mut cases: BTreeMap<String, CaseRows> = BTreeMap::new();
    for a in args {
        for r in parse(Path::new(&a))? {
            let entry = cases.entry(r.case_id.clone()).or_default();
            if entry.fiber.is_empty() {
                entry.fiber = r.fiber.clone();
            }
            if entry.fiber != r.fiber {
                return Err("fiber mismatch".into());
            }
            entry.rows.push(r);
        }
    }

    let expected = ["JSCHEMA-001", "OASV-001", "UCD2-001", "WCWIDTH-001"];
    let mut reach_by_fiber: BTreeMap<String, Vec<(String, String, bool, String, String)>> =
        BTreeMap::new();
    let mut executed_atoms = 0usize;
    let mut unresolved_atoms = 0usize;
    for case in expected {
        let c = cases
            .get(case)
            .ok_or_else(|| format!("missing case {case}"))?;
        executed_atoms += c.rows.len();
        unresolved_atoms += c.rows.iter().filter(|r| r.status != "OK").count();
        let (reach, admitted, d36, dcore) = case_reach(c, case)?;
        println!(
            "CASE={case}\tFIBER={}\tADMITTED={}\tREACH={reach}\tD36={d36}\tD36_CORE={dcore}",
            c.fiber, admitted
        );
        reach_by_fiber.entry(c.fiber.clone()).or_default().push((
            case.into(),
            reach,
            admitted,
            d36,
            dcore,
        ));
    }

    let mut e_collisions = 0usize;
    let mut d36_collisions = 0usize;
    let mut dcore_collisions = 0usize;
    for (fiber, vals) in &reach_by_fiber {
        let admitted: Vec<_> = vals.iter().filter(|v| v.2).collect();
        let es: BTreeSet<_> = admitted.iter().map(|v| v.1.as_str()).collect();
        let ds: BTreeSet<_> = admitted.iter().map(|v| v.3.as_str()).collect();
        let cs: BTreeSet<_> = admitted.iter().map(|v| v.4.as_str()).collect();
        if es.len() > 1 {
            e_collisions += 1;
            println!(
                "NU3_COLLISION_FIBER={fiber}\tREACHES={}",
                es.into_iter().collect::<Vec<_>>().join(",")
            );
        }
        if ds.len() > 1 {
            d36_collisions += 1;
        }
        if cs.len() > 1 {
            dcore_collisions += 1;
        }
    }

    println!("FRESH_CASES=4");
    println!("FRESH_LINEAGE_KINDS=1");
    println!("FRESH_RESEARCH_LAB_N=0");
    println!("NU3_FRESH_E_COLLISION_FIBERS={e_collisions}");
    println!("D36_COLLISION_FIBERS={d36_collisions}");
    println!("D36_CORE_COLLISION_FIBERS={dcore_collisions}");
    println!("EXECUTED_ATOMIC_ROWS={executed_atoms}");
    println!("UNRESOLVED_ATOMIC_ROWS={unresolved_atoms}");
    println!(
        "DECLARED_PROBE_CLASS_ENUMERATION={}",
        if unresolved_atoms == 0 {
            "COMPLETE"
        } else {
            "EXECUTED_WITH_UNRESOLVED"
        }
    );
    println!(
        "INTERNAL_RESIDUE_WITHIN_DECLARED_PROBE_CLASS={}",
        if unresolved_atoms == 0 {
            "ZERO"
        } else {
            "UNRESOLVED"
        }
    );
    println!("OPEN_WORLD_RESIDUE=NOT_ELIMINATED");
    if e_collisions > 0 {
        println!("NU3_NATURALISTIC_SUFFICIENCY=FAIL");
    } else {
        println!("NU3_NATURALISTIC_SUFFICIENCY=NOT_DEFEATED_ON_ADMITTED_FRESH_CORPUS");
    }
    println!("NU3_NATURALISTIC_IDENTIFICATION=HOLD");
    println!("POST_REVEAL_RESCUE=FORBIDDEN");
    Ok(())
}
