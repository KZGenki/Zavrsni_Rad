import sqlite3
import Core


user_types = ["Gost", "Korisnik", "Operator", "Administrator"]


class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.type = user_type

    def __str__(self):
        return self.username


class Search:
    def __init__(self, query, year, use_year, use_author, use_title):
        self.query = query
        self.year = year
        self.use_year = use_year
        self.use_author = use_author
        self.use_title = use_title

    def __str__(self):
        return self.query


def clear_master(master):
    slaves = master.grid_slaves()
    for slave in slaves:
        slave.destroy()


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
    cursor.execute("insert into korisnici (korisnik, password, type) values(?, ?, 1)", (username, password))
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


def exec_query(query, params=None):
    conn = sqlite3.connect("knjizara.db")
    if params is None:
        cursor = conn.execute(query)
    else:
        cursor = conn.execute(query, params)
    data = []
    headers = []
    try:
        for header in cursor.description:
            headers.append(header[0])
    except:
        pass
    else:
        data.append(headers)
        for row in cursor:
            cols = []
            for col in row:
                cols.append(col)
            data.append(row)
    finally:
        conn.commit()
        conn.close()
        return data


# update sql after database data filling
def get_list(user, search_object: Search):
    query = "SELECT * FROM company"
    if search_object.use_author + search_object.use_year + search_object.use_title >= 1:
        query += " WHERE "
        query += "(" if search_object.use_year == 1 and search_object.use_title + search_object.use_author >= 1 else ""
        query += "name LIKE ?" if search_object.use_author == 1 else ""
        query += " OR " if search_object.use_author+search_object.use_title == 2 else ""
        query += "address LIKE ?" if search_object.use_title == 1 else ""
        query += ") AND " if search_object.use_year == 1 and search_object.use_title + search_object.use_author >= 1 else ""
        query += "age=?" if search_object.use_year == 1 else ""

    params = []
    for i in range(search_object.use_title + search_object.use_author):
        params.append("%"+search_object.query+"%")
    if search_object.use_year == 1:
        params.append(search_object.year)

    # print(query, tuple(params))
    return exec_query(query, params)
    pass


# make_reservations
def add_to_cart(user):
    pass


def list_cart(user):
    pass


def buy(user):
    pass


def get_users():
    data = exec_query("SELECT * FROM korisnici ORDER BY type DESC")
    users = []
    for i in range(len(data)-1):
        users.append(User(data[i+1][0], data[i+1][1], data[i+1][2]))
    return users
