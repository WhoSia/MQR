"""MQR 4.122 P4: geometric nonidentification from fixed volume (mathematical model only).

Independent closed-form vs midpoint checks for radial missing shells in an ideal
sphere and a centered point-source inverse-square kernel. Not BEST hardware.
No experimental source, shielding, or assembly instructions.
"""
import math

R=0.6675
VREMOVED=0.0150
BEST_INNER_VOL=1.22545
BEST_INNER_L_CM=52.03

def sphere_volume(radius):
    return 4*math.pi*radius**3/3

def endpoint_for_equal_volume(start):
    return (start**3+3*VREMOVED/(4*math.pi))**(1/3)

def removed_path_exact(start,end):
    return end-start

def removed_path_midpoint(start,end,n=50000):
    dr=(end-start)/n
    return sum((4*math.pi*(start+(i+.5)*dr)**2*dr)/
               (4*math.pi*(start+(i+.5)*dr)**2)
               for i in range(n))

def run():
    exact_full_path_cm=R*100
    original_full_vol=sphere_volume(R)
    b_near=endpoint_for_equal_volume(.10)
    b_far=endpoint_for_equal_volume(.50)
    results=[]
    for kind,a,b in (("near",.10,b_near),("far",.50,b_far)):
        assert b<R
        removed_vol=sphere_volume(b)-sphere_volume(a)
        removed_len=removed_path_exact(a,b)
        numeric=removed_path_midpoint(a,b)
        assert abs(removed_vol-VREMOVED)<1e-12
        assert abs(numeric-removed_len)<1e-12
        results.append((kind,removed_vol,(R-removed_len)*100,removed_len*100,a,b))
    near,far=results
    assert far[2]-near[2]>6.0
    assert abs((original_full_vol-VREMOVED)-(original_full_vol-VREMOVED))<1e-12
    print("MQR_4122_P4_EQUAL_VOLUME_LOCATION_COUNTEREXAMPLE=PASS")
    print(f"ideal_full_volume_m3={original_full_vol:.9f}")
    print(f"both_toy_volume_m3={original_full_vol-VREMOVED:.9f}")
    for kind,volume,path,loss,a,b in results:
        print(f"{kind}_removed_volume_m3={volume:.9f} "
              f"{kind}_path_cm={path:.6f} "
              f"{kind}_lost_path_cm={loss:.6f}")
    print(f"path_separation_cm={far[2]-near[2]:.6f}")
    print(f"BEST_published_inner_volume_m3={BEST_INNER_VOL:.5f}")
    print(f"BEST_published_inner_effective_length_cm={BEST_INNER_L_CM:.2f}")
    print("MQR_4122_P4_ACTUAL_BEST_TARGET_SHAPE=HOLD")
    print("MQR_4122_P4_ACTUAL_BEST_PATH_REPLICATION=HOLD")

if __name__=="__main__":
    run()
