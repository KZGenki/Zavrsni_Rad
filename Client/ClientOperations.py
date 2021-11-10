import Core
from datetime import datetime
import Client


user_types = ["Gost", "Korisnik", "Operator", "Administrator"]
HOST = '127.0.0.1'
PORT = 50007
client = Client.ClientData(HOST, PORT)


def now():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def login(username="Guest", password="Guest"):
    return client.send_receive(Core.Login(username, password))


def new_user(username, password):
    return client.send_receive(Core.NewUser(username, password))


def exec_query(query, params=None):
    return client.send_receive(Core.ExecQuery(query, params))


def get_list(user, search_object):
    return client.send_receive(Core.GetList(user, search_object))


def get_book_from_search(search_object, index):
    return client.send_receive(Core.GetBookFromSearch(search_object, index))


def save_cart(cart):
    return client.send_receive(Core.SaveCart(cart))


def list_cart(user):
    return client.send_receive(Core.ListCart(user))


def buy(cart, total_price):
    return client.send_receive(Core.Buy(cart, total_price))


def get_users():
    return client.send_receive(Core.GetUsers())


def update_user(user):
    return client.send_receive(Core.UpdateUser(user))


def new_user2(user):
    return client.send_receive(Core.NewUser2(user))


def update_authors(author):
    return client.send_receive(Core.UpdateAuthors(author))


def get_new_author_id():
    return client.send_receive(Core.GetNewAuthorId())


def get_authors(raw_data=None):
    return client.send_receive(Core.GetAuthors(raw_data))


def get_new_publisher_id():
    return client.send_receive(Core.GetNewPublisherId())


def update_publishers(publisher):
    return client.send_receive(Core.UpdatePublishers(publisher))


def get_publishers(raw_data=None):
    return client.send_receive(Core.GetPublishers(raw_data))


def get_new_book_id():
    return client.send_receive(Core.GetNewBookId())


def get_books(raw_data=None, adv=None, restricted=None):
    return client.send_receive(Core.GetBooks(raw_data, adv, restricted))


def update_books(book):
    return client.send_receive(Core.UpdateBooks(book))


def stats(from_date, to_date, precision):  # precision 1 year, 2 month, 3 day
    return client.send_receive(Core.Stats(from_date, to_date, precision))


def reservations(user, index=None):
    return client.send_receive(Core.Reservations(user, index))


def remove_reservation(user, book_id):
    return client.send_receive(Core.RemoveReservation(user, book_id))


def add_reservation(user, book, quantity):
    return client.send_receive(Core.AddReservation(user, book, quantity))


def edit_reservation(user, book, quantity):
    return client.send_receive(Core.EditReservation(user, book, quantity))
