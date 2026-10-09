//! MQR-4.100 P3: independently parse and evaluate exact row-matched penguin records.
//! Retrospective exploration; no estimator of ecological abundance/independent sensor accuracy.
use std::{collections::{BTreeMap, BTreeSet, HashSet}, env, fs};
fn cells(line:&str)->Vec<String>{
    let mut out=Vec::new();let mut buf=String::new();let mut quoted=false;
    let mut cs=line.trim_end_matches('\r').chars().peekable();
    while let Some(c)=cs.next(){
        match c {
            '"' if quoted && cs.peek()==Some(&'"')=>{buf.push('"');cs.next();},
            '"'=>quoted=!quoted,
            ',' if !quoted=>{out.push(std::mem::take(&mut buf));},
            _=>buf.push(c),
        }
    }
    assert!(!quoted,"Unexpected multi-line quote (source contract)");
    out.push(buf);out
}
#[derive(Clone)] struct Bird {
    year:String, specimen_id:String, sample:String,
    species:String, x:[f64;2]
}
fn col<'a>(r:&'a[String],h:&[String],s:&str)->&'a str {
    &r[h.iter().position(|v|v==s).expect("Missing column")]
}
fn read(path:&str)->(Vec<Bird>,usize,usize,usize){
    let input=fs::read_to_string(path).expect("Missing externally pinned original");
    let mut lines=input.lines();let header=cells(lines.next().unwrap());
    assert_eq!(header.len(),17);
    let mut birds=Vec::new();let mut total=0;let mut allkeys=HashSet::new();
    let mut weakkeys=HashSet::new();let mut collisions=0;
    for line in lines {
        if line.trim().is_empty(){continue}
        let fields=cells(line);
        assert_eq!(fields.len(),17,"Invalid CSV quoting");
        total+=1;
        let year=col(&fields,&header,"studyName").to_string();
        let specimen_id=col(&fields,&header,"Individual ID").to_string();
        let sample=col(&fields,&header,"Sample Number").to_string();
        assert!(allkeys.insert((year.clone(),specimen_id.clone())),
            "Year + individual ID not unique in original source");
        if !weakkeys.insert((year.clone(),sample.clone())){collisions+=1;}
        let a=col(&fields,&header,"Culmen Length (mm)");
        let b=col(&fields,&header,"Flipper Length (mm)");
        if a=="NA"||b=="NA"||a.is_empty()||b.is_empty(){continue;}
        birds.push(Bird{year,specimen_id,sample,species:col(&fields,&header,"Species").to_string(),
                        x:[a.parse().unwrap(),b.parse().unwrap()]});
    }
    (birds,total,collisions,allkeys.len())
}
fn mean(v:&[f64])->f64 {v.iter().sum::<f64>()/v.len() as f64}
fn main(){
    let path=env::args().nth(1).expect("Usage: cargo run --bin p3_paired_original -- source.csv");
    let (birds,n,weakcollisions,unique)=read(&path);
    assert_eq!((n,birds.len(),weakcollisions,unique),(344,342,124,344));
    let training=birds.iter().filter(|x|x.year!="PAL0910").collect::<Vec<_>>();
    let testing=birds.iter().filter(|x|x.year=="PAL0910").collect::<Vec<_>>();
    assert_eq!((training.len(),testing.len()),(223,119));
    let names=training.iter().map(|r|r.species.clone()).collect::<BTreeSet<_>>();
    assert_eq!(names.len(),3);
    let mut scales=[0.0;2];
    for d in 0..2{
        let values=training.iter().map(|b|b.x[d]).collect::<Vec<_>>();
        let m=mean(&values);
        scales[d]=(values.iter().map(|x|(x-m)*(x-m)).sum::<f64>()/values.len() as f64).sqrt();
        assert!(scales[d]>0.0);
    }
    let mut centroids=BTreeMap::new();
    for label in &names {
        let subset=training.iter().filter(|r|&r.species==label).collect::<Vec<_>>();
        centroids.insert(label.clone(),[
            subset.iter().map(|r|r.x[0]).sum::<f64>()/subset.len() as f64,
            subset.iter().map(|r|r.x[1]).sum::<f64>()/subset.len() as f64
        ]);
    }
    let predict=|b:&Bird,use_flipper:bool|->String{
        let mut ranked=centroids.iter().map(|(name,m)|{
            let mut d=((b.x[0]-m[0])/scales[0]).powi(2);
            if use_flipper {d+=((b.x[1]-m[1])/scales[1]).powi(2);}
            (name.clone(),d)
        }).collect::<Vec<_>>();
        ranked.sort_by(|a,b|a.1.total_cmp(&b.1).then_with(||a.0.cmp(&b.0)));
        ranked[0].0.clone()
    };
    let ids=training.iter().map(|r|r.specimen_id.as_str()).collect::<HashSet<_>>();
    let mut bill=0;let mut paired=0;let mut gains=0;let mut losses=0;
    let mut repeated=0;let mut new_id_n=0;let mut new_id_bill=0;let mut new_id_pair=0;
    for b in &testing{
        let old=predict(b,false)==b.species;
        let joint=predict(b,true)==b.species;
        if old {bill+=1;}
        if joint {paired+=1;}
        if !old&&joint {gains+=1;}
        if old&&!joint {losses+=1;}
        if ids.contains(b.specimen_id.as_str()){repeated+=1;}
        else{
            new_id_n+=1;
            if old{new_id_bill+=1;}
            if joint{new_id_pair+=1;}
        }
    }
    assert_eq!((bill,paired,gains,losses,repeated,new_id_n,new_id_bill,new_id_pair),
               (83,113,32,2,75,44,36,41));
    println!("P3_RUST_PAIRED_ORIGINAL_AUDIT=PASS all=344 paired=342 train=223 heldout=119 weak_sample_key_collisions=124");
    println!("P3_RUST_RETROSPECTIVE_YEAR_HOLDOUT bill_correct={bill} paired_correct={paired} gains={gains} losses={losses}");
    println!("P3_RUST_IDENTIFIER_STRING_OVERLAP test_repeated={repeated} test_nonoverlap={new_id_n} nonoverlap_bill={new_id_bill} nonoverlap_paired={new_id_pair}");
    println!("P3_SCIENTIFIC_STATUS=PUBLIC_REUSED_ORIGINAL_NO_INDEPENDENT_SENSOR_OR_TRANSPORT");
}
#[cfg(test)] mod tests{
    use super::*;
    #[test] fn escaped_csv_stage(){assert_eq!(cells("1,\"Adult, 1 Egg Stage\",2"),vec!["1","Adult, 1 Egg Stage","2"]);}
    #[test] fn quoted_quotes(){assert_eq!(cells("a,\"x\"\"y\",b"),vec!["a","x\"y","b"]);}
}
