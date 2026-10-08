//! P8.7: a source-grounded counterfactual negative-reference bridge.
//!
//! Every source case has the SAME fixed Maxent predictor scores, the SAME
//! external target positives, and TWO precisely defined target-backgrounds:
//! Q_unrecorded = source grid cells without recorded occurrence;
//! Q_all_valid = multiset union of scored positive cells and unrecorded cells.
//! This second background is a counterfactual source-derived grid design,
//! NOT the original Maxent training-region 4-fold CV background.
//!
//! Exact empirical algebra:
//! AUC(f;P+,Q_all) = N_neg/(N_pos+N_neg) AUC(f;P+,Q_unrecorded)
//!                 + N_pos/(N_pos+N_neg) * 1/2,
//! where both score sets remain unchanged. We calculate actual rank AUC
//! independently for BOTH references and test the identity, including ties.
//! No claim of spatial leakage, independent grid errors or causal policy effect.
use std::{env,fs};

fn rank_auc(positives:&[f64], negatives:&[f64])->Result<f64,String>{
    if positives.is_empty() || negatives.is_empty(){return Err("empty positive or background reference".into())}
    if positives.iter().chain(negatives.iter()).any(|x|!x.is_finite() || !(0.0..=1.0).contains(x)){
        return Err("bad source prediction".into())
    }
    let mut reference=negatives.to_vec();
    reference.sort_by(f64::total_cmp);
    let mut wins_twice:u128=0;
    for p in positives{
        let lower=reference.partition_point(|q|*q<*p);
        let equal_or_lower=reference.partition_point(|q|*q<=*p);
        wins_twice+=(lower as u128)*2+(equal_or_lower-lower) as u128;
    }
    Ok(wins_twice as f64/(2.0*positives.len() as f64*reference.len() as f64))
}

fn compare(source:&str)->Result<(usize,usize,f64,f64,f64),String>{
    let mut pos=vec![];let mut neg=vec![];
    let mut lines=source.lines();
    if lines.next()!=Some("label,score"){return Err("wrong stream schema".into())}
    for line in lines.filter(|line|!line.is_empty()){
        let (label,score)=line.split_once(',').ok_or("source row missing column")?;
        let val:f64=score.parse().map_err(|_|"non numeric score")?;
        match label{"1"=>pos.push(val),"0"=>neg.push(val),_=>return Err("unknown target class".into())}
    }
    let base=rank_auc(&pos,&neg)?;
    let mut union=neg.clone();union.extend_from_slice(&pos);
    let normalized=rank_auc(&pos,&union)?;
    let pos_on_pos=rank_auc(&pos,&pos)?;
    if (pos_on_pos-0.5).abs()>1e-12{return Err("source positive-v-positive identity failed".into())}
    let mixture=base*neg.len() as f64/union.len() as f64+
                0.5*pos.len() as f64/union.len() as f64;
    if (mixture-normalized).abs()>1e-12 {
        return Err(format!("empirical reference-normalization identity failed: {mixture} != {normalized}"));
    }
    Ok((pos.len(),neg.len(),base,normalized,normalized-base))
}
fn main(){
    let args:Vec<_>=env::args().collect();
    if args.len()!=3 {
        eprintln!("usage: cargo run --bin reference_union_auc -- <case-id> <source-scores.csv>");
        std::process::exit(2)
    }
    let raw=fs::read_to_string(&args[2]).expect("missing raw source score stream");
    let (npos,nneg,original,uniform,delta)=compare(&raw).expect("invalid reference bridge");
    println!("MQR490_REFERENCE_BRIDGE_CASE={}",args[1]);
    println!("MQR490_REFERENCE_BRIDGE_POSITIVE_N={npos}");
    println!("MQR490_REFERENCE_BRIDGE_UNRECORDED_N={nneg}");
    println!("MQR490_REFERENCE_BRIDGE_SOURCE_NEGATIVE_AUC={original:.8}");
    println!("MQR490_REFERENCE_BRIDGE_ALL_GRID_BACKGROUND_AUC={uniform:.8}");
    println!("MQR490_REFERENCE_BRIDGE_CHANGE_ONLY_NEGATIVE_DEFINITION={delta:+.8}");
    println!("MQR490_REFERENCE_BRIDGE_EMPIRICAL_MIXTURE_IDENTITY=PASS");
    println!("MQR490_REFERENCE_BRIDGE_MATCHED_CV_BACKGROUND=NOT_ESTABLISHED");
}
#[cfg(test)]
mod tests{
    use super::*;
    #[test]
    fn target_grid_union_changes_auc_with_fixed_model(){
        let (p,n,old,new,d)=compare("label,score\n1,0.8\n1,0.9\n0,0.1\n0,0.2\n").unwrap();
        assert_eq!((p,n),(2,2));
        assert!((old-1.0).abs()<1e-12);
        assert!((new-0.75).abs()<1e-12);
        assert!((d+0.25).abs()<1e-12);
    }
    #[test]
    fn tied_and_equal_ranks(){
        let (_,_,old,new,d)=compare("label,score\n1,0.5\n0,0.5\n").unwrap();
        assert!((old-0.5).abs()<1e-12 && (new-0.5).abs()<1e-12 && d.abs()<1e-12);
        assert!(compare("label,score\n1,nan\n0,0.5\n").is_err());
    }
}
