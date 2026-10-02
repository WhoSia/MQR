module Main where

import Data.Char (toUpper)
import Data.List (tails)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import System.Environment (getArgs)
import System.Exit (exitFailure)

data Status = Fail | Hold | Pass deriving (Eq, Ord, Show)
data Root = Root String String Status String deriving Show
data Bridge = Bridge String Status deriving Show
data Naturality = Naturality String Status String String deriving Show
data PathW = PathW String String String Status deriving Show
data Assumption = Assumption String String Status deriving Show

data Packet = Packet
  { ident :: String
  , claimKind :: String
  , sourceAuth :: Maybe Status
  , finalAuth :: Maybe Status
  , roots :: [Root]
  , degrees :: S.Set String
  , covers :: [(String,String)]
  , queryRoots :: [(String,String)]
  , generates :: [(String,String,String)]
  , endpoint :: String
  , bridges :: [Bridge]
  , naturalities :: [Naturality]
  , paths :: [PathW]
  , pathEq :: M.Map (String,String) Status
  , extensions :: M.Map String Status
  , coherenceSpec :: Maybe (Status,String)
  , ancestors :: [(String,Status)]
  , preserved :: S.Set (String,String)
  , assumptions :: [Assumption]
  , defeats :: [String]
  , justificationTarget :: String
  , justifies :: [(String,String)]
  , directReceipt :: String
  , requested :: Maybe Status
  } deriving Show

emptyPacket :: Packet
emptyPacket = Packet "" "" Nothing Nothing [] S.empty [] [] [] "" [] [] []
  M.empty M.empty Nothing [] S.empty [] [] "" [] "" Nothing

upper :: String -> String
upper = map toUpper

parseStatus :: String -> Either String Status
parseStatus x = case upper x of
  "FAIL" -> Right Fail
  "HOLD" -> Right Hold
  "PASS" -> Right Pass
  _ -> Left ("invalid status " ++ x)

statusText :: Status -> String
statusText Fail = "FAIL"
statusText Hold = "HOLD"
statusText Pass = "PASS"

meet :: Status -> Status -> Status
meet = min

rootId :: Root -> String
rootId (Root i _ _ _) = i

rootKind :: Root -> String
rootKind (Root _ k _ _) = k

rootState :: Root -> Status
rootState (Root _ _ s f) =
  meet s $ case f of
    "LIVE" -> Pass
    "STALE" -> Hold
    "EXPIRED" -> Fail
    _ -> Fail

bridgeId :: Bridge -> String
bridgeId (Bridge i _) = i

bridgeStatus :: Bridge -> Status
bridgeStatus (Bridge _ s) = s

canonPair :: String -> String -> (String,String)
canonPair a b = if a <= b then (a,b) else (b,a)

