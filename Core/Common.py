def clear_master(master):
    slaves = master.grid_slaves()
    for slave in slaves:
        slave.destroy()


class Login:
    def __init__(self, username="Guest", password="Guest"):
        self.classname = "Login"
        self.username = username
        self.password = password


class NewUser:
    def __init__(self, username, password):
        self.classname = "NewUser"
        self.username = username
        self.password = password


class ExecQuery:
    def __init__(self, query, params=None):
        self.classname = "ExecQuery"
        self.query = query
        self.params = params


class GetList:
    def __init__(self, user, search_object):
        self.classname = "GetList"
        self.user = user
        self.search_object = search_object


class GetBookFromSearch:
    def __init__(self, search_object, index):
        self.classname = "GetBookFromSearch"
        self.index = index
        self.search_object = search_object


class SaveCart:
    def __init__(self, cart):
        self.classname = "SaveCart"
        self.cart = cart


class ListCart:
    def __init__(self, user):
        self.classname = "ListCart"
        self.user = user


class Buy:
    def __init__(self, cart, total_price):
        self.classname = "Buy"
        self.cart = cart
        self.total_price = total_price


class GetUsers:
    def __init__(self):
        self.classname = "GetUsers"
        pass


class UpdateUser:
    def __init__(self, user):
        self.classname = "UpdateUser"
        self.user = user


class NewUser2:
    def __init__(self, user):
        self.classname = "NewUser2"
        self.user = user


class UpdateAuthors:
    def __init__(self, author):
        self.classname = "UpdateAuthors"
        self.author = author


class GetNewAuthorId:
    def __init__(self):
        self.classname = "GetNewAuthorId"
        pass


class GetAuthors:
    def __init__(self, raw_data=None):
        self.classname = "GetAuthors"
        self.raw_data = raw_data


class GetNewPublisherId:
    def __init__(self):
        self.classname = "GetNewPublisherId"
        pass


class UpdatePublishers:
    def __init__(self, publisher):
        self.classname = "UpdatePublishers"
        self.publisher = publisher


class GetPublishers:
    def __init__(self, raw_data=None):
        self.classname = "GetPublishers"
        self.raw_data = raw_data


class GetNewBookId:
    def __init__(self):
        self.classname = "GetNewBookId"
        pass


class GetBooks:
    def __init__(self, raw_data=None, adv=None, restricted=None):
        self.classname = "GetBooks"
        self.raw_data = raw_data
        self.adv = adv
        self.restricted = restricted


class UpdateBooks:
    def __init__(self, books):
        self.classname = "UpdateBooks"
        self.books = books


class Stats:
    def __init__(self, from_date, to_date, precision):
        self.classname = Stats.__name__
        self.from_date = from_date
        self.to_date = to_date
        self.precision = precision


class Reservations:
    def __init__(self, user, index=None):
        self.classname = Reservations.__name__
        self.user = user
        self.index = index


class RemoveReservation:
    def __init__(self, user, book_id):
        self.classname = RemoveReservation.__name__
        self.user = user
        self.book_id = book_id


class AddReservation:
    def __init__(self, user, book, quantity):
        self.classname = AddReservation.__name__
        self.user = user
        self.book = book
        self.quantity = quantity


class EditReservation:
    def __init__(self, user, book, quantity):
        self.classname = EditReservation.__name__
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
