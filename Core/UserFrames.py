from tkinter import *

import Core


class CartFrame(LabelFrame):
    def __init__(self, master=None):
        LabelFrame.__init__(self, master, text="Korpa", padx=5, pady=5)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.listbox = Listbox(self, width=40)
        self.listbox.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.btn_remove = Button(self, text="Ukloni", command=self.remove)
        self.btn_remove.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.lbl_text = Label(self, text="Racun:")
        self.lbl_text.grid(row=2, column=0, sticky="w")
        self.var_total = StringVar()
        self.var_total.set("0.00 Din")
        self.lbl_total = Label(self, textvariable=self.var_total)
        self.lbl_total.grid(row=2, column=1, sticky="e")
        self.line = Frame(self, height=0.5, bg="black")
        self.line.grid(row=3, column=0, columnspan=2, padx=5, pady=(0, 5), sticky="ew")
        self.btn_buy = Button(self, text="Kupi", command=self.buy)
        if self.master.master.user.type != 0:
            self.btn_reservation = Button(self, text="Rezervisi", command=self.reservation)
            self.btn_reservation.grid(row=4, column=0, sticky="ew")
            self.btn_buy.grid(row=4, column=1, sticky="ew")
        else:
            self.btn_buy.grid(row=4, column=0, columnspan=2, sticky="ew")

    def buy(self):
        pass

    def remove(self):
        pass

    def reservation(self):
        pass


class Workspace(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        # first row
        Label(self, text="Pretrazi:").grid(row=0, column=0)
        self.varSearch = StringVar()
        Entry(self, textvariable=self.varSearch, width=70).grid(row=0, column=1, sticky="ew")
        Label(self, text="Godina:").grid(row=0, column=2)
        self.varYear = IntVar()
        self.varYear.set(2021)
        Spinbox(self, textvariable=self.varYear, from_=1900, to=2050, width=4).grid(row=0, column=3)
        Button(self, text="Pretraga", command=self.search).grid(row=0, column=4)
        # second row
        row = Frame(self)
        Label(row, text="Pretrazi po: ").grid(row=1, column=0)
        self.varAuthor = IntVar()
        Checkbutton(row, text="autoru", variable=self.varAuthor, onvalue=1, offvalue=0).grid(row=1, column=1)
        self.varTitle = IntVar()
        Checkbutton(row, text="nazivu", variable=self.varTitle, onvalue=1, offvalue=0).grid(row=1, column=2)
        self.varYear2 = IntVar()
        Checkbutton(row, text="godini", variable=self.varYear2, onvalue=1, offvalue=0).grid(row=1, column=3)
        row.grid(row=1, column=0, columnspan=5, sticky="nw")
        # third row
        Button(self, text="Smesti u korpu", command=self.add_to_cart).grid(row=2, column=0, columnspan=5, sticky="ew")
        # fourth row, DataGridView
        self.DataGridView = Core.DataGridView(self)
        self.DataGridView.grid(row=3, column=0, columnspan=5, sticky="nsew")
        # right side
        self.cart = CartFrame(self)
        self.cart.grid(row=0, column=5, rowspan=4, sticky="nsew", padx=(5, 0))
        self.search()

    def search(self):
        data = Core.get_list(self.master.user, Core.Search(self.varSearch.get(), self.varYear.get(),
                                                           self.varYear2.get(), self.varAuthor.get(),
                                                           self.varTitle.get()))
        self.DataGridView.show_data(data)
        pass

    def add_to_cart(self):
        pass
