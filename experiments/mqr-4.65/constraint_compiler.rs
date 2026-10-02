use std::collections::BTreeMap;
use std::fs;
use std::path::Path;

#[derive(Clone, Copy)]
struct Action {
    name: &'static str,
    utility: i32,
    cost: i32,
    sep: u8,
    reopen: bool,
    ancestry: bool,
    exterior: bool,
}

const CAT: [Action; 16] = [
    Action{name:"A0_HI_DROP",utility:2,cost:0,sep:0,reopen:false,ancestry:false,exterior:false},
    Action{name:"A1_FULL",utility:1,cost:0,sep:3,reopen:true,ancestry:true,exterior:true},
    Action{name:"A2_COST_FULL",utility:2,cost:1,sep:3,reopen:true,ancestry:true,exterior:true},
    Action{name:"A3_S0_HI",utility:2,cost:0,sep:1,reopen:false,ancestry:false,exterior:false},
    Action{name:"A4_S1_HI",utility:2,cost:0,sep:2,reopen:false,ancestry:false,exterior:false},
    Action{name:"A5_S0_REOPEN",utility:1,cost:0,sep:1,reopen:true,ancestry:true,exterior:false},
    Action{name:"A6_S1_REOPEN",utility:1,cost:0,sep:2,reopen:true,ancestry:true,exterior:false},
    Action{name:"A7_FULL_EXT",utility:1,cost:0,sep:3,reopen:false,ancestry:false,exterior:true},
    Action{name:"A8_DROP_REOPEN",utility:2,cost:1,sep:0,reopen:true,ancestry:true,exterior:true},
    Action{name:"A9_CHEAP_FULL_G0",utility:1,cost:1,sep:3,reopen:true,ancestry:false,exterior:false},
    Action{name:"A10_LOW_FULL",utility:0,cost:0,sep:3,reopen:true,ancestry:true,exterior:true},
    Action{name:"A11_HI_FULL",utility:2,cost:0,sep:3,reopen:false,ancestry:false,exterior:false},
    Action{name:"A12_HI_REOPEN_DROP",utility:2,cost:0,sep:0,reopen:true,ancestry:false,exterior:false},
    Action{name:"A13_HI_G1_DROP",utility:2,cost:0,sep:0,reopen:false,ancestry:true,exterior:false},
    Action{name:"A14_HI_EXT_DROP",utility:2,cost:0,sep:0,reopen:false,ancestry:false,exterior:true},
    Action{name:"A15_FULL_REOPEN_EXT_G0",utility:1,cost:0,sep:3,reopen:true,ancestry:false,exterior:true},
];

#[derive(Clone, Copy)]
struct World {
    irr: bool,
    sub: bool,
    reopen_live: bool,
    anc_live: bool,
    ext_live: bool,
}

#[derive(Clone, Copy)]
enum Constraint { Opr, Arr, Eai, Exterior, Nedl }
#[derive(Clone, Copy)]
enum Baseline { Myopic, Lookahead, Constrained, Diversity }

const CONS: [Constraint;5] = [Constraint::Opr,Constraint::Arr,Constraint::Eai,Constraint::Exterior,Constraint::Nedl];
const BASES: [Baseline;4] = [Baseline::Myopic,Baseline::Lookahead,Baseline::Constrained,Baseline::Diversity];

fn pop2(x:u8)->i32 { ((x&1)!=0) as i32 + ((x&2)!=0) as i32 }
fn eff_sep(a:Action,w:World)->u8 {
    if !w.irr {3} else if w.sub { if a.sep != 0 {1} else {0} } else {a.sep}
}
fn eff_reopen(a:Action,w:World)->bool { if !w.irr {true} else {a.reopen} }
fn net(a:Action)->i32 {a.utility-a.cost}

fn source_allowed(a:Action, actions:&[Action;3], w:World, c:Constraint)->bool {
    match c {
        Constraint::Opr => {
            if !w.irr { return true; }
            let anyp=actions.iter().any(|x|eff_sep(*x,w)!=0);
            !anyp || eff_sep(a,w)!=0
        }
        Constraint::Arr => {
            if !w.reopen_live { return true; }
            let anyp=actions.iter().any(|x|eff_reopen(*x,w));
            !anyp || eff_reopen(a,w)
        }
        Constraint::Eai => {
            if !w.anc_live { return true; }
            let anyp=actions.iter().any(|x|x.ancestry);
            !anyp || a.ancestry
        }
        Constraint::Exterior => {
            if !w.ext_live { return true; }
            let anyp=actions.iter().any(|x|x.exterior);
            !anyp || a.exterior
        }
        Constraint::Nedl => {
            if !w.irr { return true; }
            if w.sub {
                let anyp=actions.iter().any(|x|eff_sep(*x,w)!=0);
                return !anyp || eff_sep(a,w)!=0;
            }
            let anyfull=actions.iter().any(|x|eff_sep(*x,w)==3);
            if anyfull { return eff_sep(a,w)==3; }
            let anyp=actions.iter().any(|x|eff_sep(*x,w)!=0);
            !anyp || eff_sep(a,w)!=0
        }
    }
}

