module Main where

import Data.Char (toUpper)
import Data.List (isPrefixOf, nub, sort)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import System.Environment (getArgs)
import System.Exit (exitFailure)

data Status = Fail | Hold | Pass deriving (Eq, Ord, Show)
data Mode = FormalMediated | Nonformal deriving (Eq, Show)

data Packet = Packet
  { pid :: String
  , mode :: Maybe Mode
  , claimScope :: String
  , worldScope :: String
  , statementScope :: String
  , worldAuthority :: Maybe Status
  , scopeEdges :: [(String,String)]
  , witnesses :: [(Status,String)]
  , ancestors :: [(String,String,Status)]
  , preserved :: S.Set String
  , defeatStates :: [String]
  , formalCustody :: String
  , requested :: String
  } deriving Show

emptyPacket :: Packet
emptyPacket = Packet "" Nothing "" "" "" Nothing [] [] [] S.empty [] "" ""

upper :: String -> String
upper = map toUpper

parseStatus :: String -> Either String Status
parseStatus s = case upper s of
  "FAIL" -> Right Fail
  "HOLD" -> Right Hold
  "PASS" -> Right Pass
  x -> Left ("invalid status " ++ x)

statusText :: Status -> String
statusText Fail = "FAIL"
statusText Hold = "HOLD"
statusText Pass = "PASS"

stripQuotes :: String -> String
stripQuotes s
  | length s >= 2 && head s == '"' && last s == '"' = init (tail s)
  | otherwise = s

parsePacket :: String -> Either String Packet
parsePacket txt = go emptyPacket False False (zip [1..] (lines txt))
  where
    go p started ended []
      | not started = Left "missing REALTRANSFER 0.5"
      | not ended = Left "missing END"
      | otherwise = validateRequired p
    go p started ended ((n,raw):xs)
      | ended = go p started ended xs
      | null ws || "#" `isPrefixOf` head ws = go p started ended xs
      | head ws == "REALTRANSFER" =
          if ws == ["REALTRANSFER","0.5"]
          then go p True ended xs
          else Left ("line "++show n++": expected REALTRANSFER 0.5")
      | not started = Left ("line "++show n++": packet must begin REALTRANSFER 0.5")
      | head ws == "END" = go p started True xs
      | otherwise = step p ws >>= \p' -> go p' started ended xs
      where ws = words raw

    step p ws = case ws of
      ["id",x] -> Right p{pid=stripQuotes x}
      ["mode",x] -> case upper x of
        "FORMAL_MEDIATED" -> Right p{mode=Just FormalMediated}
        "NONFORMAL" -> Right p{mode=Just Nonformal}
        y -> Left ("invalid mode "++y)
      ["claim_scope",x] -> Right p{claimScope=x}
      ["world_scope",x] -> Right p{worldScope=x}
      ["statement_scope",x] -> Right p{statementScope=x}
      ["world_authority",x] -> do s<-parseStatus x; Right p{worldAuthority=Just s}
      ["scope_contains",a,b] -> Right p{scopeEdges=(a,b):scopeEdges p}
      ("semantic_witness":_:st:warrant:_) -> do
        s<-parseStatus st
        let w=upper warrant
        if w `elem` ["EXTERNAL","SELF","UNTESTED"]
          then Right p{witnesses=(s,w):witnesses p}
          else Left ("invalid warrant "++w)
      ["ancestor",a,role,st] -> do
        s<-parseStatus st
        let r=upper role
        if r `elem` ["LOAD_BEARING","AUXILIARY"]
          then Right p{ancestors=(a,r,s):ancestors p}
          else Left ("invalid ancestor role "++r)
      ["preserve",a] -> Right p{preserved=S.insert a (preserved p)}
      ("defeat_path":_:st:_) ->
        let d=upper st in
        if d `elem` ["REACHABLE","DEAD","FORBIDDEN"]
          then Right p{defeatStates=d:defeatStates p}
          else Left ("invalid defeat state "++d)
      ("formal_custody":st:_) ->
        let s=upper st in
        if s `elem` ["PASS","HOLD","FAIL","NOT_APPLICABLE"]
          then Right p{formalCustody=s}
          else Left ("invalid formal custody "++s)
      ["authorize",a] ->
        let x=upper a in
        if x `elem` ["PASS","HOLD","FAIL","NOT_APPLICABLE"]
          then Right p{requested=x}
          else Left ("invalid authorization "++x)
      _ -> Left ("malformed command: " ++ unwords ws)

    validateRequired p
      | null (pid p) || mode p == Nothing || null (claimScope p) || null (worldScope p)
        || worldAuthority p == Nothing || null (formalCustody p) || null (requested p)
        = Left "missing required transfer field"
      | mode p == Just FormalMediated && null (statementScope p)
        = Left "FORMAL_MEDIATED requires statement_scope"
      | otherwise = Right p

reachable :: [(String,String)] -> String -> String -> Bool
reachable edges sup sub
  | sup == sub = True
  | otherwise = bfs S.empty [sup]
  where
    bfs _ [] = False
    bfs seen (x:xs)
      | S.member x seen = bfs seen xs
      | otherwise =
          let ys=[b | (a,b)<-edges,a==x]
          in sub `elem` ys || bfs (S.insert x seen) (xs++ys)

