//! MQR-4.90 canonical, dependency-free executable scientific admissibility court.
//! All printed numbers are source-reported observations; not independent replications.
//! GitHub CI runs this binary after Python extraction and before formal regressions.
use std::collections::{BTreeMap, BTreeSet};
use std::fs;
use std::path::Path;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Selection {
    DevelopmentOnly,
    TestOracleMaximum,
    TargetThreshold,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Direction {
    Prospective,
    SpatiallyDisjoint,
    Retrospective,
    Overlapping,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum ClaimScope {
    FutureForecast,
    SpatialTransport,
    HistoricalBackcast,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum NegativeDesign {
    VerifiedAbsence,
    PresenceBackground,
    UnrecordedGridCell,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Reason {
    TestInformedSelection,
    TargetScopeMismatch,
    TargetDesignMismatch,
    DeploymentPolicyMismatch,
    NoPairedUncertainty,
    MissingCohortGenealogy,
    MissingIndependentTarget,
}

#[derive(Debug, Clone, Copy)]
struct Evidence {
    selection: Selection,
    direction: Direction,
    cv_negative: NegativeDesign,
    target_negative: NegativeDesign,
    same_deployment_policy: bool,
    has_paired_uncertainty: bool,
    has_cohort_genealogy: bool,
    independent_target: bool,
}

impl Evidence {
    fn evaluate(&self) -> Vec<Reason> {
        self.evaluate_for(ClaimScope::FutureForecast)
    }

    fn evaluate_for(&self, claim: ClaimScope) -> Vec<Reason> {
        let mut result = Vec::new();
        if self.selection != Selection::DevelopmentOnly {
            result.push(Reason::TestInformedSelection);
        }
        let target_matches_claim = matches!(
            (claim, self.direction),
            (ClaimScope::FutureForecast, Direction::Prospective)
                | (ClaimScope::SpatialTransport, Direction::SpatiallyDisjoint)
                | (ClaimScope::HistoricalBackcast, Direction::Retrospective)
        );
        if !target_matches_claim {
            result.push(Reason::TargetScopeMismatch);
        }
        if self.cv_negative != self.target_negative {
            result.push(Reason::TargetDesignMismatch);
        }
        if !self.same_deployment_policy {
            result.push(Reason::DeploymentPolicyMismatch);
        }
        if !self.has_paired_uncertainty {
            result.push(Reason::NoPairedUncertainty);
        }
        if !self.has_cohort_genealogy {
            result.push(Reason::MissingCohortGenealogy);
        }
        if !self.independent_target {
            result.push(Reason::MissingIndependentTarget);
        }
        result
    }
}

fn eligible_template() -> Evidence {
    Evidence {
        selection: Selection::DevelopmentOnly,
        direction: Direction::Prospective,
        cv_negative: NegativeDesign::VerifiedAbsence,
        target_negative: NegativeDesign::VerifiedAbsence,
        same_deployment_policy: true,
        has_paired_uncertainty: true,
        has_cohort_genealogy: true,
        independent_target: true,
    }
}

/// Exact decimal AUC in *milli-AUC*; no binary floating comparison or silent rounding.
fn milli(text: &str) -> Result<i32, String> {
    let (whole, decimal) = text.trim().split_once('.')
        .ok_or_else(|| format!("missing AUC decimal point: {text}"))?;
    if !(whole == "0" || whole == "1") || decimal.is_empty()
        || decimal.len() > 3 || !decimal.bytes().all(|b| b.is_ascii_digit()) {
        return Err(format!("unsupported exact AUC format: {text}"));
    }
    let numerator: i32 = decimal.parse::<i32>().map_err(|e| e.to_string())?;
    let scale = 10_i32.pow((3 - decimal.len()) as u32);
    let score = whole.parse::<i32>().unwrap() * 1000 + numerator * scale;
    if !(0..=1000).contains(&score) {
        return Err(format!("invalid AUC: {text}"));
    }
    Ok(score)
}

fn csv_rows(path: &Path, header: &str) -> Result<Vec<Vec<String>>, String> {
    let raw = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let mut lines = raw.lines();
    if lines.next() != Some(header) {
        return Err(format!("source schema mismatch: {}", path.display()));
    }
    let result: Vec<_> = lines.filter(|l| !l.trim().is_empty())
        .map(|line| line.split(',').map(|f| f.trim().to_owned()).collect()).collect();
    Ok(result)
}

const KOLD_HEADER: &str =
    "dataset,training_policy,cv_method,GBM,RF,XGB,LGB,reported_mean,source_table,selection_type";
const MATSUI_HEADER: &str =
    "species,calibration,target,internal_cv_auc,external_region_auc,source_cv_table,source_external_table,cv_negative_definition,external_negative_definition,extraction_scope";

#[derive(Debug)]
struct Audit {
    kold_rows: usize,
    kold_cells: usize,
    matsui_pairs: usize,
    matsui_families: usize,
    kold_spread: BTreeMap<(String, String, String), i32>,
    matsui_signed_gap: BTreeMap<(String, String), i32>,
}

fn audit_sources(directory: &Path) -> Result<Audit, String> {
    let kold = csv_rows(&directory.join("koldasbayeva_2025_tables_2_3_oracle_auc.csv"), KOLD_HEADER)?;
    if kold.len() != 36 {
        return Err(format!("expected 36 oracle reporting rows, found {}", kold.len()));
    }
    let mut kold_map = BTreeMap::new();
    let mut kold_count = BTreeMap::new();
    for row in &kold {
        if row.len() != 10 {
            return Err("broken Kold row".into());
        }
        if row[9] != "oracle_test_max" {
            return Err("oracle reporting class was silently promoted".into());
        }
        let species = &row[0];
        let policy = &row[1];
        if !["Gentianella campestris", "Thaleichthys pacificus"].contains(&species.as_str())
            || !["RETRAIN", "LAST FOLD"].contains(&policy.as_str()) {
            return Err("unrecognized target or final-model policy".into());
        }
        let cv = &row[2];
        let printed: Vec<_> = (3..=7).map(|i| milli(&row[i])).collect::<Result<_, _>>()?;
        // Four algorithm values, each printed to 0.001; mean can differ by 0.001.
        let total: i32 = printed.iter().take(4).sum();
        if (total - printed[4] * 4).abs() > 4 {
            return Err(format!("printed algorithm/mean discrepancy: {row:?}"));
        }
        if row[8] != (if species == "Gentianella campestris" {"Table 2"} else {"Table 3"}) {
            return Err("wrong original figure/table lineage".into());
        }
        let key = (species.clone(), policy.clone(), cv.clone());
        if kold_map.insert(key, printed[4]).is_some() {
            return Err("duplicate target-policy-CV cell".into());
        }
        *kold_count.entry((species.clone(), policy.clone())).or_insert(0_usize) += 1;
    }
    if kold_count.len() != 4 || kold_count.values().any(|n| *n != 9) {
        return Err("incomplete block matrix".into());
    }
    let matsui = csv_rows(&directory.join("matsui_2026_native_only_external_auc_pairs.csv"), MATSUI_HEADER)?;
    if matsui.len() != 10 {
        return Err(format!("expected 10 fixed native-only pairs, found {}", matsui.len()));
    }
    let mut seen = BTreeSet::new();
    let mut groups = BTreeMap::new();
    let mut gaps = BTreeMap::new();
    for row in &matsui {
        if row.len() != 10 || row[9] != "native_only" || row[5] != "A4" {
            return Err("Matsui stratum/metadata mismatch".into());
        }
        let (calibration, table, cv, expected_count) = match row[0].as_str() {
            "Oxalis latifolia" => ("America", "A1", 870, 3),
            "Digitaria sanguinalis" => ("Europe", "A2", 820, 4),
            "Amaranthus retroflexus" => ("North America", "A3", 850, 3),
            _ => return Err("unknown Matsui source family".into()),
        };
        if row[1] != calibration || row[6] != table
            || row[7] != "Maxent background"
            || row[8] != "grid cells without recorded presences"
            || row[2] == row[1]
            || milli(&row[3])? != cv {
            return Err("Matsui cross-design or genealogy discrepancy".into());
        }
        let key = (row[0].clone(), row[2].clone());
        if !seen.insert(key.clone()) {
            return Err("duplicated external target".into());
        }
        gaps.insert(key, cv - milli(&row[4])?);
        *groups.entry(row[0].clone()).or_insert(0_usize) += 1;
        if *groups.get(&row[0]).unwrap() > expected_count {
            return Err("unexpected native-only region".into());
        }
    }
    if groups.len() != 3
        || groups.get("Oxalis latifolia") != Some(&3)
        || groups.get("Digitaria sanguinalis") != Some(&4)
        || groups.get("Amaranthus retroflexus") != Some(&3) {
        return Err("regional coverage incomplete".into());
    }
    let diff = |species: &str, policy: &str, cv: &str| -> Result<i32, String> {
        let target = (species.to_string(), policy.to_string(), cv.to_string());
        let random = (species.to_string(), policy.to_string(), "Random".to_string());
        Ok(*kold_map.get(&target).ok_or("missing source cell")? -
           *kold_map.get(&random).ok_or("missing Random baseline")?)
    };
    let plant = "Gentianella campestris";
    let fish = "Thaleichthys pacificus";
    for (species, policy, cv, expected) in [
        (plant, "LAST FOLD", "SP 600", 32), (plant, "RETRAIN", "SP 600", 3),
        (fish, "RETRAIN", "SPT 85", 8), (fish, "LAST FOLD", "SPT 85", -10),
    ] {
        if diff(species, policy, cv)? != expected {
            return Err(format!("published AUC contrast drifted {species}/{policy}/{cv}"));
        }
    }
    for (species, target, expected) in [
        ("Oxalis latifolia", "Oceania", 340),
        ("Oxalis latifolia", "Europe", -20),
        ("Amaranthus retroflexus", "Oceania", -70),
        ("Digitaria sanguinalis", "Africa", 260),
    ] {
        if gaps.get(&(species.to_owned(), target.to_owned())) != Some(&expected) {
            return Err(format!("Matsui source pair drifted {species}/{target}"));
        }
    }
    Ok(Audit {
        kold_rows: kold.len(), kold_cells: kold.len() * 4,
        matsui_pairs: matsui.len(), matsui_families: groups.len(),
        kold_spread: kold_map, matsui_signed_gap: gaps,
    })
}

fn exact_null_oracle() -> (usize, usize, usize, usize) {
    let mut sum_all = 0_usize;
    let mut sum_selected = 0_usize;
    let mut selected = 0_usize;
    let mut total = 0_usize;
    for p in 0..4 {
        for q in (p + 1)..4 {
            let count = (0..4).filter(|i| *i != p && *i != q)
                .map(|n| usize::from(p > n) + usize::from(q > n)).sum::<usize>();
            sum_all += count;
            total += 1;
            if count * 10 > 7 * 4 {
                selected += 1;
                sum_selected += count;
            }
        }
    }
    (sum_all, sum_selected, selected, total)
}

/// AUC wins for one fixed model under an explicitly chosen negative sample.
fn auc_wins(positives: &[i32], negatives: &[i32]) -> Result<(usize, usize), String> {
    if positives.is_empty() || negatives.is_empty() {
        return Err("AUC needs both classes".to_owned());
    }
    let wins = positives.iter().flat_map(|p| negatives.iter().map(move |n| (*p > *n) as usize)).sum();
    Ok((wins, positives.len() * negatives.len()))
}

fn verdict() -> Result<(), String> {
    let path = Path::new(env!("CARGO_MANIFEST_DIR")).parent()
        .ok_or("manifest directory has no dataset parent")?;
    let data = audit_sources(path)?;
    assert_eq!((data.kold_rows, data.kold_cells, data.matsui_pairs, data.matsui_families),
               (36, 144, 10, 3));
    let (all, trunc, admitted, n) = exact_null_oracle();
    if (all, trunc, admitted, n) != (12, 7, 2, 6) {
        return Err("exact six-case AUC oracle fixture mismatch".into());
    }
    let mut oracle = eligible_template();
    oracle.selection = Selection::TestOracleMaximum;
    if oracle.evaluate() != vec![Reason::TestInformedSelection] {
        return Err("oracle test rejection boundary breached".into());
    }
    let mut target = eligible_template();
    target.cv_negative = NegativeDesign::PresenceBackground;
    target.target_negative = NegativeDesign::UnrecordedGridCell;
    if !target.evaluate().contains(&Reason::TargetDesignMismatch) {
        return Err("reference negative design boundary breached".into());
    }
    let mut retrospective = eligible_template();
    retrospective.direction = Direction::Retrospective;
    if !retrospective.evaluate().contains(&Reason::TargetScopeMismatch) {
        return Err("retrospective future claim allowed".into());
    }
    let mut overlapping = eligible_template();
    overlapping.direction = Direction::Overlapping;
    if !overlapping.evaluate().contains(&Reason::TargetScopeMismatch) {
        return Err("overlapping future claim allowed".into());
    }
    let mut spatial = eligible_template();
    spatial.direction = Direction::SpatiallyDisjoint;
    if !spatial.evaluate_for(ClaimScope::SpatialTransport).is_empty()
        || !spatial.evaluate().contains(&Reason::TargetScopeMismatch) {
        return Err("spatial-only evidence cannot be routed to proper scope".into());
    }
    let mut historical = eligible_template();
    historical.direction = Direction::Retrospective;
    if !historical.evaluate_for(ClaimScope::HistoricalBackcast).is_empty()
        || !historical.evaluate().contains(&Reason::TargetScopeMismatch) {
        return Err("retrospective evidence cannot be routed to proper scope".into());
    }
    let mut filtered = eligible_template();
    filtered.selection = Selection::TargetThreshold;
    if !filtered.evaluate().contains(&Reason::TestInformedSelection) {
        return Err("target-outcome conditioned pool promoted".into());
    }
    if data.kold_spread.len() != 36 || data.matsui_signed_gap.len() != 10 {
        return Err("canonical key counts changed".into());
    }
    // One unchanged predictor and unchanged positives [3,4] yield either
    // AUC 1 or AUC 0 solely by changing reference-negative rank choices.
    // It is a two-criterion countermodel, not a measured Matsui effect.
    if auc_wins(&[3, 4], &[1, 2])? != (4, 4)
        || auc_wins(&[3, 4], &[5, 6])? != (0, 4) {
        return Err("identical model / changed negative design countermodel failed".into());
    }
    if !eligible_template().evaluate().is_empty() {
        return Err("positive-control profile is incorrectly rejected".into());
    }
    println!("MQR490_RUST_CANONICAL_SOURCE_ROWS=36");
    println!("MQR490_RUST_CANONICAL_MATSUI_PAIRS=10");
    println!("MQR490_RUST_CANONICAL_FAMILIES=3");
    println!("MQR490_RUST_CANONICAL_NULL_COUNTS=12,7,2,6");
    println!("MQR490_RUST_SCOPE_ROUTING=PASS");
    println!("MQR490_RUST_REFERENCE_NEGATIVE_COUNTERMODEL=PASS");
    println!("MQR490_RUST_PRIMARY_SIGNED_EFFECTS=0");
    println!("MQR490_RUST_POOLED_EFFECT=HOLD");
    println!("MQR490_RUST_VERDICT=PASS");
    Ok(())
}

fn main() {
    if let Err(err) = verdict() {
        eprintln!("MQR490_RUST_FAIL={err}");
        std::process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn admissibility_all_fields_independent() {
        let base = eligible_template();
        assert!(base.evaluate().is_empty());
        let alternatives: Vec<(Evidence, Reason)> = vec![
            (Evidence { selection: Selection::TestOracleMaximum, ..base }, Reason::TestInformedSelection),
            (Evidence { selection: Selection::TargetThreshold, ..base }, Reason::TestInformedSelection),
            (Evidence { direction: Direction::Retrospective, ..base }, Reason::TargetScopeMismatch),
            (Evidence { direction: Direction::Overlapping, ..base }, Reason::TargetScopeMismatch),
            (Evidence { target_negative: NegativeDesign::PresenceBackground, ..base }, Reason::TargetDesignMismatch),
            (Evidence { same_deployment_policy: false, ..base }, Reason::DeploymentPolicyMismatch),
            (Evidence { has_paired_uncertainty: false, ..base }, Reason::NoPairedUncertainty),
            (Evidence { has_cohort_genealogy: false, ..base }, Reason::MissingCohortGenealogy),
            (Evidence { independent_target: false, ..base }, Reason::MissingIndependentTarget),
        ];
        for (fixture, failure) in alternatives {
            assert_eq!(fixture.evaluate(), vec![failure]);
        }
    }
    #[test]
    fn target_claim_scope_changes_admission_legally() {
        let base = eligible_template();
        let spatial = Evidence { direction: Direction::SpatiallyDisjoint, ..base };
        assert_eq!(spatial.evaluate_for(ClaimScope::SpatialTransport), vec![]);
        assert_eq!(spatial.evaluate(), vec![Reason::TargetScopeMismatch]);
        let past = Evidence { direction: Direction::Retrospective, ..base };
        assert_eq!(past.evaluate_for(ClaimScope::HistoricalBackcast), vec![]);
        assert_eq!(past.evaluate(), vec![Reason::TargetScopeMismatch]);
        assert_eq!(past.evaluate_for(ClaimScope::SpatialTransport), vec![Reason::TargetScopeMismatch]);
    }
    #[test]
    fn source_reported_effects_are_not_pooled() {
        verdict().unwrap();
    }
    #[test]
    fn exact_auc_oracle_distribution() {
        assert_eq!(exact_null_oracle(), (12, 7, 2, 6));
        // Expected unconditional AUC 12/(6*4)=0.5;
        // conditioned AUC 7/(2*4)=0.875.
    }
    #[test]
    fn reference_sampling_alone_can_reverse_auc() {
        let positives = [3, 4];
        assert_eq!(auc_wins(&positives, &[1, 2]).unwrap(), (4, 4));
        assert_eq!(auc_wins(&positives, &[5, 6]).unwrap(), (0, 4));
        assert!(auc_wins(&positives, &[]).is_err());
    }
    #[test]
    fn exact_decimal_rejects_bad_source() {
        assert_eq!(milli("0.79").unwrap(), 790);
        assert_eq!(milli("1.000").unwrap(), 1000);
        assert!(milli("1.001").is_err());
        assert!(milli("0.1234").is_err());
        assert!(milli("NaN").is_err());
    }
}
