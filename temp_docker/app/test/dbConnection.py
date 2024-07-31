from ..models.main_db.connection import MongoDB

class DBconnectionTest:
    def __init__(self):
        self.mongo = MongoDB()
        self.mongo.connectDB()
        
    def databaseTest(self):
        dblist = test.get_client().list_database_names()
        
        if "tp_sd1" in dblist: True
        else: False
    
    def collection(self):
        collectionList = test.get_database().list_collection_names()

        if "people" in collectionList: return True
        else: False
