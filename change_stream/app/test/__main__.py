from app.test.dbConnection import MongoDBtest
from app.test.changesDbConnection import ChangesDBtest

dbTest = MongoDBtest()

if dbTest.databaseTest(): print("   . Main Database connection works :)")
else: print("   . Main Database connection isn't work :(")

if dbTest.mainCollectionTest(): print("   . Main collection connection works :)")
else: print("   . Main collectione connection isn't work :(")

changesDbTest = ChangesDBtest()

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

if changesDbTest.databaseTest(): print("   . Changes Database connection works :)")
else: print("   . Main Database connection isn't work :(")

if changesDbTest.collectionsTest(): print("   . Changes collections connection works :)")
else: print("   . Main collectione connection isn't work :(")

if changesDbTest.createTest(doc): print("   . CREATE operation works :)")
else: print("   . CREATE operation is't work :(")

if changesDbTest.readOneTest(): print("   . READ operation works :)")
else: print("   . READ operation is't work :(")

if changesDbTest.cleanTest(): print("   . CLEAN operation works :)")
else: print("   . CLEAN operation is't work :(")