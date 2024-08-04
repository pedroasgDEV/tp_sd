from pymongo import change_stream
from app.utils.database import MongoDB
from app.utils.changes_database import ChangesDB
from app.services.emails import SendEmail
from app.config import main_mongodb, recv_email, changes_mongodb
import time

class DB_Listener:
    def __init__(self):
        mongo = MongoDB()
        mongo.connectDB()
        self.__detabase = mongo.get_database()
        self.__collection = self.__detabase[main_mongodb["COLLECTION_MAIN"]]
        
        self.__changesDB = ChangesDB()
        self.__changesDB.connectDB()
        
        self.__email = SendEmail(recv_email["EMAIL"])
        
    def post_listener(self):
        pipeline = [{'$match': {'operationType': 'insert'}}]
        
        with self.__collection.watch(pipeline) as stream:
            for change in stream:
                self.__changesDB.create(changes_mongodb["COLLECTION_POST"], change)
                self.__email.send(change, "POST")
                
    def put_listener(self):
        pipeline = [{'$match': {'operationType': 'update'}}]
        
        with self.__collection.watch(pipeline) as stream:
            for change in stream:
                self.__changesDB.create(changes_mongodb["COLLECTION_PUT"], change)
                self.__email.send(change, "PUT")
    
    def delete_listener(self):
        pipeline = [{'$match': {'operationType': 'delete'}}]
        
        with self.__collection.watch(pipeline) as stream:
            for change in stream:
                self.__changesDB.create(changes_mongodb["COLLECTION_DELETE"], change)
                self.__email.send(change, "DELETE")
                
    def cleanAllChanges(self):
        return self.__changesDB.clean()


test = DB_Listener()    
while True:
    test.post_listener()
    time.sleep(5)
        
        
        