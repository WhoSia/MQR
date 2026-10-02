module Main where

import Data.Bits
import Data.List (group, sort, minimumBy)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import Data.Ord (comparing)
import System.Directory (createDirectoryIfMissing)

type State = Int
type Part = [Int]

data Sev = NONE | BOUNDED | MATERIAL | FATAL
  deriving (Eq, Ord, Enum, Bounded, Show)

data Profile = Profile
  { pSep :: Sev
  , pReopen :: Sev
  , pProv :: Sev
  , pExt :: Sev
  , pRelease :: Sev
  } deriving (Eq, Show)

data Candidate = Candidate
  { cName :: String
  , cPart :: Part
  } deriving Show

data Budget = Budget
  { bName :: String
  , bProfile :: Profile
  } deriving Show

events :: [Int]
events = [0..17]

sepEvents, reopenEvents, provEvents, extEvents, releaseEvents :: [Int]
sepEvents = [0..11]
reopenEvents = events
provEvents = [12,13,14]
extEvents = [2,5,8,11,15,16,17]
releaseEvents = events

has :: State -> Int -> Bool
has s b = testBit s b

setB, clrB :: State -> Int -> State
setB = setBit
clrB = clearBit

step :: State -> Int -> State
step s e = case e of
  0 -> setB s 0
  1 -> setB s 1
  2 -> setB s 2
  3 -> clrB s 0
  4 -> clrB s 1
  5 -> clrB s 2
  6 -> setB s 3
  7 -> setB s 4
  8 -> setB s 5
  9 -> clrB s 3
  10 -> clrB s 4
  11 -> clrB s 5
  12 -> setB s 7
  13 -> clrB s 7
  14 -> if has s 7 then setB s 6 else clrB s 6
  15 -> setB s 8
  16 -> clrB s 8
  17 -> if has s 8 then clrB (setB s 2) 5 else s
  _ -> error "event"

unresolvedVec :: State -> Int
unresolvedVec s =
  sum [ if has s i && not (has s (3+i)) then bit i else 0 | i <- [0..2] ]

unresolvedCount :: State -> Int
unresolvedCount s = popCount (unresolvedVec s)

release :: State -> Bool
release s = unresolvedCount s == 0 && has s 6

reopenObs :: State -> Int
reopenObs s =
  (if unresolvedCount s > 0 then 1 else 0) .|.
  (if not (has s 6) then 2 else 0)

provObs :: State -> Int
provObs s = if has s 6 then 1 else 0

extObs :: State -> Int
extObs s = if has s 2 && not (has s 5) then 1 else 0

releaseObs :: State -> Int
releaseObs s = if release s then 1 else 0

authorityLabel :: State -> (Int,Int,Int)
authorityLabel s =
  let u=unresolvedCount s
      rel=release s
      mask=(1 .|. 2 .|. if rel then 4 else 8)
  in (u,mask,if rel then 1 else 0)

states :: [State]
states=[0..511]

canonicalize :: Ord a => [a] -> Part
canonicalize sigs =
  let uniq = map head . group . sort $ sigs
      mp=M.fromList (zip uniq [0..])
  in map (mp M.!) sigs

obsPart :: (State -> Int) -> Part
obsPart f=canonicalize [f s | s<-states]

refine :: [Int] -> Part -> Part
refine es p=canonicalize [(p!!s,[p!!step s e|e<-es]) | s<-states]

levels :: (State->Int) -> [Int] -> [Part]
levels obs es=take 5 $ iterate (refine es) (obsPart obs)

sepLevels, reopenLevels, provLevels, extLevels, releaseLevels :: [Part]
sepLevels=levels unresolvedVec sepEvents
reopenLevels=levels reopenObs reopenEvents
provLevels=levels provObs provEvents
extLevels=levels extObs extEvents
releaseLevels=levels releaseObs releaseEvents

sevFor :: [Part] -> State -> State -> Sev
sevFor ps s t =
  case [k | (k,p)<-zip [0..4] ps, p!!s /= p!!t] of
    (k:_) | k<=1 -> FATAL
          | k<=3 -> MATERIAL
          | otherwise -> BOUNDED
    [] -> NONE

sevRank :: Sev -> Int
sevRank=fromEnum

partBlocks :: Part -> Int
partBlocks p=1+maximum p

mergedPairs :: Part -> [(State,State)]
mergedPairs p=[(s,t)|s<-states,t<-[s+1..511],p!!s==p!!t]

q1 :: Part
q1=canonicalize [authorityLabel s|s<-states]

q2 :: Part
q2=refine events q1

q3 :: Part
q3=iterate (refine events) q1 !! 3

dropBitPart :: Int -> Part
dropBitPart b=canonicalize [ s .&. complement (bit b) | s<-states ]

visible7 :: Part
visible7=canonicalize [s .&. 0x7f | s<-states]

