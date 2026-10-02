#include <algorithm>
#include <array>
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
  vector<string> o; string x; stringstream ss(s);
  while(getline(ss,x,d)) o.push_back(x);
  return o;
}
vector<map<string,string>> read_tsv(const string&path){
  ifstream in(path); if(!in) throw runtime_error("open failed");
  string line; getline(in,line); auto h=split(line,'\t');
  vector<map<string,string>> rows;
  while(getline(in,line)){
    if(line.empty()) continue;
    auto xs=split(line,'\t'); map<string,string> r;
    for(size_t i=0;i<h.size();++i) r[h[i]]=i<xs.size()?xs[i]:"";
    rows.push_back(r);
  }
  return rows;
}
int rank3(vector<array<int,3>> v){
  int r=0;
  for(int col=0;col<3;col++){
    int piv=-1;
    for(int i=r;i<(int)v.size();i++) if(v[i][col]){piv=i;break;}
    if(piv<0) continue;
    swap(v[r],v[piv]);
    for(int i=0;i<(int)v.size();i++) if(i!=r && v[i][col])
      for(int j=0;j<3;j++) v[i][j]^=v[r][j];
    r++;
  }
  return r;
}
int main(){
  auto rows=read_tsv("experiments/mqr-4.70/RESPONSE-MATRIX-FREEZE.tsv");
  vector<string> H,T;
  for(auto const&kv:rows[0]) if(kv.first!="history") T.push_back(kv.first);
  sort(T.begin(),T.end());
  map<pair<string,string>,int> R;
  for(auto&r:rows){
    H.push_back(r["history"]);
    for(auto&t:T)R[{r["history"],t}]=stoi(r[t]);
  }

  map<string,array<int,3>> V;
  vector<string> linear;
  for(auto&t:T){
    array<int,3> v={R[{"H100",t}],R[{"H010",t}],R[{"H001",t}]};
    bool ok=true;
    for(auto&h:H){
      int a=h[1]-'0',b=h[2]-'0',c=h[3]-'0';
      int pred=(v[0]*a+v[1]*b+v[2]*c)%2;
      if(pred!=R[{h,t}]){ok=false;break;}
    }
    if(ok){V[t]=v;linear.push_back(t);}
  }

  vector<string> loops;
  for(auto&t:T){
    set<int>s; for(auto&h:H)s.insert(R[{h,t}]);
    if(s.size()==1) loops.push_back(t);
  }

  vector<pair<string,string>> parallels;
  for(size_t i=0;i<T.size();i++)for(size_t j=i+1;j<T.size();j++){
    bool same=true;
    for(auto&h:H) if(R[{h,T[i]}]!=R[{h,T[j]}]){same=false;break;}
    if(same && find(loops.begin(),loops.end(),T[i])==loops.end() &&
       find(loops.begin(),loops.end(),T[j])==loops.end())
      parallels.push_back({T[i],T[j]});
  }

  vector<array<string,3>> bases;
  for(size_t i=0;i<linear.size();i++)for(size_t j=i+1;j<linear.size();j++)for(size_t k=j+1;k<linear.size();k++){
    vector<array<int,3>> cols={V[linear[i]],V[linear[j]],V[linear[k]]};
    if(rank3(cols)==3) bases.push_back({linear[i],linear[j],linear[k]});
  }

  set<array<string,3>> qb;
  for(auto b:bases){
    for(auto&x:b) if(x=="R") x="A";
    sort(b.begin(),b.end());
    qb.insert(b);
  }

  int pair_obligations=0;
  for(size_t i=0;i<H.size();i++)for(size_t j=i+1;j<H.size();j++) pair_obligations++;

  vector<array<int,3>> all;
  for(auto&t:linear)all.push_back(V[t]);
  bool ok=rank3(all)==3 && bases.size()==24 && qb.size()==16 &&
          find(loops.begin(),loops.end(),"CONST")!=loops.end();

  bool ar=false; for(auto&p:parallels) if((p.first=="A"&&p.second=="R")||(p.first=="R"&&p.second=="A")) ar=true;
  ok = ok && ar;

  cout<<"MQR470_CPP_HYPERGRAPH="<<(ok?"PASS":"FAIL")<<"\n";
  cout<<"MQR470_CPP_GF2_RANK="<<rank3(all)<<"\n";
  cout<<"MQR470_CPP_RANK3_BASE_COUNT="<<bases.size()<<"\n";
  cout<<"MQR470_CPP_DUPLICATE_QUOTIENT_BASE_COUNT="<<qb.size()<<"\n";
  cout<<"MQR470_CPP_PAIR_SEPARATOR_OBLIGATIONS="<<pair_obligations<<"\n";
  cout<<"MQR470_CPP_LOOP_CONST="<<(find(loops.begin(),loops.end(),"CONST")!=loops.end()?"YES":"NO")<<"\n";
  cout<<"MQR470_CPP_PARALLEL_A_R="<<(ar?"YES":"NO")<<"\n";
  return ok?0:1;
}
