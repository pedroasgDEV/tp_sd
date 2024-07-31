from ..models.main_db.connection import MongoDB
from ..models.main_db.collections.people import PeopleCollection

class CRUDtest:
    def __init__(self):
        #Start connection
        self.___mongo = MongoDB()
        self.___mongo.connectDB()
        self.___database = self.___mongo.get_database()
        self.___collection = PeopleCollection(self.___database)
        self.doc_UD_id = None
    
    def create(self, doc):
        doc_insert = self.___collection.insert_document(doc)

        if doc_insert.acknowledged: 
            self.doc_insert_id = doc_insert.inserted_id
            return True
        
        else: return False

    def readTest(self, qnt):
        docs_read = ___collection.select_many_random(qnt)

        if len(docs_read) == qnt: return True
        else: return False
        
    def updateTest(self, doc):
        doc_update = ___collection.edit_registry(self.doc_UD_id, doc)
        
        if doc_update.modified_count == 1: return True
        else: return False
        
    def deleteTest(self):
        doc_del = ___collection.delete_registry(self.doc_UD_id)

        if doc_del.deleted_count == 1:  return True
        else: return False


    
    
    

doc = {
    "name": "Pedro Augusto Sousa Gonçalves",
    "email": "pedro.asg@aluno.ufop.edu.br",
    "phone": "(38) 99810-7189",
    "address": {
    "number": 62,
    "street": "Pedro Alexandrino Rufino",
    "city": "Ouro Preto",
    "state": "Minas Gerais",
    "country": "Brazil",
    "description": "62, Pedro Alexandrino Rufino, Ouro Preto, Minas Gerais, Brazil",
    "postcode": 35400
    },
    "img": "https://randomuser.me/api/portraits/men/32.jpg",
    "description": "Name: Pedro Augusto Sousa Gonçalves\nCPF: 127.211.966-18\nEmail: pedro.asg@aluno.ufop.edu.br\nPhone: (38) 99810-7189\nAddress: 62, Pedro Alexandrino Rufino, Ouro Preto, Minas Gerais, Brazil",
    "cpf": {
    "cpf": "12721196618",
    "description": "127.211.966-18"
    }
}

doc_update = {
    "email": "email@falso.com"
}