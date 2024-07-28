import json

def getTeamAliases(dataFileName, teamsToAvoidFileName):
  with open(dataFileName, 'r', encoding='utf-8') as file:
      data = json.load(file)
  with open(teamsToAvoidFileName, 'r', encoding='utf-8') as file:
      teamsToAvoid = json.load(file)

  teamAliases = {}

  for team in data:
      current_name = team["participant_name"]
      if current_name in teamsToAvoid:
          continue
      names_history = team["names_history"].split(',')
      for name in names_history:
          teamAliases[name] = current_name
  return teamAliases

if __name__ == "__main__":
    print(getTeamAliases("teams.json", "teamsToAvoid.json"))