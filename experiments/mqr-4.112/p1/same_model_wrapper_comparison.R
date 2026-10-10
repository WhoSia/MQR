# MQR-4.112 P1-F: same FER physical data, same JAGS model, old/new wrapper.
# Old upstream AgeS_Computation.R is evaluated verbatim after blob verification.
# The comparison is a stochastic pilot, NOT author-2021 exact environment replication.
options(warn=1, timeout=180)
dir.create("p1f_out",showWarnings=FALSE)
stopifnot(requireNamespace("rjags",quietly=TRUE),
          requireNamespace("BayLum",quietly=TRUE),
          requireNamespace("coda",quietly=TRUE),
          requireNamespace("ArchaeoPhases",quietly=TRUE))
suppressPackageStartupMessages(library(BayLum))
suppressPackageStartupMessages(library(coda))
stopifnot(as.character(packageVersion("BayLum"))=="0.3.3")
sourcepath <- "upstream_BayLum_AgeS_Computation_2021.R"
stopifnot(file.exists(sourcepath))
sourcehash <- trimws(system2("git",c("hash-object",sourcepath),stdout=TRUE))
stopifnot(identical(sourcehash,"8f269dc7d417aaf677b9ab7fba0ba42c71fd45f7"))
histpath <- "p1_out/historical_2021_snapshot_processed.rds"
modernpath <- "p1_out/current_2025_created_data.rds"
stopifnot(file.exists(histpath),file.exists(modernpath))
old_data <- readRDS(histpath)
new_data <- readRDS(modernpath)
samples <- c("FER1","FER3")
stopifnot(identical(as.numeric(old_data$J),c(49,49)),
          identical(as.numeric(old_data$K),as.numeric(new_data$K)))
# Bound measurement arrays: both interfaces will receive exactly old_data.
# Independently confirm old/current numerical source multisets prior to model runs.
for(i in seq_along(samples)){
 sig <- function(x,y) apply(cbind(x,y),1,function(v)
   paste(formatC(signif(v,12),digits=12,format="fg"),collapse="|"))
 stopifnot(identical(sort(sig(old_data$LT[[i]],old_data$sLT[[i]])),
                     sort(sig(new_data$LT[[i]],new_data$sLT[[i]]))))
}
n <- 2L
prior <- rep(c(10,100),n)
bin_per_sample <- rep(1L,n)
cs <- cumsum(bin_per_sample)
theta <- diag(old_data$ddot_env[2,cs] +
              (old_data$ddot_env[1,cs])^2 * old_data$dLab[2,cs])
strata <- matrix(c(rep(1,n),rep(0,n*n)),nrow=n+1,ncol=n,byrow=TRUE)
stopifnot(identical(dim(theta),c(2L,2L)),all(is.finite(theta)),
          identical(dim(strata),c(3L,2L)))
model_obj <- new.env(parent=globalenv())
data("Model_AgeS",package="BayLum",envir=model_obj)
growth <- "AgesMultiCS2_EXPZO"
dist <- "lognormal_A"
model_text <- get("Model_AgeS",envir=model_obj)[[growth]][[dist]]
stopifnot(is.character(model_text),length(model_text)==1L,nchar(model_text)>100L)
# JAGS data compilation mirrors, field-for-field, both original upstream wrappers.
lengths <- vapply(old_data$LT,function(x)nrow(x),integer(1))
offset <- c(0,cumsum(lengths))
make_mat <- function(field,width){
 z <- matrix(0,nrow=sum(old_data$J),ncol=width)
 for(i in seq_len(n)){
   m <- old_data[[field]][[i]]
   z[(offset[i]+1):offset[i+1],seq_len(ncol(m))] <- m
 }
 z
}
jags_data <- list(
 N=make_mat("LT",max(old_data$K)+1L),
 sN=make_mat("sLT",max(old_data$K)+1L),
 IT=make_mat("ITimes",max(old_data$K)),
 sDlab=old_data$dLab[1,],
 J=old_data$J,K=old_data$K,I=n,
 ddot=old_data$ddot_env[1,cs],Gamma=theta,xbound=prior,
 StratiConstraints=strata,index=c(0,cumsum(old_data$J)),
 BinPerSample=bin_per_sample,CSBinPerSample=cs
)
stopifnot(identical(dim(jags_data$N),c(98L,7L)),
          identical(dim(jags_data$sN),c(98L,7L)),
          identical(dim(jags_data$IT),c(98L,6L)),
          all(is.finite(jags_data$N[is.finite(jags_data$N)])))
