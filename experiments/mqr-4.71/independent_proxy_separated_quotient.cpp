#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std; using Row=map<string,string>;
vector<string> sp(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
vector<Row> rd(const string&p){ifstream in(p);string l;getline(in,l);auto h=sp(l,'\t');vector<Row>r;while(getline(in,l)){if(l.empty())continue;auto x=sp(l,'\t');Row q;for(size_t i=0;i<h.size();++i)q[h[i]]=i<x.size()?x[i]:"";r.push_back(q);}return r;}
set<string> gs(const Row&s){set<string>g;for(auto&x:sp(s.at("generators"),','))if(!x.empty())g.insert(x);return g;}
string tr(const Row&s,string t){auto g=gs(s);if(t=="RIVAL_ENTRY")return g.count("RIVAL")?"R|1":"N|0";if(t=="TECH_UNLOCK"){if(!g.count("INSTRUMENT"))return"N|0";return s.at("tech_state")=="T1"?"I|1":"U|0";}if(t=="ETHICS_REVIEW"){if(!g.count("EXTERNAL"))return"N|0";return s.at("ethics_state")=="E1"?"E|1":"EB|0";}if(t=="BUDGET_UNLOCK"){if(!g.count("EXTERNAL"))return"N|0";return s.at("budget_state")=="HIGH"?"C|1":"CB|0";}throw runtime_error("t");}
string sig(const Row&s){string z;for(string t:{"RIVAL_ENTRY","TECH_UNLOCK","ETHICS_REVIEW","BUDGET_UNLOCK"})z+=tr(s,t)+";";return z;}
bool suff(const vector<Row>&S,const vector<string>&F){map<string,set<string>>m;for(auto&s:S){string k;for(auto&f:F)k+=s.at(f)+"|";m[k].insert(sig(s));}for(auto&[k,v]:m)if(v.size()>1)return false;return true;}
int main(){auto S=rd("experiments/mqr-4.71/PROXY-SEPARATION-FREEZE.tsv");vector<string>F={"current_envelope","generators","tech_state","budget_state","ethics_state","revision_state","ancestry_label"},target={"generators","tech_state","budget_state","ethics_state"},proxy={"tech_state","budget_state","ethics_state","ancestry_label"};vector<vector<string>>M;for(int k=0;k<=(int)F.size()&&M.empty();++k)for(int m=0;m<(1<<(int)F.size());++m){if(__builtin_popcount((unsigned)m)!=k)continue;vector<string>x;for(int i=0;i<(int)F.size();++i)if(m&(1<<i))x.push_back(F[i]);if(suff(S,x))M.push_back(x);}set<string>sg;for(auto&s:S)sg.insert(sig(s));bool ok=S.size()==8&&sg.size()==5&&M.size()==1&&M[0]==target&&!suff(S,proxy);cout<<"MQR471_CPP_PHASE2_PROXY_SEPARATION="<<(ok?"PASS":"FAIL")<<"\n";cout<<"MQR471_CPP_PHASE2_RAW_STATES="<<S.size()<<"\n";cout<<"MQR471_CPP_PHASE2_PREDICTIVE_CLASSES="<<sg.size()<<"\n";cout<<"MQR471_CPP_PHASE2_MINIMAL_FEATURE_COUNT="<<(M.empty()?0:M[0].size())<<"\n";if(!M.empty()){cout<<"MQR471_CPP_PHASE2_MINIMAL_FEATURE_SET=";for(size_t i=0;i<M[0].size();++i){if(i)cout<<",";cout<<M[0][i];}cout<<"\n";}cout<<"MQR471_CPP_PHASE2_ANCESTRY_PROXY_BROKEN="<<(!suff(S,proxy)?"YES":"NO")<<"\n";return ok?0:1;}
