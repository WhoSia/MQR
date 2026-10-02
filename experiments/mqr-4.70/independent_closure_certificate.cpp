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

vector<string> split(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
vector<map<string,string>> read_tsv(const string&p){
 ifstream in(p);if(!in)throw runtime_error("open");
 string line;getline(in,line);auto h=split(line,'\t');vector<map<string,string>> rs;
 while(getline(in,line)){if(line.empty())continue;auto xs=split(line,'\t');map<string,string>r;for(size_t i=0;i<h.size();++i)r[h[i]]=i<xs.size()?xs[i]:"";rs.push_back(r);}return rs;
}
struct D{vector<string>H,T;map<pair<string,string>,string>R;map<string,vector<string>>F;};
D load(){
 D d;auto rows=read_tsv("experiments/mqr-4.70/RESPONSE-MATRIX-FREEZE.tsv");
 for(auto const&kv:rows[0])if(kv.first!="history")d.T.push_back(kv.first);
 sort(d.T.begin(),d.T.end());
 for(auto&r:rows){d.H.push_back(r["history"]);for(auto&t:d.T)d.R[{r["history"],t}]=r[t];}
 auto fr=read_tsv("experiments/mqr-4.70/PROBE-FAMILIES-FREEZE.tsv");
 for(auto&r:fr)d.F[r["family_id"]]=r["members"]=="-"?vector<string>{}:split(r["members"],',');
 return d;
}
string sig(const D&d,const string&h,const vector<string>&U){string s;for(auto&t:U)s+=d.R.at({h,t})+"|";return s;}
bool reconstructible(const D&d,const vector<string>&U,const string&t){
 map<string,string>seen;
 for(auto&h:d.H){auto s=sig(d,h,U),y=d.R.at({h,t});if(seen.count(s)&&seen[s]!=y)return false;seen[s]=y;}return true;
}
set<string> exterior_splitters(const D&d,const vector<string>&U){
 map<string,vector<string>> cls;
 for(auto&h:d.H)cls[sig(d,h,U)].push_back(h);
 set<string> us(U.begin(),U.end()),out;
 for(auto&t:d.T)if(!us.count(t)){
   for(auto&kv:cls){
     auto&c=kv.second;
     for(size_t i=0;i<c.size();++i)for(size_t j=i+1;j<c.size();++j)
       if(d.R.at({c[i],t})!=d.R.at({c[j],t}))out.insert(t);
   }
 }
 return out;
}
bool c4(const D&d,const vector<string>&U){for(auto&t:d.T)if(!reconstructible(d,U,t))return false;return true;}
vector<vector<string>> minimal_c4(const D&d){
 int n=d.T.size();
 for(int k=0;k<=n;k++){
   vector<vector<string>>w;
   for(int mask=0;mask<(1<<n);++mask){
     if(__builtin_popcount((unsigned)mask)!=k)continue;
     vector<string>U;for(int i=0;i<n;i++)if(mask&(1<<i))U.push_back(d.T[i]);
     if(c4(d,U))w.push_back(U);
   }
   if(!w.empty())return w;
 }
 return {};
}
int main(){
 auto d=load();
 auto fAB=d.F["F_AB"],fABC=d.F["F_ABC"];
 auto sp=exterior_splitters(d,fAB);
 auto mins=minimal_c4(d);
 bool abC4=c4(d,fAB),abcC4=c4(d,fABC);
 bool ok=!abC4&&abcC4&&sp==set<string>({"C","K","P"})&&mins.size()==24&&mins[0].size()==3;
 cout<<"MQR470_CPP_CLOSURE_COURT="<<(ok?"PASS":"FAIL")<<"\n";
 cout<<"MQR470_CPP_F_AB_C4="<<(abC4?"TRUE":"FALSE")<<"\n";
 cout<<"MQR470_CPP_F_ABC_C4="<<(abcC4?"TRUE":"FALSE")<<"\n";
 cout<<"MQR470_CPP_F_AB_EXTERIOR_SPLITTERS=";
 bool first=true;for(auto&s:sp){if(!first)cout<<",";cout<<s;first=false;}cout<<"\n";
 cout<<"MQR470_CPP_MINIMAL_C4_FAMILY_COUNT="<<mins.size()<<"\n";
 cout<<"MQR470_CPP_MINIMAL_C4_FAMILY_SIZE="<<(mins.empty()?0:mins[0].size())<<"\n";
 return ok?0:1;
}
