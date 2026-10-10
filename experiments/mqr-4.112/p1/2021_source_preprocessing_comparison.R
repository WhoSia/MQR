# MQR-4.112 P1-B: real 2021 Git-snapshot BayLum vs 2025/26 BayLum 0.3.3
# 2021 upstream repo commit 2c267b63c2b7017cae1e141d0969eb0765ad2500
# file blob git hash 5c9aeefda52b7be8a5ae28aaf0e3fef055e5bdf8
# Experimental admission: only TWO mandatory API-adaptation shims; no formula edits.
options(warn=1)
dir.create("p1_out",showWarnings=FALSE)
root <- normalizePath("PracticalGuideToBayLum_Data/data",mustWork=TRUE)
samples <- c("FER1","FER3")
stopifnot(requireNamespace("BayLum"),requireNamespace("Luminescence"))
stopifnot(as.character(packageVersion("BayLum"))=="0.3.3")
cat("BAYLUM_CURRENT",as.character(packageVersion("BayLum")),
    "LUMINESCENCE_CURRENT",as.character(packageVersion("Luminescence")),"\n")
old_src <- "upstream_BayLum_Generate_DataFile_2021.R"
stopifnot(file.exists(old_src))
file_sha <- trimws(system2("git",c("hash-object",old_src),stdout=TRUE))
stopifnot(identical(file_sha,"5c9aeefda52b7be8a5ae28aaf0e3fef055e5bdf8"))
txt <- paste(readLines(old_src,warn=FALSE),collapse="\n")
oldpath <- "file = paste0(Path, FolderNames[bf])"
oldlist <- ")[[1]]"
hits <- function(x,pattern)lengths(regmatches(x,gregexpr(pattern,x,fixed=TRUE)))[[1]]
if(hits(txt,oldpath)!=1L||hits(txt,oldlist)!=1L){
  stop("2021 source author fixed-API assumptions not met; no silent changes")
}
adapted <- sub(oldpath,'file = file.path(Path, FolderNames[bf], "bin.BIN")',
                txt,fixed=TRUE)
adapted <- sub(oldlist,")",adapted,fixed=TRUE)
writeLines(c(
 "Historical upstream source commit: 2c267b63c2b7017cae1e141d0969eb0765ad2500",
 "Historical upstream blob: 5c9aeefda52b7be8a5ae28aaf0e3fef055e5bdf8",
 "BRIDGE 1: directory path -> actual original bin.BIN file path (same original bytes)",
 "BRIDGE 2: remove obsolete [[1]] wrapper around R-Lum single-file S4 import",
 "No scientific model or Lx/Tx/dose formula altered.",
 "2021-11-11 snapshot contemporaneous but not proven identical to article author's run."),
 "p1_out/historical_api_bridge.txt")
env <- new.env(parent=globalenv())
eval(parse(text=adapted),envir=env)
oldfn <- get("Generate_DataFile",envir=env)
error_text<-NULL;stack_text<-NULL
old <- tryCatch(
  withCallingHandlers(oldfn(Path=paste0(root,"/"),FolderNames=samples,
      Nb_sample=2,verbose=FALSE),
    error=function(e){
      stack_text <<- paste(vapply(sys.calls(),
        function(call)paste(deparse(call),collapse=" "),character(1)),collapse="\n")
    }),
  error=function(e){error_text<<-conditionMessage(e);NULL})
