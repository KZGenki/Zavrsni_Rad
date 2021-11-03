from tkinter import *
from tkinter import messagebox
import sqlite3
import Core


class OperatorFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Button(self, text="Dodaj knjigu", command=self.tk_add_book).grid(row=0, column=0, sticky="ew")
        Button(self, text="Dodaj autora", command=self.tk_add_author).grid(row=1, column=0, sticky="ew")
        Button(self, text="Dodaj izdavaca", command=self.tk_add_publisher).grid(row=2, column=0, sticky="ew")
        Button(self, text="Dodaj placeholder", command=self.tk_add_book).grid(row=3, column=0, sticky="ew")

    def tk_add_book(self):
        pass

    def tk_add_publisher(self):
        pass

    def tk_add_author(self):
        author = Core.get_new_author_id()
        toplevel = Toplevel(self)
        EditAuthor(toplevel, author).pack()
        pass


class EditPublisher(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)


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
    def __init__(self, master=None):
        Frame.__init__(self, master)