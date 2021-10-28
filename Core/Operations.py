import sqlite3

import Core


class User:
    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

    def __str__(self):
        return self.username


def login(username="Guest", password="Guest"):
    conn = sqlite3.connect("knjizara.db")
    cursor = conn.execute("select * from korisnici where korisnik=?", (username,))
    data = []
    for col in cursor:
        data.append(col)
    conn.close()
    if len(data) != 1:
        raise Core.LoginError("Korisnik ne postoji, proveri korisnicko ime")
    if len(data[0]) == 3:
        if data[0][0] == username and data[0][1] == password:
            return User(username, password, data[0][2])
    raise Core.LoginError("Lozinka se ne poklapa, proveri lozinku")


def new_user(username, password):
    conn = sqlite3.connect("knjizara.db")
    cursor = conn.execute("select korisnik from korisnici where korisnik=?", (username,))
    data = []
    for col in cursor:
        data.append(col)
    if len(data) != 0:
        conn.close()
        raise Core.LoginError("Korisnicko ime je zauzeto, unesite drugo ime")
    cursor.execute("insert into korisnici (korisnik, password, type) values(?, ?, 0)", (username, password))
    conn.commit()
    cursor.execute("select * from korisnici where korisnik=? and password =?", (username, password))
    data = []
    for col in cursor:
        data.append(col)
    conn.commit()
    conn.close()
    if len(data) != 1:
        raise Core.LoginError("Greska u bazi, nalog nije napravljen")
    if len(data[0]) == 3:
        if data[0][0] == username and data[0][1] == password:
            return User(username, password, data[0][2])
    raise Core.LoginError("Greska u bazi, nalog je neispravan")


def get_list(user, search_term):
    pass


# make_reservations
def add_to_cart(user):
    pass


def list_cart(user):
    pass


def buy(user):
    pass

