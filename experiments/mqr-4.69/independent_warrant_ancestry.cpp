#include <algorithm>
#include <array>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
using Row=std::map<std::string,std::string>;

std::vector<std::string> split(const std::string&s){
  std::vector<std::string> out; std::stringstream ss(s); std::string x;
  while(std::getline(ss,x,'\t')) out.push_back(x);
  return out;
}
std::vector<Row> read_tsv(const std::string&path){
  std::ifstream in(path); if(!in) throw std::runtime_error("open failed: "+path);
  std::string line; std::getline(in,line); auto hdr=split(line);
  std::vector<Row> rows;
  while(std::getline(in,line)){ if(line.empty()) continue; auto xs=split(line); Row r;
    for(size_t i=0;i<hdr.size();++i) r[hdr[i]]= i<xs.size()?xs[i]:"";
    rows.push_back(r);
  }
  return rows;
}
const std::array<std::string,4> FEATURES={"authorization_state","provenance_state","defeater_state","revision_state"};

std::string transition(const std::string&u,const Row&f){
  auto a=f.at("authorization_state"), p=f.at("provenance_state"), d=f.at("defeater_state"), r=f.at("revision_state");
  if(u=="AUTHORIZATION_CHECK"){
    return (a=="RETROSPECTIVE"||a=="UNAUTHORIZED") ? "HOLD_REAUTHORIZE" : "STABLE";
  }
  if(u=="REVISION_REPLAY"){
    if(a=="RETROSPECTIVE") return "REOPEN_REQUIRED";
    if(r=="REASON_MUTATION") return "HOLD_REASON_RECONSTITUTE";
    return "STABLE";
  }
  if(u=="WITHDRAW_ANCESTRY_SUPPORT"||u=="REPRODUCE_UNDER_INDEPENDENT_ANCESTRY")
    return p=="COMMON_MODE_SINGLE_ROOT" ? "REOPEN_REQUIRED" : "STABLE";
  if(u=="REOPEN_WITH_HELD_OUT_DEFEATER")
    return d=="SURVIVED_D1" ? "STABLE" : "REOPEN_REQUIRED";
  if(u=="REOPEN_WITH_HELD_OUT_DEFEATER_D3") return "REOPEN_REQUIRED";
  if(u=="COUNTERFACTUAL_RECONSTITUTION")
    return r=="REVERSAL" ? "REOPEN_REQUIRED" : "STABLE";
  if(u=="AUDIT_SOURCE"||u=="SCOPE_EXPANSION") return "STABLE";
  throw std::runtime_error("unknown intervention: "+u);
}
std::string relation(const std::string&a,const std::string&b){return a==b?"FUNGIBLE":"SEPARATES";}