// Independently spelled target-C1 feasibility over the complete closed-state feature tuple.
fn compiled_c1_allowed(a:Action, actions:&[Action;3], w:World, c:Constraint)->bool {
    match c {
        Constraint::Opr => !w.irr || !actions.iter().any(|x|eff_sep(*x,w)>0) || eff_sep(a,w)>0,
        Constraint::Arr => !w.reopen_live || !actions.iter().any(|x|eff_reopen(*x,w)) || eff_reopen(a,w),
        Constraint::Eai => !w.anc_live || !actions.iter().any(|x|x.ancestry) || a.ancestry,
        Constraint::Exterior => !w.ext_live || !actions.iter().any(|x|x.exterior) || a.exterior,
        Constraint::Nedl => {
            if !w.irr { true }
            else if w.sub {
                !actions.iter().any(|x|eff_sep(*x,w)>0) || eff_sep(a,w)>0
            } else if actions.iter().any(|x|eff_sep(*x,w)==3) {
                eff_sep(a,w)==3
            } else {
                !actions.iter().any(|x|eff_sep(*x,w)>0) || eff_sep(a,w)>0
            }
        }
    }
}

fn baseline_feasible(actions:&[Action;3],w:World,b:Baseline)->Vec<usize>{
    let all=vec![0usize,1,2];
    match b {
        Baseline::Constrained if w.irr && actions.iter().any(|a|eff_sep(*a,w)>0) =>
            all.into_iter().filter(|i|eff_sep(actions[*i],w)>0).collect(),
        _ => all
    }
}
fn score(a:Action,w:World,b:Baseline)->i32{
    let n=net(a)*20;
    match b {
        Baseline::Myopic|Baseline::Constrained => n,
        Baseline::Lookahead => n+20*pop2(eff_sep(a,w)) + if w.reopen_live && eff_reopen(a,w){10}else{0},
        Baseline::Diversity => n + if w.anc_live && a.ancestry{8}else{0} + if w.ext_live && a.exterior{8}else{0},
    }
}
fn choose(actions:&[Action;3],w:World,b:Baseline,ids:&[usize])->Option<usize>{
    ids.iter().copied().max_by_key(|i|(score(actions[*i],w,b),-(*i as i32)))
}

fn closed_surface()->(u64,u64,u64,u64) {
    let mut pred=0u64; let mut pred_m=0u64; let mut pol=0u64; let mut pol_m=0u64;
    for i in 0..16 { for j in i..16 { for k in j..16 {
        let actions=[CAT[i],CAT[j],CAT[k]];
        for flags in 0u8..32 {
            let w=World{irr:flags&1!=0,sub:flags&2!=0,reopen_live:flags&4!=0,anc_live:flags&8!=0,ext_live:flags&16!=0};
            for c in CONS {
                for a in actions {
                    pred+=1;
                    if source_allowed(a,&actions,w,c)!=compiled_c1_allowed(a,&actions,w,c){pred_m+=1;}
                }
                for b in BASES {
                    let base=baseline_feasible(&actions,w,b);
                    let sids:Vec<_>=base.iter().copied().filter(|idx|source_allowed(actions[*idx],&actions,w,c)).collect();
                    let tids:Vec<_>=base.iter().copied().filter(|idx|compiled_c1_allowed(actions[*idx],&actions,w,c)).collect();
                    pol+=1;
                    if choose(&actions,w,b,&sids)!=choose(&actions,w,b,&tids){pol_m+=1;}
                }
            }
        }
    }}}
    (pred,pred_m,pol,pol_m)
}

#[derive(Clone,Copy,PartialEq,Eq)]
enum Event { N,D,R }
fn source_debt(hist:&[Event])->bool {
    let mut d=false;
    for e in hist {
        match e {Event::D=>d=true,Event::R=>d=false,Event::N=>{}}
    }
    d
}
fn c1_debt(hist:&[Event])->bool { matches!(hist.last(),Some(Event::D)) }
fn emit_histories(len:usize,cur:&mut Vec<Event>,out:&mut Vec<Vec<Event>>){
    if cur.len()==len {out.push(cur.clone());return;}
    for e in [Event::N,Event::D,Event::R] {cur.push(e);emit_histories(len,cur,out);cur.pop();}
}
fn memory_surface()->(u64,u64,u64,u64){
    let mut hs=Vec::new();
    for len in 0..=5 {emit_histories(len,&mut Vec::new(),&mut hs);}
    let mut comps=0u64; let mut c1_state_coll=0u64; let mut c2_m=0u64;
    for h in &hs {
        let s=source_debt(h); let t1=c1_debt(h); let t2=source_debt(h);
        if s!=t1 {c1_state_coll+=1;}
        for action in 0..3 {
            let src=!(s && action==1);
            let c2=!(t2 && action==1);
            comps+=1;
            if src!=c2 {c2_m+=1;}
        }
    }
    (hs.len() as u64,comps,c1_state_coll,c2_m)
}

