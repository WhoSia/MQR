# MQR-4.112 P1: original FER provenance-preserving preprocessing comparison
# Two algorithms shipped with the SAME BayLum 0.3.3:
#  (A) legacy Generate_DataFile() with one transparent directory->actual BIN path shim
#  (B) officially supported create_DataFile() preserving original author CSV
# This compares the implemented algorithms; the true 2021 package version remains unverified.
options(warn=1)
dir.create("p1_out",showWarnings=FALSE)
stopifnot(requireNamespace("BayLum"),requireNamespace("Luminescence"))
stopifnot(as.character(packageVersion("BayLum"))=="0.3.3")
root <- normalizePath("PracticalGuideToBayLum_Data/data",mustWork=TRUE)
samples <- c("FER1","FER3")
csvpath <- function(sample,fn) file.path(root,sample,fn)
input <- function(sample) csvpath(sample,"bin.BIN")
sha <- function(f) trimws(strsplit(system2("sha256sum",f,stdout=TRUE)," +")[[1]][1])
h <- c(FER1="8328723705b6cdf33d65ab9c946fb7a1461b51f0861b4bbc3bf531f2d4460786",
       FER3="510c0af01b4eaf6b8283aac857b093682e158f2a900da39db1dabdd3780e56d4")
for(s in samples) stopifnot(sha(input(s))==h[[s]])
cat("P1 pinned raw input hashes PASS",paste(samples,collapse=","),"\n")
# Reconstruct the exact P0 modern config, with original source rules; no arbitrary filtering.
config <- lapply(samples, function(s) {
  v <- readLines(csvpath(s,"rule.csv"),warn=FALSE)
  v <- v[grepl("=",v,fixed=TRUE)]
  k <- trimws(sub("=.*$","",v))
  x <- as.numeric(trimws(sub("^[^=]*=","",v)))
  stopifnot(length(k)==10,all(is.finite(x)))
  list(sample=s,files=input(s),settings=list(
    dose_source=as.numeric(read.csv(csvpath(s,"DoseSource.csv"))[1,]),
    dose_env=as.numeric(read.csv(csvpath(s,"DoseEnv.csv"))[1,]),
    rules=as.list(stats::setNames(x,k))))
})
modern <- BayLum::create_DataFile(config_file=config,verbose=FALSE)
saveRDS(modern,"p1_out/modern_create_DataFile.rds")
cat("P1 modern J",paste(modern$J,collapse=","),"K",paste(modern$K,collapse=","),"\n")
# In current Luminescence, supplying a FOLDER path to read_BIN2R can select additional
# objects than the single author 2021 'bin.BIN', causing old code to fail.
# Make ONLY this one source-call edit, with exact old expression verification.
legacy <- BayLum::Generate_DataFile
txt <- paste(deparse(body(legacy),width.cutoff=500L),collapse="\n")
needle <- "file = paste0(Path, FolderNames[bf])"
nmatch <- lengths(regmatches(txt,gregexpr(needle,txt,fixed=TRUE)))[1]
if(nmatch!=1) stop(sprintf("legacy patch assumption incorrect, expected 1 site found %s",nmatch))
patched <- sub(needle,'file = file.path(Path, FolderNames[bf], "bin.BIN")',txt,fixed=TRUE)
stopifnot(!identical(txt,patched))
body(legacy) <- parse(text=patched)[[1]]
cat("P1 legacy current-package source patched ONE filename resolution expression; SHA(original function body)",
    sha({ f<-tempfile(); writeLines(txt,f);f }),"\n")
error_text <- NULL
old <- tryCatch(suppressWarnings(legacy(Path=paste0(root,"/"),
    FolderNames=samples,Nb_sample=2,verbose=FALSE)),
    error=function(e){error_text<<-conditionMessage(e);NULL})
