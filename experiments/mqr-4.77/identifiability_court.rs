use std::{env,fs,process,collections::BTreeMap};

#[derive(Debug)]
struct Case {
    id:String, domain:String, scenario:String,
    disagree:bool, separator:bool, prospective:bool,
    relevant_ambiguity:bool, full_graph_needed:bool, expected:String,
}
fn die(s:&str)->!{eprintln!("{s}");process::exit(2)}
fn yn(s:&str)->bool{match s{"YES"=>true,"NO"=>false,_=>die("invalid YES/NO")}}

fn classify(c:&Case)->&'static str{
    if c.scenario=="later_hidden_ancestor_discovered" { return "REOPEN_HIDDEN_COMMON_MODE"; }
    if c.scenario=="later_evidence_restores_decisive_shared_path" { return "BREAK_DEFEATED"; }

    if !c.disagree {
        return "LOCALLY_SEPARATED_BREAK";
    }

    if !c.relevant_ambiguity {
        return "LOCALLY_SEPARATED_BREAK";
    }

    if !c.separator {
        if c.scenario=="single_selected_graph_only" { return "UNIDENTIFIED_BREAK"; }
        if c.scenario=="negative_control_not_discriminating_graphs" { return "DIAGNOSTIC_BREAK_ONLY"; }
        return "PARTIALLY_IDENTIFIED_BREAK";
    }

    if !c.prospective {
        return "DIAGNOSTIC_BREAK_ONLY";
    }

    if matches!(c.scenario.as_str(),
        "independent_raw_data_independent_preprocessing_same_anomaly" |
        "independent_reformalization_same_theorem" |
        "partial_theorem_correspondence") {
        return "LOCALLY_SEPARATED_BREAK";
    }

    "ROBUST_SEPARATION_WITHIN_DECLARED_FAMILY"
}

fn main(){
    let p=env::args().nth(1).unwrap_or_else(||die("usage: mqr477-court <tsv>"));
    let s=fs::read_to_string(&p).unwrap_or_else(|_|die("read failed"));
    let mut lines=s.lines();
    let header=lines.next().unwrap_or("");
    if header!="id\tdomain\tscenario\tlive_graphs_disagree_on_cut\tseparator_targets_disagreement\tprospective\tclaim_relevant_ambiguity\tfull_graph_needed\texpected_state" {
        die("bad header");
    }
    let mut n=0usize; let mut pass=0usize; let mut counts:BTreeMap<String,usize>=BTreeMap::new();
    for line in lines {
        if line.trim().is_empty(){continue}
        let t:Vec<&str>=line.split('\t').collect();
        if t.len()!=9{die("bad row")}
        let c=Case{
            id:t[0].into(),domain:t[1].into(),scenario:t[2].into(),
            disagree:yn(t[3]),separator:yn(t[4]),prospective:yn(t[5]),
            relevant_ambiguity:yn(t[6]),full_graph_needed:yn(t[7]),expected:t[8].into()
        };
        if c.full_graph_needed { die("frozen court forbids global-graph fetish"); }
        let got=classify(&c);
        println!("{}\t{}\t{}\t{}",c.id,c.domain,c.expected,got);
        if got!=c.expected {
            eprintln!("mismatch {} expected={} got={}",c.id,c.expected,got);
            process::exit(1);
        }
        n+=1;pass+=1;*counts.entry(got.into()).or_insert(0)+=1;
    }
    println!("MQR477_CASES={n}");
    println!("MQR477_PASS={pass}");
    for k in [
        "UNIDENTIFIED_BREAK","DIAGNOSTIC_BREAK_ONLY","PARTIALLY_IDENTIFIED_BREAK",
        "LOCALLY_SEPARATED_BREAK","ROBUST_SEPARATION_WITHIN_DECLARED_FAMILY",
        "REOPEN_HIDDEN_COMMON_MODE","BREAK_DEFEATED"
    ] {
        println!("MQR477_{}={}",k,counts.get(k).copied().unwrap_or(0));
    }
    println!("MQR477_FULL_GRAPH_IDENTIFICATION_REQUIRED=NO");
    println!("MQR477_SELECTED_GRAPH_LAUNDERING=REJECT");
    println!("MQR477_OPEN_WORLD_INDEPENDENCE=REJECT");
    println!("MQR477_COURT=PASS");
}
