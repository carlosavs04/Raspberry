from Sensor import Sensor
from Led import Led
from Lectura import Lectura
import threading, json, keyboard, time
from MongoDB import MongoDB

class Menu:
    def __init__(self):
        self.lectura = Lectura()
        self.bandera = False
        self.bandera2 = 0
        self.ultrasonico = Sensor("ult", [23, 24], "Sensor ultrasonico", "Sensor para medir distancia")
        self.temperatura = Sensor("tmp", [4], "Sensor DHT11", "Sensor para medir temperatura y humedad")
        self.led = Led(17)
        self.objeto_mongo = MongoDB()
        self.wait = 120
        self.timer_count = 0
        self.repeat = 2
        self.enter_pressed = False
        self.collection = "Sensores"

    def contador(self, tiempo):
        for i in range(tiempo, -1, -1):
            time.sleep(1)
        return True

    def menu(self):
        if self.repeat == 2:
            conexion = self.objeto_mongo.createConnection()
            if conexion == True:
                self.bandera2 = 1
                self.repeat = 1

            else:
                self.bandera2 = 2
                self.repeat = 1

        opcion = '0'
        while opcion != '6':
            print("1. Medir distancia")
            print("2. Medir temperatura y humedad")
            print("3. Medir todos los sensores")
            print("4. Encender led")
            print("5. Apagar led")
            print("6. Salir")

            opcion = input("Introduce una opción: ")
            if opcion == '1':
                self.medirDistancia()

            elif opcion == '2':
                self.medirTemperatura()

            elif opcion == '3':
                self.medirTodos()    

            elif opcion == '4':
                self.encenderLed()
            
            elif opcion == '5':
                self.apagarLed()

            elif opcion == '6':
                print("Saliendo...")
            
            else:
                print("Opción inválida.")

    def medirDistancia(self):
        if self.bandera2 == 1:
            listaSensores = self.lectura.mostrar()
            if len(listaSensores) >= 1:
                for i in listaSensores:
                    if self.objeto_mongo.find_one(self.collection, i) == None:
                        self.objeto_mongo.insert_one(self.collection, i)
                    else:
                        pass

                self.lectura.clearFile("Sensores.json")
            self.borrarHilo()

        enter_thread = threading.Thread(target=self.enter)
        enter_thread.start()
        while True:
            data = self.ultrasonico.lectura()
            distancia = json.loads(data)
            if len(distancia) >= 1:
                for i in distancia:
                    print(i)
                    self.lectura.agregar(i)
                    if self.bandera2 == 1:
                        self.guardarArchivo(i)

            if self.enter_pressed:
                break
        
    def medirTemperatura(self):
        if self.bandera2 == 1:
            listaSensores = self.lectura.mostrar()
            if len(listaSensores) >= 1:
                for i in listaSensores:
                    if self.objeto_mongo.find_one(self.collection, i) == None:
                        self.objeto_mongo.insert_one(self.collection, i)
                    else:
                        pass

                self.lectura.clearFile("Sensores.json")
            self.borrarHilo()

        enter_thread = threading.Thread(target=self.enter)
        enter_thread.start()
        while True:
            data = self.temperatura.lectura()
            temperatura = json.loads(data)
            if len(temperatura) >= 1:
                for i in temperatura:
                    print(i)
                    self.lectura.agregar(i)
                    if self.bandera2 == 1:
                        self.guardarArchivo(i)

            if self.enter_pressed:
                break

    def medirTodos(self):
        sensores = [self.ultrasonico, self.temperatura]
        
        if self.bandera2 == 1:
            listaSensores = self.lectura.mostrar()
            if len(listaSensores) >= 1:
                for i in listaSensores:
                    if self.objeto_mongo.find_one(self.collection, i) == None:
                        self.objeto_mongo.insert_one(self.collection, i)
                    else:
                        pass

                self.lectura.clearFile("Sensores.json")
            self.borrarHilo()

        enter_thread = threading.Thread(target=self.enter)
        enter_thread.start()
        while True:
            for i in sensores:
                data = json.loads(i.lectura())
                if len(data) >= 1:
                    for j in data:
                        print(j)
                        self.lectura.agregar(j)
                        if self.bandera2 == 1:
                            self.guardarArchivo(j)

            if self.enter_pressed:
                break

    def encenderLed(self):
        self.led.encender()

    def apagarLed(self):
        self.led.apagar()

    def enter(self):
        self.enter_pressed = False
        keyboard.wait('enter')
        self.enter_pressed = True

    def guardarArchivo(self, datos):
        if self.objeto_mongo.insert_one(self.collection, datos) == False:
            self.bandera2 = 2
            print("La conexión con la base de datos no se pudo establecer. Guardando en archivo...")
            ultimoSensor = datos
            self.lectura.clearFile("Sensores.json")
            self.lectura.agregar(ultimoSensor)

    def borrarHilo(self):
        timer = threading.Timer(self.wait, self.borrarHilo)
        timer.start()

        if self.bandera2 == 1:
            self.timer_count += 1
            if self.timer_count >= self.wait / 60:
                self.lectura.clearFile("Sensores.json")
                self.timer_count = 0

        else:
            self.timer_count = 0
        
if __name__ == "__main__":
    menu = Menu()
    menu.menu()