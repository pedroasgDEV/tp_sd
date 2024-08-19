from pymongo import change_stream
from app.utils.database import MongoDB
from app.utils.changes_database import ChangesDB
from app.services.emails import SendEmail
from app.config import main_mongodb, recv_email, changes_mongodb
from json import dumps

class DB_Listener:
    def __init__(self):
        mongo = MongoDB()
        mongo.connectDB()
        self.__detabase = mongo.get_database()
        self.__collection = self.__detabase[main_mongodb["COLLECTION_MAIN"]]
        
        self.__changesDB = ChangesDB()
        self.__changesDB.connectDB()
        
        self.__email = SendEmail(recv_email["EMAIL"])
        
    def listener(self):
        try:
            with self.__collection.watch() as stream:
                for change in stream:
                    
                    if change["operationType"] == "insert":
                        self.__changesDB.create(changes_mongodb["COLLECTION_POST"], change)
                        print("\n\n__________________ Um doc foi criado __________________\n")
                        #self.__email.send(change, "POST")
                        
                    elif change["operationType"] == "update":
                        self.__changesDB.create(changes_mongodb["COLLECTION_PUT"], change)
                        print("\n\n__________________ Um doc foi atualizado __________________\n")
                        #self.__email.send(change, "PUT")
                        
                    elif change["operationType"] == "delete":
                        self.__changesDB.create(changes_mongodb["COLLECTION_DELETE"], change)
                        print("\n\n__________________ Um doc foi deletado __________________\n")
                        #self.__email.send(change, "DELETE")
                    
                    print(change)
                        
        except KeyboardInterrupt:
            print("Interrupted by user, shutting down...")
            
        finally:
            self.__email.close()
        
        
        