#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std; using Row=map<string,string>;
vector<string> sp(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
vector<Row> rd(const string&p){ifstream in(p);string l;getline(in,l);auto h=sp(l,'\t');vector<Row>rs;while(getline(in,l)){if(l.empty())continue;auto x=sp(l,'\t');Row r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<x.size()?x[i]:"";rs.push_back(r);}return rs;}
bool executable(const Row&r){return r.at("feasibility")=="AVAILABLE"&&r.at("permission")=="PERMITTED"&&r.at("budget")=="LOW";}
string verdict(const Row&r){
 if(r.at("scientific_split")!="YES")return "STABLE";
 if(r.at("scope_kind")=="SCIENTIFIC_RELEVANCE")return executable(r)?"DOWNGRADE":"DOWNGRADE_DEBT";
 if(r.at("scope_kind")=="CURRENT_EXECUTION")return executable(r)?"DOWNGRADE":"STABLE_SCOPED";
 throw runtime_error("scope");
}
int main(){
 auto R=rd("experiments/mqr-4.71/CLOSURE-DEFEASIBILITY-FREEZE.tsv");
 int mm=0; map<string,map<string,string>> p;
 for(auto&r:R){
   auto g=verdict(r); if(g!=r["expected"])mm++;
   auto id=r["case_id"]; auto pos=id.find('_'); auto base=id.substr(0,pos);
   p[base][r["scope_kind"]]=g;
 }
 int sep=0; for(auto&[k,v]:p)if(v["SCIENTIFIC_RELEVANCE"]!=v["CURRENT_EXECUTION"])sep++;
 bool ok=mm==0&&sep==3;
 cout<<"MQR471_CPP_CLOSURE_DEFEASIBILITY="<<(ok?"PASS":"FAIL")<<"\n";
 cout<<"MQR471_CPP_CASES="<<R.size()<<"\n";
 cout<<"MQR471_CPP_SCOPE_SEPARATION_CASES="<<sep<<"\n";
 cout<<"MQR471_CPP_EXECUTION_COMPLETE_NE_SCIENTIFIC_COMPLETE="<<(sep==3?"YES":"NO")<<"\n";
 return ok?0:1;
}
