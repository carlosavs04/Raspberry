from Ultrasonico import Ultrasonico
from Temperatura import Temperatura
from Led import Led

class Menu:
    def __init__(self):
        self.sensorUltrasonico = Ultrasonico(23, 24)
        self.sensorTemperatura = Temperatura(4)
        self.led = Led(17)

    def menu(self):
        opcion = '0'
        while opcion != '5':
            print("1. Medir distancia")
            print("2. Medir temperatura y humedad")
            print("3. Encender led")
            print("4. Apagar led")
            print("5. Salir")

            opcion = input("Introduce una opción: ")
            if opcion == '1':
                self.medirDistancia()

            elif opcion == '2':
                self.medirTemperatura()

            elif opcion == '3':
                self.encenderLed()
            
            elif opcion == '4':
                self.apagarLed()

            elif opcion == '5':
                print("Saliendo...")
            
            else:
                print("Opción inválida.")

    def medirDistancia(self):
        distancia = self.sensorUltrasonico.medirDistancia()
        print("Distancia: {} cm".format(distancia))

    def medirTemperatura(self):
        temperatura, humedad = self.sensorTemperatura.medirTemperatura()
        print("Temperatura: {0:0.1f}* °C".format(temperatura))
        print("Humedad: {1:0.1f} %".format(humedad))

    def encenderLed(self):
        self.led.encender()
    
    def apagarLed(self):
        self.led.apagar()

if __name__ == "__main__":
    menu = Menu()
    menu.menu()