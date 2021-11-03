from tkinter import *
from tkinter import messagebox
import sqlite3
import Core


class AdminMainFrame(Frame):
    def __init__(self, master=None, user=None):
        Frame.__init__(self, master)
        self.user = user
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        # buttons
        self.btn_user = Button(self.master.top_row, text="Korisnik", command=self.tk_user)
        self.btn_user.grid(row=0, column=0, sticky="e")
        self.btn_operator = Button(self.master.top_row, text="Operator", command=self.tk_operator)
        self.btn_operator.grid(row=0, column=1, sticky="e")
        self.btn_admin = Button(self.master.top_row, text="Admin", command=self.tk_admin)
        self.btn_admin.grid(row=0, column=2, sticky="e")
        self.btn_advanced = Button(self.master.top_row, text="Napredno", command=self.tk_advanced)
        self.btn_advanced.grid(row=0, column=3, sticky="e")

        self.working_frame = Frame(self)  # Core.Workspace(self)
        # self.working_frame.grid(row=1, column=0, sticky="nsew")
        self.tk_admin()

    def tk_user(self):
        if self.btn_user["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.Workspace(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_user["relief"] = SUNKEN

    def tk_advanced(self):
        if self.btn_advanced["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.AdvancedFrame(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_advanced["relief"] = SUNKEN

    def tk_operator(self):
        if self.btn_operator["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = Core.OperatorFrame(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_operator["relief"] = SUNKEN

    def tk_admin(self):
        if self.btn_admin["relief"] != SUNKEN:
            self.working_frame.destroy()
            self.working_frame = AdminFrame(self)
            self.working_frame.grid(row=1, column=0, sticky="nsew")
            self.raise_buttons()
            self.btn_admin["relief"] = SUNKEN

    def raise_buttons(self):
        self.btn_user["relief"] = RAISED
        self.btn_advanced["relief"] = RAISED
        self.btn_operator["relief"] = RAISED
        self.btn_admin["relief"] = RAISED


class AdvancedFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        Label(self, text="Query").grid(row=0, column=0, sticky="w")
        self.varQuery = StringVar()
        Entry(self, textvariable=self.varQuery, width=40).grid(row=0, column=1, sticky="ew")
        Button(self, text="Execute", command=self.query).grid(row=0, column=2, sticky="e")
        self.DataGridView = Core.DataGridView(self)
        self.DataGridView.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.varError = StringVar()
        Label(self, textvariable=self.varError).grid(row=2, column=0, columnspan=3, sticky="w")

    def query(self):
        if self.varQuery.get() == "":
            query = "select name from sqlite_master where type='table' and name not like 'sqlite_%';"
        else:
            query = self.varQuery.get()
        try:
            data = Core.exec_query(query)
        except sqlite3.Error as e:
            self.varError.set(str(e))
        else:
            self.varError.set("Success")
            self.DataGridView.show_data(data)


class AdminFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.ListUsersFrame = ListUsersFrame(self)
        self.ListUsersFrame.grid(row=0, column=0, sticky="nw")


class EditUserFrame(Frame):
    def __init__(self, master=None, user=None):
        Frame.__init__(self, master)
        self.user = user
        self.varUsername = StringVar()
        self.varPassword = StringVar()
        self.varType = IntVar()
        self.varT = StringVar()

        Label(self, text="Korisnicko ime: ").grid(row=0, column=0, sticky="e")
        usr = Entry(self, textvariable=self.varUsername, state=DISABLED)
        usr.grid(row=0, column=1, sticky="ew")
        Label(self, text="Lozinka: ").grid(row=1, column=0, sticky="e")
        Entry(self, textvariable=self.varPassword).grid(row=1, column=1, sticky="ew")
        Label(self, text="Tip: ").grid(row=2, column=0, sticky="e")
        sb = Spinbox(self, textvariable=self.varType, from_=0, to=3, command=lambda: self.varT.set(Core.user_types[self.varType.get()]))
        sb.grid(row=2, column=1, sticky="ew")
        Label(self, textvariable=self.varT).grid(row=3, column=0, columnspan=2, sticky="ew")
        Button(self, text="Azuriraj", command=self.tk_update_user).grid(row=4, column=0, columnspan=2, sticky="ew")
        # if editing existing user or creating new user
        if self.user is not None:
            self.varUsername.set(self.user.username)
            self.varPassword.set(self.user.password)
            self.varType.set(self.user.type)
            self.varT.set(Core.user_types[self.user.type])
            if self.user.type == 3:
                if self.user.username == self.master.master.master.master.user.username:
                    sb["state"] = DISABLED
        else:
            usr["state"] = NORMAL
            self.varType.set(1)
            self.varT.set(Core.user_types[1])

    def tk_update_user(self):
        if self.user is not None:
            new_user_data = Core.User(self.user.username, self.varPassword.get(), self.varType.get())
            if new_user_data.password != self.user.password or new_user_data.type != self.user.type:
                Core.update_user(new_user_data)
                self.master.master.tk_get_users()
                self.master.destroy()
            else:
                messagebox.showinfo("Obavestenje", "Nisu izmenjeni podaci, nece biti izvrseno azuriranje")
        else:
            new_user_data = Core.User(self.varUsername.get(), self.varPassword.get(), self.varType.get())
            if new_user_data.password != "" and new_user_data.username != "":
                try:
                    Core.new_user2(new_user_data)
                except sqlite3.IntegrityError:
                    messagebox.showerror("Greska", "Postoji korisnik sa istim korisnickim imenom")
                else:
                    self.master.master.tk_get_users()
                    self.master.destroy()
            else:
                messagebox.showinfo("Obavestenje", "Nisu izmenjeni podaci, nece biti izvrseno azuriranje")
        pass


class ListUsersFrame(LabelFrame):
    def __init__(self, master=None):
        LabelFrame.__init__(self, master, text="Korisnici", padx=5, pady=5)
        self.users = []
        self.lb_users = Listbox(self)
        self.lb_users.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.lb_users.bind("<Double-Button-1>", self.tk_edit_selected_user)
        Button(self, text="Dodaj", command=self.tk_add_user).grid(row=1, column=0, sticky="ew")
        Button(self, text="Izmeni", command=self.tk_edit_selected_user).grid(row=1, column=1, sticky="ew")
        self.tk_get_users()

    def tk_get_users(self):
        self.lb_users.delete(0, END)
        self.users = Core.get_users()
        for user in self.users:
            self.lb_users.insert(END, user)
        pass

    def tk_edit_selected_user(self, args=None):
        try:
            user = self.users[self.lb_users.curselection()[0]]
        except IndexError:
            messagebox.showwarning("Greska", "Niste izabrali korisnika")
        else:
            toplevel = Toplevel(self)
            EditUserFrame(toplevel, user).pack()
        pass

    def tk_add_user(self):
        toplevel = Toplevel(self)
        EditUserFrame(toplevel).pack()

