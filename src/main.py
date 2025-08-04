from getAllData import getAllData
import os
import sys

regionAbbrevParam = sys.argv[1]
regionAbbrevs = ["ea", "emea", "na", "sa"] if regionAbbrevParam == "world" else [regionAbbrevParam]
matchFiles = [[f"../bsc-2025-raw/february/{regionAbbrev.upper()} MFs.json",
              f"../bsc-2025-raw/february/{regionAbbrev.upper()} MQs1.json",
              f"../bsc-2025-raw/february/{regionAbbrev.upper()} MQs2.json",
              f"../bsc-2025-raw/march/{regionAbbrev.upper()} MFs.json",
              f"../bsc-2025-raw/march/{regionAbbrev.upper()} MQs1.json",
              f"../bsc-2025-raw/march/{regionAbbrev.upper()} MQs2.json",
              f"../bsc-2025-raw/april/{regionAbbrev.upper()} MFs.json",
              f"../bsc-2025-raw/april/{regionAbbrev.upper()} MQs1.json",
              f"../bsc-2025-raw/april/{regionAbbrev.upper()} MQs2.json",
              f"../bsc-2025-raw/june/{regionAbbrev.upper()} MFs.json",
              f"../bsc-2025-raw/june/{regionAbbrev.upper()} MQs1.json",
              f"../bsc-2025-raw/june/{regionAbbrev.upper()} MQs2.json",
              f"../bsc-2025-raw/july/{regionAbbrev.upper()} MFs.json",
              f"../bsc-2025-raw/july/{regionAbbrev.upper()} MQs1.json",
              f"../bsc-2025-raw/july/{regionAbbrev.upper()} MQs2.json",
              # f"../bsc-2025-raw/august/{regionAbbrev.upper()} MFs.json",
              f"../bsc-2025-raw/august/{regionAbbrev.upper()} MQs1.json",
              f"../bsc-2025-raw/august/{regionAbbrev.upper()} MQs2.json"
             ] for regionAbbrev in regionAbbrevs]
matchFiles = [matchFile for regionMatchFiles in matchFiles for matchFile in regionMatchFiles]
if regionAbbrevParam == "world":
  matchFiles.extend(
    [
      "../bsc-2025-raw/world/Brawl Cup.json"
    ]
  )
  regionAbbrevs.append("world")
results = getAllData(matchFiles, [f"../bsc-2025-raw/leaderboards/2025-{regionAbbrev.lower()}-leaderboard.json" for regionAbbrev in regionAbbrevs])

outputFileName = f"../output/{regionAbbrevParam.lower()}/{regionAbbrevParam.lower()}-data.pgn"
with open(outputFileName, 'w', encoding='utf-8') as file:
  for teams, result in results.items():
    team1Wins = result[0]
    team2Wins = result[1]
    for i in range(team1Wins):
      file.write(f'[White "{teams[0]}"]\n')
      file.write(f'[Black "{teams[1]}"]\n')
      file.write('[Result "1-0"]\n')
    for i in range(team2Wins):
      file.write(f'[White "{teams[0]}"]\n')
      file.write(f'[Black "{teams[1]}"]\n')
      file.write('[Result "0-1"]\n')
file.close()

game_cutoff = 30

os.system(f"..{os.sep}ordo -Q -G -j ../output/{regionAbbrevParam.lower()}/{regionAbbrevParam.lower()}-h2h.txt -o ../output/{regionAbbrevParam.lower()}/{regionAbbrevParam.lower()}-rankings.txt -t {game_cutoff} -p ../output/{regionAbbrevParam.lower()}/{regionAbbrevParam.lower()}-data.pgn")
