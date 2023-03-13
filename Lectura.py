from Lista import Lista
from bson import ObjectId

class Lectura(Lista):
    def __init__(self, nombre = "", descripcion = "", valores = "", tipoDato = "", fecha = ""):
        super().__init__("Sensores.json")
        self._id = ObjectId()
        self.nombre = nombre
        self.descripcion = descripcion
        self.valores = valores
        self.tipoDato = tipoDato
        self.fecha = fecha

    def __str__(self):
        return f"Nombre: {self.nombre}, Descripción: {self.descripcion}, Valores: {self.valores}, Tipo de dato: {self.tipoDato}, Fecha: {self.fecha}"
    
    def getDict(self):
        diccionario = []
        if type(self) == list:
            for i in self:
                if type(i) == dict:
                    diccionario.append(i)
                else:
                    diccionario.append(i.getDict())

            return diccionario
    
        elif type(self) == dict:
            diccionario.append(self.lista)

        else:
            dictionary = { "_id": str(self._id), "nombre": self.nombre, "descripcion": self.descripcion, "valores": self.valores, "tipoDato": self.tipoDato, "fecha": self.fecha }
            diccionario.append(dictionary)
            return diccionario
        
    def getObject(self):
        sensor_json = self.json.readDocument()
        sensor_obj = []
        
        for i in sensor_json:
            cli = Lectura(i["_id"], i["nombre"], i["descripcion"], i["valores"], i["tipoDato"], i["fecha"])
            sensor_obj.append(cli)
        
        return sensor_obj