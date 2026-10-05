use std::{env,fs,process};

#[derive(Debug)]
struct Case {
    id:String, domain:String, origin:String, route:String, corr:String,
    broken:bool, prov:bool, residual:bool, post:bool, split_merge:String, expected:String,
}
fn die(s:&str)->!{eprintln!("{s}");process::exit(2)}
fn yn(s:&str)->bool{match s{"YES"=>true,"NO"=>false,_=>die("invalid YES/NO")}}
fn classify(c:&Case)->&'static str{
    if c.post { return "NO_UPGRADE"; }
    if c.corr=="DISJOINT" { return "NO_UPGRADE"; }
    if c.split_merge=="MERGE" { return "MERGE_COLLAPSE"; }
    if c.split_merge=="SPLIT" || c.corr=="REFINE" { return "SPLIT_REQUIRED"; }
    if !c.broken {
        if matches!(c.route.as_str(),"OTHER_LAB_SAME_CALIBRATION"|"SECOND_PROVER_SAME_ENCODING") {
            return "DIAGNOSTIC_REPLICATION_ONLY";
        }
        return "NO_UPGRADE";
    }
    if !c.prov { return "NO_UPGRADE"; }
    if matches!(c.route.as_str(),"NEW_INSTRUMENT_FAMILY"|"DISTINCT_ENCODING_INDEPENDENT_DERIVATION") && !c.residual {
        return "CROSS_ROUTE_INDEPENDENCE_UPGRADE";
    }
    "LOCAL_AUTHORITY_UPGRADE"
}
fn main(){
    let p=env::args().nth(1).unwrap_or_else(||die("usage: mqr476-court <tsv>"));
    let s=fs::read_to_string(&p).unwrap_or_else(|_|die("read failed"));
    let mut lines=s.lines();
    let header=lines.next().unwrap_or("");
    if header!="case_id\tdomain\tsource_origin\ttransport_route\tchallenge_correspondence\trelevant_common_mode_broken\tindependent_cut_provenance\tresidual_common_mode\tpostoutcome_tuned\tsplit_merge_state\texpected" {
        die("bad header");
    }
    let mut n=0usize; let mut pass=0usize;
    let mut local=0; let mut cross=0; let mut diag=0; let mut split=0; let mut merge=0; let mut no=0;
    for line in lines {
        if line.trim().is_empty(){continue}
        let t:Vec<&str>=line.split('\t').collect();
        if t.len()!=11{die("bad row")}
        let c=Case{id:t[0].into(),domain:t[1].into(),origin:t[2].into(),route:t[3].into(),corr:t[4].into(),
            broken:yn(t[5]),prov:yn(t[6]),residual:yn(t[7]),post:yn(t[8]),split_merge:t[9].into(),expected:t[10].into()};
        if c.origin!="INTERNAL"{die("frozen court expects INTERNAL source origin")}
        let got=classify(&c);
        println!("{}\t{}\t{}\t{}",c.id,c.domain,c.expected,got);
        if got!=c.expected { eprintln!("mismatch {} expected={} got={}",c.id,c.expected,got); process::exit(1); }
        n+=1; pass+=1;
        match got {
            "LOCAL_AUTHORITY_UPGRADE"=>local+=1,
            "CROSS_ROUTE_INDEPENDENCE_UPGRADE"=>cross+=1,
            "DIAGNOSTIC_REPLICATION_ONLY"=>diag+=1,
            "SPLIT_REQUIRED"=>split+=1,
            "MERGE_COLLAPSE"=>merge+=1,
            "NO_UPGRADE"=>no+=1,
            _=>{}
        }
    }
    println!("MQR476_CASES={n}");
    println!("MQR476_PASS={pass}");
    println!("MQR476_LOCAL={local}");
    println!("MQR476_CROSS={cross}");
    println!("MQR476_DIAGNOSTIC={diag}");
    println!("MQR476_SPLIT={split}");
    println!("MQR476_MERGE={merge}");
    println!("MQR476_NO_UPGRADE={no}");
    println!("MQR476_ORIGIN_NONLAUNDERING=PASS");
    println!("MQR476_CHALLENGE_COURT=PASS");
}
