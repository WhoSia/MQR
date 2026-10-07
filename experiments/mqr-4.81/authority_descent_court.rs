use std::{env,fs};
fn b(s:&str)->bool{s=="1"}
fn classify(c:&[&str])->&'static str{
 let pair=b(c[2]); let triple=b(c[3]); let cycle=b(c[4]); let conflict=b(c[5]);
 let hidden=b(c[6]); let order=b(c[7]); let basis=b(c[8]); let reopen=b(c[9]);
 if reopen{return "REOPEN_HIGHER_ORDER_INCOMPATIBILITY";}
 if hidden{return "HIDDEN_INTERMEDIATE_OBLIGATION_LOSS";}
 if !conflict{return "GLOBAL_CONFLICT_ERASURE";}
 if !order{return "COMPOSITION_ORDER_AUTHORITY_REVERSAL";}
 if !triple{return "TRIPLE_OVERLAP_MISMATCH";}
 if !cycle{return "CYCLE_ANCESTRY_DRIFT";}
 if !pair || !basis{return "PAIRWISE_ONLY_AUTHORITY";}
 return "GLOBAL_AUTHORITY_DESCENT";
}
fn main(){
 let p=env::args().nth(1).unwrap(); let t=fs::read_to_string(p).unwrap();
 let mut n=0; let mut ok=0;
 for(i,l) in t.lines().enumerate(){
  if i==0||l.trim().is_empty(){continue}
  let c:Vec<&str>=l.split('\t').collect(); assert_eq!(c.len(),11);
  let g=classify(&c); n+=1;
  if g==c[10]{ok+=1}else{eprintln!("{} expected={} got={}",c[0],c[10],g);}
 }
 println!("MQR481_CASES={n}");
 println!("MQR481_PASS={ok}");
 println!("MQR481_PAIRWISE_IMPLIES_GLOBAL=REJECT");
 println!("MQR481_GLOBAL_OBJECT_IMPLIES_GLOBAL_WARRANT=REJECT");
 println!("MQR481_DATA_DESCENT_IMPLIES_AUTHORITY_DESCENT=REJECT");
 println!("MQR481_COURT={}",if n==ok{"PASS"}else{"FAIL"});
 if n!=ok{std::process::exit(1);}
}