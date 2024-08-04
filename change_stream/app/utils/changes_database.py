from pymongo import MongoClient
from app.config import mongodb_config
from app.utils.database import MongoDB

class ChangesDB(MongoDB):
    def __init__(self):
        super().__init__(self)
        
    def connectDB(self):
        self.__client = MongoClient(self.__link)
        self.__database = self.__client[mongodb_config["CHANGES_DATABASE"]]
        
    def create(self, collection, doc):
        collection = self.__database[collection]
        
        data = collection.insert_one(doc)
        
        return data.inserted_id
    
    def clean(self):
        collections = self.__database.list_collection_names()
        
        for col_name in collections:
            col = self.__database[col_name]
            col.delete_many({})