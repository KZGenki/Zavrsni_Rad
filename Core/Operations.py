import sqlite3


class User:
    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

    def __str__(self):
        return self.username


def login(username="Guest", password="Guest"):
    conn = sqlite3.connect("knjizara.db")
    cursor = conn.execute("select * from korisnici where korisnik=? and password =?", (username, password))
    data = []
    for col in cursor:
        data.append(col)
    if len(data) == 1:
        if len(data[0]) == 3:
            if data[0][0] == username and data[0][1] == password:
                return User(username, password, data[0][2])
    conn.close()
    return -1


def new_user(username, password):
    conn = sqlite3.connect("knjizara.db")
    cursor = conn.execute("select korisnik from korisnici where korisnik=?", (username,))
    data = []
    for col in cursor:
        data.append(col)
    if len(data) != 0:
        conn.close()
        return -1
    cursor.execute("insert into korisnici (korisnik, password, type) values(?, ?, 0)", (username, password))
    conn.commit()
    cursor.execute("select * from korisnici where korisnik=? and password =?", (username, password))
    data = []
    for col in cursor:
        data.append(col)
    if len(data) == 1:
        if len(data[0]) == 3:
            if data[0][0] == username and data[0][1] == password:
                return User(username, password, data[0][2])
    conn.commit()
    conn.close()
    return -1
    pass


def get_list(user, search_term):
    pass


# make_reservations
def add_to_cart(user):
    pass


def list_cart(user):
    pass


def buy(user):
    pass

