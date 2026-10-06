use std::{env,fs};
fn b(s:&str)->bool{s=="1"}
fn classify(c:&[&str])->&'static str{
 let prospective=b(c[2]); let warrant=b(c[3]); let finite=b(c[4]); let competing=b(c[5]);
 let escape=b(c[6]); let institution=b(c[7]); let post=b(c[8]); let sm=c[9];
 if escape {return "OFF_TARGET_ESCAPE";}
 if sm=="split"{return "SPLIT_REQUIRED";}
 if sm=="merge"{return "MERGE_REQUIRED";}
 if post || !prospective {return "PROVISIONAL_TARGET";}
 if institution && !warrant {return "UNWARRANTED_TARGET";}
 if finite && warrant {return "FINITE_CONTRACT_CLOSED";}
 if competing && warrant {return "COMPETING_CONSTITUTIONS";}
 if warrant {return "LOCALLY_WARRANTED_TARGET";}
 "PROVISIONAL_TARGET"
}
fn main(){
 let p=env::args().nth(1).unwrap(); let t=fs::read_to_string(p).unwrap();
 let mut n=0;let mut ok=0;
 for (i,l) in t.lines().enumerate(){if i==0||l.trim().is_empty(){continue;} let c:Vec<&str>=l.split('\t').collect();
 assert_eq!(c.len(),11); let got=classify(&c); n+=1; if got==c[10]{ok+=1}else{eprintln!("{} {} {}",c[0],c[10],got);}
 }
 println!("MQR479_CASES={n}");println!("MQR479_PASS={ok}");
 println!("MQR479_TARGET_SUCCESS_CERTIFIES_CONSTITUTION=REJECT");
 println!("MQR479_LARGER_TARGET_IMPLIES_BETTER_WARRANT=REJECT");
 println!("MQR479_FINER_PARTITION_IMPLIES_STRONGER_WARRANT=REJECT");
 println!("MQR479_COURT={}",if n==ok{"PASS"}else{"FAIL"});
 if n!=ok{std::process::exit(1);}
}