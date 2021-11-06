import sqlite3
import Core
from datetime import datetime


user_types = ["Gost", "Korisnik", "Operator", "Administrator"]


def now():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')


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
        self.name = "" if name is None else name
        self.surname = "" if surname is None else surname

    def __str__(self):
        return self.name + " " + self.surname


class Publisher:
    def __init__(self, id_publisher, name=None):
        self.id_publisher = id_publisher
        self.name = "" if name is None else name

    def __str__(self):
        return self.name


class Book:
    def __init__(self, id_book, title=None, author=None, year=None, index=None, price=None, quantity=None,
                 publisher=None, hidden=None):
        self.id_book = id_book
        self.title = "" if title is None else title
        self.author = 0 if author is None else author
        self.year = 2021 if year is None else year
        self.index = "" if index is None else index
        self.price = 0 if price is None else price
        self.quantity = 0 if quantity is None else quantity
        self.publisher = 0 if publisher is None else publisher
        self.hidden = 0 if hidden is None else hidden

    def __str__(self):
        return self.title

    def equal(self, book):
        if self.id_book == book.id_book and self.title == book.title and self.author == book.author and \
                self.year == book.year and self.index == book.index and self.price == book.price and \
                self.quantity == book.quantity and self.publisher == book.publisher and self.hidden == book.hidden:
            return True
        return False


class Cart:
    def __init__(self, user, books, quantities):
        self.user = user
        self.books = books
        self.quantities = quantities


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


def get_list(user, search_object: Search):
    query = "SELECT naslov AS 'Naslov', godina_izdanja AS 'Godina izdanja', (ime || ' ' || prezime) AS 'Autor', naziv" \
            " AS 'Izdavac', (kolicina_na_stanju - sum(kolicina)) as Raspolozivo FROM knjige " \
            "INNER JOIN autori ON knjige.id_autora = autori.id_autora " \
            "INNER JOIN izdavaci ON knjige.id_izdavaca = izdavaci.id_izdavaca " \
            "INNER JOIN rezervacije ON knjige.id_knjige = rezervacije.id_knjige WHERE deleted = 0 " \
            "GROUP BY knjige.id_knjige HAVING Raspolozivo > 0"
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
    return exec_query(query, params)
    pass


def get_book_from_search(search_object, index):
    query = "SELECT id_knjige FROM knjige " \
            "INNER JOIN autori ON knjige.id_autora = autori.id_autora " \
            "INNER JOIN izdavaci ON knjige.id_izdavaca = izdavaci.id_izdavaca WHERE deleted = 0"
    if search_object.use_author + search_object.use_year + search_object.use_title >= 1:
        query += " WHERE "
        query += "(" if search_object.use_year == 1 and search_object.use_title + search_object.use_author >= 1 else ""
        query += "(ime || ' ' || prezime) LIKE ?" if search_object.use_author == 1 else ""
        query += " OR " if search_object.use_author + search_object.use_title == 2 else ""
        query += "naslov LIKE ?" if search_object.use_title == 1 else ""
        query += ") AND " if search_object.use_year == 1 and search_object.use_title + search_object.use_author >= 1 \
            else ""
        query += "godina_izdanja=?" if search_object.use_year == 1 else ""
    query += " LIMIT 1 OFFSET ?"
    params = []
    for i in range(search_object.use_title + search_object.use_author):
        params.append("%" + search_object.query + "%")
    if search_object.use_year == 1:
        params.append(search_object.year)
    params.append(index)
    book_id = exec_query(query, params)[1][0]
    books = get_books(restricted=True)
    for book in books:
        if book.id_book == book_id:
            return book
    pass


# make_reservations
def save_cart(cart):
    params = []
    query = "INSERT INTO rezervacije (korisnik, id_knjige, kolicina) VALUES"
    delete = "DELETE FROM rezervacije where korisnik = ?"
    exec_query(delete, (cart.user.username,))
    if len(cart.books) != 0:
        for i in range(len(cart.books)):
            params.append(cart.user.username)
            params.append(cart.books[i].id_book)
            params.append(cart.quantities[i])
        query += " (?, ?, ?)" + (len(cart.books) - 1) * ", (?, ?, ?)"
        exec_query(query, tuple(params))
    else:
        exec_query(delete, (cart.user.username,))


