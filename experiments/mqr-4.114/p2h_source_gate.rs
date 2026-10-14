//! MQR-4.114 P2-H: bounded documentary gate and marginal-covariance counterexample.
//! Uses only source-typed manually audited labels. NOT a laboratory measurement.
const MATRIX: &str = include_str!("fixtures/p2h_evidence_matrix.psv");
#[derive(Debug)]
struct Row<'a> { id: &'a str, source: &'a str, custody: &'a str, independent: &'a str, gate: &'a str }
fn parse(input: &str) -> Result<Vec<Row<'_>>, String> {
    let mut lines = input.lines();
    if lines.next() != Some("id|source_class|custody|physical_independence|claim_gate") {
        return Err("schema mismatch".into());
    }
    let mut rows = Vec::new();
    for (i, line) in lines.enumerate() {
        if line.trim().is_empty() { continue; }
        let p: Vec<_> = line.split('|').collect();
        if p.len()!=5 || p.iter().any(|x| x.is_empty()) {
            return Err(format!("malformed row {}", i+2));
        }
        rows.push(Row{id:p[0],source:p[1],custody:p[2],independent:p[3],gate:p[4]});
    }
    if rows.is_empty() { return Err("empty matrix".into()); }
    Ok(rows)
}
fn audit(rows: &[Row<'_>]) -> Result<(), String> {
    let mut ids = std::collections::HashSet::new();
    for r in rows {
        if !ids.insert(r.id) { return Err(format!("duplicate id {}",r.id)); }
        if r.independent != "UNVERIFIED" { return Err(format!("unexpected independently certified reference: {}", r.id)); }
        match r.id {
            "bipm2018" if r.source=="ORIGINAL_PUBLISHED_REPORT" && r.custody=="SOURCE_DOCUMENT_READ" && r.gate=="AGGREGATE_SOURCE_VALUES" => {},
            "nist917c2020" if r.source=="HISTORICAL_CERTIFICATE_REVISION" && r.gate=="CERTIFIED_CHEMICAL_PURITY_ONLY" => {},
            "four917c_labs" if r.source=="SHARED_CATALOGUE_DESIGNATION" && r.gate=="NO_BETWEEN_LAB_COVARIANCE" => {},
            "retrospectoscope2024" if r.source=="LATER_DERIVED_COMPILATION" && r.custody=="PUBLIC_URL_VERIFIED" && r.gate=="NO_RAW_DETECTOR_CLAIM" => {},
            "original_reporting_forms" if r.custody=="CURRENT_BYTES_UNVERIFIED" => {},
            "original_injection_traces" if r.custody=="CURRENT_BYTES_UNVERIFIED" => {},
            "same_serum_external_reference" if r.custody=="NOT_VERIFIED" && r.gate=="NO_PHYSICAL_TRUTH_CLAIM" => {},
            "drive_search20261014" if r.custody=="NOT_IDENTIFIED_BY_TARGETED_SEARCH" && r.gate=="NO_ABSENCE_CLAIM" => {},
            _ => return Err(format!("unrecognized or improperly promoted row {}", r.id)),
        }
    }
    if ids.len()!=8 { return Err(format!("expected 8 rows, found {}",ids.len())); }
    Ok(())
}
// Two hypothetical bivariate normal covariance matrices with equal marginals.
// Valid positive-definite for 0<rho<1. Neither represents measured CCQM correlations.
fn two_lab_marginal_counterexample(u:f64,rho:f64) -> bool {
    if !(u.is_finite() && u>0.0 && rho.is_finite() && rho>0.0 && rho<1.0) {return false;}
    let v=u*u;
    let independent=[[v,0.0],[0.0,v]];
    let dependent=[[v,rho*v],[rho*v,v]];
    independent[0][0]==dependent[0][0] && independent[1][1]==dependent[1][1]
        && dependent[0][0]*dependent[1][1]-dependent[0][1]*dependent[1][0]>0.0
        && independent[0][1]!=dependent[0][1]
}
fn main() {
    let rows=parse(MATRIX).expect("fixture schema");
    audit(&rows).expect("documentary promotion gate");
    assert!(two_lab_marginal_counterexample(0.004,0.5));
    println!("p2h_fixture_rows={}",rows.len());
    println!("p2h_source_gate=PASS_BOUNDED");
    println!("p2h_marginal_covariance_counterexample=PASS_MATHEMATICAL");
    println!("p2h_raw_workbooks=UNVERIFIED");
    println!("p2h_independent_same_serum_reference=HOLD");
    println!("p2h_new_empirical_measurements=NONE");
}
#[cfg(test)]
mod tests {
 use super::*;
 #[test] fn frozen_fixture_valid() {audit(&parse(MATRIX).unwrap()).unwrap();}
 #[test] fn no_duplicate_ids() {
   let text=format!("{}\n{}",MATRIX,"bipm2018|ORIGINAL_PUBLISHED_REPORT|SOURCE_DOCUMENT_READ|UNVERIFIED|AGGREGATE_SOURCE_VALUES");
   assert!(audit(&parse(&text).unwrap()).is_err());
 }
 #[test] fn prohibit_promotion() {
   let changed=MATRIX.replace("retrospectoscope2024|LATER_DERIVED_COMPILATION|PUBLIC_URL_VERIFIED|UNVERIFIED", "retrospectoscope2024|ORIGINAL_PUBLISHED_REPORT|ORIGINAL_BYTES_INSPECTED|CERTIFIED");
   assert!(audit(&parse(&changed).unwrap()).is_err());
 }
 #[test] fn search_absence_not_proven() {
   let changed=MATRIX.replace("NOT_IDENTIFIED_BY_TARGETED_SEARCH","NONEXISTENT");
   assert!(audit(&parse(&changed).unwrap()).is_err());
 }
 #[test] fn covariance_counterexample() {
   for u in [0.001,0.004,2.0] {for rho in [0.1,0.5,0.99] {assert!(two_lab_marginal_counterexample(u,rho));}}
 }
 #[test] fn covariance_invalid_conditions() {
   for rho in [-0.1,0.0,1.0,1.2,f64::NAN] {assert!(!two_lab_marginal_counterexample(0.004,rho));}
   assert!(!two_lab_marginal_counterexample(0.0,0.5));
 }
}
