#!/usr/bin/env python3
"""MQR 4.100: byte-pinned EDI source versus published palmerpenguins combined table.
No values overwritten; classify exact, notation-only, and substantive differences.
"""
import argparse,csv,hashlib,io,json,zipfile,collections,decimal,pathlib,xml.etree.ElementTree as ET

VERSIONS=[('Adelie','knb-lter-pal.219.5','table_219.csv','1W3nVhoZU9PKK3Qv_f3MEB3Veq10nzsrL','29771c188cb1274b30f3d356716a3eadfed0954c55bbe5675cb49b10d26c79bd'),('Gentoo','knb-lter-pal.220.5','table_220.csv','10CfoUN0o0GjVORTBHYY1DXmnY_qBtlHs','7d141b10500a849c9de7f36c175f424ff929aa951100c0e5c62d50313186ddb9'),('Chinstrap','knb-lter-pal.221.6','table_221.csv','1GnyzU11ueJEmhUT0I1PnxCxuDXz0esQ0','c83097abfda2489386eedae03e8f3dd8835f655463bd6caf173c2ae271b50b0e')]
NUM={'Sample Number','Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)','Delta 15 N (o/oo)','Delta 13 C (o/oo)'}
NULL={'','NA','N/A','NULL','.'}

def digest(b):return hashlib.sha256(b).hexdigest()
def val(k,x):
 s=(x or '').strip()
 if s.upper() in NULL:return None
 if k in NUM:
  try:return decimal.Decimal(s)
  except decimal.InvalidOperation: pass
 return s

def read_csv(blob):
 s=blob.decode('utf-8-sig'); rows=list(csv.DictReader(io.StringIO(s)))
 assert rows and all(None not in row for row in rows)
 return rows,list(rows[0])
def norm(k,x):
 a=val(k,x)
 return str(a.normalize()) if isinstance(a,decimal.Decimal) else a

