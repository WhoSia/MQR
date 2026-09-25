module Main where
import Data.Char(toUpper)
import Data.List(tails)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import System.Environment(getArgs)
import System.Exit(exitFailure)
data St=F|H|P deriving(Eq,Ord,Show)
data Root=Root String String St String deriving Show
data Bridge=Bridge String St deriving Show
data Nat=Nat String St String String deriving Show
data Pw=Pw String String String St deriving Show
data Packet=Packet{ident::String,kind::String,sa::Maybe St,fa::Maybe St,roots::[Root],degrees::S.Set String,covers::[(String,String)],qroots::[(String,String)],gens::[(String,String,String)],endpoint::String,bridges::[Bridge],nats::[Nat],paths::[Pw],peq::M.Map(String,String)St,exts::M.Map String St,coh::Maybe(St,String),anc::[(String,St)],pres::S.Set(String,String),defs::[String],target::String,just::[(String,String)],direct::String,req::Maybe St}deriving Show
empty=Packet"" "" Nothing Nothing[]S.empty[][][]""[][][]M.empty M.empty Nothing[]S.empty[]""[]""Nothing
up=map toUpper
ps x=case up x of{"FAIL"->Right F;"HOLD"->Right H;"PASS"->Right P;_->Left"bad status"}
tx F="FAIL";tx H="HOLD";tx P="PASS";mt=min
rs(Root _ _ s f)=mt s(case f of{"LIVE"->P;"STALE"->H;"EXPIRED"->F;_->F})
pair a b=if a<=b then(a,b)else(b,a)
parse s=go empty False False(lines s)where
 go p st en []|not st=Left"missing header"|not en=Left"missing END"|otherwise=Right p
 go p st en(r:xs)|en=go p st en xs|null w||head w=="#"=go p st en xs|head w=="REALSUBSTITUTE"=if w==["REALSUBSTITUTE","0.7"]then go p True en xs else Left"bad header"|not st=Left"no header"|head w=="END"=go p st True xs|otherwise=step p w>>= \q->go q st en xs where w=words r
 step p w=case w of
  ["id",x]->Right p{ident=x}
  ["claim_kind",x]->Right p{kind=up x}
  ["source_authority",x]->do s'<-ps x;Right p{sa=Just s'}
  ["final_authority",x]->do s'<-ps x;Right p{fa=Just s'}
  ["root",i,k,s',f]->do z<-ps s';Right p{roots=roots p++[Root i(up k)z(up f)]}
  ["degree",d]->Right p{degrees=S.insert d(degrees p)}
  ["cover",d,r]->Right p{covers=covers p++[(d,r)]}
  ["query_root",q,r]->Right p{qroots=qroots p++[(q,r)]}
  ["generate",b,a,z]->Right p{gens=gens p++[(b,a,z)]}
  ["endpoint_query",q]->Right p{endpoint=q}
  ["bridge",i,_,_,s']->do z<-ps s';Right p{bridges=bridges p++[Bridge i z]}
  ["naturality",b,s',m,r]->do z<-ps s';Right p{nats=nats p++[Nat b z(up m)r]}
  ["path",i,a,z,s']->do q<-ps s';Right p{paths=paths p++[Pw i a z q]}
  ["path_equal",a,b,s']->do q<-ps s';Right p{peq=M.insert(pair a b)q(peq p)}
  ["extension",a,s']->do q<-ps s';Right p{exts=M.insert(up a)q(exts p)}
  ["coherence",s',m]->do q<-ps s';Right p{coh=Just(q,up m)}
  ["ancestor",a,s']->do q<-ps s';Right p{anc=anc p++[(a,q)]}
  ["preserve",b,a]->Right p{pres=S.insert(b,a)(pres p)}
  ["assumption",_,_,_]->Right p
  ["defeat",d]->Right p{defs=defs p++[up d]}
  ["justification_target",x]->Right p{target=x}
  ["justify",a,b]->Right p{just=just p++[(a,b)]}
  ["direct_receipt",x]->Right p{direct=up x}
  ["authorize",x]->do q<-ps x;Right p{req=Just q}
  _->Left("bad line "++unwords w)
rm p=M.fromList[(i,r)|r@(Root i _ _ _)<-roots p]
used p=S.fromList([r|(_,r)<-covers p]++[r|(_,r)<-qroots p]++[r|Nat _ _ m r<-nats p,m=="EMPIRICAL",r/="NONE"])
cext p=if S.null u then F else foldl mt P[case M.lookup x m of{Just r@(Root _ "EXTERNAL" _ _)->rs r;_->F}|x<-S.toList u]where u=used p;m=rm p
cbasis p=if S.null(degrees p)then H else foldl mt P[one d|d<-S.toList(degrees p)]where m=rm p;one d=let ss=[rs r|(dd,x)<-covers p,dd==d,Just r@(Root _ "EXTERNAL" _ _)<-[M.lookup x m]]in if null ss then F else maximum ss
cquery p=if S.member(endpoint p)final then P else F where m=rm p;start=S.fromList[q|(q,x)<-qroots p,Just r@(Root _ "EXTERNAL" _ _)<-[M.lookup x m],rs r/=F];final=foldl step start(bridges p);step fr(Bridge b _)=S.fromList[z|(bb,a,z)<-gens p,bb==b,S.member a fr]
cnat p=foldl mt P[one b|Bridge b _<-bridges p]where m=rm p;one b=case[n|n@(Nat x _ _ _)<-nats p,x==b]of{[]->H;(Nat _ _ "SELF" _:_)->F;(Nat _ _ "UNTESTED" _:_)->H;(Nat _ s "EMPIRICAL" r:_)->case M.lookup r m of{Just rr@(Root _ "EXTERNAL" _ _)->mt s(rs rr);_->F};(Nat _ s _ _:_) -> s}
cpath p|null(paths p)=H|length(paths p)==1=let(Pw _ _ _ s)=head(paths p)in s|otherwise=foldl mt P(states++eqs)where ps'=paths p;Pw _ a z _=head ps';states=[s|Pw _ x y s<-ps',x==a,y==z]++[F|any(\(Pw _ x y _)->x/=a||y/=z)ps'];prs=[(u,v)|(u:rest)<-tails ps',v<-rest];eqs=[M.findWithDefault H(pair i j)(peq p)|(Pw i _ _ _,Pw j _ _ _)<-prs]
ccong p=if length(paths p)<=1 then P else mt(M.findWithDefault H"PRE"(exts p))(M.findWithDefault H"POST"(exts p))
ccoh p=case coh p of{Just(s,"CLOSED")->s;Just(F,_)->F;_->H}
canc p=if null(anc p)then H else if all(\(a,_)->all(\(Bridge b _)->S.member(b,a)(pres p))(bridges p))(anc p)then foldl mt P(map snd(anc p))else F
cnew p=if kind p=="NEW_EMPIRICAL"then F else P
cdef p=if null(defs p)then H else if all(=="REACHABLE")(defs p)then P else F
nodes n es=go S.empty[n]where go s[] =s;go s(x:xs)|S.member x s=go s xs|otherwise=go(S.insert x s)(xs++[b|(a,b)<-es,a==x])
cex p=if S.null ex then F else if all(\n->not(S.null(S.intersection ex(nodes n(just p)))))(S.toList(nodes(target p)(just p)))then P else F where ex=S.fromList[i|Root i "EXTERNAL" _ _<-roots p]
cbridge p=foldl mt P[s|Bridge _ s<-bridges p]
cglobal p=let m=rm p;rootst=[rs r|x<-S.toList(used p),Just r<-[M.lookup x m]];ceil=foldl mt(maybe F id(sa p))(map snd(anc p)++rootst)in if maybe F id(fa p)>ceil then F else P
cdirect p=case direct p of{"ABSENT"->P;"PASS"->P;"HOLD"->H;"FAIL"->H;_->F}
derive p=M.fromList(base++[("substitution",foldl mt P(map snd base))])where base=[("external_root",cext p),("world_contact_basis",cbasis p),("query_basis",cquery p),("naturality",cnat p),("path_independence",cpath p),("congruence",ccong p),("higher_coherence",ccoh p),("ancestry",canc p),("no_new_empirical_degree",cnew p),("defeat_to_world",cdef p),("exteriority",cex p),("bridge_state",cbridge p),("global_nonamplification",cglobal p),("direct_conflict",cdirect p)]
power[]=[[]];power(x:xs)=let r=power xs in r++map(x:)r
mins p=let rr=[i|r@(Root i "EXTERNAL" _ _)<-roots p,rs r==P];good ss=all(\d->any(\(dd,r)->dd==d&&elem r ss)(covers p))(S.toList(degrees p));g=filter good(power rr)in if null g then[]else let k=minimum(map length g)in filter((==k).length)g
emit p d=do putStrLn"HASKELL-REAL-SUBSTITUTION=0.7";mapM_(\k->putStrLn("coordinate."++k++"="++tx(d M.!k)))["external_root","world_contact_basis","query_basis","naturality","path_independence","congruence","higher_coherence","ancestry","no_new_empirical_degree","defeat_to_world","exteriority","bridge_state","global_nonamplification","direct_conflict","substitution"];let mm=mins p;putStrLn("wcb.minimum_declared_roots="++if null mm then"UNAVAILABLE"else show(length(head mm)))
run mini f=do s<-readFile f;case parse s of{Left e->putStrLn e>>exitFailure;Right p->if mini then let mm=mins p in putStrLn("DECLARED_WCB_MIN_ROOTS="++if null mm then"UNAVAILABLE"else show(length(head mm)))>>putStrLn"WCB_MINIMALITY_IS_RELATIVE_TO_DECLARED_DEGREES_AND_COVERS=TRUE" else let d=derive p;g=d M.!"substitution";r=maybe F id(req p)in if r>g then putStrLn"SUBSTITUTION_LAUNDERING">>exitFailure else emit p d}
main=do a<-getArgs;case a of{["--basis-minimality",f]->run True f;[]->exitFailure;fs->mapM_(run False)fs}
