#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
static vector<string> split(const string&s,char d){vector<string>o;string x;stringstream ss(s);while(getline(ss,x,d))o.push_back(x);return o;}
int main(){
 ifstream f("experiments/mqr-4.73/RECOVERABILITY-FREEZE.tsv");
 string line; getline(f,line); auto h=split(line,'\t');
 int n=0,bad=0; bool post=false,black=false,self=false,unc=false,noncons=false;
 while(getline(f,line)){
   auto v=split(line,'\t'); unordered_map<string,string> r; for(size_t i=0;i<h.size();++i)r[h[i]]=v[i];
   string w=r["witness"], got="HOLD_UNEARNED"; bool indep=r["model_independent"]=="YES", sem=r["semantic_scope_preserved"]=="YES";
   if(w=="LOSSLESS_INVERSE"&&indep&&sem) got="RECOVERABLE_EXACT";
   else if((w=="CLAIM_SUFFICIENT_DECODER"||w=="CALIBRATION_BRIDGE")&&indep&&sem) got="RECOVERABLE_SCOPE";
   else if(w=="BLACKWELL_GARBLING"&&indep&&sem) got="RECOVERABLE_LOCAL_BASELINE";
   else if(w=="POSTHOC_PREDICTOR") got="NOT_RECOVERABLE_POSTHOC";
   else if(w=="PARTIAL_BRIDGE") got="NOT_RECOVERABLE_HIDDEN_LOSS";
   else if(w=="SUCCESSOR_SELF_MODEL"&&!indep) got="HOLD_MODEL_DEPENDENT";
   else if(w=="LOWER_UNCERTAINTY_ONLY") got="NOT_RECOVERABLE_LOSSY";
   else if((w=="CONSERVATIVE_EXTENSION"||w=="CHECKED_CERTIFICATE")&&indep&&sem) got="RECOVERABLE_RELATIVE";
   else if(w=="NONCONSERVATIVE_EXTENSION") got="NOT_RECOVERABLE_SEMANTIC";
   ++n; if(got!=r["expected"]){++bad; cerr<<r["case_id"]<<" "<<got<<" != "<<r["expected"]<<"\n";}
   if(r["case_id"]=="R3")post=got=="NOT_RECOVERABLE_POSTHOC";
   if(r["case_id"]=="R5")black=got=="RECOVERABLE_LOCAL_BASELINE";
   if(r["case_id"]=="R7")self=got=="HOLD_MODEL_DEPENDENT";
   if(r["case_id"]=="R8")unc=got=="NOT_RECOVERABLE_LOSSY";
   if(r["case_id"]=="R11")noncons=got=="NOT_RECOVERABLE_SEMANTIC";
 }
 bool ok=bad==0&&post&&black&&self&&unc&&noncons;
 cout<<"MQR473_CPP_RECOVERABILITY="<<(ok?"PASS":"FAIL")<<"\n";
 cout<<"MQR473_CPP_RECOVERABILITY_CASES="<<n<<"\n";
 cout<<"MQR473_CPP_POSTHOC_BLOCKED="<<(post?"YES":"NO")<<"\n";
 cout<<"MQR473_CPP_LOWER_UNCERTAINTY_NOT_ENOUGH="<<(unc?"YES":"NO")<<"\n";
 return ok?0:1;
}
