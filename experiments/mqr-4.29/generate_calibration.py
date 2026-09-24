#!/usr/bin/env python3
from __future__ import annotations
import itertools,random
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"experiments"/"mqr-4.29"/"generated"
OUT.mkdir(parents=True,exist_ok=True)

HEAD=["lane","id","w_success","w_total","w_repeat_decoy","n_lineages","n_replicate_decoy",
      "i_invariant","i_total","i_rival_count_decoy","t_success","t_total","t_train_decoy",
      "d_covered","d_total","d_challenge_decoy"]
KEY=["lane","id","W","N","I","T","D","L_W","L_N","L_I","L_T","L_D"]

def write(path,head,rows):
    path.write_text("\t".join(head)+"\n"+"\n".join("\t".join(map(str,r)) for r in rows)+"\n",encoding="utf-8")

exact_levels=[.25,.50,1.00]
noisy_levels=[.20,.50,.80]
public=[]; public_decoy=[]; key=[]
idx=0
for combo in itertools.product(range(3),repeat=5):
    eid=f"E{idx:03d}"
    vals=[exact_levels[i] for i in combo]
    counts=[int(v*4) for v in vals]
    rng=random.Random(112358+idx)
    dec=[rng.randint(5,50) for _ in range(5)]
    row=["exact",eid,counts[0],4,dec[0],counts[1],dec[1],counts[2],4,dec[2],counts[3],4,dec[3],counts[4],4,dec[4]]
    public.append(row)
    public_decoy.append(["exact",eid,counts[0],4,1000+idx,counts[1],2000+idx,counts[2],4,3000+idx,counts[3],4,4000+idx,counts[4],4,5000+idx])
    key.append(["exact",eid,*[f"{v:.6f}" for v in vals],*combo])
    idx+=1

idx=0
for combo in itertools.product(range(3),repeat=5):
    eid=f"N{idx:03d}"
    latent=[noisy_levels[i] for i in combo]
    obs=[]
    for a,p in enumerate(latent):
        rng=random.Random(20260924+idx*1009+a*9176)
        n=64
        obs.append(sum(rng.random()<p for _ in range(n)))
    rng=random.Random(271828+idx)
    dec=[rng.randint(5,80) for _ in range(5)]
    row=["noisy",eid,obs[0],64,dec[0],obs[1],dec[1],obs[2],64,dec[2],obs[3],64,dec[3],obs[4],64,dec[4]]
    public.append(row)
    public_decoy.append(["noisy",eid,obs[0],64,10000+idx,obs[1],11000+idx,obs[2],64,12000+idx,obs[3],64,13000+idx,obs[4],64,14000+idx])
    key.append(["noisy",eid,*[f"{v:.6f}" for v in latent],*combo])
    idx+=1

write(OUT/"public.tsv",HEAD,public)
write(OUT/"public_decoy.tsv",HEAD,public_decoy)
write(OUT/"hidden_key.tsv",KEY,key)

print("BASE_WORLDS=243")
print("LANES=2")
print("PUBLIC_ROWS=486")
print("HIDDEN_KEY_SEPARATE=PASS")
print("DECOY_TWIN_ROWS=486")
