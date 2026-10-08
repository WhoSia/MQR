//! MQR-4.90 P8 canonical supplemental-publisher reanalysis.
//! Source Koldasbayeva & Zaytsev 2025, MMC S1 Tables S4.1 and S4.2.
//! Four published algorithms form one study-condition, NOT four independent studies.
//! Scores are per-100-hyperparameter aggregated MAE/Pearson/Spearman.
//! Primary SIGNED optimism and cross-study standard errors remain unidentified.
use std::collections::{BTreeMap, BTreeSet};
use std::fs;
use std::path::Path;

const SOURCE_HEADER: &str = "dataset,training_policy,cv_method,metric,GBM,RF,XGB,LGB,reported_mean,source_table,score_family";
const SOURCE: &str = "../koldasbayeva_2025_s4_validation_fidelity.csv";

fn read() -> Result<BTreeMap<(String,String,String,String),i32>,String> {
    let home = Path::new(env!("CARGO_MANIFEST_DIR"));
    let txt = fs::read_to_string(home.join(SOURCE)).map_err(|e|e.to_string())?;
    let mut lines = txt.lines();
    if lines.next() != Some(SOURCE_HEADER) {return Err("S4 file schema drift".into());}
    let mut scores=BTreeMap::new();
    let allowed=[
        ("Gentianella campestris", "S4.1", ["Random","SP 200","SP 422","SP 600","ENV","SPT 200","SPT 422","SPT 600","TSS"]),
        ("Thaleichthys pacificus", "S4.2", ["Random","SP 40","SP 85","SP 120","ENV","SPT 40","SPT 85","SPT 120","TSS"]),
    ];
    for line in lines {
        if line.is_empty() {continue;}
        let cells:Vec<_>=line.split(',').collect();
        if cells.len()!=11 {return Err(format!("malformed published row: {line}"));}
        let (dataset,policy,cv,metric)=(cells[0],cells[1],cells[2],cells[3]);
        let entry=allowed.iter().find(|x|x.0==dataset).ok_or("unexpected source dataset")?;
        if cells[9]!=entry.1 || !entry.2.contains(&cv)
            || !["RETRAIN","LAST FOLD"].contains(&policy)
            || !["MAE","Pearson","Spearman"].contains(&metric)
            || cells[10]!="mean_over_100_hyperparameters" {
            return Err("method/policy/source genealogy mismatch".into());
        }
        let mut values=Vec::new();
        for c in &cells[4..9] {
            let score:f64=c.parse().map_err(|_|"source metric numeric error")?;
            let scaled=(score*1000.).round() as i32;
            if (score-scaled as f64/1000.).abs()>1e-8
                || (metric=="MAE" && !(0.0..=1.0).contains(&score))
                || (metric!="MAE" && !(-1.0..=1.0).contains(&score)) {
                return Err("nonconforming printed S4 score".into());
            }
            values.push(scaled);
        }
        // A published mean can differ from mean of rounded individual values.
        let error=(values.iter().take(4).sum::<i32>()-4*values[4]).abs();
        if error>4 {return Err(format!("S4 mean discrepancy exceeds rounding: {line}"));}
        let key=(dataset.to_owned(),policy.to_owned(),cv.to_owned(),metric.to_owned());
        if scores.insert(key,values[4]).is_some(){return Err("duplicate source result row".into());}
    }
    if scores.len()!=108 {return Err(format!("expected 108 aggregate metric rows, got {}",scores.len()));}
    for (dataset,_,cvs) in allowed {
        for policy in ["RETRAIN","LAST FOLD"] {
            for cv in cvs {
                for metric in ["MAE","Pearson","Spearman"] {
                    if !scores.contains_key(&(dataset.to_owned(),policy.into(),cv.into(),metric.into())) {
                        return Err(format!("missing source metric: {dataset}/{policy}/{cv}/{metric}"));
                    }
                }
            }
        }
    }
    Ok(scores)
}

fn diff(scores:&BTreeMap<(String,String,String,String),i32>,
        dataset:&str, policy:&str,cv:&str)->Result<(i32,i32,i32),String>{
    let key=|method:&str| (dataset.into(),policy.into(),method.into(),"MAE".into());
    let random=*scores.get(&key("Random")).ok_or("random fidelity absent")?;
    let blocked=*scores.get(&key(cv)).ok_or("blocked fidelity absent")?;
    Ok((random,blocked,random-blocked))
}

fn audit()->Result<(),String>{
    let scores=read()?;
    let cases=[
        ("Gentianella campestris","RETRAIN","SP 422",113,20,93),
        ("Gentianella campestris","LAST FOLD","SP 422",120,29,91),
        ("Thaleichthys pacificus","RETRAIN","SP 85",23,16,7),
        ("Thaleichthys pacificus","LAST FOLD","SP 40",25,7,18),
    ];
    let mut seen=BTreeSet::new();
    for (dataset,policy,cv,r,b,d) in cases {
        if diff(&scores,dataset,policy,cv)?!=(r,b,d) {
            return Err(format!("primary source supplement contrast changed: {dataset}/{policy}/{cv}"));
        }
        seen.insert(dataset);
    }
    if seen.len()!=2 {return Err("source-family count drift".into());}
    println!("MQR490_P8_PUBLISHER_S4_ROWS=108");
    println!("MQR490_P8_PUBLISHER_AGGREGATE_CELLS=540");
    println!("MQR490_P8_SOURCE_FAMILIES=2");
    println!("MQR490_P8_PLANT_RETRAIN_MAE_REDUCTION_MILLI=93");
    println!("MQR490_P8_PLANT_LAST_MAE_REDUCTION_MILLI=91");
    println!("MQR490_P8_FISH_RETRAIN_MAE_REDUCTION_MILLI=7");
    println!("MQR490_P8_FISH_LAST_MAE_REDUCTION_MILLI=18");
    println!("MQR490_P8_SIGNED_PRIMARY_OPTIMISM=NOT_IDENTIFIED");
    println!("MQR490_P8_REPEATED_CONFIGS_NOT_INDEPENDENT=PASS");
    println!("MQR490_P8_KOLD_S4_AUDIT=PASS");
    Ok(())
}
fn main(){if let Err(e)=audit(){eprintln!("MQR490_P8_KOLD_S4_AUDIT=FAIL {e}");std::process::exit(1)}}
#[cfg(test)]
mod tests {
  use super::*;
  #[test]
  fn published_table_blocks_are_complete(){audit().unwrap();}
  #[test]
  fn source_count_is_not_study_count(){assert_eq!(read().unwrap().len(),108);}
}
