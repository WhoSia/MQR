function audit(){
 const gram=R=>Array.from({length:R[0].length},(_,i)=>Array.from({length:R[0].length},(_,j)=>R.reduce((s,r)=>s+r[i]*r[j],0)));
 const eff=R=>{const G=gram(R),t=G.reduce((s,r,i)=>s+r[i],0),q=G.reduce((s,r)=>s+r.reduce((u,x)=>u+x*x,0),0);return q===0?null:t*t/q};
 const tests={zeroUndefined:eff([[0,0]])===null,identity:eff([[1,0],[0,1]])===2,duplicate:eff([[1,0],[0,1],[1,0]])===9/5,scale:eff([[10,0],[0,1]])===10201/10001,newDirection:eff([[1,0,0],[0,1,0],[0,0,10]])===10404/10002,uniformScale:eff([[7,0],[0,7]])===2};
 const duplication=Array.from({length:16},(_,i)=>{const k=i+1;return {copies:k,rank:2,effective:eff([...Array.from({length:k},()=>[1,0]),[0,1]]),analytic:(k+1)**2/(k*k+1)}});
 tests.duplicationExact=duplication.every(x=>x.effective===x.analytic);
 tests.duplicationDecreases=duplication.every((x,i)=>i===0||x.effective<duplication[i-1].effective);
 tests.independentDirectionCanLowerEffectiveRank=eff([[1,0,0],[0,1,0],[0,0,10]])<eff([[1,0,0],[0,1,0]]);
 if(!Object.values(tests).every(Boolean))throw Error(JSON.stringify(tests));
 return {source:"MQR 0.4-C participation-ratio formula",scope:"nonnegative abstract response matrices, not instrument data; exact ranks for displayed diagonal/support examples",zero:"undefined 0/0; no observed response is not absence of vulnerabilities",duplication,examples:{identity:2,oneDuplicate:9/5,scale10:10201/10001,newDirection10:10404/10002},tests};
}
console.log(JSON.stringify(audit(),null,2));
