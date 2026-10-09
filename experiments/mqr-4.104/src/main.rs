//! MQR-4.104 P1: finite correlated witness nonidentification court.
//! Synthetic truth-bit worlds, NOT real reference truth certificates.
use std::collections::BTreeMap;
type CountMap=BTreeMap<Vec<u8>,usize>;
fn distribution(wrong: bool, count: usize, certified: bool) -> CountMap {
 let mut outcomes=CountMap::new();
 for truth in 0..=1u8 {
   let proxy= if wrong {1-truth} else {truth};
   let mut receipt=vec![proxy;count];
   if certified {receipt.push(truth);}
   *outcomes.entry(receipt).or_insert(0)+=1;
 }
 outcomes
}
fn risk(wrong:bool)->(usize,usize) {
 let errors=(0..=1u8).filter(|&t| (if wrong {1-t} else {t})!=t).count();
 (errors,2)
}
fn court(){
 for k in 1..=4 {
  assert_eq!(distribution(false,k,false),distribution(true,k,false));
  assert_ne!(risk(false),risk(true));
  assert_ne!(distribution(false,k,true),distribution(true,k,true));
 }
 // Pseudo-third readers sharing correlated errors do not make valid gold labels.
 let a=distribution(false,3,false);
 let b=distribution(true,3,false);
 assert_eq!(a,b);
 println!("MQR4104_P1_CORRELATED_WITNESSES_1_TO_4_OBSERVATIONALLY_EQUIVALENT");
 println!("MQR4104_P1_TRUTH_RISK_W0=0/2_W1=2/2");
 println!("MQR4104_P1_ASSUMED_CERTIFIED_ORACLE_BREAKS_EQUIVALENCE_CONDITIONALLY");
 println!("MQR4104_P1_SYNTHETIC_NONIDENTIFICATION_PASS;INDEPENDENT_REFERENCE_TRUTH_HOLD");
}
fn main(){court();}
#[cfg(test)] mod tests{
 use super::*;
 #[test] fn copy_count_does_not_identify_truth(){for k in 1..=4{assert_eq!(distribution(false,k,false),distribution(true,k,false));}}
 #[test] fn risk_differs_even_with_identical_observables(){assert_eq!(risk(false),(0,2));assert_eq!(risk(true),(2,2));}
 #[test] fn third_correlated_label_not_gold(){assert_eq!(distribution(false,3,false),distribution(true,3,false));}
 #[test] fn hypothetical_certified_label_separates_worlds(){for k in 1..=4{assert_ne!(distribution(false,k,true),distribution(true,k,true));}}
}