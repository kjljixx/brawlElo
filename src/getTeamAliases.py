import json
import sys

def getTeamAliases(dataFileName):
  with open(dataFileName, 'r', encoding='utf-8') as file:
      data = json.load(file)

  teamAliases = {}

  for team in data:
      current_name = team["participant_name"]
      names_history = team["names_history"].split(',')
      for name in names_history:
          teamAliases[name] = current_name
  return teamAliases

if __name__ == "__main__":
    print(getTeamAliases(sys.argv[1]))