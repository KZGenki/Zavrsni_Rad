from tkinter import *
from tkinter import messagebox
import Core


class CartFrame(LabelFrame):
    def __init__(self, master=None):
        LabelFrame.__init__(self, master, text="Korpa", padx=5, pady=5)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.items = []
        self.quantities = []
        self.listbox = Listbox(self, width=40)
        self.listbox.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.scrollbar = Scrollbar(self, command=self.listbox.yview)
        self.scrollbar.grid(row=0, column=3, sticky="ns")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.btn_remove = Button(self, text="Ukloni", command=self.remove)
        self.btn_remove.grid(row=1, column=0, sticky="ew")
        self.btn_remove_one = Button(self, text="Ukloni jedan", command=self.remove_one)
        self.btn_remove_one.grid(row=1, column=1, sticky="ew")
        self.lbl_text = Label(self, text="Račun:")
        self.lbl_text.grid(row=2, column=0, sticky="w")
        self.var_total = StringVar()
        self.var_total.set("0.0 Din")
        self.lbl_total = Label(self, textvariable=self.var_total)
        self.lbl_total.grid(row=2, column=1, sticky="e")
        self.line = Frame(self, height=0.5, bg="black")
        self.line.grid(row=3, column=0, columnspan=2, padx=5, pady=(0, 5), sticky="ew")
        self.btn_buy = Button(self, text="Kupi", command=self.buy)
        if self.master.master.user.type != 0:
            self.btn_reservation = Button(self, text="Rezerviši", command=self.reservation)
            self.btn_reservation.grid(row=4, column=0, sticky="ew")
            self.btn_buy.grid(row=4, column=1, sticky="ew")
            self.load_reservation()
        else:
            self.btn_buy.grid(row=4, column=0, columnspan=2, sticky="ew")

    def add(self, book):
        index = -1
        for i in range(len(self.items)):
            if self.items[i].equal(book):
                index = i
                break
        if index == -1:
            self.quantities.append(1)
            self.items.append(book)
            self.listbox.insert(END, book)
            self.listbox.insert(END, "   " + str(book.price) + " Din   x" + str(self.quantities[index]) + "     " +
                                str(book.price * self.quantities[index])+" Din")
        else:
            if self.quantities[i] + 1 > self.items[i].quantity:
                messagebox.showwarning("Upozorenje", "Dostignuta je maksimalna dostupna količina")
                return
            self.quantities[i] += 1
            self.listbox.delete(index * 2 + 1)
            self.listbox.insert(index * 2 + 1, "   " + str(book.price) + " Din   x" +
                                str(self.quantities[index]) + "     " + str(book.price * self.quantities[index])+" Din")
        self.total()

    def total(self):
        total = 0.0
        for i in range(len(self.items)):
            total += self.items[i].price * self.quantities[i]
        self.var_total.set(str(total) + " Din")
        return total

    def buy(self):
        if len(self.items) != 0:
            cart = Core.Cart(self.master.master.user, self.items, self.quantities)
            Core.buy(cart, self.total())
            self.load_reservation()
            self.master.search()
        else:
            messagebox.showwarning("Upozorenje", "Korpa je prazna, ubacite proizvod u korpu prvo")
        pass

    def remove(self):
        try:
            index = self.listbox.curselection()[0]
            if index % 2 == 1:
                index = index - 1
            self.items.pop(int(index/2))
            self.quantities.pop(int(index/2))
            self.listbox.delete(index, index + 1)
            self.total()
            if len(self.items) == 0:
                Core.save_cart(Core.Cart(self.master.master.user, [], []))
                self.master.search()
        except IndexError as e:
            messagebox.showwarning("Upozorenje", "Niste izabrali stavku u korpi")
        pass

    def remove_one(self):
        try:
            index = self.listbox.curselection()[0]
            if index % 2 == 1:
                index = index - 1
                index = int(index/2)
            if self.quantities[index] <= 1:
                self.remove()
                return
            self.quantities[index] -= 1
            self.listbox.delete(index * 2 + 1)
            self.listbox.insert(index * 2 + 1, "   " + str(self.items[index].price) + " Din   x" +
                                str(self.quantities[index]) + "     " + str(self.items[index].price *
                                                                            self.quantities[index])+" Din")
            self.total()
        except IndexError as e:
            messagebox.showwarning("Upozorenje", "Niste izabrali stavku u korpi")
        pass

    def reservation(self):
        if len(self.items) != 0:
            cart = Core.Cart(self.master.master.user, self.items, self.quantities)
            Core.save_cart(cart)
            self.master.search()
        else:
            messagebox.showwarning("Upozorenje", "Korpa je prazna, ubacite proizvod u korpu prvo")
        pass

    def load_reservation(self):
        cart = Core.list_cart(self.master.master.user)
        self.items = cart.books
        self.quantities = cart.quantities
        self.listbox.delete(0, END)
        for i in range(len(self.items)):
            self.listbox.insert(END, self.items[i])
            self.listbox.insert(END, "   " + str(self.items[i].price) + " Din   x" + str(self.quantities[-1]) +
                                "     " + str(self.items[i].price * self.quantities[-1]) + " Din")
        self.total()


class Workspace(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        # first row
        Label(self, text="Pretraži:").grid(row=0, column=0)
        self.varSearch = StringVar()
        Entry(self, textvariable=self.varSearch, width=70).grid(row=0, column=1, sticky="ew")
        Label(self, text="Godina:").grid(row=0, column=2)
        self.varYear = IntVar()
        self.varYear.set(2021)
        Spinbox(self, textvariable=self.varYear, from_=1900, to=2050, width=4).grid(row=0, column=3)
        Button(self, text="Pretraga", command=self.search).grid(row=0, column=4)
        # second row
        row = Frame(self)
        Label(row, text="Pretraži po: ").grid(row=1, column=0)
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
        self.DataGridView = Core.DataGridView(self, double_click=self.add_to_cart)
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

    def add_to_cart(self, arg=None):
        index = self.DataGridView.index()
        book = Core.get_book_from_search(Core.Search(self.varSearch.get(), self.varYear.get(), self.varYear2.get(),
                                                     self.varAuthor.get(), self.varTitle.get()), index)
        if book.quantity >= 1:
            self.cart.add(book)
        pass
