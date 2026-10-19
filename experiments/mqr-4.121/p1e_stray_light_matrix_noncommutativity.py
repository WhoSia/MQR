"""MQR-4.121 P1E: illustrative intensity-domain matrix correction, not observed spectrometer data."""
from math import log10
def mv(m,v): return [sum(a*b for a,b in zip(row,v)) for row in m]
def inv2(m):
 a,b=m[0];c,d=m[1];det=a*d-b*c
 if abs(det)<1e-14: raise ValueError("singular")
 return [[d/det,-b/det],[-c/det,a/det]]
def absorb(v):
 if min(v)<=0: raise ValueError("nonpositive intensity")
 return [-log10(x) for x in v]
def run():
 M=[[.99,.01],[.02,.98]]
 T=[.01,.5]
 O=mv(M,T)
 corrected=absorb(mv(inv2(M),O))
 wrong=mv(inv2(M),absorb(O))
 target=absorb(T)
 assert max(abs(a-b) for a,b in zip(corrected,target))<1e-12
 assert max(abs(a-b) for a,b in zip(wrong,target))>.1
 return {"true_T":T,"measured_T":O,"true_A":target,"measured_A":absorb(O),"corrected_A":corrected,"wrong_A":wrong,"wrong_error":max(abs(a-b) for a,b in zip(wrong,target))}
if __name__=="__main__": print(run())
