// Finite exhaustive congruences, canonical forms modulo state and action permutations.
function incompatibleMaxima(){
 function parts(n){let out=[];function f(p,m){if(p.length===n){out.push(p);return;}for(let i=0;i<=m+1;i++)f([...p,i],Math.max(m,i));}f([0],0);return out;}
 const perm=a=>a.length?a.flatMap((x,i)=>perm(a.filter((_,j)=>j!==i)).map(y=>[x,...y])):[[]];
 function canonical(q){let keys=[];for(const p of perm(q[0].map((_,i)=>i)))for(const a of [[0,1],[1,0]]){const inv=p.map((_,i)=>p.indexOf(i));keys.push(JSON.stringify(a.map(i=>p.map(j=>inv[q[i][j]]))));}return keys.sort()[0];}
 function qs(T){let out=new Map;for(const p of parts(T[0].length)){const k=Math.max(...p)+1;let q=T.map(t=>{let a=Array(k).fill(-1);for(let i=0;i<p.length;i++){let v=p[t[i]];if(a[p[i]]!==-1&&a[p[i]]!==v)return null;a[p[i]]=v;}return a;});if(q.some(x=>x===null))continue;let key=canonical(q);if(!out.has(key))out.set(key,{k,p,q});}return out;}
 let seed=5701;function rnd(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return Math.floor(seed/4294967296*n);}
 const draw=n=>[0,1].map(()=>Array.from({length:n},()=>rnd(n)));
 for(let i=0;i<2000;i++){const A=draw(4),B=draw(4),a=qs(A),b=qs(B);let shared=[...a].filter(([key])=>b.has(key));const max=Math.max(...shared.map(([,v])=>v.k));const top=shared.filter(([,v])=>v.k===max);if(max>1&&top.length>1){const witnesses=top.map(([key,v])=>({key,A:v,B:b.get(key)}));return {searchCount:i+1,A,B,max,witnesses,nonIsomorphic:witnesses.length};}}
 throw Error("no witness");
}
console.log(JSON.stringify(incompatibleMaxima(),null,2));
