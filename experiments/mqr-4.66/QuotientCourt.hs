module Main where

import Data.Bits
import Data.List (group, sort)
import qualified Data.Map.Strict as M
import System.CPUTime
import Text.Printf

type State = Int
type Block = Int

data Event
  = Rp0 | Rp1 | Rp2 | Rm0 | Rm1 | Rm2
  | Sp0 | Sp1 | Sp2 | Sm0 | Sm1 | Sm2
  | PGood | PBad | Audit | XOn | XOff | Novelty
  deriving (Eq, Ord, Enum, Bounded, Show)

events :: [Event]
events = [minBound .. maxBound]

bitR, bitS :: Int -> Int
bitR i = i
bitS i = 3 + i

bitC, bitP, bitX :: Int
bitC = 6
bitP = 7
bitX = 8

has :: State -> Int -> Bool
has s b = testBit s b

setB, clrB :: State -> Int -> State
setB = setBit
clrB = clearBit

step :: State -> Event -> State
step s e = case e of
  Rp0 -> setB s (bitR 0)
  Rp1 -> setB s (bitR 1)
  Rp2 -> setB s (bitR 2)
  Rm0 -> clrB s (bitR 0)
  Rm1 -> clrB s (bitR 1)
  Rm2 -> clrB s (bitR 2)
  Sp0 -> setB s (bitS 0)
  Sp1 -> setB s (bitS 1)
  Sp2 -> setB s (bitS 2)
  Sm0 -> clrB s (bitS 0)
  Sm1 -> clrB s (bitS 1)
  Sm2 -> clrB s (bitS 2)
  PGood -> setB s bitP
  PBad -> clrB s bitP
  Audit -> if has s bitP then setB s bitC else clrB s bitC
  XOn -> setB s bitX
  XOff -> clrB s bitX
  Novelty ->
    if has s bitX
      then clrB (setB s (bitR 2)) (bitS 2)
      else s

unresolved :: State -> Int
unresolved s =
  length [ i | i <- [0..2], has s (bitR i) && not (has s (bitS i)) ]

release :: State -> Bool
release s = unresolved s == 0 && has s bitC

actionMask :: State -> Int
actionMask s =
  let base = 1 .|. 2
  in if release s then base .|. 4 else base .|. 8

label :: State -> (Int,Int,Int)
label s = (unresolved s, actionMask s, if release s then 1 else 0)

encodeLabel :: State -> Int
encodeLabel s =
  let (u,m,r) = label s
  in u * 64 + m * 2 + r

states :: [State]
states = [0..511]

canonicalize :: Ord a => [a] -> [Block]
canonicalize sigs =
  let uniq = map head . group . sort $ sigs
      mp = M.fromList (zip uniq [0..])
  in map (mp M.!) sigs

q0 :: [Block]
q0 = canonicalize [ unresolved s | s <- states ]

q1 :: [Block]
q1 = canonicalize [ label s | s <- states ]

refineOnce :: [Block] -> [Block]
refineOnce part =
  canonicalize
    [ (encodeLabel s, part !! s, [ part !! step s e | e <- events ])
    | s <- states
    ]

iterateN :: Int -> [Block] -> [Block]
iterateN 0 p = p
iterateN n p = iterateN (n-1) (refineOnce p)

stable :: [Block] -> ([Block],Int)
stable p0 = go p0 0
  where
    go p n =
      let p' = refineOnce p
      in if p' == p then (p,n) else go p' (n+1)

blockCount :: [Block] -> Int
blockCount p = 1 + maximum p

visibleSig :: State -> Int
visibleSig s = s .&. 0x7f

mergedPairCount :: (State -> Int) -> Integer
mergedPairCount f =
  let counts = M.elems $ M.fromListWith (+) [ (f s, 1::Integer) | s <- states ]
  in sum [ quot (n*(n-1)) 2 | n <- counts ]

historiesOf :: Int -> [[Event]]
historiesOf 0 = [[]]
historiesOf n = [ e:xs | e <- events, xs <- historiesOf (n-1) ]