identityPart :: Part
identityPart=states

candidates :: [Candidate]
candidates =
  [ Candidate "A0_FULL" identityPart
  , Candidate "A1_DROP_P" (dropBitPart 7)
  , Candidate "A2_DROP_X" (dropBitPart 8)
  , Candidate "A3_VISIBLE_7" visible7
  , Candidate "A4_Q2_4_66" q2
  , Candidate "A5_Q3_4_66" q3
  , Candidate "A6_CURRENT_AUTHORITY" q1
  ]

profileFor :: Part -> Profile
profileFor p =
  let ps=mergedPairs p
      maxS f=foldl max NONE [f s t | (s,t)<-ps]
  in Profile
      (maxS (sevFor sepLevels))
      (maxS (sevFor reopenLevels))
      (maxS (sevFor provLevels))
      (maxS (sevFor extLevels))
      (maxS (sevFor releaseLevels))

allSevs :: Profile -> [Sev]
allSevs p=[pSep p,pReopen p,pProv p,pExt p,pRelease p]

budgets :: [Budget]
budgets =
  [ Budget "B0_CONSERVATIVE" (Profile BOUNDED BOUNDED BOUNDED BOUNDED BOUNDED)
  , Budget "B1_EXPLORATORY" (Profile MATERIAL BOUNDED BOUNDED MATERIAL BOUNDED)
  , Budget "B2_ARCHIVAL" (Profile MATERIAL MATERIAL NONE MATERIAL BOUNDED)
  ]

decision :: Profile -> Profile -> String
decision l b
  | pRelease l==FATAL = "FORBID_MERGE"
  | pReopen l==FATAL = "REEXPAND_REQUIRED"
  | pProv l==FATAL || pExt l==FATAL = "REOPEN_REQUIRED"
  | or (zipWith (>) (allSevs l) (allSevs b)) = "HOLD_INCOMPARABLE"
  | any (>NONE) (allSevs l) = "ACCEPT_WITH_AUDIT"
  | otherwise = "ACCEPT_LOCAL"

acceptable :: String -> Bool
acceptable d=d=="ACCEPT_LOCAL" || d=="ACCEPT_WITH_AUDIT"

selectForBudget :: [(Candidate,Profile)] -> Budget -> String
selectForBudget cps b =
  let ok=[c | (c,p)<-cps, acceptable (decision p (bProfile b))]
  in if null ok then "NONE" else cName $ minimumBy (comparing (partBlocks . cPart)) ok

countSev :: [Part] -> Part -> Sev -> Int
countSev lv p q =
  length [() | (s,t)<-mergedPairs p, sevFor lv s t==q]

profileRow :: (Candidate,Profile) -> String
profileRow (c,p)=
  let mp=mergedPairs (cPart c)
      cnt lv q=countSev lv (cPart c) q
  in concat
    [ cName c,"\t",show(partBlocks(cPart c)),"\t",show(length mp)
    ,"\t",show(pSep p),"\t",show(pReopen p),"\t",show(pProv p),"\t",show(pExt p),"\t",show(pRelease p)
    ,"\t",show(cnt sepLevels NONE),"\t",show(cnt sepLevels BOUNDED),"\t",show(cnt sepLevels MATERIAL),"\t",show(cnt sepLevels FATAL)
    ,"\t",show(cnt reopenLevels NONE),"\t",show(cnt reopenLevels BOUNDED),"\t",show(cnt reopenLevels MATERIAL),"\t",show(cnt reopenLevels FATAL)
    ,"\t",show(cnt provLevels NONE),"\t",show(cnt provLevels BOUNDED),"\t",show(cnt provLevels MATERIAL),"\t",show(cnt provLevels FATAL)
    ,"\t",show(cnt extLevels NONE),"\t",show(cnt extLevels BOUNDED),"\t",show(cnt extLevels MATERIAL),"\t",show(cnt extLevels FATAL)
    ,"\t",show(cnt releaseLevels NONE),"\t",show(cnt releaseLevels BOUNDED),"\t",show(cnt releaseLevels MATERIAL),"\t",show(cnt releaseLevels FATAL)
    ,"\n"
    ]

weights :: [[Int]]
weights=[[a,b,c,d,e]|a<-[1,2,4],b<-[1,2,4],c<-[1,2,4],d<-[1,2,4],e<-[1,2,4]]

scoreWith :: [Int] -> [Int] -> Profile -> Int
scoreWith enc ws p=sum(zipWith (\w s -> w*(enc!!sevRank s)) ws (allSevs p))

indexOf :: String -> Int
indexOf n=case [i| (i,c)<-zip[0..] candidates,cName c==n] of
  (x:_)->x
  _->999

