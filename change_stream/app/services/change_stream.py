from pymongo import change_stream
from app.utils.database import MongoDB
import threading

class DB_Listener:
    def __init__():
        self.__database = MongoDB()
        self.__database.connectDB()
        self.__eventListeners = []
        
    def post_listener():
        return
    
    def put_listener():
        return
    
    def delete_listener():
        return
        
        
        
        