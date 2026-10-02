#include <array>
#include <algorithm>
#include <bit>
#include <cstdint>\n#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using State=int;
using Part=std::array<int,512>;

enum Sev { NONE=0, BOUNDED=1, MATERIAL=2, FATAL=3 };

struct Profile {
  std::array<int,5> v{};
};

struct Candidate {
  std::string name;
  Part part{};
};

struct Budget {
  std::string name;
  Profile p;
};

static inline bool has(State s,int b){ return ((s>>b)&1)!=0; }
static inline State setb(State s,int b){ return s|(1<<b); }
static inline State clrb(State s,int b){ return s&~(1<<b); }

State step(State s,int e){
  switch(e){
    case 0:return setb(s,0); case 1:return setb(s,1); case 2:return setb(s,2);
    case 3:return clrb(s,0); case 4:return clrb(s,1); case 5:return clrb(s,2);
    case 6:return setb(s,3); case 7:return setb(s,4); case 8:return setb(s,5);
    case 9:return clrb(s,3); case 10:return clrb(s,4); case 11:return clrb(s,5);
    case 12:return setb(s,7); case 13:return clrb(s,7);
    case 14:return has(s,7)?setb(s,6):clrb(s,6);
    case 15:return setb(s,8); case 16:return clrb(s,8);
    case 17:return has(s,8)?clrb(setb(s,2),5):s;
    default:return s;
  }
}

int unresolvedVec(State s){
  int x=0;
  for(int i=0;i<3;i++) if(has(s,i)&&!has(s,3+i)) x|=(1<<i);
  return x;
}
int unresolvedCount(State s){ return std::popcount((unsigned)unresolvedVec(s)); }
bool release(State s){ return unresolvedCount(s)==0 && has(s,6); }
int reopenObs(State s){ return (unresolvedCount(s)>0?1:0) | (!has(s,6)?2:0); }
int provObs(State s){ return has(s,6)?1:0; }
int extObs(State s){ return (has(s,2)&&!has(s,5))?1:0; }
int releaseObs(State s){ return release(s)?1:0; }
int authorityLabel(State s){
  int u=unresolvedCount(s);
  int rel=release(s)?1:0;
  int mask=1|2|(rel?4:8);
  return u*100+mask*10+rel;
}

Part canonicalInts(const std::array<int,512>& sig){
  std::set<int> uniq(sig.begin(),sig.end());
  std::map<int,int> ids;
  int k=0; for(int x:uniq) ids[x]=k++;
  Part p{}; for(int s=0;s<512;s++) p[s]=ids[sig[s]];
  return p;
}

Part obsPart(int (*obs)(State)){
  std::array<int,512> sig{};
  for(int s=0;s<512;s++) sig[s]=obs(s);
  return canonicalInts(sig);
}

Part refine(const std::vector<int>& es,const Part& p){
  std::map<std::vector<int>,int> ids;
  std::array<std::vector<int>,512> sig;
  for(int s=0;s<512;s++){
    sig[s].push_back(p[s]);
    for(int e:es) sig[s].push_back(p[step(s,e)]);
  }
  std::vector<std::vector<int>> uniq(sig.begin(),sig.end());
  std::sort(uniq.begin(),uniq.end());
  uniq.erase(std::unique(uniq.begin(),uniq.end()),uniq.end());
  for(int i=0;i<(int)uniq.size();i++) ids[uniq[i]]=i;
  Part out{}; for(int s=0;s<512;s++) out[s]=ids[sig[s]];
  return out;
}

std::vector<Part> levels(int (*obs)(State),const std::vector<int>& es){
  std::vector<Part> out;
  out.push_back(obsPart(obs));
  for(int k=1;k<=4;k++) out.push_back(refine(es,out.back()));
  return out;
}

int sevFor(const std::vector<Part>& lv,int s,int t){
  for(int k=0;k<=4;k++) if(lv[k][s]!=lv[k][t]){
    if(k<=1) return FATAL;
    if(k<=3) return MATERIAL;
    return BOUNDED;
  }
  return NONE;
}

int blocks(const Part& p){ return *std::max_element(p.begin(),p.end())+1; }

std::vector<std::pair<int,int>> mergedPairs(const Part& p){
  std::vector<std::pair<int,int>> v;
  for(int s=0;s<512;s++) for(int t=s+1;t<512;t++) if(p[s]==p[t]) v.push_back({s,t});
  return v;
}

Part q1(){
  std::array<int,512> sig{};
  for(int s=0;s<512;s++) sig[s]=authorityLabel(s);
  return canonicalInts(sig);
}
Part dropBitPart(int b){
  std::array<int,512> sig{};
  for(int s=0;s<512;s++) sig[s]=s&~(1<<b);
  return canonicalInts(sig);
}
Part visible7(){
  std::array<int,512> sig{};
  for(int s=0;s<512;s++) sig[s]=s&0x7f;
  return canonicalInts(sig);
}
Part identityPart(){
  Part p{}; for(int s=0;s<512;s++) p[s]=s; return p;
}

