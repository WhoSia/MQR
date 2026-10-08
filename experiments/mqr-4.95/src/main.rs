//! MQR-4.95: real publisher-source label auditing and finite-risk identification.
//! All science calculations use std-only Rust; no Python model or CSV utilities.
//! New FNV site permutation + GD logistic is NOT author sklearn replication.
//! Target labels are re-read only after scores, site selections and policies fix.
use std::collections::{BTreeMap, BTreeSet};
use std::error::Error;
use std::fs::{self, File};
use std::io::{BufRead, BufReader, Write};
use std::path::Path;

const F: usize = 19;
const N_TARGET: usize = 64;
const BUDGETS: [usize; 6] = [0, 4, 8, 16, 32, 64];
const WEST_MAX: f64 = 24.720692;
const EAST_MIN: f64 = 25.278482;
const SOURCE_ROOT: &str = "Serov2026/egorser0v/Importance-reweighting/46c4d011c9f0cd0614c08e7edb68ac2491f659c8";
const ORIGINAL_BLOB: &str = "0e1c83dda391229ffd3cb69573d184eebf1c7bdd";
const AUDIT_SALT: &str = "MQR495-OriginalSite-Fnv64-v1";
const EPOCHS: usize = 1000;
const STEP: f64 = 0.12;
const RIDGE: f64 = 0.015;

