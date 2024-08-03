from pymongo import MongoClient
from app.config import mongodb_config

class MongoDB:
    def __init__(self):
        self.__link = "mongodb+srv://{}:{}@{}.ckosrqe.mongodb.net/?retryWrites=true&w=majority&appName={}".format(
            mongodb_config["USERNAME"],
            mongodb_config["PASSWORD"],
            mongodb_config["PROJECT"],
            mongodb_config["APP"]
        )
        self.__client = None
        self.__database = None
        
    def connectDB(self):
        self.__client = MongoClient(self.__link)
        self.__database = self.__client[mongodb_config["DATABASE"]]
        
    def get_client(self):
        return self.__client
    
    def get_database(self):
        return self.__database

