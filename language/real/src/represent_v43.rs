//! REALREPRESENT 0.43-CANDIDATE.
//! Typed finite measurement-representation changes and target sufficiency.
//! Separates a commutative numeric transform, observation-partition fidelity,
//! physical quantity declaration, operation ancestry and external world warrant.
//! No existing Real Lang compiler/promotion surface is modified.
#![forbid(unsafe_code)]
use std::{collections::{BTreeMap,BTreeSet},env,fs};

#[derive(Clone,Debug)]
enum Transform { Affine(i128,i128,i128), FloorDiv(i128), Table(BTreeMap<String,String>) }
#[derive(Clone,Debug)]
struct History { name:String, fields:BTreeMap<String,String> }
#[derive(Clone,Debug)]
struct Court {
    id:String,basis:String,source_sha:Option<String>,target:String,
    from:String,to:String,
    source_quantity:String,destination_quantity:String,
    source_unit:String,destination_unit:String,
    source_operation:String,destination_operation:String,
    transformation:Transform,histories:Vec<History>,
}
fn atom(s:&str)->bool{!s.is_empty()&&s.len()<=90&&s.bytes().all(|c|
    c.is_ascii_alphanumeric()||c==b'_'||c==b'-'||c==b'.')}
fn one(map:&mut BTreeMap<String,String>,key:&str,v:&str)->Result<(),String>{
    if !atom(v){return Err(format!("invalid {key}"));}
    if map.insert(key.into(),v.into()).is_some(){return Err(format!("duplicate {key}"));}
    Ok(())
}
fn parse(input:&str)->Result<Court,String>{
 let mut lines=input.lines().map(str::trim).filter(|x|!x.is_empty()&&!x.starts_with('#'));
 if lines.next()!=Some("REALREPRESENT 0.43-CANDIDATE"){return Err("expected REALREPRESENT 0.43-CANDIDATE".into());}
 let mut props=BTreeMap::<String,String>::new();let mut worlds=Vec::new();let mut names=BTreeSet::new();
 let mut maps=BTreeMap::new();let mut tr=None;let mut ended=false;
 for line in lines.by_ref(){
  if line=="END"{ended=true;break;}
  let tokens:Vec<_>=line.split_whitespace().collect();
  match tokens.as_slice(){
    [key,value] if ["id","basis","source_sha256","target","source","destination",
     "quantity_source","quantity_destination","unit_source","unit_destination",
     "operation_source","operation_destination"].contains(key)=>{
       if *key=="source_sha256" {
         if value.len()!=64||!value.bytes().all(|x|x.is_ascii_hexdigit()){
            return Err("invalid SHA256".into());
         }
         if props.insert((*key).into(),(*value).into()).is_some(){
            return Err("duplicate source hash".into());
         }
       } else { one(&mut props,key,value)?; }
    }
    ["transform","AFFINE",n,d,b]=>{
       if tr.is_some(){return Err("duplicate transform".into());}
       let n=n.parse::<i128>().map_err(|_|"bad affine numerator")?;
       let d=d.parse::<i128>().map_err(|_|"bad affine denominator")?;
       let b=b.parse::<i128>().map_err(|_|"bad affine intercept")?;
       if d<=0||n<=0{return Err("affine needs strictly positive fraction".into());}
       tr=Some(Transform::Affine(n,d,b));
    }
    ["transform","FLOOR_DIV",n]=>{
       if tr.is_some(){return Err("duplicate transform".into());}
       let n=n.parse::<i128>().map_err(|_|"bad floor divisor")?;
       if n<=0{return Err("nonpositive floor divisor".into());}
       tr=Some(Transform::FloorDiv(n));
    }
    ["transform","TABLE"]=>{
       if tr.is_some(){return Err("duplicate transform".into());}
       tr=Some(Transform::Table(BTreeMap::new()));
    }
    ["map",src,dst] if atom(src)&&atom(dst)=>{
       if maps.insert((*src).to_string(),(*dst).to_string()).is_some(){
          return Err("duplicate source mapping".into());
       }
    }
    ["world",name,fields @ ..] if atom(name)&&fields.len()>=3=>{
       if !names.insert((*name).to_string()){return Err("duplicate world name".into());}
       let mut kv=BTreeMap::new();
       for pair in fields{
           let (key,value)=pair.split_once('=').ok_or("world field requires k=v")?;
           if !atom(key)||!atom(value)||kv.insert(key.into(),value.into()).is_some(){
               return Err("bad or duplicate world field".into());
           }
       }
       worlds.push(History{name:(*name).into(),fields:kv});
       if worlds.len()>64{return Err("max 64 finite histories".into());}
    }
    _=>return Err(format!("unknown/malformed statement: {line}")),
  }
 }
 if !ended||lines.next().is_some(){return Err("exactly one END and no trailing commands".into());}
 let need=["id","basis","target","source","destination","quantity_source",
           "quantity_destination","unit_source","unit_destination",
           "operation_source","operation_destination"];
 if need.iter().any(|n|!props.contains_key(*n)){return Err("missing mandatory field".into());}
 let basis=props["basis"].clone();
 if !["FINITE_COUNTERMODEL","SOURCE_REPORTED"].contains(&basis.as_str()){
     return Err("invalid basis".into());
 }
 let sha=props.remove("source_sha256");
 if (basis=="FINITE_COUNTERMODEL"&&sha.is_some())||
     (basis=="SOURCE_REPORTED"&&sha.is_none()){
     return Err("source authority boundary: source-report requires SHA; countermodel forbids it".into());
 }
 let from=props["source"].clone();let to=props["destination"].clone();let target=props["target"].clone();
 if from==to||from==target||to==target||worlds.len()<2{
     return Err("three distinct source/destination/target fields and >=2 worlds required".into());
 }
 let schema:BTreeSet<_>=worlds[0].fields.keys().cloned().collect();
 if [from.as_str(),to.as_str(),target.as_str()].iter().any(|x|!schema.contains(*x))||
    worlds.iter().any(|w|w.fields.keys().cloned().collect::<BTreeSet<_>>()!=schema){
    return Err("all worlds must have complete identical schema".into());
 }
 let transformation=tr.ok_or("missing transform")?;
 let transformation=match transformation{
  Transform::Table(_)=>{
      if maps.is_empty(){return Err("TABLE needs map entries".into());}
      let observed:BTreeSet<String>=worlds.iter().map(|w|w.fields[&from].clone()).collect();
      if observed!=maps.keys().cloned().collect(){return Err("table map must exactly cover observed source values".into());}
      Transform::Table(maps)
  }
  x=>{
      if !maps.is_empty(){return Err("map declarations allowed only for TABLE".into());}
      x
  }
 };
 Ok(Court{
  id:props["id"].clone(),basis,source_sha:sha,target,from,to,
  source_quantity:props["quantity_source"].clone(),
  destination_quantity:props["quantity_destination"].clone(),
  source_unit:props["unit_source"].clone(),
  destination_unit:props["unit_destination"].clone(),
  source_operation:props["operation_source"].clone(),
  destination_operation:props["operation_destination"].clone(),
  transformation,histories:worlds,
 })
}
fn declared_type_valid(c:&Court)->bool{
 if c.source_quantity!=c.destination_quantity{return false;}
 match &c.transformation{
  Transform::Table(_)=>c.source_unit=="SYMBOL"&&c.destination_unit=="SYMBOL",
  Transform::FloorDiv(_)=>c.source_unit==c.destination_unit,
  Transform::Affine(n,d,b)=>{
    let units=(c.source_quantity.as_str(),c.source_unit.as_str(),c.destination_unit.as_str());
    let expected=match units{
     ("DOSE","Gy","mGy")=>Some((1000,1,0)),
     ("DOSE","mGy","Gy")=>Some((1,1000,0)),
     ("TIME","s","ms")=>Some((1000,1,0)),
     ("TIME","ms","s")=>Some((1,1000,0)),
     ("LENGTH","m","cm")=>Some((100,1,0)),
     ("LENGTH","cm","m")=>Some((1,100,0)),
     ("LENGTH","m","mm")=>Some((1000,1,0)),
     ("LENGTH","mm","m")=>Some((1,1000,0)),
     _=>None
    };
    if c.source_unit==c.destination_unit {
       *n==1 && *d==1 && *b==0
    }else {
       expected.is_some_and(|(x,y,z)|*n*y==x**d&&*b==z)
    }
  }
 }
}
fn translation_matches(c:&Court)->bool{
 c.histories.iter().all(|w|{
   let a=&w.fields[&c.from];let b=&w.fields[&c.to];
   match &c.transformation{
    Transform::Table(table)=>table.get(a)==Some(b),
    Transform::Affine(n,d,offset)=>{
      let (Ok(src),Ok(dst))=(a.parse::<i128>(),b.parse::<i128>()) else {return false;};
      src.checked_mul(*n).and_then(|v|offset.checked_mul(*d)
         .and_then(|bb|v.checked_add(bb))).zip(dst.checked_mul(*d))
         .is_some_and(|(lhs,rhs)|lhs==rhs)
    }
    Transform::FloorDiv(div)=>{
      let (Ok(src),Ok(dst))=(a.parse::<i128>(),b.parse::<i128>()) else {return false;};
      src.div_euclid(*div)==dst
    }
   }
 })
}
fn kernel(c:&Court,field:&str)->BTreeSet<(usize,usize)>{
 let mut pairs=BTreeSet::new();
 for i in 0..c.histories.len(){for j in i+1..c.histories.len(){
  if c.histories[i].fields[field]==c.histories[j].fields[field]{pairs.insert((i,j));}
 }}pairs
}
fn factorizes(c:&Court,field:&str)->bool{
 let k=kernel(c,field);
 !k.iter().any(|(i,j)|c.histories[*i].fields[&c.target]!=c.histories[*j].fields[&c.target])
}
fn render(c:&Court)->String{
 let typed=declared_type_valid(c);
 let transform=translation_matches(c);
 let a=kernel(c,&c.from);let b=kernel(c,&c.to);
 let comparison=if a==b{"EQUIVALENT"}
   else if a.is_subset(&b){"DESTINATION_COARSER"}
   else if b.is_subset(&a){"DESTINATION_FINER"}
   else {"INCOMPARABLE"};
 let fa=factorizes(c,&c.from);let fb=factorizes(c,&c.to);
 let op=c.source_operation==c.destination_operation;
 let structure=if !typed{"FAIL_QUANTITY_OR_UNIT"}
  else if !transform{"FAIL_NONCOMMUTING_TRANSFORM"}
  else if !op{"HOLD_DIFFERENT_OPERATION"}
  else if fa&&!fb{"FAIL_TARGET_WARRANT_LOST"}
  else if !fa{"HOLD_SOURCE_TARGET_UNIDENTIFIED"}
  else {"PASS_CONDITIONAL_FINITE_MODEL"};
 format!("representation.version=0.43-CANDIDATE\n\
 representation.id={}\nrepresentation.basis={}\nrepresentation.history_count={}\n\
 representation.source_quantity={}\nrepresentation.destination_quantity={}\n\
 representation.type_contract={}\nrepresentation.numeric_or_label_transform={}\n\
 representation.operation_ancestry={}\nrepresentation.observation_partition={}\n\
 representation.source_target_factors={}\nrepresentation.destination_target_factors={}\n\
 representation.conditional_transport={}\n\
 representation.world_authority=HOLD\nrepresentation.operation_empirical_grounding=UNVERIFIED\n\
 representation.historical_ancestry_verification=NOT_INFERRED\n\
 representation.source_truth_from_sha256=NOT_INFERRED\n\
 representation.real_language_promotion=UNPROMOTED_CANDIDATE\n",
 c.id,c.basis,c.histories.len(),c.source_quantity,c.destination_quantity,
 if typed{"PASS_DECLARED_TYPES"}else{"FAIL"},
 if transform{"PASS_FINITE_VALUES"}else{"FAIL"},
 if op{"SAME_LABEL_ONLY_UNVERIFIED"}else{"DIFFERENT_OPERATION_REQUIRES_TRANSFER"},
 comparison,if fa{"PASS_FINITE"}else{"FAIL_TWIN_HISTORIES"},
 if fb{"PASS_FINITE"}else{"FAIL_TWIN_HISTORIES"},structure)
}
fn main(){
 let path=env::args().nth(1).unwrap_or_else(||{
   eprintln!("usage: real-v43-represent <source.real>");std::process::exit(2);
 });
 let text=fs::read_to_string(path).unwrap_or_else(|e|{
   eprintln!("READ_ERROR: {e}");std::process::exit(2);
 });
 match parse(&text){Ok(c)=>print!("{}",render(&c)),Err(e)=>{
   eprintln!("REJECTED: {e}");std::process::exit(2);
 }}
}
#[cfg(test)]
mod tests {
 use super::*;
 const OK:&str="REALREPRESENT 0.43-CANDIDATE\nid dose\nbasis FINITE_COUNTERMODEL\ntarget underlying\nsource old\ndestination new\nquantity_source DOSE\nquantity_destination DOSE\nunit_source Gy\nunit_destination mGy\noperation_source RISØ\noperation_destination RISØ\ntransform AFFINE 1000 1 0\nworld a old=1 new=1000 underlying=A\nworld b old=2 new=2000 underlying=B\nworld c old=3 new=3000 underlying=C\nEND\n";
 #[test]fn exact_unit_bijection_has_same_fibers(){let c=parse(OK).unwrap();let r=render(&c);assert!(r.contains("observation_partition=EQUIVALENT"));assert!(r.contains("conditional_transport=PASS_CONDITIONAL_FINITE_MODEL"));}
 #[test]fn wrongly_claimed_dose_unit_conversion_rejected_structurally(){let s=OK.replace("transform AFFINE 1000 1 0","transform AFFINE 1 1 0").replace("new=1000","new=1").replace("new=2000","new=2").replace("new=3000","new=3");let c=parse(&s).unwrap();assert!(render(&c).contains("conditional_transport=FAIL_QUANTITY_OR_UNIT"));}
 #[test]fn identical_numbers_different_physical_quantities_are_not_equivalent(){let s=OK.replace("quantity_destination DOSE","quantity_destination TEMPERATURE");let c=parse(&s).unwrap();assert!(render(&c).contains("conditional_transport=FAIL_QUANTITY_OR_UNIT"));}
 #[test]fn noncommuting_conversion_cannot_launder_warrant(){let s=OK.replace("new=2000","new=2100");let c=parse(&s).unwrap();assert!(render(&c).contains("conditional_transport=FAIL_NONCOMMUTING_TRANSFORM"));}
 #[test]fn changed_operation_holds_even_when_values_commute(){let s=OK.replace("operation_destination RISØ","operation_destination DIFFERENT_PIPELINE");let c=parse(&s).unwrap();assert!(render(&c).contains("conditional_transport=HOLD_DIFFERENT_OPERATION"));}
 fn lossy(q2:&str)->String{format!("REALREPRESENT 0.43-CANDIDATE\nid loss\nbasis FINITE_COUNTERMODEL\ntarget q\nsource a\ndestination b\nquantity_source COUNT\nquantity_destination COUNT\nunit_source COUNT\nunit_destination COUNT\noperation_source PROTOCOL\noperation_destination PROTOCOL\ntransform FLOOR_DIV 10\nworld w1 a=10 b=1 q=X\nworld w2 a=11 b=1 q={q2}\nworld w3 a=20 b=2 q=Z\nEND\n")}
 #[test]fn valid_processing_can_destroy_target_identification(){let c=parse(&lossy("Y")).unwrap();let r=render(&c);assert!(r.contains("observation_partition=DESTINATION_COARSER"));assert!(r.contains("source_target_factors=PASS_FINITE"));assert!(r.contains("destination_target_factors=FAIL_TWIN_HISTORIES"));assert!(r.contains("conditional_transport=FAIL_TARGET_WARRANT_LOST"));}
 #[test]fn lossy_reduction_can_preserve_specific_target(){let c=parse(&lossy("X")).unwrap();let r=render(&c);assert!(r.contains("observation_partition=DESTINATION_COARSER"));assert!(r.contains("conditional_transport=PASS_CONDITIONAL_FINITE_MODEL"));}
 #[test]fn table_can_permute_symbolic_encoding(){let s="REALREPRESENT 0.43-CANDIDATE\nid rename\nbasis FINITE_COUNTERMODEL\ntarget q\nsource a\ndestination b\nquantity_source HISTORY_TAG\nquantity_destination HISTORY_TAG\nunit_source SYMBOL\nunit_destination SYMBOL\noperation_source SAME\noperation_destination SAME\ntransform TABLE\nmap X V\nmap Y U\nworld h1 a=X b=V q=P\nworld h2 a=Y b=U q=Q\nEND\n";let c=parse(s).unwrap();assert!(render(&c).contains("observation_partition=EQUIVALENT"));}
 #[test]fn noninjective_symbolic_encoding_creates_target_loss(){let s="REALREPRESENT 0.43-CANDIDATE\nid collapse\nbasis FINITE_COUNTERMODEL\ntarget q\nsource a\ndestination b\nquantity_source TAG\nquantity_destination TAG\nunit_source SYMBOL\nunit_destination SYMBOL\noperation_source CODE\noperation_destination CODE\ntransform TABLE\nmap X Z\nmap Y Z\nworld h1 a=X b=Z q=P\nworld h2 a=Y b=Z q=Q\nEND\n";let c=parse(s).unwrap();assert!(render(&c).contains("conditional_transport=FAIL_TARGET_WARRANT_LOST"));}
 #[test]fn self_certifying_empirical_claim_fails(){assert!(parse(&OK.replace("basis FINITE_COUNTERMODEL","basis SOURCE_REPORTED")).is_err());}
 #[test]fn extra_commands_or_different_schemas_fail(){assert!(parse(&(OK.to_string()+"world fake old=4 new=4000 underlying=D\n")).is_err());assert!(parse(&OK.replace("underlying=C","another=C")).is_err());}
 #[test]fn duplicate_world_field_rejected(){assert!(parse(&OK.replace("old=1 new=1000","old=1 old=2 new=1000")).is_err());}
 #[test]fn cannot_pretend_unknown_conversion_physically_verified(){let s=OK.replace("unit_destination mGy","unit_destination C");let c=parse(&s).unwrap();assert!(render(&c).contains("type_contract=FAIL"));}
 #[test]fn equality_requires_same_quantity_not_same_operation_label(){let s=OK.replace("quantity_source DOSE","quantity_source TIME").replace("quantity_destination DOSE","quantity_destination TIME");let c=parse(&s).unwrap();assert!(render(&c).contains("type_contract=FAIL"));}
}
