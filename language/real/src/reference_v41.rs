//! REALREFERENCE 0.41-CANDIDATE: static source/assumption firewall.
//! Unpromoted companion to the Real-Language line. Not an external verifier.
//! New executable does NOT alter REALPACKET 0.2/0.3 or REALACQUIRE 0.29.
use std::{collections::BTreeMap,env,fs};

#[derive(Debug,PartialEq,Eq)]
struct Court { n:u64, m:u64, d:u64, kd:u64,kg:u64, certificate:String,selection:String,source:String }
fn parse(s:&str)->Result<Court,String>{
 let mut lines=s.lines().map(str::trim).filter(|s|!s.is_empty() && !s.starts_with('#'));
 if lines.next()!=Some("REALREFERENCE 0.41-CANDIDATE") {return Err("expected REALREFERENCE 0.41-CANDIDATE".into())}
 let mut values=BTreeMap::new();let mut ended=false;
 for line in lines {
   if line=="END" {ended=true;break}
   let tokens=line.split_whitespace().collect::<Vec<_>>();
   if tokens.len()!=2 {return Err(format!("two-field line required: {line}"))}
   let k=tokens[0];
   if !["n","paired","disagree","cap_disagree","cap_agree","certificate","selection","source_sha256"].contains(&k) {return Err(format!("unknown field {k}; no latent truth/independence/oracle controls allowed"))}
   if values.insert(k,tokens[1]).is_some() {return Err(format!("duplicate field {k}"))}
 }
 if !ended || values.len()!=8 {return Err("complete 8-field packet and END required".into())}
 let num=|k:&str|->Result<u64,String>{values.get(k).ok_or(format!("missing {k}"))?.parse().map_err(|_|format!("invalid integer {k}"))};
 let n=num("n")?;let m=num("paired")?;let d=num("disagree")?;let kd=num("cap_disagree")?;let kg=num("cap_agree")?;
 if n==0 || m>n || d>m || kd>d || kg>m-d {return Err("invalid counts or caps".into())}
 let certificate=values["certificate"].to_owned();let selection=values["selection"].to_owned();let source=values["source_sha256"].to_owned();
 if !["NONE","HYPOTHETICAL","CLAIMED_EXTERNAL"].contains(&certificate.as_str()){return Err("certificate must disclose status".into())}
 if !["STUDY_SELECTED","TARGET_ENUMERATED"].contains(&selection.as_str()) {return Err("selection must be explicit".into())}
 if source.len()!=64 || !source.bytes().all(|b| b.is_ascii_hexdigit()) {return Err("invalid source SHA256".into())}
 if certificate=="NONE" && (kd!=0 || kg!=0) {return Err("NO certificate cannot supply alleged zero-error caps".into())}
 Ok(Court{n,m,d,kd,kg,certificate,selection,source})
}
fn bounds(c:&Court)->(u64,u64){
 if c.certificate=="NONE" {(0,c.n)} else {(c.d-c.kd,c.d+c.kg+(c.n-c.m))}
}
fn render(c:&Court)->String {
 let (lo,hi)=bounds(c);
 let reason=match c.certificate.as_str(){
  "NONE"=>"NO_REFERENCE_ERROR_CERTIFICATE",
  "HYPOTHETICAL"=>"SENSITIVITY_ONLY_NOT_WORLD_CONTACT",
  "CLAIMED_EXTERNAL"=>"EXTERNAL_CLAIM_UNVERIFIED_BY_COMPILER",
  _=>unreachable!()
 };
 format!("reference.source_sha256={}\nreference.finite_bounds=[{},{}]/{}\nreference.formal_arithmetic=PASS\nreference.world_authority=HOLD:{}\nreference.selection={}\nreference.target_transport=HOLD\nreference.statistical_independence=NOT_ESTABLISHED\nreference.real_language_promotion=UNPROMOTED_CANDIDATE\n",c.source,lo,hi,c.n,reason,c.selection)
}
fn main(){
 let p=env::args().nth(1).expect("expected typed REALREFERENCE packet file");
 let s=fs::read_to_string(p).expect("packet read failed");
 match parse(&s){Ok(c)=>print!("{}",render(&c)),Err(err)=>{eprintln!("REJECTED: {err}");std::process::exit(2)}}
}
#[cfg(test)]mod tests{
 use super::*;
 const SHA:&str="d441a516cb0cfba50d6eb1d71662a1a3ff9c9e57546800e8127c59303a3ed842";
 fn packet(cert:&str,kd:u64,kg:u64)->String {format!("REALREFERENCE 0.41-CANDIDATE\nn 487\npaired 402\ndisagree 76\ncap_disagree {kd}\ncap_agree {kg}\ncertificate {cert}\nselection STUDY_SELECTED\nsource_sha256 {SHA}\nEND\n")}
 #[test]fn genuine_hold_unconditional(){let x=parse(&packet("NONE",0,0)).unwrap();assert_eq!(bounds(&x),(0,487));assert!(render(&x).contains("world_authority=HOLD"))}
 #[test]fn conditional_sharp_bounds_no_world_launder(){let x=parse(&packet("HYPOTHETICAL",7,3)).unwrap();assert_eq!(bounds(&x),(69,164));assert!(render(&x).contains("SENSITIVITY_ONLY_NOT_WORLD_CONTACT"))}
 #[test]fn claimed_external_not_self_certifying(){let x=parse(&packet("CLAIMED_EXTERNAL",7,3)).unwrap();assert_eq!(bounds(&x),(69,164));assert!(render(&x).contains("EXTERNAL_CLAIM_UNVERIFIED_BY_COMPILER"))}
 #[test]fn reject_unearned_k_and_opaque_text(){assert!(parse(&packet("NONE",7,3)).is_err());let bad=packet("NONE",0,0).replace("END","independence YES\nEND");assert!(parse(&bad).is_err())}
 #[test]fn reject_reordered_inconsistent_or_duplicate(){let a=packet("HYPOTHETICAL",77,0);assert!(parse(&a).is_err());let b=packet("HYPOTHETICAL",0,0).replace("n 487","n 487\nn 487");assert!(parse(&b).is_err())}
}
