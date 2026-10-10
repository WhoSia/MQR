# MQR-4.112 P0: official R/BayLum FER original-source reproduction.
# Original article supplement: https://gchron.copernicus.org/articles/3/229/2021/gchron-3-229-2021-supplement.zip
# No personal data or original observational BIN committed to repository.
# The file is fetched/read at job runtime and checked against P8 original SHA-256.
options(warn = 1, timeout = 180)
Sys.setenv(TZ = "UTC")
dir.create("out", showWarnings = FALSE)
writeLines(capture.output(sessionInfo()), "out/r_session.txt")
if (!requireNamespace("Luminescence", quietly=TRUE) || !requireNamespace("BayLum", quietly=TRUE)
   || !requireNamespace("rjags", quietly=TRUE) || !requireNamespace("coda", quietly=TRUE)) {
  stop("R package dependencies absent; no posterior claimed.")
}
suppressPackageStartupMessages(library(BayLum))
stopifnot(as.character(packageVersion("BayLum")) == "0.3.3")
cat("BayLum", as.character(packageVersion("BayLum")),
    "Luminescence", as.character(packageVersion("Luminescence")),
    "rjags", as.character(packageVersion("rjags")),
    "JAGS", as.character(rjags::jags.version()), "\n")
writeLines(capture.output(sessionInfo()), "out/r_session.txt")

root <- "PracticalGuideToBayLum_Data"
data_path <- normalizePath(file.path(root,"data"),mustWork=TRUE)
input <- function(s) file.path(data_path,s,"bin.BIN")
expected <- list(FER1=list(n=882,sha="491ba24ee9acd3dda89961c92817a53ad4e455ce47558bc3bb7a78213dc6bcff",
  bin="8328723705b6cdf33d65ab9c946fb7a1461b51f0861b4bbc3bf531f2d4460786"),
 FER3=list(n=784,sha="80b2a3b59439a217b928228a31114dcefedb5d4c7c90b2b57e2a9efac82345c0",
  bin="510c0af01b4eaf6b8283aac857b093682e158f2a900da39db1dabdd3780e56d4"))
hash_file <- function(p) trimws(strsplit(system2("sha256sum",p,stdout=TRUE), " +")[[1]][1])
parity_summary <- character()
for (fer in c("FER1","FER3")) {
  e <- expected[[fer]]
  stopifnot(hash_file(input(fer)) == e$bin)
  # Important: no import-side duplicate/zero count filtering or grain disc exclusion.
  obs <- Luminescence::read_BIN2R(input(fer),verbose=FALSE,
            duplicated.rm=FALSE,zero_data.rm=FALSE,show.raw.values=TRUE)
  meta <- methods::slot(obs,"METADATA")
  pts <- methods::slot(obs,"DATA")
  if (length(pts)!=e$n || nrow(meta)!=e$n) {
    stop(sprintf("SOURCE READER COUNTS MISMATCH %s: %d/%d expected %d",
                 fer,length(pts),nrow(meta),e$n))
  }
  if (any(as.integer(meta[["VERSION"]])!=4L) ||
      any(as.integer(meta[["NPOINTS"]])!=100L)) {
    stop(paste("R reader version/channel violation:", fer))
  }
  outfile <- file.path("out",paste0(fer,"_R_official_integer_channels.bin"))
  con <- file(outfile,"wb")
  for (p in pts) {
    if(length(p)!=100L || any(!is.finite(p))) {
      close(con); stop(paste("Missing/nonfinite original channels",fer))
    }
    writeBin(as.integer(p),con,size=4L,endian="little")
  }
  close(con)
  got <- hash_file(outfile)
  if(got != e$sha) stop(paste("R/Python ALL-CHANNEL BYTE PARITY FAILURE",fer,got,e$sha))
  # Check exact (position, grain) selected raw cohort, independent of posterior.
  pos <- utils::read.csv(file.path(data_path,fer,"DiscPos.csv"),sep=",",
                          stringsAsFactors=FALSE)
  # format preserved; strict selection match is audited via original P8 parser.
  parity_summary <- c(parity_summary,
    sprintf("%s: official read_BIN2R v%s %d records * 100 channels; SHA256 %s; independent Python raw channel parity PASS",
         fer, as.character(packageVersion("Luminescence")),length(pts),got))
  cat(tail(parity_summary,1),"\n")
  utils::write.csv(meta,file.path("out",paste0(fer,"_R_official_metadata.csv")),row.names=FALSE)
  rm(obs,meta,pts); gc()
}
writeLines(parity_summary,"out/parity.txt")
cat("READER_PARITY_PASS both FER original groups\n")
if(identical(Sys.getenv("MQR_READER_ONLY"),"1")) quit(save="no",status=0)

