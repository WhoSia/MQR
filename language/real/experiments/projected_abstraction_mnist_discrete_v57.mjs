// Discrete reconstruction of Xia & Bareinboim 2025 Appendix D.2; no MNIST pixels or GAN.
// Author generator: https://github.com/CausalAILab/ProjectedCausalAbstractions/blob/main/src/datagen/color_mnist.py
function run(){
 const pR=z=>z===0?.1:.9;
 function exact(z,light,orRetry=false){
  const r=pR(z), rShade=light?.3:.7,bShade=light?.7:.3;
  const red=r*rShade,blue=(1-r)*bShade,accept=red+blue;
  const retryR=orRetry&&z===1?1:r;
  const retryRed=retryR*rShade/(retryR*rShade+(1-retryR)*bShade);
  const post=red+(1-accept)*retryRed;
  return {z,light,accept,postRed:post,label:.1+.8*post};
 }
 let seed=20261128;function rnd(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;}
 function sim(z,light,orRetry,N){let count=0;for(let i=0;i<N;i++){let flip=rnd()<.1?1:0;let red=z^flip;let shade=rnd()<.7?1:0;while((red?1-shade:shade)!==light){flip=rnd()<.1?1:0;red=orRetry?z|flip:z^flip;shade=rnd()<.7?1:0;}count+=red^(rnd()<.1?1:0);}return count/N;}
 const variants=[];for(const z of [0,1])for(const light of [0,1])for(const orRetry of [false,true]){const v=exact(z,light,orRetry),mc=sim(z,light,orRetry,200000);if(Math.abs(v.label-mc)>.006)throw Error("Monte Carlo mismatch");variants.push({...v,orRetry,mc});}
 // Discrete sufficient statistics for Appendix D.2, no pixels or neural nets.
 const sizes=[1000,3162,10000,31622,100000],trials=30,target=exact(0,1).label;
 const rows=[];for(const n of sizes){let sq=[0,0,0];for(let i=0;i<trials;i++){let a=0,b=0,c=0,d=0,red=0,redN=0,blue=0,blueN=0,red0=0,blue0=0;for(let j=0;j<n;j++){let z=rnd()<.5?0:1,r=z^(rnd()<.1?1:0),l=r?+(rnd()>=.7):+(rnd()<.7),y=r^(rnd()<.1?1:0);if(l){a+=y;b++;if(z===0){c+=y;d++;if(r)red0++;else blue0++;}}if(r){red+=y;redN++;}else{blue+=y;blueN++;}}
 const values=[a/b,c/d,(red/redN*red0+blue/blueN*blue0)/(red0+blue0)];for(let k=0;k<3;k++)sq[k]+=(values[k]-target)**2;}
 rows.push({n,pooled:Math.sqrt(sq[0]/trials),projected:Math.sqrt(sq[1]/trials),fine:Math.sqrt(sq[2]/trials)});}
 if(Math.abs(target-3/22)>1e-12)throw Error("target");
 return {variants,rows,target,pooledPopulation:.34,pooledBias:.34-target,trials,mcN:200000};
}
console.log(JSON.stringify(run(),null,2));
