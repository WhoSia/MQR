// Synthetic variable-mass conservative systems; run with node; no external dependencies.
function run() {
  const cases=[]; const tol=2e-10;
  function near(a,b){if(Math.abs(a-b)>tol)throw Error(`mismatch ${a} ${b}`);}
  for(const eps of [-.1,-.05,0,.05,.1]) for(const A of [.1,.25,.5,.75,1]){
    const N=8192,dt=2*Math.PI/N;let mom=[0,0,0,0],massMin=Infinity;
    for(let i=0;i<N;i++){const y=A*Math.cos((i+.5)*dt),g=Math.sqrt((1-2*eps*y)/(1+2*eps*y)),x=y*g,dx=g*(1-2*eps*y/(1-4*eps*eps*y*y)),w=1+2*eps*y; if(dx<=0||w<=0)throw Error("invalid branch");massMin=Math.min(massMin,(w/dx)**2); for(let j=0;j<4;j++)mom[j]+=dt*w*x**j;}
    near(mom[0],2*Math.PI);near(mom[1]/mom[0],0);near(mom[2]/mom[0],A*A/2);
    if(eps!==0 && Math.sign(mom[3])!==-Math.sign(eps))throw Error("third moment failed separation"); if(eps===0)near(mom[3],0);
    const a=A*Math.sqrt((1-2*eps*A)/(1+2*eps*A)),b=-A*Math.sqrt((1+2*eps*A)/(1-2*eps*A)),p=(1+2*eps*A)/2;
    const h=[0,1,2,3].map(j=>p*a**j+(1-p)*b**j);
    near(h[1],0);near(h[2],A*A);near(h[3],-4*eps*A**4/Math.sqrt(1-4*eps*eps*A*A));
    const D=h[0]*h[2]-h[1]**2, S=(h[0]*h[3]-h[1]*h[2])/D, P=(h[1]*h[3]-h[2]**2)/D;
    const aa=(S+Math.sqrt(S*S-4*P))/2,bb=(S-Math.sqrt(S*S-4*P))/2,pp=(h[1]-bb)/(aa-bb);
    near(aa,a);near(bb,b);near(pp,p);
    cases.push({eps,A,period:mom[0],mean:mom[1]/mom[0],second:mom[2]/mom[0],third:mom[3]/mom[0],massMin});
  }
  return cases;
}
console.log(JSON.stringify(run(),null,2));
