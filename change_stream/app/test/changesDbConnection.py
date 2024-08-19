from app.utils.changes_database import ChangesDB
from app.config import changes_mongodb

class ChangesDBtest:
    def __init__(self):
        self.__mongo = ChangesDB()
        self.__mongo.connectDB()
        self.__doc_UD_id = []
        print("___________________ Changes Database connection test ___________________")
        
    def databaseTest(self):
        dblist = self.__mongo.get_client().list_database_names()

        if changes_mongodb["DATABASE"] in dblist: return True
        else: return False
    
    def collectionsTest(self):
        collectionList = self.__mongo.get_database().list_collection_names()
        
        if changes_mongodb["COLLECTION_POST"] not in collectionList: return False
        elif changes_mongodb["COLLECTION_PUT"] not in collectionList: return False
        elif changes_mongodb["COLLECTION_DELETE"] not in collectionList: return False
        else: return True
    
    def createTest(self, doc):
        collectionList = self.__mongo.get_database().list_collection_names()
        
        for col in collectionList:
            
            doc_insert = self.__mongo.create(col, doc)
            
            if not doc_insert.acknowledged: 
                return False
            
            self.__doc_UD_id.append(str(doc_insert.inserted_id))
        
        return True

    def readOneTest(self):
        collectionList = self.__mongo.get_database().list_collection_names()
        
        i = 0
        for col in collectionList:
            
            result = self.__mongo.readOne(col, self.__doc_UD_id[i])
            
            if str(result["_id"]) != self.__doc_UD_id[i]: 
                return False

            i += 1
            
        return True
        
    def cleanTest(self):
        collectionList = self.__mongo.get_database().list_collection_names()

        self.__mongo.clean()
        
        for col_name in collectionList:
            col = self.__mongo.get_database().get_collection(col_name)
            if col.count_documents({}) > 0: return False
            
        return True