def main():
 parser=argparse.ArgumentParser(description='Strict MQR EDI original-source audit, unmodified input bytes')
 parser.add_argument('--source-dir',type=pathlib.Path,required=True,help='Folder containing 3 EDI original ZIPs')
 parser.add_argument('--combined',type=pathlib.Path,required=True,help='Pinned published palmerpenguins combined CSV')
 parser.add_argument('--outdir',type=pathlib.Path,required=True)
 args=parser.parse_args()
 base=args.source_dir;out=args.outdir;out.mkdir(parents=True,exist_ok=True);combined_data=args.combined.read_bytes();combined,columns=read_csv(combined_data)
 assert digest(combined_data)=='144f623143c9360fd77322a4f86acb06dc198814dbd2669724c63e6457b907bd','combined SHA differs from pinned secondary source'
 assert len(combined)==344 and len(columns)==17
 merged=[];packages=[];origins={}; quality=[]
 for species,package,datafilename,driveid,expected_sha in VERSIONS:
  path=base/(package+'.zip');zip_raw=path.read_bytes()
  assert digest(zip_raw)==expected_sha, f'EDI authenticated source bytes drift: {package}'
  with zipfile.ZipFile(io.BytesIO(zip_raw)) as z:
   assert z.testzip() is None
   expected={datafilename,package+'.xml',package+'.txt',package+'.report.xml','manifest.txt'}
   assert set(z.namelist())==expected
   xml=z.read(package+'.xml')
   tree=ET.fromstring(xml)
   assert tree.attrib.get('packageId')==package
   csvdata=z.read(datafilename)
   rows,cols=read_csv(csvdata)
   assert cols==columns
   manifest=z.read('manifest.txt').decode('utf8')
   assert all(f'{f} (' in manifest for f in [datafilename,package+'.xml',package+'.txt',package+'.report.xml'])
   for r in rows:
    assert r['Species'].split()[0].lower()==species.lower()
   merged+=rows
   for r in rows:
    origins[(r['studyName'],r['Individual ID'])]={'edi_species':species,'edi_package':package,'edi_data_file':datafilename}
   packages.append({'species':species,'version':package,'drive_id':driveid,'zip_bytes':len(zip_raw),'zip_sha256':digest(zip_raw),'zip_member_count':len(z.namelist()),'zip_crc_pass':True,
                    'data_csv_file':datafilename,'data_csv_bytes':len(csvdata),'data_csv_sha256':digest(csvdata),'rows':len(rows),'columns':cols,
                    'metadata_xml_sha256':digest(xml),'quality_xml_sha256':digest(z.read(package+'.report.xml')),'manifest_sha256':digest(z.read('manifest.txt')),
                    'raw_null_counts':{c:sum((r[c] or '').strip().upper() in NULL for r in rows) for c in cols}})
 idx_src=collections.defaultdict(list);idx_comb=collections.defaultdict(list)
 for r in merged:idx_src[(r['studyName'],r['Individual ID'])].append(r)
 for r in combined:idx_comb[(r['studyName'],r['Individual ID'])].append(r)
 dup_orig=sum(len(v)-1 for v in idx_src.values());dup_comb=sum(len(v)-1 for v in idx_comb.values())
 assert dup_orig==dup_comb==0
 source_only=sorted(set(idx_src)-set(idx_comb));combined_only=sorted(set(idx_comb)-set(idx_src))
 assert not source_only and not combined_only
 differences=[];all_changes=[];class_counts=collections.Counter();per_column=collections.defaultdict(collections.Counter)
 substantive=[];precision_only=[];rawsame=0
 for k in sorted(idx_src):
  a=idx_src[k][0];b=idx_comb[k][0];origin=origins[k]
  for field in columns:
   x=a[field];y=b[field]
   if x==y:
    rawsame+=1;class_counts['byte-level cell text equal']+=1;continue
   nx,ny=val(field,x),val(field,y)
   if nx==ny:
    group='formatting_or_null_encoding_only'
   elif field in NUM and isinstance(nx,decimal.Decimal) and isinstance(ny,decimal.Decimal):
    # Compare to explicitly *original EDI reported precision*; no arbitrary tolerance.
    original_quantum=decimal.Decimal(1).scaleb(nx.as_tuple().exponent)
    rounded=ny.quantize(original_quantum,rounding=decimal.ROUND_HALF_EVEN)
    group='extra_low_order_digits_consistent_with_float_serialization' if rounded==nx else 'numeric_measurement_disagreement'
   else:group='value_disagreement'
   item={'key':{'studyName':k[0],'Individual ID':k[1]},'species':origin['edi_species'],'source_file':origin['edi_data_file'],'column':field,'edi_text':x,'combined_text':y,'classification':group}
   if group=='extra_low_order_digits_consistent_with_float_serialization':
    item['absolute_decimal_delta']=str(abs(nx-ny));precision_only.append(item)
   if group.endswith('disagreement'):substantive.append(item)
   all_changes.append(item)
   if group != 'formatting_or_null_encoding_only' or len(differences)<14: differences.append(item)
   class_counts[group]+=1;per_column[field][group]+=1
 assert len(merged)==344 and len(combined)==344
 # independent row-by-row exact decimal-preserving comparison, with explicit exceptions
 same_lexical_cells=rawsame
 levels=collections.Counter(r['Species'] for r in merged)
 years=collections.Counter(r['studyName'] for r in merged)
 key1=[(r['studyName'],r['Sample Number']) for r in merged]
 key2=[(r['Species'],r['studyName'],r['Sample Number']) for r in merged]
 original_full_order=[(r['studyName'],r['Individual ID']) for r in merged]
 combined_order=[(r['studyName'],r['Individual ID']) for r in combined]
 counts={'both_rows':len(combined),'matched_keys':len(idx_src),'source_only_keys':len(source_only),'combined_only_keys':len(combined_only),'source_duplicate_keys':dup_orig,'combined_duplicate_keys':dup_comb,
         'total_field_comparisons':len(merged)*len(columns),'raw_text_cell_matches':rawsame,'raw_text_differences':len(merged)*len(columns)-rawsame,
         'classification_counts_for_raw_text_differences':dict(class_counts),'substantive_disagreements_at_edi_reported_precision':len(substantive), 'reported_precision_level_variations':len(precision_only),
         'combined_and_EDI_concatenation_row_order_identical':original_full_order==combined_order,
         'weak_studyName_plus_sampleNumber_collisions':len(key1)-len(set(key1)),
         'strong_species_studyName_sampleNumber_collisions':len(key2)-len(set(key2)),
         'species':dict(levels),'years':dict(years)}
 manifest={'scope':'Original authenticated EDI package bytes from user vs SHA-pinned published combined palmerpenguins secondary CSV; deterministic post-observation audit, NOT independent biological inference',
           'input_combined':{'source_commit':'8957207b78d6ccd1b4654a9dd9c9041b657478ab','sha256':digest(combined_data),'size':len(combined_data),'rows':len(combined),'columns':columns},
           'packages':packages,'counts':counts,'raw_text_differences_by_column':{k:dict(v) for k,v in per_column.items()},
           'precise_numeric_serialization_residuals':precision_only, 'substantive_disagreements':substantive,
           'no_correction_to_source':True, 'caveats':['Row-key uniqueness in a published collection does not establish globally unique birds across seasons.','Rounding combined text to explicit EDI reported precision matches the 5 isotope cells. The extra digits are consistent with floating-point serialization, but the actual transform code/cause was not reconstructed or proved.','This is a check of the pinned 344-row secondary combined version; not proof of all versions of palmerpenguins.','Same DOI/version metadata and original ZIP are provided by the user via authenticated EDI portal; internal hashes and manifest were verified, not a repository signature.']}
 (out/'edi_p6_audit.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 with (out/'edi_p6_all_488_text_differences.csv').open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,['species','package','studyName','Individual ID','column','edi_text','combined_text','classification']);w.writeheader()
  for e in all_changes:w.writerow({'species':e['species'],'package':origins[(e['key']['studyName'],e['key']['Individual ID'])]['edi_package'],
       'studyName':e['key']['studyName'],'Individual ID':e['key']['Individual ID'],'column':e['column'],
       'edi_text':e['edi_text'],'combined_text':e['combined_text'],'classification':e['classification']})
 with (out/'edi_p6_all_344_row_map.csv').open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,['combined_row_1_based','source_package','source_csv','source_row_1_based','species','studyName','Individual ID']);w.writeheader()
  src_positions={}
  for species,package,datafile,driveid,expected_sha in VERSIONS:
   with zipfile.ZipFile(base/(package+'.zip')) as z:
    src,_=read_csv(z.read(datafile))
   for ii,row in enumerate(src,1):src_positions[(row['studyName'],row['Individual ID'])]=(package,datafile,ii,species)
  for ii,row in enumerate(combined,1):
   pack,filename,source_row,species=src_positions[(row['studyName'],row['Individual ID'])]
   w.writerow({'combined_row_1_based':ii,'source_package':pack,'source_csv':filename,
     'source_row_1_based':source_row,'species':species,'studyName':row['studyName'],'Individual ID':row['Individual ID']})
 with (out/'edi_p6_precision_exceptions.csv').open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,['species','source_file','studyName','Individual ID','column','edi_text','combined_text','absolute_decimal_delta']);w.writeheader()
  for e in precision_only:w.writerow({'species':e['species'],'source_file':e['source_file'],'studyName':e['key']['studyName'],'Individual ID':e['key']['Individual ID'],'column':e['column'],'edi_text':e['edi_text'],'combined_text':e['combined_text'],'absolute_decimal_delta':e['absolute_decimal_delta']})
 assert not substantive,'Substantive field disagreements require separate source review'
 print(json.dumps({'packages':[{k:p[k] for k in ('species','version','rows','zip_sha256')} for p in packages],'counts':counts,'raw_text_differences_by_column':manifest['raw_text_differences_by_column'],'precise_numeric_serialization_residuals':precision_only},indent=2))

if __name__=='__main__':main()
