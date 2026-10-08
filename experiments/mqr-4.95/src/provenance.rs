//! Research-root conflict court: original publisher paper reports GBIF-derived
//! Anemone nemorosa observations. Portal/file/DOI differences alone do not
//! establish independent observations or a valid binary non-detection witness.
//! No string-based fixture here is an externally verified observation receipt.

pub const ORIGINAL_GBIF_ANEMONE_DOWNLOAD:&str="0031144-240626123714530";
pub const ORIGINAL_TAXON:&str="Anemone nemorosa L.";

#[derive(Debug,Clone,Copy,PartialEq,Eq)]
pub enum SourceVerdict {
    TaxonMismatch,
    ReusedOriginalDownload,
    OverlappingObservationId,
    TargetFrameMismatch,
    BinaryNegativeObservationMissing,
    SourceAncestryUnresolved,
    CandidateForExternalHumanAuditOnly,
}
#[derive(Debug)]
pub struct Candidate<'a> {
    pub taxon: &'a str,
    pub gbif_download_key: Option<&'a str>,
    pub original_observation_ids: &'a [&'a str],
    pub prospective_observation_ids: &'a [&'a str],
    pub target_site_protocol_matched: bool,
    pub verified_binary_non_detection: bool,
    pub source_ancestry_independently_checked: bool,
}
pub fn court(c:&Candidate<'_>)->SourceVerdict {
    if c.taxon!=ORIGINAL_TAXON{return SourceVerdict::TaxonMismatch;}
    if c.gbif_download_key==Some(ORIGINAL_GBIF_ANEMONE_DOWNLOAD) {
        return SourceVerdict::ReusedOriginalDownload;
    }
    if c.prospective_observation_ids.iter().any(|id|c.original_observation_ids.contains(id)){
        return SourceVerdict::OverlappingObservationId;
    }
    if !c.target_site_protocol_matched{return SourceVerdict::TargetFrameMismatch;}
    if !c.verified_binary_non_detection{return SourceVerdict::BinaryNegativeObservationMissing;}
    if !c.source_ancestry_independently_checked ||
       c.original_observation_ids.is_empty() ||
       c.prospective_observation_ids.is_empty() {
        return SourceVerdict::SourceAncestryUnresolved;
    }
    // Reaching this state merely allows a further human audit and does NOT
    // independently authenticate field records or prove sampling design.
    SourceVerdict::CandidateForExternalHumanAuditOnly
}
pub fn example_known_original_collision()->SourceVerdict {
    court(&Candidate{
        taxon:ORIGINAL_TAXON,
        gbif_download_key:Some(ORIGINAL_GBIF_ANEMONE_DOWNLOAD),
        original_observation_ids:&[],
        prospective_observation_ids:&[],
        target_site_protocol_matched:true,
        verified_binary_non_detection:true,
        source_ancestry_independently_checked:false
    })
}
#[cfg(test)]
mod tests {
    use super::*;
    fn fixture<'a>(key:Option<&'a str>)->Candidate<'a>{
        Candidate{
            taxon:ORIGINAL_TAXON,
            gbif_download_key:key,
            original_observation_ids:&["orig-1","orig-2"],
            prospective_observation_ids:&["new-1","new-2"],
            target_site_protocol_matched:true,
            verified_binary_non_detection:true,
            source_ancestry_independently_checked:true
        }
    }
    #[test] fn same_gbif_parent_download_not_independent_despite_portal_name(){
        assert_eq!(example_known_original_collision(),SourceVerdict::ReusedOriginalDownload);
        assert_eq!(court(&fixture(Some(ORIGINAL_GBIF_ANEMONE_DOWNLOAD))),SourceVerdict::ReusedOriginalDownload);
    }
    #[test] fn new_download_and_recycled_observation_id_is_ancestry_collision(){
        let mut x=fixture(Some("different-new-download"));
        x.prospective_observation_ids=&["new-1","orig-2"];
        assert_eq!(court(&x),SourceVerdict::OverlappingObservationId);
    }
    #[test] fn source_record_without_observed_absence_is_not_binary_calibration(){
        let mut x=fixture(Some("different-new-download"));
        x.verified_binary_non_detection=false;
        assert_eq!(court(&x),SourceVerdict::BinaryNegativeObservationMissing);
    }
    #[test] fn mismatched_taxon_and_target_scope_are_not_promoted(){
        let mut x=fixture(None);
        x.taxon="Anemone species unspecified";
        assert_eq!(court(&x),SourceVerdict::TaxonMismatch);
        x.taxon=ORIGINAL_TAXON;
        x.target_site_protocol_matched=false;
        assert_eq!(court(&x),SourceVerdict::TargetFrameMismatch);
    }
    #[test] fn different_url_with_unknown_observation_ancestry_remains_hold(){
        let mut x=fixture(Some("different-new-download"));
        x.original_observation_ids=&[];
        assert_eq!(court(&x),SourceVerdict::SourceAncestryUnresolved);
        x.original_observation_ids=&["orig-1"];
        x.source_ancestry_independently_checked=false;
        assert_eq!(court(&x),SourceVerdict::SourceAncestryUnresolved);
        x.source_ancestry_independently_checked=true;
        assert_eq!(court(&x),SourceVerdict::CandidateForExternalHumanAuditOnly);
    }
}
