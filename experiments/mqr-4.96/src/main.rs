//! Original 2024 GBIF source-label provenance, geographic coordinate-uncertainty,
//! and coarse geographic/year overlap. Rust std only, no causal significance claim.
use std::{collections::{BTreeMap,BTreeSet},env,fs::{self,File},io::{BufRead,BufReader,Write},error::Error,path::Path};
const SPRING:&str="acf9b46d-e71a-4ccb-91d2-a021ffda4dd4";
const KASTIKKA:&str="f2e389da-39c3-4f21-8d72-b7d574d924a9";
type ResultX<T>=Result<T,Box<dyn Error>>;
fn fail(x:impl Into<String>)->Box<dyn Error>{
 std::io::Error::new(std::io::ErrorKind::InvalidData,x.into()).into()
}
#[derive(Clone,Copy,Default,Debug)]struct Table{n:u64,absent:u64,spring:u64,spring_absent:u64}
impl Table{
 fn add(&mut self,s:bool,negative:bool){
   self.n+=1;self.absent+=negative as u64;self.spring+=s as u64;
   self.spring_absent+=(s&&negative) as u64;
 }
 fn present(self)->u64{self.n-self.absent}
 fn other(self)->u64{self.n-self.spring}
}
#[derive(Clone,Copy,Default)]struct Uncertainty{missing:u64,lt1:u64,from1to10:u64,from10to100:u64,atleast100:u64}
impl Uncertainty{
 fn add(&mut self,x:Option<f64>){
   match x {
      Some(v) if v.is_finite()&&v>=100000.0=>self.atleast100+=1,
      Some(v) if v.is_finite()&&v>=10000.0=>self.from10to100+=1,
      Some(v) if v.is_finite()&&v>=1000.0=>self.from1to10+=1,
      Some(v) if v.is_finite()&&v>=0.0=>self.lt1+=1,
      _=>self.missing+=1
   }
 }
 fn all(self)->u64{self.missing+self.lt1+self.from1to10+self.from10to100+self.atleast100}
}
#[derive(Clone,Copy,Default)]struct SourceStat{table:Table,uncertainty:Uncertainty}
struct Record{
 dataset:String,negative:bool,lat:Option<f64>,lon:Option<f64>,year:Option<i32>,unc:Option<f64>
}
fn field(header:&[&str],s:&str)->ResultX<usize>{header.iter().position(|&x|x==s).ok_or_else(||fail(format!("original source missing field {s}")))}
fn parse_opt(v:&str)->Option<f64>{
 let v=v.trim();
 if v.is_empty()||v=="NA" {return None;}
 v.parse::<f64>().ok().filter(|x|x.is_finite())
}
fn parse(path:&str)->ResultX<(Vec<Record>,BTreeMap<String,SourceStat>,BTreeMap<(bool,bool),Uncertainty>)>{
 let mut lines=BufReader::new(File::open(path)?).lines();
 let h=lines.next().ok_or_else(||fail("empty GBIF source"))??;
 let header:Vec<&str>=h.trim_end_matches('\r').split('\t').collect();
 let fkeys=["gbifID","datasetKey","occurrenceStatus","decimalLatitude","decimalLongitude","year","coordinateUncertaintyInMeters"];
 let indices=fkeys.map(|x|field(&header,x)).into_iter().collect::<ResultX<Vec<_>>>()?;
 let mut ids=BTreeSet::new();let mut rows=Vec::new();
 let mut source=BTreeMap::<String,SourceStat>::new();
 let mut ugroup=BTreeMap::<(bool,bool),Uncertainty>::new();
 for (line_no,l) in lines.enumerate(){
  let l=l?;
  let items=l.trim_end_matches('\r').split('\t').collect::<Vec<_>>();
  if items.len()!=header.len(){return Err(fail(format!("GBIF original TSV invalid field count at row {}",line_no+2)));}
  let [id,src,status,lat,lon,year,unc]=indices.map(|i|items[i]);
  if id.is_empty()||src.is_empty(){return Err(fail("missing GBIF id or dataset provenance"));}
  if !ids.insert(id.to_owned()){return Err(fail("reused original gbifID"));}
  let negative=match status{"ABSENT"=>true,"PRESENT"=>false,_=>return Err(fail("unsupported original occurrence status"))};
  let spring=src==SPRING;
  let u=parse_opt(unc);
  let e=source.entry(src.to_owned()).or_default();
  e.table.add(spring,negative);e.uncertainty.add(u);
  ugroup.entry((spring,negative)).or_default().add(u);
  let yr=year.parse::<i32>().ok().filter(|&v|(2000..=2024).contains(&v));
  rows.push(Record{dataset:src.into(),negative,lat:parse_opt(lat),lon:parse_opt(lon),year:yr,unc:u});
 }
 if rows.len()!=29543||ids.len()!=29543||source.len()!=27{
    return Err(fail(format!("2024 exact source count mismatch rows={} unique ids={} sources={}",rows.len(),ids.len(),source.len())));
 }
 Ok((rows,source,ugroup))
}
fn entropy(positive:f64)->f64{
 if positive<=0.0||positive>=1.0{0.0}else{-positive*positive.log2()-(1.0-positive)*(1.0-positive).log2()}
}
fn bin(r:&Record,deg:f64,yrs:i32)->Option<(i32,i32,i32)>{
 let (lat,lon,year)=(r.lat?,r.lon?,r.year?);
 if !(-90.0..=90.0).contains(&lat)||!(-180.0..=180.0).contains(&lon){return None;}
 Some(((lat/deg).floor() as i32,(lon/deg).floor() as i32,(year-2000)/yrs))
}
#[derive(Default)]struct Overlap{
 strata_total:usize,strata_both:usize,n_both:u64,spring_both:u64,other_both:u64,
 actual_spring_negative:u64,all_negative:u64,expected_spring_negative:f64,unbinned:u64,
 original_source_spring_in_overlap:u64
}
fn overlap(rows:&[Record],deg:f64,years:i32)->Overlap{
 let mut groups=BTreeMap::<(i32,i32,i32),Table>::new();
 let mut out=Overlap::default();
 for r in rows {
  if let Some(key)=bin(r,deg,years){
    groups.entry(key).or_default().add(r.dataset==SPRING,r.negative);
  }else{out.unbinned+=1;}
 }
 out.strata_total=groups.len();
 for g in groups.values(){
  if g.spring>0&&g.other()>0{
   out.strata_both+=1;out.n_both+=g.n;out.spring_both+=g.spring;out.other_both+=g.other();
   out.actual_spring_negative+=g.spring_absent;out.all_negative+=g.absent;
   out.expected_spring_negative+=g.spring as f64 * g.absent as f64/g.n as f64;
  }
 }
 out
}
fn report(rows:&[Record], source:&BTreeMap<String,SourceStat>,
    unc:&BTreeMap<(bool,bool),Uncertainty>,out:&str)->ResultX<()>{
 let n=rows.len() as u64; let mut all=Table::default();
 for r in rows{all.add(r.dataset==SPRING,r.negative);}
 let spring=source.get(SPRING).ok_or_else(||fail("Spring source missing"))?;
 let kastikka=source.get(KASTIKKA).ok_or_else(||fail("Kastikka source missing"))?;
 if spring.table.n!=14651||spring.table.absent!=11165||
    kastikka.table.n!=9686||kastikka.table.absent!=0||
    all.absent!=11166||all.present()!=18377||all.spring!=14651{
      return Err(fail("historical 2024 source label count drift"));
 }
 let mut group_unc=BTreeMap::<bool,Uncertainty>::new();
 for r in rows{group_unc.entry(r.dataset==SPRING).or_default().add(r.unc);}
 let s_unc=*group_unc.get(&true).unwrap();
 if s_unc.lt1>0||s_unc.missing>0||s_unc.atleast100!=4010 {
   return Err(fail("observed Spring location uncertainty distribution drift"));
 }
 fs::create_dir_all(out)?;
 let mut dataset=File::create(Path::new(out).join("mqr496-original-27-dataset-source-support.tsv"))?;
 writeln!(dataset,"datasetKey\tABSENT\tPRESENT\tTOTAL\tcoord_lt1km\tcoord_1to10km\tcoord_10to100km\tcoord_ge100km\tcoord_missing")?;
 let mut n_zero_only=0;let mut n_one_only=0;let mut n_two=0;
 for (k,e) in source{
  let t=e.table;let u=e.uncertainty;
  writeln!(dataset,"{k}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}",t.absent,t.present(),t.n,u.lt1,u.from1to10,u.from10to100,u.atleast100,u.missing)?;
  if t.absent==0{n_one_only+=1;}else if t.present()==0{n_zero_only+=1;}else{n_two+=1;}
 }
 let mut spatial=File::create(Path::new(out).join("mqr496-original-source-by-label-geouncertainty.tsv"))?;
 writeln!(spatial,"isSpring\tisAbsent\tTOTAL\tlt1km\t1to10km\t10to100km\tge100km\tmissing")?;
 for((s,y),u)in unc{
  writeln!(spatial,"{s}\t{y}\t{}\t{}\t{}\t{}\t{}\t{}",u.all(),u.lt1,u.from1to10,u.from10to100,u.atleast100,u.missing)?;
 }
 let base_majority=all.present().max(all.absent);
 let source_majority=spring.table.absent.max(spring.table.present())+
   (all.present()-spring.table.present()).max(all.absent-spring.table.absent);
 let correct_negative=spring.table.absent; // Spring classified absent.
 let correct_positive=all.present()-spring.table.present(); // others classified present.
 let balanced=(correct_negative as f64 / all.absent as f64
              + correct_positive as f64 / all.present() as f64)/2.0;
 let total_h=entropy(all.present()as f64/n as f64);
 let hs=spring.table.n as f64/n as f64*entropy(spring.table.present() as f64/spring.table.n as f64)
   + (n-spring.table.n)as f64/n as f64*
     entropy((all.present()-spring.table.present()) as f64/(n-spring.table.n)as f64);
 let mut h27=0.0;
 for e in source.values(){h27+=e.table.n as f64/n as f64*entropy(e.table.present() as f64/e.table.n as f64);}
 let mut s=String::new();
 s.push_str("MQR496_ORIGINAL_GBIF_ROOT=0031144-240626123714530\n");
 s.push_str("MQR496_ORIGINAL_27_SOURCES_29543_ROWS=PASS\n");
 s.push_str(&format!("MQR496_ABSENT={} PRESENT={} SPRING_ABSENT={} OTHER_ABSENT={}\n",all.absent,all.present(),spring.table.absent,all.absent-spring.table.absent));
 s.push_str(&format!("MQR496_ORIGINAL_SOURCE_CLASS_SUPPORT=NO_NEGATIVE:{} NO_POSITIVE:{} BOTH:{}\n",n_one_only,n_zero_only,n_two));
 s.push_str(&format!("MQR496_SOURCE_ONLY_IN_SAMPLE_ACCURACY={:.9} BASE_MAJORITY_ACCURACY={:.9} BALANCED_ACCURACY={:.9}\n",
    source_majority as f64/n as f64,base_majority as f64/n as f64,balanced));
 s.push_str(&format!("MQR496_INFORMATION_H_Y_BITS={total_h:.9} H_Y_GIVEN_SPRING_BINARY={hs:.9} H_Y_GIVEN_27_SOURCE={h27:.9} MI_SPRING_BITS={:.9} MI_ALL_SOURCE_BITS={:.9}\n",
    total_h-hs,total_h-h27));
 for (group,u) in &group_unc {
  s.push_str(&format!("MQR496_COORD_UNCERTAINTY_SPRING_{}=LT1KM:{} 1TO10KM:{} 10TO100KM:{} GE100KM:{} MISSING:{}\n",
   group,u.lt1,u.from1to10,u.from10to100,u.atleast100,u.missing));
 }
 for (tag,deg,years) in [("PRIMARY_1DEG_3YR",1.0,3),("SENSITIVITY_2DEG_5YR",2.0,5)]{
  let o=overlap(rows,deg,years);
  if o.n_both==0{return Err(fail(format!("{tag}: zero common geographic/year strata; descriptive contrast infeasible")));}
  s.push_str(&format!("MQR496_STRATIFIED_{tag}=STRATA_TOTAL:{} STRATA_BOTH:{} ROWS_BOTH:{} SPRING_ROWS_BOTH:{} OTHER_ROWS_BOTH:{} OBSERVED_SPRING_ABSENT:{} EXPECTED_SPRING_ABSENT_IF_CONDITIONAL_EXCHANGEABLE:{:.6} DIFFERENCE:{:.6} UNBINNED:{}\n",
   o.strata_total,o.strata_both,o.n_both,o.spring_both,o.other_both,
   o.actual_spring_negative,o.expected_spring_negative,
   o.actual_spring_negative as f64-o.expected_spring_negative,o.unbinned));
 }
 s.push_str("MQR496_SOURCE_LABEL_ASSOCIATION=PASS_DESCRIPTIVE_NOT_CAUSAL\n");
 s.push_str("MQR496_FINE_SITE_GEOGRAPHIC_AUTHORITY=HOLD_COORDINATE_UNCERTAINTY\n");
 s.push_str("MQR496_SPATIAL_STRATIFICATION_INFERENCE=HOLD_NONRANDOM_SOURCE_AND_CLUSTERED_SAMPLING\n");
 s.push_str("MQR496_SOURCE_CONDITIONAL_FINLAND_POPULATION_TRANSPORT=HOLD_NO_PROTOCOL_BRIDGE\n");
 File::create(Path::new(out).join("mqr496-source-semantics-verdict.txt"))?.write_all(s.as_bytes())?;
 print!("{s}");
 Ok(())
}
fn main()->ResultX<()>{
 let args=env::args().collect::<Vec<_>>();
 if args.len()!=3{return Err(fail("usage: mqr496-source-semantics ORIGINAL_2024_GBIF_TSV OUTPUT_DIR"));}
 let(rows,sources,unc)=parse(&args[1])?;
 report(&rows,&sources,&unc,&args[2])
}
#[cfg(test)]
mod tests{
 use super::*;
 #[test]fn zero_entropy_at_constant_label(){assert_eq!(entropy(0.0),0.0);assert_eq!(entropy(1.0),0.0);assert!((entropy(0.5)-1.0).abs()<1e-12);}
 #[test]fn missing_uncertainty_is_not_zero(){let mut u=Uncertainty::default();u.add(None);u.add(Some(0.0));u.add(Some(100000.0));u.add(Some(9999.0));assert_eq!((u.missing,u.lt1,u.from1to10,u.atleast100),(1,1,1,1));}
 #[test]fn original_geographic_time_bin_rounding(){let r=Record{dataset:SPRING.into(),negative:false,lat:Some(60.999),lon:Some(24.0),year:Some(2024),unc:None};assert_eq!(bin(&r,1.0,3),Some((60,24,8)));assert_eq!(bin(&r,2.0,5),Some((30,12,4)));}
 #[test]fn coarsened_stratum_with_one_source_no_overlap(){let rows=vec![
  Record{dataset:SPRING.into(),negative:true,lat:Some(60.5),lon:Some(24.5),year:Some(2020),unc:Some(100000.0)},
  Record{dataset:"other".into(),negative:false,lat:Some(60.5),lon:Some(24.5),year:Some(2020),unc:Some(300.0)},
  Record{dataset:"other".into(),negative:false,lat:Some(65.5),lon:Some(24.5),year:Some(2020),unc:Some(300.0)}];
  let o=overlap(&rows,1.0,3);assert_eq!((o.strata_total,o.strata_both,o.n_both,o.unbinned),(2,1,2,0));assert!((o.expected_spring_negative-0.5).abs()<1e-12);
 }
 #[test]fn unknown_year_is_not_silently_imputed(){let r=Record{dataset:SPRING.into(),negative:true,lat:Some(60.5),lon:Some(24.5),year:None,unc:None};assert!(bin(&r,1.0,3).is_none());}
}
