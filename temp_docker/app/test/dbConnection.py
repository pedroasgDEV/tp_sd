from ..models.connection import MongoDB

class DBconnectionTest:
    def __init__(self):
        self.mongo = MongoDB()
        self.mongo.connectDB()
        print("___________________ Database connection test ___________________")
        
    def databaseTest(self):
        dblist = self.mongo.get_client().list_database_names()

        if "tp_sd1" in dblist: return True
        else: return False
    
    def mainCollectionTest(self):
        collectionList = self.mongo.get_database().list_collection_names()
        
        if "people" in collectionList: return True
        else: return False
