from JsonFile import JsonFile

class Lista:
    def __init__(self, archivo):
        self.json = JsonFile(archivo)
        self.lista = self.json.readDocument()

    def agregar(self, datos):
        self.lista.append(datos)
        self.json.writeDocument(self.lista)

    def actualizar(self, cli, datos):
        if self.lista:
            self.lista[int(cli)] = datos
            self.json.writeDocument(self.lista)

    def mostrar(self):
        return self.lista
    
    def eliminar(self, cli):
        if self.lista:
            self.lista.pop(int(cli))
            self.json.writeDocument(self.lista)

    def buscar(self, cli):
        if self.lista:
            return self.lista[int(cli)]

    def clearFile(self, archivo):
        self.lista.clear()
        self.json.writeDocument([])
    
        