function witness(){
const states=Array.from({length:16},(_,i)=>Array.from({length:4},(_,j)=>(i>>j)&1?1:-1));
const coeff=(f,mask)=>states.reduce((a,s)=>a+f(s)*s.reduce((p,x,i)=>p*((mask>>i)&1?x:1),1),0)/16;
const row=K=>{
const f=s=>Math.log(2*Math.cosh(K*s.reduce((a,b)=>a+b,0)));
const c=Array.from({length:16},(_,i)=>coeff(f,i));
const approx=(s,full)=>c.reduce((a,b,m)=>a+((full||m!==15)?b*s.reduce((p,x,i)=>p*((m>>i)&1?x:1),1):0),0);
const weights=states.map(s=>Math.exp(f(s))), w2=states.map(s=>Math.exp(approx(s,false))), z=weights.reduce((a,b)=>a+b,0),z2=w2.reduce((a,b)=>a+b,0);
return {K,C0:c[0],pair:c[3],four:c[15],formula_four:(Math.log(Math.cosh(4*K))-4*Math.log(Math.cosh(2*K)))/8,max_full_error:Math.max(...states.map(s=>Math.abs(f(s)-approx(s,true)))),max_pairwise_log_error:Math.max(...states.map(s=>Math.abs(f(s)-approx(s,false)))),pairwise_projection_TV:weights.reduce((a,x,i)=>a+Math.abs(x/z-w2[i]/z2),0)/2,odd_max:Math.max(...c.filter((_,m)=>m.toString(2).replace(/0/g,"").length%2===1).map(Math.abs)),pair_spread:Math.max(...[3,5,6,9,10,12].map(m=>Math.abs(c[m]-c[3])))}
};
const rows=[0,.1,.25,.5,1,2,-.5].map(row);
const checks={all_reconstruct:rows.every(r=>r.max_full_error<1e-12),analytic_four:rows.every(r=>Math.abs(r.four-r.formula_four)<1e-12),zero_coupling:Math.abs(rows[0].four)<1e-12,nonzero_four_negative:rows.slice(1).every(r=>r.four<0),odd_symmetry:rows.every(r=>r.odd_max<1e-12),pair_permutation:rows.every(r=>r.pair_spread<1e-12),pairwise_failure:rows.slice(1).every(r=>r.max_pairwise_log_error>1e-8),sign_symmetry:Math.abs(rows[3].four-rows[6].four)<1e-12};
if(!Object.values(checks).every(Boolean))throw Error("witness failed");
return {scope:"finite equilibrium star graph, dimensionless coupling; exact marginal, not an RG critical point or historical reproduction",rows,checks};
}
console.log(JSON.stringify(witness(),null,2));
