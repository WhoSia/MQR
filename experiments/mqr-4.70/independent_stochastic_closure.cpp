#include <cmath>
#include <iostream>
#include <tuple>
using namespace std;

struct Exp { double p0,p1; };

tuple<double,double,bool> kernel(Exp s, Exp d){
  double det=(1-s.p0)*s.p1-(1-s.p1)*s.p0;
  double a=(d.p0*s.p1-d.p1*s.p0)/det;
  double b=((1-s.p0)*d.p1-(1-s.p1)*d.p0)/det;
  bool valid=(a>=-1e-12 && a<=1+1e-12 && b>=-1e-12 && b<=1+1e-12);
  return {a,b,valid};
}
double err(Exp e){
  return 0.5*(min(1-e.p0,1-e.p1)+min(e.p0,e.p1));
}
int main(){
  Exp E{0.25,0.75},F{0.10,0.90},G{0.40,0.60};
  auto [aF,bF,vF]=kernel(E,F);
  auto [aG,bG,vG]=kernel(E,G);
  bool c3=(E.p0!=E.p1);
  bool ok=c3 && !vF && vG &&
    fabs(aF+0.3)<1e-9 && fabs(bF-1.3)<1e-9 &&
    fabs(aG-0.3)<1e-9 && fabs(bG-0.7)<1e-9 &&
    err(F)<err(E) && err(E)<err(G);
  cout<<"MQR470_CPP_STOCHASTIC_CLOSURE="<<(ok?"PASS":"FAIL")<<"\n";
  cout<<"MQR470_CPP_F_KERNEL="<<aF<<","<<bF<<"\n";
  cout<<"MQR470_CPP_G_KERNEL="<<aG<<","<<bG<<"\n";
  cout<<"MQR470_CPP_C3_C4_SEPARATION="<<((c3&&!vF)?"YES":"NO")<<"\n";
  return ok?0:1;
}