use std::{env, fs};

#[derive(Debug)]
struct Row {
    id:String, prospective:bool, coverage:bool, ontology_common:bool, grammar_common:bool,
    ancestry_diverse:bool, separator_found:bool, separates_live:bool,
    finite_complete:bool, postoutcome:bool, reopen:bool, split_merge:String, expected:String
}

fn b(s:&str)->bool { s=="1" }

fn classify(r:&Row)->&'static str {
    if r.reopen { return "REOPEN_GENERATOR_ANCESTRY"; }
    if r.postoutcome || !r.prospective { return "DIAGNOSTIC_FAMILY_ONLY"; }
    if r.split_merge=="split" { return "SPLIT_REQUIRED"; }
    if r.split_merge=="merge" { return "MERGE_COLLAPSE"; }
    if !r.separator_found { return "NO_SEPARATOR_AUTHORITY"; }
    if (r.ontology_common || r.grammar_common) && !r.ancestry_diverse {
        return "COMMON_MODE_GENERATOR";
    }
    if r.ancestry_diverse && r.coverage && r.separates_live {
        return "ANCESTRY_DIVERSE_LOCAL_AUTHORITY";
    }
    "FAMILY_RELATIVE_SEPARATION"
}

fn main() {
    let path=env::args().nth(1).expect("usage: court TSV");
    let txt=fs::read_to_string(path).expect("read");
    let mut total=0usize; let mut pass=0usize;
    let mut counts=std::collections::BTreeMap::<String,usize>::new();
    for (i,line) in txt.lines().enumerate() {
        if i==0 || line.trim().is_empty() { continue; }
        let c:Vec<&str>=line.split('\t').collect();
        assert_eq!(c.len(),14,"bad columns: {line}");
        let r=Row{id:c[0].into(),prospective:b(c[2]),coverage:b(c[3]),ontology_common:b(c[4]),
            grammar_common:b(c[5]),ancestry_diverse:b(c[6]),separator_found:b(c[7]),
            separates_live:b(c[8]),finite_complete:b(c[9]),postoutcome:b(c[10]),reopen:b(c[11]),
            split_merge:c[12].into(),expected:c[13].into()};
        let got=classify(&r);
        total+=1;
        *counts.entry(got.into()).or_insert(0)+=1;
        if got==r.expected {pass+=1;} else {eprintln!("{} expected={} got={}",r.id,r.expected,got);}
        if r.finite_complete && got=="ANCESTRY_DIVERSE_LOCAL_AUTHORITY" {
            println!("MQR478_RELATIVE_FINITE_GRAMMAR_TERMINATION=ALLOWED");
        }
    }
    println!("MQR478_CASES={total}");
    println!("MQR478_PASS={pass}");
    for (k,v) in counts { println!("{k}={v}"); }
    println!("MQR478_SELF_CERTIFYING_COMPLETENESS=REJECT");
    println!("MQR478_GENERATOR_PLURALITY_IMPLIES_INDEPENDENCE=REJECT");
    println!("MQR478_FAMILY_SATURATION_IMPLIES_OPEN_WORLD_NONSEPARABILITY=REJECT");
    println!("MQR478_SEPARATOR_CONSTITUTION_CIRCULARITY=REJECT");
    println!("MQR478_COURT={}", if total==pass {"PASS"} else {"FAIL"});
    if total!=pass { std::process::exit(1); }
}
