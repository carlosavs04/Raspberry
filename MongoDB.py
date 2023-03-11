import pymongo
from pymongo.server_api import ServerApi

class MongoDB:
    def __init__(self):
        self.client = ""
        self.database = ""
        
    def createConnection(self):
        try:
            self.client = pymongo.MongoClient("mongodb+srv://root:admin@cluster0.jrax7sh.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
            self.database = self.client["Raspberry"]
            print("Conexión exitosa.")
            return True
        
        except Exception as e:
            print("Error al conectar a la base de datos: ", e)
            return False

    def insert_one(self, collection, data):
        self.database[collection].insert_one(data)

    def insert_many(self, collection, data):
        self.database[collection].insert_many(data)
    
    def find_one(self, collection, data):
        return self.database[collection].find_one(data)
    
    def find(self, collection, data):
        return self.database[collection].find(data)
    
    def update_one(self, collection, data, new_data):
        self.database[collection].update_one(data, new_data)

    def delete_one(self, collection, data):
        self.database[collection].delete_one(data)

    def delete_many(self, collection, data):
        self.database[collection].delete_many(data)
   