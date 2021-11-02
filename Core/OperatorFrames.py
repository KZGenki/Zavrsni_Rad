from tkinter import *
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
        pass
