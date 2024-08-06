from app.utils.database import MongoDB
from app.config import main_mongodb

class MongoDBtest:
    def __init__(self):
        self.__mongo = MongoDB()
        self.__mongo.connectDB()
        print("___________________ Database connection test ___________________")
        
    def databaseTest(self):
        dblist = self.__mongo.get_client().list_database_names()

        if main_mongodb["DATABASE"] in dblist: return True
        else: return False
    
    def mainCollectionTest(self):
        collectionList = self.__mongo.get_database().list_collection_names()
        
        if main_mongodb["COLLECTION_MAIN"] in collectionList: return True
        else: return False