if(is.null(old)){
  cat("HISTORICAL_API_ONLY_DECODE_HOLD",error_text,"\n")
  writeLines(c(error_text,stack_text),"p1_out/historical_error_stack.txt")
  writeLines("HISTORICAL_INPUT_PARITY=HOLD, 2021 exact source could not execute in modern R",
             "p1_out/historical_verdict.txt")
  quit(save="no",status=0)
}
saveRDS(old,"p1_out/historical_2021_snapshot_processed.rds")
# Recreate source-defined P0 official new data normalization (same default filters).
config <- lapply(samples,function(s){
  src<-file.path(root,s)
  lines<-readLines(file.path(src,"rule.csv"),warn=FALSE)
  lines<-lines[grepl("=",lines,fixed=TRUE)]
  keys<-trimws(sub("=.*$","",lines))
  nums<-as.numeric(trimws(sub("^[^=]*=","",lines)))
  stopifnot(length(keys)==10L,all(is.finite(nums)))
  list(sample=s,files=file.path(src,"bin.BIN"),
       settings=list(
         dose_source=as.numeric(read.csv(file.path(src,"DoseSource.csv"))[1,]),
         dose_env=as.numeric(read.csv(file.path(src,"DoseEnv.csv"))[1,]),
         rules=as.list(stats::setNames(nums,keys))))
})
modern<-BayLum::create_DataFile(config_file=config,verbose=FALSE)
saveRDS(modern,"p1_out/current_2025_created_data.rds")
fields<-c("LT","sLT","ITimes","regDose","dLab","ddot_env","J","K","Nb_measurement")
rows<-list();examples<-list()
shape<-function(x)paste(if(is.null(dim(x)))length(x) else dim(x),collapse="x")
for(field in fields){
  a<-old[[field]];b<-modern[[field]]
  if(is.null(a)||is.null(b))stop("Missing preprocessing field: ",field)
  idx<-if(is.list(a))seq_along(a) else 0L
  for(k in idx){
    x<-if(k==0L)a else a[[k]]
    y<-if(k==0L)b else b[[k]]
    aa<-as.numeric(x);bb<-as.numeric(y)
    n<-min(length(aa),length(bb))
    delta<-if(n>0)abs(aa[seq_len(n)]-bb[seq_len(n)]) else numeric()
    mask<-if(n>0)is.na(delta)|(delta>1e-10) else logical()
    mask[is.na(aa[seq_len(n)])&is.na(bb[seq_len(n)])]<-FALSE
    bad<-sum(mask)+abs(length(aa)-length(bb))
    rec<-data.frame(field=field,cohort=if(k==0L)"JOINT" else samples[k],
      historical_shape=shape(x),modern_shape=shape(y),
      compared=n,mismatches=bad,
      max_absolute_delta=if(any(is.finite(delta)))max(delta[is.finite(delta)]) else NA_real_,
      historic_median=if(any(is.finite(aa)))median(aa[is.finite(aa)]) else NA_real_,
      modern_median=if(any(is.finite(bb)))median(bb[is.finite(bb)]) else NA_real_,
      nonfinite_historical=sum(!is.finite(aa)),nonfinite_modern=sum(!is.finite(bb)))
    rows[[length(rows)+1L]]<-rec
    if(any(mask)){
      take<-head(which(mask),12L)
      examples[[length(examples)+1L]]<-data.frame(field=field,
        cohort=rec$cohort,index=take,old=aa[take],new=bb[take],
        abs_delta=delta[take])
    }
    cat("HISTORICAL_2021_VS_MODERN",field,rec$cohort,
        "shapes",rec$historical_shape,rec$modern_shape,
        "mismatches",bad,"max_delta",rec$max_absolute_delta,
        "medians",rec$historic_median,rec$modern_median,"\n")
  }
}
tab<-do.call(rbind,rows)
write.csv(tab,"p1_out/2021_vs_2025_field_deltas.csv",row.names=FALSE)
if(length(examples))write.csv(do.call(rbind,examples),
    "p1_out/2021_vs_2025_first_disagreement_cells.csv",row.names=FALSE)
all_eq<-all(tab$mismatches==0L)&all(tab$historical_shape==tab$modern_shape)
cat("P1 HISTORICAL SOURCE INPUT PARITY:",if(all_eq)"PASS" else "FAIL_BOUNDED","\n")
writeLines(if(all_eq)"HISTORICAL_INPUT_PARITY=PASS"
    else "HISTORICAL_INPUT_PARITY=FAIL_BOUNDED",
    "p1_out/historical_verdict.txt")
