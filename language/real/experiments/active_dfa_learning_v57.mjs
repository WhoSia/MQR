// Literature-based reproduction: Angluin 1987; Rivest-Schapire 1993; Isberner-Steffen 2014. Run with Node; deterministic seeded synthetic teacher.
function runStudy(){
 const alphabet=["0","1"];
 function step(d,w,q=d.start){for(const a of w)q=d.t[q][Number(a)];return q;}
 function accept(d,w){return d.f[step(d,w)];}
 function exactCE(a,b,cap=Infinity){const seen=new Set(),q=[[a.start,b.start,""]];let checked=0;for(let i=0;i<q.length;i++){const [x,y,w]=q[i],key=x+","+y;if(seen.has(key))continue;seen.add(key);checked++;if(a.f[x]!==b.f[y])return {w,checked};if(w.length<cap)for(const z of alphabet)q.push([a.t[x][+z],b.t[y][+z],w+z]);}return {w:null,checked};}
 function minCount(d){const r=[d.start],seen=new Set(r);for(let i=0;i<r.length;i++)for(const x of d.t[r[i]])if(!seen.has(x)){r.push(x);seen.add(x);}let p=d.f.slice();for(;;){const keys=new Map(),next=Array(d.t.length).fill(-1);for(const x of r){const k=[d.f[x],...d.t[x].map(y=>p[y])].join(",");if(!keys.has(k))keys.set(k,keys.size);next[x]=keys.get(k);}let stable=r.every(x=>r.every(y=>(p[x]===p[y])===(next[x]===next[y])));if(stable)return keys.size;p=next;}}
 function learn(mq,eq,mode){
  const S=[""],E=[""],cache=new Map();let eqs=0,oracleChecked=0,actions=0,ceCount=0,maxCE=0,analysisNew=0;
  function ask(w){if(!cache.has(w)){cache.set(w,mq(w));actions+=w.length;}return cache.get(w);}
  const row=w=>E.map(e=>ask(w+e)).join("");
  for(let rounds=0;rounds<10000;rounds++){
    const sr=S.map(row);let changed=false;
    for(const s of S){for(const a of alphabet){const u=s+a;if(!sr.includes(row(u))){S.push(u);changed=true;break;}}if(changed)break;}
    if(changed)continue;
    for(let i=0;i<S.length&&!changed;i++)for(let j=i+1;j<S.length&&!changed;j++)if(sr[i]===sr[j])for(const a of alphabet){const k=E.findIndex(e=>ask(S[i]+a+e)!==ask(S[j]+a+e));if(k>=0){const e=a+E[k];if(E.includes(e))throw Error("inconsistent existing column");E.push(e);changed=true;break;}}
    if(changed)continue;
    const keys=[...new Set(sr)],reps=keys.map(k=>S[sr.indexOf(k)]);
    const h={start:keys.indexOf(row("")),t:reps.map(s=>alphabet.map(a=>keys.indexOf(row(s+a)))),f:reps.map(s=>ask(s))};
    eqs++;const z=eq(h);oracleChecked+=z.checked;if(z.w===null)return {h,mq:cache.size,actions,eqs,oracleChecked,ceCount,maxCE,analysisNew,rows:S.length,cols:E.length};
    const w=z.w;ceCount++;maxCE=Math.max(maxCE,w.length);if(!w.length)throw Error("empty counterexample");
    if(mode==="prefix"){for(let i=0;i<=w.length;i++){const p=w.slice(0,i);if(!S.includes(p))S.push(p);}}
    else if(mode==="suffix"){const n=cache.size,alpha=i=>ask(reps[step(h,w.slice(0,i))]+w.slice(i));let lo=0,hi=w.length,l=alpha(lo),r=alpha(hi);if(l===r)throw Error("not counterexample");while(hi-lo>1){const mid=Math.floor((lo+hi)/2);if(alpha(mid)===l)lo=mid;else hi=mid;}const e=w.slice(hi);if(E.includes(e))throw Error("old discriminator");E.push(e);analysisNew+=cache.size-n;}
    else throw Error("mode");
  }throw Error("nontermination");
 }
 let seed=20261128;const rng=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return Math.floor(seed/4294967296*n);};
 const targets=[];for(const n of [4,8,16,32])for(let i=0;i<8;i++){targets.push({kind:"random",n,start:0,t:Array.from({length:n},()=>[rng(n),rng(n)]),f:Array.from({length:n},()=>rng(2))});}
 for(const n of [4,8,16,32]){targets.push({kind:"cycle",n,start:0,t:Array.from({length:n},(_,i)=>[(i+1)%n,i]),f:Array.from({length:n},(_,i)=>+(i===0))});targets.push({kind:"threshold",n,start:0,t:Array.from({length:n},(_,i)=>[Math.min(i+1,n-1),0]),f:Array.from({length:n},(_,i)=>+(i===n-1))});}
 const results=targets.map(d=>{const a=learn(w=>accept(d,w),h=>exactCE(d,h),"prefix"),b=learn(w=>accept(d,w),h=>exactCE(d,h),"suffix"),minimum=minCount(d);for(const x of [a,b]){if(exactCE(d,x.h).w!==null||x.h.t.length!==minimum)throw Error("incorrect learned DFA");delete x.h;}return {kind:d.kind,n:d.n,minimum,a,b};});
 const d=targets.find(d=>d.kind==="threshold"&&d.n===16);const bounded=learn(w=>accept(d,w),h=>exactCE(d,h,8),"suffix");const hidden=exactCE(d,bounded.h).w;if(hidden===null||hidden.length!==15)throw Error("bound witness failed");
 const sum=(k,m)=>results.reduce((s,r)=>s+r[k][m],0);
 return {results,summary:{targets:results.length,minimumVerified:2*results.length,prefix:{mq:sum("a","mq"),actions:sum("a","actions"),eqs:sum("a","eqs"),oracleChecked:sum("a","oracleChecked")},suffix:{mq:sum("b","mq"),actions:sum("b","actions"),eqs:sum("b","eqs"),oracleChecked:sum("b","oracleChecked")},suffixFewer:results.filter(r=>r.b.mq<r.a.mq).length,suffixEqual:results.filter(r=>r.b.mq===r.a.mq).length,suffixMore:results.filter(r=>r.b.mq>r.a.mq).length,capWitness:{cap:8,hypothesisStates:bounded.h.t.length,counterexample:hidden,actualMinimum:minCount(d)}}};
}
console.log(JSON.stringify(runStudy(),null,2));
