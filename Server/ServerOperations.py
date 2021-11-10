import Operations
import Core


def exec_data(data):
    print(data)
    new_data = None
    if data.classname == "Login":
        new_data = Operations.login(data.username, data.password)
    elif data.classname == "NewUser""":
        new_data = Operations.new_user(data.username, data.password)
    elif data.classname == "ExecQuery":
        new_data = Operations.exec_query(data.query, data.params)
    elif data.classname == "GetList":
        new_data = Operations.get_list(data.user, data.search_object)
    elif data.classname == "GetBookFromSearch":
        new_data = Operations.get_book_from_search(data.search_object, data.index)
    elif data.classname == "SaveCart":
        new_data = Operations.save_cart(data.cart)
    elif data.classname == "ListCart":
        new_data = Operations.list_cart(data.user)
    elif data.classname == "Buy":
        new_data = Operations.buy(data.cart, data.total_price)
    elif data.classname == "GetUsers":
        new_data = Operations.get_users()
    elif data.classname == "UpdateUser":
        new_data = Operations.update_user(data.user)
    elif data.classname == "NewUser2":
        new_data = Operations.new_user2(data.user)
    elif data.classname == "UpdateAuthors":
        new_data = Operations.update_authors(data.author)
    elif data.classname == "GetNewAuthorId":
        new_data = Operations.get_new_author_id()
    elif data.classname == "GetAuthors":
        new_data = Operations.get_authors(data.raw_data)
    elif data.classname == "GetNewPublisherId":
        new_data = Operations.get_new_publisher_id()
    elif data.classname == "UpdatePublishers":
        new_data = Operations.update_publishers(data.publisher)
    elif data.classname == "GetPublishers":
        new_data = Operations.get_publishers(data.raw_data)
    elif data.classname == "GetNewBookId":
        new_data = Operations.get_new_book_id()
    elif data.classname == "GetBooks":
        new_data = Operations.get_books(data.raw_data, data.adv, data.restricted)
    elif data.classname == "UpdateBooks":
        new_data = Operations.update_books(data.book)
    elif data.classname == "Stats":
        new_data = Operations.stats(data.from_date, data.to_date, data.precision)
    elif data.classname == "Reservations":
        new_data = Operations.reservations(data.user, data.index)
    elif data.classname == "RemoveReservation":
        new_data = Operations.remove_reservation(data.user, data.book_id)
    elif data.classname == "AddReservation":
        new_data = Operations.add_reservation(data.user, data.book, data.quantity)
    elif data.classname == "EditReservation":
        new_data = Operations.edit_reservation(data.user, data.book, data.quantity)
    return new_data
