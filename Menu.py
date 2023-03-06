from Sensor import Sensor
from Led import Led

class Menu:
    def __init__(self):
        self.ultrasonico = Sensor("ult", [23, 24], "Sensor ultrasonico", "Sensor para medir distancia")
        self.temperatura = Sensor("tmp", [4], "Sensor DHT11", "Sensor para medir temperatura")
        self.humedad = Sensor("hum", [4], "Sensor DHT11", "Sensor para medir humedad")
        self.led = Led(17)

    def menu(self):
        opcion = '0'
        while opcion != '5':
            print("1. Medir distancia")
            print("2. Medir temperatura")
            print("3. Medir humedad")
            print("4. Encender led")
            print("5. Apagar led")
            print("6. Salir")

            opcion = input("Introduce una opción: ")
            if opcion == '1':
                self.medirDistancia()

            elif opcion == '2':
                self.medirTemperatura()

            elif opcion == '3':
                self.medirHumedad()

            elif opcion == '4':
                self.encenderLed()
            
            elif opcion == '5':
                self.apagarLed()

            elif opcion == '6':
                print("Saliendo...")
            
            else:
                print("Opción inválida.")

    def medirDistancia(self):
        distancia = self.ultrasonico.lectura()
        print("Distancia: {} cm".format(distancia))

    def medirTemperatura(self):
        temperatura = self.temperatura.lectura()
        print("Temperatura: {0:0.1f}* °C".format(temperatura))

    def medirHumedad(self):
        humedad = self.temperatura.lectura()
        print("Humedad: {1:0.1f} %".format(humedad))

    def encenderLed(self):
        self.led.encender()

    def apagarLed(self):
        self.led.apagar()

if __name__ == "__main__":
    menu = Menu()
    menu.menu()