from pymongo import MongoClient
from bson.objectid import ObjectId
from app.config import mongodb_config
from app.utils.database import MongoDB

class ChangesDB:
    def __init__(self):
        super().__init__()
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
        self.__database = self.__client[mongodb_config["CHANGES_DATABASE"]]
        
    def get_client(self):
        return self.__client
    
    def get_database(self):
        return self.__database
    
    def create(self, collection, doc):
        collection = self.__database[collection]
        
        result = collection.insert_one(doc)
        
        return result
    
    def readOne(self, collection, id):
        collection = self.__database[collection]
        
        result = collection.find_one({"_id": ObjectId(id)})
        
        return result
        
    def clean(self):
        collections = self.__database.list_collection_names()
        
        for col_name in collections:
            col = self.__database[col_name]
            col.delete_many({})