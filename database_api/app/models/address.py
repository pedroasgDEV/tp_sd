class Address:
    def __init__(self, number=-1, street="NOSTREET", city="NOCITY", state="NOSATATE", country="NOCOUNTRY", postcode=-1):
        try:
            self._number = number
            self._street = street
            self._city = city
            self._state = state
            self._country = country
            self._postcode = postcode
        except Exception as e:
            raise Exception(f"ERRO: object cannot be created\n{e}")

        self._description = self.__str__()

    def __str__(self):
        return f"{self._number}, {self._street}, {self._city}, {self._state}, {self._country}"

    @property
    def description(self):
        return self._description

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError("TYPE_ERRO: number is a number")
        self._number = number

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street):
        if not isinstance(street, str):
            raise TypeError("TYPE_ERRO: street is a string")
        self._street = street

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise TypeError("TYPE_ERRO: city is a string")
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if not isinstance(state, str):
            raise TypeError("TYPE_ERRO: state is a string")
        self._state = state

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if not isinstance(country, str):
            raise TypeError("TYPE_ERRO: country is a string")
        self._country = country

    @property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        if not isinstance(postcode, int):
            raise TypeError("TYPE_ERRO: postcode is a number")
        self._postcode = postcode
