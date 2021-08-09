class Knjiga:
    def __init__(self, naslov, indeks, autor):
        self.naslov = naslov
        self.indeks = indeks
        self.autor = autor

    def __str__(self) -> str:
        return self.naslov + " " + self.autor + " ID:" + str(self.indeks)