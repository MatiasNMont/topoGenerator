from fileManager import fileManager
import json

name = ""

def CreatemainFile(nameProduct):
    FMName = nameProduct+"Example"
    FMMain = fileManager(FMName,nameProduct)
    FMMain.javaClassGen()
    FMMain.addMainFile()
def CreateInfrastructure(nameProduct):
    fileNameInf = nameProduct+"Infrastructure"
    FMInfrastructure = fileManager(fileNameInf,nameProduct)
    FMInfrastructure.javaClassGen()
    jsonFile = open('scratch.json')
    dataStore = json.load(jsonFile)
    FMInfrastructure.addInfrastructure(dataStore)

if __name__ == "__main__":
    nameProduct = input("Entry file name (Recommended few characters):")
    CreateInfrastructure(nameProduct)
    CreatemainFile(nameProduct)