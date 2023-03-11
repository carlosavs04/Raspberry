import json, os

class JsonFile:
    def __init__(self, archivo):
        self.archivo = archivo

    def readDocument(self):
        data = []
        file_exists = os.path.isfile(self.archivo)
        
        if file_exists:
            nDocument = open(self.archivo, "r")
            data = json.loads(nDocument.read())
            return data

    def writeDocument(self, datos):
        nDocument = open(self.archivo, "w")
        data = json.dumps(datos, indent = 3)
        nDocument.write(data)
        return nDocument
    
    def clearFile(self, archivo):
        os.remove(archivo)

    def clearAllFiles(self):
        for i in os.listdir():
            if i.endswith(".json"):
                os.remove(i)