if(is.null(old)){
  cat("LEGACY_ALGORITHM_RUNTIME_BLOCKED:",error_text,"\n")
  writeLines(error_text,"p1_out/legacy_runtime_error.txt")
  writeLines("LEGACY_COMPARE=HOLD, modern model imported; no elementwise equality asserted",
             "p1_out/verdict.txt")
  quit(save="no",status=0)
}
saveRDS(old,"p1_out/legacy_Generate_DataFile_with_filename_shim.rds")
fields <- c("LT","sLT","ITimes","regDose","dLab","ddot_env","J","K","Nb_measurement")
cat("P1 legacy J",paste(old$J,collapse=","),"K",paste(old$K,collapse=","),"\n")
summary <- data.frame(field=character(),sample=character(),shape_old=character(),
    shape_modern=character(),n_compared=integer(),n_mismatches=integer(),
    max_abs=double(),median_abs=double(),n_nonfinite_old=integer(),n_nonfinite_modern=integer(),
    stringsAsFactors=FALSE)
details <- list()
for(f in fields){
  a <- old[[f]]; b <- modern[[f]]
  if(is.null(a)||is.null(b))stop("Missing source field: ",f)
  if(is.list(a)&&!is.data.frame(a)){
    if(length(a)!=length(b))stop("List cohort count mismatch at ",f)
    chunks <- seq_along(a)
  }else chunks <- 0
  for(i in chunks){
    x<-if(i==0)a else a[[i]]
    y<-if(i==0)b else b[[i]]
    shape<-function(v)paste(if(is.null(dim(v)))length(v) else dim(v),collapse="x")
    sx<-shape(x);sy<-shape(y)
    vx<-as.numeric(x);vy<-as.numeric(y)
    same_shape<-identical(dim(x),dim(y)) && length(vx)==length(vy)
    usable<-if(same_shape) length(vx) else min(length(vx),length(vy))
    diff<-if(usable) abs(vx[seq_len(usable)]-vy[seq_len(usable)]) else numeric()
    nanpair<-if(usable) is.na(vx[seq_len(usable)])&is.na(vy[seq_len(usable)]) else logical()
    mismatch<-if(usable) is.na(diff)|(!is.finite(diff))|(diff>1e-10) else logical()
    mismatch[nanpair]<-FALSE
    nbad <- sum(mismatch)+(if(!same_shape)abs(length(vx)-length(vy)) else 0)
    row <- data.frame(field=f,sample=if(i==0)"JOINT" else samples[i],shape_old=sx,
      shape_modern=sy,n_compared=usable,n_mismatches=nbad,
      max_abs=if(length(diff)&&any(is.finite(diff)))max(diff[is.finite(diff)]) else NA_real_,
      median_abs=if(length(diff)&&any(is.finite(diff)))median(diff[is.finite(diff)]) else NA_real_,
      n_nonfinite_old=sum(!is.finite(vx)),n_nonfinite_modern=sum(!is.finite(vy)))
    summary <- rbind(summary,row)
    if(nbad>0&&usable>0){
      take<-which(mismatch)[seq_len(min(12,sum(mismatch)))]
      details[[paste(f,i,sep="_")]]<-data.frame(field=f,sample=row$sample,index=take,
          old=vx[take],modern=vy[take],abs_delta=diff[take])
    }
    cat("P1_FIELD",f,row$sample,"shape",sx,sy,"n_diff",nbad,
        "max_abs",format(row$max_abs,digits=10),"\n")
  }
}
write.csv(summary,"p1_out/field_level_comparison.csv",row.names=FALSE)
if(length(details))write.csv(do.call(rbind,details),"p1_out/first_mismatch_cells.csv",row.names=FALSE)
all_equal<-all(summary$n_mismatches==0)&&all(summary$shape_old==summary$shape_modern)
cat("P1 ELEMENTWISE ALGORITHM PARITY:",if(all_equal)"PASS" else "FAIL_BOUNDED","\n")
cat("P1 raw data and both actual algorithms compared; result does not prove 2021 package revision parity.\n")
writeLines(sprintf("LEGACY_CURRENT_PACKAGE_VS_MODERN_ALGORITHM=%s",if(all_equal)"PASS" else "FAIL_BOUNDED"),
           "p1_out/verdict.txt")
