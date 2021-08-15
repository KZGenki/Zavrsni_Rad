class Racun:
    def __init__(self, id_racuna, id_korisnika, id_liste, datum, cena):
        self.__id_racuna = id_racuna
        self.id_korisnika = id_korisnika
        self.id_liste = id_liste
        self.datum = datum
        self.cena = cena

    def __str__(self):
        return "racun(" + str(self.__id_racuna) + ", " + str(self.id_korisnika) + ", " + str(self.id_liste) + ", " + str(self.datum) + ", " + str(self.cena) + ")"