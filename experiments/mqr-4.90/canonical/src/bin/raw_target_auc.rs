//! MQR 4.90 independent raw-score AUC calculation under a FIXED
//! target reference-negative definition; does not upgrade AUC across
//! heterogeneous sampling designs to signed generalization optimism.
use std::{env, fs};
fn compute_auc(raw: &str) -> Result<(f64, usize, usize), String> {
    let mut pos: Vec<f64> = Vec::new();
    let mut neg: Vec<f64> = Vec::new();
    for (i, line) in raw.lines().enumerate() {
        if i == 0 {
            if line.trim() != "label,score" {
                return Err("score stream schema mismatch".into());
            }
            continue;
        }
        if line.trim().is_empty() {
            continue;
        }
        let (tag, value) = line.trim().split_once(',')
            .ok_or("score row needs label and score")?;
        let v: f64 = value.parse().map_err(|_| "invalid source score")?;
        if !v.is_finite() || !(0.0..=1.0).contains(&v) {
            return Err("non-finite or out-of-range cloglog prediction".into());
        }
        match tag {
            "1" => pos.push(v),
            "0" => neg.push(v),
            _ => return Err("invalid target class".into()),
        }
    }
    if pos.is_empty() || neg.is_empty() {
        return Err("AUC needs both presence and reference-negative cells".into());
    }
    neg.sort_by(|a,b| a.total_cmp(b));
    // All pairwise matches; ties count exactly one half.
    let mut wins2: u128 = 0;
    for p in &pos {
        let less = neg.partition_point(|n| *n < *p);
        let equal_or_less = neg.partition_point(|n| *n <= *p);
        wins2 += (less as u128) * 2 + (equal_or_less - less) as u128;
    }
    let auc = wins2 as f64 / (2.0 * pos.len() as f64 * neg.len() as f64);
    Ok((auc, pos.len(), neg.len()))
}
fn main() {
    let args: Vec<_> = env::args().collect();
    if args.len() != 2 {
        eprintln!("usage: cargo run --bin raw_target_auc -- <score-stream.csv>");
        std::process::exit(2);
    }
    let src = fs::read_to_string(&args[1]).expect("source stream read failed");
    let (auc, npos, nneg) = compute_auc(&src).expect("source score verification failed");
    println!("MQR490_P8_RECOMPUTED_EXTERNAL_AUC={auc:.8}");
    println!("MQR490_P8_REFERENCE_PRESENCE_COUNT={npos}");
    println!("MQR490_P8_REFERENCE_NEGATIVE_COUNT={nneg}");
    if (auc - 0.53).abs() > 0.005 {
        eprintln!("MQR490_P8_MATCH_ORIGINAL_ROUNDED_AUC=FAIL: {auc:.8} vs 0.53");
        std::process::exit(1);
    }
    println!("MQR490_P8_MATCH_ORIGINAL_ROUNDED_AUC=PASS");
    println!("MQR490_P8_CROSS_DESIGN_SIGNED_BIAS=NOT_IDENTIFIED");
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn handles_exact_wins_losses_and_ties() {
        assert_eq!(compute_auc("label,score\n1,0.9\n0,0.2\n").unwrap().0, 1.);
        assert_eq!(compute_auc("label,score\n1,0.1\n0,0.8\n").unwrap().0, 0.);
        assert_eq!(compute_auc("label,score\n1,0.5\n0,0.5\n").unwrap().0, 0.5);
        assert!(compute_auc("label,score\n1,0.5\n").is_err());
        assert!(compute_auc("label,score\n1,nan\n0,0.5\n").is_err());
    }
}