def list_cart(user):
    query = "SELECT * FROM knjige INNER JOIN rezervacije ON knjige.id_knjige = rezervacije.id_knjige WHERE korisnik = ?"
    data = exec_query(query, (user.username,))
    books = []
    quantities = []
    for i in range(len(data) - 1):
        books.append(Book(data[i+1][0], data[i+1][1], data[i+1][2], data[i+1][3], data[i+1][4], data[i+1][5],
                          data[i+1][6], data[i+1][7], data[i+1][8]))
        quantities.append(data[i+1][11])
    return Cart(user, books, quantities)


def buy(cart, total_price):
    if len(cart.books) != 0:
        data = exec_query("select MAX(id_racuna) from racuni")
        if data[1][0] is None:
            bill_id = 0
        else:
            bill_id = data[1][0] + 1
        # add new bill into racuni table
        bill_query = "INSERT INTO racuni (id_racuna, korisnik, datum, popust, ukupna_cena) VALUES (?, ?, ?, ?, ?)"
        bill_params = (bill_id, cart.user.username, now(), 0, total_price)
        exec_query(bill_query, bill_params)
        # add books into prodate_knjige table
        sold_query = "INSERT INTO prodate_knjige (id_knjige, id_racuna, cena, kolicina) VALUES"
        sold_params = []
        for i in range(len(cart.books)):
            sold_params.append(cart.books[i].id_book)
            sold_params.append(bill_id)
            sold_params.append(cart.books[i].price)
            sold_params.append(cart.quantities[i])
            # update storage values
            if cart.books[i].quantity - cart.quantities[i] > 0:
                exec_query("UPDATE knjige SET kolicina_na_stanju = ? WHERE id_knjige = ?",
                           (cart.books[i].quantity - cart.quantities[i], cart.books[i].id_book))
            else:
                exec_query("UPDATE knjige SET kolicina_na_stanju = 0, deleted = 1 WHERE id_knjige = ?",
                           (cart.books[i].id_book,))
        sold_query += " (?, ?, ?, ?)" + (len(cart.books) - 1) * ", (?, ?, ?, ?)"
        exec_query(sold_query, sold_params)
        save_cart(Cart(cart.user, [], []))


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


def get_books(raw_data=None, adv=None, restricted=None):
    if restricted is not None:
        data = exec_query("select knjige.id_knjige, naslov, id_autora, godina_izdanja, indeks, cena, "
                          "(kolicina_na_stanju - sum(kolicina)) as raspolozivo , id_izdavaca, deleted "
                          "from knjige inner join rezervacije on knjige.id_knjige = rezervacije.id_knjige "
                          "group by knjige.id_knjige")
    elif adv is not None:
        data = exec_query("select knjige.id_knjige, naslov, id_autora, godina_izdanja, indeks, cena, kolicina_na_stanju"
                          ", (kolicina_na_stanju - sum(kolicina)) as raspolozivo , id_izdavaca, deleted "
                          "from knjige inner join rezervacije on knjige.id_knjige = rezervacije.id_knjige "
                          "group by knjige.id_knjige")
    else:
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


def stats(from_date, to_date, precision):  # precision 1 year, 2 month, 3 day
    if precision == 1:
        format = "%Y"
    elif precision == 2:
        format = "%Y-%m"
    else:
        format = "%Y-%m-%d"
    query = "SELECT strftime('" + format + "', datum) AS Datum, COUNT(racuni.id_racuna) AS 'Broj kupaca', SUM(ukupna_cena) " \
            "AS Suma, SUM(id_knjige) AS 'Broj knjiga' FROM racuni INNER JOIN prodate_knjige " \
            "ON racuni.id_racuna = prodate_knjige.id_racuna WHERE Datum > ? AND Datum < ? " \
            "GROUP BY strftime('" + format + "', datum)"
    return exec_query(query, (from_date, to_date))
