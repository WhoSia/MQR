//! MQR-4.90 P8 reference-normalization IDENTIFICATION court.
//!
//! AUC(f;P+,Q-) = E_Q g_f(N), where 0<=g_f<=1 is the
//! pairwise (tie-adjusted) ranking probability against P+.
//! If f and P+ are FIXED and TV(Q1,Q0)<=delta,
//! |AUC(f;P+,Q1)-AUC(f;P+,Q0)|<=delta.
//! This is a standard total-variation expectation inequality, not a
//! new theorem. The actual CV/background and external unrecorded-grid
//! distributions have NO verified TV bound. All delta<1 examples are
//! HYPOTHETICAL sensitivity analyses, NOT empirical corrections.
//!
//! Data fixture source: raw Zenodo 19970795 source scores reproduced
//! independently in Rust GitHub Actions 37728772674, 10 case results;
//! all belong to only THREE biological families under ONE publication.
use std::collections::BTreeSet;
use std::{env,fs};
use std::path::Path;

const HEADER: &str = "source_case,n_positive,n_negative,published_external_auc,recomputed_external_auc,source_doi,source_actions_run";
fn route(name:&str)->Result<&'static str,String>{
    if name.starts_with("Oxalis_latifolia_") { Ok("Oxalis latifolia") }
    else if name.starts_with("Digitaria_sanguinalis_") { Ok("Digitaria sanguinalis") }
    else if name.starts_with("Amaranthus_retroflexus_") { Ok("Amaranthus retroflexus") }
    else { Err(format!("unknown biological source family: {name}")) }
}
fn hypothetical_reference_only_bounds(external:f64,delta:f64)->(f64,f64){
    assert!((0.0..=1.0).contains(&external) && (0.0..=1.0).contains(&delta));
    (0.0_f64.max(external-delta)-external,
     1.0_f64.min(external+delta)-external)
}
fn audit()->Result<(),String>{
    let path=Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent().ok_or("no source parent")?
        .join("matsui_2026_native_only_raw_auc_reproduction.csv");
    let src=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut lines=src.lines();
    if lines.next()!=Some(HEADER) {return Err("source case schema mismatch".into())}
    let mut seen=BTreeSet::new();
    let mut families=BTreeSet::new();
    let mut count=0;
    for row in lines.filter(|x|!x.is_empty()) {
        let c:Vec<_>=row.split(',').collect();
        if c.len()!=7 {return Err("invalid raw target reproduction row".into())}
        if !seen.insert(c[0]){return Err("same target included twice".into())}
        families.insert(route(c[0])?);
        let positive:usize=c[1].parse().map_err(|_|"invalid positive count")?;
        let negative:usize=c[2].parse().map_err(|_|"invalid negative count")?;
        let expected:f64=c[3].parse().map_err(|_|"invalid original AUC")?;
        let recomputed:f64=c[4].parse().map_err(|_|"invalid recomputed AUC")?;
        if positive==0 || negative==0 ||
           !(0.0..=1.0).contains(&recomputed) ||
           (recomputed-expected).abs()>0.005001 ||
           c[5]!="10.5281/zenodo.19970795" || c[6]!="37728772674" {
            return Err(format!("source provenance or AUC reproduction invalid: {}",c[0]));
        }
        let (vacuous_lo,vacuous_hi)=hypothetical_reference_only_bounds(recomputed,1.0);
        let (sensitivity_lo,sensitivity_hi)=hypothetical_reference_only_bounds(recomputed,0.10);
        if !(vacuous_lo<=0. && vacuous_hi>=0. && sensitivity_lo<=0. && sensitivity_hi>=0.) {
            return Err("unknown reference-normalization set excludes unchanged reference".into());
        }
        println!("MQR490_P8_TV_CASE={} SOURCE_AUC={:.8} UNBOUNDED_DELTA=[{:.8},{:.8}] CONDITIONAL_IF_TV_LE_0.10=[{:.8},{:.8}]",
            c[0],recomputed,vacuous_lo,vacuous_hi,sensitivity_lo,sensitivity_hi);
        count+=1;
    }
    if count!=10 || families.len()!=3 {return Err("ten targets or three families not accounted".into())}
    println!("MQR490_P8_TV_PRIOR_BOUND=NOT_MEASURED");
    println!("MQR490_P8_COMMON_PREDICTOR=NOT_RECONSTRUCTED_ACROSS_CV");
    println!("MQR490_P8_EMPIRICAL_CAUSAL_OPTIMISM=NOT_IDENTIFIED");
    println!("MQR490_P8_PARTIAL_IDENTIFICATION_TYPE_COURT=PASS");
    Ok(())
}
fn main(){if let Err(e)=audit(){eprintln!("MQR490_P8_PARTIAL_IDENTIFICATION_TYPE_COURT=FAIL {e}");std::process::exit(1)}}
#[cfg(test)]
mod tests{
use super::*;
#[test] fn extreme_external_auc_bounds(){assert_eq!(hypothetical_reference_only_bounds(0.,1.),(0.,1.));assert_eq!(hypothetical_reference_only_bounds(1.,1.),(-1.,0.));}
#[test] fn hypothetical_tv_is_not_observation(){
    let (lo,hi)=hypothetical_reference_only_bounds(0.53192970,0.10);
    assert!((lo+0.10).abs()<1e-10 && (hi-0.10).abs()<1e-10);
    let (lo2,hi2)=hypothetical_reference_only_bounds(0.53192970,1.0);
    assert!((lo2+0.53192970).abs()<1e-10 && (hi2-0.46807030).abs()<1e-10);
}
#[test] fn verified_source_rows_are_typed(){audit().unwrap();}
}