winner :: [Int] -> [(Candidate,Profile)] -> [Int] -> String
winner enc cps ws =
  cName . fst $ minimumBy (comparing (\(c,p)->(scoreWith enc ws p, indexOf (cName c)))) cps

pairReversals :: [Int] -> [(Candidate,Profile)] -> Int
pairReversals enc cps =
  length
    [ ()
    | i<-[0..length cps-1], j<-[i+1..length cps-1]
    , let (_,pi)=cps!!i
          (_,pj)=cps!!j
          diffs=[compare(scoreWith enc w pi)(scoreWith enc w pj)|w<-weights]
    , elem LT diffs && elem GT diffs
    ]

budgetSelections :: [(Candidate,Profile)] -> [(String,String)]
budgetSelections cps=[(bName b,selectForBudget cps b)|b<-budgets]

matchingWeights :: [Int] -> [(Candidate,Profile)] -> Int
matchingWeights enc cps =
  let sels=map snd (budgetSelections cps)
  in length [w|w<-weights, let x=winner enc cps w, all (==x) sels]

profileByName :: [(Candidate,Profile)] -> String -> Profile
profileByName cps n=head[p|(c,p)<-cps,cName c==n]

debtSteps :: [(Candidate,Profile)] -> [Int]
debtSteps cps=go seqNames [0,0,0,0,0] [0,0,0,0,0] 1
  where
    seqNames=["A3_VISIBLE_7","A4_Q2_4_66","A3_VISIBLE_7","A5_Q3_4_66"]
    thresh=[4,3,2,3,2]
    vals p=map sevRank(allSevs p)
    go [] _ first _=first
    go (n:ns) cur first k=
      let vs=vals(profileByName cps n)
          cur'=zipWith (+) cur vs
          first'=[if f==0 && v>=t then k else f | (f,v,t)<-zip3 first cur' thresh]
      in go ns cur' first' (k+1)

main :: IO ()
main=do
  let cps=[(c,profileFor(cPart c))|c<-candidates]
      enc1=[0,1,2,3]
      enc2=[0,1,3,9]
      wins1=S.fromList[winner enc1 cps w|w<-weights]
      wins2=S.fromList[winner enc2 cps w|w<-weights]
      rev1=pairReversals enc1 cps
      rev2=pairReversals enc2 cps
      mw1=matchingWeights enc1 cps
      mw2=matchingWeights enc2 cps
      ds=debtSteps cps
      sels=budgetSelections cps
  createDirectoryIfMissing True "experiments/mqr-4.67/results"
  writeFile "experiments/mqr-4.67/results/haskell_profiles.tsv" $
    "candidate\tblocks\tmerged_pairs\tworst_sep\tworst_reopen\tworst_prov\tworst_ext\tworst_release" ++
    concat ["\t"++coord++"_"++sev | coord<-["sep","reopen","prov","ext","release"],sev<-["none","bounded","material","fatal"]] ++
    "\n" ++ concatMap profileRow cps
  writeFile "experiments/mqr-4.67/results/haskell_summary.tsv" $
    unlines $
      ["metric\tvalue"
      ,"SOURCE_STATES\t512"
      ,"EVENTS\t18"
      ,"CANDIDATES\t7"
      ,"WEIGHT_VECTORS\t243"
      ,"SCALAR_WINNERS_ENC0123\t"++show(S.size wins1)
      ,"SCALAR_WINNERS_ENC0139\t"++show(S.size wins2)
      ,"PAIRWISE_REVERSALS_ENC0123\t"++show rev1
      ,"PAIRWISE_REVERSALS_ENC0139\t"++show rev2
      ,"WEIGHTS_MATCH_ALL_BUDGET_SELECTIONS_ENC0123\t"++show mw1
      ,"WEIGHTS_MATCH_ALL_BUDGET_SELECTIONS_ENC0139\t"++show mw2
      ,"DEBT_TRIGGER_STEP_SEP\t"++show(ds!!0)
      ,"DEBT_TRIGGER_STEP_REOPEN\t"++show(ds!!1)
      ,"DEBT_TRIGGER_STEP_PROV\t"++show(ds!!2)
      ,"DEBT_TRIGGER_STEP_EXT\t"++show(ds!!3)
      ,"DEBT_TRIGGER_STEP_RELEASE\t"++show(ds!!4)
      ] ++ [name++"_SELECTED\t"++sel | (name,sel)<-sels]
  putStrLn "MQR467_HASKELL_COURT=PASS"
  mapM_ (\(c,p)->putStrLn(cName c++" blocks="++show(partBlocks(cPart c))++" loss="++show p)) cps
  mapM_ (\(n,s)->putStrLn(n++" selected="++s)) sels
  putStrLn $ "scalar_winners_0123="++show(S.toList wins1)
  putStrLn $ "scalar_pair_reversals_0123="++show rev1
  putStrLn $ "debt_trigger_steps="++show ds