#[derive(Clone)]
struct Site {
    row_id: usize, lat: f64, lon: f64, site_id: String, bio: [f64; F],
}
#[derive(Clone, Copy, Debug)]
struct LossPair { neg: f64, pos: f64 }
impl LossPair {
    fn from_p(p: f64) -> Self {
        let p = p.clamp(1e-6, 1. - 1e-6);
        Self { neg: -(1. - p).ln(), pos: -p.ln() }
    }
    fn extrema(self) -> (f64, f64) { (self.neg.min(self.pos), self.neg.max(self.pos)) }
    fn actual(self, y: u8) -> f64 { if y == 1 { self.pos } else { self.neg } }
    fn span(self) -> f64 { (self.neg - self.pos).abs() }
}
#[derive(Clone, Copy, Debug)]
struct Bound { lower: f64, upper: f64 }
impl Bound { fn width(self) -> f64 { self.upper - self.lower } }
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum RootClaim { SamePublisher, UnattestedOtherPublisher, IndependentlyAttested }
fn can_upgrade_external(root: RootClaim, sites_verified: bool, labels_verified: bool, policy_frozen: bool) -> bool {
    root == RootClaim::IndependentlyAttested && sites_verified && labels_verified && policy_frozen
}
fn fnv(bytes: &[u8]) -> u64 {
    let mut h: u64 = 14695981039346656037;
    for x in bytes { h ^= u64::from(*x); h = h.wrapping_mul(1099511628211); }
    h
}
fn rank(prefix: &str, value: &str) -> u64 {
    fnv(format!("{AUDIT_SALT}|{prefix}|{value}").as_bytes())
}
fn error(msg: &str) -> Box<dyn Error> {
    std::io::Error::new(std::io::ErrorKind::InvalidData, msg).into()
}
fn headers(raw: &str) -> Vec<&str> {
    raw.trim_start_matches('\u{feff}').trim_end().split(',').map(|field|field.trim().trim_matches('"')).collect()
}
fn columns(path: &str) -> Result<(usize,usize,usize,usize,[usize;F]),Box<dyn Error>> {
    let file=File::open(path)?;
    let header=BufReader::new(file).lines().next().ok_or_else(|| error("empty publisher CSV"))??;
    let keys=headers(&header);
    let idx=|name: &str| -> Result<usize,Box<dyn Error>> {
        keys.iter().position(|z| *z==name).ok_or_else(||error(&format!("missing source CSV field: {name}")))
    };
    let mut bio=[0;F];
    for j in 0..F { bio[j]=idx(&format!("bio{}",j+1))?; }
    Ok((idx("lat")?,idx("long")?,idx("year")?,idx("presence")?,bio))
}
fn finite_frame(path: &str) -> Result<(Vec<Site>,usize),Box<dyn Error>> {
    let (ilat,ilon,iy,_label,bi)=columns(path)?;
    let mut frame=Vec::new();
    let mut raw_count=0;
    for (i,line) in BufReader::new(File::open(path)?).lines().enumerate() {
        if i==0 { continue; }
        raw_count+=1;
        let line=line?;
        let values:Vec<&str>=line.split(',').collect();
        let parsed=|| -> Option<Site> {
            let lat=values.get(ilat)?.trim().parse::<f64>().ok()?;
            let lon=values.get(ilon)?.trim().parse::<f64>().ok()?;
            let year=values.get(iy)?.trim().parse::<f64>().ok()?;
            if !(2013.0..=2024.0).contains(&year) || !lat.is_finite() || !lon.is_finite() ||
                !(59.0..=71.5).contains(&lat) || !(19.0..=32.5).contains(&lon) {
                return None;
            }
            let mut bio=[0.0_f64;F];
            for j in 0..F {
                bio[j]=values.get(bi[j])?.trim().parse().ok()?;
                if !bio[j].is_finite(){ return None; }
            }
            let site_id=format!("{lat:.6}|{lon:.6}");
            Some(Site{row_id:i+1,lat,lon,site_id,bio})
        };
        if let Some(r)=parsed() { frame.push(r); }
    }
    Ok((frame,raw_count))
}
// This reads "presence" only for precisely requested rows, not the entire target.
fn reveal_labels(path: &str, desired: &BTreeSet<usize>) -> Result<BTreeMap<usize,u8>, Box<dyn Error>> {
    let (_,_,_,label_col,_)=columns(path)?;
    let mut labels=BTreeMap::new();
    for (i,line) in BufReader::new(File::open(path)?).lines().enumerate() {
        if i==0 || !desired.contains(&(i+1)) { continue; }
        let line=line?;
        let bits:Vec<&str>=line.split(',').collect();
        let y: u8=bits.get(label_col).ok_or_else(||error("target label column missing"))?.trim().parse()?;
        if y>1 { return Err(error("nonbinary original label, abort")); }
        labels.insert(i+1,y);
    }
    if labels.len()!=desired.len(){return Err(error("not every chosen original site label was found"));}
    Ok(labels)
}
fn sites(frame: &[Site], role: &str) -> Vec<Site> {
    let mut single:BTreeMap<String,(u64,Site)>=BTreeMap::new();
    for r in frame {
        let rowrank=rank("DEDUP",&format!("{}|{}",r.row_id,r.site_id));
        match single.get(&r.site_id) {
            Some((old,_)) if *old <= rowrank => {},
            _ => { single.insert(r.site_id.clone(),(rowrank,r.clone())); }
        }
    }
    let mut rows:Vec<Site>=single.into_values().map(|(_,r)|r).collect();
    rows.sort_by_key(|r|(rank(role,&r.site_id),r.site_id.clone()));
    rows
}
struct Scaling { mean:[f64;F], sd:[f64;F] }
impl Scaling {
    fn fit(train:&[Site])->Self {
        let n=train.len() as f64;
        let mut mean=[0.;F];
        let mut sd=[0.;F];
        for r in train { for j in 0..F { mean[j]+=r.bio[j]/n; }}
        for r in train {for j in 0..F {sd[j]+=(r.bio[j]-mean[j]).powi(2)/n;}}
        for item in &mut sd { *item= item.sqrt().max(1e-12); }
        Self{mean,sd}
    }
    fn x(&self,r:&Site)->[f64;F] {
        let mut x=[0.;F];
        for j in 0..F {x[j]=(r.bio[j]-self.mean[j])/self.sd[j];}
        x
    }
}
fn sigmoid(z:f64)->f64 {
    if z>=0. {1./(1.+(-z).exp())} else {let e=z.exp();e/(1.+e)}
}
fn train_predictor(fit:&[Site], labels:&BTreeMap<usize,u8>) -> Result<(Scaling,[f64;F+1]),Box<dyn Error>> {
    let positive=fit.iter().filter(|r|labels.get(&r.row_id)==Some(&1)).count();
    if positive==0 || positive==fit.len(){return Err(error("source FIT lacks two original classes"));}
    let scaler=Scaling::fit(fit);
    let x:Vec<[f64;F]>=fit.iter().map(|r|scaler.x(r)).collect();
    let ys:Vec<f64>=fit.iter().map(|r|f64::from(labels[&r.row_id])).collect();
    let n=fit.len() as f64;
    let mut coef=[0.;F+1];
    for _ in 0..EPOCHS {
        let mut grad=[0.;F+1];
        for (row,y) in x.iter().zip(ys.iter()) {
            let logit=coef[0]+(0..F).map(|j|coef[j+1]*row[j]).sum::<f64>();
            let diff=sigmoid(logit)-y;
            grad[0]+=diff/n;
            for j in 0..F {grad[j+1]+=diff*row[j]/n;}
        }
        coef[0]-=STEP*grad[0];
        for j in 1..=F {coef[j]-=STEP*(grad[j]+RIDGE*coef[j]);}
    }
    if !coef.iter().all(|q|q.is_finite()){return Err(error("numerical issue fitting source-only logistic model"));}
    Ok((scaler,coef))
}
fn score(model:&[f64;F+1], scaler:&Scaling, r:&Site)->f64 {
    let x=scaler.x(r);
    sigmoid(model[0]+(0..F).map(|j|model[j+1]*x[j]).sum::<f64>()).clamp(1e-6,1.-1e-6)
}
fn label_free_bounds(pairs:&[LossPair]) -> Bound {
    let n=pairs.len() as f64;
    let mut lower=0.;
    let mut upper=0.;
    for p in pairs {let (a,b)=p.extrema();lower+=a/n;upper+=b/n;}
    Bound{lower,upper}
}
fn observed_bound(pairs:&[LossPair],labels:&[u8],selection:&[usize]) -> Bound {
    let observed:BTreeSet<usize>=selection.iter().copied().collect();
    let mut lower=0.;
    let mut upper=0.;
    let n=pairs.len() as f64;
    for (i,p) in pairs.iter().enumerate(){
        if observed.contains(&i) {
            let loss=p.actual(labels[i]);
            lower+=loss/n; upper+=loss/n;
        } else {
            let (lo,hi)=p.extrema();
            lower+=lo/n;upper+=hi/n;
        }
    }
    Bound{lower,upper}
}
fn audit_order(pairs:&[LossPair],target:&[Site],strategy:&str)->Vec<usize> {
    let mut order:Vec<usize>=(0..pairs.len()).collect();
    match strategy {
        "hash" => order.sort_by_key(|&i|(rank("AUDIT_HASH",&target[i].site_id),target[i].site_id.clone())),
        "top_width" => order.sort_by(|&i,&j| pairs[j].span().total_cmp(&pairs[i].span()).then_with(||target[i].site_id.cmp(&target[j].site_id))),
        "latitude_stratified_top_width" => {
            let mut geo:Vec<usize>=order.clone();
            geo.sort_by(|&i,&j|target[i].lat.total_cmp(&target[j].lat).then_with(||target[i].site_id.cmp(&target[j].site_id)));
            let mut bands:Vec<Vec<usize>>=Vec::new();
            for group in 0..4 {
                let mut g=geo[group*16..(group+1)*16].to_vec();
                g.sort_by(|&i,&j|pairs[j].span().total_cmp(&pairs[i].span()).then_with(||target[i].site_id.cmp(&target[j].site_id)));
                bands.push(g);
            }
            order.clear();
            for q in 0..16 { for band in &bands {order.push(band[q]);} }
        },
        _ => panic!("unexpected frozen audit strategy")
    }
    order
}
fn assert_invariants(pairs:&[LossPair], y:&[u8],oracle:f64,order:&[usize],style:&str)
    -> Result<(),Box<dyn Error>> {
    let n=pairs.len();
    if n!=N_TARGET||y.len()!=n||order.len()!=n||order.iter().copied().collect::<BTreeSet<_>>().len()!=n {
        return Err(error("nonunique or wrong-size audit order"));
    }
    let mut old=f64::INFINITY;
    for &k in &BUDGETS {
        let set=&order[..k];
        let bound=observed_bound(pairs,y,set);
        let width=pairs.iter().enumerate().filter(|(i,_)|!set.contains(i))
            .map(|(_,p)|p.span()).sum::<f64>() / n as f64;
        if (width-bound.width()).abs()>1e-9 || bound.width()>old+1e-9 ||
           oracle<bound.lower-1e-9 || oracle>bound.upper+1e-9 {
            return Err(error(&format!("{style}: sharp contraction, monotonicity or oracle containment failed")));
        }
        old=bound.width();
    }
    if old.abs()>1e-9 {return Err(error("complete target audit did not identify finite mean exactly"));}
    Ok(())
}
fn main()->Result<(),Box<dyn Error>> {
    let args:Vec<String>=std::env::args().collect();
    if args.len()!=3{return Err(error("usage: cargo run -- SOURCE_CSV OUTPUT_DIR"));}
    let path=&args[1];
    let out=&args[2];
    fs::create_dir_all(out)?;
    let (frame,raw_rows)=finite_frame(path)?;
    if frame.len()!=2905 {return Err(error("MQR493 frozen complete coordinate+BIO source count mismatch"));}
    let west=sites(&frame.iter().filter(|r|r.lon<=WEST_MAX).cloned().collect::<Vec<_>>(),"WEST");
    let east=sites(&frame.iter().filter(|r|r.lon>=EAST_MIN).cloned().collect::<Vec<_>>(),"EAST");
    if west.len()<576 || east.len()<N_TARGET {return Err(error("geographic original target site sample infeasible"));}
    let fit=&west[..512];
    let validation=&west[512..576];
    let target=&east[..N_TARGET];
    let mut ids=BTreeSet::new();
    for r in fit.iter().chain(validation).chain(target) {if !ids.insert(r.site_id.clone()){return Err(error("site overlap"));}}
    let source_ids=fit.iter().chain(validation).map(|r|r.row_id).collect::<BTreeSet<_>>();
    let source_labels=reveal_labels(path,&source_ids)?;
    let (scaler,model)=train_predictor(fit,&source_labels)?;
    let scores:Vec<f64>=target.iter().map(|r|score(&model,&scaler,r)).collect();
    let pairs:Vec<LossPair>=scores.iter().map(|&p|LossPair::from_p(p)).collect();
    let unlabelled=label_free_bounds(&pairs);
    let methods=["hash","top_width","latitude_stratified_top_width"];
    let strategies:Vec<(&str,Vec<usize>)>=methods.iter()
        .map(|&s|(s,audit_order(&pairs,target,s))).collect();
    // The data-dependent order is frozen from P/X and predictions; no target Y consulted yet.
    let target_ids=target.iter().map(|r|r.row_id).collect::<BTreeSet<_>>();
    let target_labels=reveal_labels(path,&target_ids)?;
    let ys:Vec<u8>=target.iter().map(|r|target_labels[&r.row_id]).collect();
    let oracle=pairs.iter().zip(ys.iter()).map(|(p,&y)|p.actual(y)).sum::<f64>() / 64.;
    for (style,order) in &strategies {assert_invariants(&pairs,&ys,oracle,order,style)?;}
    // Maximum width shrink for any k equal-cost label observations: sort by span.
    let best=strategies.iter().find(|z|z.0=="top_width").unwrap();
    for (style,order) in &strategies {
        for &k in &BUDGETS {
            let winner=observed_bound(&pairs,&ys,&best.1[..k]).width();
            let candidate=observed_bound(&pairs,&ys,&order[..k]).width();
            if winner>candidate+1e-9 {return Err(error(&format!("top-width optimality violated for {style} k={k}")));}
        }
    }
    if can_upgrade_external(RootClaim::SamePublisher,true,true,true) ||
       can_upgrade_external(RootClaim::UnattestedOtherPublisher,true,true,true) {
        return Err(error("authority gate falsely promotes same/unattested source"));
    }
    let mut csv=File::create(Path::new(out).join("mqr495-target-audit-intervals.csv"))?;
    writeln!(csv,"strategy,observed_sites,total_target_sites,lower,upper,width,oracle,positive_observed,source_root_status")?;
    let mut summary=File::create(Path::new(out).join("mqr495-source-risk-witness.txt"))?;
    writeln!(summary,"MQR495_STATE=REAL_ORIGINAL_SOURCE_FINITE_TARGET_AUDIT")?;
    writeln!(summary,"ORIGINAL_PUBLISHER_ROOT={SOURCE_ROOT}")?;
    writeln!(summary,"ORIGINAL_CSV_GIT_BLOB_SHA1={ORIGINAL_BLOB}")?;
    writeln!(summary,"MQR495_RAW_ROWS={raw_rows}")?;
    writeln!(summary,"MQR495_ELIGIBLE_ROWS={}",frame.len())?;
    writeln!(summary,"MQR495_UNIQUE_WEST_SITES={}",west.len())?;
    writeln!(summary,"MQR495_UNIQUE_EAST_SITES={}",east.len())?;
    writeln!(summary,"MQR495_SOURCE_FIT=512 SOURCE_G=64 TARGET_P=64")?;
    writeln!(summary,"MQR495_MODEL=RUST_SOURCE_ONLY_GD_LOGISTIC_F19_EPOCHS{EPOCHS}_STEP{STEP}_RIDGE{RIDGE}")?;
    writeln!(summary,"MQR495_SEAL=TARGET_LABELS_READ_AFTER_SCORES_AND_ALL_AUDIT_ORDERS")?;
    writeln!(summary,"MQR495_NO_EXTERNAL_ROOT=TRUE; MQR495_NO_DESIGN_RANDOMIZED_CI=TRUE")?;
    writeln!(summary,"MQR495_TARGET_LABELS_POSTHOC_POSITIVE={}",ys.iter().filter(|&&x|x==1).count())?;
    writeln!(summary,"MQR495_ORACLE_REALIZED_LOGLOSS={oracle:.12}")?;
    writeln!(summary,"MQR495_UNLABELED_SHARP_CONVEX_HULL=[{:.12},{:.12}] WIDTH={:.12}",unlabelled.lower,unlabelled.upper,unlabelled.width())?;
    for (style,order) in strategies {
        for &k in &BUDGETS {
            let b=observed_bound(&pairs,&ys,&order[..k]);
            let observed_positive=order[..k].iter().filter(|&&i|ys[i]==1).count();
            writeln!(csv,"{style},{k},64,{:.12},{:.12},{:.12},{:.12},{observed_positive},SAME_PUBLISHER",
                 b.lower,b.upper,b.width(),oracle)?;
            println!("MQR495_AUDIT=policy:{style} k:{k} lower:{:.9} upper:{:.9} width:{:.9} oracle:{:.9}",
                     b.lower,b.upper,b.width(),oracle);
        }
    }
    println!("MQR495_ORIGINAL_SOURCE_AUDIT=PASS");
    println!("MQR495_INDEPENDENT_CALIBRATION_WITNESS=HOLD");
    println!("MQR495_DESIGN_BASED_POPULATION_CI=HOLD");
    Ok(())
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn source_same_or_unattested_not_external() {
        assert!(!can_upgrade_external(RootClaim::SamePublisher,true,true,true));
        assert!(!can_upgrade_external(RootClaim::UnattestedOtherPublisher,true,true,true));
        assert!(!can_upgrade_external(RootClaim::IndependentlyAttested,true,false,true));
        assert!(!can_upgrade_external(RootClaim::IndependentlyAttested,false,true,true));
        assert!(!can_upgrade_external(RootClaim::IndependentlyAttested,true,true,false));
        assert!(can_upgrade_external(RootClaim::IndependentlyAttested,true,true,true)); // mocked attested constructor, not real evidence
    }
    #[test] fn finite_label_bounds_exact_adversarial_worlds() {
        let p=[0.01,0.15,0.31,0.67,0.82,0.98];
        let loss:Vec<LossPair>=p.iter().map(|&v|LossPair::from_p(v)).collect();
        let known=[1usize,4usize];
        let actual=[0,1,1,0,0,1];
        let b=observed_bound(&loss,&actual,&known);
        let mut w_lo=actual;let mut w_hi=actual;
        for i in 0..p.len() {
            if !known.contains(&i){
                w_lo[i]=if loss[i].pos<=loss[i].neg {1}else{0};
                w_hi[i]=if loss[i].pos>=loss[i].neg {1}else{0};
            }
        }
        let risk=|w:[u8;6]|loss.iter().enumerate().map(|(i,q)|q.actual(w[i])).sum::<f64>()/6.;
        assert!((risk(w_lo)-b.lower).abs()<1e-12);
        assert!((risk(w_hi)-b.upper).abs()<1e-12);
        assert_eq!(w_lo[1],actual[1]);assert_eq!(w_hi[4],actual[4]);
        assert!((b.width()-loss.iter().enumerate().filter(|(i,_)|!known.contains(i)).map(|(_,q)|q.span()).sum::<f64>()/6.).abs()<1e-12);
    }
    #[test] fn equal_cost_top_width_is_exactly_optimal() {
        let p=[0.02,0.1,0.3,0.65,0.8,0.99];
        let pairs:Vec<LossPair>=p.iter().map(|&v|LossPair::from_p(v)).collect();
        let y=[0,1,0,1,1,0];
        let mut ranks=(0..6).collect::<Vec<_>>();
        ranks.sort_by(|&i,&j|pairs[j].span().total_cmp(&pairs[i].span()));
        for k in 0..=6{
            let best=observed_bound(&pairs,&y,&ranks[..k]).width();
            for mask in 0u8..64{
                if mask.count_ones() as usize==k{
                    let sel=(0..6).filter(|&i|mask&(1<<i)!=0).collect::<Vec<_>>();
                    assert!(best<=observed_bound(&pairs,&y,&sel).width()+1e-12);
                }
            }
        }
    }
    #[test] fn quoted_original_csv_header() {assert_eq!(headers(r#""lat","long","bio1""#), vec!["lat","long","bio1"]);}
    #[test] fn stable_fnv_source_selection() {assert_eq!(fnv(b"hello"),0xa430d84680aabd0b);}
}
