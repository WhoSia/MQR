#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using State=int;
using Part=std::array<int,512>;

enum Event {
 RP0,RP1,RP2,RM0,RM1,RM2,
 SP0,SP1,SP2,SM0,SM1,SM2,
 PGOOD,PBAD,AUDIT,XON,XOFF,NOVELTY
};
constexpr int EVENT_COUNT=18;

static inline bool has(State s,int b){return (s>>b)&1;}
static inline State setb(State s,int b){return s|(1<<b);}
static inline State clrb(State s,int b){return s&~(1<<b);}

State step(State s,int e){
  switch(e){
    case RP0:return setb(s,0); case RP1:return setb(s,1); case RP2:return setb(s,2);
    case RM0:return clrb(s,0); case RM1:return clrb(s,1); case RM2:return clrb(s,2);
    case SP0:return setb(s,3); case SP1:return setb(s,4); case SP2:return setb(s,5);
    case SM0:return clrb(s,3); case SM1:return clrb(s,4); case SM2:return clrb(s,5);
    case PGOOD:return setb(s,7); case PBAD:return clrb(s,7);
    case AUDIT:return has(s,7)?setb(s,6):clrb(s,6);
    case XON:return setb(s,8); case XOFF:return clrb(s,8);
    case NOVELTY:return has(s,8)?clrb(setb(s,2),5):s;
  }
  return s;
}
int unresolved(State s){
  int n=0;
  for(int i=0;i<3;i++) if(has(s,i)&&!has(s,3+i)) n++;
  return n;
}
bool release(State s){return unresolved(s)==0 && has(s,6);}
int actionMask(State s){return 1|2|(release(s)?4:8);}
std::array<int,3> label(State s){return {unresolved(s),actionMask(s),release(s)?1:0};}
int encodeLabel(State s){auto l=label(s);return l[0]*64+l[1]*2+l[2];}

template<class T>
Part canonical(const std::array<T,512>& sig){
  std::set<T> uniq(sig.begin(),sig.end());
  std::map<T,int> ids;
  int i=0; for(auto const& x:uniq) ids[x]=i++;
  Part p{}; for(int s=0;s<512;s++) p[s]=ids[sig[s]];
  return p;
}

Part q0(){
  std::array<int,512> sig{};
  for(int s=0;s<512;s++) sig[s]=unresolved(s);
  return canonical(sig);
}
Part q1(){
  std::array<std::array<int,3>,512> sig{};
  for(int s=0;s<512;s++) sig[s]=label(s);
  return canonical(sig);
}
Part refine(const Part& p){
  using Sig=std::array<int,20>;
  std::array<Sig,512> sig{};
  for(int s=0;s<512;s++){
    sig[s][0]=encodeLabel(s);
    sig[s][1]=p[s];
    for(int e=0;e<EVENT_COUNT;e++) sig[s][2+e]=p[step(s,e)];
  }
  return canonical(sig);
}
Part iterateN(Part p,int n){for(int i=0;i<n;i++)p=refine(p);return p;}
std::pair<Part,int> stable(Part p){
  int rounds=0;
  while(true){
    Part q=refine(p);
    if(q==p) return {p,rounds};
    p=q; rounds++;
  }
}
int blocks(const Part& p){return *std::max_element(p.begin(),p.end())+1;}

long long mergedPairs(const std::array<int,512>& sig){
  std::map<int,long long> c;
  for(int s=0;s<512;s++) c[sig[s]]++;
  long long ans=0;
  for(auto [k,n]:c) ans+=n*(n-1)/2;
  return ans;
}
long long mergedPairsPart(const Part& p){
  std::array<int,512> sig{}; for(int s=0;s<512;s++)sig[s]=p[s];
  return mergedPairs(sig);
}

void writeMap(const std::string& path,const Part& p){
  std::ofstream f(path);
  f<<"state\tblock\n";
  for(int s=0;s<512;s++) f<<s<<"\t"<<p[s]<<"\n";
}

void enumHist(int depth,int maxDepth,State s,const Part& q4,
              long long& count,std::set<State>& reached,std::set<int>& qblocks){
  count++; reached.insert(s); qblocks.insert(q4[s]);
  if(depth==maxDepth) return;
  for(int e=0;e<EVENT_COUNT;e++) enumHist(depth+1,maxDepth,step(s,e),q4,count,reached,qblocks);
}

int main(){
  Part p0=q0(),p1=q1(),p2=refine(p1),p3=iterateN(p1,3);
  auto [p4,rounds]=stable(p1);

  long long hcount=0;
  std::set<State> reached;
  std::set<int> hblocks;
  enumHist(0,4,0,p4,hcount,reached,hblocks);

  if(hcount!=111151){std::cerr<<"history drift "<<hcount<<"\n";return 2;}

  std::array<int,512> vis{};
  for(int s=0;s<512;s++) vis[s]=s&0x7f;

  const std::string out="experiments/mqr-4.66/results";
  writeMap(out+"/cpp_q1_mapping.tsv",p1);
  writeMap(out+"/cpp_q3_mapping.tsv",p3);
  writeMap(out+"/cpp_q4_mapping.tsv",p4);

  std::vector<std::pair<std::string,long long>> rows={
    {"SOURCE_STATES",512},
    {"EVENTS",18},
    {"HISTORIES_0_4",hcount},
    {"DISTINCT_REACHED_SOURCE_STATES",(long long)reached.size()},
    {"Q0_BLOCKS",blocks(p0)},
    {"Q1_BLOCKS",blocks(p1)},
    {"Q2_BLOCKS",blocks(p2)},
    {"Q3_BLOCKS",blocks(p3)},
    {"Q4_BLOCKS",blocks(p4)},
    {"Q4_REFINEMENT_ROUNDS",rounds},
    {"Q3_EQUALS_Q4",p3==p4?1:0},
    {"Q4_HISTORY_BLOCKS",(long long)hblocks.size()},
    {"N1_VISIBLE_MERGED_PAIRS",mergedPairs(vis)},
    {"Q1_MERGED_PAIRS",mergedPairsPart(p1)},
    {"Q3_MERGED_PAIRS",mergedPairsPart(p3)}
  };
  std::ofstream f(out+"/cpp_summary.tsv");
  f<<"metric\tvalue\n";
  for(auto const& [k,v]:rows) f<<k<<"\t"<<v<<"\n";

  std::cout<<"MQR466_CPP_SOURCE_STATES=512\n";
  std::cout<<"MQR466_CPP_HISTORIES="<<hcount<<"\n";
  std::cout<<"MQR466_CPP_Q0_BLOCKS="<<blocks(p0)<<"\n";
  std::cout<<"MQR466_CPP_Q1_BLOCKS="<<blocks(p1)<<"\n";
  std::cout<<"MQR466_CPP_Q2_BLOCKS="<<blocks(p2)<<"\n";
  std::cout<<"MQR466_CPP_Q3_BLOCKS="<<blocks(p3)<<"\n";
  std::cout<<"MQR466_CPP_Q4_BLOCKS="<<blocks(p4)<<"\n";
  std::cout<<"MQR466_CPP_Q4_ROUNDS="<<rounds<<"\n";
  std::cout<<"MQR466_CPP_Q3_EQUALS_Q4="<<(p3==p4?"YES":"NO")<<"\n";
  std::cout<<"MQR466_CPP_VISIBLE_PAIRS="<<mergedPairs(vis)<<"\n";
  std::cout<<"MQR466_CPP_INDEPENDENT=PASS\n";
  return 0;
}