# This code only adjudicates preprocessing; posterior attribution requires
# a source-aligned JAGS run with EXACT old data and same model, not an assumption.


# P1-C: distinguish genuine channel/ratio differences from cohort row permutations.
# The 2021 algorithm deliberately uses the author DiscPos.csv row order.
# The new converter may use the raw BIN physical acquisition order instead.
order_rows <- list()
for (i in seq_along(samples)) {
  s <- samples[i]
  old_lt <- old$LT[[i]]
  new_lt <- modern$LT[[i]]
  old_se <- old$sLT[[i]]
  new_se <- modern$sLT[[i]]
  stopifnot(identical(dim(old_lt),dim(new_lt)),identical(dim(old_se),dim(new_se)))
  col_set_match <- logical(ncol(old_lt))
  for (j in seq_len(ncol(old_lt))) {
    x <- sort(signif(old_lt[,j],digits=12L))
    y <- sort(signif(new_lt[,j],digits=12L))
    col_set_match[j] <- isTRUE(all.equal(x,y,tolerance=1e-10,check.attributes=FALSE))
    cat("P1_COLUMN_VALUE_MULTISET",s,"COL",j,"MATCH",col_set_match[j],"\n")
  }
  old_sig <- apply(cbind(old_lt,old_se),1,function(v)
          paste(formatC(signif(v,12L),digits=12,format="fg"),collapse="|"))
  new_sig <- apply(cbind(new_lt,new_se),1,function(v)
          paste(formatC(signif(v,12L),digits=12,format="fg"),collapse="|"))
  map <- match(old_sig,new_sig)
  row_match <- sum(!is.na(map))
  perfect_multiset <- identical(sort(old_sig),sort(new_sig))
  cat("P1_PERMUTATION_TEST",s,"whole_row_matched",row_match,"of",length(old_sig),
      "perfect_row_multiset",perfect_multiset,
      "all_column_value_multisets",all(col_set_match),"\n")
  dp <- read.csv(file.path(root,s,"DiscPos.csv"),stringsAsFactors=FALSE)
  stopifnot(nrow(dp)==nrow(old_lt))
  orig <- Luminescence::read_BIN2R(file.path(root,s,"bin.BIN"),
       verbose=FALSE,zero_data.rm=FALSE,duplicated.rm=FALSE)
  meta <- orig@METADATA
  observed <- unique(meta[,c("POSITION","GRAIN")])
  source_keys <- paste(dp[[1]],dp[[2]],sep=":")
  raw_keys <- paste(observed$POSITION,observed$GRAIN,sep=":")
  rawmap <- match(source_keys,raw_keys)
  cat("P1_SOURCE_ID_MAP",s,"49 raw keys linked",sum(!is.na(rawmap)),
      "source order equals raw order",identical(seq_along(rawmap),as.integer(rawmap)),
      "first 8 map positions",paste(head(rawmap,8),collapse=","),"\n")
  # Identify whether the modern rows are exactly the raw acquisition-key order.
  if(all(!is.na(rawmap))){
    keyed_match <- all(abs(old_lt-modern$LT[[i]][rawmap,,drop=FALSE])<1e-10) &&
                   all(abs(old_se-modern$sLT[[i]][rawmap,,drop=FALSE])<1e-10)
    cat("P1_SOURCE_KEY_ALIGNED_LT_AND_SLT_EQUAL",s,keyed_match,"\n")
  }
  rec <- data.frame(sample=s,grain_source_order=seq_along(map),
      source_disc=dp[[1]],source_grain=dp[[2]],
      modern_row_from_signal_signature=map,modern_raw_key_index=rawmap,
      stringsAsFactors=FALSE)
  order_rows[[i]]<-rec
}
write.csv(do.call(rbind,order_rows),"p1_out/grain_order_and_signature_crosswalk.csv",
          row.names=FALSE)
cat("P1 row-permutation adjudication completed; model causal attribution still needs old input MCMC.\n")
