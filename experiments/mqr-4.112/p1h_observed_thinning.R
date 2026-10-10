# P1-H empirical thinning test: ONLY observed 2021 public FER3 grains.
# No imputation; does not estimate the causal effect of unavailable full grains.
options(warn=1)
stopifnot(requireNamespace("rjags"),requireNamespace("coda"))
c<-readRDS("p1f_out/frozen_mathematical_contract.rds")
stopifnot(c$growth=="AgesMultiCS2_EXPZO",c$distribution=="lognormal_A",
          identical(as.integer(c$jags_data$J),c(49L,49L)))
dir.create("p1h_out",showWarnings=FALSE)
d<-c$jags_data
original_index<-seq_len(sum(d$J))
cat("OBSERVED_ONLY_DATA",length(original_index),"FER1",d$J[1],"FER3",d$J[2],"\n")
stopifnot(length(original_index)==98L)
set.seed(41120182L)
scenarios<-list(
 full49=seq_len(49L),
 first37=sort(sample.int(49L,37L)),
 second37=sort(sample.int(49L,37L)),
 first25=sort(sample.int(49L,25L)),
 second25=sort(sample.int(49L,25L))
)
results<-list()
for (case in names(scenarios)){
 pick<-scenarios[[case]]
 stopifnot(length(pick)==length(unique(pick)),all(pick %in% seq_len(49L)))
 keep<-c(1:49,49L+pick)
 sub<-d
 for(field in c("N","sN","IT"))sub[[field]]<-d[[field]][keep,,drop=FALSE]
 sub$J<-as.integer(c(49L,length(pick)))
 sub$index<-c(0L,cumsum(sub$J))
 stopifnot(nrow(sub$N)==sum(sub$J),nrow(sub$sN)==sum(sub$J),
           nrow(sub$IT)==sum(sub$J),all(sub$J>0L),
           identical(sub$K,d$K),identical(sub$Gamma,d$Gamma))
 seed<-as.integer(500000+match(case,names(scenarios))*100L+c(1,2,3))
 ini<-lapply(seed,function(x)
   list(".RNG.name"="base::Mersenne-Twister",".RNG.seed"=x))
 con<-textConnection(c$jags_model)
 model<-rjags::jags.model(con,data=sub,inits=ini,n.chains=3L,n.adapt=0L,quiet=TRUE)
 close(con)
 completed<-rjags::adapt(model,n.iter=4000L,end.adaptation=TRUE,progress.bar="none")
 update(model,4000L,progress.bar="none")
 chains<-rjags::coda.samples(model,c("A","D","sD"),n.iter=4000L,
                             thin=5L,progress.bar="none")
 stopifnot(length(chains)==3L,all(vapply(chains,nrow,integer(1))==800L))
 e<-coda::effectiveSize(chains)
 g<-coda::gelman.diag(chains,multivariate=FALSE,autoburnin=FALSE)$psrf
 z<-as.matrix(chains)
 for (i in 1:2){
  key<-paste0("A[",i,"]")
  y<-z[,key]
  h<-coda::HPDinterval(coda::mcmc(y),prob=.95)
  results[[length(results)+1L]]<-data.frame(
    case=case,sample=c("FER1","FER3")[i],
    kept_FER3_rows=length(pick),FER3_row_ids=paste(pick,collapse=";"),
    mean_ka=mean(y),hpd_low_ka=h[1,1],hpd_high_ka=h[1,2],
    draws=length(y),adaptation_complete=isTRUE(completed),
    ess=unname(e[key]),rhat_upper=unname(g[key,"Upper C.I."]),
    mcse_ka=sd(y)/sqrt(e[key]))
 }
 cat("P1H_ACTUAL_OBSERVED_ONLY_THINNING",case,"FER3_N",length(pick),
     "mean",mean(z[,"A[2]"]),"adaptation",completed,"\n")
}
tab<-do.call(rbind,results)
tab$diagnostic<-ifelse(tab$adaptation_complete &
 is.finite(tab$rhat_upper) & tab$rhat_upper<1.05 &
 is.finite(tab$ess) & tab$ess>=200,"PASS","HOLD")
write.csv(tab,"p1h_out/observed_only_thinning.csv",row.names=FALSE)
stopifnot(nrow(tab)==10L)
cat("P1H_THINNING_ACTUAL_JAGS_COMPLETED_5_SCENARIOS\n")
cat("P1H_FULL_UNOBSERVED_GRAIN_AGGREGATE_CAUSAL_EFFECT_UNIDENTIFIED\n")
