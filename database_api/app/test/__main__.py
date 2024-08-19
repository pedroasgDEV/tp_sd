from app.test.dbConnection import DBconnectionTest
from app.test.dbCRUD import CRUDtest

dbTest = DBconnectionTest()

if dbTest.databaseTest(): print("   . Database connection works :)")
else: print("   . Database connection isn't work :(")

if dbTest.mainCollectionTest(): print("   . Main collection connection works :)")
else: print("   . Main collectione connection isn't work :(")

crudTest = CRUDtest()

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


if crudTest.createTest(doc): print("   . CREATE operation works :)")
else: print("   . CREATE operation is't work :(")

if crudTest.readTest(100): print("   . READ operation works :)")
else: print("   . READ operation is't work :(")

if crudTest.readOneTest(): print("   . READ_ONE operation works :)")
else: print("   . READ_ONE operation is't work :(")

if crudTest.updateTest(doc_update): print("   . UPDATE operation works :)")
else: print("   . UPDATE operation is't work :(")

if crudTest.deleteTest(): print("   . DELETE operation works :)")
else: print("   . DELETE operation is't work :(")