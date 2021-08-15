class Korisnik:
    def __init__(self, id_korisnika, username, password, type):
        self.__id_korisnika = id_korisnika
        self.username = username
        self.password = password
        self.type = type

    def __str__(self):
        return "korinik(" + str(self.__id_korisnika) + ", " + str(self.username) + ", " + str(self.password) + ", " + str(self.type) + ")"