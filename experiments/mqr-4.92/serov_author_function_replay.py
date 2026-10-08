#!/usr/bin/env python3
"""MQR 4.92: bounded replay of author-defined Serov 2026 risk estimators.

This program verifies the public author's source file against a frozen Git blob,
then executes only the unmodified AST function definitions essential to
MCE and KMM risk estimators on an explicitly SYNTHETIC fixed fixture.
No model training, paper-table reproduction or inference about KMM superiority.
"""
import ast
import hashlib
import json
import math
from pathlib import Path
from urllib.request import Request, urlopen

SOURCE_ROOT = "Serov-Koldasbayeva-Zaytsev-2026"
REPO = "egorser0v/Importance-reweighting"
COMMIT = "46c4d011c9f0cd0614c08e7edb68ac2491f659c8"
FILE = "source/estimations.py"
GIT_BLOB_SHA1 = "9ce9a0c4639bdce4faace03a4b9236e92aa0f446"
FUNCTIONS = ("MCE","compute_rbf","adjust_sigma","kernel_mean_matching","KMM_error")
OUT = Path("mqr492-serov-source-probe.json")

def verified_original_code():
    url = f"https://raw.githubusercontent.com/{REPO}/{COMMIT}/{FILE}"
    req = Request(url, headers={"User-Agent":"MQR492-source-attested-risk/1.0"})
    with urlopen(req, timeout=35) as response:
        data = response.read(90_000)
    if len(data) > 20_000:
        raise ValueError("bounded upstream file unexpectedly large")
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + bytes([0]) + data).hexdigest()
    if blob != GIT_BLOB_SHA1:
        raise ValueError(f"upstream source identity mismatch: {blob}")
    return data.decode("utf-8")

def source_functions(source):
    import numpy as np
    from scipy.special import logsumexp
    from cvxopt import matrix, solvers
    tree = ast.parse(source, filename=FILE)
    defs = {n.name:n for n in tree.body if isinstance(n, ast.FunctionDef)}
    if any(name not in defs for name in FUNCTIONS):
        raise ValueError("expected original estimator function missing")
    module = ast.Module(body=[defs[k] for k in FUNCTIONS], type_ignores=[])
    ast.fix_missing_locations(module)
    env = {"np":np,"logsumexp":logsumexp,"matrix":matrix,"solvers":solvers}
    # These are exact publisher function ASTs, with dependency imports supplied
    # separately; no statements or argument values are changed.
    exec(compile(module, FILE, "exec"), env, env)
    solvers.options["show_progress"] = False
    return env

def main():
    import numpy as np
    original = verified_original_code()
    fn = source_functions(original)
    rng = np.random.default_rng(492)
    # Deliberately separate source/target feature distributions; labels generated
    # from one fixed positive synthetic loss function, never paper species data.
    g = rng.normal(loc=[0.0,0.2],scale=[0.8,0.75],size=(24,2))
    p = rng.normal(loc=[0.95,-0.45],scale=[0.7,0.65],size=(24,2))
    loss = lambda X: 0.35 + (0.28*X[:,0]-0.17*X[:,1]-0.1)**2
    log_loss = lambda X: np.log(loss(X))
    cap = 10.0
    weights = fn["kernel_mean_matching"](p,g,kern="rbf",B=cap)
    kmm_log = float(fn["KMM_error"](log_loss,p,g,cap))
    source_log = float(fn["MCE"](log_loss,g))
    target_oracle_log = float(fn["MCE"](log_loss,p))
    if len(weights)!=len(g) or not np.all(np.isfinite(weights)):
        raise AssertionError("bad upstream QP weights")
    if np.any(weights < -1e-8) or np.any(weights > cap+1e-8):
        raise AssertionError("upstream QP violated source weight cap")
    expected_kmm = float(np.dot(weights,loss(g))/len(g))
    if not math.isclose(math.exp(kmm_log),expected_kmm,rel_tol=1e-10,abs_tol=1e-12):
        raise AssertionError("source KMM error does not match independent weighted-loss sum")
    if not math.isclose(math.exp(source_log),float(np.mean(loss(g))),rel_tol=1e-10):
        raise AssertionError("source MCE does not match unweighted source risk")
    if not math.isclose(math.exp(target_oracle_log),float(np.mean(loss(p))),rel_tol=1e-10):
        raise AssertionError("source target oracle does not match target loss mean")
    if math.isclose(expected_kmm,math.exp(source_log),rel_tol=1e-9):
        raise AssertionError("test fixture failed to exercise nonuniform reweighting")
    out = {"study_root":SOURCE_ROOT,"repository":REPO,"commit":COMMIT,
      "file":FILE,"git_blob_sha1":GIT_BLOB_SHA1,
      "source_status":"FROZEN_UPSTREAM_ORIGINAL_FUNCTIONS_EXECUTED",
      "experiment_class":"PREDECLARED_SYNTHETIC_ESTIMATOR_SMOKE_TEST",
      "source_n":len(g),"target_n":len(p),"loss":"quadratic_positive_synthetic",
      "metrics":{"MCE_g_source_unweighted_risk":math.exp(source_log),
          "KMM_source_reweighted_risk":math.exp(kmm_log),
          "MCE_p_true_target_oracle_risk":math.exp(target_oracle_log)},
      "upstream_weight":{"min":float(np.min(weights)), "max":float(np.max(weights)),
          "sum":float(np.sum(weights))},
      "numerical_checks":{"KMM_literal_source_matches_independent_weighted_sum":True,
          "MCE_g_matches_source_mean":True,
          "MCE_p_matches_target_oracle_mean":True},
      "nonadmissions":[
         "Not a paper-specific empirical dataset replay",
         "Not proof of KMM superiority or source risk correction",
         "True target loss oracle is not a deployment estimator",
         "Serov risk estimates must not be pooled with Matsui external AUC",
         "24 rows per population are an intentionally synthetic numerical smoke test"]}
    OUT.write_text(json.dumps(out,indent=2),encoding="utf8")
    print("MQR492_UPSTREAM_SEROV_PINNED_SOURCE=PASS")
    print("MQR492_SOURCE_RISK_ESTIMATOR_REPLAY="+json.dumps(out["metrics"],sort_keys=True))
    print("MQR492_INDEPENDENT_ESTIMATOR_NUMERICAL_CHECK=PASS")

if __name__=="__main__":
    main()
