//! Read-only dependency triage. Zero automatic delete authority.
//! Run from repository root: rustc tools/mqr-retirement-audit.rs -o /tmp/mqr-retirement-audit && /tmp/mqr-retirement-audit
use std::collections::BTreeMap;
use std::fs;
use std::path::Path;
use std::process::Command;

const CANDIDATES: &[&str] = &[
    "experiments/mqr_4107/calibration_identifiability.py",
    "experiments/mqr_4107/calibration_model_misspecification.py",
    "experiments/mqr_4107/independent_principle_court.py",
    "experiments/mqr_4107/regnault_comparability.py",
    "experiments/mqr_4108/graph_table_sufficiency_counterexample.py",
    "experiments/mqr_4108/traceability_counterexample.py",
    "experiments/mqr_4109/provenance_blackwell_court.py",
];

fn is_text(path: &str) -> bool {
    let p = Path::new(path);
    let ext = p.extension().and_then(|s| s.to_str()).unwrap_or("");
    matches!(ext, "md" | "rs" | "py" | "toml" | "yml" | "yaml" | "sh" | "json" | "txt" | "lean" | "xml" | "ini" | "cfg")
}
fn operation_surface(path: &str) -> bool {
    path.starts_with(".github/workflows/") || path.starts_with("tools/")
        || path.starts_with("experiments/") || path.starts_with("language/")
        || path.starts_with("protocols/") || path.starts_with("doctrine/")
}
fn contains_reference(haystack: &str, path: &str) -> bool {
    let parent = path.rsplit_once('/').unwrap().0;
    let base = path.rsplit('/').next().unwrap();
    haystack.contains(path) ||
    haystack.contains(base) ||
    haystack.contains(&format!("{parent}/**")) ||
    haystack.contains(&format!("{parent}/*"))
}
fn main() {
    let out = Command::new("git").args(["ls-files","-z"]).output()
        .expect("git ls-files must be runnable from repo root");
    assert!(out.status.success(), "git ls-files failed");
    let paths: Vec<String> = out.stdout.split(|b| *b == 0)
        .filter(|part| !part.is_empty())
        .map(|part| String::from_utf8_lossy(part).into_owned()).collect();
    let mut decoded = BTreeMap::new();
    for path in &paths {
        if !is_text(path) || path == "tools/mqr-retirement-audit.rs" { continue; }
        if let Ok(buf) = fs::read(path) {
            if buf.len() < 2_000_000 {
                decoded.insert(path.clone(), String::from_utf8_lossy(&buf).into_owned());
            }
        }
    }
    println!("MQR_REVERSE_DEPENDENCY_AUDIT;tracked_paths={};text_scanned={};mode=ADVISORY_NO_DELETION",
        paths.len(), decoded.len());
    for candidate in CANDIDATES {
        if !paths.iter().any(|p| p == candidate) {
            if *candidate == "experiments/mqr_4107/calibration_model_misspecification.py" {
                println!("CANDIDATE={candidate}");
                println!("  status=RETIRED_ARCHIVED_DRIVE_1Q5EGGj74dLfxxC3sOj2yE3Ni2_Z9ydjd");
                continue;
            }
            panic!("unaccounted missing candidate: {candidate}");
        }
        let mut operational = Vec::new();
        let mut documentary = Vec::new();
        for (p, body) in &decoded {
            if p == candidate { continue; }
            if contains_reference(body, candidate) {
                if operation_surface(p) {operational.push(p.as_str());}
                else {documentary.push(p.as_str());}
            }
        }
        println!("CANDIDATE={candidate}");
        println!("  operational_references={}; documentary_references={}", operational.len(),documentary.len());
        for p in operational { println!("  OP:{p}"); }
        for p in documentary { println!("  DOC:{p}"); }
        println!("  verdict=HOLD_PENDING_RUNTIME_GLOBS_DYNAMIC_IMPORTS_ARCHIVE_AND_HUMAN_CHECK");
    }
    println!("MQR_RETIREMENT_STATIC_DEPENDENCY_AUDIT_FINISHED;AUTO_DELETE=0");
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn matches_direct_filename_and_dir_globs() {
        let p="experiments/mqr_4108/traceability_counterexample.py";
        assert!(contains_reference("python experiments/mqr_4108/traceability_counterexample.py",p));
        assert!(contains_reference("python traceability_counterexample.py",p));
        assert!(contains_reference("paths: ['experiments/mqr_4108/**']",p));
        assert!(!contains_reference("read unrelated.txt",p));
    }
    #[test] fn distinguishes_operational_from_documentary() {
        assert!(operation_surface(".github/workflows/test.yml"));
        assert!(operation_surface("language/real/src/main.rs"));
        assert!(!operation_surface("research/historical.md"));
        assert!(!operation_surface("README.md"));
    }
}
