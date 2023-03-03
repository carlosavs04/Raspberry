from Ultrasonico import Ultrasonico
from Temperatura import Temperatura
from Led import Led
import time
import json
import datetime

class Sensor:
    def __init__(self, key = "", pines = [], nombre = "", descripcion = ""):
        self.key = key
        self.pines = pines
        self.nombre = nombre
        self.descripcion = descripcion

    def choseSensor(self):
        self.sensor = ""
        lectura = []

        if self.key == "ult":
            self.sensor = Ultrasonico(self.pines[0], self.pines[1])
            distancia = self.sensor.medirDistancia()
            lectura.append(distancia)

        elif self.key == "tmp":
            self.sensor = Temperatura(self.pines[0])
            temperatura, humedad = self.sensor.medirTemperatura()
            lectura.append(temperatura, humedad)

        elif self.key == "led1":
            self.sensor = Led(self.pines[0])
            self.sensor.encender()

        elif self.key == "led2":
            self.sensor = Led(self.pines[0])
            self.sensor.apagar()

        else: 
            print("Sensor no encontrado")
            return None
        
        return lectura

    def lectura(self):
        valores = self.choseSensor()
        tiempo = time.time()
        fecha = datetime.datetime.fromtimestamp(tiempo).strftime('%H:%M:%S')

        data = {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "valores": valores,
            "fecha": fecha
        }

        dataJson = json.dumps(data)
        return dataJson