parsePacket :: String -> Either String Packet
parsePacket input = go emptyPacket False False (lines input)
  where
    go p started ended []
      | not started = Left "missing REALSUBSTITUTE 0.7"
      | not ended = Left "missing END"
      | otherwise = validate p
    go p started ended (raw:xs)
      | ended = go p started ended xs
      | null ws || head ws == "#" = go p started ended xs
      | head ws == "REALSUBSTITUTE" =
          if ws == ["REALSUBSTITUTE","0.7"]
            then go p True ended xs
            else Left "expected REALSUBSTITUTE 0.7"
      | not started = Left "packet must begin REALSUBSTITUTE 0.7"
      | head ws == "END" = go p started True xs
      | otherwise = step p ws >>= \p' -> go p' started ended xs
      where
        ws = words raw

    step p ws = case ws of
      ["id",x] -> Right p{ident=x}
      ["claim_kind",x] -> Right p{claimKind=upper x}
      ["source_authority",x] -> do
        s <- parseStatus x
        Right p{sourceAuth=Just s}
      ["final_authority",x] -> do
        s <- parseStatus x
        Right p{finalAuth=Just s}
      ["root",i,k,s,f] -> do
        st <- parseStatus s
        Right p{roots=roots p ++ [Root i (upper k) st (upper f)]}
      ["degree",d] -> Right p{degrees=S.insert d (degrees p)}
      ["cover",d,r] -> Right p{covers=covers p ++ [(d,r)]}
      ["query_root",q,r] -> Right p{queryRoots=queryRoots p ++ [(q,r)]}
      ["generate",b,a,z] -> Right p{generates=generates p ++ [(b,a,z)]}
      ["endpoint_query",q] -> Right p{endpoint=q}
      ["bridge",i,_,_,s] -> do
        st <- parseStatus s
        Right p{bridges=bridges p ++ [Bridge i st]}
      ["naturality",b,s,m,r] -> do
        st <- parseStatus s
        Right p{naturalities=naturalities p ++ [Naturality b st (upper m) r]}
      ["path",i,a,z,s] -> do
        st <- parseStatus s
        Right p{paths=paths p ++ [PathW i a z st]}
      ["path_equal",a,b,s] -> do
        st <- parseStatus s
        Right p{pathEq=M.insert (canonPair a b) st (pathEq p)}
      ["extension",side,s] -> do
        st <- parseStatus s
        Right p{extensions=M.insert (upper side) st (extensions p)}
      ["coherence",s,m] -> do
        st <- parseStatus s
        Right p{coherenceSpec=Just(st,upper m)}
      ["ancestor",a,s] -> do
        st <- parseStatus s
        Right p{ancestors=ancestors p ++ [(a,st)]}
      ["preserve",b,a] ->
        Right p{preserved=S.insert (b,a) (preserved p)}
      ["assumption",k,v,s] -> do
        st <- parseStatus s
        Right p{assumptions=assumptions p ++ [Assumption k (upper v) st]}
      ["defeat",d] ->
        Right p{defeats=defeats p ++ [upper d]}
      ["justification_target",x] ->
        Right p{justificationTarget=x}
      ["justify",a,b] ->
        Right p{justifies=justifies p ++ [(a,b)]}
      ["direct_receipt",x] ->
        Right p{directReceipt=upper x}
      ["authorize",x] -> do
        st <- parseStatus x
        Right p{requested=Just st}
      _ -> Left ("malformed command: " ++ unwords ws)

    validate p
      | null (ident p) || null (claimKind p) || sourceAuth p == Nothing
        || finalAuth p == Nothing || null (roots p) || null (bridges p)
        || null (endpoint p) || null (justificationTarget p)
        || null (directReceipt p) || requested p == Nothing
          = Left "missing required v0.7 field"
      | otherwise = Right p

rootMap :: Packet -> M.Map String Root
rootMap p = M.fromList [(rootId r,r) | r <- roots p]

usedRoots :: Packet -> S.Set String
usedRoots p = S.fromList $
  [r | (_,r) <- covers p] ++
  [r | (_,r) <- queryRoots p] ++
  [r | Naturality _ _ m r <- naturalities p, m == "EMPIRICAL", r /= "NONE"]

externalRoot :: Packet -> Status
externalRoot p
  | S.null u = Fail
  | otherwise = foldl meet Pass [one x | x <- S.toList u]
  where
    u = usedRoots p
    rm = rootMap p
    one x = case M.lookup x rm of
      Just r | rootKind r == "EXTERNAL" -> rootState r
      _ -> Fail

worldContactBasis :: Packet -> Status
worldContactBasis p
  | S.null (degrees p) = Hold
  | otherwise = foldl meet Pass [one d | d <- S.toList (degrees p)]
  where
    rm = rootMap p
    one d =
      let ss = [rootState r | (dd,x) <- covers p, dd == d,
                              Just r <- [M.lookup x rm], rootKind r == "EXTERNAL"]
      in if null ss then Fail else maximum ss

queryBasis :: Packet -> Status
queryBasis p
  | S.null start = Fail
  | S.member (endpoint p) final = Pass
  | otherwise = Fail
  where
    rm = rootMap p
    start = S.fromList
      [q | (q,x) <- queryRoots p, Just r <- [M.lookup x rm],
           rootKind r == "EXTERNAL", rootState r /= Fail]
    final = foldl step start (bridges p)
    step fr b =
      S.fromList [z | (bb,a,z) <- generates p, bb == bridgeId b, S.member a fr]

