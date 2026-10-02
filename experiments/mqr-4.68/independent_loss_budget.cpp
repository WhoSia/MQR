#include <array>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using Row=std::map<std::string,std::string>;

std::vector<std::string> split(const std::string&s){
  std::vector<std::string> out; std::stringstream ss(s); std::string x;
  while(std::getline(ss,x,'\t')) out.push_back(x); return out;
}
int sev(const std::string&s){
  if(s=="NONE")return 0; if(s=="BOUNDED")return 1; if(s=="MATERIAL")return 2; return 3;
}
std::string decision(const Row&r){
  if(r.at("warrant_complete")!="YES") return "HOLD_WARRANT_OPEN";
  if(r.at("transport_valid")!="YES") return "HOLD_TRANSPORT";
  if(r.at("revision_requested")=="YES") return r.at("revision_authorized")=="YES"?"REVISION_AUTHORIZED":"REVISION_FORBIDDEN";
  if(r.at("loss_release")=="FATAL") return "FORBID_MERGE";
  if(r.at("reopening_trigger")=="YES") return "REEXPAND_REQUIRED";
  std::map<std::string,std::array<int,5>> C{
    {"exploratory",{2,1,1,2,1}},
    {"audit",{1,2,1,1,1}},
    {"public_release",{1,1,1,1,0}},
    {"cross_domain",{1,1,1,1,1}}
  };
  auto c=C.at(r.at("context"));
  std::array<int,5> v{sev(r.at("loss_sep")),sev(r.at("loss_reopen")),sev(r.at("loss_prov")),sev(r.at("loss_ext")),sev(r.at("loss_release"))};
  if(v[1]==3) return "REEXPAND_REQUIRED";
  if(v[2]==3||v[3]==3) return "REOPEN_REQUIRED";
  for(int i=0;i<5;i++) if(v[i]>c[i]) return "HOLD_CONTEXT_CEILING";
  for(int i=0;i<5;i++) if(v[i]>0) return "ACCEPT_WITH_AUDIT";
  return "ACCEPT_LOCAL";
}
std::string baseline(const Row&r){
  if(r.at("scalar_warrant")=="INDEPENDENT") return "UTILITY_RECOVERY_CONTROL";
  if(r.at("revision_requested")=="YES") return "PREFERENCE_REVISION_BASELINE";
  if(r.at("loss_release")=="FATAL"||r.at("reopening_trigger")=="YES") return "HARD_CONSTRAINT_EQUIVALENT";
  if(r.at("transport_valid")!="YES") return "PARTIAL_ORDER_BASELINE";
  if(r.at("scalar_representation")=="YES") return "REPRESENTATION_ONLY";
  return "NO_BASELINE_MATCH";
}
int main(int argc,char**argv){
  std::string path=argc>1?argv[1]:"experiments/mqr-4.68/COURT-FREEZE.tsv";
  std::ifstream in(path); if(!in){std::cerr<<"open failed\n";return 2;}
  std::string line; std::getline(in,line); auto hdr=split(line);
  std::vector<Row> rows;
  while(std::getline(in,line)){ if(line.empty())continue; auto xs=split(line); Row r; for(size_t i=0;i<hdr.size();i++)r[hdr[i]]=xs[i]; rows.push_back(r); }
  std::filesystem::create_directories("experiments/mqr-4.68/results");
  std::ofstream out("experiments/mqr-4.68/results/cpp_results.tsv");
  out<<"case\tdecision\tbaseline\n";
  int mismatch=0, utility=0, repr=0, hard=0, pref=0, transport=0, posthoc=0;
  for(auto&r:rows){
    auto d=decision(r), b=baseline(r); out<<r["case"]<<"\t"<<d<<"\t"<<b<<"\n";
    if(d!=r["expected_decision"]||b!=r["expected_baseline"])mismatch++;
    utility+=b=="UTILITY_RECOVERY_CONTROL"; repr+=b=="REPRESENTATION_ONLY";
    hard+=b=="HARD_CONSTRAINT_EQUIVALENT"; pref+=b=="PREFERENCE_REVISION_BASELINE";
    transport+=d=="HOLD_TRANSPORT"; posthoc+=d=="REVISION_FORBIDDEN";
  }
  std::ofstream s("experiments/mqr-4.68/results/cpp_summary.tsv");
  s<<"metric\tvalue\n";
  s<<"CASES\t"<<rows.size()<<"\n";
  s<<"EXPECTATION_MISMATCHES\t"<<mismatch<<"\n";
  s<<"UTILITY_RECOVERY_CONTROLS\t"<<utility<<"\n";
  s<<"REPRESENTATION_ONLY_CASES\t"<<repr<<"\n";
  s<<"HARD_CONSTRAINT_EQUIVALENT_CASES\t"<<hard<<"\n";
  s<<"PREFERENCE_REVISION_BASELINE_CASES\t"<<pref<<"\n";
  s<<"TRANSPORT_HOLDS\t"<<transport<<"\n";
  s<<"POSTHOC_REVISION_FORBIDDEN\t"<<posthoc<<"\n";
  if(mismatch){std::cout<<"MQR468_CPP_COURT=FAIL mismatches="<<mismatch<<"\n";return 1;}
  std::cout<<"MQR468_CPP_COURT=PASS\n"; return 0;
}
