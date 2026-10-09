//! P6: independent Rust verification of three EDI original CSV tables vs
//! the pinned palmerpenguins secondary CSV. These are already-published
//! observations. Matching rows is provenance, not measurement validation.
use std::{collections::{BTreeMap,BTreeSet},env,fs,io::BufRead,path::Path};

const FIELDS: usize = 17;
fn cells(line:&str)->Vec<String>{
    let mut out=Vec::new(); let mut word=String::new(); let mut quoted=false;
    let mut chars=line.trim_end_matches('\r').chars().peekable();
    while let Some(c)=chars.next() {
        match c {
            '"' if quoted && chars.peek()==Some(&'"') => {word.push('"');chars.next();},
            '"' => quoted=!quoted,
            ',' if !quoted => out.push(std::mem::take(&mut word)),
            _ => word.push(c)
        }
    }
    assert!(!quoted,"Source CSV spans lines, parser contract must be revised");
    out.push(word);out
}
fn read(path:&Path)->(Vec<String>,Vec<Vec<String>>){
    let text=fs::read_to_string(path).expect("Missing original input");
    let mut lines=text.lines().filter(|s|!s.is_empty());
    let h=cells(lines.next().expect("CSV lacks header"));
    assert_eq!(h.len(),FIELDS);
    let rows=lines.map(cells).collect::<Vec<_>>();
    assert!(rows.iter().all(|r|r.len()==FIELDS),"Unexpected CSV shape");
    (h,rows)
}
fn comparable(a:&str,b:&str,is_numeric:bool)->bool{
    let x=a.trim();let y=b.trim();
    let null=|t:&str|t.is_empty()||t=="NA"||t=="N/A"||t=="NULL"||t==".";
    if null(x)||null(y){return null(x)&&null(y);}
    if is_numeric {
        match (x.parse::<f64>(),y.parse::<f64>()){
            (Ok(p),Ok(q)) if p.is_finite()&&q.is_finite()=> {
                return (p-q).abs()<=1.0e-12
            }
            _=>{}
        }
    }
    x==y
}
fn main(){
    let input=env::args().skip(1).collect::<Vec<_>>();
    assert_eq!(input.len(),4,"Usage: p6_edi_court table_219.csv table_220.csv table_221.csv published.csv");
    let (cols_219,a)=read(Path::new(&input[0]));
    let (cols_220,b)=read(Path::new(&input[1]));
    let (cols_221,c)=read(Path::new(&input[2]));
    let (cols_combined,d)=read(Path::new(&input[3]));
    assert_eq!(cols_219,cols_220);assert_eq!(cols_219,cols_221);
    assert_eq!(cols_219,cols_combined);
    assert_eq!((a.len(),b.len(),c.len(),d.len()),(152,124,68,344));
    let joined=[a,b,c].concat();
    let study=cols_219.iter().position(|s|s=="studyName").unwrap();
    let bird=cols_219.iter().position(|s|s=="Individual ID").unwrap();
    let sample=cols_219.iter().position(|s|s=="Sample Number").unwrap();
    let species=cols_219.iter().position(|s|s=="Species").unwrap();
    let numeric=["Sample Number","Culmen Length (mm)","Culmen Depth (mm)",
                 "Flipper Length (mm)","Body Mass (g)","Delta 15 N (o/oo)","Delta 13 C (o/oo)"];
    let numeric_ix=cols_219.iter().map(|s|numeric.contains(&s.as_str())).collect::<Vec<_>>();
    let mut ids=BTreeMap::<(String,String),usize>::new();
    let mut weak=BTreeSet::<(String,String)>::new();
    let mut strong=BTreeSet::<(String,String,String)>::new();
    for (i,row) in joined.iter().enumerate(){
        let key=(row[study].clone(),row[bird].clone());
        assert!(ids.insert(key,i).is_none(),"Duplicate source bird/year key");
        weak.insert((row[study].clone(),row[sample].clone()));
        strong.insert((row[species].clone(),row[study].clone(),row[sample].clone()));
    }
    assert_eq!((ids.len(),weak.len(),strong.len()),(344,220,344));
    let mut match_keys=BTreeSet::new();
    let mut raw_diff=0_usize;let mut semantic_diff=0_usize;let mut fixed_digits=0_usize;
    for row in &d{
        let key=(row[study].clone(),row[bird].clone());
        assert!(match_keys.insert(key.clone()),"Duplicate combined key");
        let old=&joined[*ids.get(&key).expect("Combined missing from original")];
        for j in 0..FIELDS{
            if old[j]!=row[j]{
                raw_diff+=1;
                // Expose when the original numeric printing adds low-order
                // decimal digits, without granting exact-decimal equality.
                if numeric_ix[j] && (old[j].contains('.') || row[j].contains('.')) {
                    if old[j].trim()!=row[j].trim() &&
                       old[j].trim_end_matches('0')!=row[j].trim_end_matches('0') {
                        let x=old[j].trim().parse::<f64>();let y=row[j].trim().parse::<f64>();
                        if let (Ok(x),Ok(y))=(x,y){
                            if x.is_finite() && y.is_finite() && x!=y &&
                               (x-y).abs()<=1.0e-12 { fixed_digits+=1; }
                        }
                    }
                }
            }
            if !comparable(&old[j],&row[j],numeric_ix[j]){semantic_diff+=1;}
        }
    }
    assert_eq!((match_keys.len(),raw_diff,semantic_diff),(344,488,0));
    // P6 primary Python receipt separately specifies 5 original-decimal
    // roundback matches, because f64 alone does not preserve source decimal scale.
    println!("MQR4100_P6_RUST_ORIGINAL_EDI_PASS rows=344 columns=17 raw_text_diffs=488 normalized_substantive=0 weak_key_collisions=124 numeric_small_diffs_binary={fixed_digits}");
}
#[cfg(test)]mod tests{
    use super::*;
    #[test]fn csv_escaped_commas(){assert_eq!(cells("a,\"Adult, 1 Egg Stage\",c"),vec!["a","Adult, 1 Egg Stage","c"]);}
    #[test]fn numeric_vs_null(){assert!(comparable("","NA",false));assert!(comparable("8.39459","8.3945900000000009",true));assert!(!comparable("8.39459","8.39460",true));}
}
