# MQR-4.112 P1: compare source 2021 BayLum preprocessing to BayLum 0.3.3.
# Author original FER BIN, DiscPos, DoseSource, DoseEnv, rule CSVs are downloaded
# by read-only workflow from the published original Guérin (2021) supplement.
# Original-source data never committed to this repository.
options(warn=1)
Sys.setenv(TZ="UTC")
stopifnot(as.character(utils::packageVersion("BayLum"))=="0.3.3")
suppressPackageStartupMessages(library(BayLum))
root <- normalizePath("PracticalGuideToBayLum_Data/data",mustWork=TRUE)
fer <- c("FER1","FER3")
dir.create("out",showWarnings=FALSE)
origbin <- function(f) file.path(root,f,"bin.BIN")
config <- lapply(fer,function(f){
  d<-file.path(root,f)
  rawRule<-readLines(file.path(d,"rule.csv"),warn=FALSE)
  rawRule<-rawRule[grepl("=",rawRule,fixed=TRUE)]
  ks<-trimws(sub("=.*$","",rawRule))
  vs<-as.numeric(trimws(sub("^[^=]*=","",rawRule)))
  stopifnot(length(vs)==10,all(is.finite(vs)))
  list(sample=f,files=origbin(f),
    settings=list(dose_source=as.numeric(utils::read.csv(file.path(d,"DoseSource.csv"))[1,]),
                  dose_env=as.numeric(utils::read.csv(file.path(d,"DoseEnv.csv"))[1,]),
                  rules=as.list(stats::setNames(vs,ks))))
})
modern <- BayLum::create_DataFile(config_file=config,verbose=FALSE)
cat("MODERN_CREATE_DATAFILE: J=",paste(modern$J,collapse=","),
    " K=",paste(modern$K,collapse=","),"\n",sep="")
# Keep the package's own 2021 legacy preprocessing algorithm (rather than
# rewriting dose/readout equations), changing ONLY the obsolete path returned
# to modern Luminescence::read_BIN2R() from folder to the original BIN file.
legacy <- BayLum::Generate_DataFile
legacyBody <- paste(deparse(body(legacy),width.cutoff=500L),collapse="\n")
old <- "file = paste0(Path, FolderNames[bf])"
stopifnot(length(gregexpr(old,legacyBody,fixed=TRUE)[[1]])==1,
          gregexpr(old,legacyBody,fixed=TRUE)[[1]][1]>0)
new <- 'file = paste0(Path, FolderNames[bf], "/bin.BIN")'
legacyBody<-sub(old,new,legacyBody,fixed=TRUE)
body(legacy)<-parse(text=legacyBody)[[1]]
environment(legacy)<-asNamespace("BayLum")
historical<-legacy(Path=paste0(root,"/"),FolderNames=fer,Nb_sample=2,
                   verbose=FALSE,duplicated.rm=FALSE,zero_data.rm=FALSE)
stopifnot(is.list(historical))
cat("LEGACY_GENERATED: J=",paste(historical$J,collapse=","),
    " K=",paste(historical$K,collapse=","),"\n",sep="")
saveRDS(modern,file.path("out","modern_BayLum033_input.rds"))
saveRDS(historical,file.path("out","legacy_semantics_current_runtime_input.rds"))
keyFields<-c("LT","sLT","ITimes","dLab","regDose","J","K","Nb_measurement","ddot_env")
overview <- data.frame(field=character(),sample=character(),dimModern=character(),
   dimLegacy=character(),nCommon=integer(),maxAbsDiff=numeric(),nNonfinite=integer(),
   identical=logical(),stringsAsFactors=FALSE)
for(key in keyFields)for(i in seq_along(fer)){
  a<-modern[[key]];b<-historical[[key]]
  if(is.list(a) && !is.data.frame(a))a<-a[[i]]
  if(is.list(b) && !is.data.frame(b))b<-b[[i]]
  if(key %in% c("dLab","ddot_env") && (is.matrix(a)||is.data.frame(a)))a<-a[,min(i,ncol(a)),drop=FALSE] else if(length(a)>1 && key %in% c("J","K","Nb_measurement"))a<-a[i]
  if(key %in% c("dLab","ddot_env") && (is.matrix(b)||is.data.frame(b)))b<-b[,min(i,ncol(b)),drop=FALSE] else if(length(b)>1 && key %in% c("J","K","Nb_measurement"))b<-b[i]
  v1<-as.vector(a);v2<-as.vector(b);n<-min(length(v1),length(v2))
  nums <- if(n>0) suppressWarnings(abs(as.numeric(v1[seq_len(n)])-as.numeric(v2[seq_len(n)]))) else numeric()
  diff <- if(length(nums)&&any(is.finite(nums)))max(nums[is.finite(nums)])else NA_real_
  nonfinite <- sum(!is.finite(nums))
  item<-data.frame(field=key,sample=fer[i],
    dimModern=paste(dim(a),collapse="x"),dimLegacy=paste(dim(b),collapse="x"),
    nCommon=n,maxAbsDiff=diff,nNonfinite=nonfinite,
    identical=isTRUE(all.equal(a,b,check.attributes=FALSE)),stringsAsFactors=FALSE)
  overview<-rbind(overview,item)
  cat(sprintf("%s %s modern=(%s) legacy=(%s) n=%s diff=%s identical=%s\n",
     key,fer[i],item$dimModern,item$dimLegacy,n,format(diff,digits=8),item$identical))
}
utils::write.csv(overview,file.path("out","legacy_modern_field_comparison.csv"),row.names=FALSE)
cat("Comparison completed with untouched original source CSV + BIN, no JAGS inference.\n")
