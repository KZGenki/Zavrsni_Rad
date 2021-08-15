class Lista:
    def __init__(self, id_liste, id_knjige, kolicina):
        self.id_liste = id_liste
        self.id_knjige = id_knjige
        self.kolicina = kolicina

    def __str__(self):
        return "lista(" + str(self.id_liste) + ", " + str(self.id_knjige) + ", " + str(self.kolicina) + ")"