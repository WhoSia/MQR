//! MQR-4.102: bounded binary decision-contrast audit.
 //! Tests exact finite Hamming-set identification; not reader error calibration.
use std::{collections::BTreeMap,env,fs::File,io::{BufRead,BufReader}};
pub fn count_interval(disagreements:i64,certified_sum:i64,audited_disagreements:i64)->(i64,i64){
    assert!(audited_disagreements>=0&&audited_disagreements<=disagreements);
    assert!(certified_sum.abs()<=audited_disagreements);
    assert_eq!((certified_sum-audited_disagreements)%2,0);
    let remain=disagreements-audited_disagreements;
    (certified_sum-remain,certified_sum+remain)
}
#[test]fn exhaustive_binary_worlds(){
    for d in 0..=9_i64 {
        for m in 0..=d {
            let mut possible=std::collections::BTreeSet::new();
            for observed in 0..(1_usize<<m){
                let audit_sum=2*(observed.count_ones() as i64)-m;
                possible.clear();
                for unobs in 0..(1_usize<<(d-m)){
                    let v=audit_sum+2*(unobs.count_ones() as i64)-(d-m);
                    possible.insert(v);
                }
                let (lo,hi)=count_interval(d,audit_sum,m);
                assert_eq!((lo,hi),(*possible.first().unwrap(),*possible.last().unwrap()));
            }
        }
    }
}
#[test]fn finite_real_receipt_contract(){
    assert_eq!(count_interval(76,0,0),(-76,76));
    assert_eq!(count_interval(76,0,10),(-66,66));
    assert_eq!(402-10,392);
    assert_eq!(10*76,760);
    // The 487-case difference is NOT defined without reader-two decisions
    // in 85 incomplete rows; no extension is presumed.
}
fn main(){
    let path=env::args().nth(1).expect("Usage: cargo run --bin adjudication_court -- SOURCE_487.csv");
    let f=BufReader::new(File::open(path).unwrap());
    let mut lines=f.lines();
    let headers:Vec<String>=lines.next().unwrap().unwrap().trim_end_matches('\r').split(',').map(str::to_owned).collect();
    let field=|name:&str|->usize{headers.iter().position(|s|s==name).unwrap()};
    let record=field("record");let paired=field("paired_complete");let q1=field("q1_QT_ms");let q2=field("q2_QT_ms");
    let mut m=0_i64;let mut n=0_i64;let mut disagreement=0_i64;
    let mut by=BTreeMap::<String,(i64,i64,i64)>::new();
    for l in lines{
        let t=l.unwrap(); if t.trim().is_empty(){continue}
        let x:Vec<_>=t.trim_end_matches('\r').split(',').collect();
        assert_eq!(x.len(),headers.len());
        let e=by.entry(x[record].to_string()).or_default();e.0+=1;n+=1;
        if x[paired]=="1"{
            m+=1;e.1+=1;
            let a=x[q1].parse::<f64>().unwrap()>=440.0;
            let b=x[q2].parse::<f64>().unwrap()>=440.0;
            if a!=b{e.2+=1;disagreement+=1;}
        } else {assert_eq!(x[paired],"0")}
    }
    assert_eq!((n,m,disagreement,by.len()),(487,402,76,11));
    assert_eq!(by["sel102"],(85,2,0));
    assert_eq!(by["sel223"],(31,31,26));
    assert_eq!(by.values().map(|v|v.2).sum::<i64>(),76);
    assert_eq!(by.values().map(|v|v.0-v.1).sum::<i64>(),85);
    let mut better=Vec::<(i64,String)>::new();
    for (rec,(_,paired,discord)) in &by{
        for _ in 0..*discord{better.push((*paired,rec.clone()));}
    }
    better.sort();
    assert_eq!(better.len(),76);
    let chosen=&better[..10];
    assert_eq!(chosen.iter().filter(|(n,_)|*n==30).count(),10);
    let width_reduction=chosen.iter().map(|(den,_)|2.0/(11.0*(*den as f64))).sum::<f64>();
    assert!((width_reduction-2.0/33.0).abs()<1e-12);
    println!("MQR4102_RUST_DISCORDANCE_402_76_AND_SHARP_BOUNDS=PASS;TRUE_REFERENCE_VALIDATION=HOLD");
}
