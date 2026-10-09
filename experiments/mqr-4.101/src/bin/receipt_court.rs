use mqr4101_fallible_reference::{sharp_error_counts,risk_dominance};
use std::{env,fs};
fn main(){
 let path=env::args().nth(1).expect("CSV required");
 let data=fs::read_to_string(path).expect("source-based CSV missing");
 let mut rows=0_u64;let mut cuts=[(400_u64,0_u64,0_u64,0_u64);5];
 for (i,s) in data.lines().enumerate(){
    if i==0 {assert_eq!(s,"cutoff_ms,record,n,m,missing,reference_disagreement,perfect_reference_lower_count,perfect_reference_upper_count");continue}
    let c=s.split(',').collect::<Vec<_>>();assert_eq!(c.len(),8);
    let parse=|j:usize| c[j].parse::<u64>().expect("integer source court");
    let cut=parse(0);let n=parse(2);let m=parse(3);let miss=parse(4);let e=parse(5);
    assert_eq!(n-m,miss);assert_eq!(e,parse(6));assert_eq!(e+miss,parse(7));
    let j=match cut{400=>0,420=>1,440=>2,460=>3,480=>4,_=>panic!("unknown cutoff")};
    assert_eq!(cuts[j].0,cut);cuts[j].1+=n;cuts[j].2+=m;cuts[j].3+=e;rows+=1;
 }
 assert_eq!(rows,55);
 for (cut,n,m,e) in cuts{
    assert_eq!((n,m),(487,402));
    let expected=match cut{400=>88,420=>76,440=>76,460=>66,480=>42,_=>unreachable!()};
    assert_eq!(e,expected);
    let (l0,u0)=sharp_error_counts(n,m,e,0).unwrap();assert_eq!((l0,u0),(e,e+85));
    assert_eq!(sharp_error_counts(n,m,e,m),Some((0,n)));
    println!("NONCLINICAL_CUTOFF {} PARTIAL_REFERENCE_MISSINGNESS [{} / {}, {} / {}]",cut,l0,n,u0,n);
 }
 assert!(risk_dominance(487,(0,487),(0,487)).unwrap().starts_with("NO"));
 println!("MQR4101_P1_RUST_INDEPENDENT_CSV_COUNT_AND_SHARPNESS_PASS; EXTERNAL_REFERENCE_ERROR_CERTIFICATE_HOLD");
}