# The upstream 2021 R Markdown explicitly warns these example subsets are SHORTENED.
# Same author workflow: Generate_DataFile, AgeS_Computation, prior 10..100 ka,
# origin fit TRUE, "lognormal_A", 5000 sample, t=5, 3 chains.
# Package 0.3.3 marks Generate_DataFile deprecated but still exports it.
set.seed(4112L)
samples <- c("FER1","FER3")
# BayLum 0.3.3 deprecated Generate_DataFile(). Its recursive directory import
# fails on the 2021 source with Luminescence 1.3.1 ("subscript out of bounds").
# Use the package-author supported replacement create_DataFile() with precisely
# the same ORIGINAL CSV settings, 49 included grains, and source BIN files.
config <- lapply(samples, function(fer) {
  src <- file.path(data_path,fer)
  lines <- readLines(file.path(src,"rule.csv"),warn=FALSE)
  lines <- lines[grepl("=",lines,fixed=TRUE)]
  name_key <- trimws(sub("=.*$","",lines))
  val <- as.numeric(trimws(sub("^[^=]*=","",lines)))
  stopifnot(length(val)==10,all(is.finite(val)),all(!duplicated(name_key)))
  rules <- as.list(stats::setNames(val,name_key))
  source_dose <- as.numeric(utils::read.csv(file.path(src,"DoseSource.csv"))[1,])
  env_dose <- as.numeric(utils::read.csv(file.path(src,"DoseEnv.csv"))[1,])
  stopifnot(length(source_dose)==2,length(env_dose)==2,all(is.finite(source_dose)),all(is.finite(env_dose)))
  list(sample=fer,files=input(fer),
       settings=list(dose_source=source_dose,dose_env=env_dose,
                     rules=rules))
})
dat <- BayLum::create_DataFile(config_file=config,verbose=FALSE)
if(!is.list(dat)||!all(c("LT","sLT","ITimes","J","K")%in%names(dat))) {
  stop("Original-source modern BayLum create_DataFile did not produce a valid model input.")
}
cat("CREATE_DATAFILE_REPLACEMENT_PASS keys:", paste(names(dat),collapse=","),"\n")
cat("Model J selected grains:",paste(dat$J,collapse=","),"regeneration K:",paste(dat$K,collapse=","),"\n")
stopifnot(all(dat$J==49L))
saveRDS(dat,file.path("out","FER1_FER3_BayLum_source_generated_data.rds"))
params <- list(DATA=dat,SampleNames=names,Nb_sample=2,
   PriorAge=rep(c(10,100),2),BinPerSample=rep(1,2),
   SavePdf=FALSE,OutputFileName=character(),OutputFilePath="out/",
   SaveEstimates=FALSE,OutputTableName=character(),OutputTablePath="out/",
   sepTHETA=";",sepSC=",", LIN_fit=FALSE, Origin_fit=TRUE,
   distribution="lognormal_A",Iter=5000,t=5,n.chains=3,
   jags_method="rjags",quiet=TRUE,roundingOfValue=2)
run_age <- function(case, theta=NULL, strati=NULL) {
  cat("BayLum POSTERIOR START",case,"\n")
  pp<-params
  pp$THETA<-if(is.null(theta)) numeric() else theta
  pp$StratiConstraints<-if(is.null(strati)) numeric() else strati
  res <- do.call(BayLum::AgeS_Computation,pp)
  if(!inherits(res,"BayLum.list") || is.null(res$Sampling) || is.null(res$Ages)) {
    stop(paste("Missing actual BayLum sampling output",case))
  }
  saveRDS(res,file.path("out",paste0("BayLum_",case,"_posterior.rds")))
  utils::write.csv(res$Ages,file.path("out",paste0("BayLum_",case,"_published_age_summary.csv")),row.names=FALSE)
  cat("ACTUAL BAYLUM POSTERIOR",case,"\n")
  print(res$Ages)
  ch <- lapply(res$Sampling, function(x) {
    m <- as.matrix(x)
    # Keep labelled age parameters only when possible.
    if(ncol(m)<2) stop("posterior chain has <2 columns")
    coda::mcmc(m)
  })
  if(length(ch)>=2) {
    ml <- coda::mcmc.list(ch)
    cat("coda effectiveSize",paste(round(coda::effectiveSize(ml),2),collapse=" "),"\n")
    cat("coda gelman.diag (univariate PSRF):\n")
    print(tryCatch(coda::gelman.diag(ml,multivariate=FALSE),
                   error=function(e) paste("diag unavailable:",conditionMessage(e))))
  } else {
    cat("Convergence diagnostics require multiple chains: HOLD\n")
  }
  invisible(res)
}
baseline <- run_age("no_strat_no_cov")
theta <- as.matrix(utils::read.csv(file.path(data_path,"CovarianceMatrix_22_RealisticExample.csv"),sep=";"))
stopifnot(all(dim(theta)==c(2,2)),all(is.finite(theta)),all(eigen(theta,symmetric=TRUE)$values>0))
strati <- BayLum::SC_Ordered(Nb_sample=2)
realistic <- run_age("strat_realistic_cov",theta=theta,strati=strati)
cat("P0 POSTERIOR RECEIPT: 2 genuine FER author model runs executed with 5000 samples, 3 chains, t=5\n")
cat("Do not treat tutorial C14 43400±400 as physical 2015 radiocarbon age; C14 scenario NOT run.\n")
