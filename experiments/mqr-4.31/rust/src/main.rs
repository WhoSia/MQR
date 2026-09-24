use std::{collections::{BTreeMap,BTreeSet},env,fs};

#[derive(Debug)]
struct Row{
    id:String,
    lineage:String,
    predicted:String,
    native:String,
    confirmatory:bool,
    source_positive:bool,
}

fn parse(path:&str)->Result<Vec<Row>,String>{
    let s=fs::read_to_string(path).map_err(|e|e.to_string())?;
    let mut it=s.lines();
    let header=it.next().ok_or("missing header")?;
    let expected="id\tlineage\tpredicted\tnative\tconfirmatory\tsource_side_positive";
    if header!=expected{return Err(format!("unexpected header: {header}"))}
    let mut rows=Vec::new();
    for (i,l) in it.enumerate(){
        if l.trim().is_empty(){continue}
        let p:Vec<&str>=l.split('\t').collect();
        if p.len()!=6{return Err(format!("line {} has {} cols",i+2,p.len()))}
        rows.push(Row{
            id:p[0].to_string(),
            lineage:p[1].to_string(),
            predicted:p[2].to_string(),
            native:p[3].to_string(),
            confirmatory:p[4]=="1",
            source_positive:p[5]=="1",
        });
    }
    Ok(rows)
}

fn main(){
    let path=env::args().nth(1).unwrap_or_else(||"experiments/mqr-4.31/fresh-adjudication.tsv".into());
    let rows=parse(&path).unwrap_or_else(|e|{eprintln!("{e}");std::process::exit(2)});
    let c:Vec<&Row>=rows.iter().filter(|r|r.confirmatory).collect();
    let exact=c.iter().filter(|r|r.predicted==r.native).count();
    let rate=exact as f64/c.len() as f64;

    let lineages:BTreeSet<_>=c.iter().map(|r|r.lineage.as_str()).collect();
    let native_states:BTreeSet<_>=c.iter().map(|r|r.native.as_str()).collect();

    let mut case_states:BTreeMap<String,BTreeSet<String>>=BTreeMap::new();
    for r in &c{
        let family=if r.id.starts_with("HWPX-R2-"){"HWPX-R2"}
                   else if r.id.starts_with("HWPX-R3-"){"HWPX-R3"}
                   else if r.id.starts_with("P30-"){"P30"}
                   else if r.id.starts_with("C3X-"){"C3X"}
                   else {"OTHER"};
        case_states.entry(family.into()).or_default().insert(r.native.clone());
    }

    let c1=native_states.contains("HOLD_UNTESTED") && native_states.contains("TRANSPORT_FAIL");
    let c2=case_states.values().any(|s|s.len()>=2);
    let c3=rate>=0.80 &&
        lineages.contains("RESEARCH_LAB") &&
        lineages.contains("ENGINEERING_DEVELOPMENT");
    let c4=c.iter().filter(|r|r.id.starts_with("HWPX-"))
        .all(|r|r.lineage=="ENGINEERING_DEVELOPMENT");
    let collapse:Vec<_>=c.iter()
        .filter(|r|r.source_positive && r.native!="TRANSPORT_PASS")
        .collect();
    let c5=collapse.len()>=2;

    println!("CONFIRMATORY_CELLS={}",c.len());
    println!("EXACT_TRANSPORT_STATE_AGREEMENT={}/{}",exact,c.len());
    println!("EXACT_TRANSPORT_STATE_RATE={:.6}",rate);
    println!("LINEAGES={}",lineages.into_iter().collect::<Vec<_>>().join(","));
    println!("NATIVE_STATES={}",native_states.into_iter().collect::<Vec<_>>().join(","));
    println!("SUCCESS_COLLAPSE_COUNTEREXAMPLES={}",collapse.len());
    for r in collapse{
        println!("SUCCESS_COLLAPSE_WITNESS={} native={}",r.id,r.native);
    }
    println!("C1_UNTESTED_VS_FAILED={}",if c1{"PASS"}else{"FAIL"});
    println!("C2_COMPONENTWISE_TRANSPORT={}",if c2{"PASS"}else{"FAIL"});
    println!("C3_CROSS_LINEAGE_CONCORDANCE={}",if c3{"PASS"}else{"FAIL"});
    println!("C4_HWPX_ENGINEERING_NONLAB={}",if c4{"PASS"}else{"FAIL"});
    println!("C5_SUCCESS_COLLAPSE_ATTACK={}",if c5{"PASS"}else{"FAIL"});

    let all=c1&&c2&&c3&&c4&&c5;
    println!("MQR431_FRESH_CONFIRMATION={}",if all{"PASS"}else{"FAIL"});
    println!("LEGACY_T={}",if all{"DEPRECATE"}else{"HOLD"});
    println!("REAL_LANGUAGE_TRANSPORT={}",if all{"TYPED_RELATION_MAP"}else{"PROVISIONAL"});
    if !all{std::process::exit(1)}
}