saveRDS(list(jags_model=model_text,jags_data=jags_data,
             growth=growth,distribution=dist,prior=prior,
             theta=theta,strata=strata,samples=samples),
        "p1f_out/frozen_mathematical_contract.rds")
writeLines(c(paste("source_2021_git_blob",sourcehash),
             paste("current_BayLum",as.character(packageVersion("BayLum"))),
             paste("rjags",as.character(packageVersion("rjags"))),
             paste("runjags",as.character(packageVersion("runjags"))),
             paste("JAGS",as.character(rjags::jags.version())),
             paste("model",growth,dist),
             paste("model_text_md5",unname(tools::md5sum("upstream_BayLum_AgeS_Computation_2021.R"))),
             "same_data_argument=historical_2021_snapshot_processed.rds",
             "same_gamma_prior_strata_model=yes",
             "seed_control=R_only_JAGS_chain_initials_not_explicit",
             "output_only_bridge=2021_list_BayLum_and_ArchaeoPhases_defunct_CredibleInterval",
             "scope=pilot_comparison_not_historical_author_runtime"),
          "p1f_out/contract.txt")
# Preserve historically exact function BODY; only make its historical namespace
# helper accessible without modifying that source or its scientific formulas.
old_env <- new.env(parent=globalenv())
# Original source is checked byte-for-byte above, then patched IN MEMORY in
# POSTERIOR REPORTING ONLY: 2026 ArchaeoPhases removed CredibleInterval.
# The adapted helper operates after coda.samples, never in likelihood/JAGS.
# Preserve exact original file, and record the exact output-only delta.
source_text <- paste(readLines(sourcepath,warn=FALSE),collapse="\n")
old_reporter <- "ArchaeoPhases::CredibleInterval"
occur <- gregexpr(old_reporter,source_text,fixed=TRUE)[[1]]
stopifnot(length(occur)>=4L,all(occur>0))
old_env$p1f_historical_output_interval <- function(x,level,roundingOfValue=3){
  m <- coda::HPDinterval(coda::mcmc(as.numeric(x)),prob=level)
  c(mean(as.numeric(x)),as.numeric(m[1,1]),as.numeric(m[1,2]))
}
adapted_source <- gsub(old_reporter,"p1f_historical_output_interval",source_text,fixed=TRUE)
stopifnot(!grepl(old_reporter,adapted_source,fixed=TRUE))
writeLines(c(
 "2021 inference function source Git blob preserved and verified",
 paste("Output-only CredibleInterval calls replaced:",length(occur)),
 "Historical ArchaeoPhases::CredibleInterval defunct on current CI runtime",
 "Only post-sampling interval reporting reimplemented by coda::HPDinterval",
 "Historical posterior draws and JAGS likelihood/priors untouched",
 "Output interval from old library NOT claimed byte/semantic identical"),
 "p1f_out/historical_output_compatibility_receipt.txt")
eval(parse(text=adapted_source,keep.source=TRUE),envir=old_env)
stopifnot(exists("AgeS_Computation",envir=old_env,inherits=FALSE))
# 2021 code invoked its package-internal list constructor. Modern BayLum
# relocated that constructor inside its wrapper. Rebuild only the output
# container interface, without modifying inference or upstream function text.
old_env$.list_BayLum <- function(...) {
  l <- list(...)
  class(l) <- "BayLum.list"
  l
}
old_fun <- get("AgeS_Computation",envir=old_env,inherits=FALSE)
common <- list(DATA=old_data,SampleNames=samples,Nb_sample=n,
 PriorAge=prior,BinPerSample=bin_per_sample,THETA=theta,
 StratiConstraints=strata,LIN_fit=FALSE,Origin_fit=TRUE,
 distribution=dist,Iter=2000L,t=5L,n.chains=3L,
 jags_method="rjags",quiet=TRUE,SavePdf=FALSE,SaveEstimates=FALSE,
 roundingOfValue=3)
