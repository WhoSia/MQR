use std::{collections::{BTreeMap, BTreeSet}, env, fs, process};

const GENERATORS: [&str; 11] = [
    "THEORY","RIVAL","ANOMALY","INSTRUMENT","DOMAIN_GRAMMAR","EXTERNAL",
    "COUNTERMODEL","FRAMEWORK_EXTENSION","PROOF_OBLIGATION","POSTOUTCOME","LABEL_ONLY"
];
const REALIZABILITY: [&str; 4] = ["AVAILABLE","CURRENTLY_UNREALIZABLE","IMPOSSIBLE_IN_PRINCIPLE","NOT_APPLICABLE"];
const PERMISSION: [&str; 3] = ["PERMITTED","BLOCKED","NOT_APPLICABLE"];
const ACTIONS: [&str; 10] = [
    "ADMIT_NEW_FAILURE","ADMIT_SCIENTIFIC_DEBT","REJECT_INCOHERENT","REJECT_IRRELEVANT",
    "HOLD_POSTOUTCOME","HOLD_SCOPE_DRIFT","SPLIT_PARENT","MERGE_CHILDREN","HOLD_UNEARNED","NO_NEW_FAILURE"
];
const EVIDENCE: [&str; 6] = ["OBSERVED","PROVED","ENUMERATED","SIMULATED","INFERRED","OPEN"];
const TRANSITIONS: [&str; 4] = ["EXPAND","SPLIT","MERGE","TRANSPORT"];

#[derive(Debug)]
struct Perturbation {
    id: String, generator: String, coherent: bool, relevant: bool, independent: bool,
    realizability: String, permission: String, scope_preserved: bool, action: String,
}
#[derive(Debug)]
struct Transition { kind:String, source:String, target:String, receipt:String }

fn die(msg: impl AsRef<str>) -> ! { eprintln!("{}", msg.as_ref()); process::exit(2) }
fn yesno(s:&str)->bool { match s { "YES"=>true, "NO"=>false, _=>die(format!("expected YES/NO, got {s}")) } }
fn req<'a>(m:&'a BTreeMap<String,String>, k:&str)->&'a str { m.get(k).map(String::as_str).unwrap_or_else(||die(format!("missing required field: {k}"))) }
fn explicit(v:&str)->bool { !v.is_empty() && v!="OPEN" }

