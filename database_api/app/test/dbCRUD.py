from app.utils.database.connection import MongoDB
from app.utils.database.collections.people import PeopleCollection

class CRUDtest:
    def __init__(self):
        #Start connection
        self.___mongo = MongoDB()
        self.___mongo.connectDB()
        self.___database = self.___mongo.get_database()
        self.___collection = PeopleCollection(self.___database)
        self.doc_UD_id = None
        print("___________________ Database CRUD test ___________________")
    
    def createTest(self, doc):
        doc_insert = self.___collection.insert_document(doc)

        if doc_insert.acknowledged: 
            self.doc_UD_id = doc_insert.inserted_id
            return True
        
        else: return False

    def readTest(self, qnt):
        docs_read = self.___collection.select_many_random(qnt)

        if len(docs_read) == qnt: return True
        else: return False
        
    def updateTest(self, doc):
        doc_update = self.___collection.edit_registry(self.doc_UD_id, doc)
        
        if doc_update.modified_count == 1: return True
        else: return False
        
    def deleteTest(self):
        doc_del = self.___collection.delete_registry(self.doc_UD_id)

        if doc_del.deleted_count == 1:  return True
        else: return False