import json
import sys

def getTeamAliases(dataFileNames):
  teamAliases = {}
  for dataFileName in dataFileNames:
    with open(dataFileName, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for team in data:
        current_name = team["participant_name"]
        names_history = team["names_history"].split(',')
        for name in names_history:
            teamAliases[name] = current_name
  return teamAliases

if __name__ == "__main__":
    print(getTeamAliases(sys.argv[1]))