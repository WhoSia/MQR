module Main where
import Data.Char(toUpper)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import System.Environment(getArgs)
import System.Exit(exitFailure)

data Status=Fail|Hold|Pass deriving(Eq,Ord,Show)
data Bridge=Bridge{bid::String,bsrc::String,bdst::String,blocal::Status,bcustody::Status} deriving Show
data Packet=Packet{
 pid::String,sourceAuth::Maybe Status,finalAuth::Maybe Status,bridges::[Bridge],
 semantics::M.Map String (Status,String),semanticComp::Maybe (Status,String),
 scopeSource::S.Set String,scopeMaps::M.Map String [(String,String)],finalClaim::S.Set String,
 ancestors::[(String,Status)],preserves::S.Set (String,String),assumptions::[(String,String,String,Status)],
 defeats::[(String,String,String,String)],directReceipt::Maybe Status,requested::Maybe Status} deriving Show

emptyP=Packet "" Nothing Nothing [] M.empty Nothing S.empty M.empty S.empty [] S.empty [] [] Nothing Nothing

up=map toUpper
parseStatus s=case up s of{"FAIL"->Right Fail;"HOLD"->Right Hold;"PASS"->Right Pass;x->Left("invalid status "++x)}
txt Fail="FAIL";txt Hold="HOLD";txt Pass="PASS"
meet a b=min a b

parsePacket s=go emptyP False False (zip [1..] (lines s)) where
 go p st en []|not st=Left"missing REALCOMPOSE 0.6"|not en=Left"missing END"|otherwise=validate p
 go p st en ((n,r):xs)
  |en=go p st en xs
  |null w || head w=="#"=go p st en xs
  |head w=="REALCOMPOSE"=if w==["REALCOMPOSE","0.6"] then go p True en xs else Left"expected REALCOMPOSE 0.6"
  |not st=Left"packet must begin REALCOMPOSE 0.6"
  |head w=="END"=go p st True xs
  |otherwise=step p w >>= \p'->go p' st en xs
  where w=words r
 step p w=case w of
  ["id",x]->Right p{pid=x}
  ["source_authority",x]->do a<-parseStatus x;Right p{sourceAuth=Just a}
  ["final_authority",x]->do a<-parseStatus x;Right p{finalAuth=Just a}
  ["bridge",i,a,b,l,c]->do l'<-parseStatus l;c'<-parseStatus c;Right p{bridges=bridges p++[Bridge i a b l' c']}
  ["semantic",i,s,warr]->do s'<-parseStatus s;Right p{semantics=M.insert i (s',up warr)(semantics p)}
  ["semantic_comp",s,warr]->do s'<-parseStatus s;Right p{semanticComp=Just(s',up warr)}
  ("scope_source":xs)->Right p{scopeSource=S.union(scopeSource p)(S.fromList xs)}
  ["scope_map",i,a,b]->Right p{scopeMaps=M.insertWith(++) i [(a,b)](scopeMaps p)}
  ("final_claim":xs)->Right p{finalClaim=S.union(finalClaim p)(S.fromList xs)}
  ["ancestor",i,s]->do s'<-parseStatus s;Right p{ancestors=ancestors p++[(i,s')]}
  ["preserve",b,a]->Right p{preserves=S.insert(b,a)(preserves p)}
  ["assumption",b,k,v,s]->do s'<-parseStatus s;Right p{assumptions=assumptions p++[(b,k,up v,s')]}
  ["defeat",b,a,z,stt]->let q=up stt in if elem q ["REACHABLE","DEAD","FORBIDDEN"] then Right p{defeats=defeats p++[(b,a,z,q)]} else Left"invalid defeat state"
  ["direct_receipt",s]->do s'<-parseStatus s;Right p{directReceipt=Just s'}
  ["authorize",s]->do s'<-parseStatus s;Right p{requested=Just s'}
  _->Left("malformed command "++unwords w)
 validate p|pid p==""||sourceAuth p==Nothing||finalAuth p==Nothing||length(bridges p)<2||requested p==Nothing=Left"missing required composition field"|otherwise=Right p

