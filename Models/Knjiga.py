class Knjiga:
    def __init__(self, id_knjige, naslov, id_autora, godina=2000, indeks=123, cena=100, kolicina=1, deleted=False):
        self.__id_knjige = id_knjige
        self.naslov = naslov
        self.godina = godina
        self.indeks = indeks
        self.id_autora = id_autora
        self.cena = cena
        self.kolicina = kolicina
        self.deleted = deleted

    def __str__(self) -> str:
        return "knjiga(" + str(self.__id_knjige) + ", " + self.naslov + ", " + str(self.indeks) + ", " + str(self.id_autora) + ", " + str(self.cena) + ", "  + str(self.kolicina) + ", " + str(self.deleted) + ")"