from getTeamAliases import getTeamAliases
import json
import sys

def getData(dataFileName, teamsFileNames, results = {}):
  with open(dataFileName, 'r', encoding='utf-8') as file:
    data = json.load(file)

  teamAliases = getTeamAliases(teamsFileNames)

  matches = data["match"]

  for match in matches:
    if match["opponent1"] == None:
      continue
    if match["opponent2"] == None:
      continue

    currResults = [0, 0]
    games = match["match_games"]
    for game in games:
      if game["opponent1"]["score"] == None:
        continue
      if game["opponent2"]["score"] == None:
        continue
      currResults[0] += game["opponent1"]["score"]
      currResults[1] += game["opponent2"]["score"] 

    if not "name" in match["opponent1"].keys():
      continue
    if not "name" in match["opponent2"].keys():
      continue
    opp1 = match["opponent1"]["name"]
    opp2 = match["opponent2"]["name"]
    if not opp1 in teamAliases.keys():
      continue
    if not opp2 in teamAliases.keys():
      continue

    opp1 = teamAliases[opp1]
    opp2 = teamAliases[opp2]
    
    if not (opp1, opp2) in results.keys():
      results[(opp1, opp2)] = currResults
    else:
      results[(opp1, opp2)][0] += currResults[0]
      results[(opp1, opp2)][1] += currResults[1]

  # return results

if __name__ == "__main__":
    print(getData(sys.argv[1], sys.argv[2]))