from app.models.cpf import Cpf
from app.models.address import Address

class Person:
    def __init__(self, name="NONAME", email="NOEMAIL", phone="NOCELL", 
                 number=-1, street="NOSTREET", city="NOCITY", state="NOSATATE",
                 country="NOCOUNTRY", postcode=-1, img="NOIMG", cpf="NOCPF"):
        try:
            self._name = name
            self._email = email
            self._phone = phone
            self._address = Address(number, street, city, state, country, postcode)
            self._img = img
            self._cpf = Cpf(cpf)
        except Exception as e:
            raise Exception(f"ERRO: object cannot be created\n{e}")
        self._description = self.__str__()

    def __str__(self):
        return f"Name: {self._name}\nCPF: {self._cpf}\nEmail: {self._email}\nPhone: {self._phone}\nAddress: {self._address.description}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("TYPE_ERRO: name is a string")
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("TYPE_ERRO: email is a string")
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("TYPE_ERRO: phone is a string")
        self._phone = phone

    @property
    def address(self):
        return self._address.description

    @address.setter
    def address(self, address):
        if not isinstance(address, Address):
            raise TypeError("TYPE_ERRO: address is an Address object")
        self._address = address

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        if not isinstance(img, str):
            raise TypeError("TYPE_ERRO: img is a string")
        self._img = img

    @property
    def cpf(self):
        return self._cpf.description

    @cpf.setter
    def cpf(self, cpf):
        if not isinstance(cpf, Cpf):
            raise TypeError("TYPE_ERRO: cpf is a Cpf object")
        self._cpf = cpf