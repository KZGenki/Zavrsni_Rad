import sqlite3
import GUI
from datetime import datetime
import Client


user_types = ["Gost", "Korisnik", "Operator", "Administrator"]
HOST = '127.0.0.1'
PORT = 50007
client = Client.ClientData(HOST, PORT)


def now():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')


class Login:
    def __init__(self, username="Guest", password="Guest"):
        self.username = username
        self.password = password


class NewUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class ExecQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params


class GetList:
    def __init__(self, user, search_object):
        self.user = user
        self.search_object = search_object


class GetBookFromSearch:
    def __init__(self, search_object, index):
        self.index = index
        self.search_object = search_object


class SaveCart:
    def __init__(self, cart):
        self.cart = cart


class ListCart:
    def __init__(self, user):
        self.user = user


class Buy:
    def __init__(self, cart, total_price):
        self.cart = cart
        self.total_price = total_price


class GetUsers:
    def __init__(self):
        pass


class UpdateUser:
    def __init__(self, user):
        self.user = user


class NewUser2:
    def __init__(self, user):
        self.user = user


class UpdateAuthors:
    def __init__(self, author):
        self.author = author


class GetNewAuthorId:
    def __init__(self):
        pass


class GetAuthors:
    def __init__(self, raw_data=None):
        self.raw_data = raw_data


class GetNewPublisherId:
    def __init__(self):
        pass


class UpdatePublishers:
    def __init__(self, publisher):
        self.publisher = publisher


class GetPublishers:
    def __init__(self, raw_data=None):
        self.raw_data = raw_data


class GetNewBookId:
    def __init__(self):
        pass


class GetBooks:
    def __init__(self, raw_data=None, adv=None, restricted=None):
        self.raw_data = raw_data
        self.adv = adv
        self.restricted = restricted


class UpdateBooks:
    def __init__(self, books):
        self.books = books


class Stats:
    def __init__(self, from_date, to_date, precision):
        self.from_date = from_date
        self.to_date = to_date
        self.precision = precision


class Reservations:
    def __init__(self, user, index=None):
        self.user = user
        self.index = index


class RemoveReservation:
    def __init__(self, user, book_id):
        self.user = user
        self.book_id = book_id


class AddReservation:
    def __init__(self, user, book, quantity):
        self.user = user
        self.book = book
        self.quantity = quantity


class EditReservation:
    def __init__(self, user, book, quantity):
        self.user = user
        self.book = book
        self.quantity = quantity


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


def login(username="Guest", password="Guest"):
    data = Login(username, password)
    client.send_data(data)
    new_data = client.get_data()
    return new_data
    pass


def new_user(username, password):
    pass


def exec_query(query, params=None):
    pass


def get_list(user, search_object):
    data = GetList(user, search_object)
    client.send_data(data)
    new_data = client.get_data()
    return new_data
    pass


def get_book_from_search(search_object, index):
    pass


def save_cart(cart):
    pass


def list_cart(user):
    pass


def buy(cart, total_price):
    pass


def get_users():
    pass


def update_user(user):
    pass


def new_user2(user):
    pass


def update_authors(author):
    pass


def get_new_author_id():
    pass


def get_authors(raw_data=None):
    pass


def get_new_publisher_id():
    pass


def update_publishers(publisher):
    pass


def get_publishers(raw_data=None):
    pass


def get_new_book_id():
    pass


def get_books(raw_data=None, adv=None, restricted=None):
    pass


def update_books(book):
    pass


def stats(from_date, to_date, precision):  # precision 1 year, 2 month, 3 day
    pass


def reservations(user, index=None):
    pass


def remove_reservation(user, book_id):
    pass


def add_reservation(user, book, quantity):
    pass


def edit_reservation(user, book, quantity):
    pass
