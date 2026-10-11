# MQR-4.112 P1-J: actual 2021 DiscPos physical grain -> old-source LT row
# -> mathematical JAGS row -> modern BayLum row. Fail on non-bijective joins.
# This witnesses ONLY the authentic 49+49 public tutorial grains.
options(warn=1)
stopifnot(requireNamespace("Luminescence"),requireNamespace("BayLum"))
root<-"PracticalGuideToBayLum_Data/data"
src<-"upstream_BayLum_Generate_DataFile_2021.R"
stopifnot(file.exists(src),
 trimws(system2("git",c("hash-object",src),stdout=TRUE))==
 "5c9aeefda52b7be8a5ae28aaf0e3fef055e5bdf8")
lines<-paste(readLines(src,warn=FALSE),collapse="\n")
# Read the implementation: selecting j in DiscPos order, the j-th lt/slt
# response derives from that j-th grain's indexed original raw records.
for(anchor in c(
 'XLS_file[[3]]<-XLS_file[[2]]',
 'names(XLS_file) <- c("BIN_FILE","DISC","GRAIN")',
 'object@METADATA[,"POSITION"]== XLS_file[j,2]',
 'object@METADATA[,"GRAIN"]== XLS_file[j,3]',
 'lt=matrix(data=NA,nrow=J[bf],ncol=K[bf]+1)',
 'lt[j,1]=(Lx-Bx)/(Tx-BTx)',
 'LT[[i]]=lt'
))stopifnot(grepl(anchor,lines,fixed=TRUE))
old<-readRDS("p1_out/historical_2021_snapshot_processed.rds")
modern<-readRDS("p1_out/current_2025_created_data.rds")
math<-readRDS("p1f_out/frozen_mathematical_contract.rds")
stopifnot(identical(as.integer(old$J),c(49L,49L)),
 identical(as.integer(modern$J),c(49L,49L)),
 identical(as.integer(math$jags_data$J),c(49L,49L)))
stopifnot(math$growth=="AgesMultiCS2_EXPZO",
          math$distribution=="lognormal_A")
dir.create("p1j_out",showWarnings=FALSE)
fmt<-function(x){
 ifelse(is.na(x),"NA",formatC(signif(x,12),format="fg",digits=12))
}
signature<-function(a,b)apply(cbind(a,b),1,function(z)
 paste(fmt(z),collapse="|"))
frames<-list()
for (i in 1:2) {
 sample<-c("FER1","FER3")[i]
 dp<-read.csv(file.path(root,sample,"DiscPos.csv"),
              strip.white=TRUE,stringsAsFactors=FALSE)
 stopifnot(identical(names(dp),c("position","grain")),nrow(dp)==49L,
           !anyNA(dp),all(dp$position>0),all(dp$grain>0),
           !anyDuplicated(paste(dp$position,dp$grain,sep=":")))
 orig<-Luminescence::read_BIN2R(file.path(root,sample,"bin.BIN"),
           verbose=FALSE,zero_data.rm=FALSE,duplicated.rm=FALSE)
 meta<-orig@METADATA
 rawkey<-unique(paste(meta$POSITION,meta$GRAIN,sep=":"))
 ids<-paste(dp$position,dp$grain,sep=":")
 stopifnot(length(rawkey)==49L,setequal(ids,rawkey))
 stopifnot(all(vapply(ids,function(s)sum(paste(meta$POSITION,
                   meta$GRAIN,sep=":")==s),integer(1))==
                   c(FER1=18L,FER3=16L)[[sample]]))
 a<-signature(old$LT[[i]],old$sLT[[i]])
 b<-signature(modern$LT[[i]],modern$sLT[[i]])
 # Important: duplicated response signatures would make the identity join
 # ambiguous and must not be resolved by R's first-match behaviour.
 if(anyDuplicated(a)>0||anyDuplicated(b)>0)stop(sample,": ambiguous response signature")
 j<-match(a,b)
 stopifnot(length(j)==49L,!anyNA(j),!anyDuplicated(j),
           identical(sort(a),sort(b)))
 stopifnot(identical(dim(old$LT[[i]]),dim(modern$LT[[i]])),
           identical(dim(old$sLT[[i]]),dim(modern$sLT[[i]])))
 # Require the actual historical JAGS data matrix to be positionally
 # identical to the old CSV-selected luminescence rows.
 rng<-if(i==1)1:49 else 50:98
 nc<-ncol(old$LT[[i]])
 cmp<-function(x,y){
  eq<-(is.na(x)&is.na(y))|
    (!is.na(x)&!is.na(y)&abs(x-y)<=1e-11)
  all(eq)
 }
 stopifnot(cmp(math$jags_data$N[rng,seq_len(nc),drop=FALSE],old$LT[[i]]),
           cmp(math$jags_data$sN[rng,seq_len(nc),drop=FALSE],old$sLT[[i]]))
 # Prove the *other* response covariates follow source-selected row identity
 # in both old-source and modern source when reordered by signature.
 stopifnot(cmp(old$ITimes[[i]],modern$ITimes[[i]][j,,drop=FALSE]))
 frames[[i]]<-data.frame(
   sample=sample,position=dp$position,grain=dp$grain,
   csv_row=seq_len(49L),jags_global_row=rng,
   modern_matched_row=j,
   signal_sig=a,stringsAsFactors=FALSE)
 cat("P1J_PHYSICAL_JAGS_ROW_BIND_PASS",sample,
     "source_rows",length(a),"jags_global",min(rng),max(rng),
     "modern_row_displacement",sum(j!=seq_len(49L)),"\n")
}
out<-do.call(rbind,frames)
stopifnot(nrow(out)==98L,
          length(unique(paste(out$sample,out$position,out$grain)))==98L)
write.csv(out,"p1j_out/public_key_to_jags_bridge.csv",row.names=FALSE)
writeLines(c(
 "SOURCE_STATUS=PUBLIC_2021_EXAMPLE_49_GRAINS_PER_SAMPLE_ONLY",
 "HISTORICAL_BAYLUM_SOURCE_COMMIT=2c267b63c2b7017cae1e141d0969eb0765ad2500",
 "SOURCE_CODE_SNAPSHOT_NOT_PROVEN_AUTHOR_INSTALLED_REVISION",
 "BIN_RAW_PHYSICAL_KEY_VS_AUTHOR_DISCPOS=PASS",
 "AUTHOR_SELECTION_ORDER_TO_HISTORICAL_L_T_ROWS=PASS_SOURCE_CONTROL",
 "HISTORICAL_L_T_TO_FROZEN_JAGS_MATRIX=PASS",
 "HISTORICAL_L_T_TO_MODERN_ROWS=BIJECTION_SIGNED_12DIGITS",
 "FULL_ORIGINAL_2015_AND_2021_COHORT=HOLD",
 "MISSING_GRAIN_AGE_EFFECT=UNIDENTIFIED"),
 "p1j_out/binding_verdict.txt")
cat("P1J_AUTHENTIC_98_OBSERVED_GRAINS_PHYSICAL_TO_JAGS_BRIDGE_COMPLETED\n")
