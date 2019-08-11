from fileManager import fileManager
import json


def CreatemainFile():
    fileNameMain=input("Entry file Main:")
    FMMain = fileManager(fileNameMain)
    FMMain.javaClassGen()

def CreateInfrastructure():
    fileNameInf = input("Entry fileName Infrastructure:")
    FMInfrastructure = fileManager(fileNameInf)
    FMInfrastructure.javaClassGen()
    jsonFile = open('scratch.json')
    dataStore = json.load(jsonFile)
    FMInfrastructure.addInfrastructure(dataStore)

if __name__ == "__main__":
    CreateInfrastructure()