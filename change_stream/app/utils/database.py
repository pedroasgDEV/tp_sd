from pymongo import MongoClient
from app.config import main_mongodb

class MongoDB:
    def __init__(self):
        self.__link = "mongodb+srv://{}:{}@{}.ckosrqe.mongodb.net/?retryWrites=true&w=majority&appName={}".format(
            main_mongodb["USERNAME"],
            main_mongodb["PASSWORD"],
            main_mongodb["PROJECT"],
            main_mongodb["APP"]
        )
        self.__client = None
        self.__database = None
        
        
    def connectDB(self):
        self.__client = MongoClient(self.__link)
        self.__database = self.get_client()[main_mongodb["DATABASE"]]
                
    def get_client(self):
        return self.__client
    
    def get_database(self):
        return self.__database
