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
vector<Row> read_tsv(const string&p){
 ifstream in(p);if(!in)throw runtime_error("open");
 string line;getline(in,line);auto h=split(line,'\t');vector<Row>rs;
 while(getline(in,line)){if(line.empty())continue;auto xs=split(line,'\t');Row r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<xs.size()?xs[i]:"";rs.push_back(r);}return rs;
}
set<string> gens(const Row&s){set<string>g;for(auto&x:split(s.at("generators"),','))if(!x.empty())g.insert(x);return g;}
tuple<string,string,string> tr(const Row&s,const string&t){
 auto g=gens(s);
 if(t=="RIVAL_ENTRY"){
   if(g.count("RIVAL"))return {"RIVAL_X","NEW_SEPARATOR","DOWNGRADE"};
   return {"NONE","NO_NEW_CONTACT","UNCHANGED"};
 }
 if(t=="TECH_UNLOCK"){
   if(!g.count("INSTRUMENT"))return {"NONE","NO_NEW_CONTACT","UNCHANGED"};
   if(s.at("tech_state")=="T1")return {"INST_Z","NEW_SEPARATOR","DOWNGRADE"};
   return {"NONE","RELEVANT_BUT_UNREALIZABLE","UNCHANGED"};
 }
 if(t=="ETHICS_REVIEW"){
   if(!g.count("EXTERNAL"))return {"NONE","NO_NEW_CONTACT","UNCHANGED"};
   if(s.at("ethics_state")=="E1")return {"ETH_H","EXECUTION_PERMISSION_CHANGED","DOWNGRADE"};
   return {"NONE","ETH_H_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED"};
 }
 if(t=="BUDGET_UNLOCK"){
   if(!g.count("EXTERNAL"))return {"NONE","NO_NEW_CONTACT","UNCHANGED"};
   if(s.at("budget_state")=="HIGH")return {"COST_Q","EXECUTION_FEASIBILITY_CHANGED","DOWNGRADE"};
   return {"NONE","COST_Q_STILL_SCIENTIFICALLY_RELEVANT","UNCHANGED"};
 }
 throw runtime_error("trigger");
}
string sig(const Row&s){
 string out;
 for(string t:{"RIVAL_ENTRY","TECH_UNLOCK","ETHICS_REVIEW","BUDGET_UNLOCK"}){
   auto [a,b,c]=tr(s,t);out+=a+"|"+b+"|"+c+";";
 }
 return out;
}
string compact(const Row&s){
 auto g=gens(s);string x;for(auto&a:g)x+=a+",";
 return x+"|"+s.at("tech_state")+"|"+s.at("budget_state")+"|"+s.at("ethics_state")+"|"+s.at("revision_state");
}
int main(){
 auto cr=read_tsv("experiments/mqr-4.71/CONTACT-FREEZE.tsv");
 auto sr=read_tsv("experiments/mqr-4.71/STATE-FREEZE.tsv");
 auto cases=read_tsv("experiments/mqr-4.71/TRIGGER-FREEZE.tsv");
 map<string,Row>C,S;for(auto&r:cr)C[r["contact_id"]]=r;for(auto&r:sr)S[r["state_id"]]=r;

 int mm=0,down=0;
 for(auto&c:cases){
   auto got=tr(S[c["state_id"]],c["trigger"]);
   auto exp=make_tuple(c["expected_admission"],c["expected_scientific_status"],c["expected_closure_effect"]);
   if(got!=exp)mm++;
   if(c["expected_closure_effect"]=="DOWNGRADE")down++;
 }
 set<string> envs;for(auto&[id,s]:S)envs.insert(s["current_envelope"]);
 bool same=envs.size()==1;
 bool insuff=sig(S["S_THEORY"])!=sig(S["S_PLURAL"]);
 bool self=get<0>(tr(S["S_THEORY"],"RIVAL_ENTRY"))=="NONE";
 bool plural=get<0>(tr(S["S_PLURAL"],"RIVAL_ENTRY"))=="RIVAL_X";
 bool anc=sig(S["S_PLURAL"])==sig(S["S_PLURAL_ALT"]);
 bool ceq=compact(S["S_PLURAL"])==compact(S["S_PLURAL_ALT"]);
 map<string,set<string>> byc;for(auto&[id,s]:S)byc[compact(s)].insert(sig(s));
 bool cs=true;for(auto&[k,v]:byc)if(v.size()>1)cs=false;
 bool ethics=C["ETH_H"]["scientific_split"]=="YES"&&C["ETH_H"]["permission"]=="BLOCKED_ETHICS"&&
   get<0>(tr(S["S_PLURAL"],"ETHICS_REVIEW"))=="NONE";
 bool cost=C["COST_Q"]["scientific_split"]=="YES"&&C["COST_Q"]["cost_state"]=="HIGH"&&
   get<0>(tr(S["S_PLURAL"],"BUDGET_UNLOCK"))=="NONE";
 bool tech=get<0>(tr(S["S_PLURAL"],"TECH_UNLOCK"))=="NONE"&&get<0>(tr(S["S_TECH1"],"TECH_UNLOCK"))=="INST_Z";
 bool ok=mm==0&&same&&insuff&&self&&plural&&anc&&ceq&&cs&&ethics&&cost&&tech&&down>=4;
 cout<<"MQR471_CPP_ENVELOPE_COURT="<<(ok?"PASS":"FAIL")<<"\n";
 cout<<"MQR471_CPP_CURRENT_ENVELOPE_INSUFFICIENT="<<(insuff?"YES":"NO")<<"\n";
 cout<<"MQR471_CPP_THEORY_ONLY_SELF_SEALS="<<(self?"YES":"NO")<<"\n";
 cout<<"MQR471_CPP_PLURAL_GENERATOR_ADMITS_RIVAL="<<(plural?"YES":"NO")<<"\n";
 cout<<"MQR471_CPP_ANCESTRY_NULL="<<(anc?"YES":"NO")<<"\n";
 cout<<"MQR471_CPP_COMPACT_STATE_SUFFICIENT="<<(cs?"YES":"NO")<<"\n";
 cout<<"MQR471_CPP_TECHNOLOGY_UNLOCK="<<(tech?"YES":"NO")<<"\n";
 cout<<"MQR471_CPP_DOWNGRADE_CASES="<<down<<"\n";
 return ok?0:1;
}
