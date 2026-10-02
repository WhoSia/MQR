#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using Row=std::map<std::string,std::string>;
std::vector<std::string> split(const std::string&s){std::vector<std::string>o;std::stringstream ss(s);std::string x;while(std::getline(ss,x,'\t'))o.push_back(x);return o;}
std::vector<Row> read_tsv(const std::string&p){std::ifstream in(p);if(!in)throw std::runtime_error("open");std::string line;std::getline(in,line);auto h=split(line);std::vector<Row>rs;while(std::getline(in,line)){if(line.empty())continue;auto x=split(line);Row r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<x.size()?x[i]:"";rs.push_back(r);}return rs;}
std::array<std::string,4> F={"authorization_state","provenance_state","defeater_state","revision_state"};
std::string tr(const std::string&u,const Row&f){
 auto a=f.at(F[0]),p=f.at(F[1]),d=f.at(F[2]),r=f.at(F[3]);
 if(u=="AUTHORIZATION_CHECK")return (a=="RETROSPECTIVE"||a=="UNAUTHORIZED")?"HOLD_REAUTHORIZE":"STABLE";
 if(u=="REVISION_REPLAY"){if(a=="RETROSPECTIVE")return"REOPEN_REQUIRED";if(r=="REASON_MUTATION")return"HOLD_REASON_RECONSTITUTE";return"STABLE";}
 if(u=="WITHDRAW_ANCESTRY_SUPPORT"||u=="REPRODUCE_UNDER_INDEPENDENT_ANCESTRY")return p=="COMMON_MODE_SINGLE_ROOT"?"REOPEN_REQUIRED":"STABLE";
 if(u=="REOPEN_WITH_HELD_OUT_DEFEATER")return d=="SURVIVED_D1"?"STABLE":"REOPEN_REQUIRED";
 if(u=="REOPEN_WITH_HELD_OUT_DEFEATER_D3")return"REOPEN_REQUIRED";
 if(u=="COUNTERFACTUAL_RECONSTITUTION")return r=="REVERSAL"?"REOPEN_REQUIRED":"STABLE";
 if(u=="AUDIT_SOURCE"||u=="SCOPE_EXPANSION")return"STABLE";
 throw std::runtime_error("unknown intervention");
}
int main(int argc,char**argv){
 std::string pp=argc>1?argv[1]:"experiments/mqr-4.69/PAIR-FREEZE.tsv";
 std::string sp=argc>2?argv[2]:"experiments/mqr-4.69/ANCESTRY-FEATURES.tsv";
 auto pairs=read_tsv(pp), sr=read_tsv(sp); std::map<std::string,Row> schema; for(auto&r:sr)schema[r["ancestry"]]=r;
 std::set<std::string> us; for(auto&p:pairs)us.insert(p["intervention"]); std::vector<std::string> U(us.begin(),us.end());
 std::map<std::string,std::vector<std::string>> cls;
 std::set<std::string> typed;
 for(auto&[anc,f]:schema){
   std::string sig; for(auto&u:U)sig+=tr(u,f)+"|";
   cls[sig].push_back(anc);
   typed.insert(f.at(F[0])+"|"+f.at(F[1])+"|"+f.at(F[2])+"|"+f.at(F[3]));
 }
 int mm=0; for(auto&p:pairs)for(std::string s:{"A","B"})if(tr(p["intervention"],schema[p["ancestry_"+s]])!=p["expected_"+s])mm++;
 if(mm){std::cout<<"MQR469_CPP_PREDICTIVE_QUOTIENT=FAIL\n";return 1;}
 std::cout<<"MQR469_CPP_PREDICTIVE_QUOTIENT=PASS\n";
 std::cout<<"MQR469_RAW_ANCESTRY_LABELS="<<schema.size()<<"\n";
 std::cout<<"MQR469_TYPED_FOUR_AXIS_STATES="<<typed.size()<<"\n";
 std::cout<<"MQR469_PREDICTIVE_CLASSES="<<cls.size()<<"\n";
 std::cout<<"MQR469_FOUR_AXIS_OVERRETENTION="<<(cls.size()<typed.size()?"YES":"NO")<<"\n";
 return 0;
}
