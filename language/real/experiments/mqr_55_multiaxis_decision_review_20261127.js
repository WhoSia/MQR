function compare(d){
 const w=d.weights;
 const P=v=>v.reduce((s,x,i)=>s+x*w[i],0);
 const geom=v=>v.some(x=>x===0)?0:Math.exp(v.reduce((s,x,i)=>s+w[i]*Math.log(x),0));
 const min=v=>Math.min(...v);
 const dominates=(a,b)=>a.every((x,i)=>x>=b[i])&&a.some((x,i)=>x>b[i]);
 const eligible=d.actions.filter(a=>a.gate);
 const metrics=d.actions.map(a=>({name:a.name,gate:a.gate,P:P(a.v),geo:geom(a.v),bottleneck:min(a.v),P_range:[P(a.low),P(a.high)],geo_range:[geom(a.low),geom(a.high)],min_range:[min(a.low),min(a.high)],dominatedBy:eligible.filter(b=>b!==a&&dominates(b.v,a.v)).map(b=>b.name),robustDominatedBy:eligible.filter(b=>b!==a&&dominates(b.low,a.high)).map(b=>b.name),worstRegret:a.gate?Math.max(0,...eligible.filter(b=>b!==a).map(b=>P(b.high)-P(a.low))):null}));
 const corners=Array.from({length:32},(_,i)=>{const v=w.map((x,j)=>x*(i&(1<<j)?1.2:.8)),s=v.reduce((a,b)=>a+b,0);return v.map(x=>x/s);});
 const wins={};for(const c of corners){const v=eligible.map(a=>({name:a.name,p:a.v.reduce((s,x,i)=>s+x*c[i],0)})).sort((a,b)=>b.p-a.p);wins[v[0].name]=(wins[v[0].name]??0)+1;}
 const selected=metrics.filter(x=>x.gate).sort((a,b)=>a.worstRegret-b.worstRegret)[0];
 const tests={allScoresBounded:d.claims.every(a=>a.v.length===7&&a.v.every(v=>v>=0&&v<=1)),intervalsContainCentral:d.actions.every(a=>a.v.every((x,i)=>0<=a.low[i]&&a.low[i]<=x&&x<=a.high[i]&&a.high[i]<=1)),weightsSum:Math.abs(w.reduce((a,b)=>a+b,0)-1)<1e-12,blockedNotSelected:selected.gate&&selected.name!=="independent matched FinBIF field validation now",tradeoffNotTotal:metrics.filter(x=>x.gate&&x.dominatedBy.length===0).length>1,noncompensation:geom([1,1,0,1,1])===0&&P([1,1,0,1,1])>0,cornerCount:Object.values(wins).reduce((a,b)=>a+b,0)===32};
 if(!Object.values(tests).every(Boolean))throw Error(JSON.stringify(tests));
 return {scope:"local action choice only; subjective independent interval box, not probabilities or empirically calibrated uncertainty. Worst regret max rival upper P minus own lower P; same candidate excluded. Conservative scenario only.",metrics,weightCornerWins:wins,selectedByMinimaxRegret:selected.name,tests};
}
if(typeof require!=="undefined"&&require.main===module){const fs=require('fs');const d=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));console.log(JSON.stringify(compare(d),null,2));}
