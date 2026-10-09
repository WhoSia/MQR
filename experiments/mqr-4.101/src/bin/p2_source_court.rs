//! Source-native independent Rust validator for MQR 4.101 P2.
//! Same fixed publisher-derived CSV as P1; no externally validated truth.
use std::{collections::BTreeMap,env,fs};
fn sharp(d:usize,g:usize,u:usize,kd:usize,kg:usize)->Option<(usize,usize)>{
 if kd>d||kg>g{return None};Some((d-kd,d+kg+u))
}
fn parse_csv(path:&str)->BTreeMap<String,[usize;4]>{
 let s=fs::read_to_string(path).expect("missing pinned QT derived CSV");
 let mut it=s.lines();let headers=it.next().expect("CSV missing header").split(',').collect::<Vec<_>>();
 let ix=|name:&str|headers.iter().position(|v|*v==name).expect("missing source column");
 let rec=ix("record");let paired=ix("paired_complete");let a=ix("q1_QT_ms");let b=ix("q2_QT_ms");
 let mut records=BTreeMap::<String,[usize;4]>::new();
 for line in it{
  let parts=line.split(',').collect::<Vec<_>>();assert_eq!(parts.len(),headers.len());
  let z=records.entry(parts[rec].to_owned()).or_default();z[0]+=1;
  match parts[paired] {
   "1"=> {z[1]+=1;let av=parts[a].parse::<f64>().expect("QT1 missing");let bv=parts[b].parse::<f64>().expect("QT2 missing");assert!(av.is_finite()&&bv.is_finite());if (av>=440.0)!=(bv>=440.0){z[2]+=1;}},
   "0"=>{z[3]+=1;assert!(parts[a].is_empty()||parts[b].is_empty());},
   _=>panic!("bad paired flag")
  }
 }
 records
}
fn main(){
 let path=env::args().nth(1).expect("source CSV path required");let d=parse_csv(&path);
 assert_eq!(d.len(),11);
 let total=[(0..4).map(|i|d.values().map(|r|r[i]).sum()).collect::<Vec<_>>()];
 assert_eq!(total[0],vec![487,402,76,85]);
 assert_eq!(d.get("sel102"),Some(&[85,2,0,83]));
 assert_eq!(d.get("sel213"),Some(&[71,69,3,2]));
 assert_eq!(d.get("sel223"),Some(&[31,31,26,0]));
 assert_eq!(sharp(76,326,85,7,3),Some((69,164)));
 assert_eq!(sharp(76,326,85,10,0),Some((66,161)));
 assert_eq!(sharp(76,326,85,0,10),Some((76,171)));
 println!("MQR4101_P2_RUST_SOURCE_SELECTION_COUNTS_PASS n=487 paired=402 disagreement=76 missing=85 sel102_missing=83 sel213_missing=2");
 println!("MQR4101_P2_RUST_CONDITIONAL_SHARPNESS_PASS;REFERENCE_DEPENDENCE_AND_TRUE_RISK_HOLD");
}
#[cfg(test)]mod tests{
 use super::*;
 #[test]fn corner_cases(){assert_eq!(sharp(76,326,85,7,3),Some((69,164)));assert_eq!(sharp(76,326,85,77,3),None);assert_eq!(sharp(0,0,5,0,0),Some((0,5)));}
 #[test]fn exhaustive_truth_assignments(){
   let mut cases=0;
   for n in 1_u32..=5 {
    for mut code in 0..3_usize.pow(n) {
     let kinds=(0..n).map(|_|{let k=code%3;code/=3;k}).collect::<Vec<_>>();
     let d=kinds.iter().filter(|&&x|x==0).count();let g=kinds.iter().filter(|&&x|x==1).count();let u=kinds.iter().filter(|&&x|x==2).count();
     for kd in 0..=d {for kg in 0..=g {
      let mut low=n as usize+1;let mut high=0;
      for assignment in 0..(1_usize<<n) {
       let mut err_d=0;let mut err_g=0;let mut risk=0;
       for (i,&type_) in kinds.iter().enumerate(){let bit=(assignment>>i)&1;risk+=bit; if type_==0 {err_d+=bit;} else if type_==1 {err_g+=bit;}}
       if d-err_d<=kd && err_g<=kg {low=low.min(risk);high=high.max(risk);}
      }
      assert_eq!(sharp(d,g,u,kd,kg),Some((low,high)));
      cases+=1;
     }}
    }
   }
   assert!(cases>1000);
 }
}