naturalityC :: Packet -> Status
naturalityC p = foldl meet Pass [one b | b <- bridges p]
  where
    rm = rootMap p
    one b = case [n | n@(Naturality bb _ _ _) <- naturalities p, bb == bridgeId b] of
      [] -> Hold
      (Naturality _ _ "SELF" _:_) -> Fail
      (Naturality _ _ "UNTESTED" _:_) -> Hold
      (Naturality _ s "EMPIRICAL" r:_) ->
        case M.lookup r rm of
          Just rr | rootKind rr == "EXTERNAL" -> meet s (rootState rr)
          _ -> Fail
      (Naturality _ s _ _:_) -> s

pathIndependence :: Packet -> Status
pathIndependence p
  | null ps = Hold
  | length ps == 1 = let PathW _ _ _ s = head ps in s
  | any wrongEndpoint ps = Fail
  | otherwise = foldl meet Pass (statuses ++ equalities)
  where
    ps = paths p
    PathW _ src0 dst0 _ = head ps
    wrongEndpoint (PathW _ s d _) = s /= src0 || d /= dst0
    statuses = [s | PathW _ _ _ s <- ps]
    pairs = [(a,b) | (a:rest) <- tails ps, b <- rest]
    equalities =
      [M.findWithDefault Hold (canonPair i j) (pathEq p)
      | (PathW i _ _ _,PathW j _ _ _) <- pairs]

congruenceC :: Packet -> Status
congruenceC p
  | length (paths p) <= 1 = Pass
  | otherwise =
      meet (M.findWithDefault Hold "PRE" (extensions p))
           (M.findWithDefault Hold "POST" (extensions p))

coherenceC :: Packet -> Status
coherenceC p = case coherenceSpec p of
  Nothing -> Hold
  Just(Fail,_) -> Fail
  Just(s,"CLOSED") -> s
  _ -> Hold

ancestryC :: Packet -> Status
ancestryC p
  | null (ancestors p) = Hold
  | all preservedEvery (ancestors p) =
      foldl meet Pass (map snd (ancestors p))
  | otherwise = Fail
  where
    preservedEvery (a,_) =
      all (\b -> S.member (bridgeId b,a) (preserved p)) (bridges p)

assumptionC :: Packet -> Status
assumptionC p
  | any ((>1) . S.size . S.fromList) (M.elems grouped) = Fail
  | otherwise = foldl meet Pass [s | Assumption _ _ s <- assumptions p]
  where
    grouped = M.fromListWith (++) [(k,[v]) | Assumption k v _ <- assumptions p]

noNewEmpirical :: Packet -> Status
noNewEmpirical p
  | claimKind p == "NEW_EMPIRICAL" = Fail
  | otherwise = Pass

defeatToWorld :: Packet -> Status
defeatToWorld p
  | null (defeats p) = Hold
  | all (=="REACHABLE") (defeats p) = Pass
  | otherwise = Fail

reachableNodes :: String -> [(String,String)] -> S.Set String
reachableNodes start es = go S.empty [start]
  where
    go seen [] = seen
    go seen (x:xs)
      | S.member x seen = go seen xs
      | otherwise = go (S.insert x seen) (xs ++ [b | (a,b) <- es, a == x])

exteriorityC :: Packet -> Status
exteriorityC p
  | S.null external = Fail
  | all reaches (S.toList nodes) = Pass
  | otherwise = Fail
  where
    external = S.fromList [rootId r | r <- roots p, rootKind r == "EXTERNAL"]
    nodes = reachableNodes (justificationTarget p) (justifies p)
    reaches n =
      not . S.null $ S.intersection external (reachableNodes n (justifies p))

bridgeState :: Packet -> Status
bridgeState p = foldl meet Pass (map bridgeStatus (bridges p))

