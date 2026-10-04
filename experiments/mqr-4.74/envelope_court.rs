use std::{collections::HashMap, fs, process};

fn yn(x:&str)->bool{match x{"YES"=>true,"NO"=>false,_=>{eprintln!("bad YES/NO {x}");process::exit(2)}}}

fn verdict(r:&HashMap<String,String>)->&'static str{
    let coherent=yn(&r["coherent"]);
    let relevant=yn(&r["claim_relevant"]);
    let independent=yn(&r["independent_motivation"]);
    let scope=yn(&r["scope_preserved"]);
    let action=r["action"].as_str();
    match action {
        "ADMIT_NEW_FAILURE" => {
            if coherent && relevant && independent && scope {"REOPEN_SUCCESSOR_AUTHORITY"} else {"HOLD_UNEARNED"}
        }
        "ADMIT_SCIENTIFIC_DEBT" => {
            if coherent && relevant && independent && scope && r["realizability"]=="CURRENTLY_UNREALIZABLE" && r["execution_permission"]=="BLOCKED"
            {"KEEP_EXECUTION_HOLD"} else {"HOLD_UNEARNED"}
        }
        "REJECT_INCOHERENT" => if !coherent {"KEEP_CERTIFICATE"} else {"HOLD_UNEARNED"},
        "REJECT_IRRELEVANT" => if !relevant {"KEEP_CERTIFICATE"} else {"HOLD_UNEARNED"},
        "HOLD_POSTOUTCOME" => if !independent {"NO_RETROACTIVE_USE"} else {"HOLD_UNEARNED"},
        "HOLD_SCOPE_DRIFT" => {
            if !scope {
                if r["domain"]=="MATH" {"SEMANTIC_TRANSPORT_REQUIRED"} else {"TRANSPORT_REQUIRED"}
            } else {"HOLD_UNEARNED"}
        }
        "SPLIT_PARENT" => "SPLIT_RECEIPT_REQUIRED",
        "MERGE_CHILDREN" => "MERGE_LOSS_AUDIT_REQUIRED",
        "HOLD_UNEARNED" => "KEEP_CERTIFICATE",
        "NO_NEW_FAILURE" => "KEEP_SCOPED_HISTORICAL_CERTIFICATE",
        _ => "HOLD_UNEARNED"
    }
}

fn main(){
    let path="experiments/mqr-4.74/COURT-FREEZE.tsv";
    let src=fs::read_to_string(path).unwrap_or_else(|e|{eprintln!("{e}");process::exit(2)});
    let mut lines=src.lines();
    let headers:Vec<&str>=lines.next().unwrap().split('\t').collect();
    let mut n=0; let mut bad=0;
    let mut under=false; let mut over=false; let mut blocked=false; let mut post=false; let mut math=false; let mut historical=false;
    for line in lines{
        if line.trim().is_empty(){continue}
        let vals:Vec<&str>=line.split('\t').collect();
        if vals.len()!=headers.len(){eprintln!("bad row {line}");process::exit(2)}
        let mut r=HashMap::new(); for(i,h) in headers.iter().enumerate(){r.insert((*h).to_string(),vals[i].to_string());}
        let got=verdict(&r); n+=1;
        if got!=r["expected"] {bad+=1;eprintln!("{}: {} != {}",r["case_id"],got,r["expected"]);}
        match r["case_id"].as_str(){
            "E1"=>under=got=="REOPEN_SUCCESSOR_AUTHORITY",
            "E3"=>over=got=="KEEP_CERTIFICATE",
            "E2"=>blocked=got=="KEEP_EXECUTION_HOLD",
            "E6"=>post=got=="NO_RETROACTIVE_USE",
            "M2"=>math=got=="SEMANTIC_TRANSPORT_REQUIRED",
            "H1"=>historical=got=="KEEP_SCOPED_HISTORICAL_CERTIFICATE",
            _=>{}
        }
    }
    let ok=bad==0&&n==15&&under&&over&&blocked&&post&&math&&historical;
    println!("MQR474_ENVELOPE_COURT={}",if ok{"PASS"}else{"FAIL"});
    println!("MQR474_CASES={n}");
    println!("MQR474_UNDERINCLUSION_REOPENS={}",if under{"YES"}else{"NO"});
    println!("MQR474_OVERINCLUSION_DOES_NOT_AUTO_DEFEAT={}",if over{"YES"}else{"NO"});
    println!("MQR474_BLOCKED_EXECUTION_PRESERVES_DEBT={}",if blocked{"YES"}else{"NO"});
    println!("MQR474_POSTOUTCOME_NO_RETROACTIVE_USE={}",if post{"YES"}else{"NO"});
    println!("MQR474_MATH_SCOPE_DRIFT_NEEDS_SEMANTIC_TRANSPORT={}",if math{"YES"}else{"NO"});
    println!("MQR474_PRIOR_SCOPED_CERTIFICATE_REMAINS_HISTORICAL={}",if historical{"YES"}else{"NO"});
    if !ok{process::exit(1)}
}
