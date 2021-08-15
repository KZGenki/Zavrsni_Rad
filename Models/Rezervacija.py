class Rezervacija:
    def __init__(self, id_rezervacije, id_korisnika, id_knjige, kolicina, datum):
        self.__id_rezervacije = id_rezervacije
        self.id_korisnika = id_korisnika
        self.id_knjige = id_knjige
        self.kolicina = kolicina
        self.datum = datum

    def __str__(self):
        return "rezervacija(" + str(self.__id_rezervacije) + ", " +  str(self.id_korisnika) + ", " + str(self.id_knjige) + ", " +  str(self.kolicina) + ", " + str(self.datum) + ")"