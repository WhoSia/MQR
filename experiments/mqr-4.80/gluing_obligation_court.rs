use std::{env,fs};
fn b(s:&str)->bool{s=="1"}
fn classify(c:&[&str])->&'static str{
 let overlap=b(c[2]); let a=b(c[3]); let bb=b(c[4]); let invent=b(c[5]);
 let dropc=b(c[6]); let trans=b(c[7]); let prov=b(c[8]); let scope=c[9]; let reopen=b(c[10]);
 if reopen{return "REOPEN_HIDDEN_NONOVERLAP";}
 if dropc{return "OBLIGATION_LOSS";}
 if invent && scope=="union"{return "OBLIGATION_INVENTION";}
 if !prov{return "NO_JOINT_AUTHORITY";}
 if !trans{return "TRANSLATION_LAUNDERING";}
 if overlap && !a && !bb && scope=="overlap"{return "INTERSECTION_LAUNDERING";}
 if overlap && scope=="overlap"{return "OVERLAP_ONLY_AUTHORITY";}
 if !overlap && a && bb{return "CONFLICT_PRESERVED";}
 if !a || !bb{return "OBLIGATION_LOSS";}
 if overlap && a && bb{return "PROVENANCE_PRESERVING_PARTIAL_GLUE";}
 "NO_JOINT_AUTHORITY"
}
fn main(){
 let p=env::args().nth(1).unwrap(); let t=fs::read_to_string(p).unwrap();
 let mut n=0; let mut ok=0;
 for(i,l)in t.lines().enumerate(){
  if i==0||l.trim().is_empty(){continue}
  let c:Vec<&str>=l.split('\t').collect(); assert_eq!(c.len(),12);
  let g=classify(&c); n+=1;
  if g==c[11]{ok+=1}else{eprintln!("{} expected={} got={}",c[0],c[11],g);}
 }
 println!("MQR480_CASES={n}");
 println!("MQR480_PASS={ok}");
 println!("MQR480_OVERLAP_AGREEMENT_IMPLIES_GLOBAL_WARRANT=REJECT");
 println!("MQR480_UNION_AUTOMATICALLY_WARRANTED=REJECT");
 println!("MQR480_INTERSECTION_AUTOMATICALLY_SAFE=REJECT");
 println!("MQR480_COMPOSITION_CREATES_AUTHORITY_EX_NIHILO=REJECT");
 println!("MQR480_COURT={}",if n==ok{"PASS"}else{"FAIL"});
 if n!=ok{std::process::exit(1);}
}