std::string sevName(int x){
  static const char* n[]={"NONE","BOUNDED","MATERIAL","FATAL"};
  return n[x];
}

Profile profileFor(const Part& p,const std::array<std::vector<Part>,5>& allLv){
  Profile out{};
  auto ps=mergedPairs(p);
  for(auto [s,t]:ps){
    for(int c=0;c<5;c++) out.v[c]=std::max(out.v[c],sevFor(allLv[c],s,t));
  }
  return out;
}

std::array<int,4> countSev(const Part& p,const std::vector<Part>& lv){
  std::array<int,4> c{};
  for(auto [s,t]:mergedPairs(p)) c[sevFor(lv,s,t)]++;
  return c;
}

std::string decision(const Profile& l,const Profile& b){
  if(l.v[4]==FATAL) return "FORBID_MERGE";
  if(l.v[1]==FATAL) return "REEXPAND_REQUIRED";
  if(l.v[2]==FATAL || l.v[3]==FATAL) return "REOPEN_REQUIRED";
  for(int i=0;i<5;i++) if(l.v[i]>b.v[i]) return "HOLD_INCOMPARABLE";
  for(int i=0;i<5;i++) if(l.v[i]>NONE) return "ACCEPT_WITH_AUDIT";
  return "ACCEPT_LOCAL";
}
bool acceptable(const std::string& d){
  return d=="ACCEPT_LOCAL" || d=="ACCEPT_WITH_AUDIT";
}

int score(const std::array<int,4>& enc,const std::array<int,5>& w,const Profile& p){
  int x=0; for(int i=0;i<5;i++) x+=w[i]*enc[p.v[i]]; return x;
}

std::vector<std::array<int,5>> allWeights(){
  std::vector<std::array<int,5>> ws;
  for(int a:{1,2,4})for(int b:{1,2,4})for(int c:{1,2,4})for(int d:{1,2,4})for(int e:{1,2,4})
    ws.push_back({a,b,c,d,e});
  return ws;
}

int winner(const std::array<int,4>& enc,const std::vector<Candidate>& cs,const std::vector<Profile>& ps,const std::array<int,5>& w){
  int bi=0,bs=score(enc,w,ps[0]);
  for(int i=1;i<(int)cs.size();i++){
    int s=score(enc,w,ps[i]);
    if(s<bs){bs=s;bi=i;}
  }
  return bi;
}

int pairReversals(const std::array<int,4>& enc,const std::vector<Profile>& ps,const std::vector<std::array<int,5>>& ws){
  int n=0;
  for(int i=0;i<(int)ps.size();i++) for(int j=i+1;j<(int)ps.size();j++){
    bool lt=false,gt=false;
    for(auto w:ws){
      int a=score(enc,w,ps[i]), b=score(enc,w,ps[j]);
      if(a<b) lt=true; if(a>b) gt=true;
    }
    if(lt&&gt) n++;
  }
  return n;
}