globalNonamp :: Packet -> Status
globalNonamp p =
  if maybe Fail id (finalAuth p) > ceiling then Fail else Pass
  where
    rm = rootMap p
    rootStates =
      [rootState r | x <- S.toList (usedRoots p), Just r <- [M.lookup x rm]]
    assumptionStates = [s | Assumption _ _ s <- assumptions p]
    ceiling = foldl meet (maybe Fail id (sourceAuth p))
      (map snd (ancestors p) ++ assumptionStates ++ rootStates)

directConflict :: Packet -> Status
directConflict p = case directReceipt p of
  "ABSENT" -> Pass
  "PASS" -> Pass
  "HOLD" -> Hold
  "FAIL" -> Hold
  _ -> Fail

derive :: Packet -> M.Map String Status
derive p = M.fromList (base ++ [("substitution", foldl meet Pass (map snd base))])
  where
    base =
      [ ("external_root", externalRoot p)
      , ("world_contact_basis", worldContactBasis p)
      , ("query_basis", queryBasis p)
      , ("naturality", naturalityC p)
      , ("path_independence", pathIndependence p)
      , ("congruence", congruenceC p)
      , ("higher_coherence", coherenceC p)
      , ("ancestry", ancestryC p)
      , ("assumption", assumptionC p)
      , ("no_new_empirical_degree", noNewEmpirical p)
      , ("defeat_to_world", defeatToWorld p)
      , ("exteriority", exteriorityC p)
      , ("bridge_state", bridgeState p)
      , ("global_nonamplification", globalNonamp p)
      , ("direct_conflict", directConflict p)
      ]

power :: [a] -> [[a]]
power [] = [[]]
power (x:xs) = let r=power xs in r ++ map (x:) r

minimalCovers :: Packet -> [[String]]
minimalCovers p =
  let rs=[rootId r | r<-roots p, rootKind r=="EXTERNAL", rootState r==Pass]
      good ss=all (\d -> any (\(dd,r)->dd==d && elem r ss) (covers p))
                  (S.toList (degrees p))
      gs=filter good (power rs)
  in if S.null (degrees p) || null gs then []
     else let m=minimum (map length gs) in filter ((==m).length) gs

coordOrder :: [String]
coordOrder =
  ["external_root","world_contact_basis","query_basis","naturality",
   "path_independence","congruence","higher_coherence","ancestry","assumption",
   "no_new_empirical_degree","defeat_to_world","exteriority","bridge_state",
   "global_nonamplification","direct_conflict","substitution"]

emit :: Packet -> M.Map String Status -> IO ()
emit p d = do
  putStrLn "HASKELL-REAL-SUBSTITUTION=0.7"
  mapM_ (\k -> putStrLn ("coordinate."++k++"="++statusText(d M.! k))) coordOrder
  let ms=minimalCovers p
  putStrLn ("wcb.minimum_declared_roots=" ++
    if null ms then "UNAVAILABLE" else show (length (head ms)))

emitMinimality :: Packet -> IO ()
emitMinimality p = do
  let ms=minimalCovers p
  putStrLn ("DECLARED_WCB_MIN_ROOTS=" ++
    if null ms then "UNAVAILABLE" else show (length (head ms)))
  putStrLn "WCB_MINIMALITY_IS_RELATIVE_TO_DECLARED_DEGREES_AND_COVERS=TRUE"

runOne :: Bool -> FilePath -> IO ()
runOne minimalityMode f = do
  input <- readFile f
  case parsePacket input of
    Left e -> putStrLn e >> exitFailure
    Right p ->
      if minimalityMode
      then emitMinimality p
      else do
        let d=derive p
            got=d M.! "substitution"
            want=maybe Fail id (requested p)
        if want > got
        then putStrLn ("SUBSTITUTION_LAUNDERING: requested "++
                       statusText want++" above derived "++statusText got) >> exitFailure
        else emit p d

main :: IO ()
main = do
  args <- getArgs
  case args of
    ["--basis-minimality",f] -> runOne True f
    [] -> exitFailure
    fs -> mapM_ (runOne False) fs
