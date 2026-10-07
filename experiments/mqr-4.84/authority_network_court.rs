use std::{env,fs};
fn b(s:&str)->bool{s=="1"}
fn classify(c:&[&str])->&'static str{
 let cycle=b(c[3]); let trans=b(c[4]); let eq=b(c[5]); let debt=b(c[6]);
 let path=b(c[7]); let acyclic=b(c[8]); let preorder=b(c[9]); let break_warrant=b(c[10]);
 let totalize=b(c[11]); let completion=b(c[12]); let incomparable=b(c[13]); let reopen=b(c[14]);
 if reopen{return "REOPEN_UNDER_NETWORK_INCONSISTENCY";}
 if cycle && !trans && !eq{return "GLOBALLY_CYCLIC_CLOSURE";}
 if cycle && trans && !eq{return "EQUIVALENCE_CLASS_FRACTURE";}
 if debt{return "RESIDUAL_DEBT_ROUTING_HOLONOMY";}
 if path{return "PATH_DEPENDENT_DOMINANCE_REVERSAL";}
 if !trans && incomparable{return "SCOPE_INDEXED_TRANSITIVITY_FAILURE";}
 if acyclic && !preorder{return "ACYCLIC_NOT_GLOBAL_PREORDER";}
 if cycle && !break_warrant{return "CYCLE_BREAKING_WARRANT_MISSING";}
 if totalize && !completion{return "ILLEGITIMATE_TOTALIZATION";}
 if incomparable{return "INCOMPARABILITY_PRESERVED";}
 "MAXIMAL_WARRANTED_COMPARISON_STRUCTURE"
}
fn main(){
 let p=env::args().nth(1).unwrap(); let t=fs::read_to_string(p).unwrap();
 let mut n=0; let mut ok=0;
 for(i,l) in t.lines().enumerate(){
  if i==0||l.trim().is_empty(){continue}
  let c:Vec<&str>=l.split('\t').collect(); assert_eq!(c.len(),16);
  let g=classify(&c); n+=1;
  if g==c[15]{ok+=1}else{eprintln!("{} expected={} got={}",c[0],c[15],g);}
 }
 println!("MQR484_CASES={n}");
 println!("MQR484_PASS={ok}");
 println!("MQR484_PAIRWISE_NE_GLOBAL=REJECT");
 println!("MQR484_TOTALIZATION_NE_COMPLETION=REJECT");
 println!("MQR484_COURT={}",if n==ok{"PASS"}else{"FAIL"});
 if n!=ok{std::process::exit(1);}
}