replay :: [Event] -> State
replay = foldl step 0

allHistories :: [[Event]]
allHistories = concatMap historiesOf [0..4]

writeMap :: FilePath -> [Block] -> IO ()
writeMap path p =
  writeFile path $ "state\tblock\n" ++
    concat [ show s ++ "\t" ++ show (p !! s) ++ "\n" | s <- states ]

main :: IO ()
main = do
  t0 <- getCPUTime
  let q2 = refineOnce q1
      q3 = iterateN 3 q1
      (q4, rounds) = stable q1
      hCount = length allHistories
      reached = map replay allHistories
      distinctReached = length . map head . group . sort $ reached
      q4HistBlocks = length . map head . group . sort $ [ q4 !! s | s <- reached ]
      q3eq = q3 == q4
      n1pairs = mergedPairCount visibleSig
      q1pairs = mergedPairCount (q1 !!)
      q3pairs = mergedPairCount (q3 !!)
      q0n=blockCount q0; q1n=blockCount q1; q2n=blockCount q2
      q3n=blockCount q3; q4n=blockCount q4
  if hCount /= 111151 then error ("history count drift: " ++ show hCount) else pure ()
  if length events /= 18 then error "event count drift" else pure ()

  let outDir = "experiments/mqr-4.66/results"
  writeMap (outDir ++ "/haskell_q1_mapping.tsv") q1
  writeMap (outDir ++ "/haskell_q3_mapping.tsv") q3
  writeMap (outDir ++ "/haskell_q4_mapping.tsv") q4

  let summary =
        [ ("SOURCE_STATES",512)
        , ("EVENTS",18)
        , ("HISTORIES_0_4",hCount)
        , ("DISTINCT_REACHED_SOURCE_STATES",distinctReached)
        , ("Q0_BLOCKS",q0n)
        , ("Q1_BLOCKS",q1n)
        , ("Q2_BLOCKS",q2n)
        , ("Q3_BLOCKS",q3n)
        , ("Q4_BLOCKS",q4n)
        , ("Q4_REFINEMENT_ROUNDS",rounds)
        , ("Q3_EQUALS_Q4",if q3eq then 1 else 0)
        , ("Q4_HISTORY_BLOCKS",q4HistBlocks)
        , ("N1_VISIBLE_MERGED_PAIRS",fromInteger n1pairs)
        , ("Q1_MERGED_PAIRS",fromInteger q1pairs)
        , ("Q3_MERGED_PAIRS",fromInteger q3pairs)
        ]
  writeFile (outDir ++ "/haskell_summary.tsv") $
    "metric\tvalue\n" ++ concat [ k ++ "\t" ++ show v ++ "\n" | (k,v) <- summary ]

  t1 <- getCPUTime
  let secs = fromIntegral (t1-t0) / 1.0e12 :: Double
  printf "MQR466_HASKELL_SOURCE_STATES=%d\n" (512::Int)
  printf "MQR466_HASKELL_HISTORIES=%d\n" hCount
  printf "MQR466_HASKELL_Q0_BLOCKS=%d\n" q0n
  printf "MQR466_HASKELL_Q1_BLOCKS=%d\n" q1n
  printf "MQR466_HASKELL_Q2_BLOCKS=%d\n" q2n
  printf "MQR466_HASKELL_Q3_BLOCKS=%d\n" q3n
  printf "MQR466_HASKELL_Q4_BLOCKS=%d\n" q4n
  printf "MQR466_HASKELL_Q4_ROUNDS=%d\n" rounds
  printf "MQR466_HASKELL_Q3_EQUALS_Q4=%s\n" (if q3eq then "YES" else "NO")
  printf "MQR466_HASKELL_VISIBLE_PAIRS=%d\n" n1pairs
  printf "MQR466_HASKELL_RUNTIME_SECONDS=%.6f\n" secs
  putStrLn "MQR466_HASKELL_CANONICAL=PASS"
