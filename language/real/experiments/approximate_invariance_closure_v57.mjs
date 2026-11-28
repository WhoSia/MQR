// Discrete synthetic test of approximate invariance; independent Bernoulli interventions.
function invarianceStudy(){
 const p=Array.from({length:21},(_,i)=>(10+4*i)/100),eps=.05,alpha=.05,rep=40;
 function connected(x){const order=x.map((_,i)=>i).sort((i,j)=>x[i]-x[j]);const groups=[[order[0]]];for(let i=1;i<order.length;i++){if(x[order[i]]-x[order[i-1]]<=eps+1e-12)groups.at(-1).push(order[i]);else groups.push([order[i]]);}return groups;}
 function diameter(x,r){const order=x.map((_,i)=>i).sort((i,j)=>x[i]-x[j]);const groups=[[order[0]]];for(let i=1;i<order.length;i++){const g=groups.at(-1);if(x[order[i]]-x[g[0]]+2*r<=eps+1e-12)g.push(order[i]);else groups.push([order[i]]);}return groups;}
 function evaluate(g){return {k:g.length,max:Math.max(...g.map(z=>Math.max(...z.map(i=>p[i]))-Math.min(...z.map(i=>p[i]))))};}
 const exact={single:evaluate(connected(p)),diameter:evaluate(diameter(p,0))};
 if(exact.single.k!==1||Math.abs(exact.single.max-.8)>1e-12||exact.diameter.k!==11)throw Error("exact mismatch");
 let seed=20261128;function rnd(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;}
 const rows=[];
 for(const n of [250,2500,25000]){const r=Math.sqrt(Math.log(2*p.length/alpha)/(2*n));let cover=0,stats={single:{k:0,max:0,fail:0},point:{k:0,max:0,fail:0},cert:{k:0,max:0,fail:0}};
 for(let t=0;t<rep;t++){const x=p.map(v=>{let s=0;for(let j=0;j<n;j++)s+=+(rnd()<v);return s/n;});cover+=+x.every((v,i)=>Math.abs(v-p[i])<=r);for(const [key,g] of Object.entries({single:connected(x),point:diameter(x,0),cert:diameter(x,r)})){const a=evaluate(g);stats[key].k+=a.k/rep;stats[key].max+=a.max/rep;stats[key].fail+=+(a.max>eps+1e-12);}}rows.push({n,r,cover,stats});}
 // two structural mechanisms have the same single-world interventional marginals but different paired potential outcomes
 const counterfactual=[{name:"Y=U",pairs:[0,1].map(u=>[u,u])},{name:"Y=X xor U",pairs:[0,1].map(u=>[u,1-u])}].map(a=>({name:a.name,marginals:[0,1].map(x=>a.pairs.reduce((s,v)=>s+v[x],0)/2),disagreement:a.pairs.filter(v=>v[0]!==v[1]).length/2,structuralInvariant:a.pairs.every(v=>v[0]===v[1])}));
 if(counterfactual[0].disagreement!==0||counterfactual[1].disagreement!==1)throw Error("counterfactual");
 return {exact,rows,counterfactual,rep,epsilon:eps};
}
console.log(JSON.stringify(invarianceStudy(),null,2));
