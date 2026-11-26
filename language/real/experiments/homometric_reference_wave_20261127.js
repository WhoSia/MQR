function checkHomometry(){
 const A=[[0,0],[1,0],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[2,4],[2,5],[3,3],[3,4],[3,5],[4,4],[4,5]];
 const B=[[0,0],[0,1],[1,0],[1,1],[1,2],[1,3],[1,4],[2,2],[2,3],[2,4],[2,5],[3,3],[3,4],[3,5],[4,5]];
 const signature=P=>{const m={};for(const x of P)for(const y of P){const k=`${x[0]-y[0]},${x[1]-y[1]}`;m[k]=(m[k]||0)+1;}return Object.entries(m).sort((a,b)=>a[0].localeCompare(b[0]));};
 const radial=P=>P.map(x=>P.map(y=>(x[0]-y[0])**2+(x[1]-y[1])**2).sort((a,b)=>a-b).join(",")).sort();
 const amp=(P,q)=>P.reduce(([a,b],x)=>{const t=2*Math.PI*(q[0]*x[0]+q[1]*x[1]);return [a+Math.cos(t),b+Math.sin(t)]},[0,0]);
 const I=([a,b])=>a*a+b*b;
 const rows=[];for(let i=0;i<16;i++)for(let j=0;j<16;j++){let q=[i/16,j/16],a=amp(A,q),b=amp(B,q);rows.push({q,a,b,diff:Math.abs(I(a)-I(b)),ref0:Math.abs(I([a[0]+1,a[1]])-I([b[0]+1,b[1]])),ref90:Math.abs(I([a[0],a[1]+1])-I([b[0],b[1]+1]))})}
 const example=rows.find(r=>r.q[0]===.25&&r.q[1]===0);
 const best=rows.reduce((a,b)=>a.ref0+a.ref90>=b.ref0+b.ref90?a:b);
 const recover=([a,b])=>[(I([a+1,b])-I([a,b])-1)/2,(I([a,b+1])-I([a,b])-1)/2];
 const maxRecovery=Math.max(...rows.flatMap(r=>[r.a,r.b].map(z=>Math.max(...recover(z).map((v,i)=>Math.abs(v-z[i]))))));
 const checks={sameCardinality:A.length===B.length&&A.length===15,exactDifferenceMultisets:JSON.stringify(signature(A))===JSON.stringify(signature(B)),notEuclideanCongruent:JSON.stringify(radial(A))!==JSON.stringify(radial(B)),equalDiffraction256:rows.every(r=>r.diff<1e-10),someReferenceSeparates:rows.some(r=>r.ref0>1e-6||r.ref90>1e-6),complexRecovery:maxRecovery<1e-10,zeroModeNoDifference:rows[0].ref0<1e-10&&rows[0].ref90<1e-10};
 if(!Object.values(checks).every(Boolean))throw new Error(JSON.stringify(checks));
 return {source:"Grimm & Baake (2008), Eq. 1, arXiv HTML and PDF page 2 image cross-check",A,B,checks,maxDiff:Math.max(...rows.map(r=>r.diff)),maxRecovery,example,best,nonzeroVectorTypes:signature(A).length-1,scope:"equal unit scatterers, finite point sets, ideal coherent reference of known complex amplitude; no instrument test, no claim of practical crystallographic phasing"};
}
console.log(JSON.stringify(checkHomometry(),null,2));
