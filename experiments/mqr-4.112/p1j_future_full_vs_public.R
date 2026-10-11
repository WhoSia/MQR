# MQR-4.112 P1-J: run source-matched full versus public JAGS posterior,
# but ONLY after a truly NEW, independently provenance-checked full cohort
# and its grain->JAGS row witness are supplied. No synthetic full grains.
options(warn=1)
stopifnot(requireNamespace("rjags"),requireNamespace("coda"))
args<-commandArgs(trailingOnly=TRUE)
if(length(args)!=3L)stop(paste(
 "USAGE: Rscript p1j_future_full_vs_public.R",
 "<genuine_author_full_contract.rds> <full_physical_row_bridge.csv>",
 "<original_full_source_custody_receipt.txt>"))
full_file<-args[1]
bridge_file<-args[2]
receipt_file<-args[3]
for(path in c(full_file,bridge_file,receipt_file)){
 if(!file.exists(path))stop("SOURCE_NOT_ACQUIRED: ",path)
}
receipt<-readLines(receipt_file,warn=FALSE)
# A receipt is a provenance *claim*, not certification. Review the author's
# signed transmission and file checksums externally before admission.
stopifnot(any(grepl("^FULL_ORIGINAL_SOURCE_INDEPENDENTLY_REVIEWED=YES$",receipt)),
          any(grepl("^ORIGINAL_BIN_FILES_SHA256=",receipt)),
          any(grepl("^ORIGINAL_AUTHOR_SOURCE_LINK=",receipt)))
public<-readRDS("p1f_out/frozen_mathematical_contract.rds")
full<-readRDS(full_file)
pubkey<-read.csv("p1j_out/public_key_to_jags_bridge.csv")
fullkey<-read.csv(bridge_file)
stopifnot(identical(pubkey$sample,c(rep("FER1",49L),rep("FER3",49L))),
          identical(as.integer(public$jags_data$J),c(49L,49L)),
          identical(as.character(full$samples),as.character(public$samples)),
          identical(full$jags_model,public$jags_model),
          identical(full$growth,public$growth),
          identical(full$distribution,public$distribution),
          identical(as.numeric(full$prior),as.numeric(public$prior)),
          identical(full$theta,public$theta),
          identical(full$strata,public$strata))
a<-public$jags_data
b<-full$jags_data
stopifnot(length(b$J)==2L,all(b$J>49L),
          identical(as.integer(b$K),as.integer(a$K)),
          identical(as.numeric(b$xbound),as.numeric(a$xbound)),
          identical(as.numeric(b$ddot),as.numeric(a$ddot)),
          identical(b$Gamma,a$Gamma),
          identical(b$StratiConstraints,a$StratiConstraints),
          identical(as.numeric(b$sDlab),as.numeric(a$sDlab)),
          identical(as.integer(b$BinPerSample),as.integer(a$BinPerSample)),
          identical(as.integer(b$CSBinPerSample),as.integer(a$CSBinPerSample)),
          identical(as.integer(b$I),as.integer(a$I)),
          nrow(b$N)==sum(b$J),nrow(b$sN)==sum(b$J),
          nrow(b$IT)==sum(b$J),
          nrow(fullkey)==sum(b$J),
          all(c("sample","position","grain","jags_global_row") %in% names(fullkey)))
make_key<-function(z)paste(z$sample,z$position,z$grain,sep=":")
pids<-make_key(pubkey)
fids<-make_key(fullkey)
stopifnot(!anyDuplicated(pids),!anyDuplicated(fids),
          setequal(fullkey$jags_global_row,seq_len(sum(b$J))),
          all(pids %in% fids),
          length(setdiff(fids,pids))>0L)
# Validate row indexing and ancestry for every physical grain from the public
# archive. Newly received full author's matrices may be arranged differently.
stopifnot(all(fullkey$jags_global_row[fullkey$sample=="FER1"] %in% seq_len(b$J[1])),
          all(fullkey$jags_global_row[fullkey$sample=="FER3"] %in%
              seq.int(b$J[1]+1L,sum(b$J))))
