from getData import getData
import sys
import os

def getAllData(dataFileNames, teamsFileName):
  results = {}
  for dataFileName in dataFileNames:
    getData(dataFileName, teamsFileName, results)
  return results

if __name__ == "__main__":
  regionAbbrev = sys.argv[1]
  matchFiles = ["../bsc-2024-raw-main/march/" + regionAbbrev.upper() + " MFs.json",
                "../bsc-2024-raw-main/april/" + regionAbbrev.upper() + " MFs.json",
                "../bsc-2024-raw-main/may/" + regionAbbrev.upper() + " MFs.json",
                "../bsc-2024-raw-main/june/" + regionAbbrev.upper() + " MFs.json",
                "../bsc-2024-raw-main/july/" + regionAbbrev.upper() + " MFs.json",
                "../bsc-2024-raw-main/march/" + regionAbbrev.upper() + " MQs.json",
                "../bsc-2024-raw-main/april/" + regionAbbrev.upper() + " MQs.json",
                "../bsc-2024-raw-main/may/" + regionAbbrev.upper() + " MQs.json",
                "../bsc-2024-raw-main/june/" + regionAbbrev.upper() + " MQs.json",
                "../bsc-2024-raw-main/july/" + regionAbbrev.upper() + " MQs.json"]
  results = getAllData(matchFiles, "../bsc-2024-raw-main/leaderboards/2024-" + regionAbbrev.lower() + "-leaderboard.json")
  
  outputFileName = "../output/" + regionAbbrev.lower() + "/" + regionAbbrev.lower() + "-data.pgn"
  with open(outputFileName, 'w', encoding='utf-8') as file:
    for teams, result in results.items():
      team1Wins = result[0]
      team2Wins = result[1]
      for i in range(team1Wins):
        file.write('[White "' + teams[0] + '"]\n')
        file.write('[Black "' + teams[1] + '"]\n')
        file.write('[Result "1-0"]\n')
      for i in range(team2Wins):
        file.write('[White "' + teams[0] + '"]\n')
        file.write('[Black "' + teams[1] + '"]\n')
        file.write('[Result "0-1"]\n')
  file.close()
  os.system(".." + os.sep +"ordo -G -o ../output/" + regionAbbrev.lower() + "/" + regionAbbrev.lower() + "-rankings.txt -t 50 -p ../output/" + regionAbbrev.lower() + "/" + regionAbbrev.lower() + "-data.pgn")
  os.system(".." + os.sep +"ordo -G -j ../output/" + regionAbbrev.lower() + "/" + regionAbbrev.lower() + "-h2h.txt  ../output/" + regionAbbrev.lower() + "/" + regionAbbrev.lower() + "-data.pgn")