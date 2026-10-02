#!/usr/bin/env python3
# Exhaustive finite meta-closure check.
# One visible state v has two compatible worlds:
# CLOSED: no hidden exterior contact.
# OPEN: one hidden admissible exterior contact.

worlds=[
    {"name":"CLOSED","visible":"V0","true_closed":True},
    {"name":"OPEN","visible":"V0","true_closed":False},
]

failures=[]
for cert_value in [False,True]:
    correctness=[cert_value==w["true_closed"] for w in worlds]
    if all(correctness):
        failures.append(cert_value)

ok=(len(failures)==0)
print("MQR471_META_CLOSURE="+("PASS" if ok else "FAIL"))
print("MQR471_VISIBLE_VIEWS=1")
print("MQR471_COMPATIBLE_WORLDS=2")
print("MQR471_VIEW_ONLY_CERTIFIERS=2")
print("MQR471_UNIFORMLY_CORRECT_CERTIFIERS="+str(len(failures)))
print("MQR471_GENERATOR_OUTPUT_COMPLETENESS_UNEARNED="+("YES" if ok else "NO"))
raise SystemExit(0 if ok else 1)