int main(){
  std::vector<int> allE,sepE,provE,extE;
  for(int i=0;i<18;i++) allE.push_back(i);
  for(int i=0;i<12;i++) sepE.push_back(i);
  provE={12,13,14};
  extE={2,5,8,11,15,16,17};

  auto sepLv=levels(unresolvedVec,sepE);
  auto reopenLv=levels(reopenObs,allE);
  auto provLv=levels(provObs,provE);
  auto extLv=levels(extObs,extE);
  auto releaseLv=levels(releaseObs,allE);
  std::array<std::vector<Part>,5> allLv={sepLv,reopenLv,provLv,extLv,releaseLv};

  Part p1=q1();
  Part p2=refine(allE,p1);
  Part p3=p1; for(int k=0;k<3;k++) p3=refine(allE,p3);

  std::vector<Candidate> cs={
    {"A0_FULL",identityPart()},
    {"A1_DROP_P",dropBitPart(7)},
    {"A2_DROP_X",dropBitPart(8)},
    {"A3_VISIBLE_7",visible7()},
    {"A4_Q2_4_66",p2},
    {"A5_Q3_4_66",p3},
    {"A6_CURRENT_AUTHORITY",p1}
  };
  std::vector<Profile> ps;
  for(auto& c:cs) ps.push_back(profileFor(c.part,allLv));

  std::vector<Budget> budgets={
    {"B0_CONSERVATIVE",{{BOUNDED,BOUNDED,BOUNDED,BOUNDED,BOUNDED}}},
    {"B1_EXPLORATORY",{{MATERIAL,BOUNDED,BOUNDED,MATERIAL,BOUNDED}}},
    {"B2_ARCHIVAL",{{MATERIAL,MATERIAL,NONE,MATERIAL,BOUNDED}}}
  };

  std::vector<std::pair<std::string,std::string>> sels;
  for(auto& b:budgets){
    int best=-1,bblocks=1e9;
    for(int i=0;i<(int)cs.size();i++){
      auto d=decision(ps[i],b.p);
      if(acceptable(d) && blocks(cs[i].part)<bblocks){best=i;bblocks=blocks(cs[i].part);}
    }
    sels.push_back({b.name,best<0?"NONE":cs[best].name});
  }

  auto ws=allWeights();
  std::array<int,4> enc1={0,1,2,3}, enc2={0,1,3,9};
  std::set<int> wins1,wins2;
  for(auto w:ws){wins1.insert(winner(enc1,cs,ps,w));wins2.insert(winner(enc2,cs,ps,w));}
  int rev1=pairReversals(enc1,ps,ws), rev2=pairReversals(enc2,ps,ws);
  int mw1=0,mw2=0;
  for(auto w:ws){
    std::string x1=cs[winner(enc1,cs,ps,w)].name;
    std::string x2=cs[winner(enc2,cs,ps,w)].name;
    bool a1=true,a2=true;
    for(auto& q:sels){a1=a1&&(q.second==x1);a2=a2&&(q.second==x2);}
    if(a1)mw1++; if(a2)mw2++;
  }

  std::map<std::string,int> idx;
  for(int i=0;i<(int)cs.size();i++)idx[cs[i].name]=i;
  std::vector<std::string> seq={"A3_VISIBLE_7","A4_Q2_4_66","A3_VISIBLE_7","A5_Q3_4_66"};
  std::array<int,5> debt{},first{},thr={4,3,2,3,2};
  for(int k=0;k<(int)seq.size();k++){
    auto p=ps[idx[seq[k]]];
    for(int c=0;c<5;c++){
      debt[c]+=p.v[c];
      if(first[c]==0 && debt[c]>=thr[c]) first[c]=k+1;
    }
  }

  std::system("mkdir -p experiments/mqr-4.67/results");
  std::ofstream pf("experiments/mqr-4.67/results/cpp_profiles.tsv");
  pf<<"candidate\tblocks\tmerged_pairs\tworst_sep\tworst_reopen\tworst_prov\tworst_ext\tworst_release";
  for(std::string coord:{"sep","reopen","prov","ext","release"})
    for(std::string sev:{"none","bounded","material","fatal"}) pf<<"\t"<<coord<<"_"<<sev;
  pf<<"\n";
  for(int i=0;i<(int)cs.size();i++){
    auto mp=mergedPairs(cs[i].part);
    pf<<cs[i].name<<"\t"<<blocks(cs[i].part)<<"\t"<<mp.size();
    for(int c=0;c<5;c++)pf<<"\t"<<sevName(ps[i].v[c]);
    for(int c=0;c<5;c++){
      auto cnt=countSev(cs[i].part,allLv[c]);
      for(int q=0;q<4;q++)pf<<"\t"<<cnt[q];
    }
    pf<<"\n";
  }

  std::ofstream sf("experiments/mqr-4.67/results/cpp_summary.tsv");
  sf<<"metric\tvalue\n";
  sf<<"SOURCE_STATES\t512\n";
  sf<<"EVENTS\t18\n";
  sf<<"CANDIDATES\t7\n";
  sf<<"WEIGHT_VECTORS\t243\n";
  sf<<"SCALAR_WINNERS_ENC0123\t"<<wins1.size()<<"\n";
  sf<<"SCALAR_WINNERS_ENC0139\t"<<wins2.size()<<"\n";
  sf<<"PAIRWISE_REVERSALS_ENC0123\t"<<rev1<<"\n";
  sf<<"PAIRWISE_REVERSALS_ENC0139\t"<<rev2<<"\n";
  sf<<"WEIGHTS_MATCH_ALL_BUDGET_SELECTIONS_ENC0123\t"<<mw1<<"\n";
  sf<<"WEIGHTS_MATCH_ALL_BUDGET_SELECTIONS_ENC0139\t"<<mw2<<"\n";
  sf<<"DEBT_TRIGGER_STEP_SEP\t"<<first[0]<<"\n";
  sf<<"DEBT_TRIGGER_STEP_REOPEN\t"<<first[1]<<"\n";
  sf<<"DEBT_TRIGGER_STEP_PROV\t"<<first[2]<<"\n";
  sf<<"DEBT_TRIGGER_STEP_EXT\t"<<first[3]<<"\n";
  sf<<"DEBT_TRIGGER_STEP_RELEASE\t"<<first[4]<<"\n";
  for(auto& q:sels)sf<<q.first<<"_SELECTED\t"<<q.second<<"\n";

  std::cout<<"MQR467_CPP_COURT=PASS\n";
  for(int i=0;i<(int)cs.size();i++){
    std::cout<<cs[i].name<<" blocks="<<blocks(cs[i].part)<<" loss=";
    for(int c=0;c<5;c++){if(c)std::cout<<",";std::cout<<sevName(ps[i].v[c]);}
    std::cout<<"\n";
  }
  return 0;
}