rankText :: String -> Maybe Int
rankText "FAIL" = Just 0
rankText "HOLD" = Just 1
rankText "PASS" = Just 2
rankText _ = Nothing

derive :: Packet -> Either String (M.Map String String)
derive p = do
  wa <- maybe (Left "missing world authority") Right (worldAuthority p)
  let load=[(a,s)|(a,r,s)<-ancestors p,r=="LOAD_BEARING"]
  if null load then Left "no LOAD_BEARING ancestry" else Right ()
  let ceiling=minimum (map snd load)
  if wa > ceiling
    then Left ("WORLD_AUTHORITY_LAUNDERING: "++statusText wa++" exceeds load-bearing ancestry ceiling "++statusText ceiling)
    else Right ()
  case mode p of
    Just Nonformal -> do
      if formalCustody p /= "NOT_APPLICABLE" then Left "NONFORMAL requires formal_custody NOT_APPLICABLE" else Right ()
      if requested p /= "NOT_APPLICABLE" then Left "NONFORMAL transfer authorization must be NOT_APPLICABLE" else Right ()
      let sc=if reachable (scopeEdges p) (worldScope p) (claimScope p) then "PASS" else "FAIL"
      Right $ M.fromList
        [("semantic","NOT_APPLICABLE"),("scope",sc),("ancestry","NOT_APPLICABLE"),
         ("defeat","NOT_APPLICABLE"),("noncircular","NOT_APPLICABLE"),
         ("formal_custody","NOT_APPLICABLE"),("transfer","NOT_APPLICABLE")]
    Just FormalMediated -> do
      let sem=if not (null (witnesses p)) && all (\(s,w)->s==Pass && w=="EXTERNAL") (witnesses p) then "PASS" else "FAIL"
          sc=if reachable (scopeEdges p) (worldScope p) (claimScope p)
                && reachable (scopeEdges p) (statementScope p) (claimScope p) then "PASS" else "FAIL"
          anc=if all (\(a,_)->S.member a (preserved p)) load then "PASS" else "FAIL"
          def=if "REACHABLE" `elem` defeatStates p then "PASS" else "FAIL"
          nonc=if not (null (witnesses p)) && all ((/="SELF").snd) (witnesses p) then "PASS" else "FAIL"
          cust=case formalCustody p of
                 "PASS"->"PASS"; "HOLD"->"HOLD"; "FAIL"->"FAIL"; _->"FAIL"
          coords=[sem,sc,anc,def,nonc,cust]
          tr | "FAIL" `elem` coords || wa==Fail = "FAIL"
             | all (=="PASS") coords && wa==Pass = "PASS"
             | otherwise = "HOLD"
      rr <- maybe (Left "FORMAL_MEDIATED authorization may not be NOT_APPLICABLE") Right (rankText (requested p))
      gr <- maybe (Left "internal transfer status error") Right (rankText tr)
      if rr>gr then Left ("TRANSFER_LAUNDERING: requested "++requested p++" above derived "++tr) else Right ()
      Right $ M.fromList
        [("semantic",sem),("scope",sc),("ancestry",anc),("defeat",def),
         ("noncircular",nonc),("formal_custody",cust),("transfer",tr)]
    Nothing -> Left "missing mode"

emit :: Packet -> M.Map String String -> IO ()
emit p d = do
  putStrLn "HASKELL-REAL-TRANSFER=0.5"
  putStrLn ("id="++pid p)
  mapM_ (\k->putStrLn ("coordinate."++k++"="++M.findWithDefault "MISSING" k d))
    ["semantic","scope","ancestry","defeat","noncircular","formal_custody","transfer"]
  putStrLn "implementation_diversity_is_not_semantic_independence=true"

minimality :: IO ()
minimality = do
  let coords=["SEMANTIC","SCOPE","ANCESTRY","DEFEAT","NONCIRCULAR","FORMAL_CUSTODY"]
      attacks=M.fromList
        [("SEMANTIC_ALIAS","SEMANTIC"),("SCOPE_PROMOTION","SCOPE"),
         ("ANCESTRY_LOSS","ANCESTRY"),("DEFEAT_MIRAGE","DEFEAT"),
         ("BRIDGE_BOOTSTRAP","NONCIRCULAR"),("FORMAL_ROUTE_CUSTODY","FORMAL_CUSTODY")]
      subsets=filter (not.null) (power coords)
      blocks ss=all (`elem` ss) (M.elems attacks)
      good=filter blocks subsets
      m=minimum (map length good)
      mins=filter ((==m).length) good
  putStrLn ("FROZEN_ATTACK_COORDINATES="++show (length coords))
  putStrLn ("MINIMUM_BLOCKING_COORDINATES="++show m)
  putStrLn ("MINIMAL_SETS="++show (map sort mins))
  putStrLn "MINIMALITY_SCOPE=FROZEN_ATTACK_FAMILY_ONLY"
  where
    power []=[[]]
    power (x:xs)=let r=power xs in r++map (x:) r

main :: IO ()
main = do
  args<-getArgs
  case args of
    ["--minimality"] -> minimality
    [] -> putStrLn "usage: runghc TransferV05.hs PACKET | --minimality" >> exitFailure
    paths -> mapM_ run paths
  where
    run path = do
      txt<-readFile path
      case parsePacket txt >>= \p -> derive p >>= \d -> Right (p,d) of
        Left e -> putStrLn e >> exitFailure
        Right (p,d) -> emit p d