# Identical nominal schedules:
# 2021: n.adapt=2000, update=2000, coda.samples=2000, thin=5.
# Later: adapt=2000, burnin=2000, sample=2000, thin=5.
# Neither gives explicit per-chain JAGS RNG initialisations through these
# historical wrapper signatures. Do NOT interpret small differences causally.
run <- function(label,invoke){
 cat("P1F RUN_START",label,"\n");flush.console()
 set.seed(4112L)
 out <- invoke()
 stopifnot(inherits(out,"BayLum.list"),!is.null(out$Sampling),!is.null(out$Ages))
 saveRDS(out,paste0("p1f_out/",label,"_actual_posterior.rds"))
 m <- as.matrix(out$Sampling)
 stopifnot(ncol(m)>=n,all(is.finite(m[,seq_len(n),drop=FALSE])))
 df <- data.frame(wrapper=label,sample=samples,
    age_mean_ka=vapply(seq_len(n),function(i)mean(m[,i]),numeric(1)),
    age_sd_ka=vapply(seq_len(n),function(i)sd(m[,i]),numeric(1)),
    q025_ka=vapply(seq_len(n),function(i)unname(quantile(m[,i],.025)),numeric(1)),
    q975_ka=vapply(seq_len(n),function(i)unname(quantile(m[,i],.975)),numeric(1)),
    draws=nrow(m),stringsAsFactors=FALSE)
 print(df)
 write.csv(df,paste0("p1f_out/",label,"_age_summary.csv"),row.names=FALSE)
 cat("P1F RUN_DONE",label,"\n")
 df
}
# Direct invocation (not a modified scientific function). Historical code
# can depend on old package helper interfaces; failure must remain visible.
old_res <- tryCatch(run("historical_exact_source",function() old_fun(
 DATA=old_data,SampleNames=samples,Nb_sample=n,
 PriorAge=prior,BinPerSample=bin_per_sample,THETA=theta,
 StratiConstraints=strata,LIN_fit=FALSE,Origin_fit=TRUE,
 distribution=dist,Iter=2000L,t=5L,n.chains=3L,
 jags_method="rjags",quiet=TRUE,SavePdf=FALSE,SaveEstimates=FALSE,
 roundingOfValue=3)),
 error=function(e){writeLines(conditionMessage(e),"p1f_out/historical_error.txt");
                   stop(e)})
new_res <- run("modern_scheduled_match",function() BayLum::AgeS_Computation(
 DATA=old_data,SampleNames=samples,Nb_sample=n,
 PriorAge=prior,BinPerSample=bin_per_sample,THETA=theta,
 StratiConstraints=strata,LIN_fit=FALSE,Origin_fit=TRUE,
 distribution=dist,Iter=2000L,t=5L,n.chains=3L,
 jags_method="rjags",quiet=TRUE,SavePdf=FALSE,SaveEstimates=FALSE,
 roundingOfValue=3,adapt=2000L,burnin=2000L,autorun=FALSE))
comparison <- merge(old_res,new_res,by="sample",suffixes=c("_historical","_modern"))
comparison$delta_ka <- comparison$age_mean_ka_modern -
                       comparison$age_mean_ka_historical
write.csv(comparison,"p1f_out/same_model_wrapper_comparison.csv",row.names=FALSE)
print(comparison)
cat("P1F_REAL_HISTORICAL_WRAPPER_AND_MODERN_WRAPPER_EXECUTED",nrow(comparison),"\n")
cat("P1F_INTERPRETATION: stochastic pilot; posterior sameness and published FER3 replication NOT independently proven\n")
