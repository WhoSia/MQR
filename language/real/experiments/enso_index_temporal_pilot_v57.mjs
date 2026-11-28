// Monthly secondary index pilot. Run from any location: node thisfile.mjs [path-to-csv].
import {readFileSync} from 'node:fs';
function pilot(csv){
 const d=csv.trim().split("\n").slice(1).map(l=>{const [year,month,x,s]=l.split(",").map(Number);return {year,month,x,s};});
 if(d.length!==420||d.some((r,i)=>r.year!==1990+Math.floor(i/12)||r.month!==1+i%12||!Number.isFinite(r.x)||!Number.isFinite(r.s)))throw Error("invalid data");
 const blocks=[d.slice(0,180),d.slice(180,300),d.slice(300)];
 const mean=a=>a.reduce((s,x)=>s+x,0)/a.length;
 const corr=(a,b)=>{const m=mean(a),n=mean(b);return a.reduce((s,x,i)=>s+(x-m)*(b[i]-n),0)/Math.sqrt(a.reduce((s,x)=>s+(x-m)**2,0)*b.reduce((s,y)=>s+(y-n)**2,0));};
 function ols(rows,k){const A=Array.from({length:k},()=>Array(k+1).fill(0));for(const r of rows){for(let i=0;i<k;i++){for(let j=0;j<k;j++)A[i][j]+=r.f[i]*r.f[j];A[i][k]+=r.f[i]*r.y;}}for(let i=0;i<k;i++){let p=i;for(let j=i+1;j<k;j++)if(Math.abs(A[j][i])>Math.abs(A[p][i]))p=j;[A[i],A[p]]=[A[p],A[i]];const v=A[i][i];if(Math.abs(v)<1e-10)throw Error("singular");for(let j=i;j<=k;j++)A[i][j]/=v;for(let m=0;m<k;m++)if(m!==i){const z=A[m][i];for(let j=i;j<=k;j++)A[m][j]-=z*A[i][j];}}return A.map(r=>r[k]);}
 const models={climatology:r=>[1],sst:r=>[1,r.x],soi:r=>[1,r.s],both:r=>[1,r.x,r.s],season:r=>[1,r.x,r.s,Math.sin(2*Math.PI*r.month/12),Math.cos(2*Math.PI*r.month/12)]};
 function rows(b,h,f,shift=0){return b.slice(0,b.length-h).map((r,i)=>({f:f({...r,s:b[(i+shift*12)%b.length].s}),y:b[i+h].x,x:r.x}));}
 const rmse=(r,b)=>Math.sqrt(mean(r.map(v=>(v.y-v.f.reduce((s,x,i)=>s+x*b[i],0))**2)));
 const results=[1,3,6].map(h=>{const scores={};for(const [name,f] of Object.entries(models)){const t=rows(blocks[0],h,f),beta=ols(t,t[0].f.length);scores[name]={beta,rmse:blocks.map(b=>rmse(rows(b,h,f),beta))};}scores.persistence={rmse:blocks.map(b=>Math.sqrt(mean(rows(b,h,models.sst).map(r=>(r.y-r.x)**2))))};const shifts=[];for(let j=1;j<10;j++){const t=rows(blocks[0],h,models.both,j),beta=ols(t,3);shifts.push(rmse(rows(blocks[2],h,models.both,j),beta));}return {h,n:blocks.map(b=>b.length-h),scores,shiftTest:shifts};});
 // Exploratory relation features: split SOI at train terciles; freeze cuts, evaluate SST conditional means.
 const ss=blocks[0].map(r=>r.s).sort((a,b)=>a-b),cuts=[ss[59],ss[119]],group=s=>s<=cuts[0]?0:s<=cuts[1]?1:2;
 const groups=blocks.map(b=>[0,1,2].map(i=>{const a=b.filter(r=>group(r.s)===i);return {n:a.length,meanSST:mean(a.map(r=>r.x))};}));
 return {n:d.length,periods:[[1990,2004],[2005,2014],[2015,2024]],correlations:blocks.map(b=>corr(b.map(r=>r.x),b.map(r=>r.s))),results,cuts,groups};
}
const path=process.argv[2]??new URL('../../../research/data/mqr_57_enso_psl_transcribed_1990_2024.csv',import.meta.url);
console.log(JSON.stringify(pilot(readFileSync(path,'utf8')),null,2));
