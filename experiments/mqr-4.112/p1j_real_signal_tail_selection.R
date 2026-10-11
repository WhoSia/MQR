# MQR-4.112 P1-J: actual observed FER3 L/T-tail selection rival.
# Target: falsify robustness to informative *within-observed* selection.
# NOT a simulation of 47 unobserved FER3 grains or actual 2015 quality screen.
options(warn=1)
stopifnot(requireNamespace("rjags"),requireNamespace("coda"))
c<-readRDS("p1f_out/frozen_mathematical_contract.rds")
x<-c$jags_data
binding<-read.csv("p1j_out/public_key_to_jags_bridge.csv",stringsAsFactors=FALSE)
stopifnot(identical(as.integer(x$J),c(49L,49L)),
          identical(as.character(binding$sample),
                    c(rep("FER1",49L),rep("FER3",49L))),
          identical(as.integer(binding$jags_global_row),seq_len(98L)),
          c$growth=="AgesMultiCS2_EXPZO",
          c$distribution=="lognormal_A")
dir.create("p1j_signal_out",showWarnings=FALSE)
f<-binding[binding$sample=="FER3",,drop=FALSE]
stopifnot(nrow(f)==49L,all(is.finite(x$N[50:98,1])))
f$natural_l_t<-x$N[50:98,1]
f$fer3_source_row<-seq_len(49L)
# Primary selection algorithm is frozen prior to any posterior.
ranked<-order(f$natural_l_t,f$position,f$grain,method="radix")
scenarios<-list(
 all_49=seq_len(49L),
 low_N25=ranked[seq_len(25L)],
 high_N25=tail(ranked,25L),
 low_N37=ranked[seq_len(37L)],
 high_N37=tail(ranked,37L))
stopifnot(all(vapply(scenarios,function(z)!anyDuplicated(z)&&
             all(z %in% 1:49),logical(1))))
write.csv(f[ranked,,drop=FALSE],
          "p1j_signal_out/observed_fer3_ranked_source_grains.csv",
          row.names=FALSE)
results<-list()
for(rep in 1:2)for(case in names(scenarios)){
  keep<-sort(scenarios[[case]])
  d<-x
  rows<-c(1:49,49L+keep)
  for(field in c("N","sN","IT"))
    d[[field]]<-x[[field]][rows,,drop=FALSE]
  d$J<-as.integer(c(49L,length(keep)))
  d$index<-as.integer(c(0L,49L,49L+length(keep)))
  stopifnot(nrow(d$N)==sum(d$J),
            identical(d$Gamma,x$Gamma),
            identical(d$xbound,x$xbound),
            identical(d$StratiConstraints,x$StratiConstraints))
  seeds<-as.integer(c(4112011,4112012,4112013) + 10000*(rep-1L))
  ini<-lapply(seeds,function(k)
    list(".RNG.name"="base::Mersenne-Twister",".RNG.seed"=k))
  con<-textConnection(c$jags_model)
  m<-rjags::jags.model(con,data=d,inits=ini,n.chains=3L,
                       n.adapt=0L,quiet=TRUE)
  close(con)
  adapted<-rjags::adapt(m,5000L,end.adaptation=TRUE,progress.bar="none")
  update(m,5000L,progress.bar="none")
  draws<-rjags::coda.samples(m,c("A","D","sD"),n.iter=5000L,
                             thin=5L,progress.bar="none")
  stopifnot(length(draws)==3L,
           all(vapply(draws,nrow,integer(1))==1000L))
  es<-coda::effectiveSize(draws)
  gr<-coda::gelman.diag(draws,multivariate=FALSE,
                        autoburnin=FALSE)$psrf
  z<-as.matrix(draws)
  for(i in 1:2){
    v<-sprintf("A[%d]",i)
    a<-z[,v]
    h<-coda::HPDinterval(coda::mcmc(a),prob=.95)
    results[[length(results)+1L]]<-data.frame(
      repetition=rep,case=case,sample=c("FER1","FER3")[i],
      fer3_grain_count=length(keep),
      age_mean_ka=mean(a),hpd95_low_ka=h[1,1],hpd95_high_ka=h[1,2],
      ess=unname(es[v]),rhat_upper=unname(gr[v,"Upper C.I."]),
      mcse_ka=sd(a)/sqrt(es[v]),adaptation_complete=isTRUE(adapted))
  }
  selected<-f[keep,c("position","grain","fer3_source_row","natural_l_t")]
  write.csv(selected,sprintf("p1j_signal_out/%s_fer3_physical_ids.csv",case),
            row.names=FALSE)
  cat("P1J_REAL_SOURCE_TAIL_SELECTION",case,"rep",rep,
      "retained",length(keep),"FER3_mean_ka",mean(z[,"A[2]"]),
      "FER1_mean_ka",mean(z[,"A[1]"]),"\n")
}
tab<-do.call(rbind,results)
tab$diagnostic<-ifelse(tab$adaptation_complete&
                        is.finite(tab$ess)&tab$ess>=400&
                        is.finite(tab$rhat_upper)&tab$rhat_upper<1.05,
                        "PASS","HOLD")
stopifnot(nrow(tab)==20L)
write.csv(tab,"p1j_signal_out/real_signal_tail_jags.csv",row.names=FALSE)
ds<-list()
for(r in 1:2) for(case in setdiff(names(scenarios),"all_49"))for(sample in c("FER1","FER3")){
  base<-tab[tab$repetition==r & tab$case=="all_49" & tab$sample==sample,,drop=FALSE]
  alt<-tab[tab$repetition==r & tab$case==case & tab$sample==sample,,drop=FALSE]
  stopifnot(nrow(base)==1L,nrow(alt)==1L)
  ds[[length(ds)+1L]]<-data.frame(
    repetition=r,case=case,sample=sample,
    difference_from_public49_ka=alt$age_mean_ka-base$age_mean_ka,
    independent_mcse_ka=sqrt(alt$mcse_ka^2+base$mcse_ka^2),
    diagnostic=if(alt$diagnostic=="PASS"&&base$diagnostic=="PASS")
               "PASS" else "HOLD")
}
write.csv(do.call(rbind,ds),"p1j_signal_out/selection_shift_from_full49.csv",
          row.names=FALSE)
writeLines(c("ORIGINAL_ALL_2015_OR_2021_GRAINS=UNAVAILABLE",
 "SELECTION_MECHANISM=ADVERSARIAL_OBSERVED_NATURAL_LT_TAIL",
 "NO_DIRECT_ESTIMATE_OF_UNOBSERVED_47_GRAINS",
 "CHANGING_OBSERVED_SELECTION_IS_NOT_PROVING_PUBLISHED_AGE_CAUSE",
 "ONE_JAGS_MATHEMATICAL_MODEL_AND_PUBLISHED_2021_PUBLIC_SIGNAL_ONLY"),
 "p1j_signal_out/interpretation_scope.txt")
cat("P1J_OBSERVED_SOURCE_INFORMATIVE_SELECTION_JAGS_COMPLETED\n")