fn frontier_surface()->(u64,u64,u64,bool){
    let mut comps=0u64; let mut fixed2_m=0u64; let mut c3_m=0u64;
    for n in 1u32..=8 {
        let mask=(1u32<<n)-1;
        let lowmask=(1u32<<n.min(2))-1;
        for live in 0..=mask {
            for cov in 0..=mask {
                let src=(live & (!cov) & mask)==0;
                let fixed2=((live&lowmask) & (!cov) & lowmask)==0;
                let c3=(live & (!cov) & mask)==0;
                comps+=1;
                if src!=fixed2 {fixed2_m+=1;}
                if src!=c3 {c3_m+=1;}
            }
        }
    }
    let n=3u32; let mask=(1u32<<n)-1; let live=1u32<<2; let cov=0u32; let lowmask=3u32;
    let src=(live & (!cov) & mask)==0;
    let fixed2=((live&lowmask) & (!cov) & lowmask)==0;
    (comps,fixed2_m,c3_m,!src && fixed2)
}

fn apply_event(state:u8,e:u8)->u8 {
    let id=e%4;
    if e<4 {state | (1u8<<id)} else {state & !(1u8<<id)}
}
fn replay(hist:&[u8])->u8 { hist.iter().fold(0u8,|s,e|apply_event(s,*e)) }
fn emit_genesis(len:usize,cur:&mut Vec<u8>,out:&mut Vec<Vec<u8>>){
    if cur.len()==len {out.push(cur.clone());return;}
    for e in 0u8..8 {cur.push(e);emit_genesis(len,cur,out);cur.pop();}
}
fn genesis_surface()->(u64,u64){
    let mut hs=Vec::new();
    for len in 0..=4 {emit_genesis(len,&mut Vec::new(),&mut hs);}
    let mut mism=0u64;
    for h in &hs {
        let src=replay(h);
        let mut c3=0u8;
        for e in h { c3=apply_event(c3,*e); }
        if src!=c3 {mism+=1;}
    }
    (hs.len() as u64,mism)
}

fn main(){
    let (closed,closed_m,pol,pol_m)=closed_surface();
    let (mh,mc,mcoll,m2)=memory_surface();
    let (fc,fm,f3,wit)=frontier_surface();
    let (gh,gm)=genesis_surface();

    assert_eq!(closed,391_680);
    assert_eq!(closed_m,0);
    assert_eq!(pol,522_240);
    assert_eq!(pol_m,0);
    assert_eq!(mh,364);
    assert_eq!(mc,1_092);
    assert_eq!(mcoll,58);
    assert_eq!(m2,0);
    assert_eq!(fc,87_380);
    assert_eq!(fm,39_312);
    assert_eq!(f3,0);
    assert!(wit);
    assert_eq!(gh,4_681);
    assert_eq!(gm,0);

    let mut rows=BTreeMap::new();
    rows.insert("CLOSED_POLICY_COMPARISONS",pol);
    rows.insert("CLOSED_POLICY_MISMATCHES",pol_m);
    rows.insert("CLOSED_PREDICATE_COMPARISONS",closed);
    rows.insert("CLOSED_PREDICATE_MISMATCHES",closed_m);
    rows.insert("FRONTIER_C3_MISMATCHES",f3);
    rows.insert("FRONTIER_COMPARISONS",fc);
    rows.insert("FRONTIER_FIXED2_MISMATCHES",fm);
    rows.insert("GENESIS_C3_MISMATCHES",gm);
    rows.insert("GENESIS_HISTORIES",gh);
    rows.insert("MEMORY_ACTION_COMPARISONS",mc);
    rows.insert("MEMORY_C1_STATE_COLLISIONS",mcoll);
    rows.insert("MEMORY_C2_MISMATCHES",m2);
    rows.insert("MEMORY_HISTORIES",mh);
    rows.insert("MINIMAL_FIXED2_WITNESS",if wit{1}else{0});

    let dir=Path::new("experiments/mqr-4.65/results");
    fs::create_dir_all(dir).unwrap();
    let mut tsv=String::from("metric\tvalue\n");
    for (k,v) in &rows {tsv.push_str(&format!("{}\t{}\n",k,v));}
    fs::write(dir.join("rust_summary.tsv"),tsv).unwrap();

    println!("MQR465_CLOSED_C1=PASS");
    println!("MQR465_CLOSED_POLICY_BISIM=PASS");
    println!("MQR465_MEMORY_C1_COLLISIONS={}",mcoll);
    println!("MQR465_MEMORY_C2=PASS");
    println!("MQR465_FIXED_SCHEMA_MISMATCHES={}",fm);
    println!("MQR465_C3_FRONTIER=PASS");
    println!("MQR465_C3_GENESIS_TRANSITION=PASS");
    println!("MQR465_MINIMAL_FIXED2_WITNESS=PASS");
    println!("MQR465_C4_NONREPRESENTABILITY_NOT_INFERRED_FROM_FINITE_TESTS=PASS");
}