endpoint p=if and[bdst a==bsrc b|(a,b)<-zip(bridges p)(tail(bridges p))] then Pass else Fail
semantic p=foldl meet Pass (locals++[comp]) where
 locals=[case M.lookup(bid b)(semantics p) of Nothing->Hold;Just(s,w)->if w=="SELF" then Fail else s|b<-bridges p]
 comp=case semanticComp p of Nothing->Hold;Just(s,w)->if w=="SELF" then Fail else s
scopeC p=if S.null(finalClaim p)||S.null(scopeSource p) then Hold else if all(\x->S.member x final)(S.toList(finalClaim p)) then Pass else Fail where
 final=foldl step(scopeSource p)(bridges p)
 step fr b=case M.lookup(bid b)(scopeMaps p) of Nothing->S.empty;Just ms->S.fromList[z|(a,z)<-ms,S.member a fr]
ancestryC p|null(ancestors p)=Hold|all ok[(b,a)|(a,_)<-ancestors p,b<-bridges p]=Pass|otherwise=Fail where ok(b,a)=S.member(bid b,a)(preserves p)
defeatC p=foldl meet Pass [one b|b<-bridges p] where
 one b=let xs=[(a,z,s)|(i,a,z,s)<-defeats p,i==bid b] in if null xs then Hold else if any(\(a,z,s)->s=="REACHABLE"&&a==bsrc b&&z==bdst b)xs then Pass else Fail
assumptionC p=if conflict then Fail else foldl meet Pass[s|(_,_,_,s)<-assumptions p] where
 m=foldl add M.empty[(k,v)|(_,k,v,_)<-assumptions p]
 add m'(k,v)=M.insertWith(++) k [v] m'
 conflict=any((>1).length.S.fromList)(M.elems m)
localC p=foldl meet Pass[meet(blocal b)(bcustody b)|b<-bridges p]
globalC p=if fa>ceiling then Fail else Pass where
 fa=maybe Fail id(finalAuth p);sa=maybe Fail id(sourceAuth p)
 ceiling=foldl meet sa([s|(_,s)<-ancestors p]++[s|(_,_,_,s)<-assumptions p])
directC p=maybe Hold id(directReceipt p)
derive p=M.fromList ks where
 ks0=[("endpoint",endpoint p),("semantic",semantic p),("scope",scopeC p),("ancestry",ancestryC p),("defeat",defeatC p),("assumption",assumptionC p),("local",localC p),("global_nonamplification",globalC p),("direct",directC p)]
 comp=foldl meet Pass(map snd ks0);ks=ks0++[("composition",comp)]

emit p d=do
 putStrLn"HASKELL-REAL-COMPOSITION=0.6"
 putStrLn("id="++pid p)
 mapM_(\k->putStrLn("coordinate."++k++"="++txt(d M.! k)))["endpoint","semantic","scope","ancestry","defeat","assumption","local","global_nonamplification","direct","composition"]
 putStrLn"composition.meaning=CONDITIONAL_PATHWISE_NONAMPLIFICATION"
 putStrLn"local_pass_does_not_imply_composite_pass=true"
 putStrLn"adjacent_pass_does_not_imply_direct_pass=true"
 putStrLn"algebraic_composability_is_not_epistemic_composability=true"

main=do
 as<-getArgs
 if null as then putStrLn"usage: runghc ComposeV06.hs PACKET..." >> exitFailure else mapM_ run as
 where
  run f=do s<-readFile f;case parsePacket s of
   Left e->putStrLn e>>exitFailure
   Right p->let d=derive p;req=maybe Fail id(requested p);got=d M.!"composition" in if req>got then putStrLn("COMPOSITION_LAUNDERING: requested "++txt req++" above derived "++txt got)>>exitFailure else emit p d
