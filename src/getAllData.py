from getData import getData
import os
import sys

def getAllData(dataFileNames, teamsFileName):
  results = {}
  for dataFileName in dataFileNames:
    getData(dataFileName, teamsFileName, results)
  return results

if __name__ == "__main__":
  print(getAllData(sys.argv[1], sys.argv[2]))