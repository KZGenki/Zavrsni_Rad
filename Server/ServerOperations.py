import Operations
import Core
import Server


def exec_data(data):
    new_data = None
    try:
        if isinstance(data, Server.Kill):
            return "kill"
        elif isinstance(data, Core.Login):
            new_data = Operations.login(data.username, data.password)
        elif isinstance(data, Core.NewUser):
            new_data = Operations.new_user(data.username, data.password)
        elif isinstance(data, Core.ExecQuery):
            new_data = Operations.exec_query(data.query, data.params)
        elif isinstance(data, Core.GetList):
            new_data = Operations.get_list(data.user, data.search_object)
        elif isinstance(data, Core.GetBookFromSearch):
            new_data = Operations.get_book_from_search(data.search_object, data.index)
        elif isinstance(data, Core.SaveCart):
            new_data = Operations.save_cart(data.cart)
        elif isinstance(data, Core.ListCart):
            new_data = Operations.list_cart(data.user)
        elif isinstance(data, Core.Buy):
            new_data = Operations.buy(data.cart, data.total_price)
        elif isinstance(data, Core.GetUsers):
            new_data = Operations.get_users()
        elif isinstance(data, Core.UpdateUser):
            new_data = Operations.update_user(data.user)
        elif isinstance(data, Core.NewUser2):
            new_data = Operations.new_user2(data.user)
        elif isinstance(data, Core.UpdateAuthors):
            new_data = Operations.update_authors(data.author)
        elif isinstance(data, Core.GetAuthors):
            new_data = Operations.get_new_author_id()
        elif isinstance(data, Core.GetAuthors):
            new_data = Operations.get_authors(data.raw_data)
        elif isinstance(data, Core.GetNewPublisherId):
            new_data = Operations.get_new_publisher_id()
        elif isinstance(data, Core.UpdatePublishers):
            new_data = Operations.update_publishers(data.publisher)
        elif isinstance(data, Core.GetPublishers):
            new_data = Operations.get_publishers(data.raw_data)
        elif isinstance(data, Core.GetNewBookId):
            new_data = Operations.get_new_book_id()
        elif isinstance(data, Core.GetBooks):
            new_data = Operations.get_books(data.raw_data, data.adv, data.restricted)
        elif isinstance(data, Core.UpdateBooks):
            new_data = Operations.update_books(data.book)
        elif isinstance(data, Core.Stats):
            new_data = Operations.stats(data.from_date, data.to_date, data.precision)
        elif isinstance(data, Core.Reservations):
            new_data = Operations.reservations(data.user, data.index)
        elif isinstance(data, Core.RemoveReservation):
            new_data = Operations.remove_reservation(data.user, data.book_id)
        elif isinstance(data, Core.AddReservation):
            new_data = Operations.add_reservation(data.user, data.book, data.quantity)
        elif isinstance(data, Core.EditReservation):
            new_data = Operations.edit_reservation(data.user, data.book, data.quantity)
    except Core.LoginError as e:
        return e
    else:
        return new_data
