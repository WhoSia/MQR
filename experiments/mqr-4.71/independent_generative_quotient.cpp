#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
using Row=map<string,string>;

vector<string> split(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
vector<Row> read_tsv(const string&p){ifstream in(p);string line;getline(in,line);auto h=split(line,'\t');vector<Row>rs;while(getline(in,line)){if(line.empty())continue;auto xs=split(line,'\t');Row r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<xs.size()?xs[i]:"";rs.push_back(r);}return rs;}
set<string> gens(const Row&s){set<string>g;for(auto&x:split(s.at("generators"),','))if(!x.empty())g.insert(x);return g;}
string tr(const Row&s,const string&t){
 auto g=gens(s);
 if(t=="RIVAL_ENTRY")return g.count("RIVAL")?"RIVAL_X|NEW_SEPARATOR|DOWNGRADE":"NONE|NO_NEW_CONTACT|UNCHANGED";
 if(t=="TECH_UNLOCK"){
  if(!g.count("INSTRUMENT"))return "NONE|NO_NEW_CONTACT|UNCHANGED";
  return s.at("tech_state")=="T1"?"INST_Z|NEW_SEPARATOR|DOWNGRADE":"NONE|RELEVANT_BUT_UNREALIZABLE|UNCHANGED";
 }
 if(t=="ETHICS_REVIEW"){
  if(!g.count("EXTERNAL"))return "NONE|NO_NEW_CONTACT|UNCHANGED";
  return s.at("ethics_state")=="E1"?"ETH_H|EXECUTION_PERMISSION_CHANGED|DOWNGRADE":"NONE|ETH_H_STILL_SCIENTIFICALLY_RELEVANT|UNCHANGED";
 }
 if(t=="BUDGET_UNLOCK"){
  if(!g.count("EXTERNAL"))return "NONE|NO_NEW_CONTACT|UNCHANGED";
  return s.at("budget_state")=="HIGH"?"COST_Q|EXECUTION_FEASIBILITY_CHANGED|DOWNGRADE":"NONE|COST_Q_STILL_SCIENTIFICALLY_RELEVANT|UNCHANGED";
 }
 throw runtime_error("trigger");
}
string fsig(const Row&s){string z;for(auto&t:{"RIVAL_ENTRY","TECH_UNLOCK","ETHICS_REVIEW","BUDGET_UNLOCK"})z+=tr(s,t)+";";return z;}
bool suff(const vector<Row>&S,const vector<string>&F){
 map<string,set<string>>m;
 for(auto&s:S){string k;for(auto&f:F)k+=s.at(f)+"|";m[k].insert(fsig(s));}
 for(auto&[k,v]:m)if(v.size()>1)return false;return true;
}
int main(){
 auto S=read_tsv("experiments/mqr-4.71/STATE-FREEZE.tsv");
 vector<string> F={"current_envelope","generators","tech_state","budget_state","ethics_state","revision_state","ancestry_label"};
 vector<vector<string>>mins;
 for(int k=0;k<=(int)F.size()&&mins.empty();++k){
  for(int mask=0;mask<(1<<(int)F.size());++mask){
   if(__builtin_popcount((unsigned)mask)!=k)continue;vector<string>x;
   for(int i=0;i<(int)F.size();++i)if(mask&(1<<i))x.push_back(F[i]);
   if(suff(S,x))mins.push_back(x);
  }
 }
 set<string> sigs;for(auto&s:S)sigs.insert(fsig(s));
 vector<string> target={"generators","tech_state","budget_state","ethics_state"};
 bool exact=mins.size()==1&&mins[0]==target;
 bool ok=S.size()==6&&sigs.size()==5&&exact;
 cout<<"MQR471_CPP_GENERATIVE_QUOTIENT="<<(ok?"PASS":"FAIL")<<"\n";
 cout<<"MQR471_CPP_RAW_STATES="<<S.size()<<"\n";
 cout<<"MQR471_CPP_PREDICTIVE_CLASSES="<<sigs.size()<<"\n";
 cout<<"MQR471_CPP_MINIMAL_FEATURE_COUNT="<<(mins.empty()?0:mins[0].size())<<"\n";
 if(!mins.empty()){cout<<"MQR471_CPP_MINIMAL_FEATURE_SET=";for(size_t i=0;i<mins[0].size();++i){if(i)cout<<",";cout<<mins[0][i];}cout<<"\n";}
 return ok?0:1;
}
