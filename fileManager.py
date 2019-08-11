
class fileManager():

    def __init__(self,fileName):
        self.className = fileName
        self.fileName = fileName+".java"
        self.javaFile = None

    def javaClassGen(self):
        self.javaFile = open(self.fileName, "w+")

    def addInfrastructure(self,dataJSON):

        print("Writing Infraestructure")
        self.javaFile=open(self.fileName,'a')
        self.javaFile.write("import package;\nimport fogtorch.infrastructure.Infrastructure;\nimport fogtorch.utils.Hardware;\nimport static java.util.Arrays.asList;\n public class  " + self.className + "{ \n")
        self.javaFile.write("\t public static Infrastructure createInfrastructure() { \n \t \t Infrastructure I = new Infrastructure();\n")
        for x in dataJSON['members']:
            if x['type'] =="CloudCentre":
                self.javaFile.write("\t\t\t I.addCloudDatacentre(\""+x['name']+"\",asList(")
                for i in range(0, len(x['software'])):
                    if i == len(x['software'])-1:
                        self.javaFile.write("\"" + x['software'][i] + "\" ),")
                    else:
                        self.javaFile.write("\""+x['software'][i]+"\",")
                self.javaFile.write(str(x['x'])+",")
                self.javaFile.write(str(x['y'])+");\n")
            elif x['type'] == "fogNode":
                self.javaFile.write("\t\t\t I.addFogNode(\"" + x['name'] + "\",asList(")
                for i in range(0, len(x['software'])):
                    if i == len(x['software'])-1:
                        self.javaFile.write("\"" + x['software'][i] + "\" ),")
                    else:
                        self.javaFile.write("\""+x['software'][i]+"\",")
                self.javaFile.write("new Hardware(")
                self.javaFile.write(str(x['hardware']['cores'])+","+str(x['hardware']['ram'])+","+str(x['hardware']['storage'])+"),")
                self.javaFile.write(str(x['x'])+",")
                self.javaFile.write(str(x['y'])+");\n")
            elif x['type'] == "link":
                self.javaFile.write("\t\t\t I.addLink(\"" + x['source'] + "\",\""+x['target']+"\","+str(x['latency'])+","+str(x['bandwidth'])+");\n" )
            elif x['type'] == "things":
                self.javaFile.write("\t\t\t I.addThing(\"" + x['name'] + "\",\""+x['typeDevice']+"\","+str(x['x'])+","+str(x['y'])+");\n")



        self.javaFile.write("\n\n\n\t\treturn I;\n \t\t} \n \t }")
        self.javaFile.close()


