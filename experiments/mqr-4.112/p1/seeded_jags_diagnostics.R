# MQR P1-G. Reuse the P1-F byte-pinned mathematical input contract.
# Direct original-style rjags engine with explicit independent chain RNG.
options(warn=1)
stopifnot(requireNamespace("rjags"),requireNamespace("coda"))
contract<-readRDS("p1f_out/frozen_mathematical_contract.rds")
stopifnot(contract$growth=="AgesMultiCS2_EXPZO",
          contract$distribution=="lognormal_A",
          all(contract$jags_data$J==49L))
dir.create("p1g_out",showWarnings=FALSE)
saveRDS(contract,"p1g_out/locked_jags_contract.rds")
results<-list()
for(rep in seq_len(2L)){
 seeds<-as.integer(c(4112011,4112012,4112013)+10000*(rep-1L))
 inits<-lapply(seeds,function(s)
   list(".RNG.name"="base::Mersenne-Twister",".RNG.seed"=s))
 con<-textConnection(contract$jags_model)
 j<-rjags::jags.model(con,data=contract$jags_data,inits=inits,
                     n.chains=3L,n.adapt=0L,quiet=TRUE)
 close(con)
 adapted<-rjags::adapt(j,5000L,end.adaptation=TRUE,progress.bar="none")
 update(j,5000L,progress.bar="none")
 posterior<-rjags::coda.samples(j,c("A","D","sD"),
                    n.iter=5000L,thin=5L,progress.bar="none")
 stopifnot(length(posterior)==3L,
           all(vapply(posterior,nrow,integer(1))==1000L))
 saveRDS(posterior,sprintf("p1g_out/rep%d_posterior.rds",rep))
 ess<-coda::effectiveSize(posterior)
 gd<-tryCatch(coda::gelman.diag(posterior,multivariate=FALSE,
                               autoburnin=FALSE)$psrf,
               error=function(e)NULL)
 m<-as.matrix(posterior)
 for(i in 1:2){
  var<-paste0("A[",i,"]")
  stopifnot(var %in% colnames(m))
  y<-m[,var]
  rh<-if(is.null(gd)) NA_real_ else gd[var,"Point est."]
  upper<-if(is.null(gd)) NA_real_ else gd[var,"Upper C.I."]
  hpd<-coda::HPDinterval(coda::mcmc(y),prob=.95)
  results[[length(results)+1L]]<-data.frame(rep=rep,
     sample=c("FER1","FER3")[i],chain_seed_1=seeds[1],
     chain_seed_2=seeds[2],chain_seed_3=seeds[3],
     adaptation_complete=isTRUE(adapted),draws=length(y),
     mean_ka=mean(y),mcse_ka=sd(y)/sqrt(ess[var]),
     ess=ess[var],rhat=rh,rhat_upper=upper,
     hpd_low_ka=hpd[1,1],hpd_high_ka=hpd[1,2])
 }
}
tab<-do.call(rbind,results)
stopifnot(nrow(tab)==4L,all(tab$draws==3000L))
tab$diagnostic<-ifelse(tab$adaptation_complete &
 is.finite(tab$rhat_upper)&tab$rhat_upper<1.05 &
 is.finite(tab$ess)&tab$ess>=400,"PASS","HOLD")
write.csv(tab,"p1g_out/independent_chain_diagnostics.csv",row.names=FALSE)
print(tab)
cat("P1G_ACTUAL_6_CHAINS_2_REPLICATES_COMPLETED\n")
cat("P1G_PUBLIC_EXAMPLE_ONLY_FULL_PUBLICATION_COHORT_HOLD\n")
