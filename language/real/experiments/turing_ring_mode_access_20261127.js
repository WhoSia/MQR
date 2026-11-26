// Standard linear stability example; no physical chemistry protocol or biological prediction.
function runWitness(){
 const J={a:1,b:-2,c:2,d:-3};
 function mode(q,du=1,dv=10){
  const a=J.a-du*q,d=J.d-dv*q,tr=a+d,det=a*d-J.b*J.c,disc=tr*tr-4*det;
  return {q,trace:tr,det,maxReal:disc>=0?(tr+Math.sqrt(disc))/2:tr/2};
 }
 function ring(n,du=1,dv=10){
  const rows=Array.from({length:n},(_,m)=>({m,...mode(4*Math.sin(Math.PI*m/n)**2,du,dv)}));
  return {n,unstable:rows.filter(x=>x.maxReal>1e-12).map(x=>x.m),peak:rows.reduce((a,b)=>a.maxReal>=b.maxReal?a:b),rows};
 }
 function check(ok,label){if(!ok)throw new Error(label);return label}
 const rings=[6,10,14,20,40].map(n=>ring(n));
 const checks=[
 check(mode(0).maxReal===-1,"homogeneous equilibrium locally stable"),
 check(Math.abs(mode(.2).det)<1e-12&&Math.abs(mode(.5).det)<1e-12,"analytic determinant roots .2 and .5"),
 check(mode(.35).maxReal>0,"continuum finite band nonempty"),
 check(rings.every(r=>r.rows.every(x=>(x.maxReal>1e-12)===(x.q>.2+1e-12&&x.q<.5-1e-12))),"spectral calculation agrees with determinant criterion on every enumerated mode"),
 check(JSON.stringify(rings.slice(0,4).map(r=>r.unstable))===JSON.stringify([[],[1,9],[],[2,18]]),"fixed-spacing cycle geometry changes accessible instability nonmonotonically"),
 check([6,10,14,20,40].every(n=>ring(n,1,1).unstable.length===0),"equal diffusion negative control"),
 check([6,10,14,20,40].every(n=>ring(n,0,0).unstable.length===0),"no diffusion negative control"),
 check(rings.every(r=>r.unstable.every(m=>r.unstable.includes(r.n-m))),"conjugate modes paired")
 ];
 return {status:"synthetic linearized dimensionless model; no nonlinear saturation or empirical claims",J,D:[1,10],band:[.2,.5],checks,rings:rings.map(({n,unstable,peak})=>({n,unstable,peak}))};
}
console.log(JSON.stringify(runWitness(),null,2));
