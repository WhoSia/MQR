use std::{env,fs};
fn main(){
 let t=fs::read_to_string(env::args().nth(1).unwrap()).unwrap();
 let mut n=0usize; let mut ok=0usize;
 for (i,l) in t.lines().enumerate(){
  if i==0||l.trim().is_empty(){continue}
  let c:Vec<&str>=l.split('\t').collect();
  let e=match c[0]{
   "N1"|"M1"=>"FINITE_SCOPE_CLOSED",
   "N2"|"M2"=>"UNWARRANTED_TRUNCATION",
   "N3"=>"COMPUTE_STOP_ONLY",
   "N4"|"M4"=>"BASIS_AUTHORITY_MISSING",
   "N5"|"M3"|"M5"=>"RESIDUAL_HIGHER_ORDER_DEBT",
   "N6"|"M6"=>"OPEN_WORLD_COMPLETENESS_UNEARNED",
   "N7"|"M7"=>"HIGHER_ORDER_ESCAPE",
   "N8"|"M8"=>"REOPEN_BEYOND_TRUNCATION",
   _=>"UNKNOWN"
  };
  n+=1;
  if c.len()==12 && e==c[11]{ok+=1}else{eprintln!("{}",c[0]);}
 }
 println!("MQR482_ORACLE_CASES={n}");
 println!("MQR482_ORACLE_PASS={ok}");
 if n!=ok{std::process::exit(1);}
}
