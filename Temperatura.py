import adafruit_dht
import time

class Temperatura:
    def __init__(self, pin):
        self.dhtDevice = adafruit_dht.DHT11(pin)

    def medirTemperatura(self):
        try:
            temperatura = self.dhtDevice.temperature
            humedad = self.dhtDevice.humidity
            array = [temperatura, humedad]
            return array
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            return None
        except Exception as error:
            self.dhtDevice.exit()
            raise error
        
if __name__ == "__main__":
    sensor = Temperatura(4)
    temperatura, humedad = sensor.medirTemperatura()
    print("Temperatura: {} C".format(temperatura))
    print("Humedad: {} %".format(humedad))
        