std::string key_for(const Row&p,const Row&f,const std::vector<int>&idx){
  std::string k=p.at("present_surface_hash")+"|"+p.at("intervention");
  for(int i:idx) k+="|"+f.at(FEATURES[i]);
  return k;
}
bool sufficient(const std::vector<Row>&pairs,const std::map<std::string,Row>&schema,const std::vector<int>&idx){
  std::map<std::string,std::string> seen;
  for(auto&p:pairs) for(std::string side:{"A","B"}){
    auto &f=schema.at(p.at("ancestry_"+side));
    auto k=key_for(p,f,idx), y=p.at("expected_"+side);
    auto it=seen.find(k);
    if(it!=seen.end() && it->second!=y) return false;
    seen[k]=y;
  }
  return true;
}
std::vector<std::vector<int>> minimal_sets(const std::vector<Row>&pairs,const std::map<std::string,Row>&schema){
  for(int n=0;n<=4;n++){
    std::vector<std::vector<int>> out;
    for(int mask=0;mask<16;mask++){
      if(__builtin_popcount((unsigned)mask)!=n) continue;
      std::vector<int> idx; for(int i=0;i<4;i++) if(mask&(1<<i)) idx.push_back(i);
      if(sufficient(pairs,schema,idx)) out.push_back(idx);
    }
    if(!out.empty()) return out;
  }
  return {};
}
int main(int argc,char**argv){
  std::string pairpath=argc>1?argv[1]:"experiments/mqr-4.69/PAIR-FREEZE.tsv";
  std::string schemapath=argc>2?argv[2]:"experiments/mqr-4.69/ANCESTRY-FEATURES.tsv";
  auto pairs=read_tsv(pairpath), srows=read_tsv(schemapath);
  std::map<std::string,Row> schema; for(auto&r:srows) schema[r["ancestry"]]=r;

  int mismatch=0, leakage=0, swapfail=0, separated=0, fungible=0;
  std::map<std::string,int> bc;
  std::vector<std::array<std::string,6>> results;

  for(auto&p:pairs){
    if(!schema.count(p["ancestry_A"])||!schema.count(p["ancestry_B"])){std::cerr<<"schema missing\n";return 2;}
    auto fa=schema[p["ancestry_A"]], fb=schema[p["ancestry_B"]];
    auto ya=transition(p["intervention"],fa), yb=transition(p["intervention"],fb), rel=relation(ya,yb);
    mismatch += ya!=p["expected_A"] || yb!=p["expected_B"] || rel!=p["expected_pair_relation"];
    leakage += p["present_surface_hash"].empty() || p["current_rule"].empty() || p["current_verdict"].empty();
    if(p["causal_swap"]=="YES"){
      auto sa=transition(p["intervention"],fb), sb=transition(p["intervention"],fa);
      swapfail += sa!=yb || sb!=ya;
    }
    separated += rel=="SEPARATES"; fungible += rel=="FUNGIBLE"; bc[p["baseline_probe"]]++;
    results.push_back({p["pair_id"],ya,yb,rel,p["control_type"],p["baseline_probe"]});
  }

  auto mins=minimal_sets(pairs,schema);
  std::filesystem::create_directories("experiments/mqr-4.69/results");
  std::ofstream o("experiments/mqr-4.69/results/cpp_results.tsv");
  o<<"pair_id\toutcome_A\toutcome_B\trelation\tcontrol_type\tbaseline_probe\n";
  for(auto&r:results) o<<r[0]<<"\t"<<r[1]<<"\t"<<r[2]<<"\t"<<r[3]<<"\t"<<r[4]<<"\t"<<r[5]<<"\n";

  std::ofstream m("experiments/mqr-4.69/results/cpp_minimal_feature_sets.tsv");
  m<<"rank\tfeature_count\tfeatures\n";
  for(size_t j=0;j<mins.size();j++){
    m<<j+1<<"\t"<<mins[j].size()<<"\t";
    if(mins[j].empty()) m<<"<EMPTY>";
    else for(size_t z=0;z<mins[j].size();z++){ if(z)m<<","; m<<FEATURES[mins[j][z]]; }
    m<<"\n";
  }

  std::ofstream s("experiments/mqr-4.69/results/cpp_summary.tsv");
  s<<"metric\tvalue\n";
  s<<"PAIRS\t"<<pairs.size()<<"\n";
  s<<"EXPECTATION_MISMATCHES\t"<<mismatch<<"\n";
  s<<"PRESENT_SURFACE_LEAKAGE\t"<<leakage<<"\n";
  s<<"CAUSAL_SWAP_FAILURES\t"<<swapfail<<"\n";
  s<<"SEPARATING_PAIRS\t"<<separated<<"\n";
  s<<"FUNGIBLE_PAIRS\t"<<fungible<<"\n";
  s<<"MINIMAL_FEATURE_COUNT\t"<<(mins.empty()?-1:(int)mins[0].size())<<"\n";
  s<<"MINIMAL_FEATURE_SET_COUNT\t"<<mins.size()<<"\n";
  for(auto&[k,v]:bc)s<<"BASELINE_"<<k<<"\t"<<v<<"\n";

  if(mismatch||leakage||swapfail||mins.empty()){
    std::cout<<"MQR469_CPP_COURT=FAIL\n"; return 1;
  }
  std::cout<<"MQR469_CPP_COURT=PASS\n";
  std::cout<<"MQR469_MINIMAL_FEATURE_COUNT="<<mins[0].size()<<"\n";
  return 0;
}
