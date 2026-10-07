use std::{env,fs};
fn b(s:&str)->bool{s=="1"}
fn classify(c:&[&str])->&'static str{
 let scope=b(c[2]); let rel=b(c[3]); let basis=b(c[4]); let debt=b(c[5]);
 let compute=b(c[6]); let selfc=b(c[7]); let open=b(c[8]); let escape=b(c[9]); let reopen=b(c[10]);
 if escape && reopen{return "REOPEN_BEYOND_TRUNCATION";}
 if escape{return "HIGHER_ORDER_ESCAPE";}
 if open{return "OPEN_WORLD_COMPLETENESS_UNEARNED";}
 if compute{return "COMPUTE_STOP_ONLY";}
 if !scope || selfc{return "UNWARRANTED_TRUNCATION";}
 if !rel{return "BASIS_AUTHORITY_MISSING";}
 if !basis || !debt{return "RESIDUAL_HIGHER_ORDER_DEBT";}
 return "FINITE_SCOPE_CLOSED";
}
fn main(){
 let p=env::args().nth(1).unwrap(); let t=fs::read_to_string(p).unwrap();
 let mut n=0; let mut ok=0;
 for(i,l) in t.lines().enumerate(){
  if i==0||l.trim().is_empty(){continue}
  let c:Vec<&str>=l.split('\t').collect(); assert_eq!(c.len(),12);
  let g=classify(&c); n+=1;
  if g==c[11]{ok+=1}else{eprintln!("{} expected={} got={}",c[0],c[11],g);}
 }
 println!("MQR482_CASES={n}");
 println!("MQR482_PASS={ok}");
 println!("MQR482_FINITE_PASS_IMPLIES_OPEN_WORLD=REJECT");
 println!("MQR482_NO_OBSTRUCTION_BELOW_N_IMPLIES_NONE_ABOVE=REJECT");
 println!("MQR482_NO_FINITE_AUTHORITY_WITHOUT_GLOBAL_COMPLETENESS=REJECT");
 println!("MQR482_COURT={}",if n==ok{"PASS"}else{"FAIL"});
 if n!=ok{std::process::exit(1);}
}