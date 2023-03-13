import json, os

class JsonFile:
    def __init__(self, archivo):
        self.archivo = archivo

    def readDocument(self):
        try:
            with open(self.archivo, 'r') as archivo_json:
                datos = json.load(archivo_json)
            return datos
        except FileNotFoundError:
            with open(self.archivo, 'w') as archivo_json:
                json.dump([], archivo_json)
            return []

    def writeDocument(self, datos):
        with open(self.archivo, 'w') as archivo_json:
            json.dump(datos, archivo_json)
    
    def clearFile(self, archivo):
        os.remove(archivo)

    def clearAllFiles(self):
        for i in os.listdir():
            if i.endswith(".json"):
                os.remove(i)