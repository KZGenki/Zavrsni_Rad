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


class Author:
    def __init__(self, id_author, name=None, surname=None):
        self.id_author = id_author
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname


class Publisher:
    def __init__(self, id_publisher, name=None):
        self.id_publisher = id_publisher
        self.name = name

    def __str__(self):
        return self.name


class Book:
    def __init__(self, id_book, title=None, author=None, year=None, index=None, price=None, quantity=None,
                 publisher=None, hidden=None):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.year = year
        self.index = index
        self.price = price
        self.quantity = quantity
        self.publisher = publisher
        self.hidden = hidden

    def __str__(self):
        return self.title

    def equal(self, book):
        if self.id_book == book.id_book and self.title == book.title and self.author == book.author and \
                self.year == book.year and self.index == book.index and self.price == book.price and \
                self.quantity == book.quantity and self.publisher == book.publisher and self.hidden == book.hidden:
            return True
        return False


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
    query = "SELECT naslov AS 'Naslov', godina_izdanja AS 'Godina izdanja', (ime || ' ' || prezime) AS 'Autor', naziv" \
            " AS 'Izdavac' FROM knjige " \
            "INNER JOIN autori ON knjige.id_autora = autori.id_autora " \
            "INNER JOIN izdavaci ON knjige.id_izdavaca = izdavaci.id_izdavaca WHERE deleted = 0"
    if search_object.use_author + search_object.use_year + search_object.use_title >= 1:
        query += " WHERE "
        query += "(" if search_object.use_year == 1 and search_object.use_title + search_object.use_author >= 1 else ""
        query += "(ime || ' ' || prezime) LIKE ?" if search_object.use_author == 1 else ""
        query += " OR " if search_object.use_author+search_object.use_title == 2 else ""
        query += "naslov LIKE ?" if search_object.use_title == 1 else ""
        query += ") AND " if search_object.use_year == 1 and search_object.use_title + search_object.use_author >= 1 \
            else ""
        query += "godina_izdanja=?" if search_object.use_year == 1 else ""

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


def update_user(user):
    exec_query("UPDATE korisnici SET password = ?, type = ? WHERE korisnik = ?",
               (user.password, user.type, user.username))


def new_user2(user):
    exec_query("INSERT INTO korisnici (korisnik, password, type) values (?, ?, ?)",
               (user.username, user.password, user.type))


def update_authors(author):
    data = exec_query("SELECT * FROM autori WHERE id_autora = ?", (author.id_author,))
    if len(data) == 1:
        exec_query("INSERT INTO autori (id_autora, ime, prezime) values(?, ?, ?)",
                   (author.id_author, author.name, author.surname))
    else:
        exec_query("UPDATE autori SET ime = ?, prezime = ? WHERE id_autora = ?",
                   (author.name, author.surname, author.id_author))


def get_new_author_id():
    data = exec_query("select MAX(id_autora) from autori")
    if data[1][0] is None:
        author = Author(0)
    else:
        author = Author(data[1][0] + 1)
    return author


def get_authors(raw_data=None):
    data = exec_query("select * from autori")
    if raw_data:
        return data
    authors = []
    for i in range(len(data) - 1):
        authors.append(Author(data[i+1][0], data[i+1][1], data[i+1][2]))
    return authors


def get_new_publisher_id():
    data = exec_query("select MAX(id_izdavaca) from izdavaci")
    if data[1][0] is None:
        publisher = Publisher(0)
    else:
        publisher = Publisher(data[1][0] + 1)
    return publisher


def update_publishers(publisher):
    data = exec_query("SELECT * FROM izdavaci WHERE id_izdavaca = ?", (publisher.id_publisher,))
    if len(data) == 1:
        exec_query("INSERT INTO izdavaci (id_izdavaca, naziv) values (?, ?)", (publisher.id_publisher, publisher.name))
    else:
        exec_query("UPDATE izdavaci SET naziv = ? WHERE id_izdavaca = ?", (publisher.name, publisher.id_publisher))


def get_publishers(raw_data=None):
    data = exec_query("select * from izdavaci")
    if raw_data:
        return data
    publishers = []
    for i in range(len(data)-1):
        publishers.append(Publisher(data[i+1][0], data[i+1][1]))
    return publishers


def get_new_book_id():
    data = exec_query("select MAX(id_knjige) from knjige")
    if data[1][0] is None:
        book = Book(0)
    else:
        book = Book(data[1][0] + 1)
    return book


def get_books(raw_data=None):
    data = exec_query("select * from knjige")
    if raw_data:
        return data
    books = []
    for i in range(len(data)-1):
        books.append(Book(data[i+1][0], data[i+1][1], data[i+1][2], data[i+1][3], data[i+1][4], data[i+1][5],
                          data[i+1][6], data[i+1][7], data[i+1][8]))
    return books


def update_books(book):
    data = exec_query("SELECT * FROM knjige WHERE id_knjige = ?", (book.id_book,))
    if len(data) == 1:
        exec_query("INSERT INTO knjige (id_knjige, naslov, id_autora, godina_izdanja, indeks, cena, kolicina_na_stanju,"
                   " id_izdavaca, deleted) values (?, ?, ?, ?, ?, ?, ?, ?, ? )", (book.id_book, book.title, book.author,
                                                                                  book.year, book.index, book.price,
                                                                                  book.quantity, book.publisher,
                                                                                  book.hidden))
    else:
        exec_query("UPDATE knjige SET naslov = ?, id_autora = ?, godina_izdanja = ?, indeks = ?, cena = ?, "
                   "kolicina_na_stanju = ?, id_izdavaca = ?, deleted = ? WHERE id_knjige = ?", (book.title, book.author,
                                                                                                book.year, book.index,
                                                                                                book.price,
                                                                                                book.quantity,
                                                                                                book.publisher,
                                                                                                book.hidden,
                                                                                                book.id_book))
    pass
