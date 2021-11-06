from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import Core


class OperatorFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(4, weight=1)
        self.btn_store = Button(self, text="Knjizara", command=self.tk_store, relief=SUNKEN)
        self.btn_store.grid(row=0, column=0, sticky="ew")
        self.btn_users = Button(self, text="Korisnici", command=self.tk_users)
        self.btn_users.grid(row=0, column=1, sticky="ew")
        self.working_frame = OperatorStorageFrame(self)
        self.working_frame.grid(row=1, column=0, columnspan=5, sticky="nsew")

    def tk_store(self):
        if self.btn_store["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = OperatorStorageFrame(self)
            self.working_frame.grid(row=1, column=0, columnspan=5, sticky="nsew")
            self.btn_store["relief"] = SUNKEN
            self.btn_users["relief"] = RAISED
        pass

    def tk_users(self):
        if self.btn_users["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = OperatorUsersFrame(self)
            self.working_frame.grid(row=1, column=0, columnspan=5, sticky="nsew")
            self.btn_store["relief"] = RAISED
            self.btn_users["relief"] = SUNKEN
        pass


class EditPublisher(Frame):
    def __init__(self, master=None, publisher=None):
        Frame.__init__(self, master)
        self.publisher = publisher
        Label(self, text="Ime:").grid(row=0, column=0, sticky="e")
        self.varName = StringVar()
        Entry(self, textvariable=self.varName).grid(row=0, column=1, sticky="ew")
        Button(self, text="Azuriraj", command=self.tk_update_publisher).grid(row=1, column=0, columnspan=2, sticky="ew")
        if self.publisher is not None:
            self.varName.set(self.publisher.name)

    def tk_update_publisher(self):
        if self.publisher.name != self.varName.get():
            publisher = Core.Publisher(self.publisher.id_publisher, self.varName.get())
            Core.update_publishers(publisher)
            self.master.destroy()
        else:
            messagebox.showinfo("Obavestenje", "Nisu uneti novi podaci, nece biti izvrseno azuriranje")


class EditAuthor(Frame):
    def __init__(self, master=None, author=None):
        Frame.__init__(self, master)
        self.author = author
        Label(self, text="Ime:").grid(row=0, column=0, sticky="e")
        self.varName = StringVar()
        Entry(self, textvariable=self.varName).grid(row=0, column=1, sticky="ew")
        Label(self, text="Prezime: ").grid(row=1, column=0, sticky="e")
        self.varSurname = StringVar()
        Entry(self, textvariable=self.varSurname).grid(row=1, column=1, sticky="ew")
        Button(self, text="Azuriraj", command=self.tk_update_author).grid(row=2, column=0, columnspan=2, sticky="ew")
        if self.author is None:
            self.author = Core.Author(0, "", "")
        self.varName.set(self.author.name)
        self.varSurname.set(self.author.surname)

    def tk_update_author(self):
        if self.author.name != self.varName.get() or self.author.surname != self.varSurname.get():
            author = Core.Author(self.author.id_author, self.varName.get(), self.varSurname.get())
            Core.update_authors(author)
            self.master.destroy()
        else:
            messagebox.showinfo("Obavestenje", "Nisu uneti novi podaci, nece biti izvrseno azuriranje")
        pass


class EditBook(Frame):
    def __init__(self, master=None, book=None):
        Frame.__init__(self, master)
        self.book = book
        self.list_of_authors = Core.get_authors()
        self.list_of_publishers = Core.get_publishers()
        self.varTitle = StringVar()
        self.varYear = IntVar()
        self.varIndex = StringVar()
        self.varPrice = DoubleVar()
        self.varQuantity = IntVar()
        self.varHidden = IntVar()
        Label(self, text="Naslov: ").grid(row=0, column=0, sticky="e")
        Entry(self, textvariable=self.varTitle).grid(row=0, column=1, sticky="ew")
        Label(self, text="Autor: ").grid(row=1, column=0, sticky="e")
        self.cbAuthors = Combobox(self, state="readonly", values=self.list_of_authors)
        self.cbAuthors.grid(row=1, column=1, sticky="ew")
        Label(self, text="Godina izdanja: ").grid(row=2, column=0, sticky="e")
        Spinbox(self, textvariable=self.varYear, from_=1900, to=2050, width=4).grid(row=2, column=1, sticky="w")
        Label(self, text="Indeks: ").grid(row=3, column=0, sticky="e")
        Entry(self, textvariable=self.varIndex).grid(row=3, column=1, sticky="ew")
        Label(self, text="Cena: ").grid(row=4, column=0, sticky="e")
        Entry(self, textvariable=self.varPrice).grid(row=4, column=1, sticky="ew")
        Label(self, text="Kolicina na stanju").grid(row=5, column=0, sticky="e")
        Spinbox(self, textvariable=self.varQuantity, from_=0, to=10000).grid(row=5, column=1, sticky="ew")
        Label(self, text="Izdavac: ").grid(row=6, column=0, sticky="e")
        self.cbPublishers = Combobox(self, state="readonly", values=self.list_of_publishers)
        self.cbPublishers.grid(row=6, column=1, sticky="ew")
        Label(self, text="Sakriven: ").grid(row=7, column=0, sticky="e")
        Checkbutton(self, variable=self.varHidden, onvalue=1, offvalue=0).grid(row=7, column=1, sticky="w")
        Button(self, text="Azuriraj", command=self.tk_update_book).grid(row=8, column=0, columnspan=2, sticky="ew")
        if self.book is not None:
            self.varTitle.set(self.book.title)
            self.varYear.set(self.book.year)
            self.varIndex.set(self.book.index)
            self.varPrice.set(self.book.price)
            self.varQuantity.set(self.book.quantity)
            self.varHidden.set(self.book.hidden)
            self.cbPublishers.current(self.book.publisher)
            self.cbAuthors.current(self.book.author)

    def tk_update_book(self):
        new_book = Core.Book(self.book.id_book, self.varTitle.get(), self.cbAuthors.current(), self.varYear.get(),
                             self.varIndex.get(), self.varPrice.get(), self.varQuantity.get(),
                             self.cbPublishers.current(), self.varHidden.get())
        if not new_book.equal(self.book):  # and self.book.title is None:
            Core.update_books(new_book)
            self.master.destroy()
        else:
            messagebox.showinfo("Obavestenje", "Nisu uneti novi podaci, nece biti izvrseno azuriranje")
        pass


class OperatorStorageFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(4, weight=1)
        self.list_of_operator_tables = ['knjige', 'autori', 'izdavaci']
        Label(self, text="Tabela:").grid(row=0, column=0, sticky="e")
        self.cbTable = Combobox(self, state="readonly", values=self.list_of_operator_tables)
        self.cbTable.bind("<<ComboboxSelected>>", self.tk_cb_change)
        self.cbTable.grid(row=0, column=1, sticky="ew")
        self.cbTable.set(self.list_of_operator_tables[0])
        Button(self, text="Dodaj", command=self.btn_add).grid(row=0, column=2, sticky="ew")
        Button(self, text="Izmeni", command=self.btn_edit).grid(row=0, column=3, sticky="ew")
        self.DataGridView = Core.DataGridView(self, double_click=self.dgv_double_click)
        self.DataGridView.grid(row=1, column=0, columnspan=5, sticky="nsew")
        self.tk_cb_change()

    def btn_add(self):
        pool = self.cbTable.get()
        if pool == self.list_of_operator_tables[0]:  # knjige
            self.tk_add_book()
        if pool == self.list_of_operator_tables[1]:  # autori
            self.tk_add_author()
        if pool == self.list_of_operator_tables[2]:  # izdavaci
            self.tk_add_publisher()

    def btn_edit(self):
        index = self.DataGridView.index()
        if index == -1:
            messagebox.showwarning("Upozorenje", "Niste izabrali red u tabeli")
        else:
            self.dgv_double_click(index)

    def tk_cb_change(self, arg=None):
        pool = self.cbTable.get()
        data = []
        if pool == self.list_of_operator_tables[0]:  # knjige
            data = Core.get_books(True)
        if pool == self.list_of_operator_tables[1]:  # autori
            data = Core.get_authors(True)
        if pool == self.list_of_operator_tables[2]:  # izdavaci
            data = Core.get_publishers(True)
        self.DataGridView.show_data(data)

    def dgv_double_click(self, index):
        pool = self.cbTable.get()
        if pool == self.list_of_operator_tables[0]:  # knjige
            data = Core.get_books()[index]
            self.toplevel_edit(book=data)
        if pool == self.list_of_operator_tables[1]:  # autori
            data = Core.get_authors()[index]
            self.toplevel_edit(author=data)
        if pool == self.list_of_operator_tables[2]:  # izdavaci
            data = Core.get_publishers()[index]
            self.toplevel_edit(publisher=data)

    def toplevel_edit(self, book=None, author=None, publisher=None):
        if book is not None:
            toplevel = Toplevel(self)
            EditBook(toplevel, book).pack()
        elif author is not None:
            toplevel = Toplevel(self)
            EditAuthor(toplevel, author).pack()
        elif publisher is not None:
            toplevel = Toplevel(self)
            EditPublisher(toplevel, publisher).pack()
        toplevel.grab_set()
        self.wait_window(toplevel)
        self.tk_cb_change()

    def tk_add_book(self):
        book = Core.get_new_book_id()
        toplevel = Toplevel(self)
        EditBook(toplevel, book).pack()
        toplevel.grab_set()
        self.wait_window(toplevel)
        self.tk_cb_change()
        pass

    def tk_add_publisher(self):
        publisher = Core.get_new_publisher_id()
        toplevel = Toplevel(self)
        EditPublisher(toplevel, publisher).pack()
        toplevel.grab_set()
        self.wait_window(toplevel)
        self.tk_cb_change()
        pass

    def tk_add_author(self):
        author = Core.get_new_author_id()
        toplevel = Toplevel(self)
        EditAuthor(toplevel, author).pack()
        toplevel.grab_set()
        self.wait_window(toplevel)
        self.tk_cb_change()
        pass


class OperatorUsersFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
