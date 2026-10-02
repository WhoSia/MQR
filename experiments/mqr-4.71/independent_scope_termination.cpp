#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std; using Row=map<string,string>;
vector<string> sp(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
vector<Row> rd(const string&p){ifstream in(p);string l;getline(in,l);auto h=sp(l,'\t');vector<Row>rs;while(getline(in,l)){if(l.empty())continue;auto x=sp(l,'\t');Row r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<x.size()?x[i]:"";rs.push_back(r);}return rs;}
string v(const Row&r){auto s=r.at("scope_source");bool known=r.at("universe_known")=="YES",comp=r.at("generator_complete_relative_to_scope")=="YES";if(s=="GENERATOR_OUTPUT_ONLY")return"HOLD_CIRCULAR";if(s=="EXECUTION_CONTRACT"&&known&&comp)return"CERTIFY_EXECUTION_ONLY";if((s=="EXTERNAL_FINITE"||s=="PROVED_GRAMMAR")&&known&&comp)return"CERTIFY_RELATIVE";return"HOLD";}
int main(){auto R=rd("experiments/mqr-4.71/SCOPE-TERMINATION-FREEZE.tsv");int mm=0,rel=0,circ=0,ex=0;for(auto&r:R){auto g=v(r);if(g!=r["expected"])mm++;if(g=="CERTIFY_RELATIVE")rel++;if(g=="HOLD_CIRCULAR")circ++;if(g=="CERTIFY_EXECUTION_ONLY")ex++;}bool ok=mm==0&&rel==2&&circ==1&&ex==1;cout<<"MQR471_CPP_SCOPE_TERMINATION="<<(ok?"PASS":"FAIL")<<"\n";cout<<"MQR471_CPP_RELATIVE_CERTIFICATES="<<rel<<"\n";cout<<"MQR471_CPP_EXECUTION_ONLY_CERTIFICATES="<<ex<<"\n";cout<<"MQR471_CPP_CIRCULAR_HOLDS="<<circ<<"\n";cout<<"MQR471_CPP_RELATIVE_NE_OPEN_WORLD=YES\n";return ok?0:1;}
