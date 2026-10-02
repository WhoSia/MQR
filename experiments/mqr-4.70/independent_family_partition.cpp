#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

vector<string> split(const string&s,char d){
  vector<string> o; string x; stringstream ss(s); while(getline(ss,x,d)) o.push_back(x); return o;
}
vector<map<string,string>> read_tsv(const string&path){
  ifstream in(path); if(!in) throw runtime_error("open failed");
  string line; getline(in,line); auto h=split(line,'\t');
  vector<map<string,string>> rows;
  while(getline(in,line)){
    if(line.empty()) continue; auto xs=split(line,'\t'); map<string,string> r;
    for(size_t i=0;i<h.size();++i) r[h[i]]=i<xs.size()?xs[i]:"";
    rows.push_back(r);
  }
  return rows;
}
struct Data{
  vector<string> H,T;
  map<pair<string,string>,string> R;
  map<string,vector<string>> F;
};
Data load(){
  Data d;
  auto rows=read_tsv("experiments/mqr-4.70/RESPONSE-MATRIX-FREEZE.tsv");
  for(auto const&kv:rows[0]) if(kv.first!="history") d.T.push_back(kv.first);
  sort(d.T.begin(),d.T.end());
  for(auto&r:rows){
    d.H.push_back(r["history"]);
    for(auto&t:d.T) d.R[{r["history"],t}]=r[t];
  }
  auto fr=read_tsv("experiments/mqr-4.70/PROBE-FAMILIES-FREEZE.tsv");
  for(auto&r:fr){
    vector<string> xs;
    if(r["members"]!="-") xs=split(r["members"],',');
    d.F[r["family_id"]]=xs;
  }
  return d;
}
vector<vector<string>> partition_of(const Data&d,const vector<string>&fam){
  map<vector<string>,vector<string>> b;
  for(auto&h:d.H){
    vector<string> sig;
    for(auto&t:fam) sig.push_back(d.R.at({h,t}));
    b[sig].push_back(h);
  }
  vector<vector<string>> p;
  for(auto&kv:b){ auto c=kv.second; sort(c.begin(),c.end()); p.push_back(c); }
  sort(p.begin(),p.end());
  return p;
}
bool refines(const vector<vector<string>>&fine,const vector<vector<string>>&coarse){
  map<string,int> idx;
  for(size_t i=0;i<coarse.size();++i) for(auto&h:coarse[i]) idx[h]=(int)i;
  for(auto&c:fine){
    set<int>s; for(auto&h:c)s.insert(idx[h]);
    if(s.size()>1) return false;
  }
  return true;
}
double entropy(const vector<string>&x){
  map<string,int> c; for(auto&v:x)c[v]++;
  double n=(double)x.size(),h=0;
  for(auto&kv:c){double p=kv.second/n; h-=p*log2(p);}
  return h;
}
double mutual_info(const vector<string>&x,const vector<string>&y){
  vector<string> xy; for(size_t i=0;i<x.size();++i)xy.push_back(x[i]+"|"+y[i]);
  return entropy(x)+entropy(y)-entropy(xy);
}
vector<string> class_labels(const Data&d,const vector<string>&fam){
  auto p=partition_of(d,fam); map<string,string> lab;
  for(size_t i=0;i<p.size();++i)for(auto&h:p[i])lab[h]=to_string(i);
  vector<string> y; for(auto&h:d.H)y.push_back(lab[h]); return y;
}
string choose_alignment(const Data&d,const vector<string>&base,const vector<string>&cand){
  auto y=class_labels(d,base); double best=-1; string pick;
  for(auto&t:cand){
    vector<string>x; for(auto&h:d.H)x.push_back(d.R.at({h,t}));
    double s=mutual_info(x,y);
    if(s>best+1e-12 || (fabs(s-best)<1e-12 && (pick.empty()||t<pick))){best=s;pick=t;}
  }
  return pick;
}
int split_score(const Data&d,const vector<string>&base,const string&t){
  auto p=partition_of(d,base); int s=0;
  for(auto&c:p) for(size_t i=0;i<c.size();++i) for(size_t j=i+1;j<c.size();++j)
    if(d.R.at({c[i],t})!=d.R.at({c[j],t})) s++;
  return s;
}
string choose_within(const Data&d,const vector<string>&base,const vector<string>&cand){
  int best=-1; string pick;
  for(auto&t:cand){
    int s=split_score(d,base,t);
    if(s>best || (s==best && (pick.empty()||t<pick))){best=s;pick=t;}
  }
  return pick;
}
vector<vector<string>> minimal_for(const Data&d,const vector<vector<string>>&target){
  vector<vector<string>> wins; int n=d.T.size();
  for(int k=0;k<=n;k++){
    for(int mask=0;mask<(1<<n);++mask){
      if(__builtin_popcount((unsigned)mask)!=k)continue;
      vector<string> fam; for(int i=0;i<n;i++)if(mask&(1<<i))fam.push_back(d.T[i]);
      if(partition_of(d,fam)==target)wins.push_back(fam);
    }
    if(!wins.empty())return wins;
  }
  return wins;
}
int main(){
  auto d=load(); map<string,vector<vector<string>>> P;
  for(auto&kv:d.F)P[kv.first]=partition_of(d,kv.second);
  int checks=0,fail=0;
  for(auto&a:d.F)for(auto&b:d.F){
    set<string>A(a.second.begin(),a.second.end()),B(b.second.begin(),b.second.end());
    if(includes(B.begin(),B.end(),A.begin(),A.end())){
      checks++; if(!refines(P[b.first],P[a.first]))fail++;
    }
  }
  auto mins=minimal_for(d,P["F_ABC"]);
  int collapsed=0,csep=0;
  for(size_t i=0;i<d.H.size();++i)for(size_t j=i+1;j<d.H.size();++j){
    bool same=true; for(auto&t:d.F["F_AB"]) if(d.R.at({d.H[i],t})!=d.R.at({d.H[j],t})) same=false;
    if(same){collapsed++; if(d.R.at({d.H[i],"C"})!=d.R.at({d.H[j],"C"}))csep++;}
  }
  string s1=choose_alignment(d,d.F["F_AB"],{"C","R","CONST"});
  string s2=choose_within(d,d.F["F_AB"],{"C","R","CONST"});
  bool good=refines(partition_of(d,{"A","B","C"}),partition_of(d,{"A","B","C"}));
  bool bad=refines(partition_of(d,{"A","B","CONST"}),partition_of(d,{"A","B","C"}));

  bool ok= fail==0 && P["F_AB"]==P["F_AX"] && P["F_AB"]==P["F_BX"] &&
           P["F_ABC"].size()>P["F_AB"].size() && mins.size()>=3 && csep>0 &&
           s1=="R" && s2=="C" && good && !bad;

  cout<<"MQR470_CPP_COURT="<<(ok?"PASS":"FAIL")<<"\n";
  cout<<"MQR470_CPP_INCLUSION_FAILURES="<<fail<<"\n";
  cout<<"MQR470_CPP_CLASSES_F_AB="<<P["F_AB"].size()<<"\n";
  cout<<"MQR470_CPP_CLASSES_F_ABC="<<P["F_ABC"].size()<<"\n";
  cout<<"MQR470_CPP_MINIMAL_FAMILY_COUNT="<<mins.size()<<"\n";
  cout<<"MQR470_CPP_COLLAPSED_PAIRS="<<collapsed<<"\n";
  cout<<"MQR470_CPP_EXTERIOR_C_SPLITS="<<csep<<"\n";
  cout<<"MQR470_CPP_CURRENT_ALIGNMENT_CHOICE="<<s1<<"\n";
  cout<<"MQR470_CPP_WITHIN_CLASS_CHOICE="<<s2<<"\n";
  cout<<"MQR470_CPP_GOOD_TRANSPORT="<<(good?"PASS":"FAIL")<<"\n";
  cout<<"MQR470_CPP_LOSSY_TRANSPORT="<<(bad?"PRESERVE":"BREAK")<<"\n";
  return ok?0:1;
}
