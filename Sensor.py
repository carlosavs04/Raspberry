from Ultrasonico import Ultrasonico
from Temperatura import Temperatura
import time
import json
import datetime
from bson import ObjectId
from Lectura import Lectura

class Sensor:
    def __init__(self, key = "", pines = [], nombre = "", descripcion = "", tipoDato = []):
        self._id = ObjectId()
        self.key = key
        self.pines = pines
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipoDato = tipoDato

    def sensores(self):
        lectura = []

        if self.key == "ult":
            ultrasonicoSensor = Ultrasonico(self.pines[0], self.pines[1])
            distancia = ultrasonicoSensor.medirDistancia()
            lectura.append(distancia)
            self.tipoDato = ["cm"]

        elif self.key == "tmp":
            dhtSensor = Temperatura(self.pines[0])
            temperatura, humedad = dhtSensor.medirTemperatura()
            lectura.append(temperatura)
            lectura.append(humedad)
            self.tipoDato = ["°C", "%"]

        else: 
            print("Sensor no encontrado")
            return None
        
        return lectura

    def lectura(self):
        valores = []
        valores = self.sensores()
        tiempo = time.time()
        fecha = datetime.datetime.fromtimestamp(tiempo).strftime('%Y-%m-%d %H:%M:%S')
        data = []

        try:
            self._id.is_valid()

        except:
            pass

        else:
            self._id = ObjectId()

        if self.key == "tmp":
            data1 = Lectura(self._id, self.nombre, self.descripcion, self.tipoDato[0], valores[0], fecha)
            data2 = Lectura(self._id, self.nombre, self.descripcion, self.tipoDato[1], valores[1], fecha)
            data.append(data1.getDict())
            data.append(data2.getDict())

        else:
            data1 = Lectura(self._id, self.nombre, self.descripcion, self.tipoDato[0], valores[0], fecha)
            data.append(data1.getDict())
            
        dataJson = json.dumps(data)
        return dataJson



