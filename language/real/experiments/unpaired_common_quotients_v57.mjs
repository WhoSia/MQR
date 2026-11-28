// Exhaustive small finite deterministic systems; Node, no dependencies.
function bridgeTrial(){
 function partitions(n){const out=[];function f(p,max){if(p.length===n){out.push(p);return;}for(let k=0;k<=max+1;k++)f([...p,k],Math.max(max,k));}f([0],0);return out;}
 function quotients(T){return partitions(T[0].length).flatMap(p=>{let k=Math.max(...p)+1;let q=T.map(t=>{let a=Array(k).fill(-1);for(let i=0;i<p.length;i++){let v=p[t[i]];if(a[p[i]]!==-1&&a[p[i]]!==v)return null;a[p[i]]=v;}return a;});return q.some(x=>x===null)?[]:[{p,k,q}];});}
 function perm(a){return a.length===0?[[]]:a.flatMap((v,i)=>perm(a.filter((_,j)=>j!==i)).map(x=>[v,...x]));}
 function solve(A,B){let qa=quotients(A),qb=quotients(B),best=0,solutions=[];const ap=perm(A.map((_,i)=>i));for(const a of qa)for(const b of qb){if(a.k!==b.k||a.k<best)continue;for(const s of perm(Array.from({length:a.k},(_,i)=>i)))for(const r of ap){if(a.q.every((t,i)=>t.every((v,j)=>s[v]===b.q[r[i]][s[j]]))){if(a.k>best){best=a.k;solutions=[];}solutions.push({a:a.p,b:b.p,s,r});}}}return {best,solutions,qa:qa.length,qb:qb.length};}
 // Independent local refinements of an asymmetric 3-state action system.
 // No pairing or quotient is passed to solve.
 const A=[[1,2,0,2],[0,0,1,1]], B=[[2,2,2,2,0,0],[4,5,1,0,2,3]];
 // Build guaranteed planted positive with independent naming and local refinements.
 const Q=[[1,2,0],[0,0,1]];
 function lift(groups,actions,offset){const n=groups.length;return actions.map((a,j)=>groups.map((g,i)=>{const targets=groups.map((h,k)=>h===Q[a][g]?k:-1).filter(k=>k>=0);return targets[(i+j+offset)%targets.length];}));}
 const ga=[2,0,1,0],gb=[1,2,0,2,1,0],aa=[0,1],ab=[1,0];const X=lift(ga,aa,0),Y=lift(gb,ab,1);
 const pos=solve(X,Y);
 const planted=pos.solutions.some(z=>ga.every((g,i)=>gb.every((h,j)=>(g===h)===(z.s[z.a[i]]===z.b[j])))&&aa.every((a,i)=>ab[z.r[i]]===a));
 if(pos.best!==3||!planted)throw Error("positive failure");
 const symmetric=solve([[1,0],[0,1]],[[0,1],[1,0]]);
 if(symmetric.best!==2||symmetric.solutions.length!==2)throw Error("symmetry failure");
 const incompatible=solve([[1,0],[0,1]],[[0,0],[1,1]]);
 if(incompatible.best!==1)throw Error("incompatible failure");
 // Cross-world duplicate has identical local tables; solver cannot infer co-reference.
 const duplicate=solve(X,Y);if(JSON.stringify(pos)!==JSON.stringify(duplicate))throw Error("duplicate result mismatch");
 let seed=20261128;function next(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return Math.floor(seed/4294967296*n);}
 let hist={1:0,2:0,3:0,4:0},ambig=0,nontrivial=0;
 for(let i=0;i<64;i++){const R=n=>[0,1].map(()=>Array.from({length:n},()=>next(n)));const z=solve(R(4),R(5));hist[z.best]++;if(z.best>1){nontrivial++;if(z.solutions.length>1)ambig++;}}
 return {positive:{X,Y,...pos,planted},symmetric,incompatible,duplicateSame:true,independentPairs:{n:64,hist,nontrivial,ambig}};
}
console.log(JSON.stringify(bridgeTrial(),null,2));
