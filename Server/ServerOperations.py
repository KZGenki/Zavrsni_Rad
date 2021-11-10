import Operations


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


def exec_data(data):
    print(data)
    new_data = None
    if data is Login:
        new_data = Operations.login(data.username, data.password)
    elif data is NewUser:
        new_data = Operations.new_user(data.username, data.password)
    elif data is ExecQuery:
        new_data = Operations.exec_query(data.query, data.params)
    elif data is GetList:
        new_data = Operations.get_list(data.user, data.search_object)
    elif data is GetBookFromSearch:
        new_data = Operations.get_book_from_search(data.search_object, data.index)
    elif data is SaveCart:
        new_data = Operations.save_cart(data.cart)
    elif data is ListCart:
        new_data = Operations.list_cart(data.user)
    elif data is Buy:
        new_data = Operations.buy(data.cart, data.total_price)
    elif data is GetUsers:
        new_data = Operations.get_users()
    elif data is UpdateUser:
        new_data = Operations.update_user(data.user)
    elif data is NewUser2:
        new_data = Operations.new_user2(data.user)
    elif data is UpdateAuthors:
        new_data = Operations.update_authors(data.author)
    elif data is GetNewAuthorId:
        new_data = Operations.get_new_author_id()
    elif data is GetAuthors:
        new_data = Operations.get_authors(data.raw_data)
    elif data is GetNewPublisherId:
        new_data = Operations.get_new_publisher_id()
    elif data is UpdatePublishers:
        new_data = Operations.update_publishers(data.publisher)
    elif data is GetPublishers:
        new_data = Operations.get_publishers(data.raw_data)
    elif data is GetNewBookId:
        new_data = Operations.get_new_book_id()
    elif data is GetBooks:
        new_data = Operations.get_books(data.raw_data, data.adv, data.restricted)
    elif data is UpdateBooks:
        new_data = Operations.update_books(data.book)
    elif data is Stats:
        new_data = Operations.stats(data.from_date, data.to_date, data.precision)
    elif data is Reservations:
        new_data = Operations.reservations(data.user, data.index)
    elif data is RemoveReservation:
        new_data = Operations.remove_reservation(data.user, data.book_id)
    elif data is AddReservation:
        new_data = Operations.add_reservation(data.user, data.book, data.quantity)
    elif data is EditReservation:
        new_data = Operations.edit_reservation(data.user, data.book, data.quantity)
    return new_data