fn main(){
    let path=env::args().nth(1).unwrap_or_else(||die("usage: real-v31-envelope <packet>"));
    let src=fs::read_to_string(&path).unwrap_or_else(|e|die(format!("read failed: {e}")));
    let mut header=false; let mut ended=false;
    let mut fields=BTreeMap::<String,String>::new();
    let mut ps=Vec::<Perturbation>::new(); let mut ts=Vec::<Transition>::new();

    for (ln, raw) in src.lines().enumerate(){
        let line=raw.trim(); if line.is_empty() || line.starts_with('#'){continue}
        if line=="REALENVELOPE 0.31-CANDIDATE"{header=true;continue}
        if line=="END"{ended=true;break}
        let t:Vec<&str>=line.split_whitespace().collect();
        if t.first()==Some(&"perturbation"){
            if t.len()!=10 { die(format!("{}:{} perturbation expects 9 args",path,ln+1)); }
            if !GENERATORS.contains(&t[2]) || !REALIZABILITY.contains(&t[6]) || !PERMISSION.contains(&t[7]) || !ACTIONS.contains(&t[9]) {
                die(format!("{}:{} invalid perturbation enum",path,ln+1));
            }
            ps.push(Perturbation{id:t[1].into(),generator:t[2].into(),coherent:yesno(t[3]),relevant:yesno(t[4]),
                independent:yesno(t[5]),realizability:t[6].into(),permission:t[7].into(),scope_preserved:yesno(t[8]),action:t[9].into()});
            continue
        }
        if t.first()==Some(&"transition"){
            if t.len()!=5 || !TRANSITIONS.contains(&t[1]) || !explicit(t[4]) { die(format!("{}:{} invalid transition",path,ln+1)); }
            ts.push(Transition{kind:t[1].into(),source:t[2].into(),target:t[3].into(),receipt:t[4].into()}); continue
        }
        if t.len()!=2 { die(format!("{}:{} invalid field",path,ln+1)); }
        fields.insert(t[0].into(),t[1].into());
    }
    if !header || !ended { die("packet must contain REALENVELOPE 0.31-CANDIDATE ... END"); }
    if req(&fields,"sealed")!="PASS" { die("sealed must be PASS"); }
    for k in ["claim_scope_hash","obligation_family_hash","envelope_id","envelope_version","admissibility_rule_hash","revision_rule_hash"] {
        if !explicit(req(&fields,k)){die(format!("{k} must be explicit"))}
    }
    let evidence=req(&fields,"evidence_kind"); if !EVIDENCE.contains(&evidence){die("invalid evidence_kind")}
    if req(&fields,"completeness_claim")!="RELATIVE_ONLY" {die("completeness_claim must be RELATIVE_ONLY")}
    if req(&fields,"open_world_complete")!="OFF" {die("open_world_complete must be OFF")}

    let transition_kinds:BTreeSet<&str>=ts.iter().map(|x|x.kind.as_str()).collect();
    let mut reopen=false; let mut debt=0usize; let mut rejected=0usize; let mut holds=0usize; let mut stable=0usize;
    for p in &ps {
        match p.action.as_str() {
            "ADMIT_NEW_FAILURE" => {
                if !p.coherent || !p.relevant || !p.independent || !p.scope_preserved {die(format!("{} cannot be admitted as same-scope new failure",p.id))}
                if p.generator=="POSTOUTCOME" {die(format!("{} post-outcome candidate cannot be prospective authority",p.id))}
                if p.realizability=="IMPOSSIBLE_IN_PRINCIPLE" {die(format!("{} impossible perturbation cannot be admitted",p.id))}
                reopen=true;
            }
            "ADMIT_SCIENTIFIC_DEBT" => {
                if !p.coherent || !p.relevant || !p.independent || !p.scope_preserved {die(format!("{} invalid scientific debt",p.id))}
                if p.realizability!="CURRENTLY_UNREALIZABLE" || p.permission!="BLOCKED" {die(format!("{} scientific debt requires unrealizable+blocked",p.id))}
                debt+=1;
            }
            "REJECT_INCOHERENT" => { if p.coherent {die(format!("{} marked incoherent but coherence=YES",p.id))} rejected+=1; }
            "REJECT_IRRELEVANT" => { if p.relevant {die(format!("{} marked irrelevant but relevant=YES",p.id))} rejected+=1; }
            "HOLD_POSTOUTCOME" => { if p.generator!="POSTOUTCOME" || p.independent {die(format!("{} invalid post-outcome hold",p.id))} holds+=1; }
            "HOLD_SCOPE_DRIFT" => { if p.scope_preserved {die(format!("{} scope drift requires scope_preserved=NO",p.id))} holds+=1; }
            "SPLIT_PARENT" => { if !transition_kinds.contains("SPLIT"){die(format!("{} split requires SPLIT transition receipt",p.id))} holds+=1; }
            "MERGE_CHILDREN" => { if !transition_kinds.contains("MERGE"){die(format!("{} merge requires MERGE transition receipt",p.id))} holds+=1; }
            "HOLD_UNEARNED" => { if p.independent {die(format!("{} HOLD_UNEARNED expects independent=NO",p.id))} holds+=1; }
            "NO_NEW_FAILURE" => stable+=1,
            _=>unreachable!()
        }
        if p.permission=="BLOCKED" && p.action=="REJECT_IRRELEVANT" {die(format!("{} execution block cannot itself imply irrelevance",p.id))}
    }

    println!("envelope.id={}",req(&fields,"envelope_id"));
    println!("envelope.version={}",req(&fields,"envelope_version"));
    println!("envelope.claim_scope_hash={}",req(&fields,"claim_scope_hash"));
    println!("envelope.obligation_family_hash={}",req(&fields,"obligation_family_hash"));
    println!("envelope.perturbation_count={}",ps.len());
    println!("envelope.transition_count={}",ts.len());
    println!("envelope.scientific_debt_count={debt}");
    println!("envelope.rejected_count={rejected}");
    println!("envelope.hold_count={holds}");
    println!("envelope.stable_control_count={stable}");
    println!("envelope.successor_authority={}",if reopen{"REOPEN"}else{"UNCHANGED_AT_DECLARED_ENVELOPE"});
    println!("envelope.prior_scoped_certificate=HISTORICALLY_VALID_AT_PRIOR_DECLARED_ENVELOPE");
    println!("envelope.completeness_claim=RELATIVE_ONLY");
    println!("envelope.open_world_complete=OFF");
    println!("envelope.size_is_authority=NO");
    println!("envelope.stress_extremity_is_relevance=NO");
    println!("envelope.later_defeat_implies_retroactive_falsehood=NO");
    println!("envelope.evidence_kind={evidence}");
    println!("envelope.status=CANDIDATE_UNPROMOTED");

    for (i,t) in ts.iter().enumerate(){
        println!("envelope.transition.{i}={}:{}->{}:{}",t.kind,t.source,t.target,t.receipt);
    }
    for (i,p) in ps.iter().enumerate(){
        println!("envelope.perturbation.{i}={}:{}:{}:{}:{}:{}:{}:{}:{}",
            p.id,p.generator,if p.coherent{"YES"}else{"NO"},if p.relevant{"YES"}else{"NO"},if p.independent{"YES"}else{"NO"},
            p.realizability,p.permission,if p.scope_preserved{"YES"}else{"NO"},p.action);
    }
}
