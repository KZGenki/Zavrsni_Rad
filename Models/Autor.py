class Autor:
    def __init__(self, id_autora, ime, prezime):
        self.__id_autora = id_autora
        self.ime = ime
        self.prezime = prezime

    def __str__(self):
        return "autor(" + str(self.__id_autora) + ", " + self.ime + ", " + self.prezime + ")"