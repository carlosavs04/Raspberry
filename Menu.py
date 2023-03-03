from Sensor import Sensor

class Menu:
    def __init__(self):
        self.ultrasonico = Sensor("ult", [23, 24], "Sensor ultrasonico", "Sensor para medir distancia")
        self.temperatura = Sensor("tmp", [4], "Sensor DHT11", "Sensor para medir temperatura y humedad")
        self.led1 = Sensor("led1", [17], "Led", "Led apagado")
        self.led2 = Sensor("led2", [27], "Led", "Led encendido")

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
                while True:
                    self.medirDistancia()

            elif opcion == '2':
                while True:
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
        distancia = self.ultrasonico
        print("Distancia: {} cm".format(distancia))

    def medirTemperatura(self):
        temperatura, humedad = self.temperatura
        print("Temperatura: {0:0.1f}* °C".format(temperatura))
        print("Humedad: {1:0.1f} %".format(humedad))

    def encenderLed(self):
        self.led1
    
    def apagarLed(self):
        self.led2

if __name__ == "__main__":
    menu = Menu()
    menu.menu()