rows<-fullkey$jags_global_row[match(pids,fids)]
for(field in c("N","sN","IT")){
 x<-a[[field]]
 y<-b[[field]][rows,,drop=FALSE]
 stopifnot(identical(dim(x),dim(y)))
 eq<-(is.na(x)&is.na(y))|(!is.na(x)&!is.na(y)&abs(x-y)<1e-9)
 if(!all(eq))stop("MATCHED_PHYSICAL_GRAIN_CHANGED_NUMERICAL_INPUT: ",field)
}
cat("P1J_FULL_COHORT_ELIGIBLE_UNDER_FROZEN_MATHEMATICAL_MODEL",
    "full_J",paste(b$J,collapse=","),"actual_new_keys",
    length(setdiff(fids,pids)),"\n")
# This estimate contrasts two *observed selection sets*, not the counterfactual
# age of missing or rejected *individual* grains. No causal attribution to
# selection mechanism without original eligibility history and selection model.
dir.create("p1j_full_out",showWarnings=FALSE)
write.csv(fullkey[!(fids %in% pids),,drop=FALSE],
          "p1j_full_out/new_observed_selected_grain_ids.csv",row.names=FALSE)
results<-list()
for(r in seq_len(2L)){
 for(cohort in c("public49","original_full")){
  d<-if(cohort=="public49")a else b
  seeds<-as.integer(c(4112011,4112012,4112013)+10000L*(r-1L))
  inits<-lapply(seeds,function(s)
    list(".RNG.name"="base::Mersenne-Twister",".RNG.seed"=s))
  con<-textConnection(public$jags_model)
  m<-rjags::jags.model(con,data=d,inits=inits,n.chains=3L,
                       n.adapt=0L,quiet=TRUE)
  close(con)
  adapted<-rjags::adapt(m,5000L,end.adaptation=TRUE,progress.bar="none")
  update(m,5000L,progress.bar="none")
  p<-rjags::coda.samples(m,c("A","D","sD"),
                     n.iter=5000L,thin=5L,progress.bar="none")
  saveRDS(p,sprintf("p1j_full_out/repeat%d_%s_posterior.rds",r,cohort))
  ess<-coda::effectiveSize(p)
  g<-coda::gelman.diag(p,multivariate=FALSE,autoburnin=FALSE)$psrf
  values<-as.matrix(p)
  for(i in 1:2){
   name<-sprintf("A[%d]",i)
   x<-values[,name]
   h<-coda::HPDinterval(coda::mcmc(x),prob=.95)
   results[[length(results)+1L]]<-data.frame(repeat=r,cohort=cohort,
     sample=c("FER1","FER3")[i],n_grains=d$J[i],
     mean_ka=mean(x),hpd_low_ka=h[1,1],hpd_high_ka=h[1,2],
     ess=unname(ess[name]),psrf_upper=unname(g[name,"Upper C.I."]),
     mcse_ka=sd(x)/sqrt(ess[name]),adapted=isTRUE(adapted))
  }
 }
}
out<-do.call(rbind,results)
out$diagnostic<-ifelse(out$adapted & out$ess>=400 &
 is.finite(out$psrf_upper)&out$psrf_upper<1.05,"PASS","HOLD")
write.csv(out,"p1j_full_out/independent_cohort_posteriors.csv",row.names=FALSE)
deltas<-list()
for(r in 1:2)for(sample in c("FER1","FER3")){
  p<-subset(out,repeat==r&cohort=="public49"&out$sample==sample)
  f<-subset(out,repeat==r&cohort=="original_full"&out$sample==sample)
  deltas[[length(deltas)+1L]]<-data.frame(repeat=r,sample=sample,
    full_minus_public_mean_ka=f$mean_ka-p$mean_ka,
    independent_mcse_ka=sqrt(p$mcse_ka^2+f$mcse_ka^2),
    diagnostic=if(p$diagnostic=="PASS"&f$diagnostic=="PASS")
                  "PASS" else "HOLD")
}
write.csv(do.call(rbind,deltas),"p1j_full_out/full_minus_public.csv",row.names=FALSE)
cat("P1J_MATCHED_FULL_VS_PUBLIC_EXECUTED_REAL_NEW_GRAINS_ONLY\n")
cat("P1J_MISSING_GRAIN_INCLUSION_EFFECT_DESCRIPTIVE_NOT_CAUSAL\n")
