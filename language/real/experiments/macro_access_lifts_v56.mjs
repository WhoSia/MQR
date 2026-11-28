// Exact finite Markov checks using integer weights; node, no dependencies.
function verifyMacro(){
 const weak=[[3n,3n,2n],[1n,1n,6n],[2n,2n,4n]],strong=[[2n,2n,4n],[2n,2n,4n],[2n,2n,4n]],labels=[0,0,1];
 function wordWeight(M,init,word){let v=init.map((a,i)=>labels[i]===word[0]?a:0n);for(const k of word.slice(1)){v=[0,1,2].map(j=>labels[j]===k?v.reduce((sum,x,i)=>sum+x*M[i][j],0n):0n);}return v.reduce((a,b)=>a+b,0n);}
 let checked=0;
 for(let len=1;len<=8;len++)for(let mask=0;mask<2**len;mask++){const word=Array.from({length:len},(_,i)=>(mask>>i)&1);for(const initial of [[1n,1n,0n],[0n,0n,2n]]){if(wordWeight(weak,initial,word)!==wordWeight(strong,initial,word))throw Error("macro word mismatch");checked++;}}
 if(weak[0][2]===weak[1][2]||strong[0][2]!==strong[1][2])throw Error("reset distinction failed");
 // Five states a,b,c,d in A, e in B; paths a->c->e vs b->d->d.
 const next=[2,3,4,3,4], C=[0,0,0,0,1];let a=0,b=1;const traces=[[C[a],C[b]]];for(let t=0;t<2;t++){a=next[a];b=next[b];traces.push([C[a],C[b]]);}
 if(JSON.stringify(traces)!=="[[0,0],[0,0],[1,0]]")throw Error("delayed witness");
 return {exactWordChecks:checked,weakResetExitNumerators:[2,6],strongResetExitNumerators:[4,4],denominator:8,delayedTrace:traces};
}
console.log(JSON.stringify(verifyMacro(),null,2));
