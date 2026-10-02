#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
using namespace std; using Row=map<string,string>;
vector<string> sp(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
vector<Row> rd(const string&p){ifstream in(p);string l;getline(in,l);auto h=sp(l,'\t');vector<Row>rs;while(getline(in,l)){if(l.empty())continue;auto x=sp(l,'\t');Row r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<x.size()?x[i]:"";rs.push_back(r);}return rs;}
tuple<string,string,string> tr(const Row&r){auto t=r.at("transition");if(t=="NONE")return{"SAME","SAME","SAME"};if(t=="TECH_UNLOCK")return{"SAME","SAME","EXPAND"};if(t=="ETHICS_RESTRICT")return{"SAME","SAME","CONTRACT"};if(t=="RIVAL_ARRIVAL")return{"EXPAND","EXPAND","SAME"};if(t=="GENERATOR_NULL_ENTRY")return{"EXPAND","SAME","SAME"};throw runtime_error("t");}
bool inc(const Row&r){bool c=r.at("candidate")=="YES",s=r.at("scientific")=="YES",x=r.at("executable")=="YES";return(!x||s)&&(!s||c);}
int main(){auto R=rd("experiments/mqr-4.71/THREE-LAYER-CONTACT-FREEZE.tsv");int mm=0;bool up=false,down=false,tech=false,gnull=false,rival=false;for(auto&r:R){auto g=tr(r),e=make_tuple(r["expected_C"],r["expected_S"],r["expected_X"]);if(g!=e||!inc(r))mm++;if(r["expected_X"]=="EXPAND")up=true;if(r["expected_X"]=="CONTRACT")down=true;if(r["case_id"]=="T_UNLOCK")tech=(g==make_tuple(string("SAME"),string("SAME"),string("EXPAND")));if(r["case_id"]=="G_NULL")gnull=(g==make_tuple(string("EXPAND"),string("SAME"),string("SAME")));if(r["case_id"]=="R_ARRIVE")rival=(g==make_tuple(string("EXPAND"),string("EXPAND"),string("SAME")));}bool ok=mm==0&&up&&down&&tech&&gnull&&rival;cout<<"MQR471_CPP_THREE_LAYER_CONTACT="<<(ok?"PASS":"FAIL")<<"\n";cout<<"MQR471_CPP_CASES="<<R.size()<<"\n";cout<<"MQR471_CPP_TECH_UNLOCK_X_ONLY="<<(tech?"YES":"NO")<<"\n";cout<<"MQR471_CPP_GENERATOR_NULL_C_ONLY="<<(gnull?"YES":"NO")<<"\n";cout<<"MQR471_CPP_RIVAL_C_S_WITHOUT_X="<<(rival?"YES":"NO")<<"\n";cout<<"MQR471_CPP_EXECUTION_NONMONOTONE="<<((up&&down)?"YES":"NO")<<"\n";return ok?0:1;}
