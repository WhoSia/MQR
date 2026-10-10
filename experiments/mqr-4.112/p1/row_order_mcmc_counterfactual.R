# MQR-4.112 P1-D: same BayLum 0.3.3/JAGS model under source-preserving
# 2021-vintage preprocessing vs modern order. Original values kept unchanged.
# Two observed original FER cohorts. No synthetic substitute or claim of 2021 model version.
options(warn=1)
stopifnot(requireNamespace("BayLum"),requireNamespace("rjags"),
          requireNamespace("coda"),requireNamespace("Luminescence"))
old<-readRDS("p1_out/historical_2021_snapshot_processed.rds")
new<-readRDS("p1_out/current_2025_created_data.rds")
samples<-c("FER1","FER3")
cat("P1_CTR MODEL_BEGIN historical vs modern, BayLum",
    as.character(packageVersion("BayLum")),"JAGS",
    as.character(rjags::jags.version()),"\n")
stopifnot(all(old$J==49),all(new$J==49),identical(as.numeric(old$K),as.numeric(new$K)),
          identical(as.numeric(old$dLab),as.numeric(new$dLab)),
          identical(as.numeric(old$ddot_env),as.numeric(new$ddot_env)))
aligned <- new
for(i in seq_along(samples)){
  signature <- function(lt,slt) apply(cbind(lt,slt),1,function(row)
              paste(formatC(signif(row,12),digits=12,format="fg"),collapse="|"))
  a<-signature(old$LT[[i]],old$sLT[[i]])
  b<-signature(new$LT[[i]],new$sLT[[i]])
  stopifnot(identical(sort(a),sort(b)))
  m<-match(a,b)
  stopifnot(length(unique(m))==length(m),!anyNA(m))
  for (f in c("LT","sLT","ITimes","regDose")) {
    aligned[[f]][[i]] <- new[[f]][[i]][m,,drop=FALSE]
    delta<-abs(old[[f]][[i]]-aligned[[f]][[i]])
    matches<-all(is.finite(delta))&&all(delta<1e-10)
    cat("SOURCE_GRAIN_ROW_ALIGNED",samples[i],f,"MATCH",matches,
        "maxDelta",if(all(is.finite(delta)))max(delta) else NA_real_,"\n")
    if(!matches)stop(paste("Cannot admit age counterfactual without numerical parity:",samples[i],f))
  }
}
stopifnot(all(old$J==aligned$J),all(old$K==aligned$K))
cat("P1_COMPLETE_NUMERICAL_MODEL_INPUT_PARITY_PASS: all statistical fields identical under exactly one grain-row permutation per cohort\n")
writeLines("P1_COMPLETE_NUMERICAL_MODEL_INPUT_PARITY=PASS",
           "p1_out/full_row_key_aligned_verdict.txt")
saveRDS(aligned,"p1_out/new_input_aligned_to_historical_rows.rds")
# Two real stochastic MCMC runs with identical algorithm, params, real original source.
# This is a *sensitivity contrast*, not exactly reproduced original 2021 R/JAGS.
AgeS_Computation <- BayLum::AgeS_Computation
run_case <- function(dat,label){
  set.seed(4112001L)
  cat("P1_MCMC_BEGIN",label,"\n")
  result<-AgeS_Computation(DATA=dat,SampleNames=samples,Nb_sample=2,
      PriorAge=rep(c(10,100),2),BinPerSample=rep(1,2),
      SavePdf=FALSE,SaveEstimates=FALSE,
      THETA=matrix(numeric(),nrow=0,ncol=1),StratiConstraints=numeric(),
      LIN_fit=FALSE,Origin_fit=TRUE,distribution="lognormal_A",
      Iter=2000,burnin=4000,adapt=1000,t=5,n.chains=3,
      jags_method="rjags",quiet=TRUE,roundingOfValue=3)
  stopifnot(inherits(result,"BayLum.list"),nrow(result$Ages)==2,
            all(is.finite(result$Ages$AGE)))
  write.csv(result$Ages,file.path("p1_out",paste0(label,"_age.csv")),row.names=FALSE)
  cat("P1_ACTUAL_MCMC_RESULT",label,"\n");print(result$Ages)
  ch<-coda::mcmc.list(lapply(result$Sampling,function(s)coda::mcmc(as.matrix(s))))
  print(coda::gelman.diag(ch,multivariate=FALSE))
  saveRDS(list(Ages=result$Ages,Sampling=result$Sampling),
     file.path("p1_out",paste0(label,"_posterior_draws.rds")))
  invisible(result$Ages)
}
hist <- run_case(old,"source_2021_rows")
modern <- run_case(new,"modern_2025_rows")
delta<-modern$AGE-hist$AGE
cat("P1_AFTER_TRUE_MCMC_ROW_ORDER_SHIFT_KA FER1",delta[1],"FER3",delta[2],"\n")
write.csv(data.frame(sample=samples,source_age_ka=hist$AGE,modern_age_ka=modern$AGE,
                     delta_ka=delta),"p1_out/mcmc_row_order_effect.csv",row.names=FALSE)
cat("MCMC ran actual old-vs-modern source matrices, no test of 2021 legacy JAGS model itself.\n")
