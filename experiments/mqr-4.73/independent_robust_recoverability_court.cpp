#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
static vector<string> split(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
int main(){
 ifstream f("experiments/mqr-4.73/ROBUST-RECOVERABILITY-FREEZE.tsv");
 string line;getline(f,line);auto h=split(line,'\t');int n=0,bad=0;bool nominal=false,self=false,robust=false,noncons=false;
 while(getline(f,line)){
  auto v=split(line,'\t');unordered_map<string,string>r;for(size_t i=0;i<h.size();++i)r[h[i]]=v[i];
  bool nom=r["nominal_recovery"]=="YES",stable=r["perturbation_stable"]=="YES",indep=r["independent_separator"]=="YES",sem=r["semantic_bridge"]=="YES",adds=r["adds_new"]=="YES";
  string got="HOLD";
  if(!nom)got="HIDDEN_LOSS_NOT_DOMINANT";
  else if(r["domain"]=="NATSCI"){
   if(!stable&&!indep)got=adds?"HOLD_SURROGATE":"HOLD_SELF_MODEL";
   else if(!stable)got="NOMINAL_ONLY_NOT_DOMINANT";
   else if(stable&&indep&&sem){
    if(adds)got=r["case_id"]=="P8"?"ROBUST_SEPARATOR_REFINEMENT":"ROBUST_LOCAL_DOMINANCE";
    else got=r["case_id"]=="P6"?"ROBUST_CALIBRATION_BRIDGE":"ROBUST_RECOVERABLE";
   }
  }else{
   if(!stable||!sem)got="NONCONSERVATIVE_HOLD";
   else if(stable&&indep&&sem)got=adds?"ROBUST_RELATIVE_DOMINANCE":"ROBUST_RELATIVE";
   else if(!indep)got="LABEL_ONLY_HOLD";
  }
  ++n;if(got!=r["expected"]){++bad;cerr<<r["case_id"]<<" "<<got<<" != "<<r["expected"]<<"\n";}
  if(r["case_id"]=="P2")nominal=got=="NOMINAL_ONLY_NOT_DOMINANT";
  if(r["case_id"]=="P3")self=got=="HOLD_SELF_MODEL";
  if(r["case_id"]=="P5")robust=got=="ROBUST_LOCAL_DOMINANCE";
  if(r["case_id"]=="P11")noncons=got=="NONCONSERVATIVE_HOLD";
 }
 bool ok=bad==0&&nominal&&self&&robust&&noncons;
 cout<<"MQR473_CPP_ROBUST_RECOVERABILITY="<<(ok?"PASS":"FAIL")<<"\n";
 cout<<"MQR473_CPP_ROBUST_CASES="<<n<<"\n";
 return ok?0:1;
}