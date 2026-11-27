function witness(){
const cases=[];
for(const m of [0,1])for(const a of [0,1])for(const b0 of [0,1]){
 const reward=(x,b)=>Number((x^b)===m);
 const history=[{a,b:b0,r:reward(a,b0)}];
 let b=b0;
 if(!history[0].r){b=1-b;history.push({a,b,r:reward(a,b)});}
 const worlds=[0,1].map(h=>({h,feedback:[0,1].map(c=>reward(a,b)),target:[0,1].map(c=>Number((a^b)===(m^(h&c))))}));
 cases.push({m,a,b0,b,history,worlds});
}
const checks={all8:cases.length===8,coordinationAtMost2:cases.every(x=>x.history.length<=2&&x.history.at(-1).r===1),sameFeedbackAcrossWorlds:cases.every(x=>JSON.stringify(x.worlds[0].feedback)===JSON.stringify(x.worlds[1].feedback)),baselineTargetSame:cases.every(x=>x.worlds[0].target[0]===x.worlds[1].target[0]),externalTestSeparates:cases.every(x=>x.worlds[0].target[1]!==x.worlds[1].target[1]),proxyCanSucceedWhileTargetFails:cases.every(x=>x.worlds[1].feedback[1]===1&&x.worlds[1].target[1]===0)};
if(!Object.values(checks).every(Boolean))throw Error("failed");
return {scope:"synthetic common-interest feedback, stipulated roles, stable local action alternatives, privately recognizable success, and independently available target test; not autonomous language invention",cases,checks};
}
console.log(JSON.stringify(witness(),null,2));
