from bson.objectid import ObjectId
from datetime import timedelta
from app.config import mongodb_config

class PeopleCollection:
    def __init__(self, database):
        self.__collection_name = mongodb_config["COLLECTION_MAIN"]
        self.__database = database

    #CREATE
    def insert_document(self, doc):
        collection = self.__database.get_collection(self.__collection_name)
        
        #Insert doc
        data = collection.insert_one(doc)
        
        return data

    #READ
    def select_many_random(self, qnt):
        if qnt == 0: return []
        
        collection = self.__database.get_collection(self.__collection_name)

        #Define pipeline
        pipeline = [
            {"$sample": {"size": qnt}}
        ]

        # Execute the agregation
        result = collection.aggregate(pipeline)
        result = list(result)
        
        #ObjectID precisa ser uma string
        for person in result:
            person["_id"] = str(person["_id"])
            
        return result

    #UPDATE
    def edit_registry(self, id, doc):
        collection = self.__database.get_collection(self.__collection_name)
        
        #Update data
        data = collection.update_one(
            { "_id": ObjectId(id) }, #Filtro
            { "$set": doc } # Campo de edição
        )
        
        return data
    
    #DELETE
    def delete_registry(self, id):
        collection = self.__database.get_collection(self.__collection_name)
        
        #delete data
        data = collection.delete_one({ "_id": ObjectId(id) })
        
        return data;