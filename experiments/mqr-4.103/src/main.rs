//! MQR-4.103 P1: exact finite adaptive verification courts.
//! Hypothetical truthful review oracle, not real QTDB 3rd-party labels.
use std::collections::BTreeMap;
mod p2;
fn histories(theta:u8)->BTreeMap<String,f64>{
 // The first verifier audits case 0 (truth theta0); second allocation depends
 // on first answer: if 0 audit case 1; if 1 audit case 2.
 // Only one truth coordinate can be seen at stage two.
 let t=[(theta>>2)&1,(theta>>1)&1,theta&1];
 let y0=t[0];let i=if y0==0{1}else{2};
 let key=format!("first=0:{};second={}:{};stop=2",y0,i,t[i]);
 BTreeMap::from([(key,1.0)])
}
fn observed_risk(theta:u8)->f64{
 let t=[(theta>>2)&1,(theta>>1)&1,theta&1];
 (t[0]+t[1]+t[2]) as f64/3.0
}
fn oracle_inclusion(theta:u8)->[bool;3]{
 let t0=(theta>>2)&1;
 [true,t0==0,t0==1]
}
fn optional_stopping_exact()->(f64,f64,f64){
 // fair coin X1,X2; stop at t=1 on success, otherwise at t=2.
 // Naive stopped sample mean is biased; stopped centered SUM still mean zero.
 let mut naive=0.0;let mut sum=0.0;let mut ipw=0.0;
 for x1 in 0..=1{for x2 in 0..=1{
  let stop=if x1==1{1.0}else{2.0};
  let x2_seen=if x1==1{0.0}else{x2 as f64};
  let avg=(x1 as f64+x2_seen)/stop;
  naive+=avg/4.0;
  sum+=((x1 as f64-0.5)+if x1==1{0.0}else{x2 as f64-0.5})/4.0;
  // full first-observation estimate has no outcome-conditioned missingness
  ipw+=(x1 as f64)/4.0;
 }}
 (naive,sum,ipw)
}
fn main(){
 let mut classes:BTreeMap<String,Vec<u8>>=BTreeMap::new();
 for truth in 0..8{for (hist,_) in histories(truth){classes.entry(hist).or_default().push(truth)}}
 assert_eq!(classes.len(),4);
 let mut witnesses=Vec::new();
 for (obs,worlds) in &classes{
  assert_eq!(worlds.len(),2);
  let gap=(observed_risk(worlds[1])-observed_risk(worlds[0])).abs();
  assert!((gap-1.0/3.0).abs()<1e-12);
  assert!(oracle_inclusion(worlds[0]).iter().filter(|&&x|x).count()==2);
  witnesses.push(format!("{obs}: worlds={worlds:?}; risk_gap={gap:.6}"));
 }
 let (naive,centered,first)=optional_stopping_exact();
 assert!((naive-0.625).abs()<1e-12);
 assert!(centered.abs()<1e-12);
 assert!((first-0.5).abs()<1e-12);
 println!("MQR4103_P1_WORLD_COUNT=8 OBS_HISTORY_CLASSES={} UNOBSERVED_TRUTH_RISK_GAP=1/3",classes.len());
 for witness in witnesses{println!("WITNESS {witness}");}
 println!("MQR4103_P1_FAIR_COIN_STOPPED_NAIVE_MEAN={naive:.6} FIXED_FIRST_MEAN={first:.6} STOPPED_CENTERED_SUM={centered:.6}");
 println!("MQR4103_P1_FINITE_ADAPTIVE_OBSERVATIONAL_EQUIVALENCE_PASS;EXTERNAL_TRUTH_HOLD");
 p2::run();
}
#[cfg(test)]
mod tests{
 use super::*;
 #[test]fn all_worlds_have_one_unobserved_slot(){for i in 0..8{assert_eq!(oracle_inclusion(i).iter().filter(|&&x|!x).count(),1)}}
 #[test]fn adaptivity_not_same_as_stopping(){let (naive,mart,first)=optional_stopping_exact();assert_eq!(naive,0.625);assert_eq!(mart,0.0);assert_eq!(first,0.5);}
 #[test]fn risk_not_identifiable(){let a=histories(0);let b=histories(1);assert_eq!(a,b);assert_ne!(observed_risk(0),observed_risk(1));}
}