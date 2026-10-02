#!/usr/bin/env python3
import math, pathlib, csv

ROOT=pathlib.Path(__file__).resolve().parent

E={0:0.25,1:0.75}
F={0:0.10,1:0.90}
G={0:0.40,1:0.60}

def solve_kernel(src,dst):
    # equations:
    # (1-p0)a + p0 b = q0
    # (1-p1)a + p1 b = q1
    p0,p1=src[0],src[1]
    q0,q1=dst[0],dst[1]
    det=(1-p0)*p1-(1-p1)*p0
    a=(q0*p1-q1*p0)/det
    b=((1-p0)*q1-(1-p1)*q0)/det
    valid=(-1e-12 <= a <= 1+1e-12 and -1e-12 <= b <= 1+1e-12)
    return a,b,valid

def distinct_partition(exp):
    return exp[0] != exp[1]

def bayes_error_equal_prior(exp):
    # optimal binary classification error from one binary observation
    # 1/2 * sum_y min(P0(y),P1(y))
    return 0.5*(min(1-exp[0],1-exp[1])+min(exp[0],exp[1]))

def main():
    aF,bF,vF=solve_kernel(E,F)
    aG,bG,vG=solve_kernel(E,G)

    c3 = distinct_partition(E)
    c4F = vF
    c4G = vG

    errE=bayes_error_equal_prior(E)
    errF=bayes_error_equal_prior(F)
    errG=bayes_error_equal_prior(G)

    out=ROOT/"results";out.mkdir(exist_ok=True)
    with open(out/"stochastic_closure.tsv","w",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["metric","value"])
        for k,v in [
            ("E_PARTITION_DISCRETE",str(c3).upper()),
            ("F_GARBLING_OF_E",str(c4F).upper()),
            ("G_GARBLING_OF_E",str(c4G).upper()),
            ("F_KERNEL_A",f"{aF:.6f}"),
            ("F_KERNEL_B",f"{bF:.6f}"),
            ("G_KERNEL_A",f"{aG:.6f}"),
            ("G_KERNEL_B",f"{bG:.6f}"),
            ("BAYES_ERROR_E",f"{errE:.6f}"),
            ("BAYES_ERROR_F",f"{errF:.6f}"),
            ("BAYES_ERROR_G",f"{errG:.6f}"),
        ]: w.writerow([k,v])

    ok=(c3 and (not c4F) and c4G and abs(aF+0.3)<1e-9 and abs(bF-1.3)<1e-9 and abs(aG-0.3)<1e-9 and abs(bG-0.7)<1e-9 and errF<errE<errG)

    print("MQR470_STOCHASTIC_CLOSURE="+("PASS" if ok else "FAIL"))
    print(f"MQR470_F_KERNEL={aF:.2f},{bF:.2f}")
    print(f"MQR470_G_KERNEL={aG:.2f},{bG:.2f}")
    print(f"MQR470_BAYES_ERRORS={errF:.2f},{errE:.2f},{errG:.2f}")
    print("MQR470_C3_C4_SEPARATION="+("YES" if c3 and not c4F else "NO"))
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
