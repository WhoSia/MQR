#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std; using Row=map<string,string>;
vector<string> sp(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
vector<Row> rd(const string&p){ifstream in(p);string l;getline(in,l);auto h=sp(l,'\t');vector<Row>rs;while(getline(in,l)){if(l.empty())continue;auto x=sp(l,'\t');Row r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<x.size()?x[i]:"";rs.push_back(r);}return rs;}
string v(const Row&r){
 auto d=r.at("domain"),t=r.at("target_mode"),cf=r.at("calibration_or_framework"),sem=r.at("semantic_transport");
 bool indep=r.at("independent_check")=="YES",defeat=r.at("defeat_route_preserved")=="YES";
 if(d=="NATSCI"){
  if(t=="EXPLORATORY")return indep&&defeat?"ADMIT_EXPLORATORY":"HOLD";
  if(t=="DIFFERENT_TARGET")return"DISTINCT_OUTCOME_SEMANTICS";
  if(cf=="THEORY_SELF_GATED"&&!indep)return"HOLD_CIRCULAR";
  if(cf=="THEORY_GUIDED"&&indep&&defeat)return"ADMIT_WITH_DEPENDENCE_RECEIPT";
  if(!defeat)return"DOWNGRADE_INHERITED_AUTHORITY";
  return"ADMIT_LOCAL";
 }
 if(d=="MATH"){
  if(cf=="COUNTERMODEL_TARGET")return"HOLD_TRANSPORT";
  if(t=="SEMANTIC_REINTERPRETATION"&&sem=="NO")return"HOLD_SEMANTIC_DRIFT";
  if(cf=="VALID_EMBEDDING"&&defeat&&sem=="YES")return"CERTIFY_TRANSPORT_RELATIVE";
  if((cf=="VALID_PROOF"||cf=="CHECKED_KERNEL")&&defeat)return"CERTIFY_RELATIVE";
  return"HOLD";
 }
 throw runtime_error("domain");
}
int main(){
 auto R=rd("experiments/mqr-4.72/COURT-FREEZE.tsv");int mm=0;map<string,string>got;
 for(auto&r:R){auto g=v(r);got[r["case_id"]]=g;if(g!=r["expected"])mm++;}
 bool ok=mm==0&&got["N3"]=="ADMIT_EXPLORATORY"&&got["N4"]=="HOLD_CIRCULAR"&&got["N6"]=="DOWNGRADE_INHERITED_AUTHORITY"&&got["M2"]=="HOLD_TRANSPORT"&&got["M5"]=="CERTIFY_RELATIVE";
 cout<<"MQR472_CPP_INTENTIONAL_CONTACT="<<(ok?"PASS":"FAIL")<<"\n";
 cout<<"MQR472_CPP_CASES="<<R.size()<<"\n";
 cout<<"MQR472_CPP_EXPLORATORY_WITHOUT_FULL_TARGET="<<(got["N3"]=="ADMIT_EXPLORATORY"?"YES":"NO")<<"\n";
 cout<<"MQR472_CPP_THEORY_SELF_GATE_BLOCKED="<<(got["N4"]=="HOLD_CIRCULAR"?"YES":"NO")<<"\n";
 cout<<"MQR472_CPP_DEFEAT_ROUTE_LOSS_DOWNGRADES="<<(got["N6"]=="DOWNGRADE_INHERITED_AUTHORITY"?"YES":"NO")<<"\n";
 cout<<"MQR472_CPP_MATH_FRAMEWORK_LABEL_NOT_ENOUGH="<<(got["M2"]=="HOLD_TRANSPORT"?"YES":"NO")<<"\n";
 return ok?0:1